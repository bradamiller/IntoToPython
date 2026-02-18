# Lesson 8: Implementing the Navigator Class

## Overview
Students package the turning logic from Lesson 7 into a **Navigator class** that can drive the XRP robot along any Manhattan path. The Navigator class stores the robot's current position and heading, determines the needed direction for each step, executes the required turn using the drivetrain, and drives one grid cell forward. By the end of this lesson, students will have a complete Navigator that accepts a path from the Manhattan class and autonomously drives the robot through it, one cell at a time.

## Learning Objectives
By the end of this lesson, students will be able to:
- Design a Navigator class with appropriate attributes (`position`, `heading`, `drivetrain`) and methods
- Implement `get_needed_direction()` to convert a coordinate delta into a compass direction
- Implement `turn_to()` using right-turn and left-turn dictionaries to physically turn the robot
- Implement `drive_path()` to loop through a list of coordinates, turning and driving at each step
- Integrate the Navigator class with the Manhattan class to drive a computed path on the robot

## Key Concepts
- **Navigator class**: A class that controls the robot's movement along a path, tracking position and heading
- **`__init__(self, start, heading)`**: Constructor that sets the starting position, initial heading, and creates a drivetrain object
- **`get_needed_direction(self, next_pos)`**: Method that computes the compass direction (N/S/E/W) needed to move from the current position to the next position
- **`turn_to(self, direction)`**: Method that compares the needed direction to the current heading, calls the drivetrain to turn the appropriate amount, and updates the heading
- **`drive_path(self, path)`**: Method that loops through each coordinate in a path, calling `turn_to()` and driving forward for each step
- **Integration**: Connecting two classes (Manhattan for path planning, Navigator for path execution) so they work together as a system

## Materials Required
- XRP Robot with charged battery
- Grid mat or taped grid (at least 4x4)
- VS Code with Python installed and XRPLib configured
- Printed Navigator class design worksheet (see Materials & Code Examples)
- Whiteboard or projector for class design diagrams
- Completed turn-logic work from Lesson 7

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 8 min
**For 3-hour sessions:** 10-12 min

1. **Review: Where We Left Off**:
   - Quick recap of Lesson 7: we can determine direction from coordinate deltas and decide which turn is needed.
   - "We built functions for `get_direction()` and `decide_turn()`. Today we are packaging those into a class that actually drives the robot."

2. **Why a Class?**:
   - We already have a Manhattan class that plans the path. Now we need a Navigator class that executes the path.
   - A class bundles the robot's state (position, heading, drivetrain) with the logic (turn, drive) into one reusable object.
   - Draw on the board:
     ```
     Manhattan class           Navigator class
     ----------------          -----------------
     .position                 .position
     .compute_path()           .heading
                               .drivetrain
                               .get_needed_direction()
                               .turn_to()
                               .drive_path()
     ```

3. **The Big Picture**:
   - Manhattan computes the path: `[(0,0), (1,0), (2,0), (2,1)]`
   - Navigator drives the path: turn, drive, turn, drive, turn, drive
   - Together they form a complete grid navigation system.

4. **Preview the Goal**:
   - By the end of this lesson, you will run a program that computes a path and the robot physically drives it on the grid.

### Guided Practice (20 minutes)
**For 50-min classes:** 18 min
**For 3-hour sessions:** 30 min

1. **Step 1: Design the `__init__` Method**:
   - Ask: "What does the Navigator need to know when it is created?"
   - Starting position (a tuple like `(0, 0)`)
   - Starting heading (a string like `"N"`)
   - A drivetrain object to control the robot
   - Write on the board:
     ```python
     class Navigator:
         def __init__(self, start, heading):
             self.position = start
             self.heading = heading
             self.drivetrain = DifferentialDrive.get_default_differential_drive()
     ```
   - Explain `DifferentialDrive.get_default_differential_drive()`: this is how XRPLib gives us access to the robot's motors.

2. **Step 2: Implement `get_needed_direction()`**:
   - This is the same logic from Lesson 7, now as a method:
     ```python
     def get_needed_direction(self, next_pos):
         row_diff = next_pos[0] - self.position[0]
         col_diff = next_pos[1] - self.position[1]
         if row_diff == 1:
             return "S"
         elif row_diff == -1:
             return "N"
         elif col_diff == 1:
             return "E"
         elif col_diff == -1:
             return "W"
     ```
   - Ask: "Why does this use `self.position` instead of a `current` parameter?" Answer: The Navigator already knows its own position.

3. **Step 3: Implement `turn_to()`**:
   - This is the core of the Navigator. It must:
     1. Compare the needed direction to the current heading
     2. Call `self.drivetrain.turn()` with the right number of degrees
     3. Update `self.heading`
   - Build it together:
     ```python
     def turn_to(self, direction):
         right_turns = {"N": "E", "E": "S", "S": "W", "W": "N"}
         left_turns = {"N": "W", "W": "S", "S": "E", "E": "N"}

         if self.heading == direction:
             pass  # No turn needed
         elif right_turns[self.heading] == direction:
             self.drivetrain.turn(90)
             self.heading = direction
         elif left_turns[self.heading] == direction:
             self.drivetrain.turn(-90)
             self.heading = direction
         else:
             self.drivetrain.turn(180)
             self.heading = direction
     ```
   - Explain the degrees: positive 90 is a right turn, negative 90 is a left turn, 180 is a U-turn.
   - Ask: "Why do we always set `self.heading = direction` after turning?" Answer: After the turn, the robot is facing the needed direction no matter which turn we made.

4. **Step 4: Implement `drive_path()`**:
   - This method ties everything together:
     ```python
     def drive_path(self, path):
         for i in range(1, len(path)):
             next_pos = path[i]
             direction = self.get_needed_direction(next_pos)
             self.turn_to(direction)
             self.drivetrain.straight(20)  # 20 cm per grid cell
             self.position = next_pos
     ```
   - Key points to discuss:
     - `range(1, len(path))`: We skip index 0 because that is the starting position (the robot is already there).
     - After driving, we update `self.position` to the new cell.
     - The distance `20` should match your grid cell size. Adjust as needed.

5. **Step 5: Integration Test on Paper**:
   - Before running on the robot, trace through a short path on the board:
     ```
     Manhattan path: [(0,0), (1,0), (1,1)]
     Navigator starts at (0,0) heading N

     Step 1: next_pos = (1,0), need S, heading is N --> turn 180, drive, position = (1,0)
     Step 2: next_pos = (1,1), need E, heading is S --> turn left, drive, position = (1,1)
     ```
   - Confirm students can trace through before moving to the robot.

### Independent Practice (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 30-40 min

**Exercise 1: Complete the Navigator Class**
- Students open the starter file `lesson-08-navigator.py` and fill in the TODO sections.
- The Manhattan class is provided complete. Students focus on Navigator methods.

**Exercise 2: Desktop Testing**
- Before deploying to the robot, students test with print statements:
  ```python
  manhattan = Manhattan((0, 0))
  path = manhattan.compute_path((2, 2))
  print("Path:", path)

  nav = Navigator((0, 0), "N")
  nav.drive_path(path)
  print("Final position:", nav.position)
  print("Final heading:", nav.heading)
  ```
- Expected output should show the path and confirm the final position is (2, 2).

**Exercise 3: Robot Test (Single Leg)**
- Place the robot at (0, 0) on the grid, facing North.
- Run the program with a short path: `(0, 0)` to `(1, 1)`.
- Observe: Does the robot turn correctly? Does it end up in the right cell?
- Adjust the `straight()` distance if the robot overshoots or undershoots.

**Exercise 4: Robot Test (Longer Path)**
- Test with a longer path: `(0, 0)` to `(2, 3)`.
- Count the steps. Does the robot visit the expected cells?
- Compare the robot's physical position with the expected path printed to the console.

### Assessment

**Formative (during lesson)**:
- Can students explain what attributes the Navigator class needs and why?
- Can they trace through `drive_path()` on paper, predicting each turn and position update?
- Can they distinguish between the roles of Manhattan (path planning) and Navigator (path execution)?
- Do their implementations handle all four turn cases correctly?

**Summative (worksheet/exit ticket)**:
1. What three attributes does the Navigator class store? Explain the purpose of each.
2. If the Navigator is at (1, 2) heading East and the next position is (1, 1), what direction is needed? What turn does the robot make?
3. Why does `drive_path()` start its loop at index 1 instead of index 0?
4. Write the `turn_to()` method from memory, including the dictionary lookups and drivetrain calls.
5. Describe in your own words how Manhattan and Navigator work together to navigate the grid.

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "The Navigator should also compute the path" | The Navigator only drives the path. The Manhattan class computes the path. Separating concerns makes the code easier to understand and debug. |
| "I need to pass the current position to `get_needed_direction`" | The Navigator already knows its position through `self.position`. That is the advantage of a class -- methods can access the object's own data. |
| "The turn dictionaries should be parameters to the constructor" | The turn dictionaries are constants (they never change). Defining them inside `turn_to()` or as class-level constants is cleaner than passing them in. |
| "After turning, I need to calculate the new heading" | The new heading is always the direction you wanted to face. If you needed to go East and you turned, you are now facing East regardless of which turn you made. |
| "`drive_path()` should start at index 0" | Index 0 is where the robot already is. Driving to your current position would be a wasted step. Start at index 1 to move to the first new cell. |
| "`self.drivetrain.turn(90)` turns left" | Positive degrees (90) is a right turn, negative degrees (-90) is a left turn. This follows the standard convention where clockwise is positive. |

## Differentiation

**For struggling students**:
- Provide the `__init__` and `get_needed_direction()` methods complete; have students focus only on `turn_to()` and `drive_path()`
- Use print statements instead of drivetrain calls for initial testing (desktop mode)
- Walk through the loop in `drive_path()` one iteration at a time with the student
- Pair with a partner who completed Lesson 7 exercises successfully
- Provide a reference card with the turn dictionaries and drivetrain method signatures

**For advanced students**:
- Add a `log` attribute that records every action (turn and drive) as a list of strings
- Implement a `return_home()` method that drives the robot back to its starting position
- Add error handling: what if `get_needed_direction()` receives a diagonal move?
- Make the grid cell size configurable by passing it to the constructor
- Add a `print_status()` method that displays current position and heading after each step

## Materials & Code Examples

### Navigator Class Design Template
```
Navigator Class
===============
Attributes:
  - position:    (row, col) tuple — where the robot is now
  - heading:     "N", "S", "E", or "W" — which way the robot faces
  - drivetrain:  DifferentialDrive object — controls the motors

Methods:
  - __init__(start, heading):     Set up position, heading, and drivetrain
  - get_needed_direction(next_pos): Return "N"/"S"/"E"/"W" based on delta
  - turn_to(direction):           Turn the robot to face the given direction
  - drive_path(path):             Drive along the entire path
```

### Complete Navigator Class
```python
from XRPLib.differential_drive import DifferentialDrive

class Navigator:

    def __init__(self, start, heading):
        """Create a Navigator at the given start position and heading."""
        self.position = start
        self.heading = heading
        self.drivetrain = DifferentialDrive.get_default_differential_drive()

    def get_needed_direction(self, next_pos):
        """Determine direction (N/S/E/W) to move from current position to next_pos."""
        row_diff = next_pos[0] - self.position[0]
        col_diff = next_pos[1] - self.position[1]
        if row_diff == 1:
            return "S"
        elif row_diff == -1:
            return "N"
        elif col_diff == 1:
            return "E"
        elif col_diff == -1:
            return "W"

    def turn_to(self, direction):
        """Turn the robot to face the given direction."""
        right_turns = {"N": "E", "E": "S", "S": "W", "W": "N"}
        left_turns = {"N": "W", "W": "S", "S": "E", "E": "N"}

        if self.heading == direction:
            pass  # Already facing the right way
        elif right_turns[self.heading] == direction:
            self.drivetrain.turn(90)
            self.heading = direction
        elif left_turns[self.heading] == direction:
            self.drivetrain.turn(-90)
            self.heading = direction
        else:
            self.drivetrain.turn(180)
            self.heading = direction

    def drive_path(self, path):
        """Drive the robot along the given path."""
        for i in range(1, len(path)):
            next_pos = path[i]
            direction = self.get_needed_direction(next_pos)
            self.turn_to(direction)
            self.drivetrain.straight(20)
            self.position = next_pos
```

### Integration Example
```python
from XRPLib.differential_drive import DifferentialDrive

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
        self.heading = heading
        self.drivetrain = DifferentialDrive.get_default_differential_drive()

    def get_needed_direction(self, next_pos):
        row_diff = next_pos[0] - self.position[0]
        col_diff = next_pos[1] - self.position[1]
        if row_diff == 1:
            return "S"
        elif row_diff == -1:
            return "N"
        elif col_diff == 1:
            return "E"
        elif col_diff == -1:
            return "W"

    def turn_to(self, direction):
        right_turns = {"N": "E", "E": "S", "S": "W", "W": "N"}
        left_turns = {"N": "W", "W": "S", "S": "E", "E": "N"}
        if self.heading == direction:
            pass
        elif right_turns[self.heading] == direction:
            self.drivetrain.turn(90)
            self.heading = direction
        elif left_turns[self.heading] == direction:
            self.drivetrain.turn(-90)
            self.heading = direction
        else:
            self.drivetrain.turn(180)
            self.heading = direction

    def drive_path(self, path):
        for i in range(1, len(path)):
            next_pos = path[i]
            direction = self.get_needed_direction(next_pos)
            self.turn_to(direction)
            self.drivetrain.straight(20)
            self.position = next_pos

# ===== Main Program =====
manhattan = Manhattan((0, 0))
navigator = Navigator((0, 0), "N")

destination = (2, 3)
path = manhattan.compute_path(destination)
print("Path to", destination, ":", path)
navigator.drive_path(path)
print("Arrived at:", navigator.position)
print("Final heading:", navigator.heading)
```

## Teaching Notes
- **Build the class incrementally.** Write `__init__` first, test it. Add `get_needed_direction()`, test it. Then `turn_to()`, then `drive_path()`. Do not write the entire class at once.
- **Test on desktop first.** Before running on the robot, add print statements inside each method so students can see the logic executing. Replace `self.drivetrain.turn(90)` with `print("Turning right 90")` for desktop testing.
- **Grid cell size matters.** The `straight(20)` call assumes 20 cm grid cells. Measure your actual grid and adjust. If cells are 15 cm, use `straight(15)`.
- **The robot will not turn perfectly.** Real turns may be off by a few degrees. This is normal. Students should expect small errors and understand that calibration is part of robotics.
- **Common coding errors to watch for:**
  - Forgetting `self` in method definitions or when accessing attributes
  - Starting the loop at 0 instead of 1 in `drive_path()`
  - Forgetting to update `self.position` after driving
  - Confusing positive and negative degrees in `turn()`
- **The Manhattan class should be provided complete.** Students should not need to rewrite it. Copy it from Lesson 5 or import it.

## Connections to Next Lessons
- **Lesson 9** (Final Project) will combine Manhattan and Navigator into a multi-destination delivery program where the robot visits a sequence of locations.
- The Navigator class becomes the execution engine that students build upon in the final project.
- Students will need to update `manhattan.position` after each leg so that the next path starts from the correct location.
