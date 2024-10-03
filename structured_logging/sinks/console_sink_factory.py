from structured_logging.sinks.I_sink_factory import ISinkFactory
from structured_logging.sinks.console_sink import ConsoleSink
from structured_logging.sinks.i_sink import ISink


class ConsoleSinkFactory(ISinkFactory):
    def create_sink(self) -> ISink:
        return ConsoleSink()
