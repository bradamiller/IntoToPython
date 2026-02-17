# Lesson 6 Slide Outline: Two-Sensor Line Following

## Slide 1: Title & Learning Objectives
**Title:** Two-Sensor Line Following

**Learning Objectives:**
- Understand why two sensors are better than one
- Calculate error using left and right sensors: `error = left - right`
- Implement a two-sensor proportional control loop
- Compare one-sensor and two-sensor line following

**Agenda:**
- Why one sensor is not enough (5 min)
- Two-sensor error calculation (10 min)
- Build and test two-sensor follower (15 min)
- Compare one-sensor vs. two-sensor (20 min)

---

## Slide 2: Hook -- The Limitation of One Sensor

**One sensor (Lesson 5) follows the EDGE:**

**[Diagram description: Top-down view of a line. One sensor is shown on the right edge of the line. An arrow shows the robot following the edge, not the center.]**

**Problem scenarios:**
- Robot drifts completely off the line to the right
- Sensor reads low (white)
- But is the line to the LEFT or to the RIGHT?
- One sensor cannot tell!

**Solution:** Use BOTH sensors -- one on each side of the line.

**Question:** "If you close one eye, can you still judge distances? What about with both eyes?"

---

## Slide 3: Two Sensors Straddle the Line

**[Diagram description: Top-down view of a line with two sensors, one on each side. Three positions shown: (1) Centered -- both sensors partially on line, (2) Drifted left -- left sensor on line, right on white, (3) Drifted right -- right sensor on line, left on white.]**

**Centered:** Both sensors read similar values
**Drifted left:** Left sensor reads high, right reads low
**Drifted right:** Right sensor reads high, left reads low

**The difference between sensors tells us EVERYTHING:**
- How far we drifted
- Which direction we drifted

---

## Slide 4: The Two-Sensor Error Formula

**One sensor (Lesson 5):**
```python
error = setpoint - sensor_reading    # Needs a setpoint!
```

**Two sensors (this lesson):**
```python
error = reflectance.get_left() - reflectance.get_right()    # No setpoint needed!
```

**How it works:**

| Robot Position | Left | Right | error = L - R | Meaning |
|---|---|---|---|---|
| Centered | 0.5 | 0.5 | 0.0 | Drive straight |
| Drifted left | 0.8 | 0.2 | +0.6 | Steer left to correct |
| Drifted right | 0.2 | 0.8 | -0.6 | Steer right to correct |
| Both on white | 0.1 | 0.1 | 0.0 | Off the line |
| Both on black | 0.9 | 0.9 | 0.0 | Intersection? |

**Key: No setpoint variable needed. The difference IS the error.**

---

## Slide 5: Applying the Correction

**Motor effort formula:**
```python
left_effort  = base_effort - error * Kp
right_effort = base_effort + error * Kp
```

**Why the signs?**
- If error is **positive** (drifted left, left sensor on line):
  - Need to steer **left** to get back
  - Slow down left motor (subtract), speed up right motor (add)
- If error is **negative** (drifted right, right sensor on line):
  - Need to steer **right** to get back
  - Speed up left motor (subtracting a negative = adding), slow down right motor

**Note:** The signs are reversed from Lesson 5 because the error formula changed.

---

## Slide 6: Trace Through the Math

**Scenario: Robot drifts left (left sensor on line)**

```
left_sensor   = 0.8
right_sensor  = 0.2
error         = 0.8 - 0.2 = 0.6
Kp            = 0.5
base_effort   = 0.3

left_effort   = 0.3 - (0.6 * 0.5) = 0.3 - 0.3 = 0.0
right_effort  = 0.3 + (0.6 * 0.5) = 0.3 + 0.3 = 0.6
```

**Result:** Left motor stops, right motor runs fast. Robot turns left, back toward center.

**Scenario: Robot drifts right (right sensor on line)**

```
left_sensor   = 0.2
right_sensor  = 0.8
error         = 0.2 - 0.8 = -0.6

left_effort   = 0.3 - (-0.6 * 0.5) = 0.3 + 0.3 = 0.6
right_effort  = 0.3 + (-0.6 * 0.5) = 0.3 - 0.3 = 0.0
```

**Result:** Right motor stops, left motor runs fast. Robot turns right, back toward center.

---

## Slide 7: The Complete Two-Sensor Program

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

**[Diagram description: Same circular control loop as Lesson 5 but with two sensor inputs: Read Left Sensor + Read Right Sensor --> Calculate Error (left - right) --> Calculate Correction --> Set Motors --> repeat.]**

---

## Slide 8: One Sensor vs. Two Sensors

**Side-by-side comparison:**

| Feature | One Sensor (Lesson 5) | Two Sensors (Lesson 6) |
|---|---|---|
| What it follows | Edge of the line | Center of the line |
| Error formula | `setpoint - sensor` | `left - right` |
| Needs setpoint? | Yes (0.5) | No |
| Motor formula | `base + correction` / `base - correction` | `base - error*Kp` / `base + error*Kp` |
| Smoothness | Good | Better |
| Recovery | Can only detect one side | Detects both sides |

**[Diagram description: Two paths around a circle. Top path (one sensor) shows slight wobble along the edge. Bottom path (two sensors) shows smooth tracking along the center.]**

---

## Slide 9: Exploring Sensor Readings

**Before running the control loop, explore the sensor values:**

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
    print(f"L={left:.2f}  R={right:.2f}  err={error:.2f}")
    time.sleep(0.2)
```

**Activity:** Slowly slide the robot across the line and watch how error changes.

- Centered: error near 0
- Left on line: error positive
- Right on line: error negative

---

## Slide 10: Exercise -- Two-Sensor Line Following

**Your task:**
1. Type in the two-sensor control program
2. Place the robot so the line runs between both sensors
3. Press the button and observe the tracking
4. Add debug printing to see the values

**Then compare:**
5. Run your Lesson 5 (one-sensor) program on the same circle
6. Run the Lesson 6 (two-sensor) program on the same circle

**Questions to answer:**
- Which version follows the line more smoothly?
- Which version handles the curved parts better?
- Which version can handle a higher base_effort without losing the line?

---

## Slide 11: A Curious Case -- Both Sensors High

**What happens when both sensors read high?**

```
left_sensor  = 0.9
right_sensor = 0.9
error        = 0.9 - 0.9 = 0.0
```

**Error is zero -- the robot drives straight.**

**But wait -- what does it mean physically when both sensors see the line?**

**[Diagram description: A taped circle with a cross (perpendicular line) taped across it. At the intersection point, both sensors are on black tape.]**

**Answer:** The robot might be at an INTERSECTION!

**This is the key idea for Lesson 7:** both sensors high = intersection detected.

---

## Slide 12: Connection to Lesson 7

**What we accomplished today:**
- Smooth two-sensor line following
- Error = left - right (no setpoint needed)
- Smoother tracking than one sensor

**Next lesson: Detecting Intersections**
- Add a taped cross to the circle
- When both sensors read high: intersection detected
- Robot stops, turns around, and continues in the opposite direction

**Preview:**
```python
if left_sensor > 0.5 and right_sensor > 0.5:
    # We are at an intersection!
    drivetrain.stop()
    drivetrain.turn(180)
```

**Question:** "How can we tell the difference between 'centered on the line' and 'at an intersection'?"
