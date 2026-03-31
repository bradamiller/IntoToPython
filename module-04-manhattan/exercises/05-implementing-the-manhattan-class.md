# Exercise 5: Implementing the Manhattan Class

**Starter code:** `code/starter/lesson-05-manhattan-class.py`

## Overview

You will turn the Manhattan algorithm into a reusable Python **class** with a `compute_path()` method. The class is partially written — you fill in the algorithm logic.

## What You Will Do

### Understand the Class Structure
The `Manhattan` class has:
- `__init__(self, start)` — stores the starting position as `self.position`.
- `compute_path(self, destination)` — computes and returns the path as a list of tuples.

### Complete compute_path()

The method has four TODO sections to fill in:

1. **Determine row_step:** If the destination row is greater than the current row, set `row_step = 1` (moving south). Otherwise, set `row_step = -1` (moving north).

2. **Determine col_step:** Same logic for columns. Greater = east (+1), smaller = west (-1).

3. **Row while loop:** While `current_row != dest_row`, add `row_step` to `current_row` and append the new position to the path.

4. **Column while loop:** While `current_col != dest_col`, add `col_step` to `current_col` and append the new position to the path.

### Test Your Class
- Uncomment the test code at the bottom of the file.
- Run `Manhattan((0, 0)).compute_path((2, 3))` and verify the path matches your hand-traced answer from Lesson 4.
- Test with a second destination: `(3, 1)`.

## Key Concepts

- A **class** bundles data (`self.position`) and behavior (`compute_path()`) together.
- The `while` loop is the right choice here because we don't know in advance how many steps are needed — we loop **until** we arrive.
- `path` starts with `[self.position]` so the starting position is always included.

## Expected Output

```
Start: (0, 0)
Destination: (2, 3)
Path: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]
Steps: 5

Start: (0, 0)
Destination: (3, 1)
Path: [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1)]
Steps: 4
```

## Common Mistakes

- **Forgetting to start the path with `[self.position]`** — the path will be missing the starting position.
- **Using `<` instead of `!=` in the while condition** — this breaks when the robot needs to move north or west (negative steps).
- **Swapping row and column in `path.append()`** — always use `(current_row, current_col)`, not the reverse.

## When You Are Done

- Test with a same-row case like `(0, 0)` to `(0, 3)`. Does the row loop run at all?
- Test with a same-position case like `(2, 2)` to `(2, 2)`. What does the path look like?
