---
geometry: margin=1in, letterpaper
pagestyle: empty
---

# Self-Service Laundry Scheduling

This project aims to analyze factors on performance in a self-service laundry.
There are three main components to this project:
the effect of rules on performance for FCFS-like scheduling,
using a stopping algorithm to find when a user should choose to do laundry,
and the effect of user strategies on performance.
They are described in more detail below as Scheduling, Stopping, and Game Theory respectively.


## Definitions and Vocabulary

The following definitions are used throughout this document and the code:

- **Process**: A set of clothes to be washed together in one Segment (e.g. whites, darks, towels).
- **Segment**: An element of a laundry task (e.g. washer, dryer).
    Segments may contain multiple Processes (e.g. combine whites and darks in dryer).
    Also referred to as a Stage and sometimes refers to an individual machine.
- **Cycle**: An element from the set of possible Segment lengths (e.g. 30, 45, 60 minutes).
- **Task**: A list of Segments that must be completed in order to finish a Process (e.g. washer and dryer).
    Segments are ordered and may be repeated (e.g. washer, washer, dryer).
- **User**: A person who has a set of Processes.
- **Wait Time**: The time between when a User submits a Process and when the Process is started.
- **Occupied Idle Time**: The time when a Segment is not running but is not available for a new Process due to a Process that has not been removed.
- **Unoccupied Idle Time**: The time when a Segment is not running and is available for a new Process.
- **Performance**: $\text{Execution Time}^{-1}$


## Algorithms

### Scheduling

This algorithm is a first-come-first-serve (FCFS) scheduling algorithm.
It is defined in `Scheduler.py` and used in `Environment.py`.
Processes are added to a queue for the appropriate segment and are executed in the order they are received.
The environment initially gives the scheduler all processes from a given user before moving on to the next user.

Only the **window** rule is implemented. The window rule is a time limit on when a user can start a process.
The **time before removal** and **concurrent use limit** rules are not implemented.


### Stopping

This is meant to be a stopping algorithm that a user would use to decide when to do laundry (processes).
A user would presumably want to do laundry when the expected wait time is low.
However, estimating the wait time has a cost and waiting too long may result in incomplete processes.
This is similar to the problem of deciding when to stop looking for a parking spot as the destination approaches.

This is partially implemented by showing wait times for processes in the simulation.


### Game Theory

This is not implemented.

This is meant to be a game theory analysis of the effect of user strategies on performance.
The following are possible user strategies:

1. Maximize concurrent processes
2. Wait for a segment to finish before starting another (minimize offsets)
3. Greedily take the first available segment for each process

This is not implemented as it requires completion of previous algorithms.


## How to Run and Results

This project is written in Python 3.10 and uses Matplotlib 3.6 for plotting.
The following command will run the project in the `src` directory:

```bash
python main.py
```

This will run the project with the default parameters and a seed of 0.
The results of each experiment will display as a scatter plot.

The adjustable parameters are in `main()` of `main.py` and are described below:

- `rules`: A dictionary of rules to apply to the environment. Only `window` is implemented.
    The value of `window` is provided to `create_users()` as the latest start time.
    Start times are uniformly distributed between `[0, window - 2*LONG)` where `LONG` is the longest cycle length.
    The `window` is not enforced unless it is passed to the environment.
- `NUM_USERS`: The number of users to simulate.
- `PROCESSES_PER_USER`: The number of processes per user.

The scatter plots show the wait time for each process and the step time they were started.
Examples using the defaults are shown in the `doc` directory with a naming convention of `washers-dryers-rules.png`.
Note that the wait time for dryers includes the washer wait time and the washer cycle time.
