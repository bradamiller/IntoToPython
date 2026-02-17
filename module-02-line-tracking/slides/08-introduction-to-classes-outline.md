# Lesson 8 Slide Outline: Introduction to Classes -- LineSensor

## Slide 1: Title & Learning Objectives
**Title:** Introduction to Classes -- LineSensor

**Learning Objectives:**
- Understand why classes are useful for organizing code
- Write a class with `__init__`, `self`, and methods
- Create objects and call methods on them
- Build a working LineSensor class for the XRP robot

**Agenda:**
- Why classes? (5 min)
- Class syntax walkthrough (10 min)
- Guided: Build LineSensor step by step (15 min)
- Practice: Write and test your own LineSensor (15 min)

---

## Slide 2: Hook -- The Problem with Our Code

**Our Lesson 7 code has everything mixed together:**
```python
reflectance = Reflectance.get_default_reflectance()
drivetrain = DifferentialDrive.get_default_differential_drive()
threshold = 0.5
base_effort = 0.4
kp = 0.5

while True:
    left = reflectance.get_left()
    right = reflectance.get_right()
    error = left - right
    if left > threshold and right > threshold:
        drivetrain.stop()
        break
    drivetrain.set_effort(base_effort - error * kp,
                          base_effort + error * kp)
```

**Problems:**
- Sensor code and driving code are tangled together
- Hard to reuse just the sensor part in another program
- Hard to read -- what does each section do?

**Question:** "How could we separate the sensor logic from the driving logic?"

---

## Slide 3: What Is a Class?

**A class is a blueprint that groups related data and functions together.**

**Analogy -- TV Remote:**
- **Data it stores:** current channel, volume level
- **Actions it can do:** change channel, adjust volume, power on/off

**Analogy -- LineSensor:**
- **Data it stores:** the reflectance hardware, a threshold value
- **Actions it can do:** get error, check for cross, check if off line

**Key vocabulary:**
| Term | Meaning |
|---|---|
| **Class** | The blueprint (the design) |
| **Object** | A specific thing built from the blueprint |
| **Method** | A function that belongs to a class |
| **Attribute** | A variable that belongs to an object |

---

## Slide 4: You Already Use Classes!

**Every time you wrote this, you were using a class:**
```python
drivetrain = DifferentialDrive.get_default_differential_drive()
drivetrain.straight(30)
drivetrain.turn(90)
drivetrain.stop()
```

- `DifferentialDrive` is a **class** (the blueprint)
- `drivetrain` is an **object** (a specific instance)
- `.straight()`, `.turn()`, `.stop()` are **methods**

**Today you will build your own class -- just like the ones in XRPLib!**

---

## Slide 5: Class Syntax -- The Basics

**Defining an empty class:**
```python
class LineSensor:
    pass
```

**Breaking it down:**
- `class` -- keyword that starts a class definition
- `LineSensor` -- the name (CamelCase: capitalize each word)
- `:` -- colon starts the body (just like `def` and `for`)
- `pass` -- placeholder for "nothing here yet"

**Creating an object (instantiation):**
```python
sensor = LineSensor()
print(type(sensor))  # <class '__main__.LineSensor'>
```

**Key point:** Parentheses `()` after the class name create a new object.

---

## Slide 6: The `__init__` Method (Constructor)

**`__init__` runs automatically when you create an object:**
```python
class LineSensor:
    def __init__(self):
        self.reflectance = Reflectance.get_default_reflectance()
        self.threshold = 0.5
```

**What each part means:**
- `def __init__(self):` -- special method, called the **constructor**
- `self` -- refers to the object being created ("me, myself")
- `self.reflectance` -- stores the sensor hardware *on this object*
- `self.threshold` -- stores 0.5 *on this object*

**Using it:**
```python
sensor = LineSensor()       # __init__ runs here!
print(sensor.threshold)     # Prints: 0.5
```

**The big idea:** `self.something` means "this object's something"

---

## Slide 7: Understanding `self`

**`self` = "the object referring to itself"**

```
LineSensor (blueprint)             Objects (built from blueprint)
    __init__(self)
        self.threshold = 0.5  -->  sensor_a.threshold = 0.5
                              -->  sensor_b.threshold = 0.5
```

**When you write:**
```python
sensor_a = LineSensor()
```
Python does this behind the scenes:
1. Creates a new empty object
2. Passes it to `__init__` as `self`
3. `self.threshold = 0.5` sets this object's threshold
4. Returns the object, which you store in `sensor_a`

**Analogy:** Two students in class each say "my name is..." -- `self` is each student's word for "my."

**Rule:** You write `self` in the definition. You NEVER write `self` when calling.
```python
# Definition: self is first parameter
def get_error(self):
    ...

# Call: no self -- Python adds it automatically
error = sensor.get_error()
```

---

## Slide 8: Adding Methods

**A method is a function inside a class:**
```python
class LineSensor:
    def __init__(self):
        self.reflectance = Reflectance.get_default_reflectance()
        self.threshold = 0.5

    def get_left(self):
        return self.reflectance.get_left()

    def get_right(self):
        return self.reflectance.get_right()

    def get_error(self):
        return self.get_left() - self.get_right()
```

**Key rules for methods:**
- Indented inside the class (one level in)
- Always take `self` as the first parameter
- Use `self.` to access attributes (`self.reflectance`)
- Use `self.` to call other methods (`self.get_left()`)

**Calling methods on an object:**
```python
sensor = LineSensor()
print(sensor.get_left())    # Read left sensor
print(sensor.get_error())   # Compute error
```

---

## Slide 9: Boolean Methods -- `is_at_cross()` and `is_off_line()`

**Methods that return True or False:**
```python
def is_at_cross(self):
    return self.get_left() > self.threshold and self.get_right() > self.threshold

def is_off_line(self):
    return self.get_left() < self.threshold and self.get_right() < self.threshold
```

**What they detect:**

| Situation | Left Sensor | Right Sensor | `is_at_cross()` | `is_off_line()` |
|---|---|---|---|---|
| On the line, centered | high | low | False | False |
| On the line, left of center | low | high | False | False |
| At an intersection (cross) | high | high | **True** | False |
| Off the line entirely | low | low | False | **True** |

**Perfect for `while` loops and `if` statements:**
```python
while not sensor.is_at_cross():
    # keep following line...

if sensor.is_off_line():
    print("Lost the line!")
```

---

## Slide 10: The Complete LineSensor Class

```python
from XRPLib.reflectance import Reflectance

class LineSensor:
    def __init__(self):
        self.reflectance = Reflectance.get_default_reflectance()
        self.threshold = 0.5

    def get_left(self):
        return self.reflectance.get_left()

    def get_right(self):
        return self.reflectance.get_right()

    def get_error(self):
        return self.get_left() - self.get_right()

    def is_at_cross(self):
        return self.get_left() > self.threshold and self.get_right() > self.threshold

    def is_off_line(self):
        return self.get_left() < self.threshold and self.get_right() < self.threshold
```

**Inventory:**
- 1 class
- 1 constructor (`__init__`)
- 2 attributes (`self.reflectance`, `self.threshold`)
- 5 methods (`get_left`, `get_right`, `get_error`, `is_at_cross`, `is_off_line`)

---

## Slide 11: Before vs. After -- Why Classes Win

**Before (Lesson 7 -- no class):**
```python
reflectance = Reflectance.get_default_reflectance()
threshold = 0.5

left = reflectance.get_left()
right = reflectance.get_right()
error = left - right
at_cross = left > threshold and right > threshold
off_line = left < threshold and right < threshold
```

**After (Lesson 8 -- with class):**
```python
sensor = LineSensor()

error = sensor.get_error()
at_cross = sensor.is_at_cross()
off_line = sensor.is_off_line()
```

**What improved:**
- Fewer lines of code where you use it
- Reads almost like English
- Sensor logic is packaged and reusable
- Threshold is stored in one place

---

## Slide 12: Common Mistakes & Connection to Lesson 9

**Watch out for these errors:**
```python
# Mistake 1: Forgetting self in method definition
def get_error():          # WRONG -- missing self
def get_error(self):      # CORRECT

# Mistake 2: Forgetting self. when accessing attributes
return reflectance.get_left()          # WRONG -- which reflectance?
return self.reflectance.get_left()     # CORRECT

# Mistake 3: Passing self when calling
sensor.get_error(sensor)   # WRONG -- Python does this automatically
sensor.get_error()         # CORRECT
```

**Coming up in Lesson 9:**
- Today: LineSensor class (sensor logic)
- Next: LineTrack class (driving logic that *uses* a LineSensor)
- This is called **object composition** -- one class using another class inside it

**Preview:**
```python
class LineTrack:
    def __init__(self):
        self.sensor = LineSensor()  # Uses LineSensor!
        self.drivetrain = DifferentialDrive.get_default_differential_drive()
```
