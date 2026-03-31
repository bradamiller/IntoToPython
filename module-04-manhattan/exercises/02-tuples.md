# Exercise 2: Tuples — Packaging Coordinates Together

**Starter code:** `code/starter/lesson-02-tuples.py`

## Overview

Instead of using separate `row` and `col` variables, you will learn to package coordinates into a **tuple** — a single variable that holds both values together.

## What You Will Do

### Part 1: Creating Position Tuples
- Create a tuple `start` set to `(0, 0)`.
- Create a tuple `destination` set to `(2, 3)`.
- Print both tuples.

### Part 2: Accessing Row and Column
- Use indexing to print the row and column of the destination separately.
- `destination[0]` gives the row, `destination[1]` gives the column.

### Part 3: Comparing Positions
- Create a `current` variable set to `(0, 0)`.
- Use `==` to check if `current` equals `start` (should be `True`).
- Check if `current` equals `destination` (should be `False`).

### Part 4: Manhattan Distance with Tuples
- Calculate the Manhattan distance between `start` and `destination` using tuple indexing.
- Use `start[0]`, `start[1]`, `destination[0]`, `destination[1]`.

### Part 5: Multiple Destinations
- Create three destination tuples: `(1, 2)`, `(3, 1)`, and `(2, 4)`.
- Calculate and print the Manhattan distance from `start` to each one.

## Key Concepts

- A **tuple** groups values together: `position = (2, 3)`.
- Access values with **indexing**: `position[0]` is the row, `position[1]` is the column.
- Tuples are **immutable** — once created, you cannot change their values.
- You can **compare** tuples with `==`.

## Expected Output

```
Start: (0, 0)
Destination: (2, 3)
Destination row: 2
Destination col: 3
At start? True
At destination? False
Manhattan distance: 5
```

## When You Are Done

- Why is a tuple better than two separate variables for storing a coordinate?
- What happens if you try `destination[0] = 5`? Why?
