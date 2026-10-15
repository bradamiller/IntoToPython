# Lesson 2: Driving Multiple Intersections

## Overview
Reaching the first intersection is two calls. Reaching the third is the same two calls three times -- a `for` loop. This lesson turns the arrival pair into a building block, `drive_intersections(count)`, and looks closely at why the second pair works at all: without `drive_past_intersection()` between them, a second `track_to_intersection()` would find `is_at_cross()` already `True` and return without moving.

An earlier version of this lesson taught a timed nudge to "clear the cross" after each intersection, with an `if i < count - 1` guard to skip it on the last one. The toolkit's `drive_past_intersection()` replaces both: it is a fixed distance, and it parks the wheels *on* the cross rather than past it, so the robot always ends up sitting on the last intersection and there is nothing to skip.

*Class extension students use `tracker.track_to_intersection()` and `tracker.drive_past_intersection()`; nothing else changes.*

## Learning Objectives
By the end of this lesson, students will be able to:
- Explain why two `track_to_intersection()` calls with nothing between them would not move the robot
- Drive a chosen number of intersections with a `for` loop around the arrival pair
- Write `drive_intersections(count)` and use it
- Say where the robot is after the last loop pass, and why there is no special case

## Key Concepts
- **The thought experiment**: after a track, the sensors are on the cross. A second track's loop condition, `not is_at_cross()`, is already `False`; the loop body never runs.
- **Second job of the drive-past**: besides parking the wheels, it carries the sensors past the tape onto plain line, so the next track has a line to follow and a new cross to find.
- **The pattern**: track, drive past, track, drive past... The loop body is the pair; `i` is only used for the print.
- **No last-intersection special case**: the drive-past moves the wheels onto the intersection, not beyond it.
- **`drive_intersections(count)`**: a `for` loop and a count, packaged -- the same shape as Module 1's `draw_polygon()`.

## Materials Required
- XRP robot; the grid; both Module 2 toolkits
- `code/starter/lesson-02-multiple-intersections.py`; `code/solutions/lesson-02-multiple-intersections.py`
- `worksheets/02-driving-multiple-intersections.md`

## Lesson Flow

### Introduction (10 minutes)
1. **The thought experiment.** Write `track_to_intersection()` twice on the board with nothing between. Trace it: the first stops with both sensors on the cross. What is `is_at_cross()` when the second starts? `True`. So `while not is_at_cross()` is `False` immediately -- the robot "arrives" without moving. "What moves the sensors off the cross?" `drive_past_intersection()`. That is its second job.
2. **The pattern.** Track, drive past, track, drive past. Ask where the robot is after two pairs: parked on the second intersection, sensors just past it.

### Guided Practice (15 minutes)
1. **Two by hand.** The pair twice; run it. Confirm the robot is on the second intersection.
2. **The loop.**
   ```python
   intersections = 3

   for i in range(intersections):
       print("Driving to intersection", i + 1)
       track_to_intersection()
       drive_past_intersection()

   print("Done! Parked on intersection", intersections)
   ```
   Walk it with `i = 0, 1, 2` and have students say where the robot is after each pass. Ask whether the last drive-past carries the robot off the final intersection. (No -- it carries the wheels *onto* it. The name says what the sensors do, not the wheels.)

### Independent Practice (20 minutes)
1. **Write the helper.** `drive_intersections(count)`: one parameter, a `for` loop, the pair inside, a print. Replace the loop in the program with `drive_intersections(3)`. Compare with the solution only after it runs. If theirs has an `if` in it, ask what it guards against.
2. **Count and check.** Run `drive_intersections(2)` and `drive_intersections(4)` from the same start; confirm the robot parks where the count says.
3. **Break it.** Remove `drive_past_intersection()` from the helper and run `drive_intersections(3)`. The robot stops at the first intersection and prints all three. Put it back. Worksheet Part 4.
4. **Challenge:** a speed parameter -- change `BASE_EFFORT` before the loop and restore it after (needs `global`, Lesson 2-8).

### Wrap-Up (5 minutes)
- Why must the drive-past come between two tracks? (The sensors are still on the cross; the second track would return at once.)
- Where is the robot after the last pass? (Parked on the last intersection.)
- What does `drive_intersections()` package? (A loop and a count around the arrival pair.)

## Common Issues
- **Robot stops at the first intersection and claims all N**: the drive-past is missing from the loop.
- **Robot overshoots the next intersection**: `BASE_EFFORT` too high for the grid spacing; slow down. The drive-past distance is fixed and should not cause this.
- **Robot ends past the last intersection**: a student added a second drive-past, or a timed nudge from an old version. One pair per intersection.

## Assessment
- Can students explain the thought experiment?
- Can they drive exactly N intersections with the helper and say where the robot ends?
- Exit ticket: "Why is there no special case for the last intersection?" (The drive-past parks on it, not past it.)
