class User:
    def __init__(self, i):
        self.i = i
        self.complete = False
        self.__return_time = 0

    def __eq__(self, other):
        return self.i == other.i
