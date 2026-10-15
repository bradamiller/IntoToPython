# Lesson 1: Introduction to the Grid

## Overview
Students move from the taped circle (Module 2) to a taped grid. A grid is lines running two ways, and wherever two cross is an intersection -- and to the robot's two sensors an intersection looks exactly like the cross on the circle: both sensors high at once. So the Module 2 toolkits drive the grid without a single change. That is the point of the module: no new Python, just *reuse*.

Arriving at an intersection is the pair from Lesson 2-9, `track_to_intersection()` then `drive_past_intersection()`: the sensors reach the cross first, and the drive-past puts the wheels on it. The pair is what "arrive" means for the rest of the course.

*If students did the Module 2 class extensions, everything below works identically through `tracker.track_to_intersection()` and so on -- only the call syntax changes.*

## Learning Objectives
By the end of this lesson, students will be able to:
- Describe the grid as lines and intersections, and explain why an intersection reads like the Module 2 cross
- Name the four driving functions and what ends each one
- Arrive at the first intersection with the pair `track_to_intersection()` + `drive_past_intersection()`
- Turn onto the crossing line with `turn_clockwise()` or `turn_counterclockwise()`

## Key Concepts
- **Grid**: taped lines in two directions; an **intersection** is where two cross -- both sensors high.
- **Toolkit reuse**: the Module 2 functions know how to follow tape and find crosses. They have no idea what a grid is, and don't need to.
- **The arrival pair**: `track_to_intersection()` stops with the sensors on the cross; `drive_past_intersection()` (8.75 cm, sensor-to-axle) parks the wheels on it and moves the sensors past the tape.
- **Turns pivot on the intersection**: the robot spins about its wheels, so the drive-past is what makes a turn land on the crossing line.

## Materials Required
- XRP robot; a taped grid, at least 3x3, same tape and surface as the Module 2 circle
- Both Module 2 toolkits (`code/solutions/lesson-01-grid-intro.py` has them at the top)
- `worksheets/01-introduction-to-the-grid.md`

## Lesson Flow

### Introduction (10 minutes)
1. **From circle to grid.** Show the grid. "Remember the cross on the circle? What if there were crosses everywhere?" A grid is intersections connected by lines. Ask what the sensors see at an intersection -- both high, exactly the Module 2 cross.
2. **The four functions.** On the board, with what ends each:
   - `track_to_intersection()` -- both sensors see the cross
   - `drive_past_intersection()` -- 8.75 cm driven; wheels on the cross
   - `turn_clockwise()` / `turn_counterclockwise()` -- a sensor finds the next line
   "Nothing in that list says row, column or grid. That's why it works here unchanged."

### Guided Practice (15 minutes)
1. **Setup.** Robot centered on a line, behind an intersection, facing along the line.
2. **The program.** Both toolkits, then two lines:
   ```python
   from XRPLib.reflectance import Reflectance
   from XRPLib.differential_drive import DifferentialDrive
   from XRPLib.board import Board

   # ===== Sensor toolkit (Module 2 Lesson 8) =====
   reflectance = Reflectance.get_default_reflectance()
   THRESHOLD = 0.5

   def get_left():
       return reflectance.get_left()

   def get_right():
       return reflectance.get_right()

   def get_error():
       return get_left() - get_right()

   def is_at_cross():
       return get_left() > THRESHOLD and get_right() > THRESHOLD

   def is_either_on_line():
       return get_left() > THRESHOLD or get_right() > THRESHOLD

   # ===== Driving toolkit (Module 2 Lesson 9) =====
   drivetrain = DifferentialDrive.get_default_differential_drive()
   BASE_EFFORT = 0.4
   KP = 0.5
   TURN_EFFORT = 0.25

   def drive_past_intersection():
       drivetrain.straight(8.75, 0.5)

   def track_to_intersection():
       while not is_at_cross():
           error = get_error()
           correction = error * KP
           drivetrain.arcade(BASE_EFFORT, -correction)
       drivetrain.stop()

   def turn_clockwise():
       drivetrain.turn(-60, TURN_EFFORT)
       drivetrain.arcade(0, -TURN_EFFORT)
       while not is_either_on_line():
           pass
       drivetrain.stop()

   def turn_counterclockwise():
       drivetrain.turn(60, TURN_EFFORT)
       drivetrain.arcade(0, TURN_EFFORT)
       while not is_either_on_line():
           pass
       drivetrain.stop()

   # ===== Main program =====
   board = Board.get_default_board()

   board.wait_for_button()
   print("Driving to first intersection...")
   track_to_intersection()
   drive_past_intersection()
   print("Intersection reached!")
   ```
3. **Discussion.** The toolkits are character-for-character Module 2. Point at where the robot stopped: wheels over the intersection, sensors just past it. "That is what arriving means from now on. Every arrival is those two calls."

### Independent Practice (15 minutes)
1. **Reach it, then turn.** Add `turn_clockwise()` after the pair and run it. The robot should end on the intersection facing the crossing line, with a sensor on it. Then try `turn_counterclockwise()`.
2. **Start on an intersection.** Put the robot *on* an intersection and run the program. It reports "Intersection reached!" at once without moving -- `is_at_cross()` was already `True`. Back it onto a plain line segment. Worksheet Part 4.
3. **Challenge:** pair, turn, pair -- a two-segment path, previewing Lesson 3.

### Wrap-Up (5 minutes)
- What is a grid intersection, to the robot? (The same both-sensors-high cross.)
- What two calls arrive at an intersection? (`track_to_intersection()`, `drive_past_intersection()`.)
- Why didn't you write any new code? (The toolkit handles tape and crosses; the grid is tape and crosses.)

## Common Issues
- **Reports the intersection instantly**: started on one. Back onto a line segment.
- **Stops short or long of the intersection**: `drive_past_intersection()`'s 8.75 cm is sensor-to-axle on an XRP; measure yours if the mounting differs.
- **Turn ends off the line**: the turn ran before the drive-past, so it pivoted in front of the intersection. Always the pair first.
- **Threshold**: same tape, same surface, so it should not need re-tuning; check if the grid was made with different tape.

## Assessment
- Can students explain why the Module 2 toolkit works on the grid unchanged?
- Can they arrive at the first intersection reliably and say where the wheels are?
- Exit ticket: "Which function turns the robot onto the crossing line, and what has to happen before it?" (`turn_clockwise()` / `turn_counterclockwise()`; the arrival pair.)
