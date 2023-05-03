from Segment import Segment, Washer, Dryer
from User import User
from Process import Process
from Scheduler import SchedulerFCFS
from collections import deque


class Environment:
    def __init__(self, washers: int, dryers: int, users: int, rules: dict[str, int] = None):
        """
        :param washers: The number of washers as a positive int
        :param dryers: The number of dryers as a positive int
        :param users: The number of users as a positive int
        :param rules: A dictionary of rules
        """
        self.__washers = [Washer(i) for i in range(washers)]
        self.__dryers = [Dryer(i) for i in range(dryers)]
        self.__users = [User(i, [], 0) for i in range(users)]  # TODO: Add processes to users
        self.__rules = rules
        self.__stats = {
            'washers': {
                'scheduled': [],  # Lists contain tuples of (process.name, segment.name)
                'completed': [],
            },
            'dryers': {
                'scheduled': [],
                'completed': [],
            },
        }
        self.__steps = 0

    def simulate(self, scheduler: SchedulerFCFS, processes: deque[Process]):
        """
        :param scheduler: A scheduler
        :param processes: A queue of processes
        """
        self.__steps = 0
        done = self.__is_complete(processes)
        while not done:
            done_adding = False
            while not done_adding:
                process = processes[0] if processes else None
                if process and process.get_start_time() <= self.__steps:
                    scheduler.notify(process)
                    processes.popleft()
                else:
                    done_adding = True

            for washer in self.__washers:
                if washer.is_occupied():
                    washer.update()
                washer.add([scheduler.update(washer[i], washer) for i in range(len(washer))])

            for dryer in self.__dryers:
                if dryer.is_occupied():
                    dryer.update()
                dryer.add([scheduler.update(dryer[i], dryer) for i in range(len(dryer))])

            # TODO: Update users

            self.__steps += 1
            done = self.__is_complete(processes)

    def log(self, kind: str, process: Process, segment: Segment):
        """
        Logs a process being scheduled or completed
        :param kind: 'scheduled' or 'completed'
        :param process: The process being logged
        :param segment: The segment the process is being logged for
        """
        self.__stats['washers' if isinstance(segment, Washer) else 'dryers'][kind].append((process.get_name(), segment.get_name()))

    def __is_complete(self, processes: deque[Process]):
        """
        Checks if the simulation is complete.
        A simulation is complete when all processes are complete and all segments are empty.
        The simulation is also complete if the number of steps exceeds the window size.
        :param processes: The queue of processes
        :return: True if the simulation is complete, False otherwise
        """
        if self.__steps >= self.__rules['window']:
            return True
        for washer in self.__washers:
            if washer.is_occupied():
                return False
        for dryer in self.__dryers:
            if dryer.is_occupied():
                return False
        return len(processes) == 0
