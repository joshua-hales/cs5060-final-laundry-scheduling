import random
import matplotlib.pyplot as plt

from Environment import Environment
from User import User
from Process import Process
from Segment import Segment, Washer, Dryer
from Scheduler import SchedulerFCFS
from collections import deque


random.seed(0)


def report(stats: dict, x_label: str, y_label: str, title: str):
    fig, ax = plt.subplots(constrained_layout=True)
    ax.grid()
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    data = {segment: {'x': [], 'y': []} for segment in stats}
    for segment, events in stats.items():
        _, data[segment]['x'], data[segment]['y'] = zip(*events['scheduled'])
    for segment, events in data.items():
        ax.scatter(events['x'], events['y'], label=segment)
    ax.legend()
    plt.show()
    plt.close()

def create_users(users: int, window: int, processes_per_user: int) -> list[User]:
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
        start_time = random.randrange(window - 2*Segment.Cycle.LONG.value)  # User won't try to start a process within 2 cycles of the end
        processes = [Process(i * processes_per_user + j, start_time, cycle, 2) for j in range(processes_per_user)]
        users_list.append(User(i, processes, start_time))
    users_list.sort(key=lambda user: user.get_start_time())
    return users_list


def main():
    rules = {
        'processes': 3,  # The maximum number of concurrent segments of one type per user
        'removal': 10,  # The minimum occupied idle time before a user can remove another user's process
        'window': 12*60,  # The global step limit that all tasks must finish within (laundry closes)
    }
    NUM_USERS = 50
    PROCESSES_PER_USER = 2
    envs = [
        Environment(6, 8),  # Don't enforce window
        Environment(6, 8, rules),  # Enforce window
        Environment(6, 6, rules),
        Environment(8, 6, rules),
    ]
    for env in envs:
        env.simulate(SchedulerFCFS(env, 2), deque(create_users(NUM_USERS, rules['window'], PROCESSES_PER_USER)))
        report(env.get_stats(), 'Step Time', 'Wait Time', 'Wait Time of Processes')


if __name__ == '__main__':
    main()
