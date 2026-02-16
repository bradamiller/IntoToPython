# Lesson 10 Worksheet: Python Functions

**Name:** __________________ **Date:** __________________ **Team:** __________________

## Part 1: Function Anatomy

Label each part of this Python function:

```python
def draw_square(size):
  A) ↑
      for i in range(4):
  B) ↑
          drivetrain.straight(size)  C) ↑
          drivetrain.turn(90)
```

Fill in the table:

| Label | Term | Meaning |
|---|---|---|
| A) | _________________ | Keyword that defines a function |
| B) | _________________ | The code that runs when function is called |
| C) | _________________ | Input to the function |

## Part 2: Syntax Matching - def vs. call

Match each to the correct category:

| Code | Definition | Call |
|---|---|---|
| A) `def draw_square(size):` | ☐ | ☐ |
| B) `draw_square(30)` | ☐ | ☐ |
| C) `def move_forward(distance):` | ☐ | ☐ |
| D) `move_forward(100)` | ☐ | ☐ |

## Part 3: Reading Function Definitions

For each function, identify the name and parameters:

**Function 1:**
```python
def draw_triangle(size, effort):
    angle = 360 / 3
    for i in range(3):
        drivetrain.straight(size, max_effort=effort)
        drivetrain.turn(angle, max_effort=effort)
```

Function name: ____________________________

Parameters: ________________________________

Number of parameters: _____

**Function 2:**
```python
def move_and_report(distance):
    drivetrain.straight(distance)
    print(f"Moved {distance} cm")
```

Function name: ____________________________

Parameters: ________________________________

Number of parameters: _____

## Part 4: Trace Function Execution

Follow this program and predict output:

```python
def greet(name):
    print(f"Hello, {name}!")

print("Before")
greet("Alice")
print("After")
```

**Output (in order):**
1. _______________________________
2. _______________________________
3. _______________________________

## Part 5: Function with Return Value

What does this function return?

```python
def calculate_angle(num_sides):
    return 360 / num_sides

angle = calculate_angle(4)
print(angle)
```

**What is printed?** _______________________________

## Part 6: Write Your Own Function

Write a Python function `draw_hexagon()` that draws a 6-sided shape:

```python
def draw_hexagon(___________):
    angle = 360 / 6
    for i in range(6):
        drivetrain.straight(_____)
        drivetrain.turn(angle)

# Call it:
draw_hexagon(_____)
```

**Parameter name:** ____________________________

**Did you use the parameter in the function body?** YES / NO

## Part 7: Parameters & Arguments

For each function call, fill in what the parameter gets:

```python
def draw_polygon(sides, size):
    angle = 360 / sides
    for i in range(sides):
        drivetrain.straight(size)
        drivetrain.turn(angle)
```

| Function Call | `sides` parameter = | `size` parameter = |
|---|---|---|
| `draw_polygon(4, 30)` | _____ | _____ |
| `draw_polygon(3, 25)` | _____ | _____ |
| `draw_polygon(6, 20)` | _____ | _____ |

## Part 8: Scope - What Variables Exist Where?

Look at this program:

```python
def my_function():
    x = 10
    print(x)

my_function()
print(x)  ← Will this work?
```

**Will `print(x)` work outside the function?** YES / NO

**Why?** _________________________________________________________________

## Part 9: Spot the Errors

Each code snippet has a mistake. Identify and fix it:

**Error 1:**
```python
draw_square(30)

def draw_square(size):
    for i in range(4):
        drivetrain.straight(size)
        drivetrain.turn(90)
```

Problem: ________________________________________________________________

Fix: ____________________________________________________________________

**Error 2:**
```python
def draw_triangle(size, effort)  # Missing something!
    for i in range(3):
        drivetrain.straight(size)
        drivetrain.turn(120)
```

Problem: ________________________________________________________________

Fix: ____________________________________________________________________

**Error 3:**
```python
def get_angle(sides):
    angle = 360 / sides
    # Missing something!

result = get_angle(4)
print(result)  ← What prints?
```

Problem: ________________________________________________________________

Fix: ____________________________________________________________________

## Part 10: Code Comparison - Blockly vs. Python

**Blockly:**
```blockly
Function: draw_square(size)
  Repeat 4 times:
    Straight(size)
    Turn(90°)
```

**Python:**
```python
def draw_square(size):
    for i in range(4):
        drivetrain.straight(size)
        drivetrain.turn(90)
```

**Similarities:** _________________________________________________________

**Differences:** __________________________________________________________

## Part 11: Writing Multiple Functions

Write two functions and then use them together:

```python
def draw_square(size):
    ________________________
    ________________________
    ________________________
    ________________________

def draw_triangle(size):
    ________________________
    ________________________
    ________________________

# Main program:
draw_square(30)
draw_triangle(25)
```

## Part 12: Function Design Analysis

For each problem, identify:
1. Function name (what should it do?)
2. Parameters (what inputs does it need?)
3. Return value (does it produce output?)

**Problem 1: "Calculate how far the robot traveled"**

Function name: ____________________________

Parameters: ________________________________

Returns: ________________________________

**Problem 2: "Draw a shape and move to next location"**

Function name: ____________________________

Parameters: ________________________________

Returns: ________________________________

## Part 13: Default Parameters (Advanced)

What does this code do?

```python
def drive(distance=50):
    drivetrain.straight(distance)

drive()          # ← Uses default
drive(100)       # ← Uses argument
```

**First call uses distance:** _____

**Second call uses distance:** _____

## Assessment

**Write a complete Python function that:**
- Takes a parameter `number_of_sides`
- Takes a parameter `side_length`
- Draws that polygon
- Prints a completion message

```python
def draw_polygon(_____________, _____________):
    angle = 360 / _____________
    
    for i in range(_____________):
        drivetrain.straight(_____________)
        drivetrain.turn(angle)
    
    print("______________________________________________")

# Test it:
draw_polygon(6, 25)
```

## Reflection

**What's the relationship between Python functions and Blockly function blocks?**

_________________________________________________________________

_________________________________________________________________

**When would you create a function vs. writing code directly?**

_________________________________________________________________

_________________________________________________________________
