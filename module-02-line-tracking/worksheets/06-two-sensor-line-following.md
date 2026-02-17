# Lesson 6 Worksheet: Two-Sensor Line Following

**Name:** __________________ **Date:** __________________ **Team:** __________________

## Part 1: One Sensor vs. Two Sensors

**One sensor (Lesson 5) follows the _____________ of the line.**

**Two sensors (Lesson 6) follow the _____________ of the line.**

**The one-sensor error formula is:** `error = _____________ - _____________`

**The two-sensor error formula is:** `error = _____________ - _____________`

**Which approach needs a setpoint variable?** One sensor / Two sensors (circle one)

## Part 2: Understanding Two-Sensor Error

**Formula:** `error = left_sensor - right_sensor`

Fill in the table. The first row is done for you.

| Robot Position | left_sensor | right_sensor | error = L - R | Robot should steer... |
|---|---|---|---|---|
| Centered | 0.5 | 0.5 | 0.0 | Straight |
| Drifted left | 0.8 | 0.2 | _________ | _________ |
| Drifted right | 0.2 | 0.8 | _________ | _________ |
| Slightly left | 0.6 | 0.4 | _________ | _________ |
| Slightly right | 0.4 | 0.6 | _________ | _________ |
| Both on white | 0.1 | 0.1 | _________ | _________ |
| Both on black | 0.9 | 0.9 | _________ | _________ |

**When error is positive, the robot has drifted:** LEFT / RIGHT (circle one)

**When error is negative, the robot has drifted:** LEFT / RIGHT (circle one)

## Part 3: Calculating Motor Efforts

**Formulas:**
```
left_effort  = base_effort - error * Kp
right_effort = base_effort + error * Kp
```

With `base_effort = 0.3` and `Kp = 0.5`, fill in the table:

| error | error * Kp | left_effort | right_effort | Which motor faster? |
|---|---|---|---|---|
| +0.6 | _________ | _________ | _________ | _________ |
| +0.2 | _________ | _________ | _________ | _________ |
| 0.0 | _________ | _________ | _________ | Equal |
| -0.2 | _________ | _________ | _________ | _________ |
| -0.6 | _________ | _________ | _________ | _________ |

## Part 4: Full Calculation Trace

Trace through the complete calculation for each scenario.

**Settings:** `Kp = 0.5`, `base_effort = 0.3`

**Scenario A: Robot drifts left**

| Step | Calculation | Value |
|---|---|---|
| left_sensor | (given) | 0.75 |
| right_sensor | (given) | 0.15 |
| error | 0.75 - 0.15 = | _________ |
| error * Kp | _________ * 0.5 = | _________ |
| left_effort | 0.3 - _________ = | _________ |
| right_effort | 0.3 + _________ = | _________ |

The robot steers: LEFT / RIGHT (circle one)

This is: CORRECT / INCORRECT because ________________________________________

**Scenario B: Robot drifts right**

| Step | Calculation | Value |
|---|---|---|
| left_sensor | (given) | 0.20 |
| right_sensor | (given) | 0.70 |
| error | 0.20 - 0.70 = | _________ |
| error * Kp | _________ * 0.5 = | _________ |
| left_effort | 0.3 - _________ = | _________ |
| right_effort | 0.3 + _________ = | _________ |

The robot steers: LEFT / RIGHT (circle one)

This is: CORRECT / INCORRECT because ________________________________________

**Scenario C: Robot is centered**

| Step | Calculation | Value |
|---|---|---|
| left_sensor | (given) | 0.45 |
| right_sensor | (given) | 0.45 |
| error | 0.45 - 0.45 = | _________ |
| error * Kp | _________ * 0.5 = | _________ |
| left_effort | 0.3 - _________ = | _________ |
| right_effort | 0.3 + _________ = | _________ |

The robot: STEERS LEFT / STEERS RIGHT / DRIVES STRAIGHT (circle one)

## Part 5: Why Are the Signs Different?

In Lesson 5 (one sensor), the motor formula was:
```
left_effort  = base_effort + correction
right_effort = base_effort - correction
```

In Lesson 6 (two sensors), the motor formula is:
```
left_effort  = base_effort - error * Kp
right_effort = base_effort + error * Kp
```

The signs flipped! Explain why in your own words:

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

Hint: Think about what "positive error" means in each version.

## Part 6: Code Comparison

**Fill in the blanks to complete both versions:**

**One-sensor version (Lesson 5):**
```python
sensor_value = reflectance.get_left()
error = _________ - sensor_value
correction = error * Kp
left_effort = base_effort _____ correction
right_effort = base_effort _____ correction
```

**Two-sensor version (Lesson 6):**
```python
left_sensor = reflectance._________()
right_sensor = reflectance._________()
error = _________ - _________
left_effort = base_effort _____ error * Kp
right_effort = base_effort _____ error * Kp
```

## Part 7: Code Prediction

What does this program print when the robot is manually moved across the line?

```python
from XRPLib.reflectance import Reflectance
import time

reflectance = Reflectance.get_default_reflectance()

while True:
    left = reflectance.get_left()
    right = reflectance.get_right()
    error = left - right
    print(f"L={left:.2f} R={right:.2f} err={error:.2f}")
    time.sleep(0.5)
```

**If both sensors are on white, the output looks like:**

`L=_____ R=_____ err=_____`

**If the left sensor is on the line and the right is on white:**

`L=_____ R=_____ err=_____`

**If both sensors are on the line:**

`L=_____ R=_____ err=_____`

## Part 8: Spot the Error

Each code snippet has a mistake. Identify and explain the issue.

**Problem 1:**
```python
while True:
    left_sensor = reflectance.get_left()
    right_sensor = reflectance.get_right()
    error = right_sensor - left_sensor       # <-- Look here
    left_effort = base_effort - error * Kp
    right_effort = base_effort + error * Kp
    drivetrain.set_effort(left_effort, right_effort)
```

What is wrong? ____________________________________________________________

What will happen? __________________________________________________________

**Problem 2:**
```python
while True:
    left_sensor = reflectance.get_left()
    right_sensor = reflectance.get_right()
    error = left_sensor - right_sensor
    left_effort = base_effort - error * Kp
    right_effort = base_effort + error * Kp
    drivetrain.set_effort(left_effort, right_effort)
    time.sleep(1)                              # <-- Look here
```

What is the problem with `time.sleep(1)`? _____________________________________

How should it be fixed? ____________________________________________________

## Part 9: The Curious Case

When BOTH sensors read high (both on black tape), the error is approximately _________.

This means the robot will _________________________________.

But physically, both sensors on black tape might mean:

_________________________________________________________________

Why could this be a problem for line following?

_________________________________________________________________

(We will solve this problem in Lesson 7!)

## Part 10: Experimental Comparison

After testing both programs on the robot, fill in your observations.

**One-sensor line following (Lesson 5):**

| Aspect | Observation |
|---|---|
| Smoothness (1-5 scale) | |
| Did it lose the line? | YES / NO |
| Best Kp value | |
| Best base_effort | |

**Two-sensor line following (Lesson 6):**

| Aspect | Observation |
|---|---|
| Smoothness (1-5 scale) | |
| Did it lose the line? | YES / NO |
| Best Kp value | |
| Best base_effort | |

**Which version performed better?** _________________________________________

**Why?** _________________________________________________________________

## Part 11: Reflection

**Explain the two-sensor error formula in your own words:**

_________________________________________________________________

_________________________________________________________________

**Why is following the center of the line better than following the edge?**

_________________________________________________________________

_________________________________________________________________

**What situation can the two-sensor approach NOT detect? (Hint: think about both sensors reading the same high value.)**

_________________________________________________________________

_________________________________________________________________
