from injector import Module, provider, Binder, singleton

from client.infrastructure.logging.client_logger import ClientLogger
from client.infrastructure.logging.i_logger import ILogger
from client.infrastructure.settings.settings import Settings
from client.infrastructure.logging.logger_config_factory import create_logger_config
from client.repositories.order_repository import OrderRepository
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.logger_creation.logger_config_builder import LoggerConfigBuilder


class AppModule(Module):
    def __init__(self, settings: Settings) -> None:
        self.__settings = settings
        self.__builder = LoggerConfigBuilder()
        self.__config = create_logger_config(self.__settings,self.__builder)

    @provider
    def provide_settings(self) -> Settings:
        return self.__settings

    @provider
    def provide_config(self) -> LoggerConfig:
        return self.__config

    def configure(self, binder: Binder) -> None:
        binder.bind(ILogger, to=ClientLogger, scope=singleton)