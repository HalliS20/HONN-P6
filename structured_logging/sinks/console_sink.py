from structured_logging.sinks.i_sink import ISink
from json import dumps

class ConsoleSink(ISink):
    def sink_data(self, data: dict):
        dumped = dumps(data, indent=4)
        print(dumped)


if __name__ == '__main__':
    ConsoleSink().sink_data({'test': 'test', 'test2': 'test2'})