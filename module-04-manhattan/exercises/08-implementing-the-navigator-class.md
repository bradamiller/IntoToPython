# Exercise 8: Implementing the Navigator Class

**Starter code:** `code/starter/lesson-08-navigator.py`

## Overview

The Navigator class brings everything together: it takes a path from the Manhattan class and **physically drives the robot** along it, turning at each step as needed. You will complete four methods in the Navigator class.

## What You Will Do

### Complete __init__()
Set three attributes:
- `self.position` — the starting (row, col) tuple.
- `self.heading` — the starting compass direction (`"N"`, `"S"`, `"E"`, or `"W"`).
- `self.drivetrain` — create using `DifferentialDrive.get_default_differential_drive()`.

### Complete get_needed_direction()
This is the same logic from Lesson 7, now as a class method:
- Calculate `row_diff` and `col_diff` between `next_pos` and `self.position`.
- Return `"N"`, `"S"`, `"E"`, or `"W"` based on the differences.

### Complete turn_to()
Turn the robot to face a given direction:
- Define `right_turns` and `left_turns` dictionaries.
- If already facing the right direction, do nothing.
- If the needed direction is a right turn, call `self.drivetrain.turn(90)`.
- If a left turn, call `self.drivetrain.turn(-90)`.
- Otherwise (opposite direction), call `self.drivetrain.turn(180)`.
- Always update `self.heading` after turning.

### Complete drive_path()
Drive the robot through a list of positions:
- Loop from index **1** to the end (index 0 is the starting position — the robot is already there).
- For each step: get the needed direction, turn to face it, drive forward with `self.drivetrain.straight(20)`, and update `self.position`.

### Test in Three Steps
1. **Test Manhattan only** — verify the path computation prints correctly.
2. **Test Navigator creation** — uncomment and check that position and heading print correctly.
3. **Test full integration** — uncomment `drive_path()` and run on the robot.

## Key Concepts

- The Navigator **does not plan** the path — it receives a path from Manhattan and drives it.
- The `for` loop starts at index 1 because the robot is already at `path[0]`.
- After each step, update `self.position` so `get_needed_direction()` works correctly for the next step.
- **Separation of concerns:** Manhattan plans, Navigator drives.

## Expected Console Output

```
Path from (0,0) to (2,2): [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

Navigator position: (0, 0)
Navigator heading: N

--- Driving path ---
Final position: (2, 2)
Final heading: E
```

## Common Mistakes

- **Forgetting to update `self.heading`** after a turn — the next turn calculation will be wrong.
- **Forgetting to update `self.position`** after driving — `get_needed_direction()` will use the old position.
- **Starting the loop at index 0** — the robot will try to "drive" to its current position.

## When You Are Done

- Does the robot physically arrive at (2, 2) on the grid?
- Does it make the correct turns (180 for the first step, then left turn at the corner)?
- Try a different path and verify the robot follows it correctly.
