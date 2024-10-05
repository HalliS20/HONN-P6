from structured_logging.command_queue.command import Command
from structured_logging.configuration.logger_config import LoggerConfig

class LoggingCommand(Command):
    def __init__(self, config: LoggerConfig, data: dict):
        self.__config = config
        self.__data = data

    def execute(self):
        processed = self.__config.processor.handle(self.__data)
        self.__config.sink.sink_data(processed)
