# Lesson 7: The Challenge of Turning

## Overview
Students confront the problem that their robot has a **heading** -- a direction it is currently facing -- and that moving to the next grid coordinate may require turning first. This lesson introduces the concept of robot heading (N, S, E, W), shows how to determine the required direction from a coordinate change, and develops the turn logic using dictionaries of right and left turns. Students work through paper exercises with diagrams before writing any code, building strong spatial reasoning that will feed directly into the Navigator class in Lesson 8.

## Learning Objectives
By the end of this lesson, students will be able to:
- Define "heading" and explain why it matters for grid navigation
- Determine the required travel direction from a coordinate delta (row and column changes)
- Use dictionaries to look up the result of a right turn or left turn from any heading
- Determine the correct turn (right, left, 180, or none) given a current heading and a needed direction
- Trace through a sequence of path coordinates on paper and list the turns required

## Key Concepts
- **Heading**: The compass direction the robot is currently facing (N, S, E, W)
- **Coordinate delta**: The difference between the next position and the current position in row and column
- **Direction from delta**: Row increases means heading South; row decreases means heading North; column increases means heading East; column decreases means heading West
- **Right turn lookup**: A dictionary mapping each heading to the heading after a 90-degree right turn
- **Left turn lookup**: A dictionary mapping each heading to the heading after a 90-degree left turn
- **180-degree turn**: When the needed direction is directly behind the robot; requires turning twice or a single 180-degree turn

## Materials Required
- XRP Robot (for demonstration only in this lesson)
- Grid mat or taped grid from previous lessons
- Printed turn-logic worksheet (see Materials & Code Examples)
- Whiteboard or projector for diagrams
- VS Code with Python installed and XRPLib configured
- Compass rose diagram handout (N/S/E/W)

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
   - Explain: "Heading is the direction the robot is currently facing. We will track it as one of four values: N, S, E, or W."
   - Physical demonstration: Place the robot on the grid. Announce its heading. Rotate it and ask students to call out the new heading.

3. **Connect to the Manhattan Path**:
   - Recall from previous lessons: the Manhattan algorithm produces a list of coordinates like `[(0,0), (1,0), (2,0), (2,1)]`.
   - "The path tells us WHERE to go. But we also need to know which way the robot is facing so we can figure out whether to turn."
   - Preview: "By the end of today, you will be able to look at any two consecutive coordinates and immediately know what turn the robot needs."

4. **Why This Matters**:
   - Without turn logic, the robot can only go in one direction
   - Real robots (cars, drones, rovers) all track heading
   - This is the bridge between the path-planning algorithm and actual robot movement

### Guided Practice (20 minutes)
**For 50-min classes:** 18 min
**For 3-hour sessions:** 25 min

1. **Step 1: Direction from Coordinate Delta**:
   - Draw a small grid on the board with row/column labels:
     ```
           Col 0   Col 1   Col 2
     Row 0  (0,0)   (0,1)   (0,2)
     Row 1  (1,0)   (1,1)   (1,2)
     Row 2  (2,0)   (2,1)   (2,2)
     ```
   - Work through examples:
     - From (0,0) to (1,0): row increases by 1, col stays same --> direction is **S** (South)
     - From (1,0) to (0,0): row decreases by 1, col stays same --> direction is **N** (North)
     - From (0,0) to (0,1): row stays same, col increases by 1 --> direction is **E** (East)
     - From (0,1) to (0,0): row stays same, col decreases by 1 --> direction is **W** (West)
   - Summarize the rule:
     ```
     row_diff = next_row - current_row
     col_diff = next_col - current_col

     row_diff == 1  --> S (South)
     row_diff == -1 --> N (North)
     col_diff == 1  --> E (East)
     col_diff == -1 --> W (West)
     ```
   - Ask students to verify: "Why does row increasing mean South?" Answer: In our grid, row 0 is at the top, like a spreadsheet. Going down increases the row number. Down is South.

2. **Step 2: The Turn Dictionaries**:
   - Ask: "If I am facing North and I turn right, which direction am I facing now?" (East)
   - Build the right-turn dictionary together on the board:
     ```python
     right_turns = {"N": "E", "E": "S", "S": "W", "W": "N"}
     ```
   - Read it aloud: "If facing North, a right turn gives East. If facing East, a right turn gives South..." and so on.
   - Now build the left-turn dictionary:
     ```python
     left_turns = {"N": "W", "W": "S", "S": "E", "E": "N"}
     ```
   - Physical check: Have students stand up, face the front of the room (North), and physically turn right. They should now face the right wall (East). Repeat for left turns.

3. **Step 3: Determining the Turn**:
   - Given a current heading and a needed direction, there are four cases:
     ```
     Case 1: heading == needed direction --> No turn needed
     Case 2: right_turns[heading] == needed direction --> Turn right (90 degrees)
     Case 3: left_turns[heading] == needed direction --> Turn left (-90 degrees)
     Case 4: None of the above --> Turn 180 degrees
     ```
   - Work through examples on the board:
     - Heading: N, Need: E --> `right_turns["N"]` is "E" --> Turn right 90
     - Heading: N, Need: W --> `left_turns["N"]` is "W" --> Turn left 90
     - Heading: N, Need: S --> Not right, not left --> Turn 180
     - Heading: N, Need: N --> Same --> No turn
     - Heading: E, Need: W --> Not right ("S"), not left ("N") --> Turn 180
   - Ask students: "How many right turns does it take to go from North to South?" (Two.) "That is why 180 degrees is the 'opposite' case."

4. **Step 4: Tracing a Full Path**:
   - Example path: `[(0,0), (1,0), (2,0), (2,1), (2,2)]`
   - Starting heading: N (facing North)
   - Trace on the board:
     ```
     At (0,0) heading N, next is (1,0): need S, turn 180 --> now heading S, drive to (1,0)
     At (1,0) heading S, next is (2,0): need S, no turn --> drive to (2,0)
     At (2,0) heading S, next is (2,1): need E, turn left --> now heading E, drive to (2,1)
     At (2,1) heading E, next is (2,2): need E, no turn --> drive to (2,2)
     ```
   - Have students call out each step before you write it.

5. **Step 5: Quick Code Preview** (if time permits):
   - Show the logic in Python without building a full class yet:
     ```python
     right_turns = {"N": "E", "E": "S", "S": "W", "W": "N"}
     left_turns = {"N": "W", "W": "S", "S": "E", "E": "N"}

     heading = "N"
     needed = "E"

     if heading == needed:
         print("No turn needed")
     elif right_turns[heading] == needed:
         print("Turn right 90")
     elif left_turns[heading] == needed:
         print("Turn left 90")
     else:
         print("Turn 180")
     ```
   - Run it in the console. Change `heading` and `needed` to test different combinations.

### Independent Practice (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

**Exercise 1: Direction from Delta (Paper)**
- Given the following pairs of coordinates, write the required direction (N, S, E, W):
  1. From (3,2) to (4,2) --> ___
  2. From (1,5) to (0,5) --> ___
  3. From (2,3) to (2,4) --> ___
  4. From (4,1) to (4,0) --> ___
  5. From (0,0) to (1,0) --> ___
- Answers: S, N, E, W, S

**Exercise 2: Turn Determination (Paper)**
- For each scenario, determine the turn needed (none, right 90, left 90, or 180):
  1. Heading: N, Need: E --> ___
  2. Heading: E, Need: E --> ___
  3. Heading: S, Need: N --> ___
  4. Heading: W, Need: S --> ___
  5. Heading: E, Need: N --> ___
  6. Heading: W, Need: E --> ___
  7. Heading: S, Need: W --> ___
  8. Heading: N, Need: W --> ___
- Answers: right 90, none, 180, left 90, left 90, 180, right 90, left 90

**Exercise 3: Full Path Trace (Paper)**
- Path: `[(0,0), (0,1), (0,2), (1,2), (2,2), (2,1), (2,0)]`
- Starting heading: E
- For each step, write: current position, heading, next position, needed direction, turn, new heading
- Expected trace:
  ```
  At (0,0) heading E, next (0,1): need E, no turn, heading stays E
  At (0,1) heading E, next (0,2): need E, no turn, heading stays E
  At (0,2) heading E, next (1,2): need S, turn right, heading becomes S
  At (1,2) heading S, next (2,2): need S, no turn, heading stays S
  At (2,2) heading S, next (2,1): need W, turn right, heading becomes W
  At (2,1) heading W, next (2,0): need W, no turn, heading stays W
  ```

**Exercise 4: Code the Turn Logic (Computer)**
- Write a Python script that:
  1. Defines the `right_turns` and `left_turns` dictionaries
  2. Asks for a heading and a needed direction (or hard-codes several test cases)
  3. Prints the required turn
- Expected code:
  ```python
  right_turns = {"N": "E", "E": "S", "S": "W", "W": "N"}
  left_turns = {"N": "W", "W": "S", "S": "E", "E": "N"}

  test_cases = [
      ("N", "E"),
      ("N", "S"),
      ("E", "E"),
      ("W", "N"),
      ("S", "W"),
  ]

  for heading, needed in test_cases:
      if heading == needed:
          turn = "No turn"
      elif right_turns[heading] == needed:
          turn = "Right 90"
      elif left_turns[heading] == needed:
          turn = "Left 90"
      else:
          turn = "Turn 180"
      print(f"Heading: {heading}, Need: {needed} --> {turn}")
  ```

### Assessment

**Formative (during lesson)**:
- Can students correctly determine direction from a coordinate delta?
- Can they use the turn dictionaries to find the result of a right or left turn?
- Can they determine the correct turn for any heading/direction pair?
- Can they trace through a multi-step path correctly on paper?

**Summative (worksheet/exit ticket)**:
1. If the robot is at (3,1) and needs to go to (3,2), what direction must it travel?
2. What are the four possible turn decisions the robot might need to make?
3. If the robot is heading West and needs to go East, what turn does it make?
4. Write the `right_turns` dictionary from memory.
5. Trace the turns for path `[(1,1), (2,1), (2,2)]` with starting heading S.

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "North means up on the screen, so row should decrease" | This is actually correct! Row 0 is at the top. Moving North (up) decreases the row number. Students sometimes second-guess themselves on this. |
| "Right and left depend on which way I'm looking at the grid" | Right and left are relative to the robot's heading, not the viewer. If the robot faces South, its right is West. |
| "A 180-degree turn is just two right turns" | Correct! But in code we handle it as a single case for efficiency. The robot can turn 180 in one command. |
| "The turn dictionaries seem arbitrary" | They follow a consistent pattern: right turns go clockwise (N->E->S->W->N), left turns go counterclockwise (N->W->S->E->N). |
| "I need to know the angle between directions" | Not with our dictionary approach. We just look up whether the needed direction matches a right turn, left turn, or neither. |
| "Row increasing means North because numbers go up" | Numbers going up means the row index increases, which means moving DOWN on the grid. Down is South. This is the most common confusion. |

## Differentiation

**For struggling students**:
- Provide a printed compass rose they can physically rotate to determine turns
- Start with only two directions (N and S) before adding E and W
- Use a physical robot on the grid: point it in a direction, ask what turn it needs
- Provide the turn dictionaries pre-written; focus on using them rather than constructing them
- Pair with a stronger student for the path-tracing exercise

**For advanced students**:
- Add diagonal directions (NE, NW, SE, SW) and extend the turn dictionaries to handle 45-degree turns
- Write a function that returns the number of degrees to turn (0, 90, -90, or 180) instead of a description
- Create a visual path tracer that prints the grid with arrows showing the robot's heading at each step
- Consider: What happens if the path has an invalid step (diagonal move on a Manhattan grid)? Write error handling.

## Materials & Code Examples

### Turn Logic Reference
```python
right_turns = {"N": "E", "E": "S", "S": "W", "W": "N"}
left_turns = {"N": "W", "W": "S", "S": "E", "E": "N"}
```

### Direction from Delta Reference
```python
def get_direction(current, next_pos):
    row_diff = next_pos[0] - current[0]
    col_diff = next_pos[1] - current[1]
    if row_diff == 1:
        return "S"
    elif row_diff == -1:
        return "N"
    elif col_diff == 1:
        return "E"
    elif col_diff == -1:
        return "W"
```

### Complete Turn Decision Logic
```python
right_turns = {"N": "E", "E": "S", "S": "W", "W": "N"}
left_turns = {"N": "W", "W": "S", "S": "E", "E": "N"}

def decide_turn(heading, needed):
    if heading == needed:
        return "none"
    elif right_turns[heading] == needed:
        return "right 90"
    elif left_turns[heading] == needed:
        return "left 90"
    else:
        return "180"
```

### Path Tracing Example
```python
right_turns = {"N": "E", "E": "S", "S": "W", "W": "N"}
left_turns = {"N": "W", "W": "S", "S": "E", "E": "N"}

def get_direction(current, next_pos):
    row_diff = next_pos[0] - current[0]
    col_diff = next_pos[1] - current[1]
    if row_diff == 1:
        return "S"
    elif row_diff == -1:
        return "N"
    elif col_diff == 1:
        return "E"
    elif col_diff == -1:
        return "W"

def decide_turn(heading, needed):
    if heading == needed:
        return "none"
    elif right_turns[heading] == needed:
        return "right 90"
    elif left_turns[heading] == needed:
        return "left 90"
    else:
        return "180"

path = [(0,0), (1,0), (2,0), (2,1), (2,2)]
heading = "N"

for i in range(len(path) - 1):
    current = path[i]
    next_pos = path[i + 1]
    needed = get_direction(current, next_pos)
    turn = decide_turn(heading, needed)
    print(f"At {current} heading {heading}, need {needed} --> {turn}")
    if turn == "right 90":
        heading = right_turns[heading]
    elif turn == "left 90":
        heading = left_turns[heading]
    elif turn == "180":
        heading = right_turns[right_turns[heading]]
    print(f"  Now heading {heading}, drive to {next_pos}")
```

### Turn Logic Worksheet
```
Name: ________________________  Date: ______________

PART A: Direction from Coordinate Delta
For each pair, write the direction (N, S, E, W):

1. (2,3) to (3,3) --> ___    2. (4,1) to (3,1) --> ___
3. (1,0) to (1,1) --> ___    4. (0,4) to (0,3) --> ___
5. (5,2) to (6,2) --> ___    6. (3,3) to (3,4) --> ___

PART B: Turn Decisions
Given heading and needed direction, write the turn:

1. Heading: N, Need: S --> ___    2. Heading: E, Need: S --> ___
3. Heading: W, Need: W --> ___    4. Heading: S, Need: E --> ___
5. Heading: N, Need: W --> ___    6. Heading: E, Need: N --> ___

PART C: Full Path Trace
Path: [(1,1), (1,2), (1,3), (2,3), (3,3), (3,2)]
Starting heading: E

Step 1: At (1,1) heading ___, next (1,2): need ___, turn ___, now heading ___
Step 2: At (1,2) heading ___, next (1,3): need ___, turn ___, now heading ___
Step 3: At (1,3) heading ___, next (2,3): need ___, turn ___, now heading ___
Step 4: At (2,3) heading ___, next (3,3): need ___, turn ___, now heading ___
Step 5: At (3,3) heading ___, next (3,2): need ___, turn ___, now heading ___
```

## Teaching Notes
- **This lesson is intentionally paper-heavy.** Students need spatial reasoning before they start coding. Rushing to code without understanding the turn logic leads to frustrating debugging.
- **The grid orientation is confusing.** Row 0 at the top (like a spreadsheet) means "down is South and increasing rows." Repeat this several times. Draw it. Point at it. Quiz them on it.
- **Physical movement helps.** Have students stand up and physically turn. "You are facing North. Turn right. What direction are you facing?" This kinesthetic exercise cements the concept.
- **The dictionaries are the key insight.** Instead of complex if/else chains with angles, we use simple lookups. This is a great example of using data structures to simplify logic.
- **Watch for right/left confusion relative to the robot.** When the robot faces South, its right is West. Students often think of right/left from the viewer's perspective, not the robot's. The dictionaries handle this automatically.
- **Common syntax errors to watch for:**
  - Using square brackets instead of curly braces for dictionaries
  - Forgetting quotes around the direction strings
  - Confusing `right_turns[heading]` (lookup) with `right_turns["N"] = "E"` (assignment)

## Connections to Next Lessons
- **Lesson 8** will package all of this turn logic into a `Navigator` class with `get_needed_direction()` and `turn_to()` methods.
- **Lesson 9** (Final Project) will combine the `Manhattan` class and `Navigator` class into a complete grid-navigation program.
- The turn dictionaries introduced here become attributes of the Navigator class, keeping the same logic but organized inside an object.
