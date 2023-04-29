from enum import Enum
from Process import Process


class Segment:

    class Cycle(Enum):
        SHORT = 30
        MEDIUM = 45
        LONG = 60

    def __init__(self, name: int):
        """
        :param name: A unique identifier for the segment as an int
        """
        self.name = name
        self.__process = None
        # TODO: Remove. Left for reference
        # self.__stats = {
        #     'occupied_idle': [],  # Lists contain tuples of (start, duration)
        #     'occupied_busy': [],
        #     'unoccupied_idle': [],
        # }

    def add(self, process: Process):
        """
        Adds a process to the segment to be run
        :param process: A Process
        """
        self.__process = process

    def update(self):
        """
        Updates the current process for a step
        """
        if self.__process:
            self.__process.update()

    def remove(self):
        """
        Removes the current process from the segment
        :return: The process that was removed
        """
        process = self.__process
        self.__process = None
        return process

    def is_occupied(self):
        """
        :return: True if the segment is occupied, False otherwise
        """
        return self.__process is not None

    def get_process(self):
        """
        :return: The current process
        """
        return self.__process


class Washer(Segment):
    def __init__(self, name: int):
        """
        :param name: A unique identifier for the segment as an int
        """
        super().__init__(name)


class Dryer(Segment):
    def __init__(self, name: int):
        """
        :param name: A unique identifier for the segment as an int
        """
        super().__init__(name)
