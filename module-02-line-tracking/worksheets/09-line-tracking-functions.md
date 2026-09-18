# Lesson 9 Worksheet: Line-Tracking Functions

**Name:** ________________________
**Date:** ________________________

---

## Part 1: Two Toolkits Concept

1. **In your own words, why do the sensor functions and the driving functions live in two separate groups instead of one big pile of functions?**

   ____________________________________________________________________

2. **Give a real-world example of one system calling on another system to do its job (not from code):**

   "A _____________ calls on a _____________ to do its job."

3. **In our code, which two Lesson 8 functions does `track_until_cross()` call?**

   a. ________________________________

   b. ________________________________

---

## Part 2: Toolkit Relationship Diagram

Fill in the blanks to complete the diagram:

```
┌──────────────────────┐       ┌──────────────────────┐
│  Sensor toolkit       │       │  drivetrain (hardware)│
│                       │       │                       │
│ get_error()           │       │ set_effort(l, r)      │
│ is_at_cross()         │       │ straight(dist, effort)│
│ is_off_line()         │       │ stop()                │
└──────────┬────────────┘       └──────────┬────────────┘
           │                                │
           │      ┌────────────────────┐    │
           └──────│  ______________     │────┘
                  │  toolkit            │
                  │                     │
                  │ track_until_cross() │
                  │ turn_right()        │
                  │ _____________()     │
                  └─────────────────────┘
```

**Fill in the toolkit name and the missing function.**

---

## Part 3: Code Tracing -- track_until_cross()

```python
def track_until_cross():
    while not is_at_cross():
        error = get_error()
        left = BASE_EFFORT - error * KP
        right = BASE_EFFORT + error * KP
        drivetrain.set_effort(left, right)
    drivetrain.stop()
```

1. **`is_at_cross()` and `get_error()` -- which lesson's functions are these?** ________________________________

2. **Is there a dot before `is_at_cross()`? What does that tell you about what kind of thing it is?** ________________________________

3. **What does `while not` mean here?** ________________________________

4. **When does the loop exit?** ________________________________

5. **What happens after the loop exits?** ________________________________

---

## Part 4: Code Tracing -- turn_right()

```python
def turn_right():
    clear_intersection()
    drivetrain.set_effort(0.3, -0.3)
    while is_off_line():
        pass
    drivetrain.stop()
```

Number the steps of what the robot does:

___ Robot stops when line is found

___ Robot drives forward 8 cm to clear the intersection

___ Robot keeps turning while off the line

___ Robot starts turning right (left forward, right backward)

___ `pass` -- do nothing extra, just keep checking

**Why does `clear_intersection()` use `drivetrain.straight(8, 0.5)` instead of `set_effort()` plus a timer?**

____________________________________________________________________

---

## Part 5: Main Program Design

Write the main program code for each task, calling the toolkit's functions directly (no object, no dots):

1. **Follow the line until a cross, then stop:**
   ```python
   ________________________________
   ```

2. **Follow to cross, turn right, follow to cross again:**
   ```python
   ________________________________
   ________________________________
   ________________________________
   ```

3. **Follow and reverse 4 times using a for loop:**
   ```python
   for i in range(____):
       ________________________________
       ________________________________
       ________________________________
   ```

---

## Part 6: Toolkit vs. No Toolkit

**With organized functions:**
```python
track_until_cross()
turn_right()
```

**Without functions (everything in main):**
```python
while not (reflectance.get_left() > 0.5 and reflectance.get_right() > 0.5):
    error = reflectance.get_left() - reflectance.get_right()
    left = 0.4 - error * 0.5
    right = 0.4 + error * 0.5
    drivetrain.set_effort(left, right)
drivetrain.stop()
drivetrain.straight(8, 0.5)
drivetrain.set_effort(0.3, -0.3)
while reflectance.get_left() < 0.5 and reflectance.get_right() < 0.5:
    pass
drivetrain.stop()
```

**Which version is easier to read?** __________

**Which version is easier to reuse?** __________

**Which version is easier to debug?** __________

---

## Reflection

**How does splitting your code into two toolkits (sensors, driving) make it better, compared to one long block of code?**

_________________________________________________________________

_________________________________________________________________

---

**Next Lesson:** The final project -- use both toolkits together for the Module 2 capstone!

---

## Part 7 (Optional Extension): Refactor into LineTrack (Object Composition)

*Skip this section if your course doesn't cover classes. Builds on the Lesson 8 worksheet's Optional Extension.*

1. **In the class version, `LineTrack` stores a `LineSensor` object as one of its own attributes. What is this pattern called?**

   _________________________________________________________________

2. **Fill in the blanks:**

   ```python
   class LineTrack:
       def __init__(self):
           self.sensor = ___________________
           self.drivetrain = DifferentialDrive.get_default_differential_drive()
           self.base_effort = 0.4
           self.kp = 0.5
   ```

3. **Rewrite this functions-version line as a method call through `self.sensor`:**

   Functions version: `is_at_cross()`

   Class version: `___________________________`

4. **True or False: `LineTrack`'s `__init__` needs the caller to build a `LineSensor` first and pass it in.**

   TRUE / FALSE -- **Why?** _________________________________________________________________

5. **What is the difference between "has-a" (composition) and "calls" (the functions version)?**

   _________________________________________________________________

   _________________________________________________________________
