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
    envs = [
        Environment(3, 3, 3),
        Environment(3, 3, 3),
        Environment(3, 3, 3),
    ]
    for env in envs:
        report(env.run(10))


if __name__ == '__main__':
    main()
