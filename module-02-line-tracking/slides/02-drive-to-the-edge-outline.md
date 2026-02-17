# Lesson 2 Slide Outline: Drive to the Edge and Stop

## Slide 1: Title & Learning Objectives
**Title:** Drive to the Edge and Stop

**Learning Objectives:**
- Write `while` loops in Python
- Use comparison operators (`<`, `>`, `==`)
- Combine sensor reading with a while loop
- Program the robot to drive until a condition is met

**Agenda:**
- while loops explained (10 min)
- Guided practice: drive to edge (15 min)
- Independent practice (20 min)

---

## Slide 2: The Problem
**Last lesson:** We read sensor values, but the robot just sat still.

**Today's goal:** Make the robot drive forward AND check the sensor continuously. When it detects the line — stop!

**Question:** "How do we repeat 'drive and check' without knowing how many times?"

---

## Slide 3: for Loop vs. while Loop
**`for` loop (Module 1):** Repeat a FIXED number of times
```python
for i in range(4):    # Always runs 4 times
    drivetrain.straight(30)
    drivetrain.turn(90)
```

**`while` loop (NEW):** Repeat UNTIL a condition changes
```python
while left < 0.5:    # Runs until left >= 0.5
    drivetrain.set_effort(0.3, 0.3)
    left = reflectance.get_left()
```

**Key difference:** `for` = fixed count. `while` = until something happens.

---

## Slide 4: while Loop Syntax
```python
while condition:
    # code that runs while condition is True
    # code stops when condition becomes False
```

**Rules:**
- Colon `:` after the condition
- Indented body (same as `for`)
- Condition is checked BEFORE each iteration
- Loop exits when condition is `False`

---

## Slide 5: Comparison Operators
| Operator | Meaning | Example | Result |
|---|---|---|---|
| `<` | Less than | `0.2 < 0.5` | `True` |
| `>` | Greater than | `0.8 > 0.5` | `True` |
| `==` | Equal to | `4 == 4` | `True` |
| `!=` | Not equal | `3 != 5` | `True` |
| `<=` | Less or equal | `5 <= 5` | `True` |
| `>=` | Greater or equal | `0.6 >= 0.5` | `True` |

**For sensors:** `left < 0.5` means "sensor is on white (below threshold)"

---

## Slide 6: Drive to the Edge
```python
threshold = 0.5

board.wait_for_button()
left = reflectance.get_left()

while left < threshold:
    drivetrain.set_effort(0.3, 0.3)
    left = reflectance.get_left()  # UPDATE!

drivetrain.stop()
print("Line detected!")
```

**Step by step:**
1. Read sensor before entering loop
2. While on white (below threshold) → drive forward
3. Update sensor reading EVERY iteration
4. When sensor hits line (above threshold) → loop exits → stop

---

## Slide 7: CRITICAL — Update Inside the Loop!
**CORRECT:**
```python
while left < threshold:
    drivetrain.set_effort(0.3, 0.3)
    left = reflectance.get_left()  # ✓ Updates!
```

**WRONG:**
```python
while left < threshold:
    drivetrain.set_effort(0.3, 0.3)
    # ✗ left never changes → infinite loop!
```

**Rule:** Always update the variable you're checking inside the while loop!

---

## Slide 8: set_effort vs. straight
**`drivetrain.straight(30)`** — Drives exactly 30cm, then stops. BLOCKS until done.

**`drivetrain.set_effort(0.3, 0.3)`** — Sets motor power and returns IMMEDIATELY.

**Why set_effort?** We need to check the sensor continuously. `straight()` would drive the whole distance before we could check!

---

## Slide 9: Your Turn!
**Exercise:** Place robot inside the taped circle. Program it to:
1. Wait for button press
2. Drive forward
3. Stop when it detects the line

**Starter code provided** — fill in the missing parts.

**Checkpoints:**
- Robot drives forward?
- Robot stops at the line?
- Print shows sensor values?

---

## Slide 10: Connection to Next Lesson
**Today:** Robot drives to the edge and STOPS.

**Next lesson (Lesson 3):** Robot drives to the edge and TURNS AROUND!
- `if/else` statements — making decisions
- "Bounce driving" — robot bounces between edges of the circle

**Preview:**
```python
if left > threshold:
    drivetrain.turn(180)  # Turn around!
else:
    drivetrain.set_effort(0.3, 0.3)  # Keep going
```
