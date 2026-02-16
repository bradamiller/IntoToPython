# Lesson 8: Hello, Python

**Module:** 1 — Learning How to Drive the Robot  
**Phase:** C — Transition to Python  
**Duration:** 50–60 minutes (or 25–30 minutes in a 3-hour format)  
**Target Audience:** High school students; have completed Lessons 1–7 (Blockly foundation)

---

## Learning Objectives

By the end of this lesson, students will be able to:
- Understand what Python is and why we're learning it (vs. Blockly)
- Read and translate Blockly blocks to Python code
- Understand basic Python syntax (indentation, colons, capitalization)
- Use the XRPLib library to control the robot in Python
- Write and run a simple Python program on the XRP robot
- Use `print()` to debug and display messages
- Understand the difference between Blockly (visual) and Python (text) programming

---

## Key Concepts

- **Python:** A text-based programming language. More powerful and flexible than visual blocks, but requires learning syntax rules.
- **Syntax:** The rules of how to write Python code (indentation matters, colons at end of lines, etc.)
- **Libraries:** Collections of pre-written code. XRPLib is a library that gives us robot control functions.
- **Imports:** Bringing in a library with `from ... import ...`
- **Functions:** Reusable named blocks of code. In Python, you write `function_name()` to call them.
- **print():** A built-in Python function that displays text in the console (useful for debugging).

---

## Materials & Prerequisites

**Hardware:**
- 1 XRP robot (per student or pair)
- USB cable (robot to computer)
- Fully charged battery

**Software:**
- VS Code (or similar Python IDE) with MicroPython extension
- XRPLib installed (see teacher-guide/xrp-setup-guide.md)
- Blockly reference (screenshots from previous lessons)

**Physical Setup:**
- Open floor or whiteboard for testing

**Prerequisites:**
- Completed Lessons 1–7 (Blockly foundation)
- Familiar with Drive and Turn blocks
- Understand command sequencing
- Have written and uploaded at least 2 Blockly programs

---

## Lesson Flow

### Introduction (5–10 minutes)

**Hook:** Show the same program in two forms:
- Left side: Blockly blocks (visual, from a previous lesson)
- Right side: Python code (text)

Ask: "These do the same thing, but one is visual blocks and one is text. Can you tell which is which? Why would someone use text instead of blocks?"

**Learning Goal:** "Today, you'll learn to write Python code. It's more powerful, and professional programmers use it. But you already know the ideas from Blockly—we're just writing them differently."

### Direct Instruction: Python Intro (10–15 minutes)

**Part 1: Why Python? (3 min)**

Explain (simply):
- Blockly is great for learning (visual, hard to mess up syntax)
- Python is what real programmers use (more flexible, can do more)
- Many industries use Python: data science, web apps, robotics, AI
- XRP robots can run full Python programs (more advanced than Blockly)

**Part 2: Python vs. Blockly (7–10 min)**

Show side-by-side examples:

**Example 1: Drive Forward**

Blockly block:
```
Drive forward for 30 cm at 50%
```

Python code:
```python
from XRPLib.differential_drive import DifferentialDrive

drivetrain = DifferentialDrive.get_default_differential_drive()
drivetrain.straight(30)
```

Explain what's happening:
- Line 1: Import (bring in) the robot control library
- Line 3: Get the drivetrain object ("the robot's wheels")
- Line 4: Tell the drivetrain to drive straight 30 cm

**Example 2: Drive and Message**

Blockly:
```
Drive forward 30 cm at 50%
"Driving forward!" (in a say/print block)
```

Python:
```python
drivetrain.straight(30)
print("Driving forward!")
```

Point out:
- `print()` displays a message
- Parentheses `()` with content inside
- Quotation marks `"..."` around text

**Example 3: Repeat / Loop**

Blockly:
```
Repeat 4 times:
  Drive forward 30 cm
  Turn right 90°
```

Python:
```python
for i in range(4):
    drivetrain.straight(30)
    drivetrain.turn(90)
```

Explain:
- `for i in range(4):` means "do this 4 times"
- Everything indented under the `for` is what repeats
- **Indentation (spaces) is very important in Python**

**Part 3: Python Syntax Rules (3–5 min)**

Key rules to remember:
1. **Indentation:** Spaces at start of line; must be consistent (code inside a loop/function must be indented)
2. **Colons `:` ** After `for`, `if`, function definitions, etc.
3. **Capitalization:** `print` is lowercase, not `Print`
4. **Parentheses `()`:** Function calls need parentheses, even if there's nothing inside
5. **Quotes:** Strings (text) go in quotes: `"hello"` or `'hello'`

Show a deliberately wrong example:
```python
# WRONG:
Print("hello")  # Should be print, not Print
drivetrain.straight 30  # Missing parentheses
```

Have students spot the errors.

### Guided Practice & Worked Example (15–20 minutes)

**Worked Example: "Drive Forward and Back" in Python**

Build this program step-by-step on the screen:

```python
from XRPLib.differential_drive import DifferentialDrive

# Get the robot object
drivetrain = DifferentialDrive.get_default_differential_drive()

# Drive forward
print("Driving forward...")
drivetrain.straight(30)

# Drive backward
print("Driving backward...")
drivetrain.straight(-30)

# Done
print("Done!")
```

Explain each line:
- **Line 1:** Import the DifferentialDrive class (robot control)
- **Line 3:** Create a `drivetrain` object (this is the robot's wheels)
- **Line 6–7:** Print a message and drive forward 30 cm
- **Line 10–11:** Print, then drive backward (negative distance)
- **Line 14:** Final message

**Activity 1: Walk Through the Program**

Ask students:
- "What will the robot do?"
- "What will be printed on the screen?"
- "Why does the second distance have a minus sign?"

Run the program while students watch. Point out the printed messages in the console.

**Activity 2: Modify and Re-Run**

Change one thing:
```python
drivetrain.straight(40)  # Changed from 30 to 40
```

Run again. Ask: "Did anything different happen?"

### Independent Practice (15–20 minutes)

**Exercise 1: Rewrite "Drive Forward and Back" (Scaffolded)**

**Instructions:**

1. Open VS Code
2. Create a new file called `lesson_08_ex1.py`
3. Copy this starter code:

```python
from XRPLib.differential_drive import DifferentialDrive

drivetrain = DifferentialDrive.get_default_differential_drive()

# TODO: Add print statement
# TODO: Drive forward 30 cm
drivetrain.straight(30)

# TODO: Add print statement
# TODO: Drive backward 30 cm
drivetrain.straight(-30)

print("Done!")
```

4. Replace each `# TODO:` with actual code
5. For example, replace `# TODO: Add print statement` with `print("Driving forward...")`
6. Upload and run on your robot

**Success Criteria:**
- [ ] Code runs without syntax errors
- [ ] Robot drives forward, then backward
- [ ] Print statements display messages in console (you see "Driving forward..." when it runs)
- [ ] You understand what each line does

**Reflection Questions:**
1. What does `from ... import` do?
2. Why does `drivetrain.straight(-30)` drive backward?
3. What would happen if you forgot the colons in `from ... import ...:`?

---

**Exercise 2: Add More Driving Commands (Challenge)**

**Instructions:**

Extend Exercise 1 to include turns:

```python
from XRPLib.differential_drive import DifferentialDrive

drivetrain = DifferentialDrive.get_default_differential_drive()

print("Starting...")

# Drive in an L-shape
drivetrain.straight(30)  # Forward
drivetrain.turn(90)      # Turn right 90 degrees
drivetrain.straight(30)  # Forward again

print("Done!")
```

**Tasks:**
1. Type this code (don't copy-paste; typing helps you learn syntax)
2. Upload and run
3. Modify it to make a different shape (try a Z-shape or triangle)
4. Add print statements between each command

**Success Criteria:**
- [ ] Code runs
- [ ] Robot moves in the pattern you intended
- [ ] Print statements mark each step

---

## Common Misconceptions

| Misconception | Reality | How to Address |
|---|---|---|
| "Python code is just Blockly written out" | Similar logic, but Python has strict syntax rules; can't be flexible | Show example error: missing colon breaks code |
| "Indentation doesn't matter" | **Indentation is mandatory** in Python; it defines code blocks | Show how indented code is inside a loop vs. outside |
| "I can use any capitalization" | Function names are case-sensitive; `print` ≠ `Print` | Show error message when wrong capitalization |
| "The colons are optional" | Colons `:` are required after `for`, `if`, `def`, etc. | Show syntax error when colon is missing |
| "`print()` is for final output only" | `print()` is a debugging tool; use it to show what's happening | Encourage liberal use: `print("Before turn")` |

---

## Assessment

**Formative Assessment (During Lesson):**
- Can students read and understand Blockly-to-Python translations?
- Do they understand indentation?
- Can they spot syntax errors?

**Summative Assessment (End of Lesson):**
Students successfully complete Exercise 1:
- Code runs without syntax errors
- Robot drives forward and backward as intended
- Print statements work and display messages

**Grading (if using a rubric):**
- [ ] Code has correct imports (10 pts)
- [ ] Syntax is correct (indentation, colons, capitalization) (15 pts)
- [ ] Robot drives as intended (15 pts)
- [ ] Print statements included and work (5 pts)
- [ ] Can explain syntax rules (5 pts)
- **Total: 50 pts** (or "Complete/Not Yet")

---

## Extensions & Differentiation

### For Students Who Need More Challenge

**Extension 1: Loop and Polygon**

Write a program that draws a square using a `for` loop:

```python
for i in range(4):
    drivetrain.straight(30)
    drivetrain.turn(90)
```

Challenge: Modify to draw a triangle (3 sides, 120° turns).

**Extension 2: Debug Syntax Errors**

Provide students with a buggy program and ask them to find and fix errors:

```python
from XRPLib.differential_drive import DifferentialDrive

drivetrain = DifferentialDrive.get_default_differential_drive()

# Errors in the code below (on purpose):
print("Driving...")
drivetrain.straight(30)  # Missing the colon in the print line above!
Print("Backing up")      # Capital P - should be lowercase
drivetrain.straight(-30)
```

Ask: "What's wrong? Fix it."

**Extension 3: Print Robot Position**

(If time permits) Show how to get encoder position:

```python
drivetrain.reset_encoder_position()
drivetrain.straight(30)
position = drivetrain.get_left_encoder_position()
print(f"Robot is at {position} cm")
```

### For Students Who Need More Support

**Scaffolded Exercise:**

Provide complete starter code with only one part missing:

```python
from XRPLib.differential_drive import DifferentialDrive

drivetrain = DifferentialDrive.get_default_differential_drive()

# YOUR TASK: Replace the ??? with a print statement
???

drivetrain.straight(30)
print("Done!")
```

Ask: "What should go in the ????"

**Pair Programming:**

- Pair confidence students together
- One types, one reads aloud what the code does
- Rotate roles

**Provide a Syntax Checklist:**

Before uploading, check:
- [ ] Does every `for` have a `:` at the end?
- [ ] Is `print` spelled correctly (lowercase)?
- [ ] Do all parentheses match (every `(` has a `)`)?
- [ ] Are strings in quotes?
- [ ] Is indentation consistent?

---

## Resources

- **XRPLib Documentation:** https://open-stem.github.io/XRP_MicroPython/
- **Python Official Docs:** https://www.python.org/doc/
- **VS Code:** https://code.visualstudio.com/
- **MicroPython:** https://micropython.org/

---

## Teacher Notes

### Key Teaching Points

1. **Frame Python as "The Next Level":** Not harder, just different. Same ideas, different syntax.
2. **Indentation is the biggest hurdle:** Spend time on this. Show how tabs vs. spaces matter.
3. **Encourage `print()` use:** It's a debugging superpower. Liberal use is good.
4. **Let students make syntax mistakes:** Errors are learning; show how to read error messages.

### Setup Checklist

- [ ] VS Code installed and XRPLib library working on all student computers
- [ ] Test a program upload before class (no surprises)
- [ ] Have a reference card with syntax rules available
- [ ] Have example programs printed or on screen for reference

### Pacing Notes

- **Full lesson (50–60 min):** Do both exercises, allow tinkering
- **Abbreviated (25–30 min in 3-hour):** Do worked example + Exercise 1, preview Exercise 2 for next time

### Common Technical Issues

**Issue:** Import errors (can't find XRPLib)
- **Fix:** Ensure XRPLib is properly installed; check PYTHONPATH

**Issue:** Indentation errors (code not running)
- **Fix:** Show how tabs and spaces cause problems; use IDE with auto-indent

**Issue:** Robot doesn't move after upload**
- **Fix:** Make sure no syntax errors; check battery; check USB connection

---

## Transition to Next Lesson

"We've now written Python code! Next lesson, we'll use `for` loops to make the robot draw shapes. You'll see how powerful loops are—instead of writing the same commands over and over, you write them once and loop!"

---

## Files

- **Starter Code:** See `module-01-driving/code/starter/lesson-08-hello-python-starter.py`
- **Solution Code:** See `module-01-driving/code/solutions/lesson-08-hello-python-solution.py`
- **Worksheet:** See `module-01-driving/worksheets/08-blockly-to-python-mapping.md`
- **Slides:** See `module-01-driving/slides/08-hello-python-slides.md`

---

## Feedback & Iteration

After teaching this lesson:
- Did syntax rules (especially indentation) sink in?
- How many students struggled with the IDE setup?
- Did print() make sense?
- What was the biggest confusion point?

Use this feedback to adjust Lesson 9 (Loops in Python).
