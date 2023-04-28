from Segment import Segment, Washer, Dryer
from User import User
from Process import Process

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

    def simulate(self, scheduler, queue: list[Process]):
        """
        :param scheduler: A scheduler
        :param queue: A queue of processes
        """
        self.__steps = 0
        while self.__steps < self.__rules['window']:
            # TODO: Add scheduling
            # TODO: Create Scheduler class
            self.__steps += 1

    def log(self):
        # TODO: Log stats
        pass

    def __is_complete(self, queue: list[Process]):
        # TODO: Check if all processes are complete and all segments are empty
        return False
