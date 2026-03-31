# Exercise 1: Coordinates on the Grid

**Starter code:** `code/starter/lesson-01-coordinates.py`

## Overview

In this exercise you will use Python variables and arithmetic to describe positions on a grid using (row, column) coordinates and calculate distances between them.

## What You Will Do

### Part 1: Creating Position Variables
- Create two variables, `start_row` and `start_col`, for the robot's starting position at the top-left corner (row 0, column 0).
- Print the starting position.

### Part 2: A Destination
- Create `dest_row` and `dest_col` variables for a destination at row 2, column 3.
- Print the destination.

### Part 3: How Far Apart?
- Calculate `row_distance` by subtracting `start_row` from `dest_row`.
- Calculate `col_distance` by subtracting `start_col` from `dest_col`.
- Print both distances.

### Part 4: Total Manhattan Distance
- Add `row_distance` and `col_distance` to get the total Manhattan distance.
- Print the result. You should get **5 blocks**.

### Part 5: Try Another Destination
- Choose a new destination at row 1, column 4.
- Calculate and print the Manhattan distance from start to this new destination.

## Key Concepts

- A grid position is described by two numbers: **row** (how far down) and **column** (how far right).
- Rows and columns start at **0**, not 1.
- The **Manhattan distance** is the total number of row steps plus column steps between two positions.

## Expected Output

```
Starting position: row 0 col 0
Destination: row 2 col 3
Row distance: 2
Column distance: 3
Manhattan distance: 5 blocks
```

## When You Are Done

- Can you explain why the Manhattan distance from (0, 0) to (2, 3) is 5?
- What would the Manhattan distance be from (0, 0) to (0, 0)?
