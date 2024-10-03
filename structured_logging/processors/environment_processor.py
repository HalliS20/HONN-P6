from structured_logging.processors.abstract_processor import AbstractProcessor


class EnvironmentProcessor(AbstractProcessor):
    def __init__(self, environment):
        super().__init__()
        self.environment = environment

    def process(self, data:dict) -> dict:
        data["environment"] = self.environment
        return data
