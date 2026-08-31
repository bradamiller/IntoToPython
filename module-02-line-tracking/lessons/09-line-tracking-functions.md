# Lesson 9: Line-Tracking Functions

## Overview
Students add a second group of functions -- `track_until_cross()`, `turn_right()`, `turn_left()` -- that combine the sensor toolkit from Lesson 8 with motor control to follow a line and turn at intersections. The driving functions simply *call* the sensor functions directly, since everything lives in the same shared scope. By the end, students will have two cooperating toolkits that can navigate a taped course.

This lesson stands on its own -- classes are never required to finish it or any later module. An **optional extension** at the end of this file shows how to repackage both toolkits as cooperating `LineSensor` and `LineTrack` classes (object composition), for courses that also want to cover OOP.

## Learning Objectives
By the end of this lesson, students will be able to:
- Explain how one group of functions can build on another group of functions
- Use the sensor functions from Lesson 8 inside new driving functions, without rewriting them
- Implement proportional line tracking inside a function
- Implement turn functions that use sensor feedback to find the line
- Test and debug a multi-function program on the robot

## Key Concepts
- **Building on prior functions**: Reusing `get_error()`, `is_at_cross()`, `is_off_line()` from Lesson 8 exactly as written
- **Shared driving constants**: `BASE_EFFORT` and `KP` as globals, the same pattern `THRESHOLD` used in Lesson 8
- **Proportional control (review)**: Steering correction proportional to error, from Lesson 5
- **State-based behavior**: A `while` loop that runs until a condition becomes true
- **Clearing the intersection**: Driving a fixed 8 cm forward after detecting a cross so the robot's turning center -- not just its sensors -- is over the intersection before it turns

## Materials Required
- XRP Robot with reflectance sensor
- Whiteboard material with taped circle and a perpendicular cross line
- VS Code with Python installed and XRPLib configured
- Working sensor toolkit from Lesson 8 (`lesson-08-sensor-functions.py`)
- Whiteboard or projector for live coding

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 8 min
**For 3-hour sessions:** 10-12 min

1. **Hook: Two Jobs, One Robot**:
   - Review: "Last lesson, we built a toolkit of sensor functions. But the robot doesn't just read sensors -- it also needs to drive."
   - Ask: "Should the driving code go inside `get_error()`?" (No -- keep sensor-reading and driving separate, the same way Module 1 kept shape-drawing functions separate from setup code.)
   - Introduce the idea: "We'll add a second toolkit -- driving functions -- that calls the sensor functions whenever it needs to know where the line is."

2. **Introduce the Relationship**:
   - Analogy: "A car has an engine. The car doesn't rebuild the engine's parts inside itself -- it just uses the engine when it needs power. Our driving functions don't reimplement sensor reading -- they call the sensor functions when they need sensor data."
   - Draw on the board:
     ```
     Sensor toolkit (Lesson 8)          Driving toolkit (Lesson 9)
       get_left(), get_right()            track_until_cross()
       get_error()                 <----  turn_right()
       is_at_cross(), is_off_line()       turn_left()
     ```

3. **Why Keep Them Separate?**:
   - **Separation of concerns**: Sensor logic stays in the Lesson 8 functions. Driving logic stays in the Lesson 9 functions. Neither needs to know how the other is implemented internally.
   - **Reusability**: The Lesson 8 sensor toolkit could be reused in a completely different program that doesn't drive at all.
   - **Readability**: `is_at_cross()` inside `track_until_cross()` reads naturally -- "keep going until we're at a cross."

4. **Preview the Goal**:
   - Show what using the driving toolkit will look like:
     ```python
     track_until_cross()
     turn_right()
     track_until_cross()
     ```
   - Ask: "Three lines of code to follow a line, detect an intersection, and turn. How long was this in Lesson 7?"

### Guided Practice: Building the Driving Toolkit (20 minutes)
**For 50-min classes:** 18 min
**For 3-hour sessions:** 25 min

1. **Step 1: The Shared Driving Globals**:
   - Add the drivetrain and driving constants, alongside the Lesson 8 sensor globals:
     ```python
     from XRPLib.differential_drive import DifferentialDrive

     drivetrain = DifferentialDrive.get_default_differential_drive()
     BASE_EFFORT = 0.4
     KP = 0.5
     ```
   - Walk through each one:
     - `drivetrain`: Stores the motor controller, same pattern as every module since Module 1.
     - `BASE_EFFORT`: How fast the robot drives forward (baseline speed).
     - `KP`: The proportional control gain from Lesson 5.
   - Key point: "These are new globals, separate from `reflectance` and `THRESHOLD` from Lesson 8, but they live in the same file, so every function below -- old and new -- can see all four."

2. **Step 2: The `track_until_cross()` Function**:
   - This is the core line-following logic from Lessons 5-7, now packaged into one function:
     ```python
     def track_until_cross():
         while not is_at_cross():
             error = get_error()
             left = BASE_EFFORT - error * KP
             right = BASE_EFFORT + error * KP
             drivetrain.set_effort(left, right)
         drivetrain.stop()
     ```
   - Walk through the logic:
     - `while not is_at_cross():` -- Keep going until both sensors detect the line (a cross). Notice this calls the Lesson 8 function directly, no prefix needed.
     - `get_error()` -- Also called directly, from the Lesson 8 toolkit.
     - The proportional control math is identical to Lesson 5, just using the global `BASE_EFFORT` and `KP` instead of local variables.
     - `drivetrain.stop()` -- Stop when the cross is detected.
   - Point out: "Notice there's no prefix anywhere -- because these aren't attributes of an object, they're just names in the file's global scope."

3. **Step 3: Clearing the Intersection**:
   - Before turning, the robot needs to drive a little further forward. When `is_at_cross()` becomes true, the *sensors* are over the intersection, but the robot's turning center (its rear axle) is still behind it. If it turns now, it will pivot around the wrong point and end up misaligned with the new line.
   - Add a small helper function:
     ```python
     def clear_intersection():
         drivetrain.straight(8, 0.5)
     ```
   - Explain: "This drives forward a fixed 8 cm -- an exact distance, not a guess based on timing -- so the turning center ends up centered on the intersection before any turn happens."
   - Point out the composition pattern again: this is a small helper function whose only job is to be called by the turn functions next.

4. **Step 4: The `turn_right()` Function**:
   - The robot needs to turn right at an intersection. The strategy:
     1. Call `clear_intersection()` to drive past the cross
     2. Start spinning right
     3. Keep spinning until a sensor finds the line again
   - Code:
     ```python
     def turn_right():
         clear_intersection()
         drivetrain.set_effort(0.3, -0.3)
         while is_off_line():
             pass
         drivetrain.stop()
     ```
   - Walk through the logic:
     - `clear_intersection()`: Drive the fixed 8 cm from Step 3.
     - `drivetrain.set_effort(0.3, -0.3)`: Left wheel forward, right wheel backward -- robot spins clockwise (right).
     - `while is_off_line(): pass`: Keep spinning as long as neither sensor sees a line. `pass` means "do nothing here -- the motors are already spinning from the line above; just keep re-checking the condition."
     - `drivetrain.stop()`: A sensor found the line, so stop.

5. **Step 5: The `turn_left()` Function**:
   - Same logic as `turn_right()` but motors are reversed:
     ```python
     def turn_left():
         clear_intersection()
         drivetrain.set_effort(-0.3, 0.3)
         while is_off_line():
             pass
         drivetrain.stop()
     ```
   - Ask students: "What is the only difference between `turn_left()` and `turn_right()`?" (The motor efforts are swapped.)

6. **Step 6: Test the Complete Program**:
   - Put both toolkits together with a test program:
     ```python
     from XRPLib.reflectance import Reflectance
     from XRPLib.differential_drive import DifferentialDrive
     from XRPLib.board import Board

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

     drivetrain = DifferentialDrive.get_default_differential_drive()
     BASE_EFFORT = 0.4
     KP = 0.5

     def clear_intersection():
         drivetrain.straight(8, 0.5)

     def track_until_cross():
         while not is_at_cross():
             error = get_error()
             left = BASE_EFFORT - error * KP
             right = BASE_EFFORT + error * KP
             drivetrain.set_effort(left, right)
         drivetrain.stop()

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

     # Test program
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
   - Upload and run on the taped circle with cross.
   - Expected behavior: Robot follows the line, stops at the cross, clears the intersection, turns right to find the line, follows again until the cross, stops.

7. **Demo Discussion**:
   - "How many lines of actual logic are in the test program?" (Just 3 function calls plus prints.)
   - "Where is all the sensor reading and motor control code?" (Organized into the toolkits above, out of the way of the main program.)
   - "Could you write a completely different program using these same functions?" (Yes -- copy the toolkit block into a new file and call the functions in a different order.)

### Independent Practice (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

**Exercise 1: Build and Test the Driving Toolkit**
- Students type the complete sensor and driving toolkits
- Write a test program that:
  1. Follows the line until a cross
  2. Turns right
  3. Follows the line again until a cross
  4. Stops
- Test on the physical setup

**Exercise 2: Add a `turn_around()` Function**
- Add a function that performs a 180-degree turn by calling `turn_right()` twice:
  ```python
  def turn_around():
      turn_right()
      turn_right()
  ```
- Test it: Follow line to cross, turn around, follow line back to cross.
- Discussion: "Why does calling `turn_right()` twice make a 180-degree turn?" (Each `turn_right()` turns roughly 90 degrees -- from the cross line to the circle line. Two of those cover 180 degrees.)

**Exercise 3 (Advanced): Add Print Logging**
- Modify `track_until_cross()` to print the error while tracking:
  ```python
  def track_until_cross():
      while not is_at_cross():
          error = get_error()
          print(f"Tracking... error={error:.2f}")
          left = BASE_EFFORT - error * KP
          right = BASE_EFFORT + error * KP
          drivetrain.set_effort(left, right)
      drivetrain.stop()
      print("Cross detected -- stopped.")
  ```
- Add similar logging to `turn_right()` and `turn_left()`
- Discussion: How does logging help with debugging?

### Assessment

**Formative (during lesson)**:
- Can students explain how `track_until_cross()` uses functions from Lesson 8 without rewriting them?
- Can they trace what happens when `track_until_cross()` is called?
- Do they understand why `clear_intersection()` runs before turning, not after?

**Summative (worksheet/exit ticket)**:
1. Which two Lesson 8 functions does `track_until_cross()` call?
2. What does `clear_intersection()` do, and why does it come before the turn instead of using a timed delay?
3. Write a function `track_and_turn_right()` that follows the line until a cross and then turns right.
4. How would you make the robot turn around (180 degrees)?
5. Why can `turn_right()` call `is_off_line()` directly, with no dot and no object in front of it?

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "The driving functions and sensor functions are all one big toolkit" | They have different responsibilities and were built in different lessons, but nothing in Python enforces a boundary between them -- they just happen to share the same global scope. Good style still groups them by purpose with comments, as shown above. |
| "I need to recreate the sensor logic inside `track_until_cross()`" | No -- `track_until_cross()` just calls `is_at_cross()` and `get_error()`, the functions already built in Lesson 8. Never rewrite logic that already has a name. |
| "The while loop in `track_until_cross()` will freeze the program" | The loop runs very fast, checking the sensor hundreds of times per second. It exits as soon as `is_at_cross()` returns `True`. |
| "`pass` does something special" | `pass` literally means "do nothing." It's needed because Python requires at least one statement in a loop body. The loop keeps re-checking its condition on its own. |
| "`clear_intersection()` driving 8 cm is arbitrary, like a guess" | It's a fixed, measured distance (the offset between the front sensors and the rear turning center on this robot), not a timing guess -- that's why it uses `drivetrain.straight(8, 0.5)` instead of `set_effort()` plus a delay. |
| "I should put all my code in one giant function" | Good design uses several small, well-named functions, each with a clear job. |

## Differentiation

**For struggling students**:
- Provide the complete sensor toolkit (Lesson 8) as a pre-written file; students only need to add the driving toolkit
- Start with just `track_until_cross()` -- add turn functions after testing
- Use the diagram from the introduction to trace how the two toolkits communicate
- Pair with a partner: one student handles the sensor toolkit, the other handles the driving toolkit
- Provide skeleton code with blanks to fill

**For advanced students**:
- Add a `track_for_distance(distance)` function that follows the line for approximately a certain distance
- Add a `set_speed(speed)` function that changes `BASE_EFFORT` (using `global`) and updates `KP` accordingly
- Explore how to handle the case where `turn_right()` never finds a line (add a timeout using a loop counter, not `time.sleep`)
- Add an `emergency_stop()` function and discuss when it would be useful
- Work through the Optional Extension below and compare the two versions directly

## Materials & Code Examples

### Complete Two-Toolkit Program
```python
from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board

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

drivetrain = DifferentialDrive.get_default_differential_drive()
BASE_EFFORT = 0.4
KP = 0.5

def clear_intersection():
    drivetrain.straight(8, 0.5)

def track_until_cross():
    while not is_at_cross():
        error = get_error()
        left = BASE_EFFORT - error * KP
        right = BASE_EFFORT + error * KP
        drivetrain.set_effort(left, right)
    drivetrain.stop()

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

board = Board.get_default_board()

board.wait_for_button()

track_until_cross()
print("Cross detected!")
turn_right()
print("Turned right!")
track_until_cross()
print("Done!")
```

### Toolkit Relationship Diagram
```
Sensor toolkit (Lesson 8)              Driving toolkit (Lesson 9)
    reflectance (hardware)                 drivetrain (hardware)
    THRESHOLD (0.5)                        BASE_EFFORT (0.4), KP (0.5)
    get_left(), get_right()                clear_intersection()
    get_error()                    <----   track_until_cross()
    is_at_cross(), is_off_line()   <----   turn_right(), turn_left()
```

## Teaching Notes
- **Build on Lesson 8.** Make sure students are comfortable calling functions and using global variables before adding this second toolkit. If the class struggled with Lesson 8, review before moving on.
- **`clear_intersection()` uses a fixed distance, not a timed delay, on purpose.** This course avoids timing-based movement everywhere: distance-based commands are consistent regardless of battery level or surface friction, while a `time.sleep()` duration has to be re-tuned constantly.
- **`pass` in the while loop may confuse students.** Explain that the loop already does something -- it checks the condition. `pass` just means "nothing extra needed inside the loop body." The motors are already spinning from the `set_effort()` call above.
- **Test incrementally.** Have students test `track_until_cross()` before adding turn functions. Then test each turn function individually.
- **Physical setup matters.** Make sure the cross line is clearly perpendicular to the circle. If the cross is at a shallow angle, `is_at_cross()` might not trigger reliably.
- **The Optional Extension is a separate, self-contained add-on.** If your course doesn't cover classes, skip it entirely -- Lesson 10 and every later module only depend on the functions above, never on the class version.

## Connections to Next Lessons
- **Lesson 10** (Final Project) will use both toolkits in a complete program that follows the circle, detects the cross 4 times, and reverses direction each time.
- **Module 3** will keep calling these exact functions for grid navigation.
- **This function-calls-function pattern** will reappear whenever multiple toolkits need to cooperate.

---

## Optional Extension: Refactor into a `LineTrack` Class (Object Composition)

*For courses that also cover classes/objects -- builds directly on the Lesson 8 Optional Extension (`LineSensor` as a class). Skip this section entirely otherwise; nothing later in the course depends on it.*

### The Idea
Now that `LineSensor` is a class, `LineTrack` becomes a class that **contains** a `LineSensor` object as one of its own attributes. This is called **object composition** -- one class storing an instance of another class (a "has-a" relationship), as opposed to the "calls" relationship the functions version used.

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

### From Functions to a Class, Step by Step

1. **The `__init__` method** -- create a `LineSensor` object and store it, alongside the drivetrain and constants:
   ```python
   class LineTrack:
       def __init__(self):
           self.sensor = LineSensor()
           self.drivetrain = DifferentialDrive.get_default_differential_drive()
           self.base_effort = 0.4
           self.kp = 0.5
   ```
   - `self.sensor = LineSensor()` is the composition step: creating a `LineSensor` object and keeping a reference to it. When you create a `LineTrack`, it automatically creates its own `LineSensor` -- the caller never has to build one separately.

2. **Turn each function into a method**, replacing direct calls to the Lesson 8 functions with calls through `self.sensor`, and using `self.` for the driving constants:
   ```python
   def clear_intersection(self):
       self.drivetrain.straight(8, 0.5)

   def track_until_cross(self):
       while not self.sensor.is_at_cross():
           error = self.sensor.get_error()
           left = self.base_effort - error * self.kp
           right = self.base_effort + error * self.kp
           self.drivetrain.set_effort(left, right)
       self.drivetrain.stop()

   def turn_right(self):
       self.clear_intersection()
       self.drivetrain.set_effort(0.3, -0.3)
       while self.sensor.is_off_line():
           pass
       self.drivetrain.stop()

   def turn_left(self):
       self.clear_intersection()
       self.drivetrain.set_effort(-0.3, 0.3)
       while self.sensor.is_off_line():
           pass
       self.drivetrain.stop()
   ```
   - Compare to the functions version: `is_at_cross()` becomes `self.sensor.is_at_cross()` -- delegating to the `LineSensor` object it contains, instead of calling a bare function.

3. **Using it:**
   ```python
   tracker = LineTrack()
   tracker.track_until_cross()
   tracker.turn_right()
   tracker.track_until_cross()
   ```
   Same three-call shape as the functions version, just through one object instead of bare function names.

### Discussion Prompt
"`LineTrack` never reads `self.sensor.reflectance` directly -- it always goes through `self.sensor.is_at_cross()` and similar methods. Why might that be good design, even though `LineTrack` technically *could* reach in and read `self.sensor.reflectance` itself?" (Delegating through methods means `LineSensor`'s internals could change completely -- a different sensor, a different threshold strategy -- and `LineTrack` wouldn't need to change at all, as long as `is_at_cross()` still means the same thing.)

### Common Misconceptions (Class Version)

| Misconception | Reality |
|---|---|
| "I need to create a `LineSensor` separately and pass it in" | `LineTrack` creates its own `LineSensor` in `__init__`. The caller doesn't need to worry about it. |
| "`LineTrack` and `LineSensor` are the same kind of thing" | They have different responsibilities. `LineSensor` handles sensor logic; `LineTrack` handles driving logic that uses sensor data through composition. |

### Worksheet
See the "Optional Extension" section at the end of the Lesson 9 worksheet for matching exercises.
