# Lesson 8: Implementing the Navigator Class

## Overview
Students package the turning logic from Lesson 7 into a **Navigator class** that can drive the XRP robot along any Manhattan path. The Navigator class stores the robot's current position and heading (as a number 0-3), determines the needed heading for each step, executes the required turns using the **LineTrack class from Module 2**, and follows the line to the next intersection. By the end of this lesson, students will have a complete Navigator that accepts a path from the Manhattan class and autonomously drives the robot through it, one intersection at a time. This is the payoff of building reusable classes: the line-following and turning code students wrote in Module 2 now powers grid navigation without any changes.

## Learning Objectives
By the end of this lesson, students will be able to:
- Design a Navigator class with appropriate attributes (`position`, `heading`, `line_track`) and methods
- Implement `get_needed_heading()` to convert a coordinate delta into a numeric heading (0-3)
- Implement `turn_to()` using modular arithmetic and a loop of right turns to physically turn the robot
- Implement `drive_path()` to loop through a list of coordinates, turning and line-following at each step
- Integrate the Navigator class with the Manhattan class to drive a computed path on the robot

## Key Concepts
- **Navigator class**: A class that controls the robot's movement along a path, tracking position and heading
- **`__init__(self, start, heading)`**: Constructor that sets the starting position, initial heading (0-3), and creates a LineTrack object
- **Numeric headings**: 0=North, 1=East, 2=South, 3=West -- the same clockwise numbering from Lesson 7
- **`get_needed_heading(self, next_pos)`**: Method that computes the numeric heading (0-3) needed to move from the current position to the next position
- **`turn_to(self, needed_heading)`**: Method that uses `(needed - current) % 4` to calculate the number of right turns, executes them in a loop, and updates the heading
- **`drive_path(self, path)`**: Method that loops through each coordinate in a path, clearing the intersection when going straight, turning as needed, and line-following to the next intersection
- **Reusing LineTrack**: The Navigator does not control motors directly. It delegates all movement to the LineTrack class students built in Module 2, demonstrating the power of reusable code.
- **Integration**: Connecting two classes (Manhattan for path planning, Navigator for path execution) so they work together as a system

## Materials Required
- XRP Robot with charged battery
- Grid mat or taped grid (at least 4x4)
- VS Code with Python installed and XRPLib configured
- Printed Navigator class design worksheet (see Materials & Code Examples)
- Whiteboard or projector for class design diagrams
- Completed turn-logic work from Lesson 7
- Working LineTrack and LineSensor classes from Module 2

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 8 min
**For 3-hour sessions:** 10-12 min

1. **Review: Where We Left Off**:
   - Quick recap of Lesson 7: headings are numbers (0=N, 1=E, 2=S, 3=W), and `(needed - current) % 4` tells us how many right turns to make.
   - "We figured out the math for turning. Today we are packaging that into a class that actually drives the robot."

2. **Why a Class?**:
   - We already have a Manhattan class that plans the path. Now we need a Navigator class that executes the path.
   - A class bundles the robot's state (position, heading) with the logic (turn, drive) into one reusable object.
   - Draw on the board:
     ```
     Manhattan class           Navigator class
     ----------------          -----------------
     .position                 .position
     .compute_path()           .heading (number 0-3)
                               .line_track (LineTrack object)
                               .get_needed_heading()
                               .turn_to()
                               .drive_path()
     ```

3. **The Big Picture -- Reusing What We Built**:
   - Manhattan computes the path: `[(0,0), (1,0), (2,0), (2,1)]`
   - Navigator drives the path by reusing LineTrack from Module 2
   - The Navigator does not touch motors directly. It calls `line_track.turn_right()` to turn and `line_track.track_until_cross()` to follow the line to the next intersection.
   - "Remember building LineTrack? That was not just a Module 2 exercise. We are using it right now. This is why we build reusable classes."

4. **Preview the Goal**:
   - By the end of this lesson, you will run a program that computes a path and the robot physically drives it on the grid, following the lines from intersection to intersection.

### Guided Practice (20 minutes)
**For 50-min classes:** 18 min
**For 3-hour sessions:** 30 min

1. **Step 1: Design the `__init__` Method**:
   - Ask: "What does the Navigator need to know when it is created?"
   - Starting position (a tuple like `(0, 0)`)
   - Starting heading (a number: 0=N, 1=E, 2=S, 3=W)
   - A LineTrack object to control line-following and turning
   - Write on the board:
     ```python
     HEADING_NAMES = ["N", "E", "S", "W"]

     class Navigator:
         def __init__(self, start, heading):
             self.position = start
             self.heading = heading  # 0=N, 1=E, 2=S, 3=W
             self.line_track = LineTrack()
     ```
   - Explain: "We do not create a DifferentialDrive here. LineTrack already has one inside it. The Navigator talks to LineTrack, and LineTrack talks to the motors. Each class has its own job."
   - Point out `HEADING_NAMES`: this list lets us print a friendly name when we want to display the heading. `HEADING_NAMES[self.heading]` converts 0 to "N", 1 to "E", etc.

2. **Step 2: Implement `get_needed_heading()`**:
   - This is the same logic from Lesson 7, now as a method that returns a number:
     ```python
     def get_needed_heading(self, next_pos):
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
     ```
   - Ask: "Why does this use `self.position` instead of a `current` parameter?" Answer: The Navigator already knows its own position. That is the advantage of a class -- methods can access the object's own data.
   - Ask: "Why numbers instead of strings?" Answer: Numbers let us do math. We can calculate how many turns we need with subtraction and modular arithmetic -- one formula handles every case.

3. **Step 3: Implement `turn_to()`**:
   - This is the core of the Navigator, and it is beautifully simple thanks to the modular arithmetic from Lesson 7:
     ```python
     def turn_to(self, needed_heading):
         turns = (needed_heading - self.heading) % 4
         for i in range(turns):
             self.line_track.turn_right()
         self.heading = needed_heading
     ```
   - Walk through the logic:
     - `(needed - current) % 4` gives the number of right turns: 0 means already facing correctly, 1 means one right turn, 2 means two right turns (U-turn), 3 means three right turns (same as one left turn).
     - The `for` loop calls `self.line_track.turn_right()` that many times.
     - `turn_right()` is sensor-based -- it drives forward off the intersection, spins right, and stops when it finds the next line. This is the same method that worked on circles in Module 3, and it works here on the grid too.
   - Ask: "Why not use `turn_left()` for 3 turns?" Answer: Three right turns and one left turn reach the same heading. Using only right turns keeps the code simple -- one loop handles every case. (Advanced students can optimize later.)

4. **Step 4: Implement `drive_path()`**:
   - This method ties everything together:
     ```python
     def drive_path(self, path):
         for i in range(1, len(path)):
             next_pos = path[i]
             needed = self.get_needed_heading(next_pos)
             turns = (needed - self.heading) % 4
             if turns == 0:
                 self.line_track.drivetrain.straight(8)
             self.turn_to(needed)
             self.line_track.track_until_cross()
             self.position = next_pos
     ```
   - Key points to discuss:
     - `range(1, len(path))`: We skip index 0 because that is the starting position (the robot is already there).
     - **Clearing the intersection**: When going straight (0 turns needed), the robot is sitting on the intersection it just arrived at. If it starts line-following immediately, the cross sensor will trigger right away. So we drive forward 8 cm to clear the intersection before calling `track_until_cross()`.
     - When turning, `turn_right()` already drives the robot off the intersection as part of its turn sequence, so no extra clearing is needed.
     - `track_until_cross()` follows the line until the robot detects the next intersection. No distance measurement needed -- the sensors tell the robot when it has arrived.
     - After arriving, we update `self.position` to the new cell.

5. **Step 5: Integration Test on Paper**:
   - Before running on the robot, trace through a short path on the board:
     ```
     Manhattan path: [(0,0), (1,0), (1,1)]
     Navigator starts at (0,0) heading 0 (North)

     Step 1: next_pos = (1,0)
             needed = 2 (South)
             turns = (2 - 0) % 4 = 2 --> turn_right twice
             track_until_cross --> arrive at (1,0)

     Step 2: next_pos = (1,1)
             needed = 1 (East)
             turns = (1 - 2) % 4 = 3 --> turn_right three times
             track_until_cross --> arrive at (1,1)
     ```
   - Confirm students can trace through before moving to the robot.
   - Ask: "What if step 2 needed heading 2 (South) again? Then turns = (2-2) % 4 = 0, so we would clear the intersection with `straight(8)` and then follow the line straight ahead."

### Independent Practice (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 30-40 min

**Exercise 1: Complete the Navigator Class**
- Students open the starter file `lesson-08-navigator.py` and fill in the TODO sections.
- The Manhattan class and LineTrack/LineSensor classes are provided complete. Students focus on Navigator methods.

**Exercise 2: Desktop Testing**
- Before deploying to the robot, students test with print statements:
  ```python
  HEADING_NAMES = ["N", "E", "S", "W"]

  manhattan = Manhattan((0, 0))
  path = manhattan.compute_path((2, 2))
  print("Path:", path)

  nav = Navigator((0, 0), 0)
  nav.drive_path(path)
  print("Final position:", nav.position)
  print("Final heading:", HEADING_NAMES[nav.heading])
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
- Can students explain what attributes the Navigator class needs and why?
- Can they trace through `drive_path()` on paper, predicting each turn count and position update?
- Can they distinguish between the roles of Manhattan (path planning) and Navigator (path execution)?
- Can they explain why the Navigator uses LineTrack instead of controlling motors directly?
- Do they understand when and why the intersection needs to be cleared?

**Summative (worksheet/exit ticket)**:
1. What three attributes does the Navigator class store? Explain the purpose of each.
2. If the Navigator is at (1, 2) heading 1 (East) and the next position is (1, 1), what heading is needed? How many right turns does the robot make? Show the modular arithmetic.
3. Why does `drive_path()` start its loop at index 1 instead of index 0?
4. Why does the robot need to drive forward 8 cm when going straight, but not when turning?
5. The Navigator does not create a DifferentialDrive. How does it control the robot's motors? Why is this a good design?

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "The Navigator should also compute the path" | The Navigator only drives the path. The Manhattan class computes the path. Separating concerns makes the code easier to understand and debug. |
| "I need to pass the current position to `get_needed_heading`" | The Navigator already knows its position through `self.position`. That is the advantage of a class -- methods can access the object's own data. |
| "The Navigator needs a DifferentialDrive" | The Navigator uses a LineTrack object, which already contains a DifferentialDrive inside it. The Navigator does not need to know about motors -- it just asks LineTrack to turn or follow a line. This is called delegation. |
| "After turning, I need to calculate the new heading" | The new heading is always the heading you wanted to face. If you needed heading 1 (East) and you turned, you are now facing East regardless of how many right turns it took. |
| "`drive_path()` should start at index 0" | Index 0 is where the robot already is. Driving to your current position would be a wasted step. Start at index 1 to move to the first new cell. |
| "Three right turns is wasteful -- just turn left" | Three right turns and one left turn reach the same heading. Using only right turns keeps the code simple: one for-loop handles all four cases (0, 1, 2, or 3 turns). Advanced students can optimize this later. |
| "I don't need the `straight(8)` when going straight" | Without clearing the intersection, `track_until_cross()` will detect the current intersection immediately and stop. The robot needs to drive past the cross before it can follow the line to the next one. |

## Differentiation

**For struggling students**:
- Provide the `__init__` and `get_needed_heading()` methods complete; have students focus only on `turn_to()` and `drive_path()`
- Use print statements instead of LineTrack calls for initial testing (desktop mode)
- Walk through the loop in `drive_path()` one iteration at a time with the student
- Pair with a partner who completed Lesson 7 exercises successfully
- Provide a reference card showing the modular arithmetic: `(needed - current) % 4` with examples

**For advanced students**:
- Add a `log` attribute that records every action (turn and drive) as a list of strings
- Implement a `return_home()` method that drives the robot back to its starting position
- Add error handling: what if `get_needed_heading()` receives a diagonal move?
- Optimize `turn_to()` to use `turn_left()` when 3 right turns are needed (compare `turns` to decide)
- Add a `print_status()` method that displays current position and heading name after each step

## Materials & Code Examples

### Navigator Class Design Template
```
Navigator Class
===============
Attributes:
  - position:    (row, col) tuple -- where the robot is now
  - heading:     number 0-3 (0=N, 1=E, 2=S, 3=W) -- which way the robot faces
  - line_track:  LineTrack object -- handles line-following and turning

Methods:
  - __init__(start, heading):        Set up position, heading, and line_track
  - get_needed_heading(next_pos):    Return 0/1/2/3 based on coordinate delta
  - turn_to(needed_heading):         Turn the robot to face the given heading
  - drive_path(path):                Drive along the entire path
```

### LineTrack and LineSensor Classes (from Module 2)
```python
from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive

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
        self.Kp = 0.5

    def track_until_cross(self):
        """Line-follow until a cross intersection is detected."""
        ...  # Implementation from Module 2

    def turn_right(self):
        """Drive forward off the intersection, spin right until finding the next line."""
        ...  # Implementation from Module 2

    def turn_left(self):
        """Drive forward off the intersection, spin left until finding the next line."""
        ...  # Implementation from Module 2
```

### Complete Navigator Class
```python
HEADING_NAMES = ["N", "E", "S", "W"]

class Navigator:

    def __init__(self, start, heading):
        """Create a Navigator at the given start position and heading."""
        self.position = start
        self.heading = heading  # 0=N, 1=E, 2=S, 3=W
        self.line_track = LineTrack()

    def get_needed_heading(self, next_pos):
        """Determine heading (0-3) to move from current position to next_pos."""
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

    def turn_to(self, needed_heading):
        """Turn the robot to face the given heading."""
        turns = (needed_heading - self.heading) % 4
        for i in range(turns):
            self.line_track.turn_right()
        self.heading = needed_heading

    def drive_path(self, path):
        """Drive the robot along the given path."""
        for i in range(1, len(path)):
            next_pos = path[i]
            needed = self.get_needed_heading(next_pos)
            turns = (needed - self.heading) % 4
            if turns == 0:
                self.line_track.drivetrain.straight(8)
            self.turn_to(needed)
            self.line_track.track_until_cross()
            self.position = next_pos
```

### Integration Example
```python
HEADING_NAMES = ["N", "E", "S", "W"]

class Manhattan:
    def __init__(self, start):
        self.position = start

    def compute_path(self, destination):
        path = [self.position]
        current_row = self.position[0]
        current_col = self.position[1]
        dest_row = destination[0]
        dest_col = destination[1]
        if dest_row > current_row:
            row_step = 1
        else:
            row_step = -1
        if dest_col > current_col:
            col_step = 1
        else:
            col_step = -1
        while current_row != dest_row:
            current_row = current_row + row_step
            path.append((current_row, current_col))
        while current_col != dest_col:
            current_col = current_col + col_step
            path.append((current_row, current_col))
        return path

class Navigator:
    def __init__(self, start, heading):
        self.position = start
        self.heading = heading  # 0=N, 1=E, 2=S, 3=W
        self.line_track = LineTrack()

    def get_needed_heading(self, next_pos):
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

    def turn_to(self, needed_heading):
        turns = (needed_heading - self.heading) % 4
        for i in range(turns):
            self.line_track.turn_right()
        self.heading = needed_heading

    def drive_path(self, path):
        for i in range(1, len(path)):
            next_pos = path[i]
            needed = self.get_needed_heading(next_pos)
            turns = (needed - self.heading) % 4
            if turns == 0:
                self.line_track.drivetrain.straight(8)
            self.turn_to(needed)
            self.line_track.track_until_cross()
            self.position = next_pos

# ===== Main Program =====
manhattan = Manhattan((0, 0))
navigator = Navigator((0, 0), 0)

destination = (2, 3)
path = manhattan.compute_path(destination)
print("Path to", destination, ":", path)
navigator.drive_path(path)
print("Arrived at:", navigator.position)
print("Final heading:", HEADING_NAMES[navigator.heading])
```

## Teaching Notes
- **Build the class incrementally.** Write `__init__` first, test it. Add `get_needed_heading()`, test it. Then `turn_to()`, then `drive_path()`. Do not write the entire class at once.
- **Emphasize reuse.** This is a key pedagogical moment. Students built LineTrack in Module 2, used it for circles in Module 3, and now it powers grid navigation in Module 4. The Navigator class is only about 25 lines because it delegates all the hard work to LineTrack.
- **Test on desktop first.** Before running on the robot, add print statements inside each method so students can see the logic executing. Replace `self.line_track.turn_right()` with `print("Turning right")` and `self.line_track.track_until_cross()` with `print("Following line to next intersection")` for desktop testing.
- **The clearing maneuver matters.** When the robot goes straight through an intersection, it must drive forward 8 cm before calling `track_until_cross()`. Without this, the sensors immediately detect the current intersection and stop. Walk through this scenario carefully on the board so students understand why.
- **`turn_right()` is sensor-based, not angle-based.** The robot does not turn exactly 90 degrees. It drives forward, spins, and stops when it finds the next line. This means it self-corrects on every turn, which is more reliable than angle-based turning.
- **Common coding errors to watch for:**
  - Forgetting `self` in method definitions or when accessing attributes
  - Starting the loop at 0 instead of 1 in `drive_path()`
  - Forgetting to update `self.position` after line-following
  - Forgetting the intersection clearing `straight(8)` for the straight-ahead case
  - Using string headings instead of numbers
- **The Manhattan class should be provided complete.** Students should not need to rewrite it. Copy it from Lesson 5 or import it.

## Connections to Next Lessons
- **Lesson 9** (Final Project) will combine Manhattan and Navigator into a multi-destination delivery program where the robot visits a sequence of locations.
- The Navigator class becomes the execution engine that students build upon in the final project.
- Students will need to update `manhattan.position` after each leg so that the next path starts from the correct location.
