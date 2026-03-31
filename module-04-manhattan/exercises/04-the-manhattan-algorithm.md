# Exercise 4: The Manhattan Algorithm — Paper First

**Starter code:** `code/starter/lesson-04-manhattan-algorithm.py`

## Overview

Before writing code to compute paths, you will **trace the Manhattan algorithm by hand** for several start/destination pairs, then record your answers in the starter file.

## The Algorithm

1. Start at the current position.
2. Move along **rows** until you reach the destination row (south if the destination row is larger, north if smaller).
3. Move along **columns** until you reach the destination column (east if the destination column is larger, west if smaller).

Rows first, then columns. Always.

## What You Will Do

### Worked Example
Read through the example trace in the starter code: `(0, 0)` to `(2, 3)`.
- Row movement: south from row 0 to row 2.
- Column movement: east from column 0 to column 3.
- Full path: `[(0,0), (1,0), (2,0), (2,1), (2,2), (2,3)]`

### Exercise 1: Trace (1, 1) to (3, 4)
- Determine the row direction (south) and column direction (east).
- Write out every position in the path.
- Type the path into the starter code.

### Exercise 2: Trace (3, 3) to (1, 0)
- The robot moves **north** and **west** this time.
- Write the full path.

### Exercise 3: Trace (0, 2) to (3, 2)
- The column is already correct — the robot only moves along rows.
- What happens to the column loop?

### Exercise 4: Trace (2, 0) to (2, 4)
- The row is already correct — the robot only moves along columns.
- What happens to the row loop?

### Exercise 5: How Many Steps?
- Count the steps for each path above (steps = length of path minus 1).
- Verify that the step count matches the Manhattan distance.

## Key Concepts

- The algorithm always moves **rows first**, then **columns**.
- When the start and destination share the same row, only column movement happens.
- When they share the same column, only row movement happens.
- The number of steps always equals the **Manhattan distance**.

## When You Are Done

- Do all your step counts match the Manhattan distance?
- Can you explain why the algorithm works correctly even when start and destination are in the same row or same column?
- You are now ready to turn this algorithm into code in Lesson 5.
