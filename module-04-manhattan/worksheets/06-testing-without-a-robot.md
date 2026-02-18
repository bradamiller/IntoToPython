# Lesson 6 Worksheet: Testing Without a Robot

**Name:** ________________________
**Date:** ________________________

---

## Part 1: Write the Expected Output

For each test case, use your hand-tracing skills from Lesson 4 to write the expected path. Then leave the "Actual Output" column blank -- you will fill it in when you run your code.

**Test Case 1: Basic forward path**
- Start: (0, 0) &nbsp;&nbsp; Destination: (2, 3)

| | Path |
|---|---|
| **Expected:** | ________________________________________________ |
| **Actual:** | ________________________________________________ |

**Expected number of steps:** __________

**Does expected match actual?** PASS / FAIL

---

**Test Case 2: Reverse direction**
- Start: (2, 3) &nbsp;&nbsp; Destination: (0, 0)

| | Path |
|---|---|
| **Expected:** | ________________________________________________ |
| **Actual:** | ________________________________________________ |

**Expected number of steps:** __________

**Does expected match actual?** PASS / FAIL

---

**Test Case 3: Same row (column movement only)**
- Start: (1, 0) &nbsp;&nbsp; Destination: (1, 3)

| | Path |
|---|---|
| **Expected:** | ________________________________________________ |
| **Actual:** | ________________________________________________ |

**Expected number of steps:** __________

**Does expected match actual?** PASS / FAIL

---

**Test Case 4: Same position (no movement)**
- Start: (2, 2) &nbsp;&nbsp; Destination: (2, 2)

| | Path |
|---|---|
| **Expected:** | ________________________________________________ |
| **Actual:** | ________________________________________________ |

**Expected number of steps:** __________

**Does expected match actual?** PASS / FAIL

---

## Part 2: What Does Each Test Cover?

Match each test case to the edge case or scenario it is designed to check:

| Test Case | What It Tests |
|---|---|
| Test 1: (0,0) to (2,3) | __________________________________ |
| Test 2: (2,3) to (0,0) | __________________________________ |
| Test 3: (1,0) to (1,3) | __________________________________ |
| Test 4: (2,2) to (2,2) | __________________________________ |

**Choose from:** Both row and column movement (positive steps) / Both row and column movement (negative steps) / Column-only movement (same row) / No movement (same position)

**Is there a scenario that is NOT covered by these four tests?** YES / NO

**If yes, what is it?** ____________________________________________________________________

---

## Part 3: Understanding the Test Code

Here is a test function. Read it carefully and answer the questions below.

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

1. **What does the `test_name` parameter do?**

   ____________________________________________________________________

2. **What does `actual == expected` compare?**

   ____________________________________________________________________

3. **When a test FAILS, what extra information is printed? Why is this helpful?**

   ____________________________________________________________________

4. **Predict the output of this call:**

```python
run_test("Test A", (0, 0), (1, 1),
         [(0, 0), (1, 0), (1, 1)])
```

**Output:** ____________________________________________________________________

5. **Predict the output of this call (with a WRONG expected value on purpose):**

```python
run_test("Test B", (0, 0), (1, 1),
         [(0, 0), (0, 1), (1, 1)])
```

**Output:**

Line 1: ____________________________________________________________________

Line 2: ____________________________________________________________________

Line 3: ____________________________________________________________________

---

## Part 4: Design Your Own Test Cases

Design 2 new test cases that cover scenarios NOT already tested in Part 1.

**Your Test Case 5:**

- Description of what this tests: ____________________________________
- Start: (_____, _____)
- Destination: (_____, _____)
- Expected path: ________________________________________________________
- Expected number of steps: __________

---

**Your Test Case 6:**

- Description of what this tests: ____________________________________
- Start: (_____, _____)
- Destination: (_____, _____)
- Expected path: ________________________________________________________
- Expected number of steps: __________

---

## Part 5: Checking Path Properties

A correct Manhattan path has four properties. For each property, explain how you would check it:

| Property | How to Check |
|---|---|
| Path starts at the correct position | Compare `path[_____]` to __________ |
| Path ends at the destination | Compare `path[_____]` to __________ |
| Number of steps equals Manhattan distance | `len(path) - 1` should equal __________ |
| Each step moves exactly one row OR one column | For every pair of consecutive positions, the difference should be __________ |

---

## Part 6: Testing Checklist

Before you put code on a robot, check off each item:

- [ ] Test with both row_step and col_step positive (down-right)
- [ ] Test with both row_step and col_step negative (up-left)
- [ ] Test with row_step positive and col_step negative (down-left)
- [ ] Test with row_step negative and col_step positive (up-right)
- [ ] Test with same row (column movement only)
- [ ] Test with same column (row movement only)
- [ ] Test with same position (no movement)
- [ ] All paths start at the correct position
- [ ] All paths end at the correct destination
- [ ] All step counts match the Manhattan distance

**How many of these tests pass?** _____ / 10

---

## Part 7: Debugging Practice

A student wrote this test and got a FAIL. Read the output and figure out what went wrong.

**Test output:**
```
Test: (3, 0) to (1, 2) - FAIL
  Expected: [(3, 0), (2, 0), (1, 0), (1, 1), (1, 2)]
  Actual:   [(3, 0), (2, 0), (1, 0), (0, 0), (-1, 0), (-2, 0)...
```

1. **What is the problem? The path keeps going instead of stopping.**

   ____________________________________________________________________

2. **Which loop is causing the problem -- the row loop or the column loop?**

   ____________________________________________________________________

3. **What mistake in the code would cause this? (Hint: think about the while condition)**

   ____________________________________________________________________

---

## Reflection

**Professional software developers write tests BEFORE running code on real hardware. Why is "test on screen before you test on the floor" a good strategy for robotics?**

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

---

**Next Lesson:** We'll tackle the challenge of **turning** -- the robot needs to face the right direction before it can drive to the next coordinate!
