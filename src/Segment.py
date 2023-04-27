class Segment:
    def __init__(self, i, name, cycles):
        """
        :param i: A unique identifier for the segment as an int
        :param name: A name for the segment as a string
        :param cycles: A dictionary of cycle durations and their probabilities
        """
        # cycles = {'duration': x:int, 'probability': y:float}
        self.i = i
        self.name = name
        self.__cycles = cycles

    def __eq__(self, other):
        return self.i == other.i and self.name == other.name
