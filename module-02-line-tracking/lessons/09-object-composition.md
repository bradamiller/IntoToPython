# Lesson 9: Object Composition -- LineTrack

## Overview
Students build a `LineTrack` class that uses the `LineSensor` class from Lesson 8 as one of its components. This introduces **object composition** -- the idea that one class can contain and use another class as part of its own data. The `LineTrack` class combines sensor reading (via `LineSensor`) with motor control (via `DifferentialDrive`) to create methods for following a line until a cross is detected and turning to find the line again. By the end, students will have two cooperating classes that can navigate a taped course.

## Learning Objectives
By the end of this lesson, students will be able to:
- Explain what object composition means and why it is useful
- Create a class that uses another class as an attribute
- Write methods that coordinate sensor input and motor output
- Implement proportional line tracking inside a class method
- Implement turn methods that use sensor feedback to find the line
- Test and debug a multi-class program on the robot

## Key Concepts
- **Object Composition**: One class storing an instance of another class as an attribute ("has-a" relationship)
- **Delegation**: When `LineTrack` needs sensor data, it asks its `LineSensor` object -- it delegates the work
- **Proportional Control (review)**: Using `get_error()` to steer smoothly
- **State-based behavior**: Methods that run until a condition is met (cross detected, line found)
- **`time.sleep()`**: Using a short delay to drive past the current intersection before looking for the next one

## Materials Required
- XRP Robot with reflectance sensor
- Whiteboard material with taped circle and a perpendicular cross line
- VS Code with Python installed and XRPLib configured
- Working `LineSensor` class from Lesson 8
- Whiteboard or projector for live coding

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 8 min
**For 3-hour sessions:** 10-12 min

1. **Hook: Two Jobs, One Robot**:
   - Review: "Last lesson, we built a LineSensor class that handles all the sensor logic. But the robot does not just read sensors -- it also needs to drive."
   - Ask: "Should we put the driving code inside LineSensor?" (No -- LineSensor is about sensors, not driving.)
   - Introduce the idea: "We need a second class that handles the driving part. But that class needs to use the sensor to know where the line is."

2. **Introduce Object Composition**:
   - Analogy: "A car has an engine. The car is one object, the engine is another object. The car uses the engine to move, but the engine does not know about the car's steering wheel. Each part has its own job."
   - In code terms: The `LineTrack` class will **contain** a `LineSensor` object and a `DifferentialDrive` object. It uses them together to follow a line.
   - Draw on the board:
     ```
     LineTrack
       |-- self.sensor = LineSensor()          <-- has-a LineSensor
       |-- self.drivetrain = DifferentialDrive  <-- has-a DifferentialDrive
       |-- self.base_effort = 0.4
       |-- self.kp = 0.5
       |
       |-- track_until_cross()   uses self.sensor and self.drivetrain
       |-- turn_right()          uses self.sensor and self.drivetrain
       |-- turn_left()           uses self.sensor and self.drivetrain
     ```

3. **Why Composition?**:
   - **Separation of concerns**: Sensor code stays in `LineSensor`. Driving logic stays in `LineTrack`. Neither class needs to know the other's internals.
   - **Reusability**: We could use `LineSensor` in a completely different program without `LineTrack`.
   - **Readability**: `self.sensor.is_at_cross()` reads naturally -- "my sensor says we are at a cross."

4. **Preview the Goal**:
   - Show what using LineTrack will look like:
     ```python
     tracker = LineTrack()
     tracker.track_until_cross()
     tracker.turn_right()
     tracker.track_until_cross()
     ```
   - Ask: "Three lines of code to follow a line, detect an intersection, and turn. How long was this in Lesson 7?"

### Guided Practice: Building the LineTrack Class (20 minutes)
**For 50-min classes:** 18 min
**For 3-hour sessions:** 25 min

1. **Step 1: The `__init__` Method**:
   - Start with the class skeleton and its constructor:
     ```python
     from XRPLib.differential_drive import DifferentialDrive
     import time

     class LineTrack:
         def __init__(self):
             self.sensor = LineSensor()
             self.drivetrain = DifferentialDrive.get_default_differential_drive()
             self.base_effort = 0.4
             self.kp = 0.5
     ```
   - Walk through each attribute:
     - `self.sensor = LineSensor()`: Creates a LineSensor object and stores it. This is **composition** -- LineTrack "has a" LineSensor.
     - `self.drivetrain`: Stores the motor controller (just like previous lessons).
     - `self.base_effort`: How fast the robot drives forward (baseline speed).
     - `self.kp`: The proportional control gain from Lesson 5.
   - Key point: "Notice that `LineSensor()` is called inside `__init__`. When you create a `LineTrack`, it automatically creates its own `LineSensor`. You do not need to create one separately."

2. **Step 2: The `track_until_cross()` Method**:
   - This is the core line-following method from Lessons 5-7, now packaged neatly:
     ```python
     def track_until_cross(self):
         while not self.sensor.is_at_cross():
             error = self.sensor.get_error()
             left = self.base_effort - error * self.kp
             right = self.base_effort + error * self.kp
             self.drivetrain.set_effort(left, right)
         self.drivetrain.stop()
     ```
   - Walk through the logic:
     - `while not self.sensor.is_at_cross():` -- Keep going until both sensors detect the line (a cross).
     - `self.sensor.get_error()` -- Ask our `LineSensor` for the current error.
     - The proportional control math is the same as Lesson 5, but now `base_effort` and `kp` come from `self`.
     - `self.drivetrain.set_effort(left, right)` -- Tell the motors what to do.
     - `self.drivetrain.stop()` -- Stop when the cross is detected.
   - Point out the composition: "See how `self.sensor` and `self.drivetrain` work together? The LineTrack class coordinates them."

3. **Step 3: The `turn_right()` Method**:
   - The robot needs to turn right at an intersection. The strategy:
     1. Start spinning right
     2. Wait briefly to drive off the cross (so the sensors are no longer on the intersection)
     3. Keep spinning until a sensor finds the line again
   - Code:
     ```python
     def turn_right(self):
         self.drivetrain.set_effort(0.3, -0.3)
         time.sleep(0.5)
         while self.sensor.is_off_line():
             pass
         self.drivetrain.stop()
     ```
   - Walk through the logic:
     - `self.drivetrain.set_effort(0.3, -0.3)`: Left wheel forward, right wheel backward -- robot spins clockwise (right).
     - `time.sleep(0.5)`: Wait half a second so the robot physically moves past the cross. Without this, the sensor might immediately see the same cross and stop.
     - `while self.sensor.is_off_line(): pass`: Keep spinning as long as neither sensor sees a line. The `pass` keyword means "do nothing -- just keep checking the condition."
     - `self.drivetrain.stop()`: A sensor found the line, so stop.

4. **Step 4: The `turn_left()` Method**:
   - Same logic as `turn_right()` but motors are reversed:
     ```python
     def turn_left(self):
         self.drivetrain.set_effort(-0.3, 0.3)
         time.sleep(0.5)
         while self.sensor.is_off_line():
             pass
         self.drivetrain.stop()
     ```
   - Ask students: "What is the only difference between `turn_left()` and `turn_right()`?" (The motor efforts are swapped.)

5. **Step 5: Test the Complete LineTrack Class**:
   - Put both classes together with a test program:
     ```python
     from XRPLib.reflectance import Reflectance
     from XRPLib.differential_drive import DifferentialDrive
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

     class LineTrack:
         def __init__(self):
             self.sensor = LineSensor()
             self.drivetrain = DifferentialDrive.get_default_differential_drive()
             self.base_effort = 0.4
             self.kp = 0.5

         def track_until_cross(self):
             while not self.sensor.is_at_cross():
                 error = self.sensor.get_error()
                 left = self.base_effort - error * self.kp
                 right = self.base_effort + error * self.kp
                 self.drivetrain.set_effort(left, right)
             self.drivetrain.stop()

         def turn_right(self):
             self.drivetrain.set_effort(0.3, -0.3)
             time.sleep(0.5)
             while self.sensor.is_off_line():
                 pass
             self.drivetrain.stop()

         def turn_left(self):
             self.drivetrain.set_effort(-0.3, 0.3)
             time.sleep(0.5)
             while self.sensor.is_off_line():
                 pass
             self.drivetrain.stop()

     # Test program
     board = Board.get_default_board()
     tracker = LineTrack()

     board.wait_for_button()

     print("Following line...")
     tracker.track_until_cross()
     print("Cross detected! Turning right...")
     tracker.turn_right()
     print("Following line again...")
     tracker.track_until_cross()
     print("Done!")
     ```
   - Upload and run on the taped circle with cross.
   - Expected behavior: Robot follows the line, stops at the cross, turns right to find the line, follows again until the cross, stops.

6. **Demo Discussion**:
   - "How many lines of actual logic are in the test program?" (Just 4 method calls plus prints.)
   - "Where is all the sensor reading and motor control code?" (Hidden inside the classes.)
   - "Could you write a completely different program using these same classes?" (Yes -- that is the point of composition and reusability.)

### Independent Practice (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

**Exercise 1: Build and Test LineTrack**
- Students type the complete `LineSensor` and `LineTrack` classes
- Write a test program that:
  1. Follows the line until a cross
  2. Turns right
  3. Follows the line again until a cross
  4. Stops
- Test on the physical setup
- Expected code:
  ```python
  from XRPLib.reflectance import Reflectance
  from XRPLib.differential_drive import DifferentialDrive
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

  class LineTrack:
      def __init__(self):
          self.sensor = LineSensor()
          self.drivetrain = DifferentialDrive.get_default_differential_drive()
          self.base_effort = 0.4
          self.kp = 0.5

      def track_until_cross(self):
          while not self.sensor.is_at_cross():
              error = self.sensor.get_error()
              left = self.base_effort - error * self.kp
              right = self.base_effort + error * self.kp
              self.drivetrain.set_effort(left, right)
          self.drivetrain.stop()

      def turn_right(self):
          self.drivetrain.set_effort(0.3, -0.3)
          time.sleep(0.5)
          while self.sensor.is_off_line():
              pass
          self.drivetrain.stop()

      def turn_left(self):
          self.drivetrain.set_effort(-0.3, 0.3)
          time.sleep(0.5)
          while self.sensor.is_off_line():
              pass
          self.drivetrain.stop()

  board = Board.get_default_board()
  tracker = LineTrack()

  board.wait_for_button()

  print("Following line...")
  tracker.track_until_cross()
  print("Cross! Turning right...")
  tracker.turn_right()
  print("Following again...")
  tracker.track_until_cross()
  print("Done!")
  ```

**Exercise 2: Add a `turn_around()` Method**
- Add a method that performs a 180-degree turn by calling `turn_right()` twice:
  ```python
  def turn_around(self):
      self.turn_right()
      self.turn_right()
  ```
- Test it: Follow line to cross, turn around, follow line back to cross.
- Discussion: "Why does calling `turn_right()` twice make a 180-degree turn?" (Each `turn_right()` turns roughly 90 degrees -- from the cross line to the circle line. Two of those cover 180 degrees.)

**Exercise 3 (Advanced): Add Print Logging to Methods**
- Modify `track_until_cross()` to print the error every 0.1 seconds while tracking:
  ```python
  def track_until_cross(self):
      while not self.sensor.is_at_cross():
          error = self.sensor.get_error()
          print(f"Tracking... error={error:.2f}")
          left = self.base_effort - error * self.kp
          right = self.base_effort + error * self.kp
          self.drivetrain.set_effort(left, right)
      self.drivetrain.stop()
      print("Cross detected -- stopped.")
  ```
- Add similar logging to `turn_right()` and `turn_left()`
- Discussion: How does logging help with debugging?

### Assessment

**Formative (during lesson)**:
- Can students explain what object composition means?
- Can they identify the "has-a" relationships in the LineTrack class?
- Can they trace what happens when `track_until_cross()` is called?
- Do they understand why `time.sleep(0.5)` is needed in the turn methods?

**Summative (worksheet/exit ticket)**:
1. What does "object composition" mean?
2. What two objects does a `LineTrack` store inside itself?
3. Why does `turn_right()` include `time.sleep(0.5)` before the while loop?
4. Write a method `track_and_turn_right()` that follows the line until a cross and then turns right.
5. How would you make the robot turn around (180 degrees)?

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "LineTrack and LineSensor are the same kind of thing" | They have different responsibilities. LineSensor handles sensor logic. LineTrack handles driving logic that uses sensor data. |
| "I need to create a LineSensor separately and pass it in" | LineTrack creates its own LineSensor in `__init__`. The caller does not need to worry about it. |
| "The while loop in track_until_cross will freeze the program" | The while loop runs very fast, checking the sensor hundreds of times per second. It exits as soon as `is_at_cross()` returns True. |
| "`pass` does something special" | `pass` literally means "do nothing." It is needed because Python requires at least one statement in a loop body. The while loop keeps running because the condition is still being checked. |
| "time.sleep(0.5) in turn methods is arbitrary" | It serves a specific purpose: giving the robot time to physically rotate past the cross so the sensors are no longer on the intersection line. Without it, the robot might immediately see the line and stop too soon. |
| "I should put all my code in one big class" | Good design uses multiple small classes, each with a clear job. This is the principle of separation of concerns. |

## Differentiation

**For struggling students**:
- Provide the complete `LineSensor` class as a pre-written file; students only need to write `LineTrack`
- Start with just `__init__` and `track_until_cross()` -- add turn methods after testing
- Use the diagram from the introduction to trace how the objects communicate
- Pair with a partner: one student handles the sensor class, the other handles the tracking class
- Provide skeleton code with blanks to fill

**For advanced students**:
- Add a `track_for_distance(distance)` method that follows the line for approximately a certain distance (using time as a rough estimate)
- Add a `set_speed(speed)` method that changes `base_effort` and updates `kp` accordingly
- Create a `turn_degrees(degrees)` method that turns an approximate number of degrees using timing
- Explore how to handle the case where `turn_right()` never finds a line (add a timeout)
- Add an `emergency_stop()` method and discuss when it would be useful

## Materials & Code Examples

### Complete Two-Class Program
```python
from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
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

class LineTrack:
    def __init__(self):
        self.sensor = LineSensor()
        self.drivetrain = DifferentialDrive.get_default_differential_drive()
        self.base_effort = 0.4
        self.kp = 0.5

    def track_until_cross(self):
        while not self.sensor.is_at_cross():
            error = self.sensor.get_error()
            left = self.base_effort - error * self.kp
            right = self.base_effort + error * self.kp
            self.drivetrain.set_effort(left, right)
        self.drivetrain.stop()

    def turn_right(self):
        self.drivetrain.set_effort(0.3, -0.3)
        time.sleep(0.5)
        while self.sensor.is_off_line():
            pass
        self.drivetrain.stop()

    def turn_left(self):
        self.drivetrain.set_effort(-0.3, 0.3)
        time.sleep(0.5)
        while self.sensor.is_off_line():
            pass
        self.drivetrain.stop()

board = Board.get_default_board()
tracker = LineTrack()

board.wait_for_button()

tracker.track_until_cross()
print("Cross detected!")
tracker.turn_right()
print("Turned right!")
tracker.track_until_cross()
print("Done!")
```

### Composition Diagram
```
LineTrack object
    |
    +-- self.sensor (LineSensor object)
    |       |-- self.reflectance (hardware)
    |       |-- self.threshold (0.5)
    |       |-- get_left(), get_right()
    |       |-- get_error()
    |       |-- is_at_cross(), is_off_line()
    |
    +-- self.drivetrain (DifferentialDrive object)
    |       |-- set_effort(), stop()
    |
    +-- self.base_effort (0.4)
    +-- self.kp (0.5)
    +-- track_until_cross()
    +-- turn_right(), turn_left()
```

## Teaching Notes
- **Build on Lesson 8.** Make sure students are comfortable with `class`, `__init__`, and `self` before introducing composition. If the class struggled with Lesson 8, spend extra time reviewing before diving into LineTrack.
- **The key insight is "has-a."** Repeat this phrase: "A LineTrack *has a* LineSensor. A LineTrack *has a* drivetrain." This is the mental model for composition.
- **The `time.sleep(0.5)` in turns is a physical-world requirement.** Explain that in code, things happen almost instantly, but the robot needs time to physically move past the intersection. Without the sleep, the turn method might immediately see the line and stop. Students should experiment with the sleep duration.
- **`pass` in the while loop may confuse students.** Explain that the while loop already does something -- it checks the condition. `pass` just means "I do not need to do anything else inside the loop body." The motors are already spinning from the `set_effort` call above.
- **Test incrementally.** Have students test `track_until_cross()` before adding turn methods. Then test each turn method individually.
- **Physical setup matters.** Make sure the cross line is clearly perpendicular to the circle. If the cross is at a shallow angle, `is_at_cross()` might not trigger reliably.
- **Expect tuning.** Students may need to adjust `base_effort`, `kp`, or the `time.sleep()` duration. This is normal robotics debugging -- encourage it.

## Connections to Next Lessons
- **Lesson 10** (Final Project) will use both classes in a complete program that follows the circle, detects the cross 4 times, and reverses direction each time.
- **Module 3** will extend `LineTrack` with grid navigation methods.
- **Composition pattern** will appear in future modules whenever multiple classes need to cooperate.
