# Exercise 4: The Manhattan Algorithm

**Starter code:** `code/starter/lesson-04-manhattan-algorithm.py`

## Overview

You will write a `compute_path(start, end)` function that returns the list of grid positions the robot visits when traveling from `start` to `end`. The path does **not** include the starting position (the robot is already there). The number of steps is `len(path)`.

The algorithm: move along **rows** first, then **columns**.

## Part 1: Positive Directions Only

Write `compute_path(start, end)` with two while loops:
1. A **south** loop that increases `current_row` toward `dest_row`.
2. An **east** loop that increases `current_col` toward `dest_col`.

Start with `path = []` and use tuple unpacking to get the row and column from `start` and `end`.

### Test your function

Add these lines to your main program and run it:

```python
path = compute_path((0, 0), (2, 3))
print("(0,0) to (2,3):", path)
print("Steps:", len(path))

path = compute_path((1, 1), (3, 4))
print("(1,1) to (3,4):", path)
print("Steps:", len(path))
```

### Expected output

```
(0,0) to (2,3): [(1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]
Steps: 5
(1,1) to (3,4): [(2, 1), (3, 1), (3, 2), (3, 3), (3, 4)]
Steps: 5
```

### Check your understanding

- Why does the south loop run before the east loop?
- What would happen if you called `compute_path((3, 3), (1, 0))` with this version? Try it and explain the result.

## Part 2: All Four Directions

The Part 1 function returns `[]` for `compute_path((3, 3), (1, 0))` because neither while loop condition is True. Fix this by adding two more while loops:

3. A **north** loop that decreases `current_row` toward `dest_row`.
4. A **west** loop that decreases `current_col` toward `dest_col`.

You do **not** need any if/else statements. Only the loops whose conditions are True will execute.

### Test your function

Add these lines and run:

```python
path = compute_path((3, 3), (1, 0))
print("(3,3) to (1,0):", path)
print("Steps:", len(path))

path = compute_path((1, 3), (3, 1))
print("(1,3) to (3,1):", path)
print("Steps:", len(path))
```

### Expected output

```
(3,3) to (1,0): [(2, 3), (1, 3), (1, 2), (1, 1), (1, 0)]
Steps: 5
(1,3) to (3,1): [(2, 3), (3, 3), (3, 2), (3, 1)]
Steps: 4
```

### Test edge cases

Add these tests:

```python
path = compute_path((2, 0), (2, 3))
print("(2,0) to (2,3):", path)
print("Steps:", len(path))

path = compute_path((0, 2), (3, 2))
print("(0,2) to (3,2):", path)
print("Steps:", len(path))

path = compute_path((1, 1), (1, 1))
print("(1,1) to (1,1):", path)
print("Steps:", len(path))
```

### Expected output

```
(2,0) to (2,3): [(2, 1), (2, 2), (2, 3)]
Steps: 3
(0,2) to (3,2): [(1, 2), (2, 2), (3, 2)]
Steps: 3
(1,1) to (1,1): []
Steps: 0
```

## Key Concepts

- The path does **not** include the starting position. Steps = `len(path)`.
- The algorithm always moves **rows first**, then **columns**.
- Four while loops handle all directions — no if/else needed.
- When start and end share the same row, only column loops run.
- When they share the same column, only row loops run.
- When start equals end, all loops are skipped and the path is empty.

## When You Are Done

- Do all your step counts match the Manhattan distance (|row difference| + |col difference|)?
- Can you explain why no if/else statements are needed?
- Can you explain why the path should not include the starting position?
