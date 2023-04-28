import random
import matplotlib.pyplot as plt

from Environment import Environment


random.seed(0)


def report(stats):
    print(stats)
    x, y = zip(*stats.items())
    fig, ax = plt.subplots()
    # TODO: Plot stats
    # TODO: Set labels
    plt.show()


def main():
    rules = {
        'processes': 3,  # The maximum number of concurrent segments of one type per user
        'removal': 10,  # The minimum occupied idle time before a user can remove another user's process
        'window': 180,  # The global step limit that all tasks must finish within (laundry closes)
    }
    envs = [
        Environment(3, 3, 3),
        Environment(3, 3, 3),
        Environment(3, 3, 3),
    ]
    for env in envs:
        # TODO: Run simulation
        # TODO: Report logged stats
        pass


if __name__ == '__main__':
    main()
