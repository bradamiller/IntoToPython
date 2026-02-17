# Lesson 8: Introduction to Classes -- LineSensor

## Overview
Students learn to create their first Python class by building a `LineSensor` class that wraps the reflectance sensor into a clean, organized object. This is the first time students encounter classes, so the lesson moves carefully from the "why" (organizing related code) through the new syntax (`class`, `__init__`, `self`, methods) to a fully working class they can test on their robot. By the end, students will have a reusable `LineSensor` object with methods for computing error, detecting intersections, and detecting when the robot has left the line.

## Learning Objectives
By the end of this lesson, students will be able to:
- Explain why classes are useful for organizing related functions and data
- Write a class definition using the `class` keyword
- Write an `__init__` method that initializes an object's data
- Understand the `self` parameter and explain its purpose
- Define methods inside a class and call them on an object
- Create an instance of a class and use its methods

## Key Concepts
- **Class**: A blueprint for creating objects that groups related data and functions together
- **Object / Instance**: A specific thing created from a class blueprint
- **`__init__` method**: The constructor -- runs automatically when you create a new object
- **`self`**: A reference to the current object; how a method accesses the object's own data
- **Method**: A function defined inside a class; always takes `self` as its first parameter
- **Attribute**: A variable that belongs to an object, accessed via `self.name`
- **Instantiation**: Creating an object from a class: `my_sensor = LineSensor()`

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
   - Ask: "This works, but what if you wanted to reuse the sensor logic in a different program? What if you wanted to share just the sensor part with a friend?"
   - Problem: The sensor code, the driving code, and the control logic are all tangled together.

2. **Introduce the Concept of a Class**:
   - Analogy: "A class is like a blueprint for a house. The blueprint describes what rooms the house has and what you can do in it. When you build an actual house from the blueprint, that is an object."
   - Second analogy: "Think of a TV remote. The remote is an object. It has data (the channel, the volume) and actions (change channel, increase volume). A class describes what every remote looks like and can do."
   - Key idea: **A class groups related data and functions together into one package.**

3. **Preview the Goal**:
   - Show what the finished code will look like:
     ```python
     sensor = LineSensor()
     error = sensor.get_error()
     at_cross = sensor.is_at_cross()
     off_line = sensor.is_off_line()
     ```
   - Ask: "Doesn't this read almost like English? That is the power of a well-designed class."

4. **Why Classes Matter**:
   - Organization: Related code stays together
   - Reusability: Use the same class in many programs
   - Readability: `sensor.is_at_cross()` is clearer than `left > 0.5 and right > 0.5`
   - Real-world: Every library you have used (`DifferentialDrive`, `Reflectance`, `Board`) is a class

### Guided Practice: Building the LineSensor Class (20 minutes)
**For 50-min classes:** 18 min
**For 3-hour sessions:** 25 min

1. **Step 1: The Empty Class**:
   - Start with the simplest possible class:
     ```python
     class LineSensor:
         pass
     ```
   - Explain each part:
     - `class`: Keyword that says "I am defining a new type of thing"
     - `LineSensor`: The name we chose (capitalized by convention -- this is called CamelCase)
     - `:`: Just like `def` and `for`, a colon starts the body
     - `pass`: Placeholder meaning "nothing here yet"
   - Create an instance:
     ```python
     sensor = LineSensor()
     print(sensor)
     print(type(sensor))
     ```
   - Output shows something like `<__main__.LineSensor object at 0x...>` -- it exists!

2. **Step 2: Adding `__init__`**:
   - Explain: "When you create a new LineSensor, what does it need to know? It needs access to the reflectance sensor hardware and a threshold value."
   - Code:
     ```python
     from XRPLib.reflectance import Reflectance

     class LineSensor:
         def __init__(self):
             self.reflectance = Reflectance.get_default_reflectance()
             self.threshold = 0.5
     ```
   - Walk through each piece:
     - `def __init__(self):` -- This is the **constructor**. Python calls it automatically when you write `LineSensor()`.
     - The double underscores (called "dunder") mean it is a special Python method.
     - `self` -- This is the object being created. Think of it as "me" -- the object referring to itself.
     - `self.reflectance` -- This creates a variable called `reflectance` that belongs to this object. It stores the hardware sensor.
     - `self.threshold` -- Another variable that belongs to this object. We store 0.5 as our default threshold.
   - Test it:
     ```python
     sensor = LineSensor()
     print(sensor.threshold)  # Prints: 0.5
     ```

3. **Step 3: The self Explanation (Critical Moment)**:
   - This is the hardest concept. Take extra time here.
   - Draw on the board:
     ```
     LineSensor (the blueprint)
         __init__(self)
             self.reflectance = ...
             self.threshold = 0.5

     sensor_a = LineSensor()   -->  sensor_a.threshold = 0.5
     sensor_b = LineSensor()   -->  sensor_b.threshold = 0.5
     ```
   - Explain: "When you write `sensor_a = LineSensor()`, Python creates a new object and passes it into `__init__` as `self`. So `self.threshold = 0.5` means 'this particular object's threshold is 0.5'."
   - Analogy: "If you have two students in the class, each has their own name. `self` is like each student saying 'my name is...'. `self.threshold` means 'my threshold'."

4. **Step 4: Adding a Simple Method**:
   - Add `get_left()` and `get_right()`:
     ```python
     class LineSensor:
         def __init__(self):
             self.reflectance = Reflectance.get_default_reflectance()
             self.threshold = 0.5

         def get_left(self):
             return self.reflectance.get_left()

         def get_right(self):
             return self.reflectance.get_right()
     ```
   - Explain:
     - A **method** is just a function defined inside a class.
     - Every method takes `self` as its first parameter -- that is how it accesses the object's data.
     - `self.reflectance` refers to the sensor hardware we stored in `__init__`.
   - Test:
     ```python
     sensor = LineSensor()
     print(sensor.get_left())
     print(sensor.get_right())
     ```
   - Point out: When you call `sensor.get_left()`, Python automatically passes `sensor` as `self`. You never write `self` in the call -- only in the definition.

5. **Step 5: Adding `get_error()`**:
   - Recall from Lesson 6: error = left - right
   - Add the method:
     ```python
     def get_error(self):
         return self.get_left() - self.get_right()
     ```
   - Explain: A method can call other methods on the same object using `self`.
   - Test:
     ```python
     sensor = LineSensor()
     error = sensor.get_error()
     print(f"Error: {error}")
     ```

6. **Step 6: Adding `is_at_cross()` and `is_off_line()`**:
   - These methods return `True` or `False` (Boolean values):
     ```python
     def is_at_cross(self):
         return self.get_left() > self.threshold and self.get_right() > self.threshold

     def is_off_line(self):
         return self.get_left() < self.threshold and self.get_right() < self.threshold
     ```
   - Explain:
     - `is_at_cross()`: Both sensors see dark (the line) -- this means a cross/intersection
     - `is_off_line()`: Neither sensor sees dark -- the robot has wandered off the line
     - These return `True` or `False`, which is perfect for `while` and `if` statements
   - Test:
     ```python
     sensor = LineSensor()
     print(f"At cross? {sensor.is_at_cross()}")
     print(f"Off line? {sensor.is_off_line()}")
     ```

7. **Demo: Complete LineSensor on Robot**:
   - Show the complete class and a test program:
     ```python
     from XRPLib.reflectance import Reflectance
     from XRPLib.board import Board
     import time

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

     # Test program
     board = Board.get_default_board()
     sensor = LineSensor()

     board.wait_for_button()

     for i in range(20):
         error = sensor.get_error()
         cross = sensor.is_at_cross()
         off = sensor.is_off_line()
         print(f"Error: {error:.2f}  Cross: {cross}  Off: {off}")
         time.sleep(0.5)
     ```
   - Upload and run on the robot. Move the robot over the line by hand to see values change.
   - Celebrate: "You just wrote your first Python class!"

### Independent Practice (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

**Exercise 1: Build the LineSensor Class from Scratch**
- Students type the complete `LineSensor` class from memory (or with minimal reference)
- Write a test program that:
  1. Creates a `LineSensor` object
  2. Reads `get_error()` in a loop 10 times
  3. Prints whether the robot is at a cross or off the line
- Expected code:
  ```python
  from XRPLib.reflectance import Reflectance
  from XRPLib.board import Board
  import time

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

  board = Board.get_default_board()
  sensor = LineSensor()

  board.wait_for_button()

  for i in range(10):
      print(f"Error: {sensor.get_error():.2f}")
      print(f"  At cross: {sensor.is_at_cross()}")
      print(f"  Off line: {sensor.is_off_line()}")
      time.sleep(0.5)
  ```

**Exercise 2: Add a `status()` Method**
- Add a new method that prints a human-readable status report:
  ```python
  def status(self):
      left = self.get_left()
      right = self.get_right()
      error = self.get_error()
      print(f"Left: {left:.2f}  Right: {right:.2f}  Error: {error:.2f}")
      if self.is_at_cross():
          print("  --> CROSS DETECTED")
      elif self.is_off_line():
          print("  --> OFF THE LINE")
      else:
          print("  --> Tracking line")
  ```
- Test by moving the robot over the line by hand

**Exercise 3 (Advanced): Add a Configurable Threshold**
- Modify `__init__` to accept an optional threshold parameter:
  ```python
  class LineSensor:
      def __init__(self, threshold=0.5):
          self.reflectance = Reflectance.get_default_reflectance()
          self.threshold = threshold
  ```
- Create two sensors with different thresholds and compare behavior:
  ```python
  sensor_low = LineSensor(0.3)
  sensor_high = LineSensor(0.7)

  print(f"Low threshold cross: {sensor_low.is_at_cross()}")
  print(f"High threshold cross: {sensor_high.is_at_cross()}")
  ```
- Discussion: When would a lower or higher threshold be useful?

### Assessment

**Formative (during lesson)**:
- Can students explain why classes are useful?
- Can they identify the parts of a class definition (`class`, `__init__`, `self`, methods)?
- Can they create an instance and call methods on it?
- Do they understand that `self` refers to the current object?

**Summative (worksheet/exit ticket)**:
1. What keyword starts a class definition?
2. What method runs automatically when you create an object?
3. Why does every method take `self` as its first parameter?
4. Write a method `is_on_line()` that returns True when at least one sensor sees the line.
5. Given `sensor = LineSensor()`, what does `sensor.get_error()` return when the robot is centered on the line?

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "A class and an object are the same thing" | A class is the blueprint; an object is a specific thing built from that blueprint. You can make many objects from one class. |
| "self is a special variable I need to type when calling methods" | You never type `self` when calling a method. Python passes it automatically. `sensor.get_error()` works -- not `sensor.get_error(sensor)`. |
| "I need to memorize the double underscores in `__init__`" | Yes, the spelling matters, but the pattern is simple: two underscores, init, two underscores. It just means "initialize." |
| "`self.threshold` and `threshold` are the same" | `self.threshold` belongs to the object and persists. A plain `threshold` inside a method is a local variable that disappears when the method ends. |
| "Methods are totally different from functions" | Methods are functions that live inside a class. The only new thing is `self` as the first parameter. |
| "I need a class for everything" | Classes are best when you have related data and functions. For simple tasks, regular functions are fine. |

## Differentiation

**For struggling students**:
- Provide the complete `LineSensor` class as a handout; focus on understanding how to use it rather than writing it from scratch
- Start with just `__init__` and one method (`get_error`) -- add others one at a time
- Use the analogy worksheet (Part 1 of the worksheet) to build intuition before writing code
- Pair with a stronger student for the exercises
- Allow reference to the guided practice code

**For advanced students**:
- Add a `calibrate()` method that reads the sensor 10 times and sets the threshold to the average
- Add a `get_position()` method that returns "left", "right", "center", "cross", or "lost" as a string
- Research Python's `__str__` method and add one to `LineSensor` so `print(sensor)` shows useful info
- Create a second class (like `Button`) that wraps `Board` with a `wait()` method

## Materials & Code Examples

### Complete LineSensor Class
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

### Test Program
```python
from XRPLib.reflectance import Reflectance
from XRPLib.board import Board
import time

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

board = Board.get_default_board()
sensor = LineSensor()

board.wait_for_button()

for i in range(20):
    error = sensor.get_error()
    cross = sensor.is_at_cross()
    off = sensor.is_off_line()
    print(f"Error: {error:.2f}  Cross: {cross}  Off: {off}")
    time.sleep(0.5)
```

### Comparison: Before and After Classes
**Before (Lesson 7 style -- no class):**
```python
reflectance = Reflectance.get_default_reflectance()
threshold = 0.5

left = reflectance.get_left()
right = reflectance.get_right()
error = left - right
at_cross = left > threshold and right > threshold
```

**After (Lesson 8 style -- with class):**
```python
sensor = LineSensor()

error = sensor.get_error()
at_cross = sensor.is_at_cross()
```

## Teaching Notes
- **This is the hardest lesson in Module 2.** Go slowly. Repeat explanations. Use analogies.
- **`self` is the biggest stumbling block.** Spend extra time on it. Draw diagrams. Show that `self` is just the object itself.
- **Do not rush to advanced topics.** Students do not need to understand inheritance, class variables, or decorators. Keep it to `__init__`, `self`, and methods.
- **Live-code everything.** Type the class one method at a time. Run it after each addition. Let students see the process.
- **Use the robot to test.** The immediate feedback of "my class works on real hardware" is motivating.
- **Common syntax errors to watch for:**
  - Forgetting `self` in the parameter list
  - Forgetting `self.` when accessing attributes or calling other methods
  - Wrong indentation (methods must be indented inside the class)
  - Forgetting the colon after `class LineSensor:`
- **Terminology tip:** Use "method" consistently for functions in a class, and "function" for standalone `def` statements. This helps students distinguish the two.

## Connections to Next Lessons
- **Lesson 9** will use the `LineSensor` class inside a new `LineTrack` class. This is called **object composition** -- one class containing another.
- **Lesson 10** (Final Project) will combine both classes in a complete program.
- **Module 3** will extend these classes for grid navigation.
