# Lesson 8 Slide Outline: Hello, Python

## Slide 1: Title & Learning Objectives
**Title:** Hello, Python

**Learning Objectives:**
- Understand what Python is and why we're learning it
- Read and translate Blockly blocks to Python code
- Understand basic Python syntax (indentation, colons, capitalization)
- Use the XRPLib library to control the robot in Python
- Write and run a simple Python program on the XRP robot

**Agenda:**
- Why Python? (5 min)
- Blockly vs. Python side-by-side (10 min)
- Python syntax rules (5 min)
- Guided: Drive forward and back (10 min)
- Practice exercises (15 min)

---

## Slide 2: Hook — Same Program, Two Languages
**Show side-by-side:**

**Blockly (Visual):**
```
Drive forward 30 cm at 50%
Turn right 90 degrees
Drive forward 30 cm at 50%
```

**Python (Text):**
```python
from XRPLib.differential_drive import DifferentialDrive
drivetrain = DifferentialDrive.get_default_differential_drive()

drivetrain.straight(30)
drivetrain.turn(90)
drivetrain.straight(30)
```

**Question:** "These do the same thing. Can you match each Blockly block to its Python line?"

**Key message:** Same logic, different syntax. You already know the ideas!

---

## Slide 3: Why Python?
**Blockly is great for learning:**
- Visual, hard to mess up syntax
- Good for getting started quickly

**Python is what professionals use:**
- More powerful and flexible
- Used in data science, web apps, robotics, AI
- XRP robots can run full Python programs

**The transition:**
- You already know the CONCEPTS (sequencing, loops, functions)
- Now you'll learn the SYNTAX (how to write it as text)
- Same ideas, different format

---

## Slide 4: Blockly → Python Translation

**Example 1: Drive Forward**

| Blockly | Python |
|---|---|
| `Drive forward 30 cm` | `drivetrain.straight(30)` |

**Example 2: Turn**

| Blockly | Python |
|---|---|
| `Turn right 90°` | `drivetrain.turn(90)` |

**Example 3: Print a Message**

| Blockly | Python |
|---|---|
| `Say "Hello!"` | `print("Hello!")` |

**Pattern:** Each Blockly block becomes one line of Python code.

---

## Slide 5: The Import Line
**Before using the robot, we need to import the library:**

```python
from XRPLib.differential_drive import DifferentialDrive
drivetrain = DifferentialDrive.get_default_differential_drive()
```

**What this means:**
- Line 1: "Get the DifferentialDrive code from the XRPLib library"
- Line 2: "Create a drivetrain object — this is the robot's wheels"

**Analogy:** Import = opening a toolbox. `drivetrain` = taking out the tool you need.

**You'll type these two lines at the top of every program.**

---

## Slide 6: Python Syntax Rules
**Five rules to remember:**

| Rule | Example | Common Mistake |
|---|---|---|
| Indentation matters | `    drivetrain.straight(30)` | Forgetting to indent inside loops |
| Colons after `for`, `if`, `def` | `for i in range(4):` | Missing the colon |
| Case sensitive | `print()` not `Print()` | Capital letters |
| Parentheses for function calls | `print("hello")` | Missing `()` |
| Quotes around text | `"hello"` or `'hello'` | Forgetting quotes |

**Most common error:** Indentation. Python uses spaces to know what's "inside" a loop or function.

---

## Slide 7: Your First Python Program
**Step-by-step walkthrough:**

```python
from XRPLib.differential_drive import DifferentialDrive

drivetrain = DifferentialDrive.get_default_differential_drive()

print("Driving forward...")
drivetrain.straight(30)

print("Driving backward...")
drivetrain.straight(-30)

print("Done!")
```

**Line by line:**
- Lines 1-3: Setup (import library, get drivetrain)
- Line 5: Print a message to the screen
- Line 6: Drive forward 30 cm
- Line 8: Print another message
- Line 9: Drive backward (negative = backward)
- Line 11: Print "Done!"

---

## Slide 8: print() Is Your Best Friend
**`print()` shows messages on the screen while the robot runs.**

```python
print("Starting the program!")
drivetrain.straight(30)
print("Finished driving forward")
drivetrain.turn(90)
print("Finished turning")
```

**Why use print()?**
- See what the robot is doing at each step
- Find bugs: "It printed 'Finished driving' but didn't turn — the bug is in the turn line!"
- Professional programmers use print() all the time for debugging

**Rule:** When in doubt, add a print statement!

---

## Slide 9: Common Errors and How to Fix Them
**Error 1: NameError**
```python
Print("hello")   # Wrong! Capital P
print("hello")   # Correct
```

**Error 2: SyntaxError (missing colon)**
```python
for i in range(4)    # Wrong! Missing :
for i in range(4):   # Correct
```

**Error 3: IndentationError**
```python
for i in range(4):
print("hello")       # Wrong! Not indented
    print("hello")   # Correct
```

**Error 4: Missing parentheses**
```python
print "hello"        # Wrong! Missing ()
print("hello")       # Correct
```

**Tip:** Read the error message — Python tells you the line number and what's wrong!

---

## Slide 10: Your Turn!
**Exercise 1: Drive Forward and Back**
1. Open VS Code and create a new file
2. Type the starter code (don't copy-paste — typing helps learn syntax!)
3. Fill in the TODO sections
4. Upload and run on your robot

**Exercise 2: L-Shape Challenge**
1. Make the robot drive in an L-shape:
   - Forward 30 cm → Turn right 90° → Forward 30 cm
2. Add print statements between each command
3. Can you make a Z-shape? A U-shape?

**Checkpoints:**
- Does your code run without errors?
- Does the robot move as expected?
- Do print statements show in the console?

---

## Slide 11: Connection to Next Lesson
**What you did today:**
- Learned Python syntax basics
- Translated Blockly blocks to Python
- Wrote and ran your first Python program
- Used print() for debugging

**Next lesson (Lesson 9):**
- Learn `for` loops in Python
- Convert Blockly Repeat blocks to Python loops
- Draw shapes with loops (square, triangle, hexagon)

**Key insight:** You already understand loops from Blockly. Next lesson, you'll just learn how to write them in Python text.
