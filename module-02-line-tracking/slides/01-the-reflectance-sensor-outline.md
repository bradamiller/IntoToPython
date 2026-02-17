# Lesson 1 Slide Outline: The Reflectance Sensor

## Slide 1: Title & Learning Objectives
**Title:** The Reflectance Sensor

**Learning Objectives:**
- Explain how reflectance sensors detect light vs. dark surfaces
- Read sensor values using the Reflectance class
- Record calibration data for your specific robot and surface
- Choose a threshold value for line detection

**Agenda:**
- How sensors work (10 min)
- Reading sensor values (15 min)
- Calibration exercise (20 min)

---

## Slide 2: Hook — How Does a Robot "See"?
**Question:** "You can see the black line. How could a robot tell the difference?"

**Discussion:** Robots don't have eyes — they use sensors that measure physical properties.

**Today:** We'll learn to read the XRP's reflectance sensors — the robot's way of "seeing" the line.

---

## Slide 3: How Reflectance Sensors Work
**The sensor has two parts:**
1. **Infrared LED** — shines light downward
2. **Light detector** — measures how much bounces back

**White surface:** Reflects most light → low value (close to 0.0)
**Black surface:** Absorbs most light → high value (close to 1.0)

**Analogy:** Flashlight on a mirror vs. a black t-shirt

**Show:** Photo of XRP underside with sensors highlighted

---

## Slide 4: Sensor Value Range
**Values range from 0.0 to 1.0:**

| Position | Left Sensor | Right Sensor |
|---|---|---|
| On white surface | ~0.1 – 0.3 | ~0.1 – 0.3 |
| On line edge | ~0.4 – 0.6 | ~0.4 – 0.6 |
| On black line | ~0.7 – 0.9 | ~0.7 – 0.9 |

**Key idea:** The transition from white to black is GRADUAL, not sudden.

**The XRP has TWO sensors** — left and right — each reads independently.

---

## Slide 5: Reading Sensors in Python
**Import and setup:**
```python
from XRPLib.reflectance import Reflectance
from XRPLib.board import Board

reflectance = Reflectance.get_default_reflectance()
board = Board.get_default_board()
```

**Read values:**
```python
board.wait_for_button()
left = reflectance.get_left()
right = reflectance.get_right()
print("Left:", left, "Right:", right)
```

**Key point:** `get_left()` and `get_right()` return a number between 0.0 and 1.0.

---

## Slide 6: Continuous Reading
**Read many times in a loop:**
```python
import time

board.wait_for_button()

for i in range(50):
    left = reflectance.get_left()
    right = reflectance.get_right()
    print("Left:", left, "  Right:", right)
    time.sleep(0.1)
```

**Why?** See how values change as you move the robot across the line.

**`time.sleep(0.1)`** — pause 0.1 seconds so readings aren't too fast to read.

---

## Slide 7: What Is a Threshold?
**Threshold:** A cutoff value to decide "on line" vs. "off line"

**Example:**
- Off line readings: 0.1, 0.2, 0.15, 0.25
- On line readings: 0.75, 0.8, 0.85, 0.9
- **Threshold = 0.5** (halfway between)

**Rule:** If sensor > threshold → on the line. If sensor < threshold → off the line.

**Important:** The threshold depends on YOUR surface and tape. Calibrate!

---

## Slide 8: Calibration Exercise
**Your task:**
1. Place robot on WHITE surface → record sensor values
2. Place robot on BLACK line → record sensor values
3. Place robot on EDGE of line → record sensor values
4. Calculate your threshold (halfway between off-line and on-line averages)

**Why calibrate?** Different surfaces, tape colors, and lighting conditions give different values.

**Save your threshold!** You'll use it for the rest of Module 2.

---

## Slide 9: Your Turn!
**Activity:**
1. Create `sensor_test.py`
2. Write the continuous reading program
3. Collect calibration data for 3 positions
4. Record in your worksheet
5. Determine your threshold value

**Checkpoints:**
- Can you read sensor values?
- Do white and black give different numbers?
- Did you find a good threshold?

---

## Slide 10: Connection to Next Lesson
**What you did today:**
- Learned how reflectance sensors work
- Read sensor values in Python
- Calibrated your sensors and chose a threshold

**Next lesson (Lesson 2):**
- Use a **`while` loop** to keep the robot driving
- Stop when the sensor detects the line
- First time the robot uses sensors to control its behavior!

**Save your calibration data — you'll need it!**
