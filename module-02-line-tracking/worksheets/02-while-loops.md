# Lesson 2 Worksheet: While Loops

**Name:** ________________________
**Date:** ________________________

---

## Part 1: while Loop Tracing

Trace through each code snippet and write the output.

### Example 1:
```python
count = 0
while count < 3:
    print(count)
    count = count + 1
```
**Output:**
```
___
___
___
```

### Example 2:
```python
x = 10
while x > 0:
    print(x)
    x = x - 3
```
**Output:**
```
___
___
___
___
```

### Example 3:
```python
left = 0.2
threshold = 0.5
while left < threshold:
    print("Driving... sensor:", left)
    left = left + 0.15
print("Stopped! sensor:", left)
```
**Output:**
```
___
___
___
___
```

---

## Part 2: for vs. while

For each scenario, decide whether a `for` loop or `while` loop is better and explain why.

1. **Draw a square (4 sides)**
   - Better loop: `for` / `while` (circle one)
   - Why? ____________________________________________________________________

2. **Drive until the robot detects a line**
   - Better loop: `for` / `while` (circle one)
   - Why? ____________________________________________________________________

3. **Print numbers from 1 to 10**
   - Better loop: `for` / `while` (circle one)
   - Why? ____________________________________________________________________

4. **Keep checking a sensor until a button is pressed**
   - Better loop: `for` / `while` (circle one)
   - Why? ____________________________________________________________________

---

## Part 3: Comparison Operators

Evaluate each expression to True or False:

| Expression | True or False? |
|---|---|
| `0.3 < 0.5` | __________ |
| `0.8 > 0.5` | __________ |
| `0.5 == 0.5` | __________ |
| `0.2 > 0.5` | __________ |
| `0.9 != 0.5` | __________ |
| `0.5 <= 0.5` | __________ |

---

## Part 4: Find the Bug

Each code snippet has a bug. Find it and explain the fix.

### Bug 1:
```python
left = reflectance.get_left()
while left < 0.5:
    drivetrain.set_effort(0.3, 0.3)
```
**Bug:** ____________________________________________________________________

**Fix:** ____________________________________________________________________

### Bug 2:
```python
while left < 0.5
    drivetrain.set_effort(0.3, 0.3)
    left = reflectance.get_left()
```
**Bug:** ____________________________________________________________________

**Fix:** ____________________________________________________________________

### Bug 3:
```python
left = reflectance.get_left()
while left > 0.5:
    drivetrain.set_effort(0.3, 0.3)
    left = reflectance.get_left()
drivetrain.stop()
```
**Bug:** ____________________________________________________________________
(Hint: When does the robot start on white surface — what is the initial value of `left`?)

---

## Part 5: Write Your Own

Write a `while` loop that counts DOWN from 5 to 1 and prints each number:

```python
count = ____
while ____________:
    print(count)
    count = ____________
```

**Expected output:**
```
5
4
3
2
1
```

---

## Reflection

**What is the most important rule about while loops that you learned today?**

_________________________________________________________________

_________________________________________________________________

---

**Next Lesson:** We'll add `if/else` inside the loop so the robot can make decisions — turn around instead of just stopping!
