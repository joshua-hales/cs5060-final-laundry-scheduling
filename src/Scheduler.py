from Process import Process
from Segment import Segment
from collections import deque


class SchedulerFCFS:
    def __init__(self, logger):
        """
        A first come, first served scheduler
        :param logger: Object that implements a log method
        """
        self.__logger = logger
        self.__queue = deque()
        self.__context_switches = 0

    def update(self, process: Process | None, segment: Segment):
        """
        Updates the current process for a step
        """
        # TODO: Double check this logic
        if not process:
            next_process = self.__queue.popleft() if self.__queue else None
        else:
            if process.is_complete():
                self.__logger.log('completed', process, segment)
                self.__context_switches += 1
                next_process = self.__queue.popleft() if self.__queue else None
            else:
                next_process = process

        if next_process and next_process.get_elapsed_time() == 0:
            self.__logger.log('scheduled', next_process, segment)
            self.__context_switches += 1
        return next_process

    def notify(self, process: Process):
        """
        Adds a process to the ready queue
        :param process: A Process
        """
        self.__queue.append(process)

    def get_context_switches(self):
        """
        :return: The number of context switches that have occurred
        """
        return self.__context_switches

    def __str__(self):
        return f'SchedulerFCFS\n\t{self.__queue}'
