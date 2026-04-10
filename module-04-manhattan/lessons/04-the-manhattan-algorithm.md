# Lesson 4: The Manhattan Algorithm

## Overview
Students learn the Manhattan distance algorithm -- a strategy for navigating a grid by moving along rows first, then columns. Named after the grid layout of Manhattan in New York City (where you cannot cut diagonally through city blocks), this approach gives the robot a simple, predictable path between any two grid positions. Students first hand-trace a few paths on paper to build a mental model of the algorithm, then write a Python `compute_path()` function in two stages: first handling positive directions only (south and east), then extending to all four directions by adding two more while loops.

## Learning Objectives
By the end of this lesson, students will be able to:
- Explain what Manhattan distance means and why it is named after Manhattan, NYC
- Describe the "rows first, then columns" navigation strategy
- Hand-trace a path on a grid to build intuition before coding
- Write a `compute_path(start, end)` function that returns a path using while loops
- Extend the function from 2 while loops (positive directions) to 4 while loops (all directions)
- Use tuple unpacking to extract row and column from a position tuple
- Identify and handle edge cases: same row, same column, and same position
- Predict the total number of steps for a given start and destination

## Key Concepts
- **Manhattan Distance**: The total number of grid steps between two points when you can only move along rows and columns (no diagonals). Calculated as |row difference| + |column difference|.
- **Grid Position**: A location on the grid represented as a tuple (row, column), where (0, 0) is the top-left corner
- **Rows First, Then Columns**: The strategy of completing all row movement before starting any column movement -- this gives a predictable, L-shaped path
- **Path**: The ordered list of grid positions the robot will move to. The starting position is NOT included (the robot is already there). For the same-position case, the path is an empty list `[]`.
- **Tuple Unpacking**: Extracting values from a tuple into separate variables: `current_row, current_col = start`
- **Edge Case**: A special situation that needs consideration -- such as when the start and destination share the same row, same column, or are the same position entirely

## Materials Required
- Grid worksheets (4x4 or 5x5 grids with labeled rows and columns) for paper tracing
- Pencils and colored markers/pens for tracing paths
- Whiteboard or projector for demonstrations
- Computers with Python for coding (Parts 1 and 2)
- Reference: A map of Manhattan, NYC (optional, for the hook)
- Solution file: `code/solutions/lesson-04-manhattan-algorithm.py`

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

### Paper Tracing (10 minutes)
**For 50-min classes:** 8 min
**For 3-hour sessions:** 12 min

Before writing any code, students trace a few paths by hand to build intuition for the algorithm.

1. **Example 1: (0,0) to (2,3)** -- positive directions only
   - Draw the grid on the board. Mark (0,0) as START and (2,3) as DESTINATION.
   - Walk through the algorithm: move rows first (down to row 2), then columns (right to column 3).
   - The robot is already at (0,0), so the path lists only the positions it moves TO:
     - Row moves: (1,0), (2,0)
     - Column moves: (2,1), (2,2), (2,3)
   - **Path: [(1,0), (2,0), (2,1), (2,2), (2,3)]**
   - Trace this on the grid with arrows. Count: 5 steps = `len(path)`.
   - Manhattan distance: |2-0| + |3-0| = 5 steps. It matches!

2. **Example 2: (2,3) to (0,1)** -- negative directions
   - Mark (2,3) as START and (0,1) as DESTINATION.
   - Row moves (up): (1,3), (0,3)
   - Column moves (left): (0,2), (0,1)
   - **Path: [(1,3), (0,3), (0,2), (0,1)]**
   - Key observation: This time the robot moves to smaller row and column numbers.

3. **Quick edge case: (1,1) to (1,1)** -- same position
   - No row moves needed. No column moves needed.
   - **Path: []** -- empty list. The robot is already there. Zero steps.

4. **The Algorithm in Plain English**:
   - Write on the board:
     ```
     1. While you are not in the correct row:
          Move one step toward the destination row.
          Add the new position to the path.
     2. While you are not in the correct column:
          Move one step toward the destination column.
          Add the new position to the path.
     3. Return the path.
     ```

### Guided Practice -- Part 1: Positive Directions (15 minutes)
**For 50-min classes:** 12 min
**For 3-hour sessions:** 20 min

Students write a `compute_path()` function that handles south/east movement (positive directions only).

1. **Set up the function**:
   - Students create a new Python file.
   - Walk through the structure together:
     ```python
     def compute_path(start, end):
         path = []
         current_row, current_col = start
         dest_row, dest_col = end

         # Move south (rows increase)
         while current_row < dest_row:
             current_row = current_row + 1
             path.append((current_row, current_col))

         # Move east (columns increase)
         while current_col < dest_col:
             current_col = current_col + 1
             path.append((current_row, current_col))

         return path
     ```

2. **Explain the key ideas**:
   - **Tuple unpacking**: `current_row, current_col = start` pulls the two values out of the tuple into separate variables. Same for `dest_row, dest_col = end`.
   - **`path = []`**: The path starts empty. The robot is already at its starting position, so we do not include it.
   - **Two while loops**: The first moves south (row increases), the second moves east (column increases). Each loop appends the new position after moving.
   - **`len(path)` is the number of steps**. No need to subtract 1 because the start is not in the path.

3. **Write a main program to test**:
   ```python
   print("===== Part 1: Positive Directions =====")
   path = compute_path((0, 0), (2, 3))
   print("(0,0) to (2,3):", path)

   path = compute_path((1, 1), (3, 4))
   print("(1,1) to (3,4):", path)
   ```

4. **Run and verify**:
   - `(0,0) to (2,3)` should produce `[(1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]` -- 5 steps
   - `(1,1) to (3,4)` should produce `[(2, 1), (3, 1), (3, 2), (3, 3), (3, 4)]` -- 5 steps
   - Compare to the hand-traced paths from earlier.

5. **Reveal the limitation**:
   - Ask: "What happens if we call `compute_path((3, 3), (1, 0))`?"
   - It returns `[]` -- an empty path! The robot thinks it has nowhere to go.
   - Why? Because `3 < 1` is False and `3 < 0` is False, so neither while loop executes.
   - We need to handle north and west movement too.

### Guided Practice -- Part 2: All Directions (10 minutes)
**For 50-min classes:** 8 min
**For 3-hour sessions:** 15 min

Students extend the function to handle all four directions.

1. **The fix: Add two more while loops**:
   - No if/else statements needed. Just add loops for north and west. Only the relevant loops will execute -- the others will be skipped automatically because their condition is False.
   ```python
   def compute_path(start, end):
       path = []
       current_row, current_col = start
       dest_row, dest_col = end

       # Move south (rows increase)
       while current_row < dest_row:
           current_row = current_row + 1
           path.append((current_row, current_col))

       # Move north (rows decrease)
       while current_row > dest_row:
           current_row = current_row - 1
           path.append((current_row, current_col))

       # Move east (columns increase)
       while current_col < dest_col:
           current_col = current_col + 1
           path.append((current_row, current_col))

       # Move west (columns decrease)
       while current_col > dest_col:
           current_col = current_col - 1
           path.append((current_row, current_col))

       return path
   ```

2. **Explain why this works**:
   - For any given trip, at most ONE row loop and ONE column loop will execute. The other two will be skipped.
   - Example: going from (3,3) to (1,0), the south loop is skipped (3 is not < 1), the north loop runs (3 > 1), the east loop is skipped (0 is not < 0 after north moves), the west loop runs (3 > 0).
   - If the start and destination are the same, ALL four loops are skipped, and the path is `[]`.

3. **Test all directions**:
   ```python
   print("===== Part 2: All Directions =====")
   path = compute_path((0, 0), (2, 3))
   print("(0,0) to (2,3):", path)

   path = compute_path((3, 3), (1, 0))
   print("(3,3) to (1,0):", path)

   path = compute_path((1, 3), (3, 1))
   print("(1,3) to (3,1):", path)
   ```

### Independent Practice (10 minutes)
**For 50-min classes:** 8 min
**For 3-hour sessions:** 15 min

Students add more test cases to their main program and verify the output.

1. **Add edge case tests**:
   - Same row: `compute_path((2, 0), (2, 3))` -- expected: `[(2, 1), (2, 2), (2, 3)]`
   - Same column: `compute_path((0, 2), (3, 2))` -- expected: `[(1, 2), (2, 2), (3, 2)]`
   - Same position: `compute_path((1, 1), (1, 1))` -- expected: `[]`

2. **Print the number of steps for each path**:
   - Add `print("Steps:", len(path))` after each test.
   - Verify that `len(path)` equals the Manhattan distance for each case.

3. **Challenge problems**:
   - `compute_path((3, 0), (0, 3))` -- moving north and east
   - `compute_path((0, 3), (3, 0))` -- moving south and west
   - Verify these two paths have the same number of steps (6) but visit different positions.

4. **Verify against paper traces**:
   - Compare the output of Part 2 to the hand-traced paths from the paper tracing section. They should match exactly.

## Assessment

**Formative (during lesson)**:
- Can students trace a path on paper before writing code?
- Can students explain what tuple unpacking does in the function?
- Can students write the two while loops for Part 1 correctly?
- Can students explain why Part 1 fails for negative directions?
- Can students add the north/west loops for Part 2 without using if/else?
- Can students identify what happens in edge cases (same row, same column, same position)?

**Summative (worksheet/exit ticket)**:
1. What is Manhattan distance? Why is it called that?
2. Given start (1,3) and end (3,1), which of the four while loops in `compute_path()` will execute? Which will be skipped?
3. What does `compute_path((0, 0), (2, 3))` return? How many steps is that?
4. What does `compute_path((2, 2), (2, 2))` return? Explain why.
5. Why does the path NOT include the starting position?

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "The robot can move diagonally on the grid" | The robot can only move along rows or columns, one step at a time. Diagonal movement is not possible on a grid -- that is the whole point of Manhattan distance. |
| "The path should include the starting position" | The path only contains positions the robot moves TO. It is already at the start, so the start is not included. For same-position, the path is `[]`. Steps = `len(path)`. |
| "You need if/else to handle all four directions" | Four separate while loops handle all directions without any if/else. For any trip, at most one row loop and one column loop will execute. The others are automatically skipped because their condition is False from the start. |
| "Rows first, then columns is the only valid strategy" | You could also do columns first, then rows. Or alternate. We chose rows first because it is simple and consistent. Any strategy that avoids diagonals will give a valid Manhattan path. |
| "Same position means the algorithm is broken" | When start equals destination, all four while loops are skipped. The path is `[]` -- an empty list meaning zero steps. This is correct behavior, not a bug. |
| "Manhattan distance counts the number of positions in the path" | Manhattan distance equals `len(path)` -- the number of steps. Since the starting position is not in the path, there is no need to subtract 1. |

## Differentiation

**For struggling students**:
- Spend more time on paper tracing before opening the computer
- Provide the Part 1 function with blanks to fill in (the while condition, the append line)
- Focus on just Part 1 first -- make sure south/east works before adding north/west
- Use colored markers on the grid: one color for row moves, another for column moves
- Pair with a partner for the coding practice
- Provide the algorithm steps as a printed reference card

**For advanced students**:
- Calculate the Manhattan distance for each test case and verify it equals `len(path)`
- Consider: What if we did "columns first, then rows" instead? How would the paths differ? Would the total distance change?
- Challenge: Could you write Part 2 with only 2 while loops instead of 4? (Hint: use a step variable of +1 or -1)
- Challenge: How many DIFFERENT Manhattan paths exist between two points? (For a 2x3 path, there are C(5,2) = 10 different paths)
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
1     Row +1          (1,0)      [(1,0)]
2     Row +1          (2,0)      [(1,0), (2,0)]
3     Col +1          (2,1)      [(1,0), (2,0), (2,1)]
4     Col +1          (2,2)      [(1,0), (2,0), (2,1), (2,2)]
5     Col +1          (2,3)      [(1,0), (2,0), (2,1), (2,2), (2,3)]

Manhattan distance: |2-0| + |3-0| = 5 steps
Path length: len(path) = 5 steps
```

### Example Path Trace: (2,3) to (0,1)
```
Step  Action          Position   Path So Far
---   ------          --------   -----------
1     Row -1          (1,3)      [(1,3)]
2     Row -1          (0,3)      [(1,3), (0,3)]
3     Col -1          (0,2)      [(1,3), (0,3), (0,2)]
4     Col -1          (0,1)      [(1,3), (0,3), (0,2), (0,1)]

Manhattan distance: |0-2| + |1-3| = 4 steps
Path length: len(path) = 4 steps
```

### Part 1: Positive Directions Only
```python
def compute_path(start, end):
    path = []
    current_row, current_col = start
    dest_row, dest_col = end

    # Move south (rows increase)
    while current_row < dest_row:
        current_row = current_row + 1
        path.append((current_row, current_col))

    # Move east (columns increase)
    while current_col < dest_col:
        current_col = current_col + 1
        path.append((current_row, current_col))

    return path


print("===== Part 1: Positive Directions =====")
path = compute_path((0, 0), (2, 3))
print("(0,0) to (2,3):", path)

path = compute_path((1, 1), (3, 4))
print("(1,1) to (3,4):", path)
```

### Part 2: All Directions
```python
def compute_path(start, end):
    path = []
    current_row, current_col = start
    dest_row, dest_col = end

    # Move south (rows increase)
    while current_row < dest_row:
        current_row = current_row + 1
        path.append((current_row, current_col))

    # Move north (rows decrease)
    while current_row > dest_row:
        current_row = current_row - 1
        path.append((current_row, current_col))

    # Move east (columns increase)
    while current_col < dest_col:
        current_col = current_col + 1
        path.append((current_row, current_col))

    # Move west (columns decrease)
    while current_col > dest_col:
        current_col = current_col - 1
        path.append((current_row, current_col))

    return path


print("===== Part 2: All Directions =====")
path = compute_path((0, 0), (2, 3))
print("(0,0) to (2,3):", path)

path = compute_path((3, 3), (1, 0))
print("(3,3) to (1,0):", path)

path = compute_path((1, 3), (3, 1))
print("(1,3) to (3,1):", path)

# Edge cases
path = compute_path((2, 0), (2, 3))
print("(2,0) to (2,3):", path)

path = compute_path((0, 2), (3, 2))
print("(0,2) to (3,2):", path)

path = compute_path((1, 1), (1, 1))
print("(1,1) to (1,1):", path)
```

### Worksheet Template (for Paper Tracing)
For each problem, students should fill in:
```
Start: (__, __)    Destination: (__, __)

Row moves (which direction?):
  Move to: (__, __)
  Move to: (__, __)
  (continue as needed)
  Row matches destination -- stop row moves

Column moves (which direction?):
  Move to: (__, __)
  Move to: (__, __)
  (continue as needed)
  Column matches destination -- stop column moves

Complete path: [                                          ]
Steps: len(path) = ___
Manhattan distance: |___| + |___| = ___
```

## Teaching Notes
- **Paper tracing comes first, but coding is the main activity.** Students hand-trace a few paths to build intuition, then spend most of the lesson writing and testing `compute_path()`. The paper work is quick and targeted -- just enough to understand the algorithm before implementing it.
- **Draw big grids.** Use the entire whiteboard for the paper tracing phase. Have students come up and trace paths with markers. The physical act of drawing the path builds understanding.
- **The Manhattan name sticks.** Students remember the algorithm better when they connect it to the real-world grid of NYC streets. If possible, show an actual map of Manhattan.
- **Start with Part 1 only.** Getting the two south/east while loops working first gives students a quick win. Then revealing the limitation (negative directions return empty paths) motivates the Part 2 extension naturally.
- **Emphasize that no if/else is needed.** The elegance of four separate while loops is that only the relevant ones execute. Students who have seen if/else may try to use it -- redirect them to the simpler approach.
- **Tuple unpacking is new for many students.** Take time to explain `current_row, current_col = start`. Show that it is equivalent to `current_row = start[0]` and `current_col = start[1]` but cleaner.
- **The path does NOT include the start.** This is a deliberate design choice: the robot is already at the starting position, so the path only lists where it needs to move. This means `len(path)` directly gives the number of steps with no subtraction needed.
- **Watch for row/column confusion.** Some students will mix up rows and columns. Reinforce: rows go across (horizontal, like rows of desks), columns go up and down (vertical, like columns on a building). On our grid, the first number is the row, the second is the column.
- **Do not skip the edge cases.** Students need to see that the algorithm handles same-row, same-column, and same-position naturally. These are not special cases -- the while loops simply do not execute when there is no movement needed.

## Connections to Next Lessons
- **Lesson 5** will introduce the `Manhattan` class that wraps `compute_path()` as a method and adds heading-based navigation logic. The function students wrote today becomes the core of that class.
- **Lesson 6** will focus on testing the `Manhattan` class without a robot -- students will compare their code output directly to the paths from this lesson.
- **Later lessons** in Module 4 will connect the computed path to actual robot movement on the physical grid.
