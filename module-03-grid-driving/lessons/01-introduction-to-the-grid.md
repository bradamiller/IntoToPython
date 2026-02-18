# Lesson 1: Introduction to the Grid

## Overview
Students transition from the taped circle (Module 2) to a taped grid. They learn how the grid is organized as intersections connected by lines, and how the `LineTrack` class from Module 2 can be used without modification to navigate between intersections. Students practice driving to the first intersection and stopping — the fundamental building block for all grid navigation.

## Learning Objectives
By the end of this lesson, students will be able to:
- Describe the physical grid layout and how intersections are formed
- Explain how cross detection from Module 2 maps to grid intersections
- Use the `LineTrack` class to drive from one intersection to the next
- Place the robot on the grid and drive to the first intersection

## Key Concepts
- **Grid**: A network of taped lines forming rows and columns on the floor
- **Intersection**: Where two taped lines cross — detected by both sensors reading high
- **LineTrack reuse**: The same `track_until_cross()` method that detected the cross on the circle now detects grid intersections
- **Code reuse**: No new classes or methods needed — Module 2 code works directly on the grid

## Materials Required
- XRP Robot with reflectance sensors
- White surface with taped grid (at least 3×3 intersections)
- Working `LineSensor` and `LineTrack` classes from Module 2
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

3. **Review: What LineTrack Already Does**:
   - `track_until_cross()` — follows line, stops at intersection
   - `turn_right()` — turns right at an intersection onto the perpendicular line
   - `turn_left()` — turns left at an intersection onto the perpendicular line
   - These three methods are ALL you need for grid navigation!

### Guided Practice: Drive to First Intersection (15 minutes)

1. **Setup**:
   - Place the robot on the grid, centered on a line, behind an intersection
   - The robot should be facing along the line toward the next intersection

2. **The Program**:
   ```python
   from XRPLib.reflectance import Reflectance
   from XRPLib.differential_drive import DifferentialDrive
   from XRPLib.board import Board
   import time

   class LineSensor:
       def __init__(self):
           self.reflectance = Reflectance.get_default_reflectance()
           self.threshold = 0.5

       def get_left(self):
           return self.reflectance.get_left()

       def get_right(self):
           return self.reflectance.get_right()

       def get_error(self):
           return self.get_left() - self.get_right()

       def is_at_cross(self):
           return self.get_left() > self.threshold and self.get_right() > self.threshold

       def is_off_line(self):
           return self.get_left() < self.threshold and self.get_right() < self.threshold

   class LineTrack:
       def __init__(self):
           self.sensor = LineSensor()
           self.drivetrain = DifferentialDrive.get_default_differential_drive()
           self.base_effort = 0.4
           self.Kp = 0.5

       def track_until_cross(self):
           while not self.sensor.is_at_cross():
               error = self.sensor.get_error()
               left = self.base_effort - error * self.Kp
               right = self.base_effort + error * self.Kp
               self.drivetrain.set_effort(left, right)
           self.drivetrain.stop()

       def turn_right(self):
           self.drivetrain.set_effort(self.base_effort, self.base_effort)
           time.sleep(0.3)
           self.drivetrain.set_effort(0.3, -0.3)
           time.sleep(0.3)
           while self.sensor.is_off_line():
               pass
           self.drivetrain.stop()

       def turn_left(self):
           self.drivetrain.set_effort(self.base_effort, self.base_effort)
           time.sleep(0.3)
           self.drivetrain.set_effort(-0.3, 0.3)
           time.sleep(0.3)
           while self.sensor.is_off_line():
               pass
           self.drivetrain.stop()

   # --- Main Program ---
   board = Board.get_default_board()
   tracker = LineTrack()

   board.wait_for_button()
   print("Driving to first intersection...")
   tracker.track_until_cross()
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
     tracker.track_until_cross()
     print("Turning right...")
     tracker.turn_right()
     print("Now facing a new direction!")
     ```

### Wrap-Up (5 minutes)

1. **Key Takeaways**:
   - The grid is built from the same lines and crosses as Module 2
   - `LineTrack` works on the grid without any changes
   - `track_until_cross()` drives to the next intersection
   - Turns reorient the robot onto a perpendicular line

2. **Preview**: Next lesson we'll drive PAST intersections to reach ones further away

## Common Issues
- **Robot detects intersection immediately**: It's starting ON an intersection. Move it slightly past
- **Robot veers off the line**: Check sensor calibration. The grid lines must be the same tape as the circle
- **Robot doesn't stop at intersection**: Check threshold value — may need recalibration for new surface
- **Turn doesn't line up**: The robot needs to be centered on the intersection before turning

## Assessment
- Can the student explain why LineTrack works on the grid?
- Can the student drive to the first intersection and stop?
- Can the student add a turn after reaching the intersection?
