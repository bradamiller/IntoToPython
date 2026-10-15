# Exercise 8: Driving the Path

**Starter code:** `code/starter/lesson-08-driving-functions.py`

## Overview

The driving functions bring everything together: they take a path from `compute_manhattan_path()` and **physically drive the robot** along it, using the four line-tracking functions from Module 2. You will complete three functions: `desired_heading()`, `turn_to()` and `drive_path()`.

*Skip to the bottom of this file for the Optional Extension (the `Navigator` class), if you did the Module 2 class extensions.*

## What You Will Do

### Complete `desired_heading()`
Lesson 7's logic as working code:
- Compute `row_diff` and `col_diff` (next minus current).
- Check **both** differences in each case: North is `col_diff == 0 and row_diff == -1`, and so on.
- If none of the four matches, `raise ValueError(...)` naming both positions.

### Complete `turn_to()`
- `turns = (desired - heading) % 4`
- If `turns == 3`, call `turn_counterclockwise()` once; otherwise call `turn_clockwise()` `turns` times.
- **Return `desired`** -- the caller needs the new heading.

### Complete `drive_path()`
- `for next_pos in path:` (the path does not include the start, so every element is somewhere new to drive to)
- Work out the heading needed; `heading = turn_to(heading, needed)`
- `track_to_intersection()` then `drive_past_intersection()` -- every time
- `position = next_pos`
- **Return `position, heading`** at the end.

### Test in three steps
1. **Desktop mode** -- swap the four Module 2 calls for `print()` and run on your laptop. The printed turns and tracks should match your paper trace.
2. **One leg** -- Module 2 functions back in; drive `[(1, 0)]`. Wheels on the intersection at the end?
3. **Full path** -- plan, **print the path**, wait for the button, drive. Capture the return value: `position, heading = drive_path(path, position, heading)`.

## Key Concepts

- The driving functions **do not plan**. They are handed a path.
- They **reuse Module 2**: `track_to_intersection()`, `turn_clockwise()`, `turn_counterclockwise()`, `drive_past_intersection()`. None of those know what a grid is.
- **Sensors lead the wheels.** `track_to_intersection()` stops with the wheels short of the cross; `drive_past_intersection()` parks them on it, so turns pivot there and the next track starts clean. After every track.
- **Told, not remembered.** `position` and `heading` are the functions' own variables. Every function that changes them returns the new value, and the caller assigns from it.

## Expected Console Output

```
=== Test 3: Drive (0,0) to (2,2) ===
Path: [(1, 0), (2, 0), (2, 1), (2, 2)]
Final position: (2, 2)
Final heading: E
```

## Common Mistakes

- **Dropping the return value**: `drive_path(...)` on its own line. The robot drives fine once; the next path is planned from the old position.
- **Forgetting `return desired`** in `turn_to()` -- `heading` in `drive_path` becomes `None` and the next `% 4` fails.
- **Reading the sensor before turning** (Module 5 habit, too early): the order inside the loop is turn, then track.
- **Including the start in the path** -- `desired_heading` raises on the zero step. That is the `raise` working.
- **Skipping `drive_past_intersection()`** -- the next track stops on the cross it is sitting on, and turns pivot in front of the intersection.

## When You Are Done

- Does the robot arrive at (2, 2) with its wheels on the intersection?
- Did the corner turn go the short way? (Facing South, needing East: one counterclockwise turn.)
- Plan a second path from where the robot ended up and drive it. Did you assign from the return value?

---

## Optional Extension: The `Navigator` Class

*Do this after the functions version works on the robot.*

`code/solutions/lesson-08-navigator-class-addon.py` has the same three functions as methods of a `Navigator` that owns `position` and `heading` and holds a `LineTrack`:

```python
navigator = Navigator((0, 0), 0)
path = compute_manhattan_path(navigator.position, (2, 2))
print("Path:", path)
board.wait_for_button()
navigator.drive_path(path)
print("Arrived at:", navigator.position)
```

This is the first constructor in the course that takes real data. Think of Lesson 2-8's blueprint and houses, with an address on every house: the method is a work order written once, with a blank for the address (`self` in the `def`); `navigator.drive_path(path)` fills the blank in with *this* navigator; inside the method, `self.position` is the position at this address and no other.

Notice what the class buys: `drive_path()` returns nothing, because `position` and `heading` live inside the navigator and are updated there. There is nothing to pass back and forth, so nothing to forget.

- Build `Navigator` with `__init__` first; print `navigator.position` and `navigator.heading`.
- Move the three functions in, adding `self` and reading `self.position` / `self.heading`.
- Run the same three tests.
