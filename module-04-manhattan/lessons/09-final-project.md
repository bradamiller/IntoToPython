# Lesson 9: Module 4 Final Project

## Overview
Students bring together everything from Module 4 by building a complete grid-navigation program that integrates the **Manhattan** class (path planning) and the **Navigator** class (path execution). The final project requires the robot to visit a sequence of four or more destinations on the grid, computing a new path for each leg of the journey. Students plan their destinations, hand-trace the first leg, test incrementally, and then run the full multi-destination sequence on the XRP robot. This lesson serves as both a culminating assessment and a celebration of what students have built across the entire module.

## Learning Objectives
By the end of this lesson, students will be able to:
- Integrate the Manhattan and Navigator classes into a single working program
- Write a main program that loops through a list of destinations, computing and driving each path
- Update `manhattan.position` after each leg so the next path starts from the correct location
- Test incrementally: Manhattan alone, one leg on the robot, then the full sequence
- Debug integration issues between two classes working together
- Demonstrate a working multi-destination navigation program on the XRP robot

## Key Concepts
- **System integration**: Combining two classes (Manhattan and Navigator) that each handle one responsibility into a complete program
- **Multi-destination loop**: A `for` loop that iterates through a list of destinations, computing and driving a path to each one
- **State synchronization**: Keeping `manhattan.position` and `navigator.position` consistent after each leg of the journey
- **Incremental testing**: Testing individual components before testing the integrated system
- **Main program structure**: The code outside the classes that creates objects and orchestrates the navigation sequence

## Materials Required
- XRP Robot with fully charged battery
- Grid mat or taped grid (at least 4x4, labeled with coordinates)
- VS Code with Python installed and XRPLib configured
- Completed Manhattan class (from Lesson 5)
- Completed Navigator class (from Lesson 8)
- Final project planning worksheet
- Printed grading rubric (see Assessment section)
- Markers or small objects to mark destination cells on the grid

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 8 min
**For 3-hour sessions:** 10-12 min

1. **The Mission Briefing**:
   - "Your robot is a delivery drone on a city grid. It starts at its home base and must visit a series of locations to make deliveries. It needs to compute the shortest path to each destination, drive there, and then continue to the next destination."
   - Show the grid with four marked destinations. "Your robot must visit all of these in order."

2. **Review the Building Blocks**:
   - Manhattan class: `compute_path(destination)` returns a list of coordinates
   - Navigator class: `drive_path(path)` turns and drives along the path
   - "You have built both of these. Today you connect them."

3. **The Main Program Pattern**:
   - Write the pseudocode on the board:
     ```
     Create Manhattan at (0, 0)
     Create Navigator at (0, 0) heading North
     destinations = [(1, 3), (3, 3), (3, 0), (0, 0)]

     For each destination:
         Compute the path from current position
         Print the path
         Drive the path
         Update Manhattan's position
     ```
   - "This is about ten lines of real code. The hard work is already inside the classes."

4. **Project Requirements Overview**:
   - At least 4 destinations
   - Must print each path before driving it
   - Must work on the physical robot
   - Must include a planning document (worksheet)

### Guided Practice (15 minutes)
**For 50-min classes:** 12 min
**For 3-hour sessions:** 20 min

1. **Step 1: Write the Main Program Together**:
   - Start with the classes already written (from previous lessons).
   - Write the main program on the board:
     ```python
     manhattan = Manhattan((0, 0))
     navigator = Navigator((0, 0), "N")

     destinations = [(2, 0), (2, 3), (0, 3), (0, 0)]

     for dest in destinations:
         print("--- Navigating to", dest, "---")
         path = manhattan.compute_path(dest)
         print("Path:", path)
         navigator.drive_path(path)
         manhattan.position = navigator.position
         print("Arrived at:", navigator.position)
         print()
     ```
   - Walk through the key line: `manhattan.position = navigator.position`. Ask: "Why is this line necessary?" Answer: After the Navigator drives to the destination, the Manhattan class needs to know the new starting position for the next `compute_path()` call.

2. **Step 2: Trace One Leg on Paper**:
   - Using the board, trace the first leg: `(0, 0)` to `(2, 0)`.
   - Path: `[(0, 0), (1, 0), (2, 0)]`
   - Navigator starts heading N:
     ```
     Step 1: At (0,0) heading N, need S --> turn 180, drive to (1,0)
     Step 2: At (1,0) heading S, need S --> no turn, drive to (2,0)
     ```
   - "After this leg, manhattan.position = (2, 0), navigator.position = (2, 0), navigator.heading = S."

3. **Step 3: Discuss Testing Strategy**:
   - Level 1: Test Manhattan alone with print statements (no robot needed)
   - Level 2: Test one leg on the robot (short path, easy to verify)
   - Level 3: Test the full sequence
   - "Do NOT skip to level 3. If something is wrong, you need to know which piece is broken."

### Independent Practice (25 minutes)
**For 50-min classes:** 20 min
**For 3-hour sessions:** 60-90 min

**Exercise 1: Complete the Planning Worksheet**
- Students fill in the project planning worksheet:
  - Choose 4+ destinations on the 4x4 grid
  - Draw the expected path for each leg
  - Hand-trace the first leg including all turns
  - Write the testing checklist

**Exercise 2: Manhattan-Only Test**
- Students run their program with print statements only (no robot):
  ```python
  manhattan = Manhattan((0, 0))
  destinations = [(2, 0), (2, 3), (0, 3), (0, 0)]

  for dest in destinations:
      path = manhattan.compute_path(dest)
      print("To", dest, ":", path)
      manhattan.position = dest
  ```
- Verify all paths look correct before involving the robot.

**Exercise 3: Single-Leg Robot Test**
- Test just the first leg on the physical robot.
- Place the robot at (0, 0) facing North.
- Run the program with only one destination.
- Does the robot arrive at the correct cell? Is the turn correct?
- Adjust `straight()` distance if needed.

**Exercise 4: Full Sequence**
- Run the complete multi-destination program.
- Watch the robot navigate to all four destinations in sequence.
- Debug any issues (wrong turns, overshooting cells, incorrect paths).

**Exercise 5: Extension Challenges (if time permits)**
- Add a "return home" destination at the end so the robot ends where it started.
- Implement a round trip: visit all destinations and then revisit them in reverse order.
- Let the user input custom destinations from the keyboard.
- Add a pause between legs using `Board.wait_for_button()`.

### Assessment

**Formative (during lesson)**:
- Can students write the main program loop without assistance?
- Do they understand why `manhattan.position` must be updated after each leg?
- Can they trace through a multi-leg journey on paper?
- Do they test incrementally rather than trying the full program immediately?

**Summative (Final Project Rubric -- 50 points total)**:

| Category | Points | Criteria |
|---|---|---|
| **Manhattan Class** | 10 | Class is complete and correctly computes paths. `compute_path()` returns correct coordinate lists for any start/destination pair. |
| **Navigator Class** | 15 | Class has correct `__init__`, `get_needed_direction()`, `turn_to()`, and `drive_path()` methods. All four turn cases handled. Position and heading updated correctly. |
| **Main Program** | 10 | Creates both objects, defines 4+ destinations, loops through destinations computing and driving each path. Updates `manhattan.position` after each leg. |
| **Robot Demonstration** | 10 | Robot physically navigates to all destinations on the grid. Turns are correct. Robot arrives at each destination cell. |
| **Planning & Documentation** | 5 | Completed planning worksheet. Hand-trace of at least one leg. Testing checklist followed. |

**Grading Notes:**
- Full credit for robot demonstration requires the robot to complete the sequence without manual intervention.
- Partial credit (5/10) for robot demonstration if the robot completes at least 2 legs correctly.
- Students who cannot run on the robot (hardware issues) can earn up to 8/10 for robot demonstration by showing correct console output with print statements tracing every turn and drive.

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "I do not need to update `manhattan.position` because Manhattan already knows where I am" | Manhattan does not automatically know the robot moved. You must explicitly set `manhattan.position = navigator.position` (or `manhattan.position = dest`) after each leg. |
| "The Navigator's heading resets to North for each leg" | The Navigator keeps its heading from the end of the previous leg. If it finished heading East, it starts the next leg heading East. This is realistic and important for correct turn calculations. |
| "I should create new Manhattan and Navigator objects for each destination" | Create them once and reuse them. The whole point of classes is that they maintain state across multiple operations. |
| "The path list includes the destination twice if I visit it again later" | Each call to `compute_path()` generates a fresh path from the current position to the new destination. Previous paths are not stored. |
| "I need to call `navigator.drive_path()` for each step individually" | `drive_path()` already loops through all the steps internally. You call it once per leg with the full path list. |
| "Print statements slow down the robot" | Print statements execute in microseconds. They are essential for debugging and do not noticeably affect robot performance. |

## Differentiation

**For struggling students**:
- Provide the complete Manhattan and Navigator classes; have students focus only on writing the main program loop
- Start with just 2 destinations instead of 4
- Provide the main program with one blank to fill in (the `manhattan.position` update line)
- Pair with a partner for the robot testing phase
- Allow desktop-only testing with full print output for partial credit

**For advanced students**:
- Add obstacle avoidance: mark certain cells as blocked and modify Manhattan to route around them
- Implement a delivery confirmation: robot pauses at each destination and waits for a button press before continuing
- Create a function that generates random destinations and navigates to them
- Add distance tracking: count total cells traveled and total turns made across the entire journey
- Implement a shortest-path optimizer that reorders destinations to minimize total travel distance

## Materials & Code Examples

### Main Program Template
```python
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board


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
board = Board.get_default_board()

manhattan = Manhattan((0, 0))
navigator = Navigator((0, 0), "N")

destinations = [(2, 0), (2, 3), (0, 3), (0, 0)]

print("=== XRP Grid Navigation ===")
print("Starting at:", manhattan.position)
print("Destinations:", destinations)
print()

board.wait_for_button()

for dest in destinations:
    print("--- Navigating to", dest, "---")
    path = manhattan.compute_path(dest)
    print("Path:", path)
    print("Steps:", len(path) - 1)
    navigator.drive_path(path)
    manhattan.position = navigator.position
    print("Arrived at:", navigator.position)
    print("Heading:", navigator.heading)
    print()

print("=== All destinations reached! ===")
print("Final position:", navigator.position)
```

### Testing Without Robot (Desktop Version)
```python
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

# Desktop test — no robot needed
manhattan = Manhattan((0, 0))
destinations = [(2, 0), (2, 3), (0, 3), (0, 0)]

for dest in destinations:
    path = manhattan.compute_path(dest)
    print("To", dest, ":", path, "  Steps:", len(path) - 1)
    manhattan.position = dest
```

## Teaching Notes
- **This is a project day, not a lecture day.** Keep the introduction short. Students should spend most of their time coding and testing.
- **Encourage incremental testing.** The most common failure mode is students who write everything at once and cannot figure out what is broken. Push them to test Manhattan alone first.
- **The `manhattan.position` update is the most common bug.** Without it, every path starts from (0, 0). When students get confused paths on the second leg, check this line first.
- **Battery life matters.** Full sequences with many turns and drives can drain the battery. Have students charge between tests if needed.
- **Celebrate successes.** When a robot completes the full sequence, let the class watch. This is the payoff for nine lessons of building up to this point.
- **Common integration bugs:**
  - Forgetting to update `manhattan.position` after each leg
  - Using a different variable name for the Manhattan and Navigator starting positions
  - Having the Navigator start at `(0, 0)` but Manhattan start somewhere else
  - Calling `compute_path()` with a position instead of a destination
- **Time management for 50-min classes:** Students may need two class periods to complete the full project. Day 1: planning and Manhattan-only testing. Day 2: robot testing and demonstration.

## Connections to Next Lessons
- This is the final lesson of Module 4. Students now have experience with:
  - Coordinate systems and tuples
  - Lists and iteration
  - Algorithm design (Manhattan distance)
  - Classes and objects (Manhattan, Navigator)
  - Testing strategies
  - Hardware integration with the XRP robot
- These skills transfer directly to future modules that may involve more complex path-planning algorithms, sensor integration, or multi-robot coordination.
- The pattern of separating planning (Manhattan) from execution (Navigator) is a fundamental software architecture principle that will appear in future projects.
