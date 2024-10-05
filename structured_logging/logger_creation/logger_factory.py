from injector import Injector
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.infrastructure.app_module import AppModule
from structured_logging.logger.logger import Logger
from structured_logging.logger_creation.logger_config_builder import LoggerConfigBuilder


def create_logger(logger_config: LoggerConfig) -> Logger:
    injector = Injector(AppModule(logger_config))
    return injector.get(Logger)



if __name__ == '__main__':
    builder = LoggerConfigBuilder()
    config = builder.build()
    logger = create_logger(config)
    logger.log(message="Hello, World!")

