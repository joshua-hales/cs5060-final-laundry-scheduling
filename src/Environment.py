from Segment import Segment
from User import User

class Environment:
    def __init__(self, washers, dryers, users):
        """
        :param washers: The number of washers as a positive int
        :param dryers: The number of dryers as a positive int
        :param users: The number of users as a positive int
        """
        self.__washers = [Segment(i, 'Washer', {'duration': 30, 'probability': 1}) for i in range(washers)]
        self.__dryers = [Segment(i, 'Dryer', {'duration': 45, 'probability': 1}) for i in range(dryers)]
        self.__users = [User(i) for i in range(users)]
        self.__stats = {}

    def run(self, steps):
        """
        :param steps: The number of steps to run as a positive int
        :return: A dictionary of statistics
        """
        for step in range(steps):
            break
        return self.__stats
