# Lesson 9 Slide Outline: Line-Tracking Functions

## Slide 1: Title & Learning Objectives
**Title:** Line-Tracking Functions

**Learning Objectives:**
- Build a second toolkit of functions that calls the Lesson 8 toolkit
- Implement proportional line tracking inside a function
- Implement turn functions that use sensor feedback
- Test a multi-function program on the robot

**Agenda:**
- Two jobs, one robot (5 min)
- Guided: Build the driving toolkit step by step (20 min)
- Practice: Write and test your own toolkit (20 min)

---

## Slide 2: Hook -- Two Jobs, One Robot

- Last lesson: a toolkit of sensor functions (reading)
- But the robot doesn't just read sensors -- it also needs to drive

**Should driving code go inside `get_error()`?**
No -- keep sensor-reading and driving separate, same as Module 1 kept shape-drawing separate from setup.

**The plan:** a second toolkit -- driving functions -- that calls the sensor functions whenever it needs to know where the line is.

---

## Slide 3: The Relationship

```
Sensor toolkit (Lesson 8)          Driving toolkit (Lesson 9)
  get_left(), get_right()            track_until_cross()
  get_error()                 <----  turn_right()
  is_at_cross(), is_off_line()       turn_left()
```

**Analogy:** A car has an engine. The car doesn't rebuild the engine's parts inside itself -- it just uses the engine when it needs power.

**Note for Classes track:** this relationship is called *object composition* (`LineTrack` "has a" `LineSensor`). In the functions version, there's no "has" -- there's just "calls."

---

## Slide 4: Preview the Goal

```python
track_until_cross()
turn_right()
track_until_cross()
```

**Three lines** to follow a line, detect an intersection, and turn.

**Why keep them separate?**
- Sensor logic stays in Lesson 8 functions
- Driving logic stays in Lesson 9 functions
- The Lesson 8 toolkit could be reused in a program that never drives at all

---

## Slide 5: Step 1 -- The Driving Globals

```python
from XRPLib.differential_drive import DifferentialDrive

drivetrain = DifferentialDrive.get_default_differential_drive()
BASE_EFFORT = 0.4
KP = 0.5
```

- New globals, separate from `reflectance`/`THRESHOLD` from Lesson 8
- Same file -- every function below (old and new) can see all four
- `BASE_EFFORT`: baseline forward speed. `KP`: proportional control gain from Lesson 5

---

## Slide 6: Step 2 -- track_until_cross()

```python
def track_until_cross():
    while not is_at_cross():
        error = get_error()
        left = BASE_EFFORT - error * KP
        right = BASE_EFFORT + error * KP
        drivetrain.set_effort(left, right)
    drivetrain.stop()
```

- `is_at_cross()` and `get_error()` are called directly -- no prefix, because they're just names in the file's global scope
- Proportional math is identical to Lesson 5, using global `BASE_EFFORT`/`KP`

---

## Slide 7: Step 3 -- Clearing the Intersection

When `is_at_cross()` becomes true, the **sensors** are over the intersection, but the turning center (rear axle) is still behind it.

```python
def clear_intersection():
    drivetrain.straight(8, 0.5)
```

- Drives forward a **fixed 8 cm** -- an exact distance, not a timing guess
- A small helper function, whose only job is to be called by the turn functions next
- No timing-based movement anywhere in this course -- distance-based is consistent regardless of battery level

---

## Slide 8: Step 4-5 -- turn_right() and turn_left()

```python
def turn_right():
    clear_intersection()
    drivetrain.set_effort(0.3, -0.3)
    while is_off_line():
        pass
    drivetrain.stop()

def turn_left():
    clear_intersection()
    drivetrain.set_effort(-0.3, 0.3)
    while is_off_line():
        pass
    drivetrain.stop()
```

**Only difference between them:** the motor efforts are swapped.

---

## Slide 9: Test the Complete Program

```python
board = Board.get_default_board()
board.wait_for_button()

print("Following line...")
track_until_cross()
print("Cross detected! Turning right...")
turn_right()
print("Following line again...")
track_until_cross()
print("Done!")
```

**Expected behavior:** follows the line, stops at the cross, clears the intersection, turns right, follows again, stops.

---

## Slide 10: Demo Discussion & Connection to Lesson 10

**How many lines of actual logic are in the test program?** Just 3 function calls plus prints.

**Where is all the sensor reading and motor control code?** Organized into the two toolkits, out of the main program's way.

**Coming up in Lesson 10:** combine both toolkits into the Module 2 final project -- follow the circle, reverse direction 4 times.

---

## Slide 11: Optional Extension -- Refactor into a Class

*For courses that also cover classes/objects. Skip if not covering classes.*

```python
class LineTrack:
    def __init__(self):
        self.sensor = LineSensor()          # composition!
        self.drivetrain = DifferentialDrive.get_default_differential_drive()
        self.base_effort = 0.4
        self.kp = 0.5

    def track_until_cross(self):
        while not self.sensor.is_at_cross():
            error = self.sensor.get_error()
            ...
```

**What changed:** `is_at_cross()` becomes `self.sensor.is_at_cross()` -- delegating to the `LineSensor` object it contains, instead of calling a bare function.

**This is object composition** -- one class storing an instance of another class as an attribute (a "has-a" relationship).
