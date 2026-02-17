# Lesson 6: Two-Sensor Line Following

## Overview
Students upgrade from single-sensor edge following to using both the left and right reflectance sensors together. The error calculation becomes simpler and more intuitive: `error = left - right`. When both sensors see the same thing, error is zero and the robot drives straight. When one sensor drifts onto the line, the difference tells the robot exactly how much and which direction to steer. This approach follows the CENTER of the line rather than its edge, giving smoother and more reliable tracking.

## Learning Objectives
By the end of this lesson, students will be able to:
- Explain why two sensors are better than one for line following
- Calculate error using two sensor values: `error = left - right`
- Predict the sign and magnitude of the error for different robot positions
- Implement a two-sensor proportional control loop
- Compare the smoothness of one-sensor vs. two-sensor line following
- Apply the corrected motor effort formula: `left = base - error * Kp`, `right = base + error * Kp`

## Key Concepts
- **Differential sensing**: Using the difference between two sensors to determine position relative to the line
- **Two-sensor error**: `error = reflectance.get_left() - reflectance.get_right()` -- positive means left is on the line, negative means right is on the line
- **Center tracking**: Two sensors straddle the line, keeping the robot centered rather than following one edge
- **Symmetric correction**: The correction is applied oppositely to each motor, creating a differential steering effect
- **No setpoint needed**: With two sensors, the setpoint is implicit -- when both sensors read the same value, error is zero

## Materials Required
- XRP Robot with reflectance sensors
- Taped circle on whiteboard material (from previous lessons)
- Computer with VS Code and XRPLib configured
- Whiteboard or projector for diagrams
- Working Lesson 5 code for comparison

## Lesson Flow

### Introduction (10 minutes)

1. **Hook: Limitations of One Sensor**
   - Recall Lesson 5: one sensor follows the edge of the line
   - Ask: "What happens if the robot drifts completely off the line? Can one sensor tell which side it is on?"
   - Answer: No -- if the sensor reads low (white), the robot does not know if it drifted left or right off the line
   - Ask: "What if we used BOTH sensors?"

2. **The Two-Sensor Idea**
   - Draw on the board: a line with two sensors straddling it
   - The robot is positioned so the line runs between the two sensors
   - When centered: both sensors are partially on the line, reading similar values
   - When drifting left: left sensor moves onto the line (high), right stays on white (low)
   - When drifting right: right sensor moves onto the line (high), left stays on white (low)

3. **The New Error Formula**
   - With one sensor (Lesson 5): `error = setpoint - sensor_reading`
   - With two sensors: `error = reflectance.get_left() - reflectance.get_right()`
   - No setpoint is needed! The difference between the sensors tells us everything.
   - Walk through the logic:
     - Both on white: `error = low - low = ~0` (go straight)
     - Left on line, right on white: `error = high - low = positive` (steer left)
     - Right on line, left on white: `error = low - high = negative` (steer right)

4. **Why This is Better**
   - With one sensor, the robot follows the EDGE -- it can only see one side
   - With two sensors, the robot follows the CENTER -- it can see both sides
   - The correction is automatically symmetric: the bigger the drift, the bigger the correction
   - Result: smoother, more reliable tracking

### Guided Practice: Building a Two-Sensor Controller (15 minutes)

1. **Step 1: Explore Sensor Readings in Pairs**
   - Before writing the control loop, read and print both sensors:
     ```python
     from XRPLib.reflectance import Reflectance
     from XRPLib.board import Board
     import time

     reflectance = Reflectance.get_default_reflectance()
     board = Board.get_default_board()

     board.wait_for_button()

     while True:
         left = reflectance.get_left()
         right = reflectance.get_right()
         error = left - right
         print(f"left={left:.2f}  right={right:.2f}  error={error:.2f}")
         time.sleep(0.2)
     ```
   - Students manually move the robot across the line and observe how error changes
   - Key observations:
     - Both on white: error near 0
     - Left on line: error is positive (e.g., +0.5 to +0.7)
     - Right on line: error is negative (e.g., -0.5 to -0.7)
     - Both on line: error near 0 (this will matter in Lesson 7)

2. **Step 2: Build the Error Table on the Board**

   | Position | left reading | right reading | error = left - right | Meaning |
   |---|---|---|---|---|
   | Centered on line | 0.5 | 0.5 | 0.0 | Drive straight |
   | Drifted left | 0.8 | 0.2 | +0.6 | Steer left to correct |
   | Drifted right | 0.2 | 0.8 | -0.6 | Steer right to correct |
   | Both on white | 0.1 | 0.1 | 0.0 | Drive straight (lost line) |
   | Both on black | 0.9 | 0.9 | 0.0 | Drive straight (intersection!) |

3. **Step 3: Apply the Correction**
   - The correction formula for two sensors:
     ```python
     left_effort  = base_effort - error * Kp
     right_effort = base_effort + error * Kp
     ```
   - Note the signs are REVERSED from Lesson 5. This is because:
     - When error is positive (left sensor on line), we need to steer left
     - Steering left means slowing the LEFT motor and speeding up the RIGHT motor
     - So: left gets MINUS correction, right gets PLUS correction

4. **Step 4: Build the Complete Program**
   - Walk through line by line:
     ```python
     from XRPLib.differential_drive import DifferentialDrive
     from XRPLib.reflectance import Reflectance
     from XRPLib.board import Board
     import time

     drivetrain = DifferentialDrive.get_default_differential_drive()
     reflectance = Reflectance.get_default_reflectance()
     board = Board.get_default_board()

     # Control settings
     Kp = 0.5             # Proportional gain -- tune this
     base_effort = 0.3    # Forward speed

     board.wait_for_button()

     while True:
         # Read both sensors
         left_sensor = reflectance.get_left()
         right_sensor = reflectance.get_right()

         # Calculate error: positive = drifted left, negative = drifted right
         error = left_sensor - right_sensor

         # Apply correction
         left_effort = base_effort - error * Kp
         right_effort = base_effort + error * Kp
         drivetrain.set_effort(left_effort, right_effort)

         time.sleep(0.01)
     ```

5. **Step 5: Compare with One-Sensor Version**
   - Show both versions side by side on the board:

   **One sensor (Lesson 5):**
   ```python
   sensor_value = reflectance.get_left()
   error = setpoint - sensor_value
   left_effort = base_effort + error * Kp
   right_effort = base_effort - error * Kp
   ```

   **Two sensors (this lesson):**
   ```python
   error = reflectance.get_left() - reflectance.get_right()
   left_effort = base_effort - error * Kp
   right_effort = base_effort + error * Kp
   ```

   - Key differences: no setpoint needed, signs are different, uses both sensors

6. **Demo on the Robot**
   - Upload and run on the taped circle
   - Place the robot so the line runs between the two sensors
   - The robot should follow the center of the line smoothly
   - Compare to Lesson 5: does it look smoother?

### Independent Practice (20 minutes)

**Exercise 1: Two-Sensor Line Following**
- Goal: Get the robot to follow the taped circle using both sensors
- Steps:
  1. Type in the complete two-sensor program
  2. Position the robot so the line is between the two sensors
  3. Press the button and observe
  4. Add debug output to see the values:
     ```python
     loop_count = 0

     while True:
         left_sensor = reflectance.get_left()
         right_sensor = reflectance.get_right()
         error = left_sensor - right_sensor

         left_effort = base_effort - error * Kp
         right_effort = base_effort + error * Kp
         drivetrain.set_effort(left_effort, right_effort)

         loop_count = loop_count + 1
         if loop_count % 50 == 0:
             print(f"L={left_sensor:.2f} R={right_sensor:.2f} err={error:.2f} Lm={left_effort:.2f} Rm={right_effort:.2f}")

         time.sleep(0.01)
     ```
  5. Watch the error values -- do they stay close to 0?
- Success criteria: Robot completes at least one full lap of the circle smoothly

**Exercise 2: Compare One Sensor vs. Two Sensors** (Challenge)
- Goal: Run both versions on the same circle and observe the difference
- Steps:
  1. Run the Lesson 5 (one-sensor) program and observe the robot
  2. Run the Lesson 6 (two-sensor) program and observe
  3. Answer these questions:
     - Which version looks smoother? Why?
     - Which version loses the line less often? Why?
     - Which version handles the curved parts of the circle better?
  4. Try increasing base_effort to 0.4 or 0.5 with both versions -- which one handles the higher speed better?
- Success criteria: Student can articulate why two sensors provide more information and better tracking than one sensor

### Assessment

**Formative (during lesson)**:
- Can students explain why two sensors are better than one?
- Can students predict the sign of the error given a robot position?
- Can students explain why the signs in the motor formula are reversed from Lesson 5?
- Does the robot successfully follow the circle?

**Summative (worksheet/exit ticket)**:
1. If the left sensor reads 0.8 and the right sensor reads 0.2, what is the error? Which direction should the robot steer?
2. If the left sensor reads 0.1 and the right sensor reads 0.7, what is the error? Which direction should the robot steer?
3. If both sensors read 0.9, what is the error? What might this situation mean physically?
4. Why does the two-sensor approach not need a setpoint?

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "Two sensors should each have their own control loop" | Both sensors feed into ONE error calculation: `error = left - right`. There is one control loop. |
| "The signs in the motor formula should be the same as Lesson 5" | The signs are reversed because the meaning of error changed. In Lesson 5, positive error meant steer one way; here, positive error means the opposite. |
| "If both sensors read the same value, the robot is lost" | If both read similar values, the robot is centered on the line (or both off it). An error near zero means drive straight. |
| "This approach uses a setpoint of 0" | There is no setpoint variable. The difference between sensors IS the error. When both sensors match, the difference is naturally zero. |
| "Two sensors means twice the code" | The code is actually simpler -- one subtraction replaces the setpoint calculation. |

## Differentiation

**For struggling students**:
- Provide the complete program and focus on manually moving the robot over the line to see how the error changes
- Use the sensor-reading print program (Step 1) extensively before moving to the control loop
- Focus on the intuition: "left sensor high means drift left, right sensor high means drift right"
- Provide a reference card with the formula and sign meanings

**For advanced students**:
- Implement a "speed boost" on straight sections: when error is near zero for many iterations, increase base_effort
- Add an average or running total of error over time -- does it correlate with how well the robot tracks?
- Try following the line at maximum speed -- what Kp works best at high speed vs. low speed?
- Research how industrial robots use differential sensors for positioning

## Materials & Code Examples

### Sensor Reading Explorer
```python
from XRPLib.reflectance import Reflectance
from XRPLib.board import Board
import time

reflectance = Reflectance.get_default_reflectance()
board = Board.get_default_board()

board.wait_for_button()

while True:
    left = reflectance.get_left()
    right = reflectance.get_right()
    error = left - right
    print(f"left={left:.2f}  right={right:.2f}  error={error:.2f}")
    time.sleep(0.2)
```

### Two-Sensor Proportional Line Follower
```python
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.reflectance import Reflectance
from XRPLib.board import Board
import time

drivetrain = DifferentialDrive.get_default_differential_drive()
reflectance = Reflectance.get_default_reflectance()
board = Board.get_default_board()

# Control settings
Kp = 0.5             # Proportional gain -- tune this
base_effort = 0.3    # Forward speed

board.wait_for_button()

while True:
    # Read both sensors
    left_sensor = reflectance.get_left()
    right_sensor = reflectance.get_right()

    # Calculate error
    error = left_sensor - right_sensor

    # Apply correction
    left_effort = base_effort - error * Kp
    right_effort = base_effort + error * Kp
    drivetrain.set_effort(left_effort, right_effort)

    time.sleep(0.01)
```

### Two-Sensor Follower with Debug Output
```python
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.reflectance import Reflectance
from XRPLib.board import Board
import time

drivetrain = DifferentialDrive.get_default_differential_drive()
reflectance = Reflectance.get_default_reflectance()
board = Board.get_default_board()

Kp = 0.5
base_effort = 0.3

board.wait_for_button()

loop_count = 0

while True:
    left_sensor = reflectance.get_left()
    right_sensor = reflectance.get_right()
    error = left_sensor - right_sensor

    left_effort = base_effort - error * Kp
    right_effort = base_effort + error * Kp
    drivetrain.set_effort(left_effort, right_effort)

    loop_count = loop_count + 1
    if loop_count % 50 == 0:
        print(f"L={left_sensor:.2f}  R={right_sensor:.2f}  err={error:.2f}  Lm={left_effort:.2f}  Rm={right_effort:.2f}")

    time.sleep(0.01)
```

## Teaching Notes
- **Sensor placement matters**: The two sensors should straddle the line. If the line is very thin or the sensors are too far apart, the robot may not see the line with both sensors simultaneously. Adjust tape width or robot position as needed.
- **The sign reversal is confusing**: Spend time on WHY `left_effort = base - error * Kp` instead of `base + error * Kp`. Draw it on the board: if the left sensor sees the line (positive error), the robot has drifted left, so it needs to steer right, which means slow the left motor.
- **Start with the explorer program**: Having students manually slide the robot over the line while watching sensor values print is very effective. They see the error go positive, negative, and zero in real time.
- **Both sensors high**: Point out the last row of the error table -- both sensors reading high gives error near 0. This is ambiguous: the robot might be centered, or it might be at an intersection. Lesson 7 will address this.
- **Kp may need re-tuning**: The Kp that worked in Lesson 5 may not be optimal here. The error values have a different range, so encourage students to tune again.
- **Success is visible**: Two-sensor following should look noticeably smoother than one-sensor following. Make sure to run both and compare.

## Connections to Next Lessons
- **Lesson 7** will add intersection detection: when BOTH sensors read high, the robot has reached a cross
- **Lesson 8** will wrap `get_left() - get_right()` into a `LineSensor` class method called `get_error()`
- The two-sensor approach becomes the standard method for all future line following in the course
