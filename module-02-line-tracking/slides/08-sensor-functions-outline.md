# Lesson 8 Slide Outline: Sensor Functions

## Slide 1: Title & Learning Objectives
**Title:** Sensor Functions

**Learning Objectives:**
- Organize related sensor code into a toolkit of functions
- Share data between functions using global variables
- Have one function call another (function composition)
- Build a working sensor toolkit for the XRP robot

**Agenda:**
- The messy code problem (5 min)
- Global variables & function composition (10 min)
- Guided: Build the sensor toolkit step by step (15 min)
- Practice: Write and test your own toolkit (15 min)

---

## Slide 2: Hook -- The Problem with Our Code

**Our Lesson 7 code has everything mixed together:**
```python
reflectance = Reflectance.get_default_reflectance()
drivetrain  = DifferentialDrive.get_default_differential_drive()
threshold = 0.5
base_effort = 0.4
kp = 0.5

while True:
    left  = reflectance.get_left()
    right = reflectance.get_right()
    error = left - right
    if left > threshold and right > threshold:
        drivetrain.stop()
        break
    drivetrain.set_effort(base_effort - error * kp,
                          base_effort + error * kp)
```

**Problems:**
- Sensor logic isn't given a name -- it's repeated wherever needed
- Hard to reuse just the sensor part in another program
- Hard to read -- what does each section do?

**Question:** "How could we package the sensor logic so it has a name?"

---

## Slide 3: The Fix -- A Toolkit of Functions

**Remember Module 1?**
```python
def draw_polygon(sides, distance):
    angle = 360 / sides
    for i in range(sides):
        drivetrain.straight(distance)
        drivetrain.turn(angle)
```

- You already turned repeated code into a named function
- We're doing the same thing here -- for sensor reading

**The twist:** several functions need to share the *same* sensor object and threshold
- Instead of passing them in every call, create them once at the top of the file as **global variables**
- Same pattern as `drivetrain` since Module 1

---

## Slide 4: Preview the Goal

**What the finished toolkit will look like:**
```python
error = get_error()
at_cross = is_at_cross()
off_line = is_off_line()
```

- No dots, no objects -- just function calls
- Reads almost like English

**Why this matters:**
| Benefit | What it means |
|---|---|
| Organization | Related code stays together, with names |
| Reusability | Copy the block into a new file, it just works |
| Readability | `is_at_cross()` beats `left > 0.5 and right > 0.5` |
| Continuity | Same skills as Module 1 -- `def`, parameters, `return` |

---

## Slide 5: Step 1 -- The Shared Globals

```python
from XRPLib.reflectance import Reflectance

reflectance = Reflectance.get_default_reflectance()
THRESHOLD = 0.5
```

- Runs once, when the program starts -- not inside any function
- `reflectance` and `THRESHOLD` are **global variables**
- Every function below can read them without receiving them as a parameter
- `THRESHOLD` is capitalized by convention: "this is a constant"

**Exact same pattern as:**
```python
drivetrain = DifferentialDrive.get_default_differential_drive()
```

---

## Slide 6: Step 2-3 -- get_left/get_right/get_error

```python
def get_left():
    return reflectance.get_left()

def get_right():
    return reflectance.get_right()

def get_error():
    return get_left() - get_right()
```

- `get_left()`/`get_right()` take no parameters -- they read the global `reflectance` instead
- `get_error()` doesn't read the sensor directly -- it **calls** `get_left()` and `get_right()`
- This is **function composition**: building bigger functions out of smaller ones

**Test it:**
```python
print(get_left())
print(get_error())
```

---

## Slide 7: Step 4 -- Boolean Functions

```python
def is_at_cross():
    return get_left() > THRESHOLD and get_right() > THRESHOLD

def is_off_line():
    return get_left() < THRESHOLD and get_right() < THRESHOLD
```

**What they detect:**

| Situation | Left Sensor | Right Sensor | `is_at_cross()` | `is_off_line()` |
|---|---|---|---|---|
| On the line, centered | high | low | False | False |
| At an intersection (cross) | high | high | **True** | False |
| Off the line entirely | low | low | False | **True** |

`THRESHOLD` is used directly, just like `get_left()` -- both are names any function can see.

---

## Slide 8: The Complete Sensor Toolkit

```python
from XRPLib.reflectance import Reflectance

reflectance = Reflectance.get_default_reflectance()
THRESHOLD = 0.5

def get_left():
    return reflectance.get_left()

def get_right():
    return reflectance.get_right()

def get_error():
    return get_left() - get_right()

def is_at_cross():
    return get_left() > THRESHOLD and get_right() > THRESHOLD

def is_off_line():
    return get_left() < THRESHOLD and get_right() < THRESHOLD
```

**Inventory:** 2 global variables, 5 functions -- no `self`, no `class`, all Module 1 skills.

---

## Slide 9: Before vs. After

**Before (Lesson 7 -- tangled inline code):**
```python
reflectance = Reflectance.get_default_reflectance()
threshold = 0.5

left  = reflectance.get_left()
right = reflectance.get_right()
error = left - right
at_cross = left > threshold and right > threshold
```

**After (Lesson 8 -- organized functions):**
```python
error = get_error()
at_cross = is_at_cross()
```

**What improved:** fewer lines where you use it, reads like English, sensor logic is packaged and reusable, `THRESHOLD` stored in one place.

---

## Slide 10: The `global` Keyword (Advanced)

**Reading a global works automatically. Changing one doesn't:**
```python
def set_threshold(new_value):
    global THRESHOLD
    THRESHOLD = new_value
```

- `is_at_cross()` only **reads** `THRESHOLD` -- no `global` needed
- `set_threshold()` **reassigns** `THRESHOLD` -- needs `global`, or Python creates a throwaway local variable instead

**One real limitation:** with globals, you can't have two sensors with two different thresholds at once -- there's only one `THRESHOLD` for the whole program.

---

## Slide 11: Common Mistakes & Connection to Lesson 9

**Watch out for these errors:**
```python
# Mistake 1: Forgetting global when reassigning
def set_threshold(new_value):
    THRESHOLD = new_value   # WRONG -- creates a local, real THRESHOLD untouched

# Mistake 2: Calling a function before its def has run
error = get_error()   # WRONG if this line runs before get_error is defined

# Mistake 3: Passing reflectance around unnecessarily
def get_left(reflectance):   # Unnecessary -- it's already a global
```

**Coming up in Lesson 9:**
- Today: sensor toolkit (reading)
- Next: driving toolkit (moving) that *calls* the sensor toolkit
- No "has-a" needed -- driving functions just call sensor functions directly

---

## Slide 12: Optional Extension -- Refactor into a Class

*For courses that also cover classes/objects. Skip if not covering classes.*

```python
class LineSensor:
    def __init__(self):
        self.reflectance = Reflectance.get_default_reflectance()
        self.threshold = 0.5

    def get_left(self):
        return self.reflectance.get_left()

    def get_error(self):
        return self.get_left() - self.get_right()
    # ... same pattern for the rest
```

**What changed:** globals become `self.` attributes set in `__init__`; each function gains `self` as its first parameter and becomes a method.

**The payoff:** `LineSensor()` can now be created twice, each with its own `threshold` -- something the functions version can't do.

---

## Slide 13: Optional Extension -- Two Independent Sensors

```python
sensor_low = LineSensor()
sensor_low.threshold = 0.3

sensor_high = LineSensor()
sensor_high.threshold = 0.7

print(sensor_low.is_at_cross())
print(sensor_high.is_at_cross())
```

**Discussion:** What would you have to do to run two sensors with different thresholds using only the functions version? *(You'd need to duplicate every function and global with a different name -- a class avoids that entirely.)*
