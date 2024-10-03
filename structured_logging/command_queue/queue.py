import threading
import time

from structured_logging.command_queue.command import Command


class Queue:
    # TODO: we also need to inject the async delay time into the constructor
    def __init__(self, async_delay: int) -> None:
        self.__async_delay = async_delay
        self.__queue = []
        self.__thread = threading.Thread(target=self.__process)
        self.__thread.daemon = True
        self.__thread.start()

    def add(self, command: Command):
        self.__queue.append(command)

    def __process(self):
        while True:
            try:
                command = self.__queue.pop(0)
                command.execute()
            except self.__queue == []:
                time.sleep(self.__async_delay)
