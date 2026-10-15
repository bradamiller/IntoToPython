# Lesson 3: Turning on the Grid

## Overview
Any route across a grid is "drive some segments, turn, drive some more." Students sequence `drive_intersections()` and the two turn functions into L-shaped paths, plan paths on paper before coding them, and learn the one ordering rule that matters: a turn comes after the arrival pair. `drive_intersections()` leaves the robot parked with its wheels on the last intersection and its sensors just past it -- exactly the position a turn needs. The robot pivots about its wheels, so it spins *on* the intersection, and the sensor-ended turn from Lesson 2-9 brings a sensor down on the crossing line. After the turn, the next drive starts with a line to follow; there is nothing to do in between.

An earlier version of this lesson claimed the turn "cleared the intersection by itself" and taught students not to clear after a turn. The turn does not drive forward at all; what makes it land is the drive-past *before* it. That is the rule to teach.

## Learning Objectives
By the end of this lesson, students will be able to:
- Sequence drives and turns into a path
- Turn at intersections with `turn_clockwise()` and `turn_counterclockwise()`, and say why the turn pivots on the intersection
- Explain what goes wrong if a turn runs before the drive-past
- Navigate an L-shaped path, planned on paper first

## Key Concepts
- **Drive, turn, drive**: `drive_intersections(2)`, `turn_clockwise()`, `drive_intersections(2)` is an L.
- **A turn needs the robot parked**: wheels on the intersection (the drive-past did that), sensors past the tape. The blind 60 degrees then the sensor-ended finish land a sensor on the crossing line.
- **Nothing between a turn and the next drive**: the turn ends with a sensor on the new line; `track_to_intersection()` follows it from there.
- **Turn before drive-past = pivot in the wrong place**: the wheels are short of the intersection, the robot spins around a point in front of it, and the sensors come down off the new line.
- **Plan on paper**: start, facing direction, segments per leg, where the turns go -- then one leg per line.

## Materials Required
- XRP robot; the grid, at least 3x3; `drive_intersections()` from Lesson 2
- `code/starter/lesson-03-turning-on-grid.py`; `code/solutions/lesson-03-turning-on-grid.py`
- `worksheets/03-turning-on-the-grid.md`; grid paper for planning

## Lesson Flow

### Introduction (10 minutes)
1. **City streets.** Go to the intersection, then turn. In code: `drive_intersections()`, a turn, `drive_intersections()` again.
2. **Where does the turn happen?** Ask where `drive_intersections()` leaves the robot. (Parked on the last intersection, wheels on the cross.) Hold the robot and pivot it about its wheels on a taped cross: the sensors sweep onto the crossing line. Now hold it with the wheels short of the cross and pivot: the sensors sweep somewhere else. "The drive-past is what makes the turn land."

### Guided Practice (15 minutes)
1. **The L.**
   ```python
   board.wait_for_button()

   drive_intersections(2)      # drive forward 2 intersections
   turn_clockwise()            # turn right onto the crossing line
   drive_intersections(2)      # drive 2 more, now sideways

   print("L-shape complete!")
   ```
   Run it. Point out there is nothing between the turn and the second drive: the turn ended with a sensor on the new line.
2. **Break it on purpose.** Replace the first `drive_intersections(2)` with two bare `track_to_intersection()` calls and one `drive_past_intersection()` after the first only, then turn. The robot pivots short of the corner and hunts. Discuss. Put the helper back -- it exists partly so the pair can't be half-written.

### Independent Practice (20 minutes)
1. **L with a left turn.** `drive_intersections(3)`, `turn_counterclockwise()`, `drive_intersections(1)`. Plan it on grid paper first: mark start, facing, legs, turn. Predict the end intersection; run; check.
2. **A U.** Drive, turn clockwise, drive one, turn clockwise, drive. Two clockwise turns reverse direction only because there is a segment between them.
3. **Your own path.** Three legs, two turns, planned on paper, predicted, then driven. Worksheet Part 4.

### Wrap-Up (5 minutes)
- What's the basic shape of any grid path? (A sequence of drives and turns.)
- What has to come before a turn? (The arrival pair -- the robot parked on the intersection.)
- What comes after a turn? (The next drive; a sensor is already on the new line.)

## Common Issues
- **Turn ends off the line / robot hunts**: the turn ran before the drive-past. Check the pair.
- **Turn overshoots the new line**: the blind part too long or `TURN_EFFORT` too high; tune in Lesson 2-9's terms.
- **Path off by one intersection**: count the legs on paper against the code; a leg of 2 drives *to* the second intersection, not past it.
- **Robot turns mid-segment**: a turn was called without an arrival pair before it.

## Assessment
- Can students write the calls for a described path, and draw the path for given calls?
- Can they explain why the turn must wait for the drive-past?
- Exit ticket: "Write the calls for 'drive 2, turn left, drive 1.'"
