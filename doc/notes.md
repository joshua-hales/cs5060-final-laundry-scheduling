# Notes and Plan

- `collections.deque` may be useful for FCFS scheduling


## Definitions and Vocabulary

- **Load**: A set of clothes to be washed together in one segment (e.g. whites, darks, towels).
- **Segment**: An element of a laundry task (e.g. washer, dryer). Segments may contain multiple loads (e.g. combine whites and darks in dryer).
- **Cycle**: An element from the set of possible segment lengths (e.g. 30, 45, 60 minutes).
- **Task**: A list of segments that must be completed in order to finish a load (e.g. washer and dryer). Segments are ordered and may be repeated (e.g. washer, washer, dryer).
- **User**: A person who has a set of loads.
- Wait
  - **Wait Time**: The time between when a user submits a load and when the load is started.
  - **Occupied Idle Time**: The time when a segment is not running but is not available for a new load due to a load that has not been removed.
  - **Unoccupied Idle Time**: The time when a segment is not running and is available for a new load.
- **Performance**: $\text{Execution Time}^{-1}$


## Possible Rules

1. Number of concurrent segments of one type per user
2. Time before forced removal of a load
3. Availability window


## Possible User Strategies

1. Maximize concurrent loads
2. Wait for a segment to finish before starting another (minimize offsets)
3. Greedily take the first available segment for each load
