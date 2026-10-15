# Exercise 7: The Challenge of Turning

**Starter code:** `code/starter/lesson-07-turning.py`

## Overview

The Manhattan class tells the robot **where** to go. Now you need to figure out **how** -- specifically, which direction to face before each step. You will implement the `desired_heading()` function and test it.

## What You Will Do

### Part 1: desired_heading()

Given the robot's current position and the next position (one step away), return the heading number the robot needs:

| Heading | Direction | row_diff | col_diff |
|---|---|---|---|
| 0 | North | -1 | 0 |
| 1 | East | 0 | +1 |
| 2 | South | +1 | 0 |
| 3 | West | 0 | -1 |

Fill in the function body with four `if` statements that each check **both** `row_diff` and `col_diff` (North is `col_diff == 0 and row_diff == -1`), returning the heading number (0, 1, 2 or 3). If none matches, `raise ValueError(...)` naming both positions -- the two are not neighbors, and the program should stop here, not later.

### Part 2: Test Your Function
Uncomment the test code and verify:
- `desired_heading((0,0), (1,0))` returns `2` (South)
- `desired_heading((1,0), (0,0))` returns `0` (North)
- `desired_heading((0,0), (0,1))` returns `1` (East)
- `desired_heading((0,1), (0,0))` returns `3` (West)
- All other test cases pass.

## Key Concepts

- **Heading as a number:** 0=North, 1=East, 2=South, 3=West (clockwise order).
- **`HEADING_NAMES = ["N", "E", "S", "W"]`** for display: `HEADING_NAMES[heading]` gives the letter.
- **One change at a time:** Between two adjacent intersections, either the row OR the column changes — never both. That gives exactly 4 cases, one for each compass direction.
- **Direction from coordinates:** Check which of `row_diff` or `col_diff` is nonzero, and whether it is +1 or -1, to pick the desired heading.
- **Counting turns:** Each clockwise turn adds 1 to the heading, and `% 4` is the wrap. `(desired - heading) % 4` is the number of clockwise quarter turns; 3 means one counterclockwise turn instead. `turn_to` in Lesson 8 does exactly this.
- **Updating heading:** After `turn_to` finishes, the new heading equals the desired heading.
- **Coming in Lesson 8:** `desired_heading`, `turn_to` and `drive_path` become real functions that drive the robot, built on the Module 2 line-tracking functions.

## Expected Output

```
===== Testing desired_heading =====
(0,0) to (1,0): 2 (S)
(1,0) to (0,0): 0 (N)
(0,0) to (0,1): 1 (E)
(0,1) to (0,0): 3 (W)
```

## When You Are Done

- Do all `desired_heading` tests pass?
- Can you trace through a full path by hand, writing `(desired - heading) % 4` at each step and saying what the robot does -- including a step where the answer is 3?
- `desired_heading` will become a method in the Navigator class in Lesson 8, along with `turn_to` (the while loop) and `drive_path` (the list walker).
