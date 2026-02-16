# Lesson 4 Worksheet: Parameters & Customization

**Name:** __________________ **Date:** __________________ **Team:** __________________

## Part 1: Parameters vs. Arguments

Fill in the table to show the difference.

| Concept | Definition | Example |
|---|---|---|
| **Parameter** | Variable in the function definition | In `draw_square(size)`, the ___________ is the parameter |
| **Argument** | Value passed when calling the function | In `draw_square(30)`, the ___________ is the argument |

## Part 2: Function with Parameters

Given this function:

```blockly
Function: draw_square(size)
  Repeat 4 times:
    Straight(size)
    Turn(90°)
```

Fill in the table showing what happens with each call:

| Function Call | Parameter Value | Expected Behavior |
|---|---|---|
| `draw_square(20)` | size = _____ | Robot draws a __________ square |
| `draw_square(50)` | size = _____ | Robot draws a __________ square |
| `draw_square(35)` | size = _____ | Robot draws a __________ square |

## Part 3: Design Functions with Parameters

For each scenario, identify what parameters are needed:

**Scenario 1: You want to draw triangles of different sizes**

Function name: draw_triangle

Parameters needed: ____________________________

Example calls:
- `draw_triangle(25)` - small triangle
- `draw_triangle(40)` - large triangle


**Scenario 2: You want to draw squares at different speeds**

Function name: draw_square

Parameters needed: ____________________________ and ____________________________

Example calls:
- `draw_square(30, 0.5)` - normal speed
- `draw_square(30, 0.9)` - fast


## Part 4: Analyze Parameter Usage

Look at each code snippet and explain what each parameter does:

**Code A:**
```blockly
Function: draw_polygon(sides, distance)
  angle = 360 ÷ sides
  Repeat sides times:
    Straight(distance)
    Turn(angle)
```

- Parameter `sides` controls: ________________________________________________
- Parameter `distance` controls: ________________________________________________


**Code B:**
```blockly
Function: move_robot(speed, time)
  Set effort (left: speed, right: speed)
  Wait time seconds
  Stop motors
```

- Parameter `speed` controls: ________________________________________________
- Parameter `time` controls: ________________________________________________

## Part 5: Parameter Order Matters

Given: `draw_rectangle(length, width)`

**Call 1:** `draw_rectangle(50, 30)` - Long sides 50cm, short sides 30cm

**Call 2:** `draw_rectangle(30, 50)` - Long sides 30cm, short sides 50cm

**Are these the same?** YES / NO

**Explain why parameter order matters:**

_________________________________________________________________

## Part 6: Write Your Own Parameterized Function

Design a function `move_and_turn(distance, angle)` that moves forward then turns.

```blockly
Function name: ________________________

Parameters: 
  1. ________________________
  2. ________________________

Function body:
[Draw or describe the code here]


Example calls:
  move_and_turn(100, 90)
  move_and_turn(50, 45)
```

## Part 7: Trace Function Calls

Follow the program and predict outputs:

```blockly
Function: draw_polygon(sides, size)
  angle = 360 ÷ sides
  Repeat sides times:
    Straight(size)
    Turn(angle)

Main Program:
  Call draw_polygon(4, 30)  ← shapes: ___________
  Call draw_polygon(3, 25)  ← shapes: ___________
  Call draw_polygon(6, 20)  ← shapes: ___________
```

## Part 8: Fix the Code

Each example has an error with parameters. Identify and fix it.

**Error 1:**
```blockly
Function: draw_square(size, effort)
  Repeat 4 times:
    Straight(30)  ← Problem: size parameter not used!
    Turn(90)
```

Fix: ____________________________________________________________________


**Error 2:**
```blockly
draw_square(30)  ← Problem: function expects 2 parameters!
```

The function definition was: `draw_square(size, effort)`

Fix: ____________________________________________________________________


**Error 3:**
```blockly
Function: draw_shape(distance, sides)
  angle = 360 ÷ sides
  Repeat sides times:
    Straight(distance)
    Turn(angle)

Call: draw_shape(25)  ← Missing an argument!
```

Fix: ____________________________________________________________________

## Reflection

**Explain how parameters make a function more flexible and reusable:**

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________
