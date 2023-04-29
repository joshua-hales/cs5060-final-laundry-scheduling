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
        self.__stats = {}
        self.__steps = 0

    def simulate(self, scheduler, processes: deque[Process]):
        """
        :param scheduler: A scheduler
        :param processes: A queue of processes
        """
        self.__steps = 0
        done = self.__is_complete(processes)
        while not done and self.__steps < self.__rules['window']:
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
                washer.add(scheduler.update(washer.get_process(), washer))

            for dryer in self.__dryers:
                if dryer.is_occupied():
                    dryer.update()
                dryer.add(scheduler.update(dryer.get_process(), dryer))

            # TODO: Update users

            self.__steps += 1
            done = self.__is_complete(processes)

    def log(self):
        # TODO: Log stats
        pass

    def __is_complete(self, queue: deque[Process]):
        # TODO: Check if all processes are complete and all segments are empty
        return False
