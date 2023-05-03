import random
import matplotlib.pyplot as plt

from Environment import Environment
from User import User
from Process import Process
from Segment import Segment, Washer, Dryer
from Scheduler import SchedulerFCFS
from collections import deque


random.seed(0)


def report(stats):
    print(stats)
    x, y = zip(*stats.items())
    fig, ax = plt.subplots()
    # TODO: Plot stats
    # TODO: Set labels
    plt.show()

def create_users(users: int, window: int, processes_per_user: int):
    """
    Creates a list of users with processes.
    Processes are assigned a random cycle and start time.
    All processes for a user have the same cycle and start time.
    :param users: The number of users
    :param window: The maximum time a simulation can run
    :param processes_per_user: The number of processes per user (total processes = users * processes_per_user)
    :return: A list of users sorted by start time
    """
    cycles = [cycle.value for cycle in Segment.Cycle]
    users_list = []
    for i in range(users):
        cycle = random.choice(cycles)
        start_time = random.randrange(window - Segment.Cycle.LONG.value)
        processes = [Process(i * processes_per_user + j, start_time, cycle) for j in range(processes_per_user)]
        users_list.append(User(i, processes, start_time))
    users_list.sort(key=lambda user: user.get_start_time())
    return users_list


def main():
    rules = {
        'processes': 3,  # The maximum number of concurrent segments of one type per user
        'removal': 10,  # The minimum occupied idle time before a user can remove another user's process
        'window': 180,  # The global step limit that all tasks must finish within (laundry closes)
    }
    envs = [
        Environment(3, 3),
        Environment(3, 3, rules),
    ]
    for env in envs:
        env.simulate(SchedulerFCFS(env), deque(create_users(3, 180, 2)))
        # TODO: Report logged stats


if __name__ == '__main__':
    main()
