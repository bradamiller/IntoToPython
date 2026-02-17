# Lesson 3: Bounce Driving

## Overview
Students learn `if/else` statements — Python's way of making decisions. Instead of stopping when the robot detects the line (Lesson 2), the robot now turns around and keeps driving. When it hits the line again, it turns around again. This "bounce driving" pattern keeps the robot inside the taped circle indefinitely, bouncing back and forth between edges.

## Learning Objectives
By the end of this lesson, students will be able to:
- Write `if/else` statements in Python
- Understand how `if/else` creates two different code paths
- Combine `while`, `if/else`, and sensor reading for continuous decision-making
- Program the robot to bounce between the edges of a taped circle
- Use `True` as a `while` loop condition for an infinite loop
- Debug sensor-based programs using `print()`

## Key Concepts
- **`if/else` statement**: Executes one block of code if a condition is True, another block if False
- **Decision making**: The robot checks a condition and chooses what to do
- **`while True`**: An infinite loop that runs forever (until the robot is turned off)
- **Bounce driving**: Drive straight, detect line, turn around, repeat
- **Logical operators**: `and`, `or`, `not` for combining conditions

## Materials Required
- XRP Robot with reflectance sensors
- White surface with taped circle (robot starts inside)
- VS Code with XRPLib installed
- Threshold value from Lesson 1

## Lesson Flow

### Introduction (10 minutes)

1. **Hook: What Now?**
   - "In Lesson 2, the robot drove to the edge and stopped. But what if we want it to keep going? Like a ball bouncing off a wall?"
   - Demo idea: Describe the behavior — drive forward, hit the edge, turn around, drive again, hit the opposite edge, turn around again... forever.

2. **Introduce `if/else`**:
   - Sometimes we need the robot to make a choice: "If the sensor sees the line, turn around. Otherwise, keep driving."
   - Syntax:
     ```python
     if condition:
         # do this when condition is True
     else:
         # do this when condition is False
     ```
   - Both blocks are indented, just like loops
   - Only ONE block runs — never both

3. **Non-Robot Example**:
   ```python
   temperature = 85
   if temperature > 80:
       print("It's hot outside!")
   else:
       print("It's comfortable.")
   ```
   - Ask: "Which message prints?" (Hot — because 85 > 80)

### Guided Practice: Bounce Driving (20 minutes)

1. **The Bounce Algorithm**:
   - Pseudocode:
     ```
     loop forever:
         read the sensor
         if sensor detects line:
             stop
             turn around
         else:
             keep driving forward
     ```

2. **Build the Program**:
   ```python
   from XRPLib.reflectance import Reflectance
   from XRPLib.differential_drive import DifferentialDrive
   from XRPLib.board import Board

   reflectance = Reflectance.get_default_reflectance()
   drivetrain = DifferentialDrive.get_default_differential_drive()
   board = Board.get_default_board()

   threshold = 0.5

   board.wait_for_button()
   print("Bounce driving started!")

   while True:
       left = reflectance.get_left()

       if left > threshold:
           # Line detected! Turn around
           drivetrain.stop()
           print("Line detected! Turning around...")
           drivetrain.turn(180)
       else:
           # No line — keep driving
           drivetrain.set_effort(0.3, 0.3)
   ```

3. **Line-by-Line Explanation**:
   - `while True:` — this loop runs forever (True is always True)
   - `left = reflectance.get_left()` — read the sensor every iteration
   - `if left > threshold:` — check if we've hit the line
   - `drivetrain.stop()` — stop before turning (cleaner turn)
   - `drivetrain.turn(180)` — turn around 180 degrees
   - `else:` — if no line detected...
   - `drivetrain.set_effort(0.3, 0.3)` — keep driving forward

4. **`while True` Explained**:
   - `while True` means "loop forever"
   - The only way to stop is to turn off the robot
   - This is common in robotics — the robot should keep running until you stop it
   - In this course, we'll use `while True` whenever we want continuous behavior

5. **Demo & Observe**:
   - Place robot inside the circle
   - Upload and run
   - Robot should drive, hit edge, turn 180°, drive back, hit other edge, turn 180°, repeat

### Independent Practice (20 minutes)

**Exercise 1: Basic Bounce Driving**
- Goal: Get the robot bouncing back and forth inside the taped circle
- Code:
  ```python
  from XRPLib.reflectance import Reflectance
  from XRPLib.differential_drive import DifferentialDrive
  from XRPLib.board import Board

  reflectance = Reflectance.get_default_reflectance()
  drivetrain = DifferentialDrive.get_default_differential_drive()
  board = Board.get_default_board()

  threshold = 0.5

  board.wait_for_button()

  while True:
      left = reflectance.get_left()

      if left > threshold:
          drivetrain.stop()
          print("Bounce!")
          drivetrain.turn(180)
      else:
          drivetrain.set_effort(0.3, 0.3)
  ```
- Success criteria:
  - [ ] Robot drives forward and detects the line
  - [ ] Robot turns around when it hits the line
  - [ ] Robot continues driving in the opposite direction
  - [ ] Behavior repeats continuously

**Exercise 2: Both Sensors** (Challenge)
- Goal: Use both sensors — if EITHER sensor detects the line, turn around
- Introduce the `or` operator:
  ```python
  while True:
      left = reflectance.get_left()
      right = reflectance.get_right()

      if left > threshold or right > threshold:
          drivetrain.stop()
          print("Bounce! Left:", left, "Right:", right)
          drivetrain.turn(180)
      else:
          drivetrain.set_effort(0.3, 0.3)
  ```
- Explain: `or` means "if either condition is True, the whole thing is True"
- Question: "Why is this better than checking just one sensor?"

### Assessment

**Formative (during lesson)**:
- Can students write correct `if/else` syntax?
- Do they understand that only one branch executes?
- Can they explain what `while True` does?

**Summative (worksheet/exit ticket)**:
1. Write an `if/else` that checks if a number is positive or negative
2. What is the difference between `if` alone and `if/else`?
3. What happens if we remove `drivetrain.stop()` before `drivetrain.turn(180)`?

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "Both `if` and `else` blocks run" | Only ONE block runs — whichever matches the condition |
| "`while True` will crash the program" | `while True` is normal in robotics; the robot runs until powered off |
| "The robot automatically stops at the line" | The robot only stops if YOUR code tells it to stop |
| "`if/else` checks happen once" | Inside `while True`, the check happens every iteration |
| "`or` means both must be true" | `or` means at least one must be true; `and` means both must be true |

## Differentiation

**For struggling students**:
- Start with just `if` (no `else`) — stop when line detected, no bounce yet
- Add the turn, then add the `else` clause
- Provide complete working code; ask them to modify the turn angle

**For advanced students**:
- Add a bounce counter that prints how many times the robot has bounced
- Try `drivetrain.turn(90)` instead of 180 and observe the different behavior
- Add `elif` (else-if) to handle a third condition

## Materials & Code Examples

### Complete Bounce Program
```python
from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board

reflectance = Reflectance.get_default_reflectance()
drivetrain = DifferentialDrive.get_default_differential_drive()
board = Board.get_default_board()

threshold = 0.5
bounce_count = 0

board.wait_for_button()

while True:
    left = reflectance.get_left()
    right = reflectance.get_right()

    if left > threshold or right > threshold:
        drivetrain.stop()
        bounce_count = bounce_count + 1
        print("Bounce #", bounce_count)
        drivetrain.turn(180)
    else:
        drivetrain.set_effort(0.3, 0.3)
```

## Teaching Notes
- **`while True` safety**: Remind students the only way to stop is turning off the robot or pressing the stop button
- **Turning accuracy**: `drivetrain.turn(180)` may not turn exactly 180° — this is expected on real hardware
- **Observation time**: The robot bounces fast. Have students watch carefully or add a `time.sleep(0.5)` after the turn

## Connections to Next Lessons
- **Lesson 4** will fix a problem: the robot bounces on the same line repeatedly. Random turns will break this pattern.
- `if/else` is used extensively in Lessons 5–10 for decision making
- `while True` becomes the standard pattern for all robot control loops
