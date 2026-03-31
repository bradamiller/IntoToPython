# Exercise 3: Lists — Building a Path

**Starter code:** `code/starter/lesson-03-lists.py`

## Overview

A single tuple is one position. A **list** of tuples is a **path**. In this exercise you will build paths by appending coordinates to a list, then iterate through them.

## What You Will Do

### Part 1: Creating a List
- Create an empty list called `path`.
- Print it and its length (should be `[]` and `0`).

### Part 2: Adding Positions with Append
- Use `path.append()` to add three positions: `(0, 0)`, `(1, 0)`, `(2, 0)`.
- Print the path after all appends. It should show `[(0, 0), (1, 0), (2, 0)]`.

### Part 3: Accessing Items in a List
- Print the first position using `path[0]`.
- Print the last position using `path[-1]`.

### Part 4: Iterating Through a Path
- Use a `for` loop to print each position in the path.

### Part 5: Building a Longer Path with a Loop
- Create a path that goes straight east from `(0, 0)` to `(0, 4)`.
- Use a `for` loop with `range(5)` to append `(0, col)` for each column value.

### Part 6: Building a Two-Part Path
- Build a path from `(0, 0)` going south to `(3, 0)`, then east to `(3, 2)`.
- Use two loops: one for the row changes, one for the column changes.
- Print the complete path and its length.

## Key Concepts

- A **list** is an ordered collection that can grow: `path = []`.
- **`append()`** adds an item to the end of a list.
- Access items by **index**: `path[0]` is the first, `path[-1]` is the last.
- **`len(path)`** gives the number of items.
- A **`for` loop** visits each item in a list.

## Expected Output (Parts 1–4)

```
Path: []
Length: 0
Path: [(0, 0), (1, 0), (2, 0)]
Length: 3
First position: (0, 0)
Last position: (2, 0)
  Visiting: (0, 0)
  Visiting: (1, 0)
  Visiting: (2, 0)
```

## When You Are Done

- How many positions are in your two-part path from Part 6? Does that match the Manhattan distance plus one?
- Why does the path length equal the Manhattan distance **plus one**?
