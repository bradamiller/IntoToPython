# Lesson 3 Worksheet: Introduction to Functions

**Name:** __________________ **Date:** __________________ **Team:** __________________

## Part 1: Function Definition vs. Function Call

Match each description to the correct term.

| Item | Definition | Function Call |
|---|---|---|
| A) Where you WRITE what the function does | | |
| B) Where you USE the function in your program | | |
| C) `draw_square()` in the main program | | |
| D) The `to draw_square` block in Functions category | | |

**Answers:** A = _________, B = _________, C = _________, D = _________

## Part 2: Identify When to Use Functions

For each scenario, write **YES** if you should create a function, or **NO** if you shouldn't.

1. _____ You need to draw 3 identical squares in your program
2. _____ You need to make the robot turn once
3. _____ You're drawing 5 different shapes (square, triangle, pentagon, hexagon, octagon)
4. _____ You need to print "Hello" one time
5. _____ You need to drive forward, then turn, then drive forward again (same sequence, 4 times)

## Part 3: Analyze Function Structure

Look at this function pseudocode and answer the questions:

```
Function: draw_square
  Repeat 4 times:
    Straight(30)
    Turn(90°)
End Function
```

**Questions:**
1. What is the name of this function? ____________________________
2. How many times does the robot go straight? ____________________________
3. What is the turn angle? ____________________________
4. Does this function have parameters (inputs)? YES / NO

## Part 4: Function Design Challenge

Design a function that draws a triangle. Fill in the blanks:

```
Function Name: draw_________

Inputs (parameters): ____________________________

Function Body:
  Repeat ____ times:
    Straight(_____)
    Turn(____)

Calls to this function:
  draw_triangle()
```

## Part 5: Trace Function Execution

Follow the program and predict the output:

```blockly
Function: draw_square
  Repeat 4 times:
    Straight(30)
    Turn(90°)

Main Program:
  Print "Starting"
  Call draw_square()
  Print "Done"
```

**What is printed and in what order?**

1. ____________________________
2. ____________________________
3. ____________________________

**What shape does the robot draw?**

____________________________

## Part 6: Identify Errors

Each code snippet has a mistake. Write what's wrong.

**Error 1:**
```blockly
Function: move_forward
  Straight(50)
  Straight(50)

Call move_forward()
Call move_forward()
Call move_forward()
```

Problem: ________________________________________________________________

What should you do instead? _______________________________________________


**Error 2:**
```blockly
Function: draw_triangle
  Repeat 3 times:
    Straight(25)
    Turn(120°)

Main Program:
  Call draw_square()  ← Problem here
```

Problem: ________________________________________________________________

Fix: ____________________________________________________________________

## Part 7: Code Comparison

**Without Functions:**
```blockly
Repeat 4 times:
  Straight(30)
  Turn(90°)

Repeat 4 times:
  Straight(30)
  Turn(90°)

Repeat 4 times:
  Straight(30)
  Turn(90°)
```

**With Functions:**
```blockly
Function: draw_square
  Repeat 4 times:
    Straight(30)
    Turn(90°)

Call draw_square()
Call draw_square()
Call draw_square()
```

**How many lines of code without functions?** ________

**How many lines of code with functions?** ________

**Which is easier to change if you want bigger squares?** ________

## Reflection

**Explain why functions are useful in your own words:**

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________
