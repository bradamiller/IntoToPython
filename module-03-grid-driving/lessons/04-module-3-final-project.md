# Lesson 4: Module 3 Final Project — Square Pattern

## Overview
Students integrate driving multiple intersections and turning to create a complete square pattern on the grid. The robot drives 2 intersections forward, turns right, and repeats 4 times — returning to its starting position. This demonstrates the power of loops, code reuse, and sequential programming on a physical grid.

## Learning Objectives
By the end of this lesson, students will be able to:
- Design a complete program that navigates a square pattern on the grid
- Use a `for` loop to repeat drive-and-turn sequences
- Debug and refine a program running on physical hardware
- Verify the robot returns to its starting position

## Key Concepts
- **Square pattern**: Drive N intersections, turn right — repeat 4 times
- **Loop structure**: One iteration = one side of the square
- **Closed path**: The robot should end where it started
- **Hardware debugging**: Adjusting timing, speed, and placement for reliable operation

## Materials Required
- XRP Robot with reflectance sensors
- White surface with taped grid (at least 4×4 intersections)
- Working `LineSensor` and `LineTrack` classes from Module 2
- VS Code with XRPLib installed

## Lesson Flow

### Introduction (5 minutes)

1. **The Challenge**:
   - "Your mission: make the robot drive a perfect square on the grid"
   - Each side = 2 intersections
   - 4 sides, 4 right turns
   - Robot should end up back where it started

2. **Planning the Square**:
   - Draw the square on paper
   - Label each side with the number of intersections
   - Mark each turn
   - One iteration of the loop = one side + one turn

### Project Requirements (5 minutes)

**The program must:**
1. Use the `LineTrack` class from Module 2
2. Drive a square pattern (2 intersections per side)
3. Use a `for` loop for the 4 repetitions
4. Print progress messages (which leg, which intersection)
5. Return to the starting position

**Grading rubric:**

| Category | Points |
|---|---|
| Code uses LineTrack class correctly | 10 |
| Square uses for loop (not copy-paste) | 10 |
| Robot completes all 4 sides | 10 |
| Robot returns to starting position | 10 |
| Print statements show progress | 5 |
| Code is readable and organized | 5 |
| **Total** | **50** |

### Guided Start (10 minutes)

1. **Starter Code Structure**:
   ```python
   from XRPLib.reflectance import Reflectance
   from XRPLib.differential_drive import DifferentialDrive
   from XRPLib.board import Board
   import time

   # --- LineSensor class (from Module 2) ---
   class LineSensor:
       # ... (copy from Module 2)

   # --- LineTrack class (from Module 2) ---
   class LineTrack:
       # ... (copy from Module 2)

   # --- Helper function ---
   def drive_intersections(tracker, count):
       for i in range(count):
           tracker.track_until_cross()
           if i < count - 1:
               tracker.drivetrain.set_effort(0.3, 0.3)
               time.sleep(0.3)

   # --- Main Program ---
   board = Board.get_default_board()
   tracker = LineTrack()

   board.wait_for_button()
   print("Module 3 Final Project - Square Pattern!")

   sides = 2  # intersections per side

   for leg in range(4):
       print("Side", leg + 1, "of 4")
       drive_intersections(tracker, sides)
       print("  Turning right...")
       tracker.turn_right()

   print("Square complete! Back at start.")
   ```

2. **Walk Through**: Each loop iteration:
   - Drives forward 2 intersections
   - Turns right at the last intersection
   - The turn leaves the robot ready for the next side

### Implementation and Testing (20 minutes)

1. **Step 1: Test one side**
   - Comment out the for loop, just run one side + turn
   - Verify the robot drives 2 intersections and turns

2. **Step 2: Test two sides**
   - Change range to 2
   - Verify the robot makes an L-shape (half the square)

3. **Step 3: Full square**
   - Change range to 4
   - Does the robot return to start?

4. **Debugging Tips**:
   - If the robot doesn't return to start, check if turns are exactly 90°
   - If the robot skips an intersection, slow down or adjust clearing time
   - If the robot veers after turning, check that `turn_right()` finds the line properly
   - Add `time.sleep(0.5)` between sides if the robot needs a pause

### Extension Challenges (if time permits)

1. **Challenge A: Bigger Square**
   - Change `sides` to 3 — drive a larger square
   - Does the robot still return to start?

2. **Challenge B: Rectangle**
   - Alternate between 2 and 3 intersections per side:
     ```python
     lengths = [2, 3, 2, 3]
     for leg in range(4):
         drive_intersections(tracker, lengths[leg])
         tracker.turn_right()
     ```

3. **Challenge C: Left-Turn Square**
   - Use `turn_left()` instead of `turn_right()`
   - The robot drives the square in the opposite direction

4. **Challenge D: Double Loop**
   - Drive the square twice without stopping
   - Use `range(8)` with alternating drives and turns

### Wrap-Up and Reflection (5 minutes)

1. **Reflection Questions**:
   - What was the hardest part of getting the square to work?
   - Why is the for loop important (vs. copy-pasting code)?
   - What would you need to change to make a triangle? (Hint: different turn angle)
   - How is this different from the polygon function in Module 1?

2. **Module 3 Summary**:
   - You reused the `LineTrack` class from Module 2 on a new surface (the grid)
   - You learned to clear intersections and drive multiple segments
   - You sequenced drives and turns to navigate complex paths
   - No new Python concepts — just putting existing tools to work!

3. **Looking Ahead to Module 4**:
   - Module 3: YOU decide the path (hardcoded drives and turns)
   - Module 4: The COMPUTER calculates the path (Manhattan algorithm)
   - "What if you could just say 'go to row 2, column 3' and the robot figures out how?"

## Common Issues
- **Robot doesn't complete the square**: Usually a turning or clearing issue. Test one side at a time.
- **Robot ends up in the wrong place**: Turns aren't exactly 90°. Adjust `turn_right()` timing.
- **Robot skips intersections**: Going too fast. Reduce `base_effort` or add delay.
- **Code too long**: Make sure you're using a for loop, not duplicating code 4 times.

## Assessment
Students demonstrate mastery by:
1. Code uses a for loop for the 4 sides
2. Robot drives 2 intersections per side
3. Robot turns right at each corner
4. Robot returns approximately to its starting position
5. Print statements track progress through the square
