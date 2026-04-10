# Exercise 5: Implementing the Manhattan Class

**Starter code:** `code/starter/lesson-05-manhattan-class.py`

## Overview

In Lesson 4 you wrote a `compute_path` function with 4 while loops. Now you will wrap that function in a **class** so the robot can store its position. The algorithm does not change -- you are just moving it into a method.

## What You Will Do

### Understand the Class Structure
The `Manhattan` class has:
- `__init__(self, start)` -- stores the starting position as `self.position`.
- `compute_path(self, destination)` -- computes and returns the path as a list of tuples.

The key difference from the Lesson 4 function: `compute_path` uses `self.position` instead of a `start` parameter. The 4 while loops stay exactly the same.

### Complete compute_path()

Copy your 4 while loops from Lesson 4 into the method. Each loop handles one direction:

1. **South loop:** `while current_row < dest_row` -- add 1 to `current_row` and append the position.
2. **North loop:** `while current_row > dest_row` -- subtract 1 from `current_row` and append the position.
3. **East loop:** `while current_col < dest_col` -- add 1 to `current_col` and append the position.
4. **West loop:** `while current_col > dest_col` -- subtract 1 from `current_col` and append the position.

There is no if/else to determine direction. Each while loop only runs when its condition is true, and skips otherwise.

### Test Your Class
- Uncomment the test code at the bottom of the file.
- Run `Manhattan((0, 0)).compute_path((2, 3))` and verify the path matches your hand-traced answer from Lesson 4.
- Test with a second case: `Manhattan((3, 3)).compute_path((1, 0))`.

## Key Concepts

- A **class** bundles data (`self.position`) and behavior (`compute_path()`) together.
- Converting a function to a method: replace the `start` parameter with `self`, and use `self.position` instead.
- The path starts **empty** (`path = []`). The start position is NOT included in the path. The number of steps is `len(path)`.
- 4 separate while loops replace the need for if/else direction logic. Loops that do not apply simply skip.

## Expected Output

```
Start: (0, 0)
Destination: (2, 3)
Path: [(1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]
Steps: 5

Start: (3, 3)
Destination: (1, 0)
Path: [(2, 3), (1, 3), (1, 2), (1, 1), (1, 0)]
Steps: 5
```

## Common Mistakes

- **Including the start position in the path** -- `path` starts as `[]`, not `[self.position]`. The path only contains the positions the robot moves to.
- **Using `!=` instead of `<` and `>`** -- the 4-loop pattern uses `<` and `>` so each loop handles exactly one direction. Using `!=` with a single loop requires an if/else to pick the step direction.
- **Swapping row and column in `path.append()`** -- always use `(current_row, current_col)`, not the reverse.
- **Forgetting `self` in the method signature** -- `def compute_path(self, destination)`, not `def compute_path(destination)`.

## When You Are Done

- Test with a same-row case like `(0, 0)` to `(0, 3)`. Do the row loops run at all?
- Test with a same-position case like `(2, 2)` to `(2, 2)`. What does the path look like? How many steps?
- Compare: what is different between your Lesson 4 function and the Lesson 5 method? What stayed the same?
