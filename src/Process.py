class Process:
    # TODO: Add support for multiple segments with different cycle times
    def __init__(self, name: int, start_time: int, cycle_time: int, segments: int = 1):
        """
        Represents a process that can be run on a segment
        :param name: A unique identifier for the process
        :param start_time: The arrival time of the process
        :param cycle_time: The time it takes to complete the process
        :param segments: The number of segments the process requires
        """
        self.__name = name
        self.__start_time = start_time
        self.__cycle_time = cycle_time
        self.__elapsed_time = 0
        self.__segments = segments - 1
        self.__segments_complete = 0

    def update(self, segment: bool = False):
        """
        Updates the process for a step
        :param segment: True if the process is being moved to a new segment, False otherwise
        """
        self.__elapsed_time += 1
        if segment:
            self.__segments_complete += 1
            self.__elapsed_time = 0

    def is_complete(self):
        """
        :return: True if the process is complete, False otherwise
        """
        return self.__segments_complete >= self.__segments

    def is_segment_complete(self):
        """
        :return: True if the process is complete for the current segment, False otherwise
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

    def get_segments(self):
        return self.__segments

    def __str__(self):
        return f"Process {self.__name} - {self.__start_time} {self.__elapsed_time}/{self.__cycle_time}"
