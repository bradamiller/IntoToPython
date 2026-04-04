# Exercise 7: The Challenge of Turning

**Starter code:** `code/starter/lesson-07-turning.py`

## Overview

The Manhattan class tells the robot **where** to go. Now you need to figure out **how** — specifically, which direction to face before each step. You will implement two functions: `get_needed_heading()` and `count_right_turns()`.

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

### Part 2: count_right_turns()

Given the heading the robot is currently facing (a number 0-3) and the heading it needs to face (also 0-3), return the number of right turns required: 0, 1, 2, or 3.

**The formula:** `(needed - current) % 4`

- 0 = no turn needed (already facing the right way)
- 1 = one right turn (90 degrees clockwise)
- 2 = two right turns (180 degrees)
- 3 = three right turns (270 degrees clockwise)

This single line handles all cases!

### Part 3: Test Your Functions
Uncomment the test code and verify:
- `get_needed_heading((0,0), (1,0))` returns `2` (South)
- `get_needed_heading((1,0), (0,0))` returns `0` (North)
- `count_right_turns(0, 1)` returns `1` (one right turn: N to E)
- `count_right_turns(0, 2)` returns `2` (two right turns: N to S)
- All other test cases pass.

## Key Concepts

- **Heading as a number:** 0=North, 1=East, 2=South, 3=West (clockwise order).
- **`HEADING_NAMES = ["N", "E", "S", "W"]`** for display: `HEADING_NAMES[heading]` gives the letter.
- **Direction from coordinates:** The difference between two adjacent positions tells you which heading number is needed.
- **Modular arithmetic:** `(needed - current) % 4` gives the number of right turns. One formula handles every case!
- **Updating heading:** After turning, the new heading is simply `needed` (the heading you turned to face).

## Expected Output

```
===== Testing get_needed_heading =====
(0,0) to (1,0): 2 (S)
(1,0) to (0,0): 0 (N)
(0,0) to (0,1): 1 (E)
(0,1) to (0,0): 3 (W)

===== Testing count_right_turns =====
Heading 0 (N), need 0 (N): 0 right turns
Heading 0 (N), need 2 (S): 2 right turns
Heading 0 (N), need 1 (E): 1 right turns
Heading 0 (N), need 3 (W): 3 right turns
Heading 1 (E), need 2 (S): 1 right turns
Heading 3 (W), need 0 (N): 1 right turns
```

## When You Are Done

- Do all heading and turn-count tests pass?
- Can you trace through a full path by hand, tracking the heading number at each step?
- These functions will become methods in the Navigator class in Lesson 8.
