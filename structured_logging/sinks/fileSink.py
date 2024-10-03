from structured_logging.sinks.i_sink import ISink
import json

class fileSink(ISink):
    def __init__(self, file_path: str) -> None:
        self.path = file_path

    def sink_data(self, data: dict):
        json_data = json.dumps(data, indent=4)

        self.file = open(self.path, 'a')
        self.file.write(json_data + '\n')
        self.file.close()