# Lesson 9 Slide Outline: Python Loops

## Slide 1: Title & Learning Objectives
**Title:** Python Loops

**Learning Objectives:**
- Understand for loop syntax in Python
- Use range() to generate sequences
- Convert Blockly repeat blocks to Python for loops
- Apply loops to robot programming

**Agenda:**
- Python syntax introduction (5 min)
- for loop & range() (8 min)
- Guided: Convert Blockly to Python (8 min)
- Practice: Write Python loops (14 min)

---

## Slide 2: Hook - Text Programming Begins
**Blockly vs. Python:**

**Blockly (Visual):**
```
Repeat 4 times:
  [Straight block]
  [Turn block]
```

**Python (Text):**
```python
for i in range(4):
    drivetrain.straight(30)
    drivetrain.turn(90)
```

**Question:** "Can you translate blocks into text code?"

---

## Slide 3: For Loop Syntax
**Python for loop basic structure:**

```python
for i in range(4):
    # Code here runs 4 times
    print("Hello")
```

**Breaking it down:**
- **for** - Keyword: start a loop
- **i** - Loop variable (counts 0, 1, 2, 3)
- **range(4)** - Generate numbers 0 through 3
- **:** - Colon ends the for line
- **Indented code** - Runs each loop iteration

**Key Point:** Indentation matters in Python!

---

## Slide 4: Understanding range()
**range(4) produces:**
```python
range(4) → [0, 1, 2, 3]  # Four values
```

**Examples:**
```python
range(3)  → [0, 1, 2]           # 3 values
range(1)  → [0]                 # 1 value
range(0)  → []                  # 0 values (empty)
range(10) → [0, 1, 2, ... 9]   # 10 values
```

**The Rule:** range(n) gives n values: 0 to n-1

**For Robots:**
```python
for i in range(4):        # Loop 4 times
    # ... do something
```

---

## Slide 5: Loop Variable
**What's the loop variable (i)?**

**It changes each iteration:**
```python
for i in range(4):
    print(i)    # What prints?

# Output:
# 0
# 1
# 2
# 3
```

**Common Uses:**
1. **Not used** - Just repeat code (most common for robots)
2. **Used in math** - `side_length = i * 10` (grow each iteration)
3. **Used in print** - `print(f"Trial {i}")`

**For Robot Loops:**
Usually you DON'T use the loop variable itself

---

## Slide 6: Blockly → Python Triangle
**Blockly:**
```
Repeat 3 times:
  Straight(30)
  Turn(120)
```

**Python:**
```python
for i in range(3):
    drivetrain.straight(30)
    drivetrain.turn(120)
```

**Translation Rules:**
- Repeat N times → `for i in range(N):`
- Indented code inside → Code inside the for loop
- Straight(distance) → `drivetrain.straight(distance)`
- Turn(angle) → `drivetrain.turn(angle)`

**Try it:** Write the template, then fill in the XRP commands

---

## Slide 7: Indentation is Critical
**CORRECT - Indented code in loop:**
```python
for i in range(3):
    print("inside loop")   # ✓ Indented - runs 3 times
```

**WRONG - Code not indented:**
```python
for i in range(3):
print("inside loop")       # ✗ NOT indented - syntax error!
```

**WRONG - Too much indentation:**
```python
for i in range(3):
        print("inside loop")   # ✗ Wrong indent level - error!
```

**Python Rule:** Indentation = code block structure

---

## Slide 8: Nested Loops
**Loop inside a loop:**

```python
for i in range(3):              # Outer loop: 3 times
    print("Outer:", i)
    for j in range(2):          # Inner loop: 2 times
        print("  Inner:", j)
```

**Output:**
```
Outer: 0
  Inner: 0
  Inner: 1
Outer: 1
  Inner: 0
  Inner: 1
Outer: 2
  Inner: 0
  Inner: 1
```

**Total runs:** 3 × 2 = 6 iterations of innermost code

**For Robots:**
```python
for i in range(5):              # Draw 5 shapes
    for j in range(4):          # Each shape has 4 sides
        drivetrain.straight(25)
        drivetrain.turn(90)
    # After each 4-side square, move to next position
    drivetrain.straight(100)
```

---

## Slide 9: Loop with Variables
**Conditional Loop (loop while condition true):**

```python
distance = 10

while distance < 100:
    drivetrain.straight(distance)
    distance = distance + 10
```

**Runs:**
1. Goes 10cm
2. Goes 20cm
3. Goes 30cm
4. ...
5. Goes 90cm
6. Stops at 100cm (condition false)

**Difference:**
- **for loop** - Fixed number of iterations
- **while loop** - Runs while condition is true

**Note:** while loops need careful design (can accidentally infinite loop!)

---

## Slide 10: Common Loop Errors
**Error 1: Indentation wrong**
```python
for i in range(4):
  drivetrain.straight(30)    # Wrong - different indent levels
    drivetrain.turn(90)
→ SyntaxError: unexpected indent
```

**Error 2: Off-by-one with range**
```python
for i in range(4):      # Runs 4 times (i = 0,1,2,3)
    ...
# NOT 5 times!
```

**Error 3: Forgetting colon**
```python
for i in range(4)   # Missing :
    print(i)
→ SyntaxError: expected ':'
```

**Fix:** Compare with correct syntax, check colons and indents

---

## Slide 11: Practice Exercises
**Exercise 1: Square Loop**
```python
# Write a for loop that draws a square
for i in range(???):
    drivetrain.straight(30)
    drivetrain.turn(90)
```

**Exercise 2: Pentagon Loop**
```python
# Write a for loop that draws a pentagon
for i in range(???):
    drivetrain.straight(25)
    drivetrain.turn(???)  # What's the angle?
```

**Exercise 3: Nested Pattern**
```python
# Write nested loops that:
# - Repeat 3 times
# - Each time: Turn 90, then move forward
for i in range(3):
    # Your code here
```

---

## Slide 12: Connection to Functions (Lesson 10)
**Preview:**
- Today: Loops make code repeat
- Next lesson: Functions make code reusable
- Combined: Functions WITH loops = powerful!

**Python function with loop (spoiler):**
```python
def draw_polygon(sides, distance):
    angle = 360 / sides
    
    for i in range(sides):
        drivetrain.straight(distance)
        drivetrain.turn(angle)

draw_polygon(4, 30)   # Draw square
draw_polygon(5, 25)   # Draw pentagon
```

**Teaser:** "Combine these tools and code becomes elegant!"
