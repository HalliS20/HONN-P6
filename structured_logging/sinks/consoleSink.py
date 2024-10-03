from structured_logging.sinks.i_sink import ISink
from json import dumps
import sys

class consoleSink(ISink):
    def sink_data(self, data: dict):
        print(dumps(data, indent=4))
        sys.stdout.flush()