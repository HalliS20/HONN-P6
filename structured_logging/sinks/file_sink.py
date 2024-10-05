from structured_logging.sinks.i_sink import ISink
import json

class FileSink(ISink):
    def __init__(self, file_path: str) -> None:
        self.path = file_path

    def sink_data(self, data: dict):
        json_data = json.dumps(data, indent=4)

        self.file = open(self.path, 'a')
        self.file.write(json_data + '\n')
        self.file.close()



if __name__ == '__main__':
    FileSink('test.json').sink_data({'test': 'test'})
