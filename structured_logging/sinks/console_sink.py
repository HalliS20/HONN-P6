from structured_logging.sinks.i_sink import ISink
from json import dumps
import sys

class ConsoleSink(ISink):
    def sink_data(self, data: dict):
        print(dumps(data, indent=4))
        sys.stdout.flush()


if __name__ == '__main__':
    ConsoleSink().sink_data({'test': 'test'})