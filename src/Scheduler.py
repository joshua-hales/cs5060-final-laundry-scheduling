from Process import Process
from Segment import Segment
from collections import deque


class SchedulerFCFS:
    def __init__(self, logger, stages: int):
        """
        A first come, first served scheduler
        :param logger: Object that implements a log method
        :param stages: The number of segments a process will go through
        """
        self.__logger = logger
        self.__queues = [deque() for _ in range(stages)]
        self.__context_switches = 0

    def update(self, process: Process | None, segment: Segment, stage: int):
        """
        Updates the current process for a step
        :param process: The current process
        :param segment: The current segment
        :param stage: The current stage
        """
        if not process:
            next_process = self.__queues[stage].popleft() if self.__queues[stage] else None
        elif process.is_segment_complete():
            self.__logger.log('completed', process, segment)
            self.__context_switches += 1
            next_process = self.__queues[stage].popleft() if self.__queues[stage] else None
            if not process.is_complete():
                process.update(segment=True)
                self.notify(process, stage+1)
        else:
            next_process = process

        if next_process and next_process.get_elapsed_time() == 0:
            self.__logger.log('scheduled', next_process, segment)
            self.__context_switches += 1
        return next_process

    def notify(self, process: Process, stage: int = 0):
        """
        Adds a process to the ready queue
        :param process: A Process
        :param stage: The stage to add the process to
        """
        self.__queues[stage].append(process)

    def get_context_switches(self):
        """
        :return: The number of context switches that have occurred
        """
        return self.__context_switches

    def __str__(self):
        return f'SchedulerFCFS\n\t{self.__queues}'
