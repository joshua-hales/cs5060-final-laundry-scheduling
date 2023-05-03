from Segment import Segment, Washer, Dryer
from User import User
from Process import Process
from Scheduler import SchedulerFCFS
from collections import deque


class Environment:
    def __init__(self, washers: int, dryers: int, rules: dict[str, int] = None):
        """
        :param washers: The number of washers as a positive int
        :param dryers: The number of dryers as a positive int
        :param rules: A dictionary of rules
        """
        self.__washers = [Washer(i) for i in range(washers)]
        self.__dryers = [Dryer(i) for i in range(dryers)]
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

    def simulate(self, scheduler: SchedulerFCFS, users: deque[User]):
        """
        :param scheduler: A scheduler
        :param users: A queue of users sorted by start time
        """
        self.__steps = 0
        done = self.__is_complete(users)
        while not done:
            done_adding = False
            while not done_adding:
                user = users[0] if users else None
                if user and user.get_start_time() <= self.__steps:
                    for process in user:
                        scheduler.notify(process)
                    users.popleft()
                else:
                    done_adding = True

            for washer in self.__washers:
                if washer.is_occupied():
                    washer.update()
                washer.add([scheduler.update(process, washer) for process in washer])

            for dryer in self.__dryers:
                if dryer.is_occupied():
                    dryer.update()
                dryer.add([scheduler.update(process, dryer) for process in dryer])

            # TODO: Update users

            self.__steps += 1
            done = self.__is_complete(users)

    def log(self, kind: str, process: Process, segment: Segment):
        """
        Logs a process being scheduled or completed
        :param kind: 'scheduled' or 'completed'
        :param process: The process being logged
        :param segment: The segment the process is being logged for
        """
        self.__stats['washers' if isinstance(segment, Washer) else 'dryers'][kind].append((process.get_name(), segment.get_name()))

    def __is_complete(self, users: deque[User]):
        """
        Checks if the simulation is complete.
        A simulation is complete when all processes are complete and all segments are empty.
        The simulation is also complete if the number of steps exceeds the window size.
        :param users: The queue of users
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
        return bool(users)
