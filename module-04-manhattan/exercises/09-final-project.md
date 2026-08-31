# Exercise 9: Final Project — Multi-Destination Navigation

**Starter code:** `code/starter/lesson-09-final-project.py`

## Overview

This is the capstone exercise for Module 4. Your robot starts at `(0, 0)` facing North and must visit **4 or more destinations** on the grid, in order. You will write the main program that ties together `compute_manhattan_path()` and `drive_path()`.

*Skip to the bottom of this file for the Optional Extension (the classes version), if your course covers classes.*

## Requirements

- At least **4 destinations** of your choosing.
- Print each path before driving it.
- Reassign `position` and `heading` from `drive_path()`'s return value after each leg so the next path starts from the right place.
- The robot must physically navigate the grid.

## What You Will Do

### Set Up
- Create a `Board` object using `Board.get_default_board()`.
- Set `position = (0, 0)` and `heading = 0` (North).
- Define a list of 4+ destination tuples.

### The Main Loop
Write a `for` loop that goes through each destination:
1. Print which destination you are navigating to.
2. Compute the path using `compute_manhattan_path(position, dest)`.
3. Print the path and number of steps.
4. Drive the path and capture the result: `position, heading = drive_path(path, position, heading)`.
5. **Reassign** `position` and `heading` from that call (critical — without this, every path starts from (0, 0)).
6. Print arrival confirmation with heading using `HEADING_NAMES[heading]`.

### Wait for Button
Add `board.wait_for_button()` before the loop starts so you can place the robot on the grid before it moves.

## Testing Strategy

Follow these levels in order:

### Level 1: Path Computation Only (No Robot)
- Comment out the `drive_path()` call and just set `position = dest` directly instead.
- Run the program and verify all printed paths look correct.
- Check that `position` updates after each leg.

### Level 2: Single Leg on Robot
- Enable driving but use only **one destination**.
- Place the robot at (0, 0) facing North on a grid line.
- Verify it follows the line and arrives at the correct cell.

### Level 3: Full Sequence
- Enable all destinations.
- Run the complete program.
- Verify the robot visits every destination in order.

## Extension Challenges

Once your basic program works, try these:

1. **Return Home:** Add `(0, 0)` as the last destination.
2. **Round Trip:** After visiting all destinations, reverse the list and visit them again in reverse order using `list(reversed(destinations))`.
3. **Button Pause:** Add `board.wait_for_button()` between each leg to check positioning.
4. **Custom Destinations:** Ask the user to type in row and column values with `input()`.

## Example Output

```
=== XRP Grid Navigation: Final Project ===
Starting at: (0, 0)
Destinations: [(2, 0), (2, 3), (0, 3), (0, 0)]

--- Navigating to (2, 0) ---
Path: [(1, 0), (2, 0)]
Steps: 2
Arrived at: (2, 0)
Heading: S

--- Navigating to (2, 3) ---
Path: [(2, 1), (2, 2), (2, 3)]
Steps: 3
Arrived at: (2, 3)
Heading: E

--- Navigating to (0, 3) ---
Path: [(1, 3), (0, 3)]
Steps: 2
Arrived at: (0, 3)
Heading: N

--- Navigating to (0, 0) ---
Path: [(0, 2), (0, 1), (0, 0)]
Steps: 3
Arrived at: (0, 0)
Heading: W

=== All destinations reached! ===
Final position: (0, 0)
```

## When You Are Done

- Does your robot visit all destinations and end in the right place?
- What was the hardest part to debug?
- Congratulations — you have built a complete autonomous grid navigation system!

---

## Optional Extension: The Classes Version

*Skip this section if your course doesn't cover classes.*

**Reference code:** `code/solutions/lesson-09-final-project-class-addon.py`

Rebuild the main program using `Manhattan` and `Navigator` objects instead of bare functions:
- Create `manhattan = Manhattan((0, 0))` and `navigator = Navigator((0, 0), 0)` once, before the loop.
- Replace `compute_manhattan_path(position, dest)` with `manhattan.compute_path(dest)`.
- Replace `position, heading = drive_path(path, position, heading)` with `navigator.drive_path(path)` -- but add one extra line the functions version doesn't need: `manhattan.position = navigator.position`, so the two objects stay in sync.

Compare the two main programs side by side. Which parts got shorter? Which parts got longer? Where would a bug be easier to spot in each version?
