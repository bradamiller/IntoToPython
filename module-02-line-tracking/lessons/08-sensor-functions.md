# Lesson 8: Sensor Functions

## Overview
Students take the tangled sensor-reading code from Lesson 7 and organize it into a small toolkit of well-named functions, the same way Module 1 organized repeated driving code into `draw_polygon()`. Nothing here is new syntax -- students already know `def`, parameters, and `return` from Module 1. The one new pattern is functions sharing state through **global variables** (the sensor object, the threshold) instead of everything living inside one function. By the end, students will have a `get_error()` / `is_at_cross()` / `is_off_line()` toolkit they can call from anywhere in the file.

This lesson stands on its own -- classes are never required to finish it or any later module. An **optional extension** at the end of this file shows how to repackage the same toolkit as a `LineSensor` class, for courses that also want to cover OOP.

## Learning Objectives
By the end of this lesson, students will be able to:
- Explain why grouping related functions together makes code more organized and reusable
- Write a set of functions that share global variables (a hardware object, a threshold constant)
- Have one function call another function to avoid repeating logic
- Use the `global` keyword to modify a global variable from inside a function
- Recognize the "before and after" difference between tangled inline code and organized functions

## Key Concepts
- **Global variable**: Created once, outside any function, and readable by every function in the file
- **Constant**: A global variable written in `ALL_CAPS` by convention, signaling "this value shouldn't normally change" (e.g. `THRESHOLD`)
- **Function composition**: A function like `get_error()` calling other functions like `get_left()` / `get_right()` instead of repeating their logic
- **Helper function**: A small function whose only job is to be called by other functions
- **The `global` keyword**: Required inside a function only when that function *reassigns* a global variable, not when it only reads one

## Materials Required
- XRP Robot with reflectance sensor
- Whiteboard material with taped line (from previous lessons)
- VS Code with Python installed and XRPLib configured
- Reference: Lesson 7 line-following code (students will refactor it)
- Whiteboard or projector for live coding

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 8 min
**For 3-hour sessions:** 10-12 min

1. **Hook: The Messy Code Problem**:
   - Show the line-following code from Lesson 7 with all the sensor logic mixed together:
     ```python
     from XRPLib.reflectance import Reflectance
     from XRPLib.differential_drive import DifferentialDrive

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
             print("Cross detected!")
             drivetrain.stop()
             break

         left_motor = base_effort - error * kp
         right_motor = base_effort + error * kp
         drivetrain.set_effort(left_motor, right_motor)
     ```
   - Ask: "This works, but what if you wanted to reuse just the sensor part in a different program? What if you wanted to check `is_at_cross()` from three different places in your code without copy-pasting the same `left > threshold and right > threshold` line each time?"
   - Problem: The sensor logic isn't given a name -- it's just inline expressions, repeated wherever it's needed.

2. **Introduce the Fix: A Toolkit of Functions**:
   - Reminder: "In Module 1, you already turned repeated driving code into `draw_polygon(sides, distance)`. We're doing the same thing here, just for sensor reading."
   - The difference this time: several functions need to share the *same* sensor object and the *same* threshold value. Instead of passing them in as parameters to every single function, we'll create them once, at the top of the file, as **global variables** -- exactly like `drivetrain` has been a global since Module 1.

3. **Preview the Goal**:
   - Show what the finished code will look like:
     ```python
     error = get_error()
     at_cross = is_at_cross()
     off_line = is_off_line()
     ```
   - Ask: "Doesn't this read almost like English?"

4. **Why This Matters**:
   - Organization: Related code stays together, with names that explain what it does
   - Reusability: Copy this block of functions into a new file and it just works
   - Readability: `is_at_cross()` is clearer than `left > 0.5 and right > 0.5`
   - Continuity: This is the exact same skill from Module 1 (`def`, parameters, `return`) applied to a new problem

### Guided Practice: Building the Sensor Toolkit (20 minutes)
**For 50-min classes:** 18 min
**For 3-hour sessions:** 25 min

1. **Step 1: The Shared Globals**:
   - Start by creating the sensor object and threshold once, at the top of the file:
     ```python
     from XRPLib.reflectance import Reflectance

     reflectance = Reflectance.get_default_reflectance()
     THRESHOLD = 0.5
     ```
   - Explain:
     - This line runs once, when the program starts -- not inside any function.
     - `reflectance` and `THRESHOLD` are **global variables**. Every function defined below can read them without receiving them as a parameter.
     - This is the exact same pattern as `drivetrain = DifferentialDrive.get_default_differential_drive()` from Module 1 -- create it once at the top, use it everywhere below.
     - `THRESHOLD` is written in capitals by convention, to signal "this is a constant -- a value we don't expect to change while the program runs."

2. **Step 2: `get_left()` and `get_right()`**:
   - Nothing new here -- just Module 1 functions:
     ```python
     def get_left():
         return reflectance.get_left()

     def get_right():
         return reflectance.get_right()
     ```
   - Point out: these functions take no parameters, but they still work, because they read the global `reflectance` instead.
   - Test:
     ```python
     print(get_left())
     print(get_right())
     ```

3. **Step 3: `get_error()` -- Functions Calling Functions**:
   - Recall from Lesson 6: error = left - right
     ```python
     def get_error():
         return get_left() - get_right()
     ```
   - Explain: `get_error()` doesn't read the sensor directly -- it calls `get_left()` and `get_right()`, the functions we just wrote. This is **function composition**: building bigger functions out of smaller ones, instead of repeating the same two lines everywhere.
   - Test:
     ```python
     error = get_error()
     print(f"Error: {error}")
     ```

4. **Step 4: `is_at_cross()` and `is_off_line()`**:
   - These return `True` or `False` (Boolean values):
     ```python
     def is_at_cross():
         return get_left() > THRESHOLD and get_right() > THRESHOLD

     def is_off_line():
         return get_left() < THRESHOLD and get_right() < THRESHOLD
     ```
   - Explain:
     - `is_at_cross()`: Both sensors see dark (the line) -- this means a cross/intersection
     - `is_off_line()`: Neither sensor sees dark -- the robot has wandered off the line
     - Notice `THRESHOLD` is used directly, no different from how `get_left()` is used -- both are just names available to every function in the file
   - Test:
     ```python
     print(f"At cross? {is_at_cross()}")
     print(f"Off line? {is_off_line()}")
     ```

5. **Demo: Complete Sensor Toolkit on Robot**:
   - Show the complete toolkit and a test program:
     ```python
     from XRPLib.reflectance import Reflectance
     from XRPLib.board import Board
     import time

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

     # Test program
     board = Board.get_default_board()

     board.wait_for_button()

     for i in range(20):
         error = get_error()
         cross = is_at_cross()
         off = is_off_line()
         print(f"Error: {error:.2f}  Cross: {cross}  Off: {off}")
         time.sleep(0.5)
     ```
   - Upload and run on the robot. Move the robot over the line by hand to see values change.
   - Celebrate: "You just organized your first Python toolkit of sensor functions!"

### Independent Practice (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

**Exercise 1: Build the Sensor Toolkit from Scratch**
- Students type the complete set of functions from memory (or with minimal reference)
- Write a test program that:
  1. Reads `get_error()` in a loop 10 times
  2. Prints whether the robot is at a cross or off the line
- Expected code:
  ```python
  from XRPLib.reflectance import Reflectance
  from XRPLib.board import Board
  import time

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

  board = Board.get_default_board()

  board.wait_for_button()

  for i in range(10):
      print(f"Error: {get_error():.2f}")
      print(f"  At cross: {is_at_cross()}")
      print(f"  Off line: {is_off_line()}")
      time.sleep(0.5)
  ```

**Exercise 2: Add a `status()` Function**
- Add a new function that prints a human-readable status report:
  ```python
  def status():
      left = get_left()
      right = get_right()
      error = get_error()
      print(f"Left: {left:.2f}  Right: {right:.2f}  Error: {error:.2f}")
      if is_at_cross():
          print("  --> CROSS DETECTED")
      elif is_off_line():
          print("  --> OFF THE LINE")
      else:
          print("  --> Tracking line")
  ```
- Test by moving the robot over the line by hand

**Exercise 3 (Advanced): A `set_threshold()` Function and the `global` Keyword**
- Add a function that changes the shared `THRESHOLD`:
  ```python
  def set_threshold(new_value):
      global THRESHOLD
      THRESHOLD = new_value
  ```
- Try it:
  ```python
  set_threshold(0.3)
  print(f"Low threshold cross: {is_at_cross()}")

  set_threshold(0.7)
  print(f"High threshold cross: {is_at_cross()}")
  ```
- Discussion: "Why does `set_threshold()` need the word `global`, but `is_at_cross()` doesn't?" (`is_at_cross()` only *reads* `THRESHOLD`, which any function can do freely. `set_threshold()` *reassigns* it -- without `global`, Python would create a brand-new local variable called `THRESHOLD` that disappears when the function ends, and the real global would be untouched.)
- Follow-up: "Could you have two sensors with two different thresholds at the same time using just globals?" (No -- there's only one `THRESHOLD` for the whole program. That's a real limitation of this approach, and it's exactly the problem the Optional Extension below solves.)

### Assessment

**Formative (during lesson)**:
- Can students explain why grouping functions together is useful?
- Can they identify which variables are global and explain why they don't need to be passed as parameters?
- Can they trace `get_error()` calling `get_left()` and `get_right()`?
- Do they understand when `global` is required inside a function?

**Summative (worksheet/exit ticket)**:
1. What line of code creates the global `reflectance` object, and where does it go in the file?
2. Why doesn't `get_error()` need `reflectance` passed in as a parameter?
3. Write a function `is_on_line()` that returns True when at least one sensor sees the line.
4. Given the toolkit above, what does `get_error()` return when the robot is centered on the line?
5. Why does `set_threshold()` need the `global` keyword but `get_error()` does not?

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "These are just Module 1 functions -- nothing has changed" | Mostly true, and that's the point! The only new idea is several functions sharing state through global variables instead of getting everything through parameters. |
| "I can change `THRESHOLD` inside any function and it updates everywhere" | Reading a global works automatically. *Reassigning* one inside a function requires the `global` keyword, or Python quietly creates a new local variable instead. |
| "The order I define these functions in matters" | In Python, a function's body isn't checked until it's called, so as long as every function is defined before you *call* any of them, the order of the `def` statements doesn't matter. We still write helpers first for readability. |
| "Global variables are always bad practice" | For one robot with one set of sensors, a few well-named globals at the top of a file is completely reasonable -- it's the same pattern used for `drivetrain` since Module 1. Globals become a real problem when a program needs several independent, simultaneous copies of the same state -- see the Optional Extension below for how classes solve that. |

## Differentiation

**For struggling students**:
- Provide the complete sensor toolkit as a handout; focus on understanding how to call it rather than writing it from scratch
- Start with just `get_error()` -- add the others one at a time
- Use the analogy warm-up (Part 1 of the worksheet) to build intuition before writing code
- Pair with a stronger student for the exercises
- Allow reference to the guided practice code

**For advanced students**:
- Add a `calibrate()` function that reads the sensor 10 times and sets `THRESHOLD` to the average (using `global`)
- Add a `get_position()` function that returns `"left"`, `"right"`, `"center"`, `"cross"`, or `"lost"` as a string
- Work through the Optional Extension below and compare the two versions directly

## Materials & Code Examples

### Complete Sensor Toolkit
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

### Comparison: Before and After
**Before (Lesson 7 style -- tangled inline code):**
```python
reflectance = Reflectance.get_default_reflectance()
threshold = 0.5

left = reflectance.get_left()
right = reflectance.get_right()
error = left - right
at_cross = left > threshold and right > threshold
```

**After (Lesson 8 style -- organized functions):**
```python
error = get_error()
at_cross = is_at_cross()
```

## Teaching Notes
- **There is no new syntax beyond global variables and functions calling functions** -- both students have already seen the pieces from Module 1.
- **The only genuinely new idea is the `global` keyword**, and it only comes up in Exercise 3.
- **Tie it back to Module 1 explicitly.** Say out loud: "This is `def`, parameters, and `return` -- the same tools from Module 1, applied to sensor code instead of shape-drawing code."
- **The Optional Extension is a separate, self-contained add-on.** If your course doesn't cover classes, skip it entirely -- Lesson 9 and every later module only depend on the functions above, never on the class version.
- **Common errors to watch for:**
  - Trying to pass `reflectance` or `THRESHOLD` as a parameter when it's already a global (harmless, but unnecessary -- point out the simplification)
  - Forgetting `global THRESHOLD` inside `set_threshold()` in Exercise 3, then being confused why the change "doesn't stick"
  - Calling a function before its `def` has run (all `def` statements must execute once, top to bottom, before any are called)

## Connections to Next Lessons
- **Lesson 9** will add a second toolkit of driving functions that calls into this sensor toolkit.
- **Lesson 10** (Final Project) will combine both toolkits in a complete program.
- **Module 3** will keep using these exact functions for grid navigation.

---

## Optional Extension: Refactor into a `LineSensor` Class

*For courses that also cover classes/objects. Skip this section entirely otherwise -- nothing later in the course depends on it. The robot behaves identically either way; this only changes how the code is packaged.*

### Why Refactor at All?
The toolkit above works well for one robot with one set of sensors. But a global variable only ever holds one value at a time -- if a program ever needed two independent sensors (two robots, or two sensor bars), `THRESHOLD` couldn't be two different things at once, as the class discussion in Exercise 3 already noticed. A **class** solves exactly this: it lets you create multiple independent copies ("instances") of the same toolkit, each with its own data.

### From Functions to a Class, Step by Step

1. **Wrap it in a `class` block:**
   ```python
   class LineSensor:
       pass
   ```
   - `class`: says "I'm defining a new kind of thing."
   - `LineSensor`: the name we chose, capitalized by convention (CamelCase).

2. **Turn the global variables into an `__init__` method:**
   The globals `reflectance` and `THRESHOLD` become **attributes** that belong to a specific object, created through `self`:
   ```python
   class LineSensor:
       def __init__(self):
           self.reflectance = Reflectance.get_default_reflectance()
           self.threshold = 0.5
   ```
   - `__init__` is the **constructor** -- it runs automatically when you write `LineSensor()`.
   - `self` refers to the specific object being built right now. Two different `LineSensor()` objects each get their own `self`, so `self.threshold = 0.5` means "*this* object's threshold is 0.5" -- a second one could be given a different value.

3. **Turn each function into a method** by adding `self` as the first parameter, and prefixing shared names with `self.`:
   ```python
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
   - Notice: everywhere `get_left()` used to call another function directly, it now needs `self.` in front -- `self.get_left()` instead of `get_left()`. Every method takes `self` as its first parameter, but you never type it when *calling* a method -- Python passes it automatically.

4. **Using it:**
   ```python
   sensor = LineSensor()
   error = sensor.get_error()
   at_cross = sensor.is_at_cross()
   ```
   Compare to the functions version -- same call shape, just `sensor.` in front instead of nothing.

### The Payoff: Multiple Independent Instances
```python
sensor_low = LineSensor()
sensor_low.threshold = 0.3

sensor_high = LineSensor()
sensor_high.threshold = 0.7

print("Low threshold cross:", sensor_low.is_at_cross())
print("High threshold cross:", sensor_high.is_at_cross())
```
This is the one thing the functions-only version genuinely cannot do: two independent objects, each with its own `threshold`, existing at the same time.

### Discussion Prompt
"What would you have had to do to run two sensors with different thresholds using only the functions version?" (There's no clean way -- you'd need to rename every function and global variable twice, e.g. `get_error_a()` / `get_error_b()`. A class avoids that entirely by giving each object its own copy of the data.)

### Common Misconceptions (Class Version)

| Misconception | Reality |
|---|---|
| "A class and an object are the same thing" | A class is the blueprint; an object is a specific thing built from it. You can make many objects from one class. |
| "self is a special variable I need to type when calling methods" | You never type `self` when calling a method. Python passes it automatically -- `sensor.get_error()`, not `sensor.get_error(sensor)`. |
| "self.threshold and a plain threshold variable are the same" | `self.threshold` belongs to the object and persists. A plain `threshold` inside a method is local and disappears when the method ends -- same idea as needing `global` in the functions version, but attached to an object instead of the whole program. |

### Worksheet
See the "Optional Extension" section at the end of the Lesson 8 worksheet for matching exercises.
