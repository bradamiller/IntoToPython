# Lesson 7: The Challenge of Turning

## Overview
Students confront the problem that their robot has a **heading** -- a direction it is currently facing -- and that moving to the next grid coordinate may require turning first. This lesson introduces the concept of robot heading as a number (0=North, 1=East, 2=South, 3=West), shows how to determine the required heading from a coordinate change, and develops a counting approach to figure out how many right turns are needed. Students work through paper exercises with diagrams, counting clockwise steps on the compass to determine right turns -- no code function needed for counting. The `get_needed_heading()` function is introduced in code; the actual turning code (a while loop) will be implemented in the Navigator class in Lesson 8.

## Learning Objectives
By the end of this lesson, students will be able to:
- Define "heading" and explain why it matters for grid navigation
- Explain why representing headings as numbers (0-3) is more useful than strings
- Determine the required heading number from a coordinate delta (row and column changes)
- Count right turns by stepping clockwise from current to needed heading
- Trace through a sequence of path coordinates on paper and list the right-turn counts required

## Key Concepts
- **Heading**: The compass direction the robot is currently facing, represented as a number: 0=North, 1=East, 2=South, 3=West
- **Heading names**: A helper list `["N", "E", "S", "W"]` converts heading numbers to letters for display
- **Coordinate delta**: The difference between the next position and the current position in row and column
- **Heading from delta**: Row increases means heading 2 (South); row decreases means heading 0 (North); column increases means heading 1 (East); column decreases means heading 3 (West)
- **Counting right turns**: Headings go clockwise 0->1->2->3->0. To find how many right turns are needed, keep stepping one turn to the right (adding 1, wrapping from 3 back to 0) until the heading matches the needed heading. Count the steps. The answer is always 0, 1, 2, or 3.
- **Wrap-around**: After heading 3 (West), the next right turn wraps back to heading 0 (North), like an odometer rolling over from 9 to 0

## Materials Required
- XRP Robot (for demonstration only in this lesson)
- Grid mat or taped grid from previous lessons
- Printed turn-logic worksheet (see Materials & Code Examples)
- Whiteboard or projector for diagrams
- VS Code with Python installed and XRPLib configured
- Compass rose diagram handout (N/S/E/W with numbers 0-3)

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 8 min
**For 3-hour sessions:** 10-12 min

1. **Hook: The Robot That Went Sideways**:
   - Place the robot on the grid facing East.
   - Ask: "If I want the robot to go to the cell directly below it (South), can I just drive forward?"
   - Let students observe: driving forward moves East, not South. The robot needs to turn first.
   - "This is the problem we are solving today. The robot knows WHERE it needs to go, but it also needs to figure out HOW to face the right direction."

2. **Introduce the Concept of Heading**:
   - Draw a compass rose on the board: N at top, S at bottom, E at right, W at left.
   - Explain: "Heading is the direction the robot is currently facing. We are going to represent it as a number: 0 for North, 1 for East, 2 for South, 3 for West."
   - Write the numbers on the compass rose, going clockwise: 0 at top, 1 at right, 2 at bottom, 3 at left.
   - Physical demonstration: Place the robot on the grid. Announce its heading number. Rotate it and ask students to call out the new heading number.
   - Ask: "Why clockwise? Because each right turn adds 1 to the heading number. That is going to be the key to everything today."

3. **Connect to the Manhattan Path**:
   - Recall from previous lessons: the Manhattan algorithm produces a list of coordinates like `[(0,0), (1,0), (2,0), (2,1)]`.
   - "The path tells us WHERE to go. But we also need to know which way the robot is facing so we can figure out whether to turn."
   - Preview: "By the end of today, you will be able to look at any two consecutive coordinates and count the exact number of right turns the robot needs."

4. **Why This Matters**:
   - Without turn logic, the robot can only go in one direction
   - Real robots (cars, drones, rovers) all track heading
   - This is the bridge between the path-planning algorithm and actual robot movement

### Guided Practice (20 minutes)
**For 50-min classes:** 18 min
**For 3-hour sessions:** 25 min

1. **Step 1: Needed Heading from Coordinate Delta**:
   - Draw a small grid on the board with row/column labels:
     ```
           Col 0   Col 1   Col 2
     Row 0  (0,0)   (0,1)   (0,2)
     Row 1  (1,0)   (1,1)   (1,2)
     Row 2  (2,0)   (2,1)   (2,2)
     ```
   - Work through examples:
     - From (0,0) to (1,0): row increases by 1, col stays same --> heading **2** (South)
     - From (1,0) to (0,0): row decreases by 1, col stays same --> heading **0** (North)
     - From (0,0) to (0,1): row stays same, col increases by 1 --> heading **1** (East)
     - From (0,1) to (0,0): row stays same, col decreases by 1 --> heading **3** (West)
   - Summarize the rule:
     ```
     row_diff = next_row - current_row
     col_diff = next_col - current_col

     row_diff == -1 --> 0 (North)
     col_diff == 1  --> 1 (East)
     row_diff == 1  --> 2 (South)
     col_diff == -1 --> 3 (West)
     ```
   - Ask students to verify: "Why does row increasing mean South?" Answer: In our grid, row 0 is at the top, like a spreadsheet. Going down increases the row number. Down is South.

2. **Step 2: Counting Right Turns**:
   - Ask: "If I am heading 0 (North) and I turn right once, what heading am I now?" (1, East.) "Turn right again?" (2, South.) "Again?" (3, West.) "Again?" (0, back to North!)
   - Write on the board: "Each right turn adds 1 to the heading. After 3 comes 0 (wrap around). Count how many right turns to get from current to needed."
   - Physical check: Have students stand up, face the front of the room (heading 0, North), and turn right. Call out the heading number at each turn: 1, 2, 3, 0.
   - Now the key question: "If I am heading 0 (North) and I need to face heading 1 (East), how many right turns?" Count clockwise: 0->1. That is 1 right turn.
   - "If I am heading 0 (North) and I need to face heading 3 (West), how many right turns?" Count clockwise: 0->1->2->3. That is 3 right turns. Verify by counting: right once (East), right again (South), right again (West). Three right turns!
   - Now the tricky case: "If I am heading 3 (West) and I need to face heading 0 (North), how many right turns?" Count clockwise: 3->0. That is just 1 step because 3 wraps around to 0. Verify physically: right from West is North. One right turn!
   - This is the key idea: we do not need subtraction or any special formula. Just count steps clockwise, and when you pass 3, wrap back to 0.
   - Write the logic on the board:
     ```
     Start at current heading.
     Keep turning right (add 1, wrap 3 back to 0).
     Count the turns until you reach the needed heading.
     ```

3. **Step 3: What the Results Mean**:
   - Write on the board:
     ```
     0 right turns = no turn needed (already facing the right way)
     1 right turn  = turn right once (90 degrees)
     2 right turns = turn right twice (180 degrees)
     3 right turns = turn right three times (270 degrees, same as turning left once)
     ```
   - Work through examples by counting clockwise:
     - Heading: 0 (N), Need: 1 (E) --> count: 0->1, that is 1 right turn
     - Heading: 0 (N), Need: 3 (W) --> count: 0->1->2->3, that is 3 right turns
     - Heading: 0 (N), Need: 2 (S) --> count: 0->1->2, that is 2 right turns
     - Heading: 0 (N), Need: 0 (N) --> already there, that is 0 right turns
     - Heading: 1 (E), Need: 3 (W) --> count: 1->2->3, that is 2 right turns
     - Heading: 2 (S), Need: 1 (E) --> count: 2->3->0->1, that is 3 right turns
   - Point out: "We did not need separate cases for right, left, and 180. Counting clockwise handles everything."

4. **Step 4: Tracing a Full Path**:
   - Example path: `[(0,0), (1,0), (2,0), (2,1), (2,2)]`
   - Starting heading: 0 (North)
   - Trace on the board:
     ```
     At (0,0) heading 0(N), next is (1,0): need 2(S), count 0->1->2 = 2 right turns, now heading 2(S), drive to (1,0)
     At (1,0) heading 2(S), next is (2,0): need 2(S), already there = 0 right turns, drive to (2,0)
     At (2,0) heading 2(S), next is (2,1): need 1(E), count 2->3->0->1 = 3 right turns, now heading 1(E), drive to (2,1)
     At (2,1) heading 1(E), next is (2,2): need 1(E), already there = 0 right turns, drive to (2,2)
     ```
   - Have students call out each step before you write it.
   - Note: After turning, the new heading IS the needed heading. We just set `heading = needed`.

5. **Step 5: Quick Code Preview** (if time permits):
   - Show the `get_needed_heading()` function in Python:
     ```python
     HEADING_NAMES = ["N", "E", "S", "W"]

     def get_needed_heading(current_pos, next_pos):
         row_diff = next_pos[0] - current_pos[0]
         col_diff = next_pos[1] - current_pos[1]
         if row_diff == -1:
             return 0    # North
         elif col_diff == 1:
             return 1    # East
         elif row_diff == 1:
             return 2    # South
         elif col_diff == -1:
             return 3    # West

     # Trace a short path, printing the needed heading at each step
     path = [(0,0), (1,0), (2,0), (2,1)]
     heading = 0

     for i in range(len(path) - 1):
         current = path[i]
         next_pos = path[i + 1]
         needed = get_needed_heading(current, next_pos)
         print(f"At {current} heading {heading}({HEADING_NAMES[heading]}), need {needed}({HEADING_NAMES[needed]})")
         heading = needed
     ```
   - Run it in the console. Students can verify the needed headings match their paper work.
   - Point out: "We are not writing the turning code yet -- you counted right turns on paper, and in the next lesson the Navigator class will use a while loop to turn right until the heading matches."

### Independent Practice (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

**Exercise 1: Needed Heading from Delta (Paper)**
- Given the following pairs of coordinates, write the required heading number and letter:
  1. From (3,2) to (4,2) --> ___ (___)
  2. From (1,5) to (0,5) --> ___ (___)
  3. From (2,3) to (2,4) --> ___ (___)
  4. From (4,1) to (4,0) --> ___ (___)
  5. From (0,0) to (1,0) --> ___ (___)
- Answers: 2 (S), 0 (N), 1 (E), 3 (W), 2 (S)

**Exercise 2: Turn Calculation (Paper)**
- For each scenario, count clockwise from current heading to needed heading and write the number of right turns:
  1. Current: 0 (N), Need: 1 (E) --> count: 0->___ = ___ right turns
  2. Current: 1 (E), Need: 1 (E) --> already there = ___ right turns
  3. Current: 2 (S), Need: 0 (N) --> count: 2->___->___ = ___ right turns
  4. Current: 3 (W), Need: 2 (S) --> count: 3->___->___->___ = ___ right turns
  5. Current: 1 (E), Need: 0 (N) --> count: 1->___->___->___ = ___ right turns
  6. Current: 3 (W), Need: 1 (E) --> count: 3->___->___ = ___ right turns
  7. Current: 2 (S), Need: 3 (W) --> count: 2->___ = ___ right turns
  8. Current: 0 (N), Need: 3 (W) --> count: 0->___->___->___ = ___ right turns
- Answers: 1, 0, 2, 3, 3, 2, 1, 3

**Exercise 3: Full Path Trace (Paper)**
- Path: `[(0,0), (0,1), (0,2), (1,2), (2,2), (2,1), (2,0)]`
- Starting heading: 1 (E)
- For each step, write: current position, heading number, next position, needed heading, clockwise count, right turns, new heading
- Expected trace:
  ```
  At (0,0) heading 1(E), next (0,1): need 1(E), already there = 0, no turn, heading stays 1(E)
  At (0,1) heading 1(E), next (0,2): need 1(E), already there = 0, no turn, heading stays 1(E)
  At (0,2) heading 1(E), next (1,2): need 2(S), count 1->2 = 1, turn right x1, heading becomes 2(S)
  At (1,2) heading 2(S), next (2,2): need 2(S), already there = 0, no turn, heading stays 2(S)
  At (2,2) heading 2(S), next (2,1): need 3(W), count 2->3 = 1, turn right x1, heading becomes 3(W)
  At (2,1) heading 3(W), next (2,0): need 3(W), already there = 0, no turn, heading stays 3(W)
  ```

**Exercise 4: Trace a Path on Paper (Paper)**
- Path: `[(0,0), (0,1), (1,1), (2,1), (2,0)]`
- Starting heading: 0 (N)
- For each step, write: current position, current heading, next position, needed heading, clockwise count of right turns, new heading
- Verify your trace by checking that the needed heading at each step matches the coordinate delta

### Assessment

**Formative (during lesson)**:
- Can students correctly determine the needed heading number from a coordinate delta?
- Can they count clockwise from current heading to needed heading to get the right-turn count?
- Can they explain what results 0, 1, 2, and 3 mean in terms of physical turns?
- Can they trace through a multi-step path correctly on paper?

**Summative (worksheet/exit ticket)**:
1. If the robot is at (3,1) and needs to go to (3,2), what heading number does it need? What letter?
2. Describe the counting method for figuring out right turns in words (count clockwise steps on the compass from current to needed).
3. If the robot is heading 3 (West) and needs to go heading 1 (East), how many right turns? Show the clockwise counting.
4. What are the four possible results of counting right turns, and what does each one mean?
5. Trace the turns for path `[(1,1), (2,1), (2,2)]` with starting heading 2 (S).

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "North means up on the screen, so row should decrease" | This is actually correct! Row 0 is at the top. Moving North (up) decreases the row number. Students sometimes second-guess themselves on this. |
| "Right and left depend on which way I'm looking at the grid" | Right and left are relative to the robot's heading, not the viewer. The counting method handles this automatically since it works with heading numbers, not spatial reasoning. |
| "What if the heading goes past 3?" | It wraps back to 0, like an odometer rolling over. Heading 3 plus one right turn becomes heading 0 (North). The code checks for this: `if heading == 4: heading = 0`. |
| "3 right turns seems wasteful, why not just turn left?" | Physically, 3 right turns and 1 left turn end up at the same heading. Our robot uses `turn_right()` from Module 2, so we simply call it the calculated number of times. The counting method tells us how many. |
| "The heading numbers seem arbitrary" | They follow a consistent clockwise pattern: 0=N, 1=E, 2=S, 3=W. Each right turn adds 1. This is what makes the math work. |
| "Row increasing means North because numbers go up" | Numbers going up means the row index increases, which means moving DOWN on the grid. Down is South. This is the most common confusion. |
| "I need separate logic for right turns, left turns, and 180" | With numeric headings and clockwise counting, a single counting approach gives a number that tells the robot exactly how many right turns to make. No separate cases needed. |

## Differentiation

**For struggling students**:
- Provide a printed compass rose with numbers (0, 1, 2, 3) they can physically rotate to count right turns
- Start with only two directions (0=North and 2=South) before adding East and West
- Use a physical robot on the grid: point it in a direction, physically count right turns to the needed heading
- Provide additional compass rose diagrams to count turns physically
- Pair with a stronger student for the path-tracing exercise
- Let them verify by physically standing and turning right the calculated number of times

**For advanced students**:
- Ask: "How would you modify the function to count left turns instead?" Answer: subtract 1 instead of adding 1, and wrap from 0 back to 3.
- Challenge them to fill in the full 4x4 right-turns table and verify all 16 combinations
- Write a `get_needed_heading()` function that takes two coordinates and returns 0-3
- Consider: Could you extend this to 8 directions (adding NE, NW, SE, SW) by wrapping at 8 instead of 4? What changes?
- Create a visual path tracer that prints the grid with arrows showing the robot's heading at each step

## Materials & Code Examples

### Heading Reference
```python
# Headings as numbers (clockwise from North)
# 0 = North, 1 = East, 2 = South, 3 = West

HEADING_NAMES = ["N", "E", "S", "W"]
```

### Needed Heading from Delta Reference
```python
HEADING_NAMES = ["N", "E", "S", "W"]

def get_needed_heading(current, next_pos):
    row_diff = next_pos[0] - current[0]
    col_diff = next_pos[1] - current[1]
    if row_diff == -1:
        return 0
    elif col_diff == 1:
        return 1
    elif row_diff == 1:
        return 2
    elif col_diff == -1:
        return 3
```

### Path Tracing Example
```python
HEADING_NAMES = ["N", "E", "S", "W"]

def get_needed_heading(current, next_pos):
    row_diff = next_pos[0] - current[0]
    col_diff = next_pos[1] - current[1]
    if row_diff == -1:
        return 0
    elif col_diff == 1:
        return 1
    elif row_diff == 1:
        return 2
    elif col_diff == -1:
        return 3

path = [(0,0), (1,0), (2,0), (2,1), (2,2)]
heading = 0

for i in range(len(path) - 1):
    current = path[i]
    next_pos = path[i + 1]
    needed = get_needed_heading(current, next_pos)
    current_name = HEADING_NAMES[heading]
    needed_name = HEADING_NAMES[needed]
    print(f"At {current} heading {heading}({current_name}), need {needed}({needed_name})")
    heading = needed
    print(f"  Now heading {heading}({HEADING_NAMES[heading]}), drive to {next_pos}")
```

### Turn Logic Worksheet
```
Name: ________________________  Date: ______________

HEADING REFERENCE: 0=North, 1=East, 2=South, 3=West
COUNTING METHOD: Count clockwise from current to needed (0->1->2->3->0)

PART A: Needed Heading from Coordinate Delta
For each pair, write the needed heading number and letter:

1. (2,3) to (3,3) --> ___ (___)    2. (4,1) to (3,1) --> ___ (___)
3. (1,0) to (1,1) --> ___ (___)    4. (0,4) to (0,3) --> ___ (___)
5. (5,2) to (6,2) --> ___ (___)    6. (3,3) to (3,4) --> ___ (___)

PART B: Turn Calculations
Count clockwise from current to needed to find the number of right turns:

1. Current: 0(N), Need: 2(S) --> count: 0->___->___ = ___ right turns
2. Current: 1(E), Need: 2(S) --> count: 1->___ = ___ right turns
3. Current: 3(W), Need: 3(W) --> already there = ___ right turns
4. Current: 2(S), Need: 1(E) --> count: 2->___->___->___ = ___ right turns
5. Current: 0(N), Need: 3(W) --> count: 0->___->___->___ = ___ right turns
6. Current: 1(E), Need: 0(N) --> count: 1->___->___->___ = ___ right turns

PART C: Full Path Trace
Path: [(1,1), (1,2), (1,3), (2,3), (3,3), (3,2)]
Starting heading: 1 (E)

Step 1: At (1,1) heading ___(___), next (1,2): need ___(___), count: ___->___ = ___ turns, now heading ___(___)
Step 2: At (1,2) heading ___(___), next (1,3): need ___(___), count: ___->___ = ___ turns, now heading ___(___)
Step 3: At (1,3) heading ___(___), next (2,3): need ___(___), count: ___->___ = ___ turns, now heading ___(___)
Step 4: At (2,3) heading ___(___), next (3,3): need ___(___), count: ___->___ = ___ turns, now heading ___(___)
Step 5: At (3,3) heading ___(___), next (3,2): need ___(___), count: ___->___ = ___ turns, now heading ___(___)
```

## Teaching Notes
- **This lesson is intentionally paper-heavy.** Students need spatial reasoning before they start coding. Rushing to code without understanding the turn logic leads to frustrating debugging.
- **The grid orientation is confusing.** Row 0 at the top (like a spreadsheet) means "down is South and increasing rows." Repeat this several times. Draw it. Point at it. Quiz them on it.
- **Physical movement helps.** Have students stand up and physically turn right. "You are heading 0. Turn right. What heading number?" This kinesthetic exercise cements the concept and lets them verify by counting turns.
- **The counting approach is the key insight.** Stepping clockwise one turn at a time and counting is something every student can do. In the next lesson, the Navigator class will use a while loop to turn right until the heading matches -- doing exactly what students do on paper.
- **The wrap-around from 3 to 0 is the key concept.** Use the clock or odometer analogy: "An odometer goes 7, 8, 9, 0, 1, 2... it wraps around. Our headings do the same: 1, 2, 3, 0, 1, 2... After 3 comes 0." This is the only tricky part -- once students get the wrap, the rest is just counting.
- **Connect to the physical robot.** Remind students that on the actual robot, each "right turn" will call `turn_right()` from Module 2 -- the sensor-based turn that drives forward briefly then spins right until it finds the outbound line. So `turns = 2` means calling `turn_right()` twice. This connection will be made concrete in Lesson 8.
- **Why all right turns?** Students may ask why we do not just turn left when the count gives 3. The answer is simplicity: one turn function, one counting method, one loop. The robot does not care whether 270 degrees right or 90 degrees left is "faster" -- both get it to the same heading. Keeping the code simple matters more than saving a turn.

## Connections to Next Lessons
- **Lesson 8** will implement the `Navigator` class with `get_needed_heading()` and a `turn_to()` method that uses a while loop to turn right until the heading matches -- translating the paper counting into code.
- **Lesson 9** (Final Project) will combine the `Manhattan` class and `Navigator` class into a complete grid-navigation program.
- The heading numbers and clockwise counting introduced here become the foundation for the Navigator class. Students already understand the logic; Lesson 8 puts it into code.
