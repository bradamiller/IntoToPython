# Exercise 8: Implementing the Navigator Class

**Starter code:** `code/starter/lesson-08-navigator.py`

## Overview

The Navigator class brings everything together: it takes a path from the Manhattan class and **physically drives the robot** along it using LineTrack from Module 2. You will complete three methods in the Navigator class.

## What You Will Do

### Complete __init__()
Set three attributes:
- `self.position` — the starting (row, col) tuple.
- `self.heading` — the starting heading number (0=N, 1=E, 2=S, 3=W).
- `self.line_track` — create using `LineTrack()`.

### Complete get_needed_heading()
This is the same logic from Lesson 7, now as a class method:
- Calculate `row_diff` and `col_diff` between `next_pos` and `self.position`.
- Return the heading number: 0 for North, 1 for East, 2 for South, 3 for West.

### Complete turn_to()
Turn the robot to face a given heading by turning right in a while loop:
- Use `while self.heading != needed_heading`: call `self.line_track.turn_right()`, then increment `self.heading` by 1 (wrap 4 to 0).
- The loop naturally stops when the robot is facing the right direction.

### Complete drive_path()
Drive the robot through a list of positions:
- Loop from index **1** to the end (index 0 is the starting position — the robot is already there).
- For each step: get the needed heading.
- If already facing the right way (`self.heading == needed`), call `self.line_track.drivetrain.straight(8)` to clear the intersection.
- Call `self.turn_to(needed)` to turn the robot.
- Call `self.line_track.track_until_cross()` to drive to the next intersection.
- Update `self.position`.

### Test in Three Steps
1. **Test Manhattan only** — verify the path computation prints correctly.
2. **Test Navigator creation** — uncomment and check that position and heading print correctly.
3. **Test full integration** — uncomment `drive_path()` and run on the robot.

## Key Concepts

- The Navigator **does not plan** the path — it receives a path from Manhattan and drives it.
- The Navigator **reuses LineTrack** from Module 2 — `track_until_cross()` for driving and `turn_right()` for turning.
- The `for` loop starts at index 1 because the robot is already at `path[0]`.
- When `self.heading == needed`, the robot must drive forward 8 cm to clear the current intersection before `track_until_cross()` looks for the next one.
- After each step, update `self.position` so `get_needed_heading()` works correctly for the next step.
- **Separation of concerns:** Manhattan plans, Navigator drives, LineTrack handles sensors.

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

- **Forgetting to update `self.heading`** after turning — the next turn calculation will be wrong.
- **Forgetting to update `self.position`** after driving — `get_needed_heading()` will use the old position.
- **Starting the loop at index 0** — the robot will try to "drive" to its current position.
- **Not clearing the intersection** when going straight — `track_until_cross()` will immediately re-detect the current crossing line.

## When You Are Done

- Does the robot physically arrive at (2, 2) on the grid?
- Does it make the correct turns (two right turns for the first step, then three right turns at the corner)?
- Try a different path and verify the robot follows it correctly.
