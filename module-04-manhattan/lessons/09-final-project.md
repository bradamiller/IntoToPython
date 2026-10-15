# Lesson 9: Module 4 Final Project

## Overview
Students bring together everything from Module 4 by building a complete grid-navigation program that integrates **`compute_manhattan_path()`** (path planning) and **`drive_path()`** (path execution). The final project requires the robot to visit a sequence of four or more destinations on the grid, computing a new path for each leg of the journey. Students plan their destinations, hand-trace the first leg, test incrementally, and then run the full multi-destination sequence on the XRP robot. This lesson serves as both a culminating assessment and a celebration of what students have built across the entire module.

This lesson stands on its own -- classes are never required. An **optional extension** at the end of this file shows the same final project built on the `Manhattan`/`Navigator` classes from the Lesson 5 and 8 extensions, for courses that also cover OOP.

## Learning Objectives
By the end of this lesson, students will be able to:
- Integrate `compute_manhattan_path()` and `drive_path()` into a single working program
- Write a main program that loops through a list of destinations, computing and driving each path
- Track `position` and `heading` in the main program, reassigning them from `drive_path()`'s return value after each leg
- Test incrementally: path computation alone, one leg on the robot, then the full sequence
- Debug integration issues between two functions working together
- Demonstrate a working multi-destination navigation program on the XRP robot

## Key Concepts
- **System integration**: Combining two functions (`compute_manhattan_path`, `drive_path`) that each handle one responsibility into a complete program
- **Multi-destination loop**: A `for` loop that iterates through a list of destinations, computing and driving a path to each one
- **Single source of truth**: Because `position` and `heading` live in one place -- the main program's own variables -- there's no separate "sync the position between two objects" step. `drive_path()` returns the updated values, and the very next `compute_manhattan_path()` call uses them directly.
- **Incremental testing**: Testing individual components before testing the integrated system
- **Main program structure**: The code that calls the functions and orchestrates the navigation sequence

## Materials Required
- XRP Robot with fully charged battery
- Grid mat or taped grid (at least 4x4, labeled with coordinates)
- VS Code with Python installed and XRPLib configured
- Completed `compute_manhattan_path()` function (from Lesson 5)
- Completed `drive_path()` function (from Lesson 8)
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
   - `compute_manhattan_path(position, destination)` returns a list of coordinates
   - `drive_path(path, position, heading)` turns and drives along the path, returning the new `(position, heading)`
   - "You have built both of these. Today you connect them."

3. **The Main Program Pattern**:
   - Write the pseudocode on the board:
     ```
     position = (0, 0)
     heading = 0  (North)
     destinations = [(1, 3), (3, 3), (3, 0), (0, 0)]

     For each destination:
         Compute the path from the current position
         Print the path
         Drive the path, capturing the new position and heading
     ```
   - "This is about eight lines of real code. The hard work is already inside the two functions."

4. **Project Requirements Overview**:
   - At least 4 destinations
   - Must print each path before driving it
   - Must work on the physical robot
   - Must include a planning document (worksheet)

### Guided Practice (15 minutes)
**For 50-min classes:** 12 min
**For 3-hour sessions:** 20 min

1. **Step 1: Write the Main Program Together**:
   - Start with the functions already written (from previous lessons).
   - Write the main program on the board:
     ```python
     HEADING_NAMES = ["N", "E", "S", "W"]

     position = (0, 0)
     heading = 0  # heading North

     destinations = [(2, 0), (2, 3), (0, 3), (0, 0)]

     # Print leg 1's plan BEFORE the button -- read it before the robot moves.
     print("Planned path for leg 1:", compute_manhattan_path(position, destinations[0]))
     board.wait_for_button()

     for dest in destinations:
         print("--- Navigating to", dest, "---")
         path = compute_manhattan_path(position, dest)
         print("Path:", path)
         position, heading = drive_path(path, position, heading)
         print("Arrived at:", position)
         print("Heading:", HEADING_NAMES[heading])
         print()
     ```
   - Walk through the key line: `position, heading = drive_path(path, position, heading)`. Ask: "Why do we reassign `position` and `heading` here?" Answer: `drive_path()` doesn't change anything outside itself -- it computes the new position and heading internally and returns them. If we don't capture the return value, the next loop iteration would still think the robot is at its old position. Then the print before the button: only leg 1 can be printed in advance, because every later leg is planned from wherever the previous one actually ends. Each later leg is printed as it is planned, just before the robot drives it.

2. **Step 2: Trace One Leg on Paper**:
   - Using the board, trace the first leg: `(0, 0)` to `(2, 0)`.
   - Path: `[(1, 0), (2, 0)]`
   - Starting at (0,0) heading 0 (North):
     ```
     Step 1: Position (0,0) heading 0 (N), desired 2 (S) --> (2-0)%4 = 2: two clockwise turns; track, drive past; at (1,0)
     Step 2: Position (1,0) heading 2 (S), desired 2 (S) --> (2-2)%4 = 0: no turn; track, drive past; at (2,0)
     ```
   - "After this leg, `position = (2, 0)`, `heading = 2` (S) -- both in the same two variables the main program already had."

3. **Step 3: Discuss Testing Strategy**:
   - Level 1: Test `compute_manhattan_path()` alone with print statements (no robot needed)
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

**Exercise 2: Path-Only Test**
- Students run their program with print statements only (no robot):
  ```python
  position = (0, 0)
  destinations = [(2, 0), (2, 3), (0, 3), (0, 0)]

  for dest in destinations:
      path = compute_manhattan_path(position, dest)
      print("To", dest, ":", path)
      position = dest
  ```
- Verify all paths look correct before involving the robot.

**Exercise 3: Single-Leg Robot Test**
- Test just the first leg on the physical robot.
- Place the robot at (0, 0) facing North.
- Run the program with only one destination.
- Does the robot arrive at the correct cell? Is the turn correct?

**Exercise 4: Full Sequence**
- Run the complete multi-destination program.
- Watch the robot navigate to all four destinations in sequence.
- Debug any issues (wrong turns, overshooting cells, incorrect paths).

**Exercise 5: Extension Challenges (if time permits)**
- Add a "return home" destination at the end so the robot ends where it started.
- Implement a round trip: visit all destinations and then revisit them in reverse order.
- Let the user input custom destinations from the keyboard.
- Add a pause between legs using `board.wait_for_button()`.

### Assessment

**Formative (during lesson)**:
- Can students write the main program loop without assistance?
- Do they understand why `position, heading = drive_path(...)` must reassign both variables?
- Can they trace through a multi-leg journey on paper?
- Do they test incrementally rather than trying the full program immediately?

**Summative (Final Project Rubric -- 50 points total)**:

| Category | Points | Criteria |
|---|---|---|
| **`compute_manhattan_path()`** | 10 | Function is complete and correctly computes paths for any position/destination pair. |
| **Driving functions** | 15 | `desired_heading()`, `turn_to()`, and `drive_path()` are correct. Turn logic uses a while loop to turn right until heading matches. Position and heading returned correctly. |
| **Main Program** | 10 | Defines 4+ destinations, loops through destinations computing and driving each path. Reassigns `position`/`heading` after each leg. |
| **Robot Demonstration** | 10 | Robot physically navigates to all destinations on the grid. Turns are correct. Robot arrives at each destination cell. |
| **Planning & Documentation** | 5 | Completed planning worksheet. Hand-trace of at least one leg. Testing checklist followed. |

**Grading Notes:**
- Full credit for robot demonstration requires the robot to complete the sequence without manual intervention.
- Partial credit (5/10) for robot demonstration if the robot completes at least 2 legs correctly.
- Students who cannot run on the robot (hardware issues) can earn up to 8/10 for robot demonstration by showing correct console output with print statements tracing every turn and drive.

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "I do not need to reassign `position` because `drive_path()` already changed it" | `drive_path()` only changes its own local copy of `position`. You must write `position, heading = drive_path(path, position, heading)` to capture the new values -- otherwise the main program's `position` never updates. |
| "The heading resets to North for each leg" | `heading` keeps its value from the end of the previous leg, because it's the same variable carried forward through the loop. If it finished heading 1 (East), it starts the next leg heading 1 (East). This is realistic and important for correct turn calculations. |
| "The path list includes the destination twice if I visit it again later" | Each call to `compute_manhattan_path()` generates a fresh path from the current position to the new destination. Previous paths are not stored. |
| "I need to call `drive_path()` for each step individually" | `drive_path()` already loops through all the steps internally. You call it once per leg with the full path list. |
| "Print statements slow down the robot" | Print statements execute in microseconds. They are essential for debugging and do not noticeably affect robot performance. |

## Differentiation

**For struggling students**:
- Provide `compute_manhattan_path()` and the driving functions complete; have students focus only on writing the main program loop
- Start with just 2 destinations instead of 4
- Provide the main program with one blank to fill in (the `position, heading = drive_path(...)` line)
- Pair with a partner for the robot testing phase
- Allow desktop-only testing with full print output for partial credit

**For advanced students**:
- Add obstacle avoidance: mark certain cells as blocked and modify `compute_manhattan_path()` to route around them
- Implement a delivery confirmation: robot pauses at each destination and waits for a button press before continuing
- Create a function that generates random destinations and navigates to them
- Add distance tracking: count total cells traveled and total turns made across the entire journey
- Work through the Optional Extension below and compare the two versions directly

## Materials & Code Examples

### Main Program
`code/solutions/lesson-09-final-project.py` is the complete program: the Module 2 sensor and line-tracking functions (`track_to_intersection`, `turn_clockwise`, `turn_counterclockwise`, `drive_past_intersection`), `compute_manhattan_path`, the three Lesson 8 driving functions, and the main loop above with leg 1 printed before the button. The student starter has the toolkit complete and the main loop as TODOs.

### Testing Without Robot (Desktop Version)
```python
def compute_manhattan_path(position, destination):
    path = []
    current_row, current_col = position
    dest_row, dest_col = destination
    while current_row < dest_row:
        current_row = current_row + 1
        path.append((current_row, current_col))
    while current_row > dest_row:
        current_row = current_row - 1
        path.append((current_row, current_col))
    while current_col < dest_col:
        current_col = current_col + 1
        path.append((current_row, current_col))
    while current_col > dest_col:
        current_col = current_col - 1
        path.append((current_row, current_col))
    return path

# Desktop test — no robot needed
position = (0, 0)
destinations = [(2, 0), (2, 3), (0, 3), (0, 0)]

for dest in destinations:
    path = compute_manhattan_path(position, dest)
    print("To", dest, ":", path, "  Steps:", len(path))
    position = dest
```

## Teaching Notes
- **This is a project day, not a lecture day.** Keep the introduction short. Students should spend most of their time coding and testing.
- **Encourage incremental testing.** The most common failure mode is students who write everything at once and cannot figure out what is broken. Push them to test `compute_manhattan_path()` alone first.
- **The `position, heading = drive_path(...)` reassignment is the most common bug.** Without it, every path starts from (0, 0). When students get confused paths on the second leg, check this line first.
- **Battery life matters.** Full sequences with many turns and drives can drain the battery. Have students charge between tests if needed.
- **Celebrate successes.** When a robot completes the full sequence, let the class watch. This is the payoff for nine lessons of building up to this point.
- **Common integration bugs:**
  - Forgetting to reassign `position, heading = drive_path(...)` after each leg
  - Using a different variable name for position in different parts of the program
  - Calling `compute_manhattan_path()` with the arguments swapped (destination first instead of position first)
- **Debugging tip:** "Is `turn_to()` returning `heading`?" -- If it's missing the `return`, every subsequent turn calculation will be wrong. Have students add a print statement right after `heading = turn_to(heading, needed)` to verify.
- **Time management for 50-min classes:** Students may need two class periods to complete the full project. Day 1: planning and path-only testing. Day 2: robot testing and demonstration.
- **If your course covers the Lesson 5 and 8 Optional Extensions (classes)**, note in the wrap-up that the class version removes the `position, heading = drive_path(...)` reassignment entirely: the navigator updates itself, and the planner is stateless, so there is no second copy of the position anywhere. That is the felt reason for the `Navigator` class.

## Connections to Next Lessons
- This is the final lesson of Module 4. Students now have experience with:
  - Coordinate systems and tuples
  - Lists and iteration
  - Algorithm design (Manhattan distance)
  - Functions, docstrings, and threading state through return values
  - Testing strategies
  - Hardware integration with the XRP robot
- These skills transfer directly to future modules that may involve more complex path-planning algorithms, sensor integration, or multi-robot coordination.
- The pattern of separating planning (`compute_manhattan_path`) from execution (`drive_path`) is a fundamental software architecture principle that will appear in future projects.

---

## Optional Extension: The Final Project with Classes

*For students who did the Lesson 5 and Lesson 8 Optional Extensions. Not graded; the rubric is the same.*

```python
board = Board.get_default_board()

planner = Manhattan()                      # stateless -- told the position every call
navigator = Navigator((0, 0), 0)           # owns position and heading
destinations = [(2, 0), (2, 3), (0, 3), (0, 0)]

print("Planned path for leg 1:", planner.compute_path(navigator.position, destinations[0]))
board.wait_for_button()

for dest in destinations:
    print("--- Navigating to", dest, "---")
    path = planner.compute_path(navigator.position, dest)
    print("Path:", path)
    navigator.drive_path(path)
    print("Arrived at:", navigator.position, "facing", HEADING_NAMES[navigator.heading])
```

Notice there is no `position, heading = ...` line and no sync line either. The navigator is the only thing that knows where the robot is; the planner is told `navigator.position` every call and remembers nothing (Lesson 5). An earlier version of this course had the planner store its own position, which needed `manhattan.position = navigator.position` after every leg -- the line everyone forgot. There is no longer a second copy to keep in step.

Code: `code/solutions/lesson-09-final-project-class-addon.py`.
