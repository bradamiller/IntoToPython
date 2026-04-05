# Exercise 7: The Challenge of Turning

**Starter code:** `code/starter/lesson-07-turning.py`

## Overview

The Manhattan class tells the robot **where** to go. Now you need to figure out **how** -- specifically, which direction to face before each step. You will implement the `get_needed_heading()` function and test it.

## What You Will Do

### Part 1: get_needed_heading()

Given the robot's current position and the next position (one step away), return the heading number the robot needs:

| Heading | Direction | row_diff | col_diff |
|---|---|---|---|
| 0 | North | -1 | 0 |
| 1 | East | 0 | +1 |
| 2 | South | +1 | 0 |
| 3 | West | 0 | -1 |

Fill in the function body using `if`/`elif` statements that check `row_diff` and `col_diff`, returning the appropriate heading number (0, 1, 2, or 3).

### Part 2: Test Your Function
Uncomment the test code and verify:
- `get_needed_heading((0,0), (1,0))` returns `2` (South)
- `get_needed_heading((1,0), (0,0))` returns `0` (North)
- `get_needed_heading((0,0), (0,1))` returns `1` (East)
- `get_needed_heading((0,1), (0,0))` returns `3` (West)
- All other test cases pass.

## Key Concepts

- **Heading as a number:** 0=North, 1=East, 2=South, 3=West (clockwise order).
- **`HEADING_NAMES = ["N", "E", "S", "W"]`** for display: `HEADING_NAMES[heading]` gives the letter.
- **Direction from coordinates:** The difference between two adjacent positions tells you which heading number is needed.
- **Counting right turns on paper:** Count clockwise steps from current heading to needed heading (0->1->2->3->0). The number of steps is the number of right turns (0, 1, 2, or 3).
- **Updating heading:** After turning, the new heading is simply `needed` (the heading you turned to face).
- **Coming in Lesson 8:** The Navigator class will use a while loop to turn right until the heading matches -- the code version of what you count on paper.

## Expected Output

```
===== Testing get_needed_heading =====
(0,0) to (1,0): 2 (S)
(1,0) to (0,0): 0 (N)
(0,0) to (0,1): 1 (E)
(0,1) to (0,0): 3 (W)
```

## When You Are Done

- Do all `get_needed_heading` tests pass?
- Can you trace through a full path by hand, tracking the heading number and counting right turns at each step?
- `get_needed_heading()` will become a method in the Navigator class in Lesson 8, along with `turn_to()` which implements the turning while loop.
