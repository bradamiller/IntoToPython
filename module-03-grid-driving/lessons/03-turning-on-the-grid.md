# Lesson 3: Turning on the Grid

## Overview
Students combine driving multiple intersections with turning at intersections. They learn to sequence drive-and-turn operations to navigate an L-shaped path on the grid. This prepares them for the final project where they'll drive a complete square pattern.

## Learning Objectives
By the end of this lesson, students will be able to:
- Sequence drive and turn operations on the grid
- Use `turn_right()` and `turn_left()` at intersections
- Navigate an L-shaped path (drive forward, turn, drive forward)
- Plan a path on the grid before writing code

## Key Concepts
- **Turn at intersection**: The robot must be at an intersection to turn onto a perpendicular line
- **Sequencing**: Alternating between driving (line following) and turning
- **Path planning**: Deciding the sequence of drives and turns before coding
- **Clearing after turns**: After turning, the robot is already past the intersection — no clearing needed

## Materials Required
- XRP Robot with reflectance sensors
- White surface with taped grid (at least 4×4 intersections)
- Working `LineSensor` and `LineTrack` classes from Module 2
- VS Code with XRPLib installed

## Lesson Flow

### Introduction (10 minutes)

1. **Hook: Navigating a Corner**:
   - Ask: "How do you turn a corner when walking on city streets?"
   - Walk to the intersection, then turn
   - Same for the robot: drive to intersection, turn, then continue driving

2. **The Sequence**:
   - Drive forward N intersections
   - Turn right (or left) at the current intersection
   - Drive forward M intersections
   - This creates an "L" shaped path!

3. **Review: turn_right() and turn_left()**:
   - Both methods from `LineTrack` class:
     - Drive forward briefly to clear the intersection
     - Start spinning in the desired direction
     - Stop when sensors find the perpendicular line
   - The turn clears the intersection automatically — no extra clearing needed after turning!

### Guided Practice: The L-Shape (15 minutes)

1. **Drive 2 intersections, turn right, drive 2 intersections**:
   ```python
   board = Board.get_default_board()
   tracker = LineTrack()

   board.wait_for_button()
   print("Starting L-shape path!")

   # Drive forward 2 intersections
   print("Leg 1: Driving 2 intersections forward...")
   tracker.track_until_cross()
   tracker.drivetrain.set_effort(0.3, 0.3)
   time.sleep(0.3)
   tracker.track_until_cross()
   print("At intersection - turning right...")

   # Turn right
   tracker.turn_right()
   print("Turn complete!")

   # Drive forward 2 more intersections
   print("Leg 2: Driving 2 intersections forward...")
   tracker.track_until_cross()
   tracker.drivetrain.set_effort(0.3, 0.3)
   time.sleep(0.3)
   tracker.track_until_cross()

   print("L-shape complete!")
   ```

2. **Discussion Points**:
   - After `turn_right()`, we DON'T need to clear — the turn already moves past the intersection
   - We go straight into `track_until_cross()` after the turn
   - The robot is now driving along the perpendicular line

3. **Using the drive_intersections function from Lesson 2**:
   ```python
   def drive_intersections(tracker, count):
       for i in range(count):
           tracker.track_until_cross()
           if i < count - 1:
               tracker.drivetrain.set_effort(0.3, 0.3)
               time.sleep(0.3)

   board.wait_for_button()

   drive_intersections(tracker, 2)  # Drive forward 2
   tracker.turn_right()             # Turn right
   drive_intersections(tracker, 2)  # Drive forward 2

   print("L-shape complete!")
   ```

### Independent Practice (15 minutes)

1. **Exercise 1: L-shape with turn_left**:
   - Drive 2 intersections, turn LEFT, drive 1 intersection
   - Verify the robot follows the expected L-shape

2. **Exercise 2: U-turn path**:
   - Drive 3 intersections forward
   - Turn right
   - Turn right (two right turns = 180°? Not quite — need to drive between them!)
   - Actually: drive 3, turn right, drive 1, turn right, drive 3

3. **Exercise 3: Plan your own path**:
   - Draw the path on paper first
   - Mark how many intersections for each leg
   - Mark the turns
   - Write the code to match your plan

### Wrap-Up (5 minutes)

1. **Key Takeaways**:
   - Turn at intersections — the robot must be at a cross to turn
   - After turning, continue driving — no clearing needed
   - Plan the path on paper before coding
   - Any path on the grid is just a sequence of drives and turns

2. **Preview**: Next lesson — the final project: driving a complete square!

## Common Issues
- **Robot turns but doesn't find the line**: The perpendicular line may be too far. Check grid spacing and `turn_right()` timing
- **Robot goes the wrong direction after turning**: Verify which turn method you used (right vs. left)
- **Robot counts wrong intersections after turning**: Make sure you're not trying to clear after the turn
- **Path doesn't match the plan**: Add print statements between each step to trace the robot's progress

## Assessment
- Can the student sequence drives and turns correctly?
- Can the student navigate an L-shaped path?
- Can the student plan a path on paper and translate it to code?
