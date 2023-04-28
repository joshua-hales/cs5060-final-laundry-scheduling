from Segment import Segment
from User import User

class Environment:
    def __init__(self, washers, dryers, users, rules=None):
        """
        :param washers: The number of washers as a positive int
        :param dryers: The number of dryers as a positive int
        :param users: The number of users as a positive int
        :param rules: A dictionary of rules
        """
        self.__washers = [Segment(i, 'Washer', {'duration': 30, 'probability': 1}) for i in range(washers)]
        self.__dryers = [Segment(i, 'Dryer', {'duration': 45, 'probability': 1}) for i in range(dryers)]
        self.__users = [User(i) for i in range(users)]
        self.__rules = rules if rules else {
            'loads': 3,  # The maximum number of concurrent segments of one type per user
            'removal': 10,  # The minimum occupied idle time before a user can remove another user's load
            'window': 180,  # The global step limit that all tasks must finish within (laundry closes)
        }
        self.__stats = {}

    def run(self, steps):
        """
        :param steps: The number of steps to run as a positive int. Must be less than the window
        :return: A dictionary of statistics
        """
        for step in range(steps):
            break
        return self.__stats

    def scheduling(self):
        """
        :return: A dictionary of statistics
        """

        return self.__stats

    def stopping(self):
        """
        :return: A dictionary of statistics
        """
        return self.__stats

    def game(self):
        """
        :return: A dictionary of statistics
        """
        return self.__stats
