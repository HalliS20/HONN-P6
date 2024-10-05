from structured_logging.configuration.environment import Environment
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.processors.environment_processor import EnvironmentProcessor
from structured_logging.processors.i_processor import IProcessor
from structured_logging.processors.null_processor import NullProcessor
from structured_logging.sinks.console_sink import ConsoleSink
from structured_logging.sinks.file_sink import FileSink
from structured_logging.sinks.i_sink import ISink


class LoggerConfigBuilder:
    def __init__(self):
        self._sink = ConsoleSink()
        self._path = None
        self._processor = NullProcessor()
        self._wait_delay_in_seconds = 0
        self._is_async = False


    def with_custom_sink(self, sink: ISink) -> 'LoggerConfigBuilder':
        self._sink = sink
        return self

    def with_file_sink(self, file_path: str) -> 'LoggerConfigBuilder':
        self._sink = FileSink(file_path)
        return self

    def with_console_sink(self) -> 'LoggerConfigBuilder':
        self._sink = ConsoleSink()
        return self

    def as_async(self, wait_delay_in_seconds: int) -> 'LoggerConfigBuilder':
        self._wait_delay_in_seconds = wait_delay_in_seconds
        self._is_async = True
        return self

    def add_environment(self, environment: Environment) -> 'LoggerConfigBuilder':
        env_proc = EnvironmentProcessor(environment)
        self.add_processor(env_proc)
        return self

    def add_processor(self, processor: IProcessor) -> 'LoggerConfigBuilder':
        self._processor.set_next(processor)
        return self

    def _clear(self):
        self._sink = None
        self._path = None
        self._processors = []
        self._environment = None
        self._wait_delay_in_seconds = 0
        self._is_async = False


    def build(self) -> LoggerConfig:
        config = LoggerConfig()
        config.sink = self._sink
        config.processor = self._processor
        config.is_async = self._is_async
        config.async_wait_delay_in_seconds = self._wait_delay_in_seconds
        self._clear()
        return config
