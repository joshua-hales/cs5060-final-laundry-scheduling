class Segment:
    def __init__(self, i, name, cycles=None):
        """
        :param i: A unique identifier for the segment as an int
        :param name: A name for the segment as a string
        :param cycles: A dictionary of cycle durations and their probabilities
        """
        self.i = i
        self.name = name
        self.__cycles = cycles if cycles else {
            'duration': 30,  # The duration of the cycle as a positive int
            'probability': 1,  # The probability of the cycle as a float between 0 and 1
        }
        self.__stats = {
            'occupied_idle': [],  # Lists contain tuples of (start, duration)
            'occupied_busy': [],
            'unoccupied_idle': [],
        }

    def __eq__(self, other):
        return self.i == other.i and self.name == other.name

    def __str__(self):
        return self.name + str(self.i)
