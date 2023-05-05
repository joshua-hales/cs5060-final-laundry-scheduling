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

    def is_complete(self) -> bool:
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

    def get_name(self) -> int:
        return self.__name

    def get_start_time(self) -> int:
        return self.__start_time

    def get_elapsed_time(self) -> int:
        return self.__elapsed_time

    def __getitem__(self, i: int) -> Process:
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
