# Lesson 5 Worksheet: Proportional Control with One Sensor

**Name:** __________________ **Date:** __________________ **Team:** __________________

## Part 1: Vocabulary Matching

Match each term to its definition.

| Term | Definition |
|---|---|
| Setpoint | A) The motor power level the robot uses for forward speed |
| Error | B) A constant that controls how strongly the robot reacts |
| Kp | C) The target sensor value the robot tries to maintain |
| Correction | D) The difference between the setpoint and the actual sensor reading |
| Base effort | E) The steering adjustment applied to the motors |

Setpoint = _____ Error = _____ Kp = _____ Correction = _____ Base effort = _____

## Part 2: Understanding Error

The setpoint is 0.5. Calculate the error for each sensor reading.

**Formula:** `error = setpoint - sensor_reading`

| sensor_reading | error = 0.5 - sensor_reading | Robot is on... |
|---|---|---|
| 0.5 | _________ | The edge (perfect) |
| 0.1 | _________ | White / Black (circle one) |
| 0.3 | _________ | White / Black (circle one) |
| 0.7 | _________ | White / Black (circle one) |
| 0.9 | _________ | White / Black (circle one) |

**When error is positive, the robot should steer:** toward the line / away from the line (circle one)

**When error is negative, the robot should steer:** toward the line / away from the line (circle one)

## Part 3: Calculating Correction

Use `correction = error * Kp` to fill in the table.

**Kp = 0.5:**

| error | correction = error * 0.5 |
|---|---|
| +0.4 | _________ |
| +0.2 | _________ |
| 0.0 | _________ |
| -0.2 | _________ |
| -0.4 | _________ |

**Now try Kp = 0.8:**

| error | correction = error * 0.8 |
|---|---|
| +0.4 | _________ |
| +0.2 | _________ |
| 0.0 | _________ |
| -0.2 | _________ |
| -0.4 | _________ |

**Which Kp gives bigger corrections?** _________

**What does a bigger correction mean for the robot?** _________________________________________

## Part 4: Calculating Motor Efforts

Use these formulas:
```
left_effort  = base_effort + correction
right_effort = base_effort - correction
```

With `base_effort = 0.3`, fill in the table:

| correction | left_effort | right_effort | Which motor is faster? | Robot steers... |
|---|---|---|---|---|
| +0.15 | _________ | _________ | Left / Right | Toward line / Away |
| +0.05 | _________ | _________ | Left / Right | Toward line / Away |
| 0.00 | _________ | _________ | Equal | Straight |
| -0.05 | _________ | _________ | Left / Right | Toward line / Away |
| -0.15 | _________ | _________ | Left / Right | Toward line / Away |

## Part 5: Full Calculation Trace

Trace through the entire proportional control calculation for each scenario.

**Settings:** `setpoint = 0.5`, `Kp = 0.5`, `base_effort = 0.3`

**Scenario A: Robot is on white (sensor reads 0.15)**

| Step | Calculation | Value |
|---|---|---|
| sensor_value | (given) | 0.15 |
| error | 0.5 - 0.15 = | _________ |
| correction | _________ * 0.5 = | _________ |
| left_effort | 0.3 + _________ = | _________ |
| right_effort | 0.3 - _________ = | _________ |

What will the robot do? _______________________________________________

**Scenario B: Robot is on the line (sensor reads 0.85)**

| Step | Calculation | Value |
|---|---|---|
| sensor_value | (given) | 0.85 |
| error | 0.5 - 0.85 = | _________ |
| correction | _________ * 0.5 = | _________ |
| left_effort | 0.3 + _________ = | _________ |
| right_effort | 0.3 - _________ = | _________ |

What will the robot do? _______________________________________________

**Scenario C: Robot is perfectly on the edge (sensor reads 0.50)**

| Step | Calculation | Value |
|---|---|---|
| sensor_value | (given) | 0.50 |
| error | 0.5 - 0.50 = | _________ |
| correction | _________ * 0.5 = | _________ |
| left_effort | 0.3 + _________ = | _________ |
| right_effort | 0.3 - _________ = | _________ |

What will the robot do? _______________________________________________

## Part 6: Blocking vs. Continuous

**Blocking call:**
```python
drivetrain.straight(30)
```
This function does what? _______________________________________________

Does the next line of code run while the robot is driving? YES / NO

**Continuous call:**
```python
drivetrain.set_effort(0.3, 0.3)
```
This function does what? _______________________________________________

Does the next line of code run while the robot is driving? YES / NO

**Why is `set_effort()` better for a control loop?**

_________________________________________________________________

## Part 7: Code Prediction

What does this program do?

```python
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board
import time

drivetrain = DifferentialDrive.get_default_differential_drive()
board = Board.get_default_board()

board.wait_for_button()

drivetrain.set_effort(0.4, 0.2)
time.sleep(3)
drivetrain.stop()
```

Which motor is faster? Left / Right

The robot will steer: Left / Right

How long will it drive? _________ seconds

## Part 8: Spot the Error

Each code snippet has a problem. Identify and explain the issue.

**Problem 1:**
```python
setpoint = 0.5
Kp = 0.5
base_effort = 0.3

sensor_value = reflectance.get_left()
error = setpoint - sensor_value
correction = error * Kp
drivetrain.set_effort(base_effort + correction, base_effort - correction)
```

What is missing? __________________________________________________________

Why does it matter? ________________________________________________________

**Problem 2:**
```python
while True:
    sensor_value = reflectance.get_left()
    error = sensor_value - setpoint           # <-- Look at this line
    correction = error * Kp
    drivetrain.set_effort(base_effort + correction, base_effort - correction)
```

What is different about the error calculation? _________________________________

What effect will this have on the robot? ________________________________________

## Part 9: Kp Tuning

You are tuning your robot and observe the following behaviors. For each, explain what you would change about Kp.

**Observation 1:** The robot follows the line but weaves back and forth rapidly, never settling down.

Kp is too: HIGH / LOW (circle one)

I should: INCREASE / DECREASE Kp (circle one)

**Observation 2:** The robot slowly drifts off the line and does not correct fast enough.

Kp is too: HIGH / LOW (circle one)

I should: INCREASE / DECREASE Kp (circle one)

**Observation 3:** The robot follows the line smoothly with only small corrections.

Kp is: ABOUT RIGHT (no change needed)

## Part 10: Tuning Record

Use this table to record your Kp tuning experiments on the actual robot.

| Trial | Kp | base_effort | Behavior | Rating (1-5) |
|---|---|---|---|---|
| 1 | 0.3 | 0.3 | | |
| 2 | 0.5 | 0.3 | | |
| 3 | 0.7 | 0.3 | | |
| 4 | 1.0 | 0.3 | | |
| 5 | _____ | _____ | | |
| 6 | _____ | _____ | | |

**Best combination:** Kp = _________ base_effort = _________

**Why did you choose this combination?**

_________________________________________________________________

_________________________________________________________________

## Part 11: Reflection

**Explain in your own words what proportional control does:**

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

**How is proportional control different from the bounce driving in Lessons 3-4?**

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

**Why is the math approach (error * Kp) better than using if/else to decide whether to turn left or right?**

_________________________________________________________________

_________________________________________________________________
