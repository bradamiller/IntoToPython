# Lesson 2: Drive to the Edge and Stop

## Overview
Students learn the `while` loop — Python's way of repeating actions until a condition is met. Combined with the reflectance sensor from Lesson 1, students program the robot to drive forward continuously until it detects the edge of the taped circle, then stop. This is the first time students use sensors to control robot behavior in real time.

## Learning Objectives
By the end of this lesson, students will be able to:
- Understand and write `while` loops in Python
- Use comparison operators (`<`, `>`, `==`, `!=`, `<=`, `>=`)
- Combine sensor reading with a `while` loop for continuous checking
- Explain the difference between `for` loops and `while` loops
- Program the robot to drive until a condition is met
- Use `print()` inside loops for debugging

## Key Concepts
- **`while` loop**: Repeats code as long as a condition is `True`; stops when the condition becomes `False`
- **Condition**: A test that evaluates to `True` or `False` (e.g., `left < 0.5`)
- **Comparison operators**: `<` (less than), `>` (greater than), `==` (equal to), `!=` (not equal to), `<=`, `>=`
- **Boolean values**: `True` and `False` — the result of a comparison
- **Sensor-driven loop**: The loop keeps running while the sensor says "no line detected"
- **`for` vs. `while`**: `for` loops run a fixed number of times; `while` loops run until a condition changes

## Materials Required
- XRP Robot with reflectance sensors
- White surface with taped circle (robot starts inside the circle)
- VS Code with XRPLib installed
- Calibration data from Lesson 1

## Lesson Flow

### Introduction (10 minutes)

1. **Hook: The Problem**:
   - Ask: "Last lesson, we read sensor values. But the robot just sat still. How do we make the robot drive AND check the sensor at the same time?"
   - Show: "We need a loop that keeps driving as long as the sensor says 'no line'. When the sensor detects the line, stop."

2. **Introduce `while` Loops**:
   - The `for` loop (from Module 1) repeats a fixed number of times: `for i in range(4)`
   - But what if we don't know how many times to repeat?
   - The `while` loop repeats as long as a condition is true:
     ```python
     while condition:
         # do something
     ```
   - When the condition becomes false, the loop stops

3. **Comparison Operators**:
   - `<` less than: `3 < 5` is `True`
   - `>` greater than: `5 > 3` is `True`
   - `==` equal to: `4 == 4` is `True`
   - `!=` not equal to: `3 != 5` is `True`
   - `<=` less than or equal, `>=` greater than or equal
   - Show examples with sensor context:
     - `left < 0.5` means "the left sensor reads less than 0.5 (on white)"
     - `left > 0.5` means "the left sensor reads more than 0.5 (on the line)"

4. **Syntax**:
   ```python
   while left < 0.5:    # condition
       # indented code runs while condition is True
       # when left >= 0.5, the loop stops
   ```
   - Just like `for` loops: colon at the end, indented body

### Guided Practice: Drive to the Edge (20 minutes)

1. **Simple while Loop Demo** (no robot):
   ```python
   count = 0
   while count < 5:
       print("Count is:", count)
       count = count + 1
   print("Done! Count is now:", count)
   ```
   - Walk through: count starts at 0, loop runs while count < 5, increments each time
   - Stops when count reaches 5

2. **Sensor-Driven while Loop**:
   - Build the program step by step:
     ```python
     from XRPLib.reflectance import Reflectance
     from XRPLib.differential_drive import DifferentialDrive
     from XRPLib.board import Board

     reflectance = Reflectance.get_default_reflectance()
     drivetrain = DifferentialDrive.get_default_differential_drive()
     board = Board.get_default_board()

     threshold = 0.5  # Use YOUR threshold from Lesson 1

     board.wait_for_button()

     # Read initial sensor value
     left = reflectance.get_left()

     # Keep driving while sensor is on white (below threshold)
     while left < threshold:
         drivetrain.set_effort(0.3, 0.3)
         left = reflectance.get_left()  # Update the reading!

     # We're here because left >= threshold (line detected!)
     drivetrain.stop()
     print("Line detected! Stopping.")
     ```

3. **Line-by-Line Explanation**:
   - `left = reflectance.get_left()` — read the sensor before entering the loop
   - `while left < threshold:` — keep looping while we're on white surface
   - `drivetrain.set_effort(0.3, 0.3)` — drive forward at 30% power
   - `left = reflectance.get_left()` — **critical**: update the sensor reading inside the loop!
   - `drivetrain.stop()` — runs after the loop exits (line was detected)

4. **Critical Point — Updating Inside the Loop**:
   - Ask: "What happens if we forget the second `left = reflectance.get_left()` inside the loop?"
   - Answer: The variable `left` never changes, the condition never becomes False, the loop runs forever!
   - This is called an **infinite loop** — the robot would drive forever
   - Rule: Always update the variable you're checking inside the while loop

5. **Demo & Test**:
   - Place robot inside the taped circle, pointing toward an edge
   - Upload and run
   - Robot should drive forward and stop when it hits the line

### Independent Practice (20 minutes)

**Exercise 1: Drive to the Edge and Stop (Scaffolded)**
- Goal: Place robot inside the taped circle. It drives forward until it detects the line, then stops.
- Starter code:
  ```python
  from XRPLib.reflectance import Reflectance
  from XRPLib.differential_drive import DifferentialDrive
  from XRPLib.board import Board

  reflectance = Reflectance.get_default_reflectance()
  drivetrain = DifferentialDrive.get_default_differential_drive()
  board = Board.get_default_board()

  threshold = 0.5  # TODO: Replace with your threshold from Lesson 1

  board.wait_for_button()

  left = reflectance.get_left()
  print("Starting value:", left)

  while left < threshold:
      drivetrain.set_effort(0.3, 0.3)
      left = reflectance.get_left()
      print("Sensor:", left)

  drivetrain.stop()
  print("Line detected! Final value:", left)
  ```
- Success criteria:
  - [ ] Robot drives forward from inside the circle
  - [ ] Robot stops when it reaches the taped line
  - [ ] Print statements show sensor values changing

**Exercise 2: Drive to the Edge with Right Sensor** (Challenge)
- Goal: Modify the program to use the RIGHT sensor instead of the left
- Then try: Use BOTH sensors — stop when EITHER sensor detects the line
  ```python
  left = reflectance.get_left()
  right = reflectance.get_right()

  while left < threshold and right < threshold:
      drivetrain.set_effort(0.3, 0.3)
      left = reflectance.get_left()
      right = reflectance.get_right()

  drivetrain.stop()
  print("Line detected!")
  ```
- Note: This previews the `and` logical operator — briefly explain: "Both conditions must be true for the loop to continue"

### Assessment

**Formative (during lesson)**:
- Can students write a while loop with correct syntax?
- Do they understand why the sensor must be re-read inside the loop?
- Can they explain the difference between `for` and `while` loops?

**Summative (worksheet/exit ticket)**:
1. What happens if you forget to update the sensor value inside the while loop?
2. Write a while loop that prints numbers from 1 to 10
3. If the threshold is 0.5 and the sensor reads 0.3, is `left < threshold` True or False?

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "`while` and `for` are the same" | `for` runs a fixed number of times; `while` runs until a condition changes |
| "The condition is checked once" | The condition is checked before EVERY iteration of the loop |
| "I don't need to update the variable" | If the variable never changes, the condition never becomes False = infinite loop |
| "`while left < 0.5` stops when left equals 0.5" | It stops when left is NOT less than 0.5 (i.e., left >= 0.5) |
| "The robot checks the sensor between commands" | The sensor is only read when you explicitly call `get_left()` or `get_right()` |

## Differentiation

**For struggling students**:
- Provide complete working code; focus on understanding what each line does
- Start with a non-robot while loop (counting) before adding sensors
- Use slow speed (0.2 effort) so there's time to observe

**For advanced students**:
- Add a counter to track how many loop iterations occurred before stopping
- Add a beep or LED change when the line is detected
- Try different speeds and observe how stopping accuracy changes

## Materials & Code Examples

### Complete Drive-to-Edge Program
```python
from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board

reflectance = Reflectance.get_default_reflectance()
drivetrain = DifferentialDrive.get_default_differential_drive()
board = Board.get_default_board()

threshold = 0.5

board.wait_for_button()
print("Driving to find the line...")

left = reflectance.get_left()

while left < threshold:
    drivetrain.set_effort(0.3, 0.3)
    left = reflectance.get_left()

drivetrain.stop()
print("Line found! Sensor value:", left)
```

## Teaching Notes
- **`set_effort()` vs. `straight()`**: `straight()` blocks until the distance is reached. `set_effort()` sets motor power and returns immediately — perfect for continuous loops.
- **Infinite loop danger**: If students forget to update the sensor, the robot drives forever. Have them ready to turn off the robot.
- **Speed matters**: Higher speeds mean less accurate stopping (momentum carries the robot past the line). Use 0.3 effort or lower.
- **Threshold tuning**: If the robot doesn't stop, the threshold may be wrong. Have students check their Lesson 1 calibration data.

## Connections to Next Lessons
- **Lesson 3** will add `if/else` inside the loop to make the robot turn around instead of stopping
- **Lesson 5** will use `while` loops for continuous proportional control (line following)
- `while` loops are the foundation for all real-time robot control in this course
