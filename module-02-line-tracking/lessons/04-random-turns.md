# Lesson 4: Random Turns

## Overview
Students discover a problem with Lesson 3's bounce driving: the robot goes back and forth on the same line, never exploring the full circle. The fix? Randomness. By importing the `random` module and using `random.randint()`, students make the robot turn a random angle each time it bounces, breaking the predictable pattern and keeping the robot inside the circle more effectively.

## Learning Objectives
By the end of this lesson, students will be able to:
- Use `import` to bring in Python's built-in `random` module
- Generate random integers with `random.randint(a, b)`
- Explain why deterministic bounce driving gets stuck in a pattern
- Modify existing code to incorporate randomness
- Understand what a module/library is and how to import one
- Use variables to store and print random values

## Key Concepts
- **`import`**: Brings in code from another module (file) so you can use it
- **Module**: A collection of pre-written functions (like a toolbox)
- **`random` module**: Python's built-in module for generating random numbers
- **`random.randint(a, b)`**: Returns a random integer between `a` and `b` (inclusive)
- **Deterministic vs. random**: Without randomness, the robot always does the same thing

## Materials Required
- XRP Robot with reflectance sensors
- White surface with taped circle
- VS Code with XRPLib installed
- Working bounce-driving code from Lesson 3

## Lesson Flow

### Introduction (10 minutes)

1. **Hook: The Problem with Predictability**:
   - Run the Lesson 3 bounce program and observe
   - Ask: "What path does the robot take?" (Back and forth on the same line)
   - "The robot keeps bouncing on the same two points. It never explores the rest of the circle."
   - "How could we fix this?" (Turn a different amount each time)

2. **Introduce `import`**:
   - Python has thousands of useful tools, organized into modules
   - To use them, we `import` them at the top of our program
   - We've already done this: `from XRPLib.reflectance import Reflectance`
   - For random numbers, we import the `random` module:
     ```python
     import random
     ```
   - Now we can use `random.randint()` to generate random numbers

3. **`random.randint()` Demo**:
   ```python
   import random

   for i in range(5):
       number = random.randint(1, 10)
       print("Random number:", number)
   ```
   - Each time it runs, you get different numbers between 1 and 10
   - `randint(1, 10)` includes both 1 and 10 (inclusive)
   - The "rand" stands for "random", "int" stands for "integer"

### Guided Practice: Adding Randomness to Bounce Driving (15 minutes)

1. **The Fix**:
   - Instead of `drivetrain.turn(180)` every time...
   - Generate a random angle: `angle = random.randint(90, 270)`
   - This gives us a turn between 90° and 270° — enough to change direction but not too small

2. **Updated Program**:
   ```python
   from XRPLib.reflectance import Reflectance
   from XRPLib.differential_drive import DifferentialDrive
   from XRPLib.board import Board
   import random

   reflectance = Reflectance.get_default_reflectance()
   drivetrain = DifferentialDrive.get_default_differential_drive()
   board = Board.get_default_board()

   threshold = 0.5

   board.wait_for_button()
   print("Random bounce driving started!")

   while True:
       left = reflectance.get_left()
       right = reflectance.get_right()

       if left > threshold or right > threshold:
           drivetrain.stop()
           angle = random.randint(90, 270)
           print("Line detected! Turning", angle, "degrees")
           drivetrain.turn(angle)
       else:
           drivetrain.set_effort(0.3, 0.3)
   ```

3. **Explain the Change**:
   - `import random` at the top — makes random functions available
   - `angle = random.randint(90, 270)` — pick a random angle each bounce
   - `drivetrain.turn(angle)` — turn by that random amount
   - `print("Turning", angle, "degrees")` — shows the angle for debugging

4. **Demo & Compare**:
   - Run the new program alongside the old one (mentally or on two robots)
   - The random version explores the whole circle instead of going back and forth

### Independent Practice (20 minutes)

**Exercise 1: Random Bounce Driving**
- Goal: Modify your Lesson 3 bounce program to use random turns
- Steps:
  1. Add `import random` at the top of your Lesson 3 program
  2. Replace `drivetrain.turn(180)` with:
     ```python
     angle = random.randint(90, 270)
     print("Turning", angle, "degrees")
     drivetrain.turn(angle)
     ```
  3. Upload and test — the robot should explore the circle more evenly
- Success criteria:
  - [ ] Robot bounces in different directions each time
  - [ ] Robot stays inside the circle (mostly)
  - [ ] Print output shows different angles each time

**Exercise 2: Tune the Range** (Challenge)
- Goal: Experiment with different random ranges and observe the behavior
- Try these ranges and record what happens:
  - `random.randint(45, 315)` — wider range
  - `random.randint(150, 210)` — narrow range (close to 180)
  - `random.randint(90, 90)` — always turns 90° (is this random?)
- Questions:
  1. Which range kept the robot inside the circle best?
  2. What happens with very small turn ranges (like 10-30)?
  3. What happens if the range includes 0?

**Exercise 3: Random Speed** (Advanced)
- Goal: Randomize both the turn angle AND the driving speed
  ```python
  while True:
      left = reflectance.get_left()
      right = reflectance.get_right()

      if left > threshold or right > threshold:
          drivetrain.stop()
          angle = random.randint(90, 270)
          print("Turning", angle, "degrees")
          drivetrain.turn(angle)
      else:
          speed = random.randint(20, 50) / 100  # 0.2 to 0.5
          drivetrain.set_effort(speed, speed)
  ```

### Assessment

**Formative (during lesson)**:
- Can students use `import random` correctly?
- Do they understand what `randint(a, b)` returns?
- Can they explain why randomness helps?

**Summative (worksheet/exit ticket)**:
1. What does `import random` do?
2. What values could `random.randint(1, 6)` return?
3. Why does always turning 180° cause a problem for bounce driving?

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "`import` runs the module's code" | `import` makes functions available; they run only when called |
| "`random.randint(1, 10)` always gives 10 numbers" | It returns ONE random number each time; call it again for another |
| "`random.randint(1, 10)` can return 0 or 11" | It only returns values between 1 and 10 (inclusive) |
| "Random means the robot will go off the circle" | Random turns keep the robot inside better because it doesn't get stuck |
| "I need to import random inside the loop" | Import once at the top of the file; use it anywhere after that |

## Differentiation

**For struggling students**:
- Provide the complete random bounce program; focus on understanding the output
- Start by just generating and printing random numbers (no robot)
- Use `random.randint(170, 190)` for a small variation that's easy to see

**For advanced students**:
- Add a "dance mode": when the robot bounces 10 times, do a victory spin
- Use `random.choice()` to pick from a list of specific angles: `random.choice([90, 180, 270])`
- Research: What other functions does the `random` module provide?

## Materials & Code Examples

### Complete Random Bounce Program
```python
from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board
import random

reflectance = Reflectance.get_default_reflectance()
drivetrain = DifferentialDrive.get_default_differential_drive()
board = Board.get_default_board()

threshold = 0.5
bounce_count = 0

board.wait_for_button()
print("Random bounce driving started!")

while True:
    left = reflectance.get_left()
    right = reflectance.get_right()

    if left > threshold or right > threshold:
        drivetrain.stop()
        bounce_count = bounce_count + 1
        angle = random.randint(90, 270)
        print("Bounce #", bounce_count, "- Turning", angle, "degrees")
        drivetrain.turn(angle)
    else:
        drivetrain.set_effort(0.3, 0.3)
```

## Teaching Notes
- **`import` placement**: Always at the top of the file — this is a Python convention
- **Determinism as a concept**: This is a good time to discuss why predictability can be bad (and good)
- **Random is not truly random**: Computer random numbers are "pseudo-random" — close enough for our purposes
- **Testing randomness**: Hard to test because output changes every run. Focus on the range being correct.

## Connections to Next Lessons
- **Lesson 5** shifts from "bouncing" to "following" — instead of bouncing off the line, the robot follows it
- `import` will be used again in Module 3+ for other libraries
- The sensor-check-inside-a-loop pattern established here carries forward to all remaining lessons
