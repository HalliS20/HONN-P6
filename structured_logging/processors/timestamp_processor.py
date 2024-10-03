import time

from structured_logging.processors.abstract_processor import AbstractProcessor


class TimestampProcessor(AbstractProcessor):

    def process(self, data : dict):
        data["timestamp"] = time.time()
        return data