# Lesson 1: Coordinates on the Grid

## Overview
Students learn how to describe positions on a grid using (row, column) coordinates. This is a conceptual lesson with no Python coding — students work with paper, pencils, and the physical grid to build a strong mental model of coordinate systems before translating that understanding into code. By the end of the lesson, students will be able to read, write, and locate any position on the grid using coordinates, setting the foundation for tuples, lists, and the Manhattan algorithm in the lessons that follow.

This lesson draws on analogies students already know — GPS coordinates, street grids, Battleship, chess — to make the abstract idea of coordinate pairs concrete. The physical grid mapping exercise is the centerpiece: students label every intersection on a real or drawn grid and answer navigation questions about it.

## Learning Objectives
By the end of this lesson, students will be able to:
- Explain what a coordinate system is and why robots need one
- Use the (row, column) convention to identify positions on a grid
- Distinguish between row (vertical position) and column (horizontal position)
- Count intersections on the physical grid to determine a robot's position
- Map every intersection on a grid to its correct coordinate pair
- Calculate how many rows and columns the robot must travel between two positions

## Key Concepts
- **Coordinate system**: A method of describing any position on a surface using an ordered pair of numbers
- **Row**: The first number in the pair — how far down from the top (row 0 is the top row)
- **Column**: The second number in the pair — how far right from the left (column 0 is the leftmost column)
- **Intersection**: The point where a row line and column line cross on the grid — each intersection is one coordinate
- **Zero-indexed**: Counting starts at 0, not 1 — the top-left corner is (0, 0), not (1, 1)

## Materials Required
- Physical grid (black tape on white surface) or large printed grid diagram
- Grid mapping worksheet (blank grid for students to label)
- Pencils and markers
- Projector or whiteboard for demonstrating coordinates
- Optional: chess board or Battleship game for analogy

## Lesson Flow

### Introduction (10 minutes)

1. **Hook: How Does a Robot Know Where It Is?**
   - Ask: "You can look around a room and tell someone where you are. How would you explain your exact position to a robot that can't see?"
   - Discussion: Draw out student ideas — landmarks, distances, directions
   - Bridge to real world: "GPS uses two numbers — latitude and longitude — to pinpoint any spot on Earth. Street addresses in cities like Manhattan use a grid: '5th Avenue and 3rd Street' is two numbers that tell you exactly where to go."
   - Reveal: "Today we're going to create a coordinate system for our robot's grid, so we can tell it exactly where it is and where to go — using just two numbers."

2. **What Is a Coordinate System?**
   - A coordinate system uses two numbers to uniquely describe any position on a flat surface
   - Examples students already know:
     - **Battleship**: "B4" means column B, row 4
     - **Chess**: "e5" means column e, row 5
     - **Spreadsheets**: cell A1, cell C7
     - **Maps**: latitude and longitude
   - Key insight: two numbers are enough to describe any position on a 2D surface
   - Our convention: **(row, column)** — row first, column second

3. **The (row, col) Convention**
   - Draw or project a 4x4 grid on the board:

     | | Col 0 | Col 1 | Col 2 | Col 3 |
     |---|---|---|---|---|
     | Row 0 | (0,0) | (0,1) | (0,2) | (0,3) |
     | Row 1 | (1,0) | (1,1) | (1,2) | (1,3) |
     | Row 2 | (2,0) | (2,1) | (2,2) | (2,3) |
     | Row 3 | (3,0) | (3,1) | (3,2) | (3,3) |

   - First number = row (how far down from the top)
   - Second number = column (how far right from the left)
   - Top-left corner is always (0, 0) — we count from zero
   - Emphasize: **(2, 3) and (3, 2) are different positions!** Order matters.

### Guided Practice (15 minutes)

1. **Reading Coordinates Together**
   - Point to positions on the projected grid and ask students to call out coordinates:
     - "What coordinate is this?" (point to row 1, column 3) -- Answer: (1, 3)
     - "What coordinate is this?" (point to row 3, column 0) -- Answer: (3, 0)
     - "What coordinate is this?" (point to row 0, column 0) -- Answer: (0, 0)
   - Reverse direction — give coordinates, students point to the position:
     - "Point to (2, 1)"
     - "Point to (0, 3)"
     - "Point to (3, 3)"

2. **Neighborhood Questions**
   - "If the robot is at (1, 2), what position is directly below it?" -- Answer: (2, 2)
   - "If the robot is at (1, 2), what position is directly to the right?" -- Answer: (1, 3)
   - "If the robot is at (0, 0), what position is one step down?" -- Answer: (1, 0)
   - "If the robot is at (3, 3), can it go further right on a 4x4 grid?" -- Answer: No, column 3 is the last column
   - Rule: Moving down increases the row. Moving right increases the column.

3. **Distance Counting**
   - "How far is it from (0, 0) to (2, 3)?"
     - Row distance: 2 - 0 = 2 rows
     - Column distance: 3 - 0 = 3 columns
     - Total intersections to cross: 2 + 3 = 5 steps
   - "How far is it from (1, 1) to (3, 2)?"
     - Row distance: 3 - 1 = 2 rows
     - Column distance: 2 - 1 = 1 column
     - Total: 2 + 1 = 3 steps
   - Explain: "This total — rows plus columns — is called the Manhattan distance. It's how many grid steps a robot must take if it can only go up, down, left, or right — no diagonals. Just like walking city blocks in Manhattan."

### Independent Practice (20 minutes)

**Exercise 1: Map the Grid**
- Goal: Label every intersection on a blank grid with its (row, col) coordinate
- Steps:
  1. Students receive a blank grid worksheet (4x4 or 5x5 depending on physical grid size)
  2. Label the top-left corner (0, 0)
  3. Fill in every remaining intersection with its correct coordinate
  4. Double-check: the bottom-right corner of a 4x4 grid should be (3, 3)
- Success criteria: Every intersection is correctly labeled with (row, col) format

**Exercise 2: Position Identification**
- Goal: Answer navigation questions using the labeled grid
- Questions:
  1. What is the coordinate of the bottom-left corner?
  2. How many total intersections are on a 4x4 grid?
  3. If the robot is at (2, 1) and moves one step right, where is it?
  4. If the robot is at (0, 3) and moves one step down, where is it?
  5. Name two positions that are in the same row but different columns
  6. Name two positions that are in the same column but different rows
  7. The robot starts at (0, 0) and needs to reach (3, 2). How many rows does it need to travel? How many columns? What is the total number of steps?

**Exercise 3: Plot the Path** (Challenge)
- Goal: Draw a path on the grid and list the coordinates visited
- Steps:
  1. Draw a path from (0, 0) to (2, 3) on the grid — only horizontal and vertical moves, no diagonals
  2. List every intersection the robot visits in order
  3. Count the total number of steps
  4. Challenge question: Is there more than one path from (0, 0) to (2, 3) that takes the same number of steps? Draw a second path if so.
- Key insight: There are multiple paths with the same length. The Manhattan algorithm will choose one specific path (rows first, then columns).

### Assessment

**Formative (during lesson)**:
- Can students correctly identify coordinates when you point to positions on the grid?
- Can students locate positions on the grid when given coordinates?
- Do students consistently put row first and column second?
- Can students calculate the distance between two positions?

**Summative (worksheet/exit ticket)**:
1. What is the coordinate of row 2, column 1 on the grid?
2. If the robot is at (1, 3), what position is directly above it?
3. Calculate the Manhattan distance from (0, 0) to (4, 2).
4. Why do we use two numbers instead of one to describe a position?
5. True or false: (2, 3) and (3, 2) are the same position. Explain your answer.

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "Row and column order doesn't matter" | Order matters! (2, 3) and (3, 2) are different positions. Our convention is always (row, column). |
| "Counting starts at 1" | We use zero-indexing: the first row is row 0, the first column is column 0. This matches how Python indexes data. |
| "Row means left-right" | Row is vertical position (how far down). Column is horizontal position (how far right). |
| "The robot can move diagonally" | On this grid, the robot follows lines and can only move up, down, left, or right — never diagonally. |
| "There's only one path between two points" | There are many paths with the same Manhattan distance. The algorithm chooses one specific route (rows first, then columns). |

## Differentiation

**For struggling students**:
- Start with a smaller 3x3 grid before moving to 4x4
- Use color coding: highlight all row-0 intersections in one color, row-1 in another
- Provide a partially filled grid and ask students to complete it
- Pair with a stronger student for the mapping exercise

**For advanced students**:
- Use a larger grid (6x6 or 8x8) for the mapping exercise
- Ask: How many total intersections on an NxN grid? (Answer: N x N)
- Challenge: How many different shortest paths exist from (0, 0) to (2, 3)? (This is a combinatorics problem)
- Research: How does GPS use coordinates? What is the difference between latitude/longitude and our (row, col) system?

## Materials & Code Examples

### Grid Diagram (for whiteboard or worksheet)
```
        Col 0    Col 1    Col 2    Col 3
         |        |        |        |
Row 0 -- * ------ * ------ * ------ *
         |        |        |        |
Row 1 -- * ------ * ------ * ------ *
         |        |        |        |
Row 2 -- * ------ * ------ * ------ *
         |        |        |        |
Row 3 -- * ------ * ------ * ------ *
```

Each `*` is an intersection with a coordinate. Students label each one.

### Distance Calculation Reference
```
From (0, 0) to (2, 3):
  Row distance:    2 - 0 = 2
  Column distance: 3 - 0 = 3
  Total steps:     2 + 3 = 5

From (1, 1) to (3, 4):
  Row distance:    3 - 1 = 2
  Column distance: 4 - 1 = 3
  Total steps:     2 + 3 = 5

From (3, 0) to (0, 2):
  Row distance:    |0 - 3| = 3
  Column distance: |2 - 0| = 2
  Total steps:     3 + 2 = 5
```

### Preview: Coordinates in Python (show but do not code)
```python
# Next lesson, we'll store these coordinates in Python:
position = (2, 3)    # This is called a "tuple"
print("Row:", position[0])
print("Col:", position[1])
```

## Teaching Notes
- **Row vs. column confusion is the #1 issue**: Repeat the convention frequently: "Row first, column second. Row is down, column is right." Consider posting this on the wall.
- **Zero-indexing is new for most students**: They are accustomed to counting from 1. Explain that Python counts from 0, so we match that convention now to avoid confusion later.
- **Physical grid is essential**: If possible, have students walk on the physical grid and call out their coordinates. Kinesthetic learning reinforces the concept far better than diagrams alone.
- **Don't rush to code**: This lesson is intentionally code-free. Students need a solid mental model of coordinates before representing them in Python. If students ask "when do we code?" tell them: "Tomorrow. Today, you're building the map the code will use."
- **Manhattan analogy**: If students have seen a map of Manhattan, show it. The streets form a grid — you can only walk along streets, not diagonally through buildings. That is exactly how our robot navigates.
- **Keep the labeled grid**: Students should save their completed grid worksheet. They will reference it throughout the module when testing coordinates and paths.

## Connections to Next Lessons
- **Lesson 2** will introduce tuples — Python's way to store a coordinate pair like (2, 3) as a single value in code
- **Lesson 3** will introduce lists — Python's way to store a sequence of coordinates as a path
- **Lesson 4** will use coordinates to build the Manhattan algorithm, which calculates a path from any start to any destination
- The (row, column) convention established here is used in every remaining lesson of Modules 4 and 5
