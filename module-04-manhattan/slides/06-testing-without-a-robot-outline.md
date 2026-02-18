# Lesson 6 Slide Outline: Testing Without a Robot

## Slide 1: Title & Learning Objectives
**Title:** Testing Without a Robot

**Learning Objectives:**
- Understand why testing without hardware is important
- Write test programs that verify algorithm output
- Compare computed paths against hand-calculated expected paths
- Build confidence in code before deploying to hardware

**Agenda:**
- Why test without a robot? (5 min)
- Writing test programs (10 min)
- Systematic testing strategy (10 min)
- Practice: Test your Manhattan class (20 min)

---

## Slide 2: Hook — Would You Fly an Untested Airplane?
**Question:** "Would a pilot fly a new airplane without testing it on the ground first?"

**Of course not!**
- Test engines on the ground
- Run simulations before flying
- Check every system before takeoff

**Same with robots:**
- Test the algorithm with print statements first
- Verify the math is correct
- THEN put it on the robot

**Today's motto:** "Test on screen before you test on the floor."

---

## Slide 3: The Separation of Concerns
**Two separate problems:**

| Problem | Where it runs | What to test |
|---|---|---|
| Computing the path | Any computer | Does the path make sense? |
| Driving the path | On the robot | Does the robot follow correctly? |

**The Manhattan class computes paths — no motors needed!**

```python
manhattan = Manhattan((0, 0))
path = manhattan.compute_path((2, 3))
print(path)   # Just prints — no robot required!
```

**Benefit:** Fix algorithm bugs BEFORE the robot drives into a wall.

---

## Slide 4: Writing a Test Program
**Basic test structure:**

```python
manhattan = Manhattan((0, 0))

# Test 1: Basic forward path
path = manhattan.compute_path((2, 3))
print("Test 1 - (0,0) to (2,3):")
print("  Path:", path)
print("  Steps:", len(path) - 1)
print()
```

**What to check:**
1. Does the path start at the correct position?
2. Does the path end at the destination?
3. Is the number of steps correct (Manhattan distance)?
4. Does each step move exactly one row or one column?

---

## Slide 5: Expected vs. Actual
**Compare what you expect with what you get:**

```python
# Expected path (from hand trace)
expected = [(0,0), (1,0), (2,0), (2,1), (2,2), (2,3)]

# Actual path (from your class)
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

**This is the core of testing:** Expected output vs. actual output.

---

## Slide 6: Systematic Test Cases
**Test different scenarios:**

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

**Test cases to cover:**

| Test | Start | Dest | Tests |
|---|---|---|---|
| Forward right | (0,0) | (2,3) | Basic case |
| Backward left | (2,3) | (0,0) | Reverse direction |
| Same row | (1,0) | (1,3) | Column only |
| Same column | (0,2) | (3,2) | Row only |
| Same spot | (1,1) | (1,1) | No movement |
| One step | (0,0) | (0,1) | Minimal path |

---

## Slide 7: Debugging with Print Statements
**If a test fails, add print statements inside compute_path:**

```python
def compute_path(self, destination):
    print("Computing path from", self.position, "to", destination)
    path = [self.position]
    current_row = self.position[0]
    current_col = self.position[1]
    # ... rest of code ...

    print("Row step:", row_step)
    print("Col step:", col_step)

    while current_row != dest_row:
        current_row = current_row + row_step
        path.append((current_row, current_col))
        print("  Added:", (current_row, current_col))
    # ...
```

**This lets you see exactly what's happening, step by step.**

**Remove print statements after debugging!**

---

## Slide 8: Common Bugs and How to Find Them
**Bug 1: Path missing the start position**
- Symptom: Path has 5 steps instead of 6
- Fix: Make sure `path = [self.position]` (include start)

**Bug 2: Path goes wrong direction**
- Symptom: (0,0) to (2,3) produces (0,0), (-1,0), (-2,0)...
- Fix: Check row_step logic — should be +1 when dest > current

**Bug 3: Infinite loop**
- Symptom: Program never finishes
- Fix: If start == destination for that axis, the while loop should not execute

**Bug 4: Off-by-one error**
- Symptom: Path goes one step too far or stops one step short
- Fix: Check while condition — should be `!=` not `<` or `>`

---

## Slide 9: Your Turn!
**Activity:**
1. Create a new file: `test_manhattan.py`
2. Copy your Manhattan class into it
3. Write at least 6 test cases using the table from Slide 6
4. Run the tests and verify all pass
5. If any fail, debug using print statements

**Test template:**
```python
# Test 1: Basic forward path
manhattan = Manhattan((0, 0))
path = manhattan.compute_path((2, 3))
expected = [(0,0), (1,0), (2,0), (2,1), (2,2), (2,3)]
print("Test 1:", "PASS" if path == expected else "FAIL")
```

**Checkpoints:**
- Do all 6 tests pass?
- Did you test reverse directions?
- Did you test edge cases (same row, same position)?

---

## Slide 10: Connection to Next Lesson
**What you did today:**
- Learned why testing without hardware matters
- Wrote systematic test programs
- Verified your Manhattan class against expected outputs
- Debugged any issues before touching the robot

**Next lesson (Lesson 7):**
- Tackle the **turning challenge** — the robot needs to face the right direction
- Learn about headings (North, South, East, West)
- Figure out turn logic: "I'm facing North, I need to go East — turn right!"

**Key insight:** The algorithm is tested and working. Now we need to make the robot actually drive it!
