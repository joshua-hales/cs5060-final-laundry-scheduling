from Process import Process


class User:
    def __init__(self, name: int, processes: list[Process], start_time: int):
        self.__name = name
        self.__processes = processes
        self.__start_time = start_time
        self.__elapsed_time = 0

    def update(self):
        self.__elapsed_time += 1

    def is_complete(self):
        for process in self.__processes:
            if not process.is_complete():
                return False
        return True

    # NOTE: May not be necessary
    def get_available_processes(self, num: int, kind: str):
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
