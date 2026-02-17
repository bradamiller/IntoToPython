# Lesson 8 Worksheet: Introduction to Classes -- LineSensor

**Name:** __________________ **Date:** __________________ **Team:** __________________

## Part 1: Class Analogy Warm-Up

A class groups related **data** and **actions** together. For each real-world object, list its data (things it knows) and actions (things it can do).

**Example -- TV Remote:**
- Data: current channel, volume level, power state
- Actions: change channel, adjust volume, power on, power off

**Your turn -- Smartphone:**
- Data: ________________________________________________________________
- Actions: _______________________________________________________________

**Your turn -- XRP Robot:**
- Data: ________________________________________________________________
- Actions: _______________________________________________________________

**How is a class like a blueprint?**

_________________________________________________________________

_________________________________________________________________

## Part 2: Class Vocabulary Matching

Match each term to its definition:

| Term | Definition |
|---|---|
| A) Class | _____ A specific thing created from a blueprint |
| B) Object | _____ A function defined inside a class |
| C) Method | _____ A blueprint that groups data and functions |
| D) Attribute | _____ Runs automatically when an object is created |
| E) `__init__` | _____ A variable that belongs to an object |
| F) `self` | _____ The object referring to itself |

## Part 3: Class Anatomy

Label each part of this class with the correct term from the word bank.

**Word bank:** class keyword, class name, constructor, self parameter, attribute, method

```python
class LineSensor:                              # A) __________ B) __________
    def __init__(self):                        # C) __________ D) __________
        self.threshold = 0.5                   # E) __________

    def get_error(self):                       # F) __________
        return self.get_left() - self.get_right()
```

## Part 4: Reading `__init__`

Look at this `__init__` method:

```python
class LineSensor:
    def __init__(self):
        self.reflectance = Reflectance.get_default_reflectance()
        self.threshold = 0.5
```

Answer these questions:

1. How many attributes does each LineSensor object have? _____

2. What are the attribute names? __________________ and __________________

3. What value does `self.threshold` start with? _____

4. When does `__init__` run? (Circle one)
   - a) When you import the file
   - b) When you write `sensor = LineSensor()`
   - c) When you call `sensor.get_error()`
   - d) At the end of the program

5. What does `self` refer to inside `__init__`?

   _________________________________________________________________

## Part 5: Method Definitions vs. Method Calls

For each line of code, write whether it is a **definition** or a **call**:

| Code | Definition or Call? |
|---|---|
| `def get_error(self):` | _________________ |
| `sensor.get_error()` | _________________ |
| `def is_at_cross(self):` | _________________ |
| `sensor.is_at_cross()` | _________________ |
| `def __init__(self):` | _________________ |
| `sensor = LineSensor()` | _________________ |

**Key question:** When you call `sensor.get_error()`, do you type `self` in the parentheses?

YES / NO

**Why?** _________________________________________________________________

## Part 6: Tracing Method Execution

Given this class and program, trace the output:

```python
class LineSensor:
    def __init__(self):
        self.threshold = 0.5
        print("LineSensor created!")

    def get_threshold(self):
        return self.threshold

sensor = LineSensor()
print(f"Threshold is {sensor.get_threshold()}")
```

**Output (in order):**

1. _______________________________

2. _______________________________

## Part 7: self.attribute vs. Local Variable

Look at these two versions. What is different?

**Version A:**
```python
class LineSensor:
    def __init__(self):
        self.threshold = 0.5

    def check(self):
        print(self.threshold)  # Uses self.threshold
```

**Version B:**
```python
class LineSensor:
    def __init__(self):
        threshold = 0.5

    def check(self):
        print(threshold)  # No self -- will this work?
```

**Will Version B work?** YES / NO

**Why?** _________________________________________________________________

_________________________________________________________________

**Rule:** To save data on an object, always use `self.` -- otherwise the variable is local and disappears when the method ends.

## Part 8: Write a Method

The `LineSensor` class has `get_left()` and `get_right()` methods. Using those, write the `get_error()` method:

```python
def get_error(self):
    return _____________________________________________
```

Now write `is_at_cross()`. It should return `True` when **both** sensors read above the threshold:

```python
def is_at_cross(self):
    return _____________________________________________
```

Now write `is_off_line()`. It should return `True` when **both** sensors read below the threshold:

```python
def is_off_line(self):
    return _____________________________________________
```

## Part 9: Using a LineSensor Object

Fill in the blanks to create and use a LineSensor:

```python
# Step 1: Create an object
sensor = _______________()

# Step 2: Read the error value
error = sensor._______________()

# Step 3: Check if robot is at a cross
if sensor._______________():
    print("Cross detected!")

# Step 4: Check if robot is off the line
if sensor._______________():
    print("Lost the line!")
```

## Part 10: Spot the Errors

Each code snippet has a mistake. Find and fix it.

**Error 1:**
```python
class LineSensor:
    def __init__():
        self.threshold = 0.5
```

Problem: ________________________________________________________________

Fix: ____________________________________________________________________

**Error 2:**
```python
class LineSensor:
    def __init__(self):
        self.threshold = 0.5

    def get_error(self):
        return reflectance.get_left() - reflectance.get_right()
```

Problem: ________________________________________________________________

Fix: ____________________________________________________________________

**Error 3:**
```python
class LineSensor:
    def __init__(self):
        self.threshold = 0.5

sensor = LineSensor()
print(sensor.threshold)
sensor.get_error(sensor)   # Something is wrong here
```

Problem: ________________________________________________________________

Fix: ____________________________________________________________________

**Error 4:**
```python
class linesensor:
    def __init__(self):
        self.threshold = 0.5
```

Problem: ________________________________________________________________

Fix: ____________________________________________________________________

## Part 11: Code Prediction

What does this program print?

```python
class Counter:
    def __init__(self):
        self.count = 0

    def add(self):
        self.count = self.count + 1

    def get_count(self):
        return self.count

c = Counter()
c.add()
c.add()
c.add()
print(c.get_count())
```

**Output:** _______________________________

**Explanation:** _________________________________________________________________

## Part 12: Before and After Comparison

Rewrite this Lesson 7 style code using the `LineSensor` class.

**Before (no class):**
```python
reflectance = Reflectance.get_default_reflectance()
threshold = 0.5

left = reflectance.get_left()
right = reflectance.get_right()
error = left - right

if left > threshold and right > threshold:
    print("At a cross!")
```

**After (with LineSensor class):**
```python
sensor = _______________()

error = sensor._______________()

if sensor._______________():
    print("At a cross!")
```

**Which version is easier to read?** _______________________________

**Why?** _________________________________________________________________

## Part 13: Design a New Method

Design a method called `is_on_line()` that returns `True` when **at least one** sensor sees the line (reads above the threshold). The robot is on the line when the left sensor OR the right sensor detects dark.

```python
def is_on_line(self):
    return _____________________________________________
```

**Test your logic:** Fill in what `is_on_line()` returns for each situation:

| Left Sensor | Right Sensor | `is_on_line()` returns |
|---|---|---|
| 0.8 (dark) | 0.2 (light) | __________ |
| 0.2 (light) | 0.7 (dark) | __________ |
| 0.8 (dark) | 0.9 (dark) | __________ |
| 0.1 (light) | 0.2 (light) | __________ |

## Part 14: Class Design Challenge (Advanced)

Design a class called `Button` that wraps the XRP board's button. Think about what data it needs and what actions it should have.

**Class name:** `Button`

**Attributes (data it stores):**
- _________________________________________________________________

**Methods (actions it can do):**
- `__init__(self)`: _________________________________________________
- `wait(self)`: ____________________________________________________
- Another method you would add: _____________________________________

**Sketch the code:**
```python
class Button:
    def __init__(self):
        _______________________________________________

    def wait(self):
        _______________________________________________
```

## Part 15: Reflection

**What is the purpose of `self` in a class?**

_________________________________________________________________

_________________________________________________________________

**What is the difference between a function (from Lesson 10 of Module 1) and a method?**

_________________________________________________________________

_________________________________________________________________

**Name one advantage of putting sensor code into a class instead of writing it directly in your program:**

_________________________________________________________________

_________________________________________________________________

**What was the most confusing part of today's lesson?**

_________________________________________________________________

_________________________________________________________________
