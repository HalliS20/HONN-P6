from structured_logging.sinks.I_sink_factory import ISinkFactory
from structured_logging.sinks.file_sink import FileSink
from structured_logging.sinks.i_sink import ISink


class FileSinkFactory(ISinkFactory):
    def __init__(self, file_path: str):
        self.path = file_path

    def create_sink(self) -> ISink:
        return FileSink(self.path)