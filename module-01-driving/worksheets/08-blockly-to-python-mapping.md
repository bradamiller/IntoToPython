# Lesson 8 Worksheet: Blockly to Python Mapping

## Overview

This worksheet helps you see how Blockly visual blocks translate to Python code. Understanding this mapping is the bridge between block-based and text-based programming.

---

## Part 1: Match Blocks to Code

Below are Blockly blocks on the left and Python code snippets on the right. **Draw a line to match each block to the equivalent code.**

### Blockly Block → Python Code

| Blockly | Python |
|---------|--------|
| **Block: Drive forward 30 cm at 50%** | `drivetrain.straight(30)` |
| **Block: Turn right 90°** | `print("Hello!")` |
| **Block: Say/Display "Hello!"** | `drivetrain.turn(90)` |
| **Block: Wait 2 seconds** | `import time` and `time.sleep(2)` |
| **Block: Repeat 4 times: [commands]** | `for i in range(4):` then indented commands |

**Answers:** 
- Drive → `drivetrain.straight(30)`
- Turn → `drivetrain.turn(90)`
- Say → `print("Hello!")`
- Wait → `time.sleep(2)`
- Repeat → `for i in range(4):`

---

## Part 2: Translate Blockly to Python

Convert each Blockly pseudo-program to Python code.

### Example 1: Drive Forward and Back

**Blockly:**
```
Drive forward 30 cm at 50%
Drive backward 30 cm at 50%
```

**Python (you write this):**
```python
drivetrain.straight(30)
drivetrain.straight(-30)
```

Explanation: Negative distance means backward.

---

### Example 2: Drive Forward, Turn, Drive Again

**Blockly:**
```
Drive forward 20 cm at 50%
Turn right 90°
Drive forward 20 cm at 50%
```

**Python (you write this):**
```python
drivetrain.straight(20)
drivetrain.turn(90)
drivetrain.straight(20)
```

---

### Example 3: Repeat (Square)

**Blockly:**
```
Repeat 4 times:
  Drive forward 30 cm
  Turn right 90°
```

**Python (you write this):**
```python
for i in range(4):
    drivetrain.straight(30)
    drivetrain.turn(90)
```

Explanation: 
- `for i in range(4):` means repeat 4 times
- Everything indented below the `for` is repeated
- **Indentation is important!**

---

## Part 3: Translate Python to English

Write what each Python program does in plain English.

### Program 1:
```python
print("Going forward...")
drivetrain.straight(40)
drivetrain.turn(45)
drivetrain.straight(40)
```

**What does it do?**
```
___________________________________________________________________________

___________________________________________________________________________
```

**Answer:** Prints "Going forward...", drives forward 40 cm, turns 45 degrees, then drives forward 40 cm again. The robot ends in a diagonal direction.

---

### Program 2:
```python
for i in range(3):
    print(f"Step {i+1}")
    drivetrain.straight(20)
    drivetrain.turn(120)
```

**What does it do?**
```
___________________________________________________________________________

___________________________________________________________________________
```

**Answer:** Repeats 3 times: prints the step number, drives forward 20 cm, and turns 120 degrees. This draws a triangle.

---

## Part 4: Spot the Syntax Errors

Each program below has **one syntax error**. Find it and fix it.

### Program 1:
```python
drivetrain.straight(30)
print "Driving..."      ← ERROR HERE
drivetrain.turn(90)
```

**Error:** `print` needs parentheses: `print("Driving...")`

---

### Program 2:
```python
for i in range(4)     ← ERROR HERE
    drivetrain.straight(30)
    drivetrain.turn(90)
```

**Error:** Missing colon after `for i in range(4):` — should be `for i in range(4):`

---

### Program 3:
```python
drivetrain.straight(30)
  print("Done")        ← ERROR HERE (spaces don't match)
```

**Error:** Indentation mismatch. `print()` is not inside a loop, so it shouldn't be indented. Should be:
```python
drivetrain.straight(30)
print("Done")
```

---

### Program 4:
```python
from XRPLib.differential_drive import DifferentialDrive

drivetrain = DifferentialDrive.get_default_differential_drive()
Print("Starting...")    ← ERROR HERE
drivetrain.straight(30)
```

**Error:** `Print` should be lowercase: `print("Starting...")`

---

## Part 5: Fill in the Missing Code

Each program is missing one line. Fill in the blank.

### Program 1: Drive and Print
```python
from XRPLib.differential_drive import DifferentialDrive

drivetrain = DifferentialDrive.get_default_differential_drive()

________________  # Print "Driving..."

drivetrain.straight(30)
```

**Answer:** `print("Driving...")`

---

### Program 2: Loop and Turn
```python
_____________ :  # Repeat 3 times
    drivetrain.straight(30)
    drivetrain.turn(120)
```

**Answer:** `for i in range(3)`

---

### Program 3: Get Encoder Position
```python
drivetrain.reset_encoder_position()
drivetrain.straight(50)
position = _______________________________  # Get position
print(f"Robot drove {position} cm")
```

**Answer:** `drivetrain.get_left_encoder_position()`

---

## Part 6: Challenge — Write Your Own

Write Python code for each scenario. (Refer to the XRPLib API reference if needed.)

### Challenge 1: Drive a Square

Write Python code that makes the robot drive a square (4 sides, 30 cm each, 90° turns).

```python
for i in range(4):
    ___________________________
    ___________________________
```

**Answer:**
```python
for i in range(4):
    drivetrain.straight(30)
    drivetrain.turn(90)
```

---

### Challenge 2: Drive Forward, Print, Turn, Print

Write Python code:
1. Print "Driving forward..."
2. Drive forward 40 cm
3. Print "Turning..."
4. Turn right 45 degrees
5. Print "Done!"

```python
_______________________________
_______________________________
_______________________________
_______________________________
_______________________________
```

**Answer:**
```python
print("Driving forward...")
drivetrain.straight(40)
print("Turning...")
drivetrain.turn(45)
print("Done!")
```

---

## Reflection

1. **What's the hardest part about switching from Blockly to Python?**

   Answer: _________________________________________________________________

2. **What's one advantage of Python over Blockly?**

   Answer: _________________________________________________________________

3. **How is indentation important in Python?**

   Answer: _________________________________________________________________

---

## Key Takeaways

✓ Blockly blocks translate directly to Python functions  
✓ Python requires syntax rules (colons, parentheses, indentation)  
✓ `import` brings in libraries like XRPLib  
✓ `print()` displays messages (useful for debugging)  
✓ `for` loops repeat code  
✓ Indentation defines code blocks  

---

**Next:** Lesson 9 will dive deeper into Python loops and how to use them to make complex programs.
