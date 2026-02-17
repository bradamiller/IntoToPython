# Lesson 5: Proportional Control with One Sensor

## Overview
Students transition from the "bounce driving" approach of Lessons 3-4 to smooth, continuous line following using proportional control. Instead of driving straight until hitting the line and then turning abruptly, the robot continuously adjusts its steering based on how far the sensor reading is from a target value (the setpoint). This is the students' first encounter with a real-time control loop -- a `while` loop that reads sensors and adjusts motors on every iteration.

## Learning Objectives
By the end of this lesson, students will be able to:
- Explain what a setpoint is and why it matters for line following
- Calculate error as the difference between a setpoint and a sensor reading
- Explain why error can be positive or negative and what each means
- Use `drivetrain.set_effort()` for continuous motor control inside a loop
- Implement a proportional control loop that follows the edge of a line
- Tune a proportional gain constant (Kp) by observing robot behavior

## Key Concepts
- **Setpoint**: The target sensor value the robot tries to maintain (the reading when perfectly on the edge of the line, approximately 0.5)
- **Error**: The difference between where the robot should be and where it actually is: `error = setpoint - sensor_reading`
- **Proportional gain (Kp)**: A constant that controls how strongly the robot reacts to error -- too high causes oscillation, too low causes sluggish response
- **Correction**: The steering adjustment applied to the motors: `correction = error * Kp`
- **Continuous control**: Using `set_effort()` inside a `while True` loop to constantly adjust the robot, rather than blocking calls like `straight()`
- **Base effort**: The forward speed the robot maintains while following the line

## Materials Required
- XRP Robot with reflectance sensors
- Taped circle on whiteboard material (from previous lessons)
- Computer with VS Code and XRPLib configured
- Whiteboard or projector for diagrams
- Sensor readings from Lesson 1 (edge value approximately 0.5)

## Lesson Flow

### Introduction (10 minutes)

1. **Hook: The Problem with Bounce Driving**
   - Recall Lessons 3-4: the robot drives straight, hits the line, turns, drives straight again
   - Ask: "Does the robot look smooth? Does it look like it is following the line?"
   - Show a video or demo of a smooth line-following robot (or describe it)
   - Key question: "How can the robot steer WHILE it is driving, instead of stopping to turn?"

2. **Introduce the Idea of Continuous Adjustment**
   - Analogy: Driving a car on a curved road -- you do not drive straight then jerk the wheel. You make tiny, constant adjustments.
   - The robot needs to do the same: constantly read the sensor and constantly adjust its steering.

3. **Introduce set_effort()**
   - In Lessons 1-4, we used `drivetrain.straight()` and `drivetrain.turn()` -- these are blocking calls. The robot finishes one before starting the next.
   - `drivetrain.set_effort(left, right)` sets both motors at once and does NOT block. The motors keep running at that effort until you change them.
   - Values range from -1 (full reverse) to 1 (full forward) for each motor.
   - This is the key to continuous control: call `set_effort()` inside a loop, and the robot can steer while driving.

4. **Quick Demo: set_effort() Basics**
   - Show this code on the board:
     ```python
     from XRPLib.differential_drive import DifferentialDrive
     from XRPLib.board import Board
     import time

     drivetrain = DifferentialDrive.get_default_differential_drive()
     board = Board.get_default_board()

     board.wait_for_button()

     # Drive straight for 2 seconds
     drivetrain.set_effort(0.5, 0.5)
     time.sleep(2)
     drivetrain.stop()
     ```
   - Ask: "What happens if left effort is higher than right?" (Turns right)
   - Ask: "What happens if right effort is higher than left?" (Turns left)

### Guided Practice: Building a Proportional Controller (20 minutes)

1. **Step 1: Review the Edge Reading**
   - Recall Lesson 1: students measured sensor values on white, on black, and on the edge
   - The edge reading is approximately 0.5 (halfway between white ~0.1 and black ~0.9)
   - This edge reading is our **setpoint** -- the value we want the sensor to stay at
   - Write on the board: `setpoint = 0.5`

2. **Step 2: Define Error**
   - Error tells us how far the robot is from where it should be:
     ```
     error = setpoint - sensor_reading
     ```
   - Walk through concrete examples on the board:

     | Situation | sensor_reading | error = 0.5 - sensor | Meaning |
     |---|---|---|---|
     | On the edge (perfect) | 0.5 | 0.0 | No correction needed |
     | Drifted onto white | 0.2 | +0.3 | Steer toward the line |
     | Drifted onto black | 0.8 | -0.3 | Steer away from the line |
     | Far onto white | 0.1 | +0.4 | Steer hard toward the line |
     | Far onto black | 0.9 | -0.4 | Steer hard away from the line |

   - Key insight: The sign of the error tells us which direction to correct. The size of the error tells us how much to correct.

3. **Step 3: Apply a Proportional Gain**
   - We do not use the raw error directly -- we multiply it by a gain constant called Kp:
     ```
     correction = error * Kp
     ```
   - Start with `Kp = 0.5`
   - Walk through the same examples:

     | error | Kp | correction = error * Kp |
     |---|---|---|
     | 0.0 | 0.5 | 0.0 (drive straight) |
     | +0.3 | 0.5 | +0.15 (steer toward line) |
     | -0.3 | 0.5 | -0.15 (steer away from line) |
     | +0.4 | 0.5 | +0.20 (steer harder toward line) |

4. **Step 4: Apply Correction to Motors**
   - We have a base effort for forward speed (e.g., 0.3)
   - We add the correction to one motor and subtract it from the other:
     ```
     left_effort  = base_effort + correction
     right_effort = base_effort - correction
     ```
   - When correction is positive: left speeds up, right slows down -- robot steers toward the line
   - When correction is negative: left slows down, right speeds up -- robot steers away from the line
   - When correction is zero: both motors run at base effort -- robot drives straight

5. **Step 5: Build the Complete Program**
   - Walk through the complete code line by line on the board:
     ```python
     from XRPLib.differential_drive import DifferentialDrive
     from XRPLib.reflectance import Reflectance
     from XRPLib.board import Board
     import time

     drivetrain = DifferentialDrive.get_default_differential_drive()
     reflectance = Reflectance.get_default_reflectance()
     board = Board.get_default_board()

     # Control settings
     setpoint = 0.5       # Target sensor value (edge of line)
     Kp = 0.5             # Proportional gain
     base_effort = 0.3    # Forward speed

     board.wait_for_button()

     while True:
         # Step 1: Read the sensor
         sensor_value = reflectance.get_left()

         # Step 2: Calculate error
         error = setpoint - sensor_value

         # Step 3: Calculate correction
         correction = error * Kp

         # Step 4: Apply to motors
         left_effort = base_effort + correction
         right_effort = base_effort - correction
         drivetrain.set_effort(left_effort, right_effort)

         # Small delay to avoid overloading the processor
         time.sleep(0.01)
     ```

6. **Step 6: Explain Each Part**
   - `while True:` -- this loop runs forever (or until we stop the program)
   - Every time through the loop: read sensor, calculate error, calculate correction, set motors
   - `time.sleep(0.01)` -- a tiny delay (10 milliseconds) to give the processor a brief rest
   - The robot is constantly adjusting -- this is the control loop

7. **Demo on the Robot**
   - Upload and run the program
   - Place the robot so the left sensor is on the edge of the taped circle
   - Press the button and observe
   - The robot should follow the edge of the circle smoothly
   - If it oscillates wildly: Kp is too high -- reduce it
   - If it drifts off the line: Kp is too low -- increase it

### Independent Practice (20 minutes)

**Exercise 1: Follow the Circle Edge**
- Goal: Get the robot to follow the edge of the taped circle using proportional control with one sensor
- Steps:
  1. Type in the complete program from the guided practice
  2. Place the robot with the left sensor on the edge of the circle
  3. Press the button and observe the behavior
  4. Add print statements to see what is happening:
     ```python
     while True:
         sensor_value = reflectance.get_left()
         error = setpoint - sensor_value
         correction = error * Kp
         left_effort = base_effort + correction
         right_effort = base_effort - correction
         drivetrain.set_effort(left_effort, right_effort)

         # Debug print -- see the values
         print(f"sensor={sensor_value:.2f} error={error:.2f} correction={correction:.2f}")

         time.sleep(0.01)
     ```
  5. Observe the printed values -- do they make sense?
- Success criteria: The robot follows the circle edge for at least one full lap without losing the line

**Exercise 2: Tune the Controller** (Challenge)
- Goal: Experiment with different values of Kp and base_effort to find the best combination
- Steps:
  1. Try `Kp = 0.3` -- what happens? (Robot responds more slowly, might drift off)
  2. Try `Kp = 1.0` -- what happens? (Robot oscillates, wiggles back and forth)
  3. Try `Kp = 0.7` -- is this better or worse?
  4. Try `base_effort = 0.2` -- robot goes slower but might be more stable
  5. Try `base_effort = 0.5` -- robot goes faster but might lose the line on tight curves
  6. Record your findings in a table:

     | Kp | base_effort | Behavior (smooth / oscillating / loses line) |
     |---|---|---|
     | 0.3 | 0.3 | |
     | 0.5 | 0.3 | |
     | 0.7 | 0.3 | |
     | 1.0 | 0.3 | |
     | 0.5 | 0.2 | |
     | 0.5 | 0.5 | |

  7. What combination works best for your robot and your circle?
- Success criteria: Student can explain how Kp and base_effort affect behavior and has found a working combination

### Assessment

**Formative (during lesson)**:
- Can students explain what a setpoint is and why 0.5 is a reasonable value?
- Can students calculate error given a sensor reading and setpoint?
- Can students predict which direction the robot will steer given a positive or negative error?
- Can students explain what happens when Kp is too high or too low?
- Does the robot successfully follow the circle edge?

**Summative (worksheet/exit ticket)**:
1. If the setpoint is 0.5 and the sensor reads 0.2, what is the error? What direction should the robot steer?
2. If Kp = 0.6 and error = 0.3, what is the correction value?
3. With base_effort = 0.3 and correction = 0.15, what are the left and right motor efforts?
4. Your robot is oscillating back and forth wildly. What should you change, and in which direction?

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "The robot should aim for sensor reading 0.0 (white)" | The robot follows the EDGE of the line, not the white surface. The setpoint is approximately 0.5 (the edge). |
| "A higher Kp is always better" | Too high a Kp causes oscillation. The best Kp is the one that gives smooth tracking without losing the line. |
| "Error is always positive" | Error can be negative (when the sensor is on the dark side of the line). The sign tells the direction of correction. |
| "set_effort() makes the robot move a certain distance" | set_effort() sets motor power levels continuously. It does not stop after a distance -- you must manage stopping yourself. |
| "The while loop runs once" | The while True loop runs continuously, reading and adjusting hundreds of times per second. |
| "We need an if/else to decide left or right" | Proportional control handles direction automatically through the sign of the error -- no if/else needed. |

## Differentiation

**For struggling students**:
- Provide the complete program and focus on understanding what each line does
- Use large print statements to make the sensor values visible
- Start with a slow base_effort (0.2) so the robot is easier to observe
- Work on a larger circle so curves are gentler
- Pair with a partner who can help with typing while they focus on understanding the math

**For advanced students**:
- Try following the line with the right sensor instead of the left -- what changes in the code?
- Add a counter that prints every 100 loops to see how fast the loop runs
- Research PID control -- what are the I (integral) and D (derivative) terms?
- Try to make the robot follow the line as FAST as possible without losing it
- Add code to stop the robot after a certain number of loops or elapsed time

## Materials & Code Examples

### Basic Proportional Line Follower (One Sensor)
```python
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.reflectance import Reflectance
from XRPLib.board import Board
import time

drivetrain = DifferentialDrive.get_default_differential_drive()
reflectance = Reflectance.get_default_reflectance()
board = Board.get_default_board()

# Control settings
setpoint = 0.5       # Target: edge of line
Kp = 0.5             # Proportional gain -- tune this!
base_effort = 0.3    # Forward speed

board.wait_for_button()

while True:
    # Read sensor
    sensor_value = reflectance.get_left()

    # Calculate error and correction
    error = setpoint - sensor_value
    correction = error * Kp

    # Apply to motors
    left_effort = base_effort + correction
    right_effort = base_effort - correction
    drivetrain.set_effort(left_effort, right_effort)

    time.sleep(0.01)
```

### Proportional Follower with Debug Output
```python
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.reflectance import Reflectance
from XRPLib.board import Board
import time

drivetrain = DifferentialDrive.get_default_differential_drive()
reflectance = Reflectance.get_default_reflectance()
board = Board.get_default_board()

setpoint = 0.5
Kp = 0.5
base_effort = 0.3

board.wait_for_button()

loop_count = 0

while True:
    sensor_value = reflectance.get_left()
    error = setpoint - sensor_value
    correction = error * Kp

    left_effort = base_effort + correction
    right_effort = base_effort - correction
    drivetrain.set_effort(left_effort, right_effort)

    # Print every 50 loops so output is readable
    loop_count = loop_count + 1
    if loop_count % 50 == 0:
        print(f"sensor={sensor_value:.2f}  error={error:.2f}  correction={correction:.2f}  L={left_effort:.2f}  R={right_effort:.2f}")

    time.sleep(0.01)
```

### Exploring set_effort() (Introductory Demo)
```python
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board
import time

drivetrain = DifferentialDrive.get_default_differential_drive()
board = Board.get_default_board()

board.wait_for_button()

# Drive straight
print("Driving straight...")
drivetrain.set_effort(0.3, 0.3)
time.sleep(2)

# Turn right (left motor faster)
print("Turning right...")
drivetrain.set_effort(0.4, 0.2)
time.sleep(2)

# Turn left (right motor faster)
print("Turning left...")
drivetrain.set_effort(0.2, 0.4)
time.sleep(2)

drivetrain.stop()
print("Done!")
```

## Teaching Notes
- **Start slow**: Use `base_effort = 0.3` or lower so students can observe and debug. Speed comes later.
- **The setpoint of 0.5 is approximate**: Each robot and each tape setup may have slightly different ideal edge readings. Encourage students to use their Lesson 1 calibration data.
- **Kp tuning is the fun part**: Let students experiment. The goal is not a perfect value but understanding the relationship between Kp and behavior.
- **Print throttling**: Printing every loop iteration will flood the console and slow down the robot. Show students how to print every Nth iteration using the modulo operator (`%`).
- **set_effort() does not clamp values**: If base_effort + correction exceeds 1.0 or goes below -1.0, the motor will be limited by hardware. This is fine for now but worth mentioning.
- **Common failure**: Robot drives off the line immediately. Check that the sensor is positioned on the edge of the line, and that the sign of the correction is correct for the sensor being used (left vs right).
- **This is a big conceptual leap**: Going from "do this, then do that" (sequential) to "constantly read and adjust" (control loop) is a significant shift. Be patient and use the car-steering analogy often.

## Connections to Next Lessons
- **Lesson 6** will extend this to use BOTH sensors, making the error calculation simpler and the tracking smoother
- **Lesson 7** will add intersection detection, where both sensors reading high signals a cross
- **Lesson 8** will wrap the sensor logic into a `LineSensor` class with methods like `get_error()` -- the same math from this lesson, organized into a reusable class
