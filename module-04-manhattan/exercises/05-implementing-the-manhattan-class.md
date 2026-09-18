# Exercise 5: A Reusable Manhattan Function

**Starter code:** `code/starter/lesson-05-manhattan-function.py`

## Overview

In Lesson 4 you wrote a `compute_path` function with 4 while loops. Now you will give it a proper name -- `compute_manhattan_path` -- and a docstring, since Module 5 will introduce a second pathfinding algorithm (Dijkstra) that needs a name of its own. The algorithm does not change -- this is a rename, not a rewrite.

*Skip to the bottom of this file for the Optional Extension (wrapping the function in a class), if your course covers classes.*

## What You Will Do

### Understand the Rename
The renamed function has the same shape as Lesson 4's, with clearer names:
- `compute_path(start, end)` becomes `compute_manhattan_path(position, destination)`.
- Every line inside the function body is unchanged -- only the `def` line and the docstring are new.

### Complete compute_manhattan_path()

Copy your 4 while loops from Lesson 4 into the function body. Each loop handles one direction:

1. **South loop:** `while current_row < dest_row` -- add 1 to `current_row` and append the position.
2. **North loop:** `while current_row > dest_row` -- subtract 1 from `current_row` and append the position.
3. **East loop:** `while current_col < dest_col` -- add 1 to `current_col` and append the position.
4. **West loop:** `while current_col > dest_col` -- subtract 1 from `current_col` and append the position.

There is no if/else to determine direction. Each while loop only runs when its condition is true, and skips otherwise.

### Test Your Function (Regression Test)
- Uncomment the test code at the bottom of the file.
- Run `compute_manhattan_path((0, 0), (2, 3))` and verify the path matches your hand-traced answer from Lesson 4 -- and matches what your Lesson 4 `compute_path` function produced.
- Test with a second case: `compute_manhattan_path((3, 3), (1, 0))`.

## Key Concepts

- A specific function name matters once a program has more than one algorithm -- `compute_manhattan_path` won't collide with Module 5's Dijkstra function.
- A **docstring** is a string literal right after `def` that documents parameters and return value -- shows up in `help()` and editor tooltips.
- The path starts **empty** (`path = []`). The starting position is NOT included in the path. The number of steps is `len(path)`.
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

- **Including the start position in the path** -- `path` starts as `[]`, not `[position]`. The path only contains the positions the robot moves to.
- **Using `!=` instead of `<` and `>`** -- the 4-loop pattern uses `<` and `>` so each loop handles exactly one direction. Using `!=` with a single loop requires an if/else to pick the step direction.
- **Swapping row and column in `path.append()`** -- always use `(current_row, current_col)`, not the reverse.
- **Forgetting the docstring's triple-quotes** -- `"""..."""`, not a `#` comment.

## When You Are Done

- Test with a same-row case like `(0, 0)` to `(0, 3)`. Do the row loops run at all?
- Test with a same-position case like `(2, 2)` to `(2, 2)`. What does the path look like? How many steps?
- Compare: what is different between your Lesson 4 function and this Lesson 5 version? What stayed the same?

---

## Optional Extension: Wrap It in a Class

*Skip this section if your course doesn't cover classes.*

**Reference code:** `code/solutions/lesson-05-manhattan-class-addon.py`

Take `compute_manhattan_path(position, destination)` and repackage it as a `Manhattan` class:
- `__init__(self, start)` stores `self.position = start`
- `compute_path(self, destination)` uses `self.position` instead of the `position` parameter -- the four while loops are otherwise unchanged

Test it with `Manhattan((0, 0)).compute_path((2, 3))` and confirm the output matches the function version exactly.
