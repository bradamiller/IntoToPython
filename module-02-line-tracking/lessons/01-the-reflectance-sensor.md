# Lesson 1: The Reflectance Sensor

## Overview
Students discover how the XRP's reflectance sensors work by reading real-time sensor values from light and dark surfaces. This is their first encounter with sensors — hardware that lets the robot "see" its environment. By the end of the lesson, students will have recorded calibration data they'll use throughout the rest of Module 2.

## Learning Objectives
By the end of this lesson, students will be able to:
- Explain how a reflectance sensor detects light vs. dark surfaces
- Import and use the `Reflectance` class from XRPLib
- Read left and right sensor values using `get_left()` and `get_right()`
- Use `print()` to display sensor values for debugging
- Identify typical sensor value ranges for white surface, black line, and line edge
- Record calibration data in a structured table

## Key Concepts
- **Reflectance sensor**: A sensor that shines infrared light downward and measures how much bounces back
- **Sensor value range**: Values from 0.0 (white/light, high reflectance) to 1.0 (black/dark, low reflectance)
- **Threshold**: A value used to decide "on the line" vs. "off the line" (typically around 0.5)
- **Calibration**: The process of measuring actual sensor values on your specific surface and tape
- **Analog vs. digital**: The sensor gives a range of values (analog), not just on/off (digital)

## Materials Required
- XRP Robot with reflectance sensors
- White surface (whiteboard material or white paper)
- Black electrical tape forming a circle on the white surface
- VS Code with XRPLib installed and configured
- Calibration data recording sheet (worksheet)

## Lesson Flow

### Introduction (10 minutes)

1. **Hook: How Does a Robot "See"?**
   - Ask: "You can see this black line on the white board. How could a robot tell the difference?"
   - Discussion: Robots don't have eyes. They use sensors that measure physical properties.
   - Show the underside of the XRP robot. Point out the two small reflectance sensors.

2. **How Reflectance Sensors Work**:
   - The sensor has two parts: an infrared LED (emitter) and a light detector (receiver)
   - The LED shines infrared light downward onto the surface
   - A white surface reflects most of the light back — the detector sees a lot of light (low value, close to 0.0)
   - A black surface absorbs most of the light — the detector sees very little light (high value, close to 1.0)
   - Analogy: "It's like shining a flashlight at a mirror (white) vs. a black t-shirt (dark)"

3. **Two Sensors, Two Readings**:
   - The XRP has a LEFT sensor and a RIGHT sensor
   - Each returns its own independent value
   - Having two sensors lets the robot figure out which side of a line it's on

### Guided Practice: Reading Sensor Values (15 minutes)

1. **Setting Up the Code**:
   - Open VS Code and create a new file: `sensor_test.py`
   - Walk through the imports and setup together:
     ```python
     from XRPLib.reflectance import Reflectance
     from XRPLib.board import Board
     import time

     reflectance = Reflectance.get_default_reflectance()
     board = Board.get_default_board()
     ```
   - Explain each line:
     - `from XRPLib.reflectance import Reflectance` — loads the sensor class from the XRP library
     - `reflectance = Reflectance.get_default_reflectance()` — creates a reflectance sensor object
     - `board = Board.get_default_board()` — gives us access to the button

2. **First Sensor Read**:
   - Add a simple one-time read:
     ```python
     board.wait_for_button()

     left = reflectance.get_left()
     right = reflectance.get_right()
     print("Left sensor:", left)
     print("Right sensor:", right)
     ```
   - Place the robot on the white surface (both sensors off the line)
   - Upload and run
   - Observe: Both values should be low (around 0.1 to 0.3)
   - Move the robot so one sensor is on the black line, run again
   - Observe: The sensor on the line should read high (around 0.7 to 0.9)

3. **Continuous Reading with a Loop**:
   - Explain: "Reading once is useful, but we want to see how the values change as we move the robot"
   - Introduce a reading loop:
     ```python
     from XRPLib.reflectance import Reflectance
     from XRPLib.board import Board
     import time

     reflectance = Reflectance.get_default_reflectance()
     board = Board.get_default_board()

     board.wait_for_button()

     for i in range(50):
         left = reflectance.get_left()
         right = reflectance.get_right()
         print("Left:", left, "  Right:", right)
         time.sleep(0.1)
     ```
   - Upload and run while slowly sliding the robot across the line

4. **Observing the Values**:
   - White surface: values around 0.1 to 0.3
   - Edge of line: values around 0.4 to 0.6
   - On the line: values around 0.7 to 0.9
   - The transition is gradual, not a sudden jump

### Independent Practice (20 minutes)

**Exercise 1: Calibration Data Collection**
- Goal: Record sensor values for three positions — off line (white), on line (black), and on the edge
- Steps:
  1. Use the continuous reading program from guided practice
  2. Place robot so BOTH sensors are on white surface — record 3–5 readings
  3. Move robot so BOTH sensors are on the black line — record 3–5 readings
  4. Move robot so LEFT sensor is on the edge of the line — record 3–5 readings
  5. Calculate the average for each position
- Code to use:
  ```python
  from XRPLib.reflectance import Reflectance
  from XRPLib.board import Board
  import time

  reflectance = Reflectance.get_default_reflectance()
  board = Board.get_default_board()

  board.wait_for_button()

  for i in range(20):
      left = reflectance.get_left()
      right = reflectance.get_right()
      print("Reading", i + 1, "- Left:", left, "  Right:", right)
      time.sleep(0.5)
  ```
- Success criteria: Students have a completed calibration table with values for all three positions

**Exercise 2: Determine Your Threshold** (Challenge)
- Goal: Pick a threshold value that separates "on the line" from "off the line"
- Steps:
  1. Look at your calibration data
  2. Find the highest "off line" value and the lowest "on line" value
  3. Pick a number halfway between them — this is your threshold
  4. Write a program that prints whether the sensor is ON or OFF the line:
     ```python
     from XRPLib.reflectance import Reflectance
     from XRPLib.board import Board
     import time

     reflectance = Reflectance.get_default_reflectance()
     board = Board.get_default_board()

     threshold = 0.5  # Replace with YOUR threshold value

     board.wait_for_button()

     for i in range(30):
         left = reflectance.get_left()
         if left > threshold:
             print("LEFT sensor: ON the line  (value:", left, ")")
         else:
             print("LEFT sensor: OFF the line (value:", left, ")")
         time.sleep(0.3)
     ```
- Note: Students have not formally learned `if/else` yet. This is a preview. Tell students: "The `if` and `else` keywords let the robot make a decision. We'll learn more in Lesson 3."

### Assessment

**Formative (during lesson)**:
- Can students explain how the reflectance sensor works?
- Can students import and use the Reflectance class correctly?
- Can students read and interpret sensor values from print output?

**Summative (worksheet/exit ticket)**:
1. What value range would you expect when the sensor is over a white surface?
2. What value range would you expect when it's over a black line?
3. If your "off line" average is 0.2 and your "on line" average is 0.8, what threshold would you choose?
4. Why does the robot have two sensors instead of one?

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "Higher value = white surface" | Higher value (closer to 1.0) = darker surface; the sensor measures how much light is absorbed |
| "The sensor reads exactly 0.0 or 1.0" | The sensor returns a range of values; readings are rarely exactly 0 or 1 |
| "Both sensors always read the same value" | Each sensor reads independently; they give different values depending on position |
| "The threshold is always 0.5" | 0.5 is a reasonable default, but the best threshold depends on your surface and tape |
| "Sensor values never change" | Values vary slightly due to surface texture, ambient light, and sensor noise |

## Differentiation

**For struggling students**:
- Provide the complete code; focus on understanding the output, not writing code
- Use a simplified version with only one sensor (left) before introducing both
- Pair with a stronger student for the calibration exercise

**For advanced students**:
- Write a program that prints a visual indicator: `"####"` for on-line, `"----"` for off-line
- Challenge: Print a diagram showing robot position relative to the line
- Research: What other sensors exist on the XRP? (rangefinder, encoders, IMU)

## Materials & Code Examples

### Basic Sensor Read
```python
from XRPLib.reflectance import Reflectance
from XRPLib.board import Board

reflectance = Reflectance.get_default_reflectance()
board = Board.get_default_board()

board.wait_for_button()

left = reflectance.get_left()
right = reflectance.get_right()
print("Left sensor:", left)
print("Right sensor:", right)
```

### Continuous Sensor Read
```python
from XRPLib.reflectance import Reflectance
from XRPLib.board import Board
import time

reflectance = Reflectance.get_default_reflectance()
board = Board.get_default_board()

board.wait_for_button()

for i in range(50):
    left = reflectance.get_left()
    right = reflectance.get_right()
    print("Left:", left, "  Right:", right)
    time.sleep(0.1)
```

## Teaching Notes
- **Physical setup matters**: Make sure the black tape is firmly pressed down with no air bubbles
- **Ambient light**: Bright overhead lights or direct sunlight can shift values. Calibration handles this.
- **Sensor height**: The reflectance sensor must be close to the surface (a few mm). If lifted, values will be unreliable.
- **Print is your friend**: Emphasize that `print()` is the most important debugging tool
- **Save calibration data**: Students should save their calibration data — they'll reference it in Lessons 2–7

## Connections to Next Lessons
- **Lesson 2** will use these sensor values with a `while` loop to drive until detecting the line
- **Lesson 3** will use `if/else` to decide what to do when the sensor detects the line
- The threshold value determined here will be used throughout the entire module
