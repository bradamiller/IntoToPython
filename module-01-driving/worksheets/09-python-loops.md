# Lesson 9 Worksheet: Python Loops

**Name:** __________________ **Date:** __________________ **Team:** __________________

## Part 1: Syntax Matching

Match each Python syntax element to its meaning.

| Syntax | Meaning |
|---|---|
| `for` | A) The variable that counts during loop |
| `i` | B) Keyword that starts a loop |
| `in` | C) Pre-built function that generates numbers |
| `range()` | D) Keyword showing which collection to iterate over |
| `:` | E) Required punctuation after for statement |

## Part 2: Understanding range()

Fill in what numbers `range()` generates:

| Code | Numbers Generated |
|---|---|
| `range(4)` | 0, 1, 2, _____ |
| `range(5)` | 0, 1, 2, _____, _____ |
| `range(3)` | _____, _____, _____ |
| `range(10)` | 0, 1, 2, ..., _____ |

**Key insight:** `range(n)` generates _____ numbers, from _____ to n-1.

## Part 3: Loop Variable Usage

For each loop, predict what will be printed:

**Loop A:**
```python
for i in range(3):
    print(i)
```

Output:
```
_____
_____
_____
```

**Loop B:**
```python
for i in range(4):
    print(f"Iteration {i+1}")
```

Output:
```
Iteration _____
Iteration _____
Iteration _____
Iteration _____
```

**Loop C:**
```python
for number in range(5):
    print(number * 2)
```

Output:
```
_____
_____
_____
_____
_____
```

## Part 4: Convert Blockly to Python

Convert each Blockly program to Python syntax:

**Blockly A:**
```blockly
Repeat 4 times:
  Straight(30)
  Turn(90)
```

**Python:**
```python
for _____ in range(_____):
    ___________________
    ___________________
```

**Blockly B:**
```blockly
Repeat 6 times:
  Print "Hello"
```

**Python:**
```python
for _____ in range(_____):
    print("_____")
```

## Part 5: Indentation Identification

Mark which lines are INSIDE the loop (indented) and which are OUTSIDE:

```python
for i in range(3):
    print("Starting loop")        ☐ Inside  ☐ Outside
    drivetrain.straight(30)       ☐ Inside  ☐ Outside
    print("Loop complete")        ☐ Inside  ☐ Outside
print("All done!")                ☐ Inside  ☐ Outside
```

## Part 6: Spot the Error

Each code snippet has a syntax error. Circle the error and write what's wrong:

**Error 1:**
```python
for i in range(4)
    drivetrain.straight(30)
```

Problem: ________________________________________________________________


**Error 2:**
```python
for i in range(3):
drivetrain.straight(30)
drivetrain.turn(90)
```

Problem: ________________________________________________________________


**Error 3:**
```python
for i in range(5):
    print(i)
    print(i)
print(i)  ← Will this work?
```

Problem: ________________________________________________________________

## Part 7: Loop Design Challenge

Write a Python loop for each task:

**Task 1: Print numbers 1 through 5**
```python
for _____ in range(_____):
    print(_____)
```

**Task 2: Draw a square**
```python
for i in range(_____):
    drivetrain.straight(30)
    drivetrain.turn(90)
```

**Task 3: Repeat "Go Robot!" 3 times**
```python
for _____ in range(_____):
    print("Go Robot!")
```

## Part 8: Loop with Calculation

What does this loop do? Trace through it:

```python
for i in range(4):
    sides = i + 3
    angle = 360 / sides
    print(f"Shape {i}: {sides} sides, {angle}° angle")
```

**Output:**
```
Shape ____: ____ sides, ____° angle
Shape ____: ____ sides, ____° angle
Shape ____: ____ sides, ____° angle
Shape ____: ____ sides, ____° angle
```

## Part 9: Nested Loops (Advanced)

What's the output of this nested loop?

```python
for i in range(2):
    for j in range(3):
        print(f"{i},{j}")
```

**Output:**
```
_____
_____
_____
_____
_____
_____
```

How many lines printed? _____

## Part 10: Real Code - Drawing Polygons

Complete this real program:

```python
from XRPLib.differential_drive import DifferentialDrive

drivetrain = DifferentialDrive.get_default_differential_drive()

# Draw a triangle (3 sides, 120° angles)
for _____ in range(_____):
    drivetrain.straight(25)
    drivetrain.turn(120)

print("Triangle complete!")
```

## Part 11: Comparison

**Without a loop (Blockly-style):**
```python
drivetrain.straight(30)
drivetrain.turn(90)
drivetrain.straight(30)
drivetrain.turn(90)
drivetrain.straight(30)
drivetrain.turn(90)
drivetrain.straight(30)
drivetrain.turn(90)
```

Number of lines: _____

**With a loop (Python):**
```python
for i in range(4):
    drivetrain.straight(30)
    drivetrain.turn(90)
```

Number of lines: _____

**Advantage of using a loop:** ____________________________________________

## Assessment

**Write a Python loop that draws a pentagon (5 sides):**

```python
for _____ in range(_____):
    drivetrain.straight(_____)
    drivetrain.turn(_____)
```

**Verify your answer:**
- For a pentagon: 5 sides, angle = 360/5 = _____°
- Your loop turns: _____ degrees total (5 × _____° per turn)
- Is the total close to 360°? YES / NO

## Reflection

**Which was harder: Blockly Repeat blocks or Python for loops?**

_________________________________________________________________

**Explain what the loop variable (i) does:**

_________________________________________________________________

_________________________________________________________________
