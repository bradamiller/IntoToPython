# Lesson 6: Testing Without a Robot

## Overview
Students learn why and how to test their Manhattan algorithm without a physical robot. The core idea is separation of concerns: the Manhattan class computes a path using pure math — no motors, no sensors, no hardware. That means students can verify their algorithm is correct by running it on any computer and comparing the output against hand-calculated expected paths. This lesson introduces a systematic testing approach using print statements, expected-vs-actual comparison, and a reusable `run_test()` helper function.

Testing without hardware is a professional software engineering practice. By catching bugs on screen before deploying to the robot, students save enormous time and frustration. A robot driving into a wall tells you something is wrong but not what or where. A failing test case on screen tells you exactly which input produced the wrong output and lets you add print statements to trace the logic step by step.

## Learning Objectives
By the end of this lesson, students will be able to:
- Explain why testing without hardware is faster and more effective than debugging on the robot
- Describe separation of concerns: algorithm logic vs. physical driving
- Write test programs that create a Manhattan object and print computed paths
- Compare expected output (hand-calculated) against actual output (from code)
- Design systematic test cases that cover all directions and edge cases
- Use a `run_test()` helper function to organize multiple tests
- Debug failing tests by adding print statements inside their code

## Key Concepts
- **Testing without hardware**: Running and verifying algorithm code on a computer without connecting to or using the physical robot
- **Separation of concerns**: The Manhattan class computes paths (pure math); the Navigator class drives the robot (hardware). Each can be tested independently.
- **Expected vs. actual**: Writing down what the output should be before running the code, then comparing it to what the code actually produces
- **Test case**: A specific input paired with its known correct output, used to verify that code works correctly
- **Edge case**: An unusual or boundary input that might break the code — such as start equals destination, or movement in only one direction
- **run_test() helper**: A reusable function that automates the compare-and-report pattern for each test case

## Materials Required
- Computers with Python/Thonny installed
- Students' completed Manhattan class from Lesson 5
- Students' completed grid worksheets from Lesson 1 (for hand-tracing expected paths)
- Projector or shared screen for live coding
- Slide deck: `slides/06-testing-without-a-robot-outline.md`

## Lesson Flow

### Introduction (5 minutes)

1. **Hook: Would You Fly an Untested Airplane?**
   - Ask: "Would a pilot fly a brand-new airplane without testing it on the ground first?"
   - Of course not — engineers test engines on the ground, run simulations, and check every system before takeoff
   - Same principle applies to robots: test the algorithm with print statements first, verify the math is correct, THEN put it on the robot
   - Today's motto: "Test on screen before you test on the floor."

2. **The Separation of Concerns**
   - Two separate problems:

     | Problem | Where it runs | What to test |
     |---|---|---|
     | Computing the path | Any computer | Does the path make sense? |
     | Driving the path | On the robot | Does the robot follow correctly? |

   - The Manhattan class computes paths — no motors needed:
     ```python
     manhattan = Manhattan((0, 0))
     path = manhattan.compute_path((2, 3))
     print(path)   # Just prints — no robot required!
     ```
   - Benefit: Fix algorithm bugs BEFORE the robot drives into a wall

### Guided Practice (20 minutes)

1. **Writing a Basic Test** (5 minutes)
   - Live code together:
     ```python
     manhattan = Manhattan((0, 0))

     # Test 1: Basic forward path
     path = manhattan.compute_path((2, 3))
     print("Test 1 - (0,0) to (2,3):")
     print("  Path:", path)
     print("  Steps:", len(path) - 1)
     print()
     ```
   - What to check:
     1. Does the path start at the correct position?
     2. Does the path end at the destination?
     3. Is the number of steps correct (Manhattan distance)?
     4. Does each step move exactly one row or one column?

2. **Expected vs. Actual Comparison** (5 minutes)
   - Hand-trace the path from (0,0) to (2,3): go down 2 rows, then right 3 columns
   - Expected: `[(0,0), (1,0), (2,0), (2,1), (2,2), (2,3)]`
   - Live code the comparison:
     ```python
     expected = [(0,0), (1,0), (2,0), (2,1), (2,2), (2,3)]

     manhattan = Manhattan((0, 0))
     actual = manhattan.compute_path((2, 3))

     if actual == expected:
         print("Test 1: PASS")
     else:
         print("Test 1: FAIL")
         print("  Expected:", expected)
         print("  Actual:  ", actual)
     ```
   - Key insight: "This is the core of testing — you decide what the answer SHOULD be, then check whether the code agrees."

3. **The run_test() Helper Function** (5 minutes)
   - The comparison pattern repeats for every test, so wrap it in a function:
     ```python
     def run_test(test_name, start, dest, expected):
         manhattan = Manhattan(start)
         actual = manhattan.compute_path(dest)
         if actual == expected:
             print(test_name, "- PASS")
         else:
             print(test_name, "- FAIL")
             print("  Expected:", expected)
             print("  Actual:  ", actual)
     ```
   - Now each test is a single function call:
     ```python
     run_test("Test 1: Basic forward",
              (0, 0), (2, 3),
              [(0,0), (1,0), (2,0), (2,1), (2,2), (2,3)])
     ```

4. **Systematic Test Cases** (5 minutes)
   - Walk through the test case table together, hand-calculating each expected path:

     | Test | Start | Dest | What it tests |
     |---|---|---|---|
     | Forward right | (0,0) | (2,3) | Basic case — down then right |
     | Backward left | (2,3) | (0,0) | Reverse direction — up then left |
     | Same row | (1,0) | (1,3) | Column movement only |
     | Same column | (0,2) | (3,2) | Row movement only |
     | Same spot | (1,1) | (1,1) | No movement — edge case |
     | One step | (0,0) | (0,1) | Minimal path |

   - Ask students to hand-trace the expected path for "Backward left" before seeing the answer
   - Emphasize: "Every direction and edge case should have a test. If you only test (0,0) to (2,3), you might miss a bug that only appears when going backward."

### Independent Practice (20 minutes)

**Exercise 1: Write the Test Suite**
- Goal: Create a test file with at least 6 test cases for the Manhattan class
- Steps:
  1. Create a new file called `test_manhattan.py`
  2. Copy the Manhattan class into it (or import it)
  3. Write the `run_test()` helper function
  4. Write at least 6 test cases using the table from Guided Practice
  5. Hand-calculate the expected path for each test before writing the code
  6. Run all tests and verify they all pass
- Success criteria: All 6 tests print "PASS"

**Exercise 2: Debug a Failing Test**
- Goal: Practice using print statements to find and fix a bug
- Steps:
  1. If any tests fail, add print statements inside `compute_path()` to trace the logic:
     ```python
     print("Computing path from", self.position, "to", destination)
     print("Row step:", row_step)
     print("Col step:", col_step)
     ```
  2. Run the failing test again and read the trace output
  3. Identify the bug and fix it
  4. Re-run all tests to confirm the fix did not break anything else
- If all tests pass on the first try: Intentionally introduce a bug (e.g., change `+1` to `-1` in `row_step`) and verify that the test catches it, then fix it

**Exercise 3: Add More Edge Cases** (Challenge)
- Goal: Think of additional test scenarios beyond the basic 6
- Ideas:
  1. Start at a corner and go to the opposite corner: (0,0) to (3,3)
  2. Start from a non-origin position: (1,2) to (3,0)
  3. A path that only goes up (decreasing row)
  4. A path that only goes left (decreasing column)
- Write the tests, hand-calculate expected paths, and verify

### Assessment

**Formative (during lesson)**:
- Can students hand-calculate an expected path before running the code?
- Can students write a test that compares expected and actual output?
- Can students use the `run_test()` helper function correctly?
- Can students add print statements to debug a failing test?

**Summative (exit ticket)**:
1. Why is it better to test the Manhattan algorithm on screen before putting it on the robot?
2. What does "separation of concerns" mean in the context of this project?
3. Write a test case for Manhattan starting at (1, 1) going to (3, 2). What is the expected path?
4. Your test shows the actual path is `[(0,0), (1,0), (2,0), (2,1)]` but the expected path is `[(0,0), (1,0), (2,0), (2,1), (2,2), (2,3)]`. What might be wrong?
5. Why is it important to test edge cases like "same position" or "one step"?

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "Testing is a waste of time — just run it on the robot" | Testing on screen is much faster. You can run 6 tests in seconds. Placing the robot, running it, and watching it fail takes minutes per attempt — and a wrong path does not tell you which line of code is broken. |
| "If one test passes, the code is correct" | One passing test only proves the code works for that specific input. Bugs often hide in reverse directions, edge cases, or unusual inputs. You need multiple tests covering different scenarios. |
| "The expected path is whatever the code outputs" | The expected path must be calculated by hand BEFORE running the code. If you just copy what the code produces, you are not testing anything — you are assuming the code is correct. |
| "Print statements are messy and unprofessional" | Print-based testing is a legitimate and effective technique, especially for learning. Professional developers use similar patterns (assertions, unit tests) that are just more formalized versions of the same idea. |
| "If the path looks right on screen, the robot will work perfectly" | A correct path guarantees the algorithm is right, but the robot may still have turning or distance calibration issues. Testing on screen eliminates algorithm bugs, and testing on the robot handles hardware bugs — both are needed. |

## Differentiation

**For struggling students**:
- Provide the `run_test()` function pre-written so students only need to fill in test cases
- Give students a worksheet with the test table and blank "Expected Path" columns to fill in by hand before coding
- Start with just 3 test cases (basic forward, same row, same spot) and add more once those pass
- Pair with a partner who has a working Manhattan class if the student's own class has bugs

**For advanced students**:
- Challenge: Write a `run_all_tests()` function that counts total passes and failures and prints a summary at the end
- Challenge: Write a test that automatically checks each step in the path moves exactly one row or one column (not both, not zero)
- Explore: Research what "unit testing" means in professional software development and how Python's `assert` statement works
- Challenge: Generate test cases programmatically — loop through all pairs of corners on a 4x4 grid and test each one

## Materials & Code Examples

### Basic Test Structure
```python
manhattan = Manhattan((0, 0))

# Test 1: Basic forward path
path = manhattan.compute_path((2, 3))
print("Test 1 - (0,0) to (2,3):")
print("  Path:", path)
print("  Steps:", len(path) - 1)
print()
```

### Expected vs. Actual Comparison
```python
# Expected path (hand-calculated)
expected = [(0,0), (1,0), (2,0), (2,1), (2,2), (2,3)]

# Actual path (from code)
manhattan = Manhattan((0, 0))
actual = manhattan.compute_path((2, 3))

# Compare
if actual == expected:
    print("Test 1: PASS")
else:
    print("Test 1: FAIL")
    print("  Expected:", expected)
    print("  Actual:  ", actual)
```

### Reusable run_test() Helper
```python
def run_test(test_name, start, dest, expected):
    manhattan = Manhattan(start)
    actual = manhattan.compute_path(dest)
    if actual == expected:
        print(test_name, "- PASS")
    else:
        print(test_name, "- FAIL")
        print("  Expected:", expected)
        print("  Actual:  ", actual)
```

### Complete Test Suite
```python
# Test 1: Basic forward path
run_test("Test 1: Forward right",
         (0, 0), (2, 3),
         [(0,0), (1,0), (2,0), (2,1), (2,2), (2,3)])

# Test 2: Reverse direction
run_test("Test 2: Backward left",
         (2, 3), (0, 0),
         [(2,3), (1,3), (0,3), (0,2), (0,1), (0,0)])

# Test 3: Same row — column movement only
run_test("Test 3: Same row",
         (1, 0), (1, 3),
         [(1,0), (1,1), (1,2), (1,3)])

# Test 4: Same column — row movement only
run_test("Test 4: Same column",
         (0, 2), (3, 2),
         [(0,2), (1,2), (2,2), (3,2)])

# Test 5: Same position — no movement
run_test("Test 5: Same spot",
         (1, 1), (1, 1),
         [(1,1)])

# Test 6: One step
run_test("Test 6: One step",
         (0, 0), (0, 1),
         [(0,0), (0,1)])
```

### Debugging with Print Statements
```python
def compute_path(self, destination):
    print("Computing path from", self.position, "to", destination)
    path = [self.position]
    current_row = self.position[0]
    current_col = self.position[1]
    dest_row = destination[0]
    dest_col = destination[1]

    row_step = 1 if dest_row > current_row else -1
    col_step = 1 if dest_col > current_col else -1
    print("Row step:", row_step, "Col step:", col_step)

    while current_row != dest_row:
        current_row = current_row + row_step
        path.append((current_row, current_col))
        print("  Added:", (current_row, current_col))

    while current_col != dest_col:
        current_col = current_col + col_step
        path.append((current_row, current_col))
        print("  Added:", (current_row, current_col))

    return path
```

## Teaching Notes
- **"Test on screen before you test on the floor"**: Repeat this phrase throughout the lesson. It is the single most important habit students can build. Many students are eager to see the robot move and will resist spending time on screen-only testing. Show them that 5 minutes of testing saves 30 minutes of chasing a robot around the room.
- **Hand-calculate expected paths first**: Do not let students run their code and then copy the output as the "expected" path. The entire point of testing is to have an independent source of truth. Have students trace the path on their grid worksheet from Lesson 1 and write down the expected list of tuples before touching the keyboard.
- **Celebrate failing tests**: When a test says "FAIL", that is the test doing its job. A test that catches a bug before the robot runs is a success, not a failure. Reframe the language: "The test found a bug for you."
- **Remove debug prints after fixing**: Remind students that print statements added for debugging should be removed (or commented out) once the bug is fixed, so the output stays clean for future test runs.
- **Common bugs to watch for**: Path missing the start position, path going in the wrong direction, infinite loop when start equals destination, off-by-one errors. The slide outline (Slide 8) lists these — walk through them if students encounter issues.

## Connections to Next Lessons
- **Lesson 7** will introduce the turning challenge — now that the algorithm is tested and correct, students need to figure out how the robot should turn at each step
- **Lesson 8** will implement the Navigator class that drives the tested paths on the physical robot
- **Lesson 9** (final project) will require students to test Manhattan output for all legs of a multi-destination route before running on the robot — the testing skills from this lesson are directly applied
- The testing mindset introduced here carries forward to Module 5, where students will test Dijkstra's algorithm the same way
