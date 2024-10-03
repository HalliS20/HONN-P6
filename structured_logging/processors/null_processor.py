from structured_logging.processors.abstract_processor import AbstractProcessor


class NullProcessor(AbstractProcessor):
    def process(self, data: dict) -> dict:
        return data
