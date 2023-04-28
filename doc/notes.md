# Notes and Plan

- `collections.deque` may be useful for FCFS scheduling


## Definitions and Vocabulary

- **Process**: A set of clothes to be washed together in one Segment (e.g. whites, darks, towels).
- **Segment**: An element of a laundry task (e.g. washer, dryer). Segments may contain multiple Processes (e.g. combine whites and darks in dryer).
- **Cycle**: An element from the set of possible Segment lengths (e.g. 30, 45, 60 minutes).
- **Task**: A list of Segments that must be completed in order to finish a Process (e.g. washer and dryer). Segments are ordered and may be repeated (e.g. washer, washer, dryer).
- **User**: A person who has a set of Processes.
- **Wait Time**: The time between when a User submits a Process and when the Process is started.
- **Occupied Idle Time**: The time when a Segment is not running but is not available for a new Process due to a Process that has not been removed.
- **Unoccupied Idle Time**: The time when a Segment is not running and is available for a new Process.
- **Performance**: $\text{Execution Time}^{-1}$


## Possible Rules

1. Number of concurrent Segments of one type per user
2. Time before forced removal of a Process
3. Availability window


## Possible User Strategies

1. Maximize concurrent Processes
2. Wait for a Segment to finish before starting another (minimize offsets)
3. Greedily take the first available Segment for each Process
