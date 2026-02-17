# Lesson 5 Slide Outline: Proportional Control with One Sensor

## Slide 1: Title & Learning Objectives
**Title:** Proportional Control with One Sensor

**Learning Objectives:**
- Understand what a setpoint is and how to calculate error
- Use `set_effort()` for continuous motor control
- Build a proportional control loop for line following
- Tune the Kp gain constant by observing behavior

**Agenda:**
- The problem with bounce driving (5 min)
- Introducing set_effort() and continuous control (5 min)
- Building the proportional controller step by step (20 min)
- Practice: Follow the circle edge and tune Kp (20 min)

---

## Slide 2: Hook -- What is Wrong with Bounce Driving?
**Bounce driving (Lessons 3-4):**
```
Drive straight --> Hit line --> Stop --> Turn --> Drive straight --> Hit line --> ...
```

**Problems:**
- Jerky, not smooth
- Robot is NOT following the line -- it is bouncing off it
- Cannot handle curves well

**What we want:**
- Robot smoothly follows the line
- Constant small adjustments, like steering a car

**Question:** "How can the robot steer while it is driving?"

---

## Slide 3: Blocking vs. Continuous Motor Control

**Blocking calls (what we used before):**
```python
drivetrain.straight(30)   # Drives 30 cm, then STOPS
drivetrain.turn(90)       # Turns 90 degrees, then STOPS
```
- Robot does one thing at a time
- Cannot read sensors WHILE driving

**Continuous control (new):**
```python
drivetrain.set_effort(0.3, 0.3)   # Sets motors and KEEPS GOING
```
- Sets motor power and returns immediately
- Motors keep running until you change them
- You can read sensors in between calls

**Key difference:** `set_effort()` does not block -- the program keeps running.

---

## Slide 4: set_effort() Examples

**Drive straight:**
```python
drivetrain.set_effort(0.3, 0.3)   # Both motors equal
```

**Turn right (left faster):**
```python
drivetrain.set_effort(0.4, 0.2)   # Left faster than right
```

**Turn left (right faster):**
```python
drivetrain.set_effort(0.2, 0.4)   # Right faster than left
```

**Stop:**
```python
drivetrain.stop()                  # Both motors off
```

**Values range from -1.0 (full reverse) to 1.0 (full forward)**

**Question:** "What would `set_effort(0.5, -0.5)` do?" (Spin in place)

---

## Slide 5: The Setpoint

**From Lesson 1, you recorded sensor values:**
- On white surface: ~0.1 to 0.3
- On the edge of the line: ~0.5
- On the black line: ~0.7 to 0.9

**The setpoint is the target value we want to maintain.**

```python
setpoint = 0.5   # The edge of the line
```

**[Diagram description: A cross-section of the taped line showing the sensor position. On the left side is white (low reading), in the middle is the edge (setpoint ~0.5), on the right is black (high reading). An arrow points to the edge labeled "This is where we want to be."]**

**Goal:** Keep the sensor reading at the setpoint by making constant small steering adjustments.

---

## Slide 6: Calculating Error

**Error = how far we are from where we want to be**

```python
error = setpoint - sensor_reading
```

**Examples (setpoint = 0.5):**

| Where is the robot? | sensor_reading | error | Meaning |
|---|---|---|---|
| On the edge (perfect) | 0.5 | 0.0 | No correction needed |
| Drifted onto white | 0.2 | +0.3 | Steer toward line |
| Drifted onto black | 0.8 | -0.3 | Steer away from line |

**Key insight:**
- **Positive error** = robot is too far off the line (on white) -- steer toward it
- **Negative error** = robot is too far on the line (on black) -- steer away
- **Zero error** = perfect position -- drive straight

---

## Slide 7: From Error to Correction

**We multiply error by a gain constant Kp:**
```python
correction = error * Kp
```

**Kp controls how aggressively the robot reacts.**

**Example with Kp = 0.5:**

| error | correction = error * 0.5 | What happens |
|---|---|---|
| +0.3 | +0.15 | Gentle steer toward line |
| -0.3 | -0.15 | Gentle steer away from line |
| +0.4 | +0.20 | Stronger steer toward line |
| 0.0 | 0.0 | Drive straight |

**Then apply correction to motors:**
```python
left_effort  = base_effort + correction
right_effort = base_effort - correction
```

**Question:** "What happens if Kp is very large, like 5.0?" (Overcorrection, oscillation)

---

## Slide 8: The Complete Control Loop

```python
setpoint = 0.5
Kp = 0.5
base_effort = 0.3

while True:
    # 1. Read sensor
    sensor_value = reflectance.get_left()

    # 2. Calculate error
    error = setpoint - sensor_value

    # 3. Calculate correction
    correction = error * Kp

    # 4. Apply to motors
    left_effort = base_effort + correction
    right_effort = base_effort - correction
    drivetrain.set_effort(left_effort, right_effort)

    time.sleep(0.01)
```

**[Diagram description: A circular flow diagram showing: Read Sensor --> Calculate Error --> Calculate Correction --> Set Motors --> (back to) Read Sensor. Label: "This loop runs hundreds of times per second."]**

---

## Slide 9: Tracing Through the Math

**Scenario: Robot drifts onto white (sensor reads 0.2)**

```
setpoint      = 0.5
sensor_value  = 0.2
error         = 0.5 - 0.2 = 0.3
Kp            = 0.5
correction    = 0.3 * 0.5 = 0.15
base_effort   = 0.3

left_effort   = 0.3 + 0.15 = 0.45
right_effort  = 0.3 - 0.15 = 0.15
```

**Result:** Left motor runs at 0.45, right motor runs at 0.15.
Left is faster, so the robot steers to the right -- back toward the line.

**Scenario: Robot drifts onto black (sensor reads 0.8)**

```
error         = 0.5 - 0.8 = -0.3
correction    = -0.3 * 0.5 = -0.15

left_effort   = 0.3 + (-0.15) = 0.15
right_effort  = 0.3 - (-0.15) = 0.45
```

**Result:** Right motor is faster, robot steers left -- away from the line.

---

## Slide 10: What Does Kp Do?

**[Diagram description: Three horizontal paths showing robot behavior. Top path labeled "Kp too low (0.1)" shows a robot drifting slowly off the line. Middle path labeled "Kp just right (0.5)" shows a robot smoothly following the curved line. Bottom path labeled "Kp too high (2.0)" shows a robot zigzagging rapidly back and forth across the line.]**

| Kp Value | Behavior |
|---|---|
| Too low (e.g., 0.1) | Robot reacts too slowly, drifts off the line |
| Just right (e.g., 0.5) | Robot follows smoothly with small adjustments |
| Too high (e.g., 2.0) | Robot overcorrects, oscillates wildly |

**Tuning Kp is about finding the sweet spot:**
- Start at 0.5
- If too wiggly, lower it
- If too sluggish, raise it

---

## Slide 11: Exercise -- Follow the Circle

**Your task:**
1. Type in the complete proportional control program
2. Place the robot on the edge of your taped circle
3. Press the button and observe
4. Tune Kp and base_effort for smooth tracking

**Complete program:**
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

while True:
    sensor_value = reflectance.get_left()
    error = setpoint - sensor_value
    correction = error * Kp
    drivetrain.set_effort(base_effort + correction,
                          base_effort - correction)
    time.sleep(0.01)
```

**Success:** Robot completes one full lap of the circle.

---

## Slide 12: Connection to Lesson 6

**What we accomplished today:**
- Smooth line following with ONE sensor using proportional control
- Understood setpoint, error, Kp, and correction

**Limitation of one sensor:**
- Only tracks one edge of the line
- If the robot drifts too far off, it cannot tell which side it is on

**Next lesson: Two-Sensor Line Following**
- Use BOTH left and right sensors
- Error = left sensor - right sensor
- Even smoother tracking, follows the CENTER of the line

**Preview:**
```python
error = reflectance.get_left() - reflectance.get_right()
```

**Question:** "Why might two sensors be better than one?"
