from enum import Enum
from Process import Process


class Segment:

    class Cycle(Enum):
        SHORT = 30
        MEDIUM = 36
        LONG = 45

    def __init__(self, name: int):
        """
        :param name: A unique identifier for the segment as an int
        """
        self.name = name
        self.__processes = []

    def add(self, processes: Process | list[Process]):
        """
        Adds processes to the segment to be run
        :param processes: A Process or list of Processes
        """
        if isinstance(processes, list):
            self.__processes.extend(processes)
        elif isinstance(processes, Process):
            self.__processes.append(processes)

    def update(self):
        """
        Updates the current processes for a step
        """
        if self.__processes:
            for process in self.__processes:
                process.update()

    def remove(self) -> list[Process]:
        """
        Removes the current processes from the segment
        :return: A list of processes that was removed
        """
        processes = self.__processes
        self.__processes = []
        return processes

    def is_occupied(self) -> bool:
        """
        :return: True if the segment is occupied, False otherwise
        """
        return bool(self.__processes)

    def get_name(self) -> int:
        """
        :return: The name of the segment
        """
        return self.name

    def __getitem__(self, i: int) -> Process:
        """
        :param i: The index of the process to return
        :return: The process at the given index
        """
        return self.__processes[i]

    def __len__(self):
        """
        :return: The number of processes in the segment
        """
        return len(self.__processes)

    def __str__(self):
        return f'Segment {self.name} {self.__processes}'


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
