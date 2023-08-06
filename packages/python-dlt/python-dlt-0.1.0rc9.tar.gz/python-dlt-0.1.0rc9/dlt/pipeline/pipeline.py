
from contextlib import contextmanager
from copy import deepcopy
import yaml
from collections import abc
from dataclasses import asdict as dtc_asdict
import tempfile
import os.path
from typing import Any, Iterator, List, Sequence, Tuple
from prometheus_client import REGISTRY

from dlt.common import json
from dlt.common.runners import pool_runner as runner, TRunArgs, TRunMetrics
from dlt.common.configuration import BasicConfiguration, make_configuration
from dlt.common.file_storage import FileStorage
from dlt.common.logger import process_internal_exception
from dlt.common.schema import Schema, normalize_schema_name
from dlt.common.typing import DictStrAny, StrAny
from dlt.common.utils import uniq_id, is_interactive
from dlt.common.sources import DLT_METADATA_FIELD, TItem, with_table_name

from dlt.extractors.extractor_storage import ExtractorStorageBase
from dlt.loaders.client_base import SqlClientBase, SqlJobClientBase
from dlt.unpacker.configuration import configuration as unpacker_configuration
from dlt.loaders.configuration import configuration as loader_configuration
from dlt.unpacker import unpacker
from dlt.loaders import loader
from dlt.pipeline.exceptions import InvalidPipelineContextException, MissingDependencyException, NoPipelineException, PipelineStepFailed, CannotRestorePipelineException, SqlClientNotAvailable
from dlt.pipeline.typing import PipelineCredentials


class Pipeline:
    def __init__(self, pipeline_name: str, log_level: str = "INFO") -> None:
        self.pipeline_name = pipeline_name
        self.default_schema_name: str = None
        self.root_path: str = None
        self.root_storage: FileStorage = None
        self.credentials: PipelineCredentials = None
        self.extractor_storage: ExtractorStorageBase = None
        self.state: DictStrAny = {}

        # addresses of pipeline components to be verified before they are run
        self._unpacker_instance: int = None
        self._loader_instance: int = None

        # patch config and initialize pipeline
        C = make_configuration(BasicConfiguration, BasicConfiguration, initial_values={
            "NAME": pipeline_name,
            "LOG_LEVEL": log_level
        })
        runner.initialize_runner(C, TRunArgs(True, 0))

    def create_pipeline(self, credentials: PipelineCredentials, working_dir: str = None, schema: Schema = None) -> None:
        # initialize root storage
        if not working_dir:
            working_dir = tempfile.mkdtemp()
        self.root_storage = FileStorage(working_dir, makedirs=True)

        # check if directory contains restorable pipeline
        try:
            self._restore_state()
            # wipe out the old pipeline
            self.root_storage.delete_folder("", recursively=True)
            self.root_storage.create_folder("")
        except FileNotFoundError:
            pass

        self.root_path = self.root_storage.storage_path
        self.credentials = credentials
        self._load_modules()
        self.extractor_storage = ExtractorStorageBase("1.0.0", True, FileStorage(os.path.join(self.root_path, "extractor"), makedirs=True), unpacker.unpack_storage)
        # create new schema if no default supplied
        if schema is None:
            schema = Schema(normalize_schema_name(self.pipeline_name))
        # persist schema with the pipeline
        self.set_default_schema(schema)
        # initialize empty state
        with self._managed_state():
            self.state = {
                "default_schema_name": self.default_schema_name,
                "pipeline_name": self.pipeline_name,
                # TODO: must come from resolved configuration
                "loader_client_type": credentials.CLIENT_TYPE,
                # TODO: must take schema prefix from resolved configuration
                "loader_schema_prefix": credentials.schema_prefix
            }

    def restore_pipeline(self, credentials: PipelineCredentials, working_dir: str) -> None:
        try:
            # do not create extractor dir - it must exist
            self.root_storage = FileStorage(working_dir, makedirs=False)
            # restore state
            try:
                self._restore_state()
            except FileNotFoundError:
                raise CannotRestorePipelineException(f"Cannot find a valid pipeline in {working_dir}")
            restored_name = self.state["pipeline_name"]
            if self.pipeline_name != restored_name:
                raise CannotRestorePipelineException(f"Expected pipeline {self.pipeline_name}, found {restored_name} pipeline instead")
            self.default_schema_name = self.state["default_schema_name"]
            credentials.schema_prefix = self.state["loader_schema_prefix"]
            self.root_path = self.root_storage.storage_path
            self.credentials = credentials
            self._load_modules()
            # schema must exist
            try:
                self.get_default_schema()
            except (FileNotFoundError):
                raise CannotRestorePipelineException(f"Default schema with name {self.default_schema_name} not found")
            self.extractor_storage = ExtractorStorageBase("1.0.0", True, FileStorage(os.path.join(self.root_path, "extractor"), makedirs=False), unpacker.unpack_storage)
        except CannotRestorePipelineException:
            pass

    def extract(self, items: Iterator[TItem], schema_name: str = None, table_name: str = None) -> None:
        # check if iterator or iterable is supported
        # if isinstance(items, str) or isinstance(items, dict) or not
        # TODO: check if schema exists
        with self._managed_state():
            default_table_name = table_name or self.pipeline_name
            # TODO: this is not very effective - we consume iterator right away, better implementation needed where we stream iterator to files directly
            all_items: List[DictStrAny] = []
            for item in items:
                # dispatch items by type
                if callable(item):
                    item = item()
                if isinstance(item, dict):
                    all_items.append(item)
                elif isinstance(item, abc.Sequence):
                    all_items.extend(item)

            try:
                self._extract_iterator(default_table_name, all_items)
            except Exception:
                raise PipelineStepFailed("extract", self.last_run_exception, runner.LAST_RUN_METRICS)

    def unpack(self, workers: int = 1, max_events_in_chunk: int = 100000) -> None:
        if is_interactive() and workers > 1:
            raise NotImplementedError("Do not use workers in interactive mode ie. in notebook")
        self._verify_unpacker_instance()
        # set runtime parameters
        unpacker.CONFIG.MAX_PARALLELISM = workers
        unpacker.CONFIG.MAX_EVENTS_IN_CHUNK = max_events_in_chunk
        # switch to thread pool for single worker
        unpacker.CONFIG.POOL_TYPE = "thread" if workers == 1 else "process"
        runner.run_pool(unpacker.CONFIG, unpacker.unpack)
        if runner.LAST_RUN_METRICS.has_failed:
            raise PipelineStepFailed("unpack", self.last_run_exception, runner.LAST_RUN_METRICS)

    def load(self, max_parallel_loads: int = 20) -> None:
        self._verify_loader_instance()
        loader.CONFIG.MAX_PARALLELISM = loader.CONFIG.MAX_PARALLEL_LOADS = max_parallel_loads
        runner.run_pool(loader.CONFIG, loader.load)
        if runner.LAST_RUN_METRICS.has_failed:
            raise PipelineStepFailed("load", self.last_run_exception, runner.LAST_RUN_METRICS)

    def flush(self) -> None:
        self.unpack()
        self.load()

    @property
    def working_dir(self) -> str:
        return os.path.abspath(self.root_path)

    @property
    def last_run_exception(self) -> BaseException:
        return runner.LAST_RUN_EXCEPTION

    def list_extracted_loads(self) -> Sequence[str]:
        self._verify_loader_instance()
        return unpacker.unpack_storage.list_files_to_unpack_sorted()

    def list_unpacked_loads(self) -> Sequence[str]:
        self._verify_loader_instance()
        return loader.load_storage.list_loads()

    def list_completed_loads(self) -> Sequence[str]:
        self._verify_loader_instance()
        return loader.load_storage.list_completed_loads()

    def list_failed_jobs(self, load_id: str) -> Sequence[Tuple[str, str]]:
        self._verify_loader_instance()
        failed_jobs: List[Tuple[str, str]] = []
        for file in loader.load_storage.list_archived_failed_jobs(load_id):
            if not file.endswith(".exception"):
                try:
                    failed_message = loader.load_storage.storage.load(file + ".exception")
                except FileNotFoundError:
                    failed_message = None
                failed_jobs.append((file, failed_message))
        return failed_jobs

    def get_default_schema(self) -> Schema:
        self._verify_unpacker_instance()
        return unpacker.schema_storage.load_store_schema(self.default_schema_name)

    def set_default_schema(self, new_schema: Schema) -> None:
        if self.default_schema_name:
            # delete old schema
            unpacker.schema_storage.remove_store_schema(self.default_schema_name)
            self.default_schema_name = None
        # save new schema
        unpacker.schema_storage.save_store_schema(new_schema)
        self.default_schema_name = new_schema.schema_name
        with self._managed_state():
            self.state["default_schema_name"] = self.default_schema_name

    def add_schema(self, aux_schema: Schema) -> None:
        unpacker.schema_storage.save_store_schema(aux_schema)

    def get_schema(self, name: str) -> Schema:
        return unpacker.schema_storage.load_store_schema(name)

    def remove_schema(self, name: str) -> None:
        unpacker.schema_storage.remove_store_schema(name)

    def sync_schema(self) -> None:
        self._verify_loader_instance()
        schema = unpacker.schema_storage.load_store_schema(self.default_schema_name)
        with loader.make_client(schema) as client:
            client.initialize_storage()
            client.update_storage_schema()

    def sql_client(self) -> SqlClientBase[Any]:
        self._verify_loader_instance()
        schema = unpacker.schema_storage.load_store_schema(self.default_schema_name)
        with loader.make_client(schema) as c:
            if isinstance(c, SqlJobClientBase):
                return c.sql_client
            else:
                raise SqlClientNotAvailable(loader.CONFIG.CLIENT_TYPE)

    def _configure_unpack(self) -> None:
        # create unpacker config
        unpacker_initial = {
            "UNPACKING_VOLUME_PATH": os.path.join(self.root_path, "unpacking"),
            "SCHEMA_VOLUME_PATH": os.path.join(self.root_path, "schemas"),
            "WRITER_TYPE": loader.supported_writer(),
            "ADD_EVENT_JSON": False
        }
        unpacker_initial.update(self._configure_runner())
        C = unpacker_configuration(initial_values=unpacker_initial)
        unpacker.configure(C, REGISTRY)
        self._unpacker_instance = id(unpacker.CONFIG)

    def _configure_load(self) -> None:
        # use credentials to populate loader config, it includes also client type
        loader_initial = dtc_asdict(self.credentials)
        loader_initial.update(self._configure_runner())
        loader_initial["DELETE_COMPLETED_JOBS"] = True
        C = loader_configuration(initial_values=loader_initial)
        try:
            loader.configure(C, REGISTRY, is_storage_owner=True)
        except ImportError:
            raise MissingDependencyException(
                f"{self.credentials.CLIENT_TYPE} loader",
                [f"python-dlt[{self.credentials.CLIENT_TYPE}]"],
                "Dependencies for specific loaders are available as extras of python-dlt"
            )
        self._loader_instance = id(loader.CONFIG)

    # def _only_active(f: TFun) -> TFun:
    #     def _wrapper(self) -> Any

    def _verify_loader_instance(self) -> None:
        if self._loader_instance is None:
            raise NoPipelineException()
        if self._loader_instance != id(loader.CONFIG):
            # TODO: consider restoring pipeline from current work dir instead
            raise InvalidPipelineContextException()

    def _verify_unpacker_instance(self) -> None:
        if self._loader_instance is None:
            raise NoPipelineException()
        if self._unpacker_instance != id(unpacker.CONFIG):
            # TODO: consider restoring pipeline from current work dir instead
            raise InvalidPipelineContextException()

    def _configure_runner(self) -> StrAny:
        return {
            "NAME": self.pipeline_name,
            "EXIT_ON_EXCEPTION": True,
            "LOADING_VOLUME_PATH": os.path.join(self.root_path, "loading")
        }

    def _load_modules(self) -> None:
        # configure loader
        self._configure_load()
        # configure unpacker
        self._configure_unpack()

    def _extract_iterator(self, default_table_name: str, items: Sequence[DictStrAny]) -> None:
        try:
            for idx, i in enumerate(items):
                if not isinstance(i, dict):
                    # TODO: convert non dict types into dict
                    items[idx] = i = {"v": i}
                if DLT_METADATA_FIELD not in i or i.get(DLT_METADATA_FIELD, None) is None:
                    # set default table name
                    with_table_name(i, default_table_name)

            load_id = uniq_id()
            self.extractor_storage.save_json(f"{load_id}.json", items)
            self.extractor_storage.commit_events(
                self.default_schema_name,
                self.extractor_storage.storage._make_path(f"{load_id}.json"),
                default_table_name,
                len(items),
                load_id
            )

            runner.LAST_RUN_METRICS = TRunMetrics(was_idle=False, has_failed=False, pending_items=0)
        except Exception as ex:
            process_internal_exception("extracting iterator failed")
            runner.LAST_RUN_METRICS = TRunMetrics(was_idle=False, has_failed=True, pending_items=0)
            runner.LAST_RUN_EXCEPTION = ex
            raise

    @contextmanager
    def _managed_state(self) -> Iterator[None]:
        backup_state = deepcopy(self.state)
        try:
            yield
        except Exception:
            # restore old state
            self.state.clear()
            self.state.update(backup_state)
            raise
        else:
            # persist old state
            self.root_storage.save("state.json", json.dumps(self.state))

    def _restore_state(self) -> None:
        self.state.clear()
        restored_state: DictStrAny = json.loads(self.root_storage.load("state.json"))
        self.state.update(restored_state)

    @staticmethod
    def save_schema_to_file(file_name: str, schema: Schema, remove_defaults: bool = True) -> None:
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(schema.as_yaml(remove_defaults=remove_defaults))

    @staticmethod
    def load_schema_from_file(file_name: str) -> Schema:
        with open(file_name, "r", encoding="utf-8") as f:
            schema_dict: DictStrAny = yaml.safe_load(f)
        return Schema.from_dict(schema_dict)
