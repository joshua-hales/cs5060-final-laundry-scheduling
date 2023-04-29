from Process import Process


class User:
    def __init__(self, name: int, processes: list[Process], start_time: int):
        """
        Represents a user that can have processes
        :param name: A unique identifier for the user
        :param processes:  A list of processes
        :param start_time: The arrival time of the user
        """
        self.__name = name
        self.__processes = processes
        self.__start_time = start_time
        self.__elapsed_time = 0

    def update(self):
        """
        Updates the user for a step
        :return:
        """
        self.__elapsed_time += 1

    def is_complete(self):
        """
        :return: True if all processes are complete, False otherwise
        """
        for process in self.__processes:
            if not process.is_complete():
                return False
        return True

    # NOTE: May not be necessary
    def get_available_processes(self, num: int, kind: str):
        """
        Get a list of available processes for a given segment type
        :param num: The maximum number of processes to return
        :param kind: The segment type
        :return: A list of available processes
        """
        available_processes = []
        for process in self.__processes:
            if process.get_remaining_time() > 0:
                available_processes.append(process)
                if len(available_processes) == num:
                    break
        return available_processes

    def get_name(self):
        return self.__name

    def get_start_time(self):
        return self.__start_time

    def get_elapsed_time(self):
        return self.__elapsed_time
