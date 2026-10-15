# Lesson 9 Worksheet: Line-Tracking Functions

**Name:** ________________________
**Date:** ________________________

---

## Part 1: Two Toolkits Concept

1. **In your own words, why do the sensor functions and the driving functions live in two separate groups instead of one big pile of functions?**

   ____________________________________________________________________

2. **Give a real-world example of one system calling on another system to do its job (not from code):**

   "A _____________ calls on a _____________ to do its job."

3. **In our code, which two Lesson 8 functions does `track_to_intersection()` call?**

   a. ________________________________

   b. ________________________________

---

## Part 2: Toolkit Relationship Diagram

Fill in the blanks to complete the diagram:

```
┌──────────────────────┐       ┌──────────────────────┐
│  Sensor toolkit       │       │  drivetrain (hardware)│
│                       │       │                       │
│ get_error()           │       │ arcade(speed, turn)   │
│ is_at_cross()         │       │ straight(dist, effort)│
│ is_either_on_line()   │       │ turn(deg, effort)     │
│                       │       │ stop()                │
└──────────┬────────────┘       └──────────┬────────────┘
           │                                │
           │      ┌────────────────────┐    │
           └──────│  ______________     │────┘
                  │  toolkit            │
                  │                     │
                  │ track_to_intersection() │
                  │ drive_past_intersection()│
                  │ turn_clockwise()    │
                  │ _____________()     │
                  └─────────────────────┘
```

**Fill in the toolkit name and the missing function.**

---

## Part 3: Code Tracing -- track_to_intersection()

```python
def track_to_intersection():
    while not is_at_cross():
        error = get_error()
        correction = error * KP
        drivetrain.arcade(BASE_EFFORT, -correction)
    drivetrain.stop()
```

1. **`is_at_cross()` and `get_error()` -- which lesson's functions are these?** ________________________________

2. **Is there a dot before `is_at_cross()`? What does that tell you about what kind of thing it is?** ________________________________

3. **What does `while not` mean here?** ________________________________

4. **When does the loop exit?** ________________________________

5. **What happens after the loop exits?** ________________________________

6. **When the loop exits, where are the sensors? Where are the wheels?** ________________________________

---

## Part 4: Code Tracing -- drive_past_intersection() and turn_clockwise()

```python
def drive_past_intersection():
    drivetrain.straight(8.75, 0.5)

def turn_clockwise():
    drivetrain.turn(-60, TURN_EFFORT)
    drivetrain.arcade(0, -TURN_EFFORT)
    while not is_either_on_line():
        pass
    drivetrain.stop()
```

1. **`drive_past_intersection()` does two jobs. Name both.**

   a. ________________________________   b. ________________________________

2. **Why is it a distance (`straight(8.75, ...)`) and not `time.sleep(0.5)` with the motors running?**

   ____________________________________________________________________

Number the steps of what the robot does in `turn_clockwise()`:

___ Robot stops when a sensor finds the crossing line

___ Robot turns 60 degrees without looking at the sensors

___ Robot keeps spinning while neither sensor is on a line

___ Robot starts spinning in place (no forward speed)

___ `pass` -- do nothing extra, just keep checking

3. **The moment `turn_clockwise()` starts, what does `is_either_on_line()` return, and why?** ________________________________

4. **So what would happen if the blind `turn(-60, ...)` were deleted?** ____________________________________________________________________

5. **Why 60 degrees and not 90?** ____________________________________________________________________

---

## Part 5: Main Program Design

Write the main program code for each task, calling the toolkit's functions directly (no object, no dots):

1. **Follow the line to a cross and park on it:**
   ```python
   ________________________________
   ________________________________
   ```

2. **Follow to cross, park, turn right, follow to cross again:**
   ```python
   ________________________________
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
       ________________________________
   ```

---

## Part 6: Toolkit vs. No Toolkit

**With organized functions:**
```python
track_to_intersection()
drive_past_intersection()
turn_clockwise()
```

**Without functions (everything in main):**
```python
while not (reflectance.get_left() > 0.5 and reflectance.get_right() > 0.5):
    error = reflectance.get_left() - reflectance.get_right()
    drivetrain.arcade(0.4, -error * 0.5)
drivetrain.stop()
drivetrain.straight(8.75, 0.5)
drivetrain.turn(-60, 0.25)
drivetrain.arcade(0, -0.25)
while not (reflectance.get_left() > 0.5 or reflectance.get_right() > 0.5):
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
           self.turn_effort = 0.25
   ```

3. **Rewrite this functions-version line as a method call through `self.sensor`:**

   Functions version: `is_at_cross()`

   Class version: `___________________________`

4. **True or False: `LineTrack`'s `__init__` needs the caller to build a `LineSensor` first and pass it in.**

   TRUE / FALSE -- **Why?** _________________________________________________________________

5. **What is the difference between "has-a" (composition) and "calls" (the functions version)?**

   _________________________________________________________________

   _________________________________________________________________
