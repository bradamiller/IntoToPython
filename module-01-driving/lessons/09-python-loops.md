# Lesson 9: Python Loops

## Overview
Students learn text-based loop syntax in Python, translating the Blockly Repeat blocks from Lessons 2-5 into `for` loops. This lesson bridges visual to text-based programming, emphasizing that the logic remains the same—only the syntax changes. Students will run loops on the robot to draw shapes, reinforcing that Python and Blockly produce identical robot behavior.

## Learning Objectives
By the end of this lesson, students will be able to:
- Convert Blockly Repeat blocks to Python `for` loops
- Write and execute `for` loops in Python
- Understand loop variables (iteration counter)
- Use indentation to define loop bodies
- Recognize when to use loops (repetition, drawing patterns)
- Debug Python syntax errors (indentation, colons)

## Key Concepts
- **for loop syntax**: `for i in range(n): [statements]`
- **Indentation**: Defines loop body (critical in Python)
- **range()**: Built-in function that generates numbers
- **Loop variable**: Counter (often named `i`) used inside loop
- **Scope**: Loop variables exist for loop duration
- **Equivalence**: Blockly Repeat block = Python for loop (same logic, different syntax)

## Materials Required
- XRP Robot with clear driving space
- VS Code with Python installed
- XRPLib imported and configured
- Reference: Lesson 8 Python code and Blockly Repeat examples from Lessons 2-5
- Whiteboard for syntax breakdown

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 7 min
**For 3-hour sessions:** 10-12 min

1. **Hook: Blockly to Text Translation**:
   - Show Blockly Repeat block side-by-side with Python for loop
   - Ask: "Same logic, different looks—what changed?"
   - Students identify: Different syntax, but still 'repeat this N times'

2. **Why loops?** (Quick review):
   - Drawing shapes (square: 4 sides, triangle: 3 sides)
   - Repeating actions (blink LED 5 times, drive in circles)
   - Avoiding code duplication (don't write straight() four times)

3. **Introduce for Loop Syntax**:
   - Show basic structure:
     ```python
     for i in range(4):
         drivetrain.straight(30)
         drivetrain.turn(90)
     ```
   - Explain each part:
     - `for`: Keyword meaning "repeat"
     - `i`: Loop counter (starts at 0, goes to 3 for range(4))
     - `in range(4)`: Generate numbers 0, 1, 2, 3
     - `:`: Tells Python "loop body follows"
     - Indentation: Which lines are inside the loop
   
4. **Syntax Emphasis**:
   - Indentation is CRITICAL (not just style, it's syntax)
   - Colon `:` is required after the for statement
   - Python counts from 0, not 1 (range(4) gives 0, 1, 2, 3)

### Guided Practice: Square with for Loop (15 minutes)
**For 50-min classes:** 12 min
**For 3-hour sessions:** 15-20 min

1. **Start with Lesson 8 Code**:
   - Open the hello-python.py file from Lesson 8
   - Review: Import DifferentialDrive, create drivetrain, call methods

2. **Introduce Loop Version**:
   - Show completed square loop code:
     ```python
     from XRPLib.differential_drive import DifferentialDrive
     
     drivetrain = DifferentialDrive.get_default_differential_drive()
     
     # Draw a square
     for i in range(4):
         drivetrain.straight(30)
         drivetrain.turn(90)
     
     print("Square complete!")
     ```

3. **Line-by-Line Breakdown**:
   - `for i in range(4):` - Start loop, repeat 4 times
   - `i` - Counter variable (we have access to it, but don't use it here)
   - First indented statement: `drivetrain.straight(30)` - Part of loop body
   - Second indented statement: `drivetrain.turn(90)` - Part of loop body
   - `print("Square complete!")` - Not indented, so runs AFTER loop completes

4. **Indentation Deep Dive**:
   - Show incorrect version (no indentation):
     ```python
     for i in range(4):
     drivetrain.straight(30)  # ERROR: Expected indentation!
     drivetrain.turn(90)
     ```
   - Show correct version:
     ```python
     for i in range(4):
         drivetrain.straight(30)  # Indented = inside loop
         drivetrain.turn(90)      # Indented = inside loop
     ```
   - Explain: Both lines must be indented by same amount (4 spaces or 1 tab)
   - VS Code auto-indentation helps, but watch for inconsistency

5. **Using the Loop Variable**:
   - Show example where `i` is actually used:
     ```python
     for i in range(4):
         print(f"Side {i+1} of square")
         drivetrain.straight(30)
         drivetrain.turn(90)
     ```
   - Output: "Side 1 of square", "Side 2 of square", etc.
   - Explain: `i` goes 0, 1, 2, 3; `i+1` goes 1, 2, 3, 4 (more intuitive)
   - f-string syntax: `f"text {variable} more text"` - inserts variable

6. **Demo & Test**:
   - Upload and run the square program
   - Observe: Robot draws a square (same as Lesson 8, but different code style)
   - Celebrate: "You've written Python loops!"

### Independent Practice: Shapes with for Loops (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

**Exercise 1: Triangle with for Loop**
- Goal: Write a loop to draw a triangle
- Scaffold:
  - Hint 1: How many sides? (3)
  - Hint 2: Loop: `for i in range(3):`
  - Hint 3: Turn angle: 120°
- Students write:
  ```python
  for i in range(3):
      drivetrain.straight(25)
      drivetrain.turn(120)
  ```
- Test on robot
- Question: "What if you wanted to print which side you're on?" (Use `print(f"Side {i+1}")`)

**Exercise 2: Pentagon with Loop & Loop Variable**
- Goal: Draw a pentagon and print progress
- Starter code provided:
  ```python
  for i in range(5):
      print(f"Drawing side {i+1}...")
      drivetrain.straight(20)
      drivetrain.turn(72)
  ```
- Task: Modify the message (e.g., "Pentagon side 1 of 5")
- Enhancement: Add `print(f"Angle this turn: {360/5}°")` inside the loop
- Challenge: Calculate angle dynamically instead of hardcoding 72

**Exercise 3: Nested Loops** (Advanced)
- Goal: Draw multiple shapes in sequence
- Concept: Loop inside loop
- Code:
  ```python
  sides_list = [3, 4, 5]  # Draw triangle, square, pentagon
  
  for num_sides in sides_list:
      angle = 360 / num_sides
      for i in range(num_sides):
          drivetrain.straight(20)
          drivetrain.turn(angle)
      
      print(f"Completed {num_sides}-sided polygon!")
      time.sleep(1)  # Wait 1 second between shapes
  ```
- Explanation: Outer loop iterates over shapes; inner loop draws each shape
- Challenge: What if you want to draw each shape twice? (Add another nested loop or use `range(2)`)

**Exercise 4: Loop with Conditional** (Bridge to Lesson 10)
- Goal: Modify loop behavior based on iteration
- Code:
  ```python
  for i in range(8):
      if i < 4:
          drivetrain.straight(30)  # First 4 sides are long
      else:
          drivetrain.straight(15)  # Last 4 sides are short
      
      drivetrain.turn(45)
  ```
- Result: Octagon with alternating side lengths
- Discussion: "When would you use this pattern?" (Variable speed, changing power, conditional actions)

### Assessment

**Formative (during lesson)**:
- Can students write correct for loop syntax?
- Do they understand indentation and its role?
- Can they identify what the loop counter represents?
- Can they convert Blockly Repeat to Python for?

**Summative (worksheet/exit ticket)**:
1. Write a for loop to print numbers 1 to 5
2. Write a for loop to draw a hexagon (6 sides, 60° angle)
3. Identify the error in this code (indentation problem):
   ```python
   for i in range(3):
   print(f"Loop iteration {i}")
       drivetrain.straight(20)
   ```
4. Predict: What will this code do?
   ```python
   for i in range(4):
       print(i)
   ```

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "Python counts from 1" | Python counts from 0; range(4) gives 0,1,2,3 |
| "Indentation is optional" | Indentation DEFINES scope in Python; it's mandatory syntax |
| "range(4) gives 0,1,2,3,4" | range(4) gives 0,1,2,3 (stops before 4) |
| "The loop variable must be named 'i'" | Any name works: `for side in range(4):` is valid |
| "I can use the loop variable before the loop" | Loop variables only exist during loop execution |
| "A loop that runs 4 times has range(5)" | A loop that runs 4 times has range(4) |

## Differentiation

**For struggling students**:
- Provide completed loop code; ask them to predict output before running
- Use simple examples first (counting, printing) before moving to robot control
- Emphasize indentation with visual guides (editor should show it)
- Practice with small loops (range(2), range(3)) before complex ones
- Use the interactive Python shell to practice: `for i in range(3): print(i)`

**For advanced students**:
- Challenge: Write a nested loop that draws 5 squares in different locations
- Research: `enumerate()` function and how it provides both index and value
- Extend: Use loops with lists—`for shape in ["circle", "square"]: print(shape)`
- Optimization: Measure performance—does loop overhead matter for 100+ iterations?
- Design: Create a program that draws a complex pattern using multiple nested loops

## Materials & Code Examples

### Basic for Loop (Square)
```python
from XRPLib.differential_drive import DifferentialDrive

drivetrain = DifferentialDrive.get_default_differential_drive()

for i in range(4):
    drivetrain.straight(30)
    drivetrain.turn(90)

print("Square drawn!")
```

### Loop with Loop Variable
```python
for i in range(5):
    print(f"Side {i+1} of pentagon")
    drivetrain.straight(20)
    drivetrain.turn(72)
```

### Nested Loops
```python
import time

for shape_count in range(2):
    print(f"Drawing shape {shape_count + 1}")
    for i in range(4):
        drivetrain.straight(25)
        drivetrain.turn(90)
    time.sleep(2)
```

### Loop with Conditional
```python
for i in range(8):
    if i % 2 == 0:  # Even iterations
        drivetrain.straight(30)
    else:  # Odd iterations
        drivetrain.straight(15)
    drivetrain.turn(45)
```

## Teaching Notes
- **Indentation errors are common**: Use an editor with visible whitespace/indentation helpers
- **range() confusion**: Emphasize that range(4) stops BEFORE 4; it's exclusive
- **Loop variable naming**: Encourage meaningful names (`for side in range(4):`) over `i`
- **Off-by-one errors**: Most common error—check range values carefully
- **Performance**: Python loops are fast enough for this use case; optimization not needed yet
- **Testing strategy**: Test each loop independently before combining
- **Success criteria**: Program runs without syntax errors, loop behavior matches prediction, robot performs expected action

## Connections to Next Lessons
- **Lesson 10: Python Functions** will use loops inside functions (combining both concepts)
- **Lesson 11: Final Project** will combine loops, functions, parameters, and conditionals
- Advanced modules may use loops for line-following, sensor polling, and complex patterns
