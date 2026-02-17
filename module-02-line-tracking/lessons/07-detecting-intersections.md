# Lesson 7: Detecting Intersections

## Overview
Students add intersection detection to their two-sensor line following from Lesson 6. A taped cross (perpendicular line) is added to the circle. When both sensors detect the line simultaneously, the robot knows it has reached an intersection. Students program the robot to follow the circle, detect the cross, turn around, and continue in the opposite direction — a preview of the final project behavior.

## Learning Objectives
By the end of this lesson, students will be able to:
- Explain what an intersection looks like to the robot's two sensors
- Write a condition that detects when both sensors are on the line
- Use logical operators (`and`, `or`, `not`) to combine conditions
- Integrate intersection detection with line following in a single program
- Program the robot to respond to intersection detection (stop, turn, etc.)
- Distinguish between normal line following and intersection events

## Key Concepts
- **Intersection**: A point where two lines cross — both sensors read high simultaneously
- **`and` operator**: Both conditions must be True: `left > 0.5 and right > 0.5`
- **`or` operator**: At least one condition must be True
- **`not` operator**: Reverses a boolean — `not True` equals `False`
- **Event detection**: Checking for a specific condition inside a continuous loop
- **State change**: The moment both sensors go from "following" to "intersection detected"

## Materials Required
- XRP Robot with reflectance sensors
- White surface with taped circle AND a taped cross (perpendicular line crossing the circle)
- VS Code with XRPLib installed
- Working two-sensor line following code from Lesson 6

## Lesson Flow

### Introduction (10 minutes)

1. **Hook: Adding the Cross**:
   - Show the circle with the new taped cross
   - Ask: "What will happen when the robot reaches this intersection while following the line?"
   - "Both sensors will be on the line at the same time — that's our signal!"

2. **How Two Sensors See an Intersection**:
   - During normal line following:
     - One sensor is on the line, the other is off, or both are partially on
     - `left` and `right` have different values
   - At an intersection (cross):
     - BOTH sensors are on the line
     - `left > threshold AND right > threshold`
   - This is how we detect the cross!

3. **Logical Operators**:
   - `and`: Both must be True → `left > 0.5 and right > 0.5`
   - `or`: At least one must be True → `left > 0.5 or right > 0.5`
   - `not`: Reverses → `not (left > 0.5)` is True when left ≤ 0.5
   - Students already saw `or` in Lesson 3. Now we use `and`.

### Guided Practice: Detecting the Cross (20 minutes)

1. **Simple Cross Detection Test**:
   ```python
   from XRPLib.reflectance import Reflectance
   from XRPLib.differential_drive import DifferentialDrive
   from XRPLib.board import Board
   import time

   reflectance = Reflectance.get_default_reflectance()
   drivetrain = DifferentialDrive.get_default_differential_drive()
   board = Board.get_default_board()

   threshold = 0.5

   board.wait_for_button()
   print("Watching for intersection...")

   while True:
       left = reflectance.get_left()
       right = reflectance.get_right()

       if left > threshold and right > threshold:
           print("CROSS DETECTED! Left:", left, "Right:", right)
       else:
           print("Normal - Left:", left, "Right:", right)
       time.sleep(0.2)
   ```
   - Manually slide the robot across the cross to test detection

2. **Combining Line Following + Cross Detection**:
   ```python
   from XRPLib.reflectance import Reflectance
   from XRPLib.differential_drive import DifferentialDrive
   from XRPLib.board import Board
   import time

   reflectance = Reflectance.get_default_reflectance()
   drivetrain = DifferentialDrive.get_default_differential_drive()
   board = Board.get_default_board()

   threshold = 0.5
   Kp = 0.5
   base_effort = 0.3

   board.wait_for_button()
   print("Following line, looking for cross...")

   while True:
       left = reflectance.get_left()
       right = reflectance.get_right()

       # Check for intersection
       if left > threshold and right > threshold:
           # Cross detected! Stop and turn around
           drivetrain.stop()
           print("Cross detected! Turning around...")
           drivetrain.turn(180)
           print("Resuming line following...")
           time.sleep(0.3)  # Brief pause to get past the cross
       else:
           # Normal line following
           error = left - right
           left_effort = base_effort - error * Kp
           right_effort = base_effort + error * Kp
           drivetrain.set_effort(left_effort, right_effort)
   ```

3. **Explain the Logic**:
   - The `if` checks for intersection FIRST
   - If no intersection, the `else` does normal line following
   - `time.sleep(0.3)` after turning prevents immediately re-detecting the cross
   - The robot follows the circle, hits the cross, turns around, follows back

4. **Demo & Test**:
   - Place robot on the circle near (but not on) the cross
   - Run the program
   - Robot should follow the line, detect the cross, turn 180°, and follow back

### Independent Practice (20 minutes)

**Exercise 1: Follow and Reverse at the Cross**
- Goal: Robot follows the circle, detects the cross, turns around, continues
- Use the guided practice code as a starting point
- Success criteria:
  - [ ] Robot follows the circle smoothly
  - [ ] Robot detects the cross and stops
  - [ ] Robot turns 180° and resumes following
  - [ ] Robot completes at least 2 reversals

**Exercise 2: Count Crossings** (Challenge)
- Goal: Count how many times the robot crosses the intersection and stop after a specific number
  ```python
  cross_count = 0
  max_crosses = 4

  board.wait_for_button()

  while cross_count < max_crosses:
      left = reflectance.get_left()
      right = reflectance.get_right()

      if left > threshold and right > threshold:
          cross_count = cross_count + 1
          drivetrain.stop()
          print("Cross #", cross_count, "detected!")
          drivetrain.turn(180)
          time.sleep(0.3)
      else:
          error = left - right
          left_effort = base_effort - error * Kp
          right_effort = base_effort + error * Kp
          drivetrain.set_effort(left_effort, right_effort)

  drivetrain.stop()
  print("Done! Crossed", cross_count, "times.")
  ```
- This previews the final project behavior!

### Assessment

**Formative (during lesson)**:
- Can students explain what both sensors reading high means?
- Do they understand the `and` operator?
- Can they integrate detection with following?

**Summative (worksheet/exit ticket)**:
1. Write a condition that is True when both sensors read above 0.5
2. What is the difference between `and` and `or`?
3. Why do we need `time.sleep(0.3)` after turning at the cross?

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "The robot detects the cross automatically" | You must write code to check for it — the robot only knows what you tell it to check |
| "`and` means either one" | `and` means BOTH must be True; `or` means at least one |
| "The cross detection works instantly" | The robot may briefly see both sensors high even on a curve — tuning may be needed |
| "I need a separate loop for cross detection" | Cross detection goes inside the same while loop as line following |
| "After turning, the robot won't find the line" | The turn should bring the robot back to the line edge; `time.sleep()` helps skip past the cross |

## Differentiation

**For struggling students**:
- Provide complete code; focus on understanding the cross detection condition
- Manually test cross detection first (no driving) to build confidence
- Use large, clear intersection tape to make detection easier

**For advanced students**:
- Instead of turning 180°, turn 90° to take the perpendicular path
- Add different behaviors for different cross counts (first cross: beep, second: blink, etc.)
- Handle "false positives" — what if both sensors briefly go high on a tight curve?

## Materials & Code Examples

### Complete Follow-and-Reverse Program
```python
from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board
import time

reflectance = Reflectance.get_default_reflectance()
drivetrain = DifferentialDrive.get_default_differential_drive()
board = Board.get_default_board()

threshold = 0.5
Kp = 0.5
base_effort = 0.3
cross_count = 0

board.wait_for_button()
print("Line following with cross detection...")

while True:
    left = reflectance.get_left()
    right = reflectance.get_right()

    if left > threshold and right > threshold:
        drivetrain.stop()
        cross_count = cross_count + 1
        print("Cross #", cross_count, "- Turning around!")
        drivetrain.turn(180)
        time.sleep(0.3)
    else:
        error = left - right
        left_effort = base_effort - error * Kp
        right_effort = base_effort + error * Kp
        drivetrain.set_effort(left_effort, right_effort)
```

## Teaching Notes
- **Physical setup**: The taped cross should be wide enough that both sensors clearly detect it. A thin cross may be missed.
- **False positives**: On tight curves, both sensors may briefly read high. If this happens, add a small delay after entering the `if` and recheck.
- **`time.sleep()` importance**: Without the sleep after turning, the robot may re-detect the cross before moving away from it.
- **This is the integration lesson**: This brings together while loops, if/else, sensors, and motor control — all concepts from Lessons 1–6.

## Connections to Next Lessons
- **Lesson 8** will package the sensor logic into a `LineSensor` class with `is_at_cross()` method
- **Lesson 9** will package the driving logic into a `LineTrack` class with `track_until_cross()` method
- **Lesson 10** (final project) uses both classes to do exactly what we did here, but with cleaner, reusable code
