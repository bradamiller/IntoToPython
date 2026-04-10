# Exercise 6: Testing Without a Robot

**Starter code:** `code/starter/lesson-06-testing.py`

## Overview

Before putting code on the robot, you will write **test cases** that verify your Manhattan class produces correct paths. The starter code includes a `run_test()` helper function and one example test — you write five more.

## What You Will Do

### Understand the Test Helper
The `run_test()` function:
1. Creates a `Manhattan` object at the given start position.
2. Calls `compute_path()` with the given destination.
3. Compares the actual path to the expected path.
4. Prints **PASS** or **FAIL** (with details if it fails).

### Test 1 (Provided): South-East
The example test goes from `(0, 0)` to `(2, 3)`. This is already written for you — run it to make sure it passes.

### Test 2: North-West
- Go from `(3, 3)` to `(1, 0)`.
- Hand-trace the expected path first, then fill it in.
- This tests negative row and column steps.

### Test 3: Same Row
- Go from `(2, 0)` to `(2, 4)`.
- The row doesn't change — only column movement.
- This tests that the row loop correctly does nothing.

### Test 4: Same Column
- Go from `(0, 2)` to `(3, 2)`.
- The column doesn't change — only row movement.

### Test 5: Already at Destination
- Go from `(1, 1)` to `(1, 1)`.
- The path should be empty (`[]`) since the robot is already there.

### Test 6: One Step Only
- Go from `(0, 0)` to `(1, 0)`.
- The path should have exactly one position: `[(1, 0)]`.

## Key Concepts

- **Test before you deploy.** Running tests on screen catches bugs before they cause problems on the robot.
- **Edge cases** are the scenarios most likely to reveal bugs: same row, same column, same position, single step.
- A good test suite covers **all four direction combinations** plus edge cases.

## Expected Output (All Passing)

```
PASS: South-East: (0,0) to (2,3)
PASS: North-West: (3,3) to (1,0)
PASS: Same row: (2,0) to (2,4)
PASS: Same column: (0,2) to (3,2)
PASS: Already there: (1,1) to (1,1)
PASS: One step: (0,0) to (1,0)
```

## When You Are Done

- Are all 6 tests passing?
- Can you think of any scenario NOT covered by these tests?
- You are now confident the Manhattan class works — time to put it on the robot!
