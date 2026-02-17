# Lesson 1 Worksheet: Sensor Calibration

**Name:** ________________________
**Date:** ________________________

---

## Part 1: Calibration Data Collection

Place your robot in each position and record the sensor values. Take 3 readings for each position and calculate the average.

### Position 1: Both Sensors on WHITE Surface

| Reading # | Left Sensor | Right Sensor |
|---|---|---|
| 1 | __________ | __________ |
| 2 | __________ | __________ |
| 3 | __________ | __________ |
| **Average** | __________ | __________ |

### Position 2: Both Sensors on BLACK Line

| Reading # | Left Sensor | Right Sensor |
|---|---|---|
| 1 | __________ | __________ |
| 2 | __________ | __________ |
| 3 | __________ | __________ |
| **Average** | __________ | __________ |

### Position 3: Left Sensor on EDGE of Line

| Reading # | Left Sensor | Right Sensor |
|---|---|---|
| 1 | __________ | __________ |
| 2 | __________ | __________ |
| 3 | __________ | __________ |
| **Average** | __________ | __________ |

---

## Part 2: Determine Your Threshold

1. What is the highest "off line" (white) average value? __________

2. What is the lowest "on line" (black) average value? __________

3. **Your threshold** (halfway between): __________

   Formula: threshold = (highest white + lowest black) / 2

4. Does 0.5 work as a reasonable threshold for your robot? (yes/no) __________

---

## Part 3: Sensor Value Prediction

Without running the robot, predict the sensor values for each scenario:

| Scenario | Left Sensor (predict) | Right Sensor (predict) |
|---|---|---|
| Both sensors on white | __________ | __________ |
| Both sensors on black line | __________ | __________ |
| Left on line, right on white | __________ | __________ |
| Right on line, left on white | __________ | __________ |
| Both sensors on line edge | __________ | __________ |

---

## Part 4: Understanding the Sensor

1. **Why does a white surface give a LOW sensor value (near 0.0)?**

   Answer: ____________________________________________________________________

2. **Why does a black surface give a HIGH sensor value (near 1.0)?**

   Answer: ____________________________________________________________________

3. **Why do we need TWO sensors instead of just one?**

   Answer: ____________________________________________________________________

4. **Why do we calibrate instead of just using 0.5 as the threshold?**

   Answer: ____________________________________________________________________

---

## Part 5: Code Matching

Match each line of code with what it does:

| Code | What It Does |
|---|---|
| `from XRPLib.reflectance import Reflectance` | A. Pauses for 0.1 seconds |
| `reflectance = Reflectance.get_default_reflectance()` | B. Reads the left sensor value |
| `left = reflectance.get_left()` | C. Creates a sensor object |
| `print("Left:", left)` | D. Loads the sensor library |
| `time.sleep(0.1)` | E. Shows the value on screen |

**Answers:** ___  ___  ___  ___  ___

---

## Reflection

**What surprised you about the sensor values?**

_________________________________________________________________

_________________________________________________________________

---

**Next Lesson:** We'll use these values with a `while` loop to make the robot drive to the line and stop!
