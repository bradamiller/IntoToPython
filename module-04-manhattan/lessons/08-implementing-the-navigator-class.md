# Lesson 8: Driving the Path

## Overview
Students package the turning logic from Lesson 7 into working functions -- `desired_heading()`, `turn_to()`, and `drive_path()` -- that drive the XRP robot along any Manhattan path. Since a robot only ever has one position and one heading at a time, these functions don't need a class to hold that state: `position` and `heading` are threaded through as parameters and handed back as return values, the same "return the updated value" pattern used for `THRESHOLD` and `heading` throughout this course. `drive_path()` executes the required turns and line-following by calling directly into the **driving toolkit from Module 2/3** -- `turn_right()`, `track_until_cross()`, `clear_intersection()`. By the end of this lesson, students will have working functions that accept a path from `compute_manhattan_path()` and autonomously drive the robot through it, one intersection at a time. This is the payoff of building a reusable toolkit: the line-following and turning code students wrote in Module 2 now powers grid navigation without any changes.

This lesson stands on its own -- classes are never required. An **optional extension** at the end of this file shows the same functions packaged into a `Navigator` class that composes a `LineTrack` object, for courses that also cover OOP.

## Learning Objectives
By the end of this lesson, students will be able to:
- Implement `desired_heading(position, next_pos)` to convert a coordinate delta into a numeric heading (0-3)
- Implement `turn_to(heading, desired)` using a while loop that turns right until facing the correct direction, returning the updated heading
- Implement `drive_path(path, position, heading)` to loop through a list of coordinates, turning and line-following at each step, returning the final position and heading
- Explain why threading `position`/`heading` through parameters and return values works without a class
- Integrate `drive_path()` with `compute_manhattan_path()` to drive a computed path on the robot

## Key Concepts
- **Threading state through return values**: `turn_to()` and `drive_path()` don't store `position`/`heading` anywhere persistent -- they receive the current values as parameters and return the updated ones. The caller keeps track by reassigning: `position, heading = drive_path(path, position, heading)`.
- **Numeric headings**: 0=North, 1=East, 2=South, 3=West -- the same clockwise numbering from Lesson 7
- **`desired_heading(position, next_pos)`**: A function that computes the numeric heading (0-3) needed to move from the current position to the next position
- **`turn_to(heading, desired)`**: A function that uses a while loop to keep turning right until the robot faces the needed heading, wrapping from 3 back to 0, then returns the new heading
- **`drive_path(path, position, heading)`**: A function that loops through each coordinate in a path, clearing the intersection when going straight, turning as needed, and line-following to the next intersection -- returns the final `(position, heading)`
- **Reusing the Module 2/3 toolkit**: These functions don't control motors directly. They call `turn_right()`, `track_until_cross()`, and `clear_intersection()` -- the exact same functions built in Module 2 and reused all through Module 3 -- demonstrating the payoff of a reusable toolkit

## Materials Required
- XRP Robot with charged battery
- Grid mat or taped grid (at least 4x4)
- VS Code with Python installed and XRPLib configured
- Printed function design worksheet (see Materials & Code Examples)
- Whiteboard or projector for design diagrams
- Completed turn-logic work from Lesson 7
- Working driving toolkit (`turn_right()`, `track_until_cross()`, `clear_intersection()`) from Module 2/3

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 8 min
**For 3-hour sessions:** 10-12 min

1. **Review: Where We Left Off**:
   - Quick recap of Lesson 7: headings are numbers (0=N, 1=E, 2=S, 3=W), and we can turn right until we face the direction we need.
   - "We figured out the logic for turning. Today we are turning that into functions that actually drive the robot."

2. **Why Return Values Instead of a Class?**:
   - There's only ever one robot, one position, one heading -- there's no need for multiple independent copies of this state, unlike, say, wanting several `LineSensor`s at once.
   - So instead of storing `position` and `heading` on an object, functions just receive them as parameters and hand back the updated versions:
     ```
     position, heading = drive_path(path, position, heading)
     ```
   - "This should look familiar -- it's the same tuple-unpacking pattern from Module 4 Lesson 2, just returning two values instead of one."

3. **The Big Picture -- Reusing What We Built**:
   - `compute_manhattan_path()` computes the path: `[(1,0), (2,0), (2,1)]`
   - `drive_path()` drives the path by reusing the Module 2/3 toolkit
   - These functions don't touch motors directly. They call `turn_right()` to turn and `track_until_cross()` to follow the line to the next intersection.
   - "Remember building those functions? That was not just a Module 2 exercise. We are using them right now. This is why we build reusable toolkits."

4. **Preview the Goal**:
   - By the end of this lesson, you will run a program that computes a path and the robot physically drives it on the grid, following the lines from intersection to intersection.

### Guided Practice (20 minutes)
**For 50-min classes:** 18 min
**For 3-hour sessions:** 30 min

1. **Step 1: Implement `desired_heading()`**:
   - This is the same logic from Lesson 7:
     ```python
     def desired_heading(position, next_pos):
         row_diff = next_pos[0] - position[0]
         col_diff = next_pos[1] - position[1]
         if row_diff == -1:
             return 0  # North
         elif col_diff == 1:
             return 1  # East
         elif row_diff == 1:
             return 2  # South
         elif col_diff == -1:
             return 3  # West
     ```
   - Ask: "Why does this take `position` as a parameter instead of reading it from somewhere else?" Answer: There's no object remembering the robot's position for us, so the caller has to pass in whatever position it currently has.
   - Ask: "Why numbers instead of strings?" Answer: Numbers let us compare and count. We can keep turning right, adding 1 to the heading each time, until we reach the heading we need. The numbers wrap around from 3 back to 0, just like a compass.

2. **Step 2: Implement `turn_to()`**:
   - This is the core of the driving toolkit. It uses a while loop to keep turning right until the robot faces the correct direction:
     ```python
     def turn_to(heading, desired):
         while heading != desired:
             turn_right()
             heading = heading + 1
             if heading == 4:
                 heading = 0
         return heading
     ```
   - Walk through the logic:
     - Keep turning right until facing the needed heading. Each `turn_right()` physically turns the robot -- this is the exact function built in Module 2, reused as-is.
     - The heading increments by 1 each time, wrapping from 3 back to 0. If the heading reaches 4, we reset it to 0 because there are only four directions (0, 1, 2, 3).
     - If the robot is already facing the right direction, the while loop does not execute at all -- zero turns.
     - `turn_right()` is sensor-based -- it drives forward off the intersection, spins right, and stops when it finds the next line. This is the same function that worked on the circle in Module 2 and the grid in Module 3, and it works here too.
     - **`return heading`**: Since `heading` is a local variable inside this function, the caller needs the updated value handed back explicitly. Forgetting this `return` is the single most common bug in this lesson.
   - Ask: "Why not use `turn_left()` for 3 turns?" Answer: Three right turns and one left turn reach the same heading. Using only right turns keeps the code simple -- one while loop handles every case. (Advanced students can optimize later.)

3. **Step 3: Implement `drive_path()`**:
   - This function ties everything together:
     ```python
     def drive_path(path, position, heading):
         for next_pos in path:
             needed = desired_heading(position, next_pos)
             if heading == needed:
                 clear_intersection()
             heading = turn_to(heading, needed)
             track_until_cross()
             position = next_pos
         return position, heading
     ```
   - Key points to discuss:
     - `for next_pos in path:` iterates directly over the path. The path does not include the starting position, so every element is a new cell to drive to.
     - **Clearing the intersection**: When going straight (0 turns needed), the robot is sitting on the intersection it just arrived at. If it starts line-following immediately, the cross sensor will trigger right away. So we call `clear_intersection()` -- the same function from Module 2/3 -- to drive forward 8 cm before calling `track_until_cross()`.
     - When turning, `turn_to()` (via `turn_right()`) already drives the robot off the intersection as part of its turn sequence, so no extra clearing is needed there.
     - `track_until_cross()` follows the line until the robot detects the next intersection. No distance measurement needed -- the sensors tell the robot when it has arrived.
     - After arriving, we update the local `position` variable to the new cell.
     - **`return position, heading`**: At the very end, hand back both updated values as a tuple, so the caller can keep using them for the next call.

4. **Step 4: Integration Test on Paper**:
   - Before running on the robot, trace through a short path on the board:
     ```
     Manhattan path: [(1,0), (1,1)]
     Starting position (0,0), starting heading 0 (North)

     Step 1: next_pos = (1,0)
             needed = 2 (South)
             heading is 0, not 2 --> enter while loop
               turn_right, heading becomes 1
               heading is 1, not 2 --> keep looping
               turn_right, heading becomes 2
               heading is 2 == 2 --> exit while loop, return 2
             track_until_cross --> arrive at (1,0)

     Step 2: next_pos = (1,1)
             needed = 1 (East)
             heading is 2, not 1 --> enter while loop
               turn_right, heading becomes 3
               turn_right, heading becomes 0 (wrapped from 4)
               turn_right, heading becomes 1
               heading is 1 == 1 --> exit while loop, return 1
             track_until_cross --> arrive at (1,1)

     drive_path returns ((1,1), 1)
     ```
   - Confirm students can trace through before moving to the robot.
   - Ask: "What if step 2 needed heading 2 (South) again? Then heading already equals needed, so the while loop does not run. We call `clear_intersection()` and then follow the line straight ahead."

### Independent Practice (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 30-40 min

**Exercise 1: Complete the Functions**
- Students open the starter file `lesson-08-navigator.py` and fill in the TODO sections.
- `compute_manhattan_path()` and the Module 2/3 driving toolkit are provided complete. Students focus on `desired_heading()`, `turn_to()`, and `drive_path()`.

**Exercise 2: Desktop Testing**
- Before deploying to the robot, students test with print statements:
  ```python
  HEADING_NAMES = ["N", "E", "S", "W"]

  path = compute_manhattan_path((0, 0), (2, 2))
  print("Path:", path)

  position, heading = (0, 0), 0
  position, heading = drive_path(path, position, heading)
  print("Final position:", position)
  print("Final heading:", HEADING_NAMES[heading])
  ```
- Expected output should show the path and confirm the final position is (2, 2).

**Exercise 3: Robot Test (Single Leg)**
- Place the robot at (0, 0) on the grid, lined up on the line and facing North.
- Run the program with a short path: `(0, 0)` to `(1, 1)`.
- Observe: Does the robot turn correctly? Does it follow the line to the next intersection? Does it stop at the right cell?

**Exercise 4: Robot Test (Longer Path)**
- Test with a longer path: `(0, 0)` to `(2, 3)`.
- Count the steps. Does the robot visit the expected cells?
- Compare the robot's physical position with the expected path printed to the console.
- Watch carefully for the "going straight" case -- does the robot correctly clear the intersection before following the line forward?

### Assessment

**Formative (during lesson)**:
- Can students explain why `position` and `heading` are passed as parameters instead of stored somewhere persistent?
- Can they trace through `drive_path()` on paper, predicting which turns happen and each position update?
- Can they distinguish between the roles of `compute_manhattan_path()` (path planning) and `drive_path()` (path execution)?
- Can they explain why `drive_path()` calls `turn_right()` and `track_until_cross()` directly instead of controlling motors itself?
- Do they understand when and why the intersection needs to be cleared?

**Summative (worksheet/exit ticket)**:
1. What two pieces of state does `drive_path()` need to track, and why does it return them instead of storing them?
2. If the robot is at (1, 2) heading 1 (East) and the next position is (1, 1), what heading is needed? Trace through the while loop in `turn_to()` and count how many right turns the robot makes.
3. Why does `drive_path()` iterate directly over the path with `for next_pos in path:` instead of skipping any elements?
4. Why does the robot need to clear the intersection when going straight, but not when turning?
5. `drive_path()` never calls `DifferentialDrive` directly. How does it control the robot's motors? Why is this a good design?

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "`drive_path()` should also compute the path" | `drive_path()` only drives the path. `compute_manhattan_path()` computes the path. Separating concerns makes the code easier to understand and debug. |
| "I need some object to remember the current position" | The caller just keeps `position` and `heading` in two plain variables and reassigns them from the return value: `position, heading = drive_path(path, position, heading)`. No object needed. |
| "`turn_to()` should update a global heading variable" | It could, but returning the new value and having the caller reassign it is more explicit and easier to trace -- you can see exactly where `heading` changes by reading the code, not by hunting for a `global` statement. |
| "Forgetting `return heading` at the end of `turn_to()` is a minor issue" | It's the most common bug in this lesson. Without it, `turn_to()` computes the right value internally but throws it away -- the caller's `heading` variable never updates, and every subsequent turn calculation is wrong. |
| "I don't need `clear_intersection()` when going straight" | Without it, `track_until_cross()` will detect the current intersection immediately and stop. The robot needs to drive past the cross before it can follow the line to the next one. |
| "Three right turns is wasteful -- just turn left" | Three right turns and one left turn reach the same heading. Using only right turns keeps the code simple: one while loop handles all cases. Advanced students can optimize this later. |

## Differentiation

**For struggling students**:
- Provide `desired_heading()` complete; have students focus only on `turn_to()` and `drive_path()`
- Use print statements instead of toolkit calls for initial testing (desktop mode)
- Walk through the loop in `drive_path()` one iteration at a time with the student
- Pair with a partner who completed Lesson 7 exercises successfully
- Provide a reference card showing the while loop pattern: "keep turning right until heading equals needed, wrapping from 3 back to 0, then return heading"

**For advanced students**:
- Add a function `log_action(action)` that appends every action (turn and drive) to a growing list of strings
- Implement a `return_home(position, heading)` function that computes and drives the path back to (0, 0)
- Add error handling: what if `desired_heading()` receives a diagonal move?
- Optimize `turn_to()` to choose between turning right and turning left based on which direction is fewer turns
- Work through the Optional Extension below and compare the two versions directly

## Materials & Code Examples

### Function Design Template
```
desired_heading(position, next_pos)  -->  returns 0/1/2/3 based on coordinate delta
turn_to(heading, desired)            -->  turns the robot, returns the new heading
drive_path(path, position, heading)  -->  drives the entire path, returns (position, heading)
```

### Driving Toolkit (from Module 2/3)
```python
from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive

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
    """Line-follow until a cross intersection is detected."""
    ...  # Implementation from Module 2

def turn_right():
    """Clear the intersection, spin right until finding the next line."""
    ...  # Implementation from Module 2
```

### Complete Driving Functions
```python
HEADING_NAMES = ["N", "E", "S", "W"]

def desired_heading(position, next_pos):
    """Determine heading (0-3) to move from position to next_pos."""
    row_diff = next_pos[0] - position[0]
    col_diff = next_pos[1] - position[1]
    if row_diff == -1:
        return 0  # North
    elif col_diff == 1:
        return 1  # East
    elif row_diff == 1:
        return 2  # South
    elif col_diff == -1:
        return 3  # West

def turn_to(heading, desired):
    """Turn the robot to face the given heading. Returns the new heading."""
    while heading != desired:
        turn_right()
        heading = heading + 1
        if heading == 4:
            heading = 0
    return heading

def drive_path(path, position, heading):
    """Drive the robot along the given path. Returns (position, heading)."""
    for next_pos in path:
        needed = desired_heading(position, next_pos)
        if heading == needed:
            clear_intersection()
        heading = turn_to(heading, needed)
        track_until_cross()
        position = next_pos
    return position, heading
```

### Integration Example
```python
HEADING_NAMES = ["N", "E", "S", "W"]

# ===== Main Program =====
position = (0, 0)
heading = 0

destination = (2, 3)
path = compute_manhattan_path(position, destination)
print("Path to", destination, ":", path)
position, heading = drive_path(path, position, heading)
print("Arrived at:", position)
print("Final heading:", HEADING_NAMES[heading])
```

## Teaching Notes
- **Build the functions incrementally.** Write `desired_heading()` first, test it. Add `turn_to()`, test it standalone with a fake starting heading. Then `drive_path()`. Do not write everything at once.
- **Emphasize reuse.** This is a key pedagogical moment. Students built the sensor/driving toolkit in Module 2, used it for the grid in Module 3, and now it powers Manhattan navigation in Module 4. `drive_path()` is only about 10 lines because it delegates all the hard work to the existing toolkit.
- **Test on desktop first.** Before running on the robot, temporarily replace `turn_right()` with `print("Turning right")` and `track_until_cross()` with `print("Following line to next intersection")` so students can see the logic executing without hardware.
- **The clearing maneuver matters.** When the robot goes straight through an intersection, it must call `clear_intersection()` before calling `track_until_cross()`. Without this, the sensors immediately detect the current intersection and stop. Walk through this scenario carefully on the board so students understand why.
- **`turn_right()` is sensor-based, not angle-based.** The robot does not turn exactly 90 degrees. It drives forward, spins, and stops when it finds the next line. This means it self-corrects on every turn, which is more reliable than angle-based turning.
- **Common coding errors to watch for:**
  - Forgetting the `return heading` at the end of `turn_to()`, or the `return position, heading` at the end of `drive_path()`
  - Including the start position in the path (it should not be there)
  - Forgetting to reassign `position, heading = drive_path(...)` in the calling code (the values are computed but never captured)
  - Forgetting the `clear_intersection()` call for the straight-ahead case
  - Using string headings instead of numbers
- **`compute_manhattan_path()` should be provided complete.** Students should not need to rewrite it. Copy it from Lesson 5 or import it.

## Connections to Next Lessons
- **Lesson 9** (Final Project) will combine `compute_manhattan_path()` and `drive_path()` into a multi-destination delivery program where the robot visits a sequence of locations.
- `drive_path()` becomes the execution engine that students build upon in the final project.
- Students will pass the updated `position` from each leg's `drive_path()` call directly into the next leg's `compute_manhattan_path()` call -- no separate synchronization step needed, since there's only one `position` variable, not two objects that could drift out of sync.

---

## Optional Extension: Package It as a `Navigator` Class

*For courses that also cover classes/objects -- builds on the Lesson 5 Optional Extension (`Manhattan` as a class). Skip this section entirely otherwise; nothing later in the course depends on it.*

### The Idea
A `Navigator` class bundles `position`, `heading`, and a `LineTrack` object together, so instead of threading state through return values, the object remembers its own state between method calls.

```python
HEADING_NAMES = ["N", "E", "S", "W"]

class Navigator:

    def __init__(self, start, heading):
        self.position = start
        self.heading = heading  # 0=N, 1=E, 2=S, 3=W
        self.line_track = LineTrack()

    def desired_heading(self, next_pos):
        row_diff = next_pos[0] - self.position[0]
        col_diff = next_pos[1] - self.position[1]
        if row_diff == -1:
            return 0  # North
        elif col_diff == 1:
            return 1  # East
        elif row_diff == 1:
            return 2  # South
        elif col_diff == -1:
            return 3  # West

    def turn_to(self, desired):
        while self.heading != desired:
            self.line_track.turn_right()
            self.heading = self.heading + 1
            if self.heading == 4:
                self.heading = 0

    def drive_path(self, path):
        for next_pos in path:
            needed = self.desired_heading(next_pos)
            if self.heading == needed:
                self.line_track.clear_intersection()
            self.turn_to(needed)
            self.line_track.track_until_cross()
            self.position = next_pos
```

### Comparing the Two Versions
| Functions version | Class version |
|---|---|
| `desired_heading(position, next_pos)` | `nav.desired_heading(next_pos)` |
| `heading = turn_to(heading, desired)` | `nav.turn_to(desired)` (updates `self.heading` in place) |
| `position, heading = drive_path(path, position, heading)` | `nav.drive_path(path)` (updates `self.position`/`self.heading` in place) |
| Caller must reassign `position, heading` after every call | `nav` remembers its own state -- no reassignment needed |

Notice the trade-off: the class version's method calls are slightly shorter (no need to pass or reassign `position`/`heading`), because that bookkeeping now happens inside the object instead of at the call site.

### Using It
```python
manhattan = Manhattan((0, 0))
navigator = Navigator((0, 0), 0)

destination = (2, 3)
path = manhattan.compute_path(destination)
print("Path to", destination, ":", path)
navigator.drive_path(path)
print("Arrived at:", navigator.position)
print("Final heading:", HEADING_NAMES[navigator.heading])
```

### Discussion Prompt
"The class version's `drive_path()` doesn't `return` anything -- but the functions version does. Why?" (The class version updates `self.position` and `self.heading` directly, so the object itself already reflects the new state. The functions version has no object to update, so it must hand the new values back explicitly.)

### Worksheet
See the "Optional Extension" section at the end of the Lesson 8 worksheet for matching exercises.
