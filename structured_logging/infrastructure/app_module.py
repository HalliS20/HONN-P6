
from injector import Module, Binder, provider
from structured_logging.command_queue.queue import Queue
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.logger.logger import Logger


class AppModule(Module):
    def __init__(self, logger_config: LoggerConfig) -> None:
        self.__logger_config = logger_config

    @provider
    def provide_delay(self) -> int:
        return self.__logger_config.async_wait_delay_in_seconds

    @provider
    def provide_config(self) -> LoggerConfig:
        return self.__logger_config


    def configure(self, binder: Binder) -> None:

        binder.bind(Logger, to=Logger)
        binder.bind(Queue, to=Queue)


