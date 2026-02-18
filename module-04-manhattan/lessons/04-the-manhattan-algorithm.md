# Lesson 4: The Manhattan Algorithm

## Overview
Students learn the Manhattan distance algorithm -- a strategy for navigating a grid by moving along rows first, then columns. Named after the grid layout of Manhattan in New York City (where you cannot cut diagonally through city blocks), this approach gives the robot a simple, predictable path between any two grid positions. This is a **paper-based lesson**: students hand-trace paths on worksheets before writing any code. By working through multiple examples with pencil and paper, students build a clear mental model of how the algorithm determines direction and generates each step of the path.

## Learning Objectives
By the end of this lesson, students will be able to:
- Explain what Manhattan distance means and why it is named after Manhattan, NYC
- Describe the "rows first, then columns" navigation strategy
- Determine the step direction (+1 or -1) for both rows and columns given a start and destination
- Hand-trace the complete path for any start/destination pair on a grid
- Identify and handle edge cases: same row, same column, and same position
- Predict the total number of steps for a given start and destination

## Key Concepts
- **Manhattan Distance**: The total number of grid steps between two points when you can only move along rows and columns (no diagonals). Calculated as |row difference| + |column difference|.
- **Grid Position**: A location on the grid represented as a tuple (row, column), where (0, 0) is the top-left corner
- **Rows First, Then Columns**: The strategy of completing all row movement before starting any column movement -- this gives a predictable, L-shaped path
- **Step Direction**: The value +1 or -1 that determines which direction to move along an axis. If the destination is greater, step is +1; if the destination is smaller, step is -1.
- **Path**: The ordered list of grid positions the robot visits from start to destination, including both the starting position and the final destination
- **Edge Case**: A special situation that needs consideration -- such as when the start and destination share the same row, same column, or are the same position entirely

## Materials Required
- Grid worksheets (4x4 or 5x5 grids with labeled rows and columns)
- Pencils and colored markers/pens for tracing paths
- Whiteboard or projector for demonstrations
- Reference: A map of Manhattan, NYC (optional, for the hook)
- No computers needed -- this is a paper lesson

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 8 min
**For 3-hour sessions:** 10-12 min

1. **Hook: Why Is It Called "Manhattan Distance"?**
   - Show a map of Manhattan, NYC (or draw a simple grid on the board)
   - Ask: "If you are at the corner of 2nd Street and 3rd Avenue, and you need to get to 5th Street and 1st Avenue, can you walk diagonally through the buildings?"
   - No! You have to walk along the streets (rows) and avenues (columns). The total distance is the number of blocks along streets plus the number of blocks along avenues.
   - This is called **Manhattan distance** -- also known as "taxicab distance" because taxis in Manhattan follow the grid too.

2. **Connect to the Robot's Grid**:
   - Draw a 4x4 grid on the board with positions labeled (0,0) through (3,3):
     ```
          Col 0   Col 1   Col 2   Col 3
     Row 0  (0,0)   (0,1)   (0,2)   (0,3)
     Row 1  (1,0)   (1,1)   (1,2)   (1,3)
     Row 2  (2,0)   (2,1)   (2,2)   (2,3)
     Row 3  (3,0)   (3,1)   (3,2)   (3,3)
     ```
   - Explain: "Our robot lives on a grid like this. It can move up, down, left, or right -- but not diagonally. We need an algorithm that tells the robot exactly which squares to visit to get from any starting position to any destination."

3. **Introduce the Strategy: Rows First, Then Columns**:
   - The simplest approach: first move along the rows until you reach the correct row, THEN move along the columns until you reach the correct column.
   - This always produces an L-shaped path (or a straight line if the row or column is already correct).
   - Ask: "Why is this simpler than trying to alternate between row and column moves?" (It is predictable, easy to implement, and always works.)

### Guided Practice: Hand-Tracing Paths (20 minutes)
**For 50-min classes:** 22 min
**For 3-hour sessions:** 30 min

1. **Example 1: (0,0) to (2,3)**
   - Draw the grid on the board. Mark (0,0) as START and (2,3) as DESTINATION.
   - Step 1 -- Determine row direction:
     - Current row: 0, Destination row: 2
     - Destination row is greater, so row_step = +1 (move down)
   - Step 2 -- Determine column direction:
     - Current column: 0, Destination column: 3
     - Destination column is greater, so col_step = +1 (move right)
   - Step 3 -- Move rows first:
     - Start at (0, 0) -- add to path
     - Row 0 is not 2, so move: (0+1, 0) = (1, 0) -- add to path
     - Row 1 is not 2, so move: (1+1, 0) = (2, 0) -- add to path
     - Row 2 equals 2 -- done with rows
   - Step 4 -- Move columns:
     - Column 0 is not 3, so move: (2, 0+1) = (2, 1) -- add to path
     - Column 1 is not 3, so move: (2, 1+1) = (2, 2) -- add to path
     - Column 2 is not 3, so move: (2, 2+1) = (2, 3) -- add to path
     - Column 3 equals 3 -- done with columns
   - **Complete path: [(0,0), (1,0), (2,0), (2,1), (2,2), (2,3)]**
   - Trace this on the grid with arrows. Count: 5 moves, 6 positions in the path.
   - Manhattan distance: |2-0| + |3-0| = 2 + 3 = 5 moves

2. **Example 2: (2,3) to (0,1)**
   - Mark (2,3) as START and (0,1) as DESTINATION.
   - Determine row direction:
     - Current row: 2, Destination row: 0
     - Destination row is smaller, so row_step = -1 (move up)
   - Determine column direction:
     - Current column: 3, Destination column: 1
     - Destination column is smaller, so col_step = -1 (move left)
   - Move rows first:
     - Start at (2, 3) -- add to path
     - (2-1, 3) = (1, 3) -- add to path
     - (1-1, 3) = (0, 3) -- add to path
     - Row 0 equals 0 -- done with rows
   - Move columns:
     - (0, 3-1) = (0, 2) -- add to path
     - (0, 2-1) = (0, 1) -- add to path
     - Column 1 equals 1 -- done with columns
   - **Complete path: [(2,3), (1,3), (0,3), (0,2), (0,1)]**
   - Key observation: This time both steps are -1. The algorithm works the same way regardless of direction.

3. **Example 3: (3,0) to (1,2)**
   - Mark (3,0) as START and (1,2) as DESTINATION.
   - Row direction: 1 < 3, so row_step = -1 (move up)
   - Column direction: 2 > 0, so col_step = +1 (move right)
   - Move rows first:
     - Start at (3, 0)
     - (2, 0)
     - (1, 0)
     - Row 1 equals 1 -- done
   - Move columns:
     - (1, 1)
     - (1, 2)
     - Column 2 equals 2 -- done
   - **Complete path: [(3,0), (2,0), (1,0), (1,1), (1,2)]**
   - This time row_step is -1 and col_step is +1 -- they can be different!

4. **Edge Cases**:
   - **Same row: (1,0) to (1,3)**
     - Row direction: 1 equals 1, so... what is row_step? We still calculate it (will be -1 since 3 is not less than 1, actually this does not matter because the while loop for rows will not execute -- the row is already correct).
     - Rows phase: current_row already equals dest_row, so skip entirely.
     - Columns phase: (1,0) -> (1,1) -> (1,2) -> (1,3)
     - **Path: [(1,0), (1,1), (1,2), (1,3)]** -- a straight horizontal line
   - **Same column: (0,2) to (3,2)**
     - Columns phase: current_col already equals dest_col, skip entirely.
     - **Path: [(0,2), (1,2), (2,2), (3,2)]** -- a straight vertical line
   - **Same position: (2,1) to (2,1)**
     - Both phases skip entirely.
     - **Path: [(2,1)]** -- just the starting position, no movement needed
     - Ask: "Is this a bug?" No! The robot is already where it needs to be. The path correctly contains just its current position.

5. **The Algorithm in Plain English**:
   - Write on the board:
     ```
     1. Start at your current position. Add it to the path.
     2. Figure out which direction to move in rows (+1 or -1).
     3. Figure out which direction to move in columns (+1 or -1).
     4. While you are not in the correct row:
          Move one step in the row direction.
          Add the new position to the path.
     5. While you are not in the correct column:
          Move one step in the column direction.
          Add the new position to the path.
     6. Return the path.
     ```

### Independent Practice (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

**Exercise: Hand-Trace Paths on the Worksheet**
- Students complete the following on their grid worksheets, showing all work:

1. **(0,0) to (3,3)** -- Moving down and right (both steps are +1)
   - Write the row_step and col_step
   - List every position in the path
   - Draw the path on the grid
   - Expected path: [(0,0), (1,0), (2,0), (3,0), (3,1), (3,2), (3,3)]

2. **(3,3) to (0,0)** -- Moving up and left (both steps are -1)
   - Expected path: [(3,3), (2,3), (1,3), (0,3), (0,2), (0,1), (0,0)]

3. **(1,3) to (3,1)** -- Moving down and left (row_step +1, col_step -1)
   - Expected path: [(1,3), (2,3), (3,3), (3,2), (3,1)]

4. **(2,2) to (2,0)** -- Same row (column movement only)
   - Expected path: [(2,2), (2,1), (2,0)]

5. **(0,1) to (3,1)** -- Same column (row movement only)
   - Expected path: [(0,1), (1,1), (2,1), (3,1)]

6. **(1,1) to (1,1)** -- Same position (no movement)
   - Expected path: [(1,1)]

7. **Challenge: Calculate the Manhattan distance for each path above** (total number of moves = length of path minus 1)

## Assessment

**Formative (during lesson)**:
- Can students determine the correct row_step and col_step for a given start and destination?
- Can students correctly trace the "rows first, then columns" path on the grid?
- Can students identify what happens in edge cases (same row, same column, same position)?
- Can students explain why the path always forms an L-shape (or a straight line)?

**Summative (worksheet/exit ticket)**:
1. What is Manhattan distance? Why is it called that?
2. Given start (0,2) and destination (3,0), what is the row_step? What is the col_step?
3. Trace the complete path from (1,0) to (3,2). List every position.
4. How many moves does the path from (0,0) to (2,3) require? How does this relate to the Manhattan distance?
5. What happens when the start and destination are in the same row? What part of the algorithm is skipped?

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "The robot can move diagonally on the grid" | The robot can only move along rows or columns, one step at a time. Diagonal movement is not possible on a grid -- that is the whole point of Manhattan distance. |
| "The step is always +1" | The step is +1 when moving to a higher row/column number and -1 when moving to a lower one. The direction depends on whether the destination is greater or smaller than the current position. |
| "The path does not include the starting position" | The path always starts with the current position. If you are at (0,0) going to (2,3), the first element of the path is (0,0). |
| "Rows first, then columns is the only valid strategy" | You could also do columns first, then rows. Or alternate. We chose rows first because it is simple and consistent. Any strategy that avoids diagonals will give a valid Manhattan path. |
| "Same position means the algorithm is broken" | When start equals destination, the row and column loops simply do not execute. The path contains just the starting position. This is correct behavior, not a bug. |
| "Manhattan distance counts the number of positions in the path" | Manhattan distance counts the number of moves (steps). The path list has one more element than the number of moves because it includes the starting position. |

## Differentiation

**For struggling students**:
- Provide pre-drawn grids with the start and destination already marked
- Work through the first two examples together as a group before independent work
- Focus on just the "rows first" phase first, then add columns
- Use colored markers: one color for row moves, another for column moves
- Pair with a partner for the independent practice
- Provide the algorithm steps as a printed reference card

**For advanced students**:
- Calculate the Manhattan distance for each path and verify it equals |row_diff| + |col_diff|
- Consider: What if we did "columns first, then rows" instead? How would the paths differ? Would the total distance change?
- Challenge: How many DIFFERENT Manhattan paths exist between two points? (For a 2x3 path, there are C(5,2) = 10 different paths)
- Think ahead: How would you write this algorithm in Python? What data structures would you need?
- Research: Where else is Manhattan distance used? (Chess, image processing, clustering algorithms)

## Materials & Code Examples

### Grid Reference (for Board Drawing)
```
         Col 0    Col 1    Col 2    Col 3
Row 0    (0,0)    (0,1)    (0,2)    (0,3)
Row 1    (1,0)    (1,1)    (1,2)    (1,3)
Row 2    (2,0)    (2,1)    (2,2)    (2,3)
Row 3    (3,0)    (3,1)    (3,2)    (3,3)
```

### Example Path Trace: (0,0) to (2,3)
```
Step  Action          Position   Path So Far
---   ------          --------   -----------
0     Start           (0,0)      [(0,0)]
1     Row +1          (1,0)      [(0,0), (1,0)]
2     Row +1          (2,0)      [(0,0), (1,0), (2,0)]
3     Col +1          (2,1)      [(0,0), (1,0), (2,0), (2,1)]
4     Col +1          (2,2)      [(0,0), (1,0), (2,0), (2,1), (2,2)]
5     Col +1          (2,3)      [(0,0), (1,0), (2,0), (2,1), (2,2), (2,3)]

Manhattan distance: |2-0| + |3-0| = 5 moves
Path length: 6 positions (5 moves + 1 starting position)
```

### Example Path Trace: (2,3) to (0,1)
```
Step  Action          Position   Path So Far
---   ------          --------   -----------
0     Start           (2,3)      [(2,3)]
1     Row -1          (1,3)      [(2,3), (1,3)]
2     Row -1          (0,3)      [(2,3), (1,3), (0,3)]
3     Col -1          (0,2)      [(2,3), (1,3), (0,3), (0,2)]
4     Col -1          (0,1)      [(2,3), (1,3), (0,3), (0,2), (0,1)]

Manhattan distance: |0-2| + |1-3| = 4 moves
```

### Algorithm in Pseudocode
```
ALGORITHM: Manhattan Path
INPUT: start (row, col), destination (row, col)
OUTPUT: list of positions from start to destination

1. path = [start]
2. current_row = start row
3. current_col = start column
4. dest_row = destination row
5. dest_col = destination column

6. IF dest_row > current_row THEN row_step = +1
   ELSE row_step = -1

7. IF dest_col > current_col THEN col_step = +1
   ELSE col_step = -1

8. WHILE current_row != dest_row:
       current_row = current_row + row_step
       ADD (current_row, current_col) to path

9. WHILE current_col != dest_col:
       current_col = current_col + col_step
       ADD (current_row, current_col) to path

10. RETURN path
```

### Worksheet Template (for Printing)
For each problem, students should fill in:
```
Start: (__, __)    Destination: (__, __)

Row direction: dest_row ___ current_row, so row_step = ___
Col direction: dest_col ___ current_col, so col_step = ___

Row moves:
  Current position: (__, __)  -- add to path
  Move row: (__, __)  -- add to path
  Move row: (__, __)  -- add to path
  (continue as needed)
  Row matches destination -- stop row moves

Column moves:
  Move col: (__, __)  -- add to path
  Move col: (__, __)  -- add to path
  (continue as needed)
  Column matches destination -- stop column moves

Complete path: [                                          ]
Manhattan distance: |___| + |___| = ___ moves
```

## Teaching Notes
- **This is a paper lesson for a reason.** Students need to internalize the algorithm before typing code. If they jump straight to coding, they will struggle to debug because they will not know what the correct answer should be.
- **Draw big grids.** Use the entire whiteboard. Have students come up and trace paths with markers. The physical act of drawing the path builds understanding.
- **The Manhattan name sticks.** Students remember the algorithm better when they connect it to the real-world grid of NYC streets. If possible, show an actual map of Manhattan.
- **Watch for row/column confusion.** Some students will mix up rows and columns. Reinforce: rows go across (horizontal, like rows of desks), columns go up and down (vertical, like columns on a building). On our grid, the first number is the row, the second is the column.
- **The step direction is the trickiest part.** Students often get confused about when to use +1 versus -1. Emphasize: if you need to go to a BIGGER number, step is +1. If you need to go to a SMALLER number, step is -1. This is true for both rows and columns independently.
- **Do not skip the edge cases.** Students need to see that the algorithm handles same-row, same-column, and same-position naturally. These are not special cases -- the while loops simply do not execute when there is no movement needed.
- **Save the student worksheets.** They will use their hand-traced paths in Lesson 6 to verify their code output.

## Connections to Next Lessons
- **Lesson 5** will translate this exact algorithm into a Python class called `Manhattan` with a `compute_path()` method. The hand-traced paths from this lesson become the expected output students will check against.
- **Lesson 6** will focus on testing the `Manhattan` class without a robot -- students will compare their code output directly to the worksheets from this lesson.
- **Later lessons** in Module 4 will connect the computed path to actual robot movement on the physical grid.
