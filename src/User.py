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
        self.__complete = False
        self.is_complete()

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
        # Avoid rechecking all processes if already complete
        if not self.__complete:
            for process in self.__processes:
                if not process.is_complete():
                    return False
            self.__complete = True
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

    def __getitem__(self, i: int):
        """
        :param i: The index of the process to return
        :return: The process at the given index
        """
        return self.__processes[i]

    def __len__(self):
        """
        :return: The number of processes the user has
        """
        return len(self.__processes)

    def __str__(self):
        return f'User {self.__name} - {self.__start_time} {self.__elapsed_time} {self.__complete}\n\t{self.__processes}'
