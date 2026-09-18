# Exercise 8: Driving the Path

**Starter code:** `code/starter/lesson-08-driving-functions.py`

## Overview

The driving functions bring everything together: they take a path from `compute_manhattan_path()` and **physically drive the robot** along it using the Module 2/3 driving toolkit. You will complete three functions: `desired_heading()`, `turn_to()`, and `drive_path()`.

*Skip to the bottom of this file for the Optional Extension (packaging these as a `Navigator` class), if your course covers classes.*

## What You Will Do

### Complete desired_heading()
This is the same logic from Lesson 7, now as working code:
- Calculate `row_diff` and `col_diff` between `next_pos` and `position`.
- Return the heading number: 0 for North, 1 for East, 2 for South, 3 for West.

### Complete turn_to()
Turn the robot to face a given heading by turning right in a while loop:
- Use `while heading != desired`: call `turn_right()`, then increment `heading` by 1 (wrap 4 to 0).
- The loop naturally stops when the robot is facing the right direction.
- **Return `heading`** at the end -- this is the step students most often forget.

### Complete drive_path()
Drive the robot through a list of positions:
- Iterate directly: `for next_pos in path:` (the path does not include the starting position, so every element is a new cell to drive to).
- For each step: get the desired heading.
- If already facing the right way (`heading == needed`), call `clear_intersection()`.
- Call `heading = turn_to(heading, needed)` to turn the robot and capture the new heading.
- Call `track_until_cross()` to drive to the next intersection.
- Update the local `position` variable.
- **Return `position, heading`** at the end.

### Test in Three Steps
1. **Test path computation only** — verify `compute_manhattan_path()` prints correctly.
2. **Set up starting state** — uncomment and check that position and heading print correctly.
3. **Test full integration** — uncomment `drive_path()` and run on the robot, capturing its return value.

## Key Concepts

- The driving functions **do not plan** the path — they receive a path from `compute_manhattan_path()` and drive it.
- They **reuse the Module 2/3 toolkit** — `track_until_cross()` for driving and `turn_right()` for turning.
- The `for` loop iterates directly over the path with `for next_pos in path:` because the path does not include the starting position.
- When `heading == needed` (no turn needed), the robot must call `clear_intersection()` to drive forward 8 cm before `track_until_cross()` looks for the next one. When a turn happens, the turning motion itself clears the cross.
- **Turning by adding 1:** Each right turn adds 1 to `heading`. When heading reaches 4, wrap back to 0. The loop stops automatically when `heading == desired`.
- After each step, update the local `position` variable so `desired_heading()` works correctly for the next step.
- **Threading state through return values:** Because `position` and `heading` are just local variables inside these functions, every function that changes them must `return` the new value so the caller can capture it.

## Expected Console Output

```
Path from (0,0) to (2,2): [(1, 0), (2, 0), (2, 1), (2, 2)]

Starting position: (0, 0)
Starting heading: N

--- Driving path ---
Final position: (2, 2)
Final heading: E
```

## Common Mistakes

- **Forgetting `return heading`** at the end of `turn_to()` — the caller's `heading` variable never updates, and every subsequent turn calculation is wrong.
- **Forgetting `return position, heading`** at the end of `drive_path()` — same problem, one level up.
- **Forgetting to reassign the return value** in the calling code: `position, heading = drive_path(...)`, not just `drive_path(...)`.
- **Including the start position in the path** — the robot will try to "drive" to where it already is.
- **Not clearing the intersection** when going straight — `track_until_cross()` will immediately re-detect the current crossing line.

## When You Are Done

- Does the robot physically arrive at (2, 2) on the grid?
- Does it make the correct turns (two right turns for the first step — heading 0 → 1 → 2 — then three right turns at the corner with the 4 → 0 wrap)?
- Try a different path and verify the robot follows it correctly.

---

## Optional Extension: The Navigator Class

*Skip this section if your course doesn't cover classes.*

**Reference code:** `code/solutions/lesson-08-navigator-class-addon.py`

Repackage the three functions as a `Navigator` class:
- `__init__(self, start, heading)` stores `self.position`, `self.heading`, and creates `self.line_track = LineTrack()`
- `desired_heading(self, next_pos)` reads `self.position` instead of a `position` parameter
- `turn_to(self, desired)` updates `self.heading` in place -- no `return` needed, since the object itself now holds the updated state
- `drive_path(self, path)` updates `self.position` and `self.heading` in place, calling `self.line_track.turn_right()` / `self.line_track.track_until_cross()` instead of the bare toolkit functions

Test it with `Navigator((0, 0), 0)` and compare the output to the function version -- it should match exactly.
