# Lesson 3 Worksheet: if/else Decisions

**Name:** ________________________
**Date:** ________________________

---

## Part 1: if/else Tracing

For each snippet, write what gets printed.

### Example 1:
```python
temperature = 75
if temperature > 80:
    print("Hot!")
else:
    print("Comfortable.")
```
**Output:** __________________

### Example 2:
```python
sensor = 0.8
threshold = 0.5
if sensor > threshold:
    print("ON the line")
else:
    print("OFF the line")
```
**Output:** __________________

### Example 3:
```python
left = 0.3
right = 0.7
if left > 0.5 or right > 0.5:
    print("At least one sensor on line")
else:
    print("Both sensors off line")
```
**Output:** __________________

### Example 4:
```python
left = 0.3
right = 0.2
if left > 0.5 and right > 0.5:
    print("Both on line!")
else:
    print("Not both on line")
```
**Output:** __________________

---

## Part 2: Logical Operators

Evaluate each expression to True or False:

| Expression | True or False? |
|---|---|
| `True and True` | __________ |
| `True and False` | __________ |
| `False and True` | __________ |
| `True or False` | __________ |
| `False or False` | __________ |
| `not True` | __________ |
| `not False` | __________ |
| `0.8 > 0.5 and 0.7 > 0.5` | __________ |
| `0.3 > 0.5 or 0.7 > 0.5` | __________ |
| `0.3 > 0.5 and 0.7 > 0.5` | __________ |

---

## Part 3: Robot Decision Table

For each sensor reading, write what the bounce driving program should do:

| Left Sensor | Right Sensor | `left > 0.5 or right > 0.5` | Action |
|---|---|---|---|
| 0.2 | 0.1 | __________ | __________ |
| 0.8 | 0.2 | __________ | __________ |
| 0.2 | 0.9 | __________ | __________ |
| 0.8 | 0.7 | __________ | __________ |
| 0.4 | 0.3 | __________ | __________ |

Actions: "Keep driving" or "Turn around"

---

## Part 4: Write the Condition

Write the Python condition for each scenario:

1. **The left sensor is on the line (above 0.5):**

   `if ________________________________:`

2. **Both sensors are off the line (both below 0.5):**

   `if ________________________________:`

3. **At least one sensor is on the line:**

   `if ________________________________:`

4. **The left sensor is on the line AND the right sensor is NOT on the line:**

   `if ________________________________:`

---

## Part 5: while True

1. **What does `while True` mean?**

   ____________________________________________________________________

2. **How do you stop a `while True` loop?**

   ____________________________________________________________________

3. **Why is `while True` useful for robots?**

   ____________________________________________________________________

---

## Reflection

**In your own words, explain how `if/else` is different from a `while` loop:**

_________________________________________________________________

_________________________________________________________________

---

**Next Lesson:** We'll add randomness to our bounce driving to make the robot explore the whole circle!
