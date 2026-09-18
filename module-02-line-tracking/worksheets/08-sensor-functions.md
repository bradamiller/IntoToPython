# Lesson 8 Worksheet: Sensor Functions

**Name:** __________________ **Date:** __________________ **Team:** __________________

## Part 1: Toolkit Warm-Up

A toolkit of functions shares **global variables** (data every function can read) and provides **functions** (actions built from that data). For each real-world object, list its shared data and its actions.

**Example -- TV Remote:**
- Shared data: current channel, volume level, power state
- Actions: change channel, adjust volume, power on, power off

**Your turn -- Smartphone:**
- Shared data: ________________________________________________________________
- Actions: _______________________________________________________________

**Your turn -- XRP Robot:**
- Shared data: ________________________________________________________________
- Actions: _______________________________________________________________

**How is a global variable like a shared notebook that every function in the file can read?**

_________________________________________________________________

_________________________________________________________________

## Part 2: Vocabulary Matching

Match each term to its definition:

| Term | Definition |
|---|---|
| A) Global variable | _____ A function whose only job is to be called by other functions |
| B) Constant | _____ A variable created once, outside any function, readable by all functions |
| C) Function composition | _____ Required inside a function only when it reassigns a global variable |
| D) Helper function | _____ A global variable written in ALL_CAPS by convention |
| E) `global` keyword | _____ One function calling another function to build up bigger behavior |

## Part 3: Toolkit Anatomy

Label each part of this code with the correct term from the word bank.

**Word bank:** global variable, constant, function definition, function call, helper function

```python
reflectance = Reflectance.get_default_reflectance()   # A) __________
THRESHOLD = 0.5                                        # B) __________

def get_error():                                       # C) __________
    return get_left() - get_right()                    # D) __________ (calls two ______ functions)

error = get_error()                                     # E) __________
```

## Part 4: Reading the Globals

Look at this code:

```python
from XRPLib.reflectance import Reflectance

reflectance = Reflectance.get_default_reflectance()
THRESHOLD = 0.5

def get_left():
    return reflectance.get_left()
```

Answer these questions:

1. How many global variables are created before any function runs? _____

2. What are their names? __________________ and __________________

3. What value does `THRESHOLD` start with? _____

4. When does `reflectance = Reflectance.get_default_reflectance()` run? (Circle one)
   - a) Every time `get_left()` is called
   - b) Once, when the program first runs, before any function is called
   - c) Only when you import the file
   - d) At the end of the program

5. Does `get_left()` need `reflectance` passed in as a parameter? Why or why not?

   _________________________________________________________________

## Part 5: Function Definitions vs. Function Calls

For each line of code, write whether it is a **definition** or a **call**:

| Code | Definition or Call? |
|---|---|
| `def get_error():` | _________________ |
| `get_error()` | _________________ |
| `def is_at_cross():` | _________________ |
| `is_at_cross()` | _________________ |
| `def get_left():` | _________________ |
| `error = get_error()` | _________________ |

**Key question:** When you call `get_error()`, is there ever a dot before it, or an object it belongs to?

YES / NO

**Why?** _________________________________________________________________

## Part 6: Tracing Function Execution

Given this code, trace the output:

```python
THRESHOLD = 0.5
print("Toolkit loaded!")

def get_threshold():
    return THRESHOLD

print(f"Threshold is {get_threshold()}")
```

**Output (in order):**

1. _______________________________

2. _______________________________

## Part 7: Global vs. Local Variable

Look at these two versions. What is different?

**Version A:**
```python
THRESHOLD = 0.5

def set_threshold(new_value):
    global THRESHOLD
    THRESHOLD = new_value

set_threshold(0.7)
print(THRESHOLD)
```

**Version B:**
```python
THRESHOLD = 0.5

def set_threshold(new_value):
    THRESHOLD = new_value   # No "global" -- will this work as expected?

set_threshold(0.7)
print(THRESHOLD)
```

**What does Version A print?** _____

**What does Version B print?** _____

**Why are they different?** _________________________________________________________________

_________________________________________________________________

**Rule:** To *change* a global variable from inside a function, you must write `global <name>` first -- otherwise Python creates a brand-new local variable with the same name, and the real global is left untouched.

## Part 8: Write a Function

The sensor toolkit has `get_left()` and `get_right()`. Using those, write `get_error()`:

```python
def get_error():
    return _____________________________________________
```

Now write `is_at_cross()`. It should return `True` when **both** sensors read above `THRESHOLD`:

```python
def is_at_cross():
    return _____________________________________________
```

Now write `is_off_line()`. It should return `True` when **both** sensors read below `THRESHOLD`:

```python
def is_off_line():
    return _____________________________________________
```

## Part 9: Using the Sensor Toolkit

Fill in the blanks to call the sensor toolkit's functions:

```python
# Step 1: Read the error value
error = _______________()

# Step 2: Check if robot is at a cross
if _______________():
    print("Cross detected!")

# Step 3: Check if robot is off the line
if _______________():
    print("Lost the line!")
```

## Part 10: Spot the Errors

Each code snippet has a mistake. Find and fix it.

**Error 1:**
```python
THRESHOLD = 0.5

def set_threshold(new_value):
    THRESHOLD = new_value

set_threshold(0.8)
print(THRESHOLD)   # Prints 0.5, not 0.8 -- why?
```

Problem: ________________________________________________________________

Fix: ____________________________________________________________________

**Error 2:**
```python
def get_error():
    return left - right   # left and right were never defined anywhere
```

Problem: ________________________________________________________________

Fix: ____________________________________________________________________

**Error 3:**
```python
error = get_error()   # This line runs first

def get_error():
    return get_left() - get_right()
```

Problem: ________________________________________________________________

Fix: ____________________________________________________________________

**Error 4:**
```python
def Get_Error():
    return get_left() - get_right()

print(get_error())   # Doesn't match the function name above
```

Problem: ________________________________________________________________

Fix: ____________________________________________________________________

## Part 11: Code Prediction

What does this program print?

```python
count = 0

def add():
    global count
    count = count + 1

def get_count():
    return count

add()
add()
add()
print(get_count())
```

**Output:** _______________________________

**Explanation:** _________________________________________________________________

## Part 12: Before and After Comparison

Rewrite this Lesson 7 style code using the sensor toolkit's functions.

**Before (tangled inline code):**
```python
reflectance = Reflectance.get_default_reflectance()
threshold = 0.5

left = reflectance.get_left()
right = reflectance.get_right()
error = left - right

if left > threshold and right > threshold:
    print("At a cross!")
```

**After (with the sensor toolkit):**
```python
error = _______________()

if _______________():
    print("At a cross!")
```

**Which version is easier to read?** _______________________________

**Why?** _________________________________________________________________

## Part 13: Design a New Function

Design a function called `is_on_line()` that returns `True` when **at least one** sensor sees the line (reads above the threshold). The robot is on the line when the left sensor OR the right sensor detects dark.

```python
def is_on_line():
    return _____________________________________________
```

**Test your logic:** Fill in what `is_on_line()` returns for each situation:

| Left Sensor | Right Sensor | `is_on_line()` returns |
|---|---|---|
| 0.8 (dark) | 0.2 (light) | __________ |
| 0.2 (light) | 0.7 (dark) | __________ |
| 0.8 (dark) | 0.9 (dark) | __________ |
| 0.1 (light) | 0.2 (light) | __________ |

## Part 14: Toolkit Design Challenge (Advanced)

Design a toolkit of functions that wraps the XRP board's button. Think about what global data it needs and what functions it should provide.

**Global variable(s) it needs:**
- _________________________________________________________________

**Functions:**
- `wait()`: ____________________________________________________
- Another function you would add: _____________________________________

**Sketch the code:**
```python
board = _______________________________________________

def wait():
    _______________________________________________
```

## Part 15: Reflection

**Why doesn't a function like `get_error()` need `reflectance` passed in as a parameter?**

_________________________________________________________________

_________________________________________________________________

**What is the difference between the functions in this lesson and the functions from Lesson 10 of Module 1?**

_________________________________________________________________

_________________________________________________________________

**Name one advantage of organizing sensor code into named functions instead of writing it directly in your program:**

_________________________________________________________________

_________________________________________________________________

**What was the most confusing part of today's lesson?**

_________________________________________________________________

_________________________________________________________________

---

## Part 16 (Optional Extension): Refactor into a Class

*Skip this section if your course doesn't cover classes.*

1. **What line turns the plain function `get_error()` into a method?** (Circle one)
   - a) Renaming it to `getError()`
   - b) Adding `self` as its first parameter
   - c) Adding a docstring
   - d) Moving it to a different file

2. **Fill in the blanks to turn this global-variable setup into a class `__init__`:**

   **Functions version:**
   ```python
   reflectance = Reflectance.get_default_reflectance()
   THRESHOLD = 0.5
   ```

   **Class version:**
   ```python
   class LineSensor:
       def __init__(___________):
           ___________.reflectance = Reflectance.get_default_reflectance()
           ___________.threshold = 0.5
   ```

3. **Fill in the blanks to turn this function into a method:**

   **Functions version:**
   ```python
   def get_error():
       return get_left() - get_right()
   ```

   **Class version:**
   ```python
   def get_error(___________):
       return ___________.get_left() - ___________.get_right()
   ```

4. **What does `self` refer to inside a method?**

   _________________________________________________________________

5. **Why can't the functions-only version have two sensors with two different thresholds at the same time, but the class version can?**

   _________________________________________________________________

   _________________________________________________________________

6. **Given `sensor_a = LineSensor()` and `sensor_b = LineSensor()`, if you set `sensor_a.threshold = 0.3` and leave `sensor_b.threshold` at 0.5, does changing `sensor_a.threshold` affect `sensor_b`?**

   YES / NO -- **Why?** _________________________________________________________________
