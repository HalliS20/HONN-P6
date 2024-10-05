
from injector import Module, provider
from structured_logging.configuration.logger_config import LoggerConfig


class AppModule(Module):
    def __init__(self, logger_config: LoggerConfig) -> None:
        self.__logger_config = logger_config

    @provider
    def provide_delay(self) -> int:
        return self.__logger_config.async_wait_delay_in_seconds

    @provider
    def provide_config(self) -> LoggerConfig:
        return self.__logger_config


