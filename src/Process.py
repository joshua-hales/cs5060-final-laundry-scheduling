class Process:
    # TODO: Add support for multiple segments with different cycle times
    def __init__(self, name: int, start_time: int, cycle_time: int):
        self.__name = name
        self.__start_time = start_time
        self.__cycle_time = cycle_time
        self.__elapsed_time = 0

    def update(self):
        self.__elapsed_time += 1

    def is_complete(self):
        return self.__elapsed_time >= self.__cycle_time

    def get_name(self):
        return self.__name

    def get_start_time(self):
        return self.__start_time

    def get_remaining_time(self):
        return self.__cycle_time - self.__elapsed_time
