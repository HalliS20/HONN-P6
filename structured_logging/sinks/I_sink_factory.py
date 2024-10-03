from abc import ABC, abstractmethod

class ISinkFactory(ABC):
    @abstractmethod
    def create_sink(self):
        pass