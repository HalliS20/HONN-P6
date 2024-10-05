from injector import inject

from client.infrastructure.logging.i_logger import ILogger
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.logger_creation.logger_factory import create_logger


class ClientLogger(ILogger):
    @inject
    def __init__(self, config:LoggerConfig) -> None:
        self.__logger = create_logger(config)

    def error(self, message: str, exception: Exception = None):
        data = {"error": message, "exception": exception}
        self.__logger.log(**data)

    def warning(self, message: str, exception: Exception = None):
        data = {"warning": message, "exception": exception}
        self.__logger.log(**data)

    def info(self, message: str):
        data = {"info": message}
        self.__logger.log(**data)

