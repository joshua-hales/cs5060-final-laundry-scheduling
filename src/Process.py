class Process:
    # TODO: Add support for multiple segments with different cycle times
    def __init__(self, name: int, start_time: int, cycle_time: int):
        """
        Represents a process that can be run on a segment
        :param name: A unique identifier for the process
        :param start_time: The arrival time of the process
        :param cycle_time: The time it takes to complete the process
        """
        self.__name = name
        self.__start_time = start_time
        self.__cycle_time = cycle_time
        self.__elapsed_time = 0

    def update(self):
        """
        Updates the current process for a step
        """
        self.__elapsed_time += 1

    def is_complete(self):
        """
        :return: True if the process is complete, False otherwise
        """
        return self.__elapsed_time >= self.__cycle_time

    def get_name(self):
        return self.__name

    def get_start_time(self):
        return self.__start_time

    def get_remaining_time(self):
        """
        :return: The remaining time for the process to complete
        """
        return self.__cycle_time - self.__elapsed_time

    def get_elapsed_time(self):
        return self.__elapsed_time
