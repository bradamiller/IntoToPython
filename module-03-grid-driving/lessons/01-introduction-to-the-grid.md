# Lesson 1: Introduction to the Grid

## Overview
Students transition from the taped circle (Module 2) to a taped grid. They learn how the grid is organized as intersections connected by lines, and how the sensor/driving toolkit from Module 2 can be used without modification to navigate between intersections. Students practice driving to the first intersection and stopping — the fundamental building block for all grid navigation.

*If your course covers the Module 2 Optional Extension (classes), everything below works identically through `tracker.track_until_cross()`, `tracker.turn_right()`, and `tracker.turn_left()` instead of bare function calls — only the call syntax changes.*

## Learning Objectives
By the end of this lesson, students will be able to:
- Describe the physical grid layout and how intersections are formed
- Explain how cross detection from Module 2 maps to grid intersections
- Use the Module 2 toolkit to drive from one intersection to the next
- Place the robot on the grid and drive to the first intersection

## Key Concepts
- **Grid**: A network of taped lines forming rows and columns on the floor
- **Intersection**: Where two taped lines cross — detected by both sensors reading high
- **Toolkit reuse**: The same `track_until_cross()` function that detected the cross on the circle now detects grid intersections
- **Code reuse**: No new functions needed — Module 2 code works directly on the grid

## Materials Required
- XRP Robot with reflectance sensors
- White surface with taped grid (at least 3×3 intersections)
- Working sensor and driving toolkit from Module 2 (Lessons 8-9)
- VS Code with XRPLib installed

## Lesson Flow

### Introduction (10 minutes)

1. **Hook: From Circle to Grid**:
   - Show the new grid setup
   - Ask: "Remember the cross on the circle? What if there were crosses EVERYWHERE?"
   - "A grid is just many intersections connected by lines"
   - The robot already knows how to follow lines and detect crosses!

2. **Grid Layout**:
   - Lines running in two directions (horizontal and vertical)
   - Where lines cross = intersection
   - Each intersection is a potential stopping point
   - The robot will use line following between intersections and cross detection to know when it arrives

3. **Review: What the Toolkit Already Does**:
   - `track_until_cross()` — follows line, stops at intersection
   - `turn_right()` — turns right at an intersection onto the perpendicular line
   - `turn_left()` — turns left at an intersection onto the perpendicular line
   - These three functions are ALL you need for grid navigation!

### Guided Practice: Drive to First Intersection (15 minutes)

1. **Setup**:
   - Place the robot on the grid, centered on a line, behind an intersection
   - The robot should be facing along the line toward the next intersection

2. **The Program**:
   ```python
   from XRPLib.reflectance import Reflectance
   from XRPLib.differential_drive import DifferentialDrive
   from XRPLib.board import Board

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

   def is_off_line():
       return get_left() < THRESHOLD and get_right() < THRESHOLD

   drivetrain = DifferentialDrive.get_default_differential_drive()
   BASE_EFFORT = 0.4
   KP = 0.5

   def clear_intersection():
       drivetrain.straight(8, 0.5)

   def track_until_cross():
       while not is_at_cross():
           error = get_error()
           left = BASE_EFFORT - error * KP
           right = BASE_EFFORT + error * KP
           drivetrain.set_effort(left, right)
       drivetrain.stop()

   def turn_right():
       clear_intersection()
       drivetrain.set_effort(0.3, -0.3)
       while is_off_line():
           pass
       drivetrain.stop()

   def turn_left():
       clear_intersection()
       drivetrain.set_effort(-0.3, 0.3)
       while is_off_line():
           pass
       drivetrain.stop()

   # --- Main Program ---
   board = Board.get_default_board()

   board.wait_for_button()
   print("Driving to first intersection...")
   track_until_cross()
   print("Intersection reached!")
   ```

3. **Discussion Points**:
   - The code is IDENTICAL to Module 2 — we're just running it on a grid instead of a circle
   - `track_until_cross()` works because grid intersections look the same as the cross on the circle
   - This is the power of code reuse!

### Independent Practice (15 minutes)

1. **Exercise 1: Drive and confirm**:
   - Place robot on the grid
   - Run the program to drive to the first intersection
   - Verify the robot stops cleanly at the intersection

2. **Exercise 2: Try from different starting positions**:
   - Start from different lines on the grid
   - Does it always reach the next intersection?
   - What happens if you start AT an intersection? (It detects it immediately!)

3. **Exercise 3: Drive and turn**:
   - After reaching the intersection, add a turn:
     ```python
     track_until_cross()
     print("Turning right...")
     turn_right()
     print("Now facing a new direction!")
     ```

### Wrap-Up (5 minutes)

1. **Key Takeaways**:
   - The grid is built from the same lines and crosses as Module 2
   - The Module 2 toolkit works on the grid without any changes
   - `track_until_cross()` drives to the next intersection
   - Turns reorient the robot onto a perpendicular line

2. **Preview**: Next lesson we'll drive PAST intersections to reach ones further away

## Common Issues
- **Robot detects intersection immediately**: It's starting ON an intersection. Move it slightly past
- **Robot veers off the line**: Check sensor calibration. The grid lines must be the same tape as the circle
- **Robot doesn't stop at intersection**: Check threshold value — may need recalibration for new surface
- **Turn doesn't line up**: The robot needs to be centered on the intersection before turning

## Assessment
- Can the student explain why the toolkit works on the grid?
- Can the student drive to the first intersection and stop?
- Can the student add a turn after reaching the intersection?
