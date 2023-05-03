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
        self.__processes = []
        # TODO: Remove. Left for reference
        # self.__stats = {
        #     'occupied_idle': [],  # Lists contain tuples of (start, duration)
        #     'occupied_busy': [],
        #     'unoccupied_idle': [],
        # }

    def add(self, processes: Process | list[Process]):
        """
        Adds processes to the segment to be run
        :param processes: A Process or list of Processes
        """
        if isinstance(processes, list):
            self.__processes.extend(processes)
        else:
            self.__processes.append(processes)

    def update(self):
        """
        Updates the current processes for a step
        """
        if self.__processes:
            for process in self.__processes:
                process.update()

    def remove(self):
        """
        Removes the current processes from the segment
        :return: A list of processes that was removed
        """
        processes = self.__processes
        self.__processes.clear()
        return processes

    def is_occupied(self):
        """
        :return: True if the segment is occupied, False otherwise
        """
        return bool(self.__processes)

    def get_name(self):
        """
        :return: The name of the segment
        """
        return self.name

    def __getitem__(self, item):
        """
        :param item: The index of the process to return
        :return: The process at the given index
        """
        return self.__processes[item]

    def __len__(self):
        """
        :return: The number of processes in the segment
        """
        return len(self.__processes)


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
