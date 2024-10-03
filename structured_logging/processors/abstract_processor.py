from abc import abstractmethod

from structured_logging.processors.i_processor import IProcessor


class AbstractProcessor(IProcessor):
    def __init__(self):
        self._next_processor = None

    def set_next(self, processor: IProcessor):
        self._next_processor = processor
        return processor

    @abstractmethod
    def process(self, data: dict) -> dict:
        pass

    def handle(self, data: dict) -> dict:
        processed_data = self.process(data)
        if self._next_processor:
            return self._next_processor.handle(processed_data)
        return processed_data
