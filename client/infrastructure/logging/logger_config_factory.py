from client.infrastructure.settings.settings import Settings, LoggingType
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.logger_creation.logger_config_builder import LoggerConfigBuilder


def create_logger_config(settings: Settings, builder: LoggerConfigBuilder) -> LoggerConfig:
    if settings.logging_type == LoggingType.CONSOLE:
        builder.with_console_sink()
    else :
        builder.with_file_sink(settings.logging_file_path)
    if settings.logging_is_async:
        builder.as_async(settings.logging_async_delay)
    builder.add_environment(settings.environment)
    return builder.build()


