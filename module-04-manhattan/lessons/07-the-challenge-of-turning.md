# Lesson 7: The Challenge of Turning

## Overview
Students confront the problem that their robot has a **heading** -- a direction it is currently facing -- and that moving to the next grid coordinate may require turning first. This lesson introduces two core insights: (1) between adjacent grid intersections, either the row OR the column changes but never both, giving exactly 4 cases that map to the 4 compass directions; and (2) representing heading as a number 0-3 lets us turn by simply adding 1 and wrapping 4 back to 0. Students design three methods on paper: `desired_heading` (which of the 4 cases is this step?), `turn_to` (a while loop that turns right until heading matches desired), and `drive_path` (for each intersection in the path, turn and drive forward one). Code implementation comes in Lesson 8.

## Learning Objectives
By the end of this lesson, students will be able to:
- Explain why only the row OR column changes between adjacent intersections (4 cases, 4 directions)
- Represent heading as a number: 0=N, 1=E, 2=S, 3=W
- Write `desired_heading(current, next_pos)` that returns 0, 1, 2, or 3 based on which coordinate changed
- Trace the `turn_to` while loop on paper, showing each value of `heading` as it updates and wraps 4 back to 0
- Describe how `drive_path` uses `desired_heading` and `turn_to` to move through a list of intersections

## Key Concepts
- **One change at a time**: Between two adjacent grid intersections, either the row changes by ±1 or the column changes by ±1, never both. Four cases total, each corresponding to one of the 4 compass directions.
- **Heading as a number**: The robot's current facing direction stored as 0 (North), 1 (East), 2 (South), or 3 (West). `HEADING_NAMES = ["N", "E", "S", "W"]` converts back to letters for display.
- **Desired heading**: The heading number needed to move from the current intersection to the next one. Derived from whether the row or column changed and in which direction.
- **Turn by adding 1**: Each right turn adds 1 to the heading. When heading reaches 4, reset to 0. This wrap is the entire mechanism of the `turn_to` while loop.
- **The three methods**: `desired_heading(current, next_pos)` picks the case. `turn_to(desired)` runs a while loop that turns right and increments heading until it matches. `drive_path(path)` ties them together, calling both for every intersection in the list.

## Materials Required
- XRP Robot (for demonstration only in this lesson)
- Grid mat or taped grid from previous lessons
- Printed turn-logic worksheet (see Materials & Code Examples)
- Whiteboard or projector for diagrams
- VS Code with Python installed and XRPLib configured
- Compass rose diagram handout (N/E/S/W with numbers 0-3)

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 8 min
**For 3-hour sessions:** 10-12 min

1. **Hook: The Robot That Went Sideways**:
   - Place the robot on the grid facing East.
   - Ask: "If I want the robot to go to the cell directly below it (South), can I just drive forward?"
   - Let students observe: driving forward moves East, not South. The robot needs to turn first.
   - "This is the problem we are solving today. The robot knows WHERE it needs to go, but it also needs to figure out HOW to face the right direction."

2. **The Key Observation — One Change at a Time**:
   - Draw two adjacent intersections on the board and ask: "What can change between them?"
   - Establish: between adjacent intersections, either the row OR the column changes — never both.
   - That gives exactly 4 cases, one for each compass direction:
     ```
     row goes down (+1)  -->  South
     row goes up   (-1)  -->  North
     col goes up   (+1)  -->  East
     col goes down (-1)  -->  West
     ```
   - "Four cases, four directions. That is the whole puzzle."

3. **Introduce the Concept of Heading**:
   - Draw a compass rose on the board: N at top, E at right, S at bottom, W at left.
   - Write heading numbers clockwise: 0 at top, 1 at right, 2 at bottom, 3 at left.
   - "Heading is the direction the robot is currently facing, stored as a number 0-3."
   - Physical demonstration: Place the robot on the grid. Announce its heading number. Rotate it right and ask students to call out the new heading number.
   - "Why numbers? Because each right turn adds 1. When we hit 4, we wrap back to 0. That is all the turn logic we need."

4. **Why This Matters**:
   - Without turn logic, the robot can only go in one direction.
   - Real robots (cars, drones, rovers) all track heading.
   - This is the bridge between the path-planning algorithm and actual robot movement.

### Guided Practice (20 minutes)
**For 50-min classes:** 18 min
**For 3-hour sessions:** 25 min

1. **Method 1 — `desired_heading` from Coordinate Change**:
   - Draw a small grid on the board with row/column labels:
     ```
           Col 0   Col 1   Col 2
     Row 0  (0,0)   (0,1)   (0,2)
     Row 1  (1,0)   (1,1)   (1,2)
     Row 2  (2,0)   (2,1)   (2,2)
     ```
   - Work through examples, highlighting "what changed?":
     - From (0,0) to (1,0): row went +1 --> heading **2** (South)
     - From (1,0) to (0,0): row went -1 --> heading **0** (North)
     - From (0,0) to (0,1): col went +1 --> heading **1** (East)
     - From (0,1) to (0,0): col went -1 --> heading **3** (West)
   - Write the method on the board:
     ```python
     def desired_heading(current, next_pos):
         row_diff = next_pos[0] - current[0]
         col_diff = next_pos[1] - current[1]
         if row_diff == -1: return 0   # North
         if col_diff ==  1: return 1   # East
         if row_diff ==  1: return 2   # South
         if col_diff == -1: return 3   # West
     ```
   - Ask students to verify: "Why does row +1 mean South?" Answer: In our grid, row 0 is at the top, like a spreadsheet. Going down increases the row. Down is South.

2. **Method 2 — `turn_to` with a While Loop**:
   - Ask: "If I am heading 0 (North) and I turn right once, what is my new heading?" (1.) "Turn right again?" (2.) "Again?" (3.) "Again?" (0 — it wraps!)
   - Physical check: Have students stand facing the front (heading 0, North) and turn right. Call out the heading at each turn: 1, 2, 3, 0.
   - "Here is the idea: keep turning right — adding 1 each time, wrapping 4 back to 0 — until the heading matches what we want. We do not count ahead of time. We just turn until we are aligned."
   - Write the method on the board:
     ```python
     def turn_to(self, desired):
         while self.heading != desired:
             self.robot.turn_right()
             self.heading = self.heading + 1
             if self.heading == 4:
                 self.heading = 0
     ```
   - Trace it for several cases by walking through the while loop line by line:
     - Start heading 0 (N), desired 2 (S): loop runs — turn, heading=1; turn, heading=2; stop. Two right turns.
     - Start heading 2 (S), desired 1 (E): loop runs — turn, heading=3; turn, heading=4, wrap to 0; turn, heading=1; stop. Three right turns (wrap triggered!).
     - Start heading 1 (E), desired 1 (E): loop condition false immediately. Zero turns.
   - Emphasize: "The while loop handles every case — 0, 1, 2, or 3 turns. You do not need to count ahead. The wrap from 4 to 0 is what makes 'turn right to go from West to North' just work."

3. **Method 3 — `drive_path` for a List of Intersections**:
   - Once we have `desired_heading` and `turn_to`, driving a whole path is short:
     ```python
     def drive_path(self, path):
         for next_pos in path:
             desired = self.desired_heading(next_pos)
             self.turn_to(desired)
             self.robot.drive_forward_one()
             self.position = next_pos
     ```
   - "For every intersection in the path: figure out which way to face, turn until you face it, drive forward one intersection, update position. Repeat."
   - Note: `self.position` must be updated after each step so the next call to `desired_heading` works correctly.

4. **Tracing a Full Path**:
   - Example path: `[(1,0), (2,0), (2,1), (2,2)]`, starting position `(0,0)`, starting heading 0 (N).
   - Trace on the board, showing each value of `self.heading` as `turn_to` runs:
     ```
     At (0,0) heading 0(N), next (1,0): row+1 --> desired 2(S).  turn_to: 0->1->2. Drive to (1,0).
     At (1,0) heading 2(S), next (2,0): row+1 --> desired 2(S).  turn_to: already 2. Drive to (2,0).
     At (2,0) heading 2(S), next (2,1): col+1 --> desired 1(E).  turn_to: 2->3->0(wrap)->1. Drive to (2,1).
     At (2,1) heading 1(E), next (2,2): col+1 --> desired 1(E).  turn_to: already 1. Drive to (2,2).
     ```
   - Have students call out each step before you write it.
   - Point out step 3 — the wrap from 3 to 0 (via heading=4) happens inside `turn_to`, and students can see it.

### Independent Practice (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

**Exercise 1: Desired Heading from Coordinate Change (Paper)**
- Given the following pairs of coordinates, say what changed and write the desired heading number and letter:
  1. From (3,2) to (4,2) --> ___ changed, desired ___ (___)
  2. From (1,5) to (0,5) --> ___ changed, desired ___ (___)
  3. From (2,3) to (2,4) --> ___ changed, desired ___ (___)
  4. From (4,1) to (4,0) --> ___ changed, desired ___ (___)
  5. From (0,0) to (1,0) --> ___ changed, desired ___ (___)
- Answers: row+1/2(S); row-1/0(N); col+1/1(E); col-1/3(W); row+1/2(S)

**Exercise 2: Trace `turn_to` on Paper**
- For each scenario, list the value of `self.heading` after each pass through the while loop, until the loop stops:
  1. Current 0(N), desired 1(E) --> heading values: ___
  2. Current 1(E), desired 1(E) --> heading values: ___
  3. Current 2(S), desired 0(N) --> heading values: ___
  4. Current 3(W), desired 2(S) --> heading values: ___
  5. Current 1(E), desired 0(N) --> heading values: ___
  6. Current 3(W), desired 1(E) --> heading values: ___
  7. Current 2(S), desired 3(W) --> heading values: ___
  8. Current 0(N), desired 3(W) --> heading values: ___
- Answers: 1; (already); 3,0; 0(wrap),1,2; 2,3,0; 0(wrap),1; 3; 1,2,3

**Exercise 3: Full Path Trace (Paper)**
- Path: `[(0,1), (0,2), (1,2), (2,2), (2,1), (2,0)]`
- Starting position: `(0,0)`, Starting heading: 1 (E)
- For each step, write: position, heading, next position, what changed, desired heading, heading values as `turn_to` runs, final heading after drive.
- Expected trace:
  ```
  At (0,0) heading 1(E), next (0,1): col+1 --> desired 1(E). turn_to: already 1. Drive. Heading 1(E).
  At (0,1) heading 1(E), next (0,2): col+1 --> desired 1(E). turn_to: already 1. Drive. Heading 1(E).
  At (0,2) heading 1(E), next (1,2): row+1 --> desired 2(S). turn_to: 2. Drive. Heading 2(S).
  At (1,2) heading 2(S), next (2,2): row+1 --> desired 2(S). turn_to: already 2. Drive. Heading 2(S).
  At (2,2) heading 2(S), next (2,1): col-1 --> desired 3(W). turn_to: 3. Drive. Heading 3(W).
  At (2,1) heading 3(W), next (2,0): col-1 --> desired 3(W). turn_to: already 3. Drive. Heading 3(W).
  ```

**Exercise 4: Trace a Path on Paper**
- Path: `[(0,1), (1,1), (2,1), (2,0)]`
- Starting position: `(0,0)`, Starting heading: 0 (N)
- For each step, write: position, heading, next position, what changed, desired, heading values through the while loop, final heading.

### Assessment

**Formative (during lesson)**:
- Can students identify which coordinate changed (row or column) between two adjacent intersections?
- Can they map each of the 4 cases to the correct compass direction?
- Can they trace the `turn_to` while loop step by step, showing each value of `self.heading` including the wrap from 4 back to 0?
- Can they trace a multi-step path calling `desired_heading`, `turn_to`, and drive in sequence?

**Summative (worksheet/exit ticket)**:
1. Between two adjacent intersections, what can change? How many total cases are there?
2. If the robot is at (3,1) and needs to go to (3,2), what changed? What is the desired heading number and letter?
3. Write out the while loop in `turn_to` from memory.
4. If the robot is heading 3 (W) and desired is 1 (E), list the values of `self.heading` after each loop iteration until the loop stops.
5. Why does `turn_to` need the line `if self.heading == 4: self.heading = 0`? Give a scenario where it matters.
6. Trace through path `[(2,1), (2,2)]` with starting position `(1,1)` and starting heading 2 (S).

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "North means up on the screen, so row should decrease" | This is correct! Row 0 is at the top. Moving North (up) decreases the row number. Students sometimes second-guess themselves on this. |
| "Right and left depend on which way I'm looking at the grid" | Right and left are relative to the robot's heading, not the viewer. The while loop works with heading numbers, so spatial reasoning is not needed once the numbers are right. |
| "What if the heading goes past 3?" | It wraps back to 0. The code checks: `if self.heading == 4: self.heading = 0`. This is the only tricky line in the whole method. |
| "Wouldn't it be faster to count turns ahead of time and loop that many times?" | It would be roughly the same amount of code, but the while loop is simpler because it stops when aligned — no separate calculation needed. Trust the loop. |
| "The heading numbers seem arbitrary" | They follow a consistent clockwise pattern: 0=N, 1=E, 2=S, 3=W. Each right turn adds 1. That consistency is what makes the wrap-around math work. |
| "Row +1 means North because numbers go up" | Numbers going up means the row index increases, which means moving DOWN on the grid. Down is South. This is the most common confusion. |
| "I need separate logic for right, left, and 180" | The while loop handles all four cases (0, 1, 2, 3 turns) with the same code. No special cases. |

## Differentiation

**For struggling students**:
- Provide a printed compass rose with numbers 0, 1, 2, 3 they can physically rotate.
- Start with only two directions (0=North and 2=South) before adding East and West.
- Use a physical robot on the grid: point it in a direction, physically turn right once at a time and call out each new heading number (including the wrap from 3 back to 0).
- Pair with a stronger student for the path-tracing exercise.
- For `turn_to` tracing, let students draw the compass and physically step around it to verify.

**For advanced students**:
- Ask: "How would you modify `turn_to` to use left turns instead?" (subtract 1, wrap 0 back to 3 — i.e., `if self.heading == -1: self.heading = 3`).
- Could you extend this to 8 directions (adding NE, NW, SE, SW) by wrapping at 8 instead of 4? What else would `desired_heading` need to detect?
- Write a visual path tracer that prints the grid with arrows showing the robot's heading at each step.
- Prove: for any starting and desired heading, the while loop always terminates in at most 3 iterations.

## Materials & Code Examples

### Heading Reference
```python
# Headings as numbers (clockwise from North)
# 0 = North, 1 = East, 2 = South, 3 = West

HEADING_NAMES = ["N", "E", "S", "W"]
```

### `desired_heading` Reference
```python
def desired_heading(current, next_pos):
    row_diff = next_pos[0] - current[0]
    col_diff = next_pos[1] - current[1]
    if row_diff == -1: return 0   # North
    if col_diff ==  1: return 1   # East
    if row_diff ==  1: return 2   # South
    if col_diff == -1: return 3   # West
```

### Path Tracing Example (Lesson 7 code — no robot yet)
```python
HEADING_NAMES = ["N", "E", "S", "W"]

def desired_heading(current, next_pos):
    row_diff = next_pos[0] - current[0]
    col_diff = next_pos[1] - current[1]
    if row_diff == -1: return 0
    if col_diff ==  1: return 1
    if row_diff ==  1: return 2
    if col_diff == -1: return 3

path = [(1,0), (2,0), (2,1), (2,2)]
position = (0,0)
heading = 0

for next_pos in path:
    desired = desired_heading(position, next_pos)
    print(f"At {position} heading {HEADING_NAMES[heading]}, desired {HEADING_NAMES[desired]}")
    # Simulate turn_to: turn right until heading matches
    while heading != desired:
        heading = heading + 1
        if heading == 4:
            heading = 0
        print(f"  ... turned right, heading now {HEADING_NAMES[heading]}")
    print(f"  Drive to {next_pos}")
    position = next_pos
```

### Turn Logic Worksheet
```
Name: ________________________  Date: ______________

HEADING REFERENCE: 0=North, 1=East, 2=South, 3=West
TURN MECHANIC: Each right turn adds 1. If heading reaches 4, wrap to 0.

PART A: Desired Heading from Coordinate Change
For each pair, name what changed and the desired heading:

1. (2,3) to (3,3) --> ___ changed, desired ___ (___)
2. (4,1) to (3,1) --> ___ changed, desired ___ (___)
3. (1,0) to (1,1) --> ___ changed, desired ___ (___)
4. (0,4) to (0,3) --> ___ changed, desired ___ (___)
5. (5,2) to (6,2) --> ___ changed, desired ___ (___)
6. (3,3) to (3,4) --> ___ changed, desired ___ (___)

PART B: Trace `turn_to` — list heading values after each loop iteration
1. Current 0(N), desired 2(S) --> heading values: ___
2. Current 1(E), desired 2(S) --> heading values: ___
3. Current 3(W), desired 3(W) --> heading values: ___
4. Current 2(S), desired 1(E) --> heading values: ___ (wrap!)
5. Current 0(N), desired 3(W) --> heading values: ___
6. Current 1(E), desired 0(N) --> heading values: ___ (wrap!)

PART C: Full Path Trace
Path: [(1,2), (1,3), (2,3), (3,3), (3,2)]
Starting position: (1,1), Starting heading: 1 (E)

Step 1: (1,1) heading ___, next (1,2): ___ changed, desired ___, turn_to values ___, drive to (1,2)
Step 2: (1,2) heading ___, next (1,3): ___ changed, desired ___, turn_to values ___, drive to (1,3)
Step 3: (1,3) heading ___, next (2,3): ___ changed, desired ___, turn_to values ___, drive to (2,3)
Step 4: (2,3) heading ___, next (3,3): ___ changed, desired ___, turn_to values ___, drive to (3,3)
Step 5: (3,3) heading ___, next (3,2): ___ changed, desired ___, turn_to values ___, drive to (3,2)
```

## Teaching Notes
- **This lesson is intentionally paper-heavy.** Students need to trace the while loop by hand before they code it. Rushing to code without understanding `turn_to` leads to frustrating debugging.
- **The grid orientation is confusing.** Row 0 at the top (like a spreadsheet) means "down is South and increasing rows." Repeat this several times. Draw it. Point at it. Quiz them on it.
- **Physical movement helps.** Have students stand up, face the front (heading 0), and turn right one step at a time, calling out each new heading including the wrap from 3 to 0. This kinesthetic exercise cements the mechanic.
- **Trace the loop, do not count ahead.** Students may want to figure out the number of turns in their heads. That is fine, but make sure they can also walk through the while loop one iteration at a time — because that is what the code does, and it is what they will debug in Lesson 8.
- **The wrap from 4 to 0 is the only tricky line.** Use the odometer analogy: "9, 10 — no, wait, 0. The odometer wraps." Once students get this, everything else is mechanical.
- **Connect to the physical robot.** On the actual robot, each loop iteration calls `turn_right()` from Module 2 — the sensor-based turn that drives forward briefly then spins right until it finds the outbound line. This connection will be made concrete in Lesson 8.
- **Why only right turns?** One turn primitive keeps the code simple: one method, one loop, no special cases. The robot does not care whether 270 degrees right or 90 degrees left is "faster" — both get it to the same heading. Simplicity wins.

## Connections to Next Lessons
- **Lesson 8** will implement the `Navigator` class with `desired_heading`, `turn_to`, and `drive_path` as methods — translating the paper design directly into Python.
- **Lesson 9** (Final Project) will combine the `Manhattan` class and `Navigator` class to drive through a list of destinations.
- The three methods and the while-loop turning mechanic introduced here become the foundation for the Navigator class. Students already understand the logic; Lesson 8 just puts it into code.
