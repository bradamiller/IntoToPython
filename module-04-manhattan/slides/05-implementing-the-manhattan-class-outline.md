# Lesson 5 Slide Outline: Implementing the Manhattan Class

## Slide 1: Title & Learning Objectives
**Title:** Implementing the Manhattan Class

**Learning Objectives:**
- Design a class with __init__ and compute_path methods
- Implement the Manhattan algorithm in Python
- Handle direction using conditional logic (+1 or -1 step)
- Build a path as a list of tuples using append()

**Agenda:**
- Class design overview (5 min)
- Building compute_path step by step (15 min)
- Guided coding (15 min)
- Testing your class (10 min)

---

## Slide 2: Hook — From Paper to Code
**Last lesson:** You traced paths by hand.

**Today:** You'll write a class that computes paths automatically.

**The goal:**
```python
manhattan = Manhattan((0, 0))
path = manhattan.compute_path((2, 3))
print(path)
# [(0,0), (1,0), (2,0), (2,1), (2,2), (2,3)]
```

**Question:** "Can you translate the hand-tracing steps into Python code?"

---

## Slide 3: Class Design — Manhattan
**What does the class need?**

**Data (stored in __init__):**
- `self.position` — the robot's current position as a tuple

**Methods:**
- `compute_path(destination)` — returns a list of tuples from current position to destination

**Class skeleton:**
```python
class Manhattan:
    def __init__(self, start):
        self.position = start

    def compute_path(self, destination):
        # Build and return the path
        pass
```

---

## Slide 4: Step 1 — Determine Direction
**First, figure out which way to go:**

```python
def compute_path(self, destination):
    path = [self.position]

    current_row = self.position[0]
    current_col = self.position[1]
    dest_row = destination[0]
    dest_col = destination[1]

    # Which direction for rows?
    if dest_row > current_row:
        row_step = 1       # Move down
    else:
        row_step = -1      # Move up

    # Which direction for columns?
    if dest_col > current_col:
        col_step = 1       # Move right
    else:
        col_step = -1      # Move left
```

**This matches what we did by hand in Lesson 4!**

---

## Slide 5: Step 2 — Move Along Rows
**Loop through rows until we reach the destination row:**

```python
    # Move along rows
    while current_row != dest_row:
        current_row = current_row + row_step
        path.append((current_row, current_col))
```

**Trace for (0, 0) to (2, 3):**

| Iteration | current_row | row_step | After | Appended |
|---|---|---|---|---|
| 1 | 0 | +1 | 1 | (1, 0) |
| 2 | 1 | +1 | 2 | (2, 0) |
| Stop | 2 == 2 | — | — | — |

**Path so far: [(0,0), (1,0), (2,0)]**

---

## Slide 6: Step 3 — Move Along Columns
**Loop through columns until we reach the destination column:**

```python
    # Move along columns
    while current_col != dest_col:
        current_col = current_col + col_step
        path.append((current_row, current_col))

    return path
```

**Continuing the trace for (0, 0) to (2, 3):**

| Iteration | current_col | col_step | After | Appended |
|---|---|---|---|---|
| 1 | 0 | +1 | 1 | (2, 1) |
| 2 | 1 | +1 | 2 | (2, 2) |
| 3 | 2 | +1 | 3 | (2, 3) |
| Stop | 3 == 3 | — | — | — |

**Final path: [(0,0), (1,0), (2,0), (2,1), (2,2), (2,3)]**

---

## Slide 7: The Complete Manhattan Class
```python
class Manhattan:
    def __init__(self, start):
        self.position = start

    def compute_path(self, destination):
        path = [self.position]

        current_row = self.position[0]
        current_col = self.position[1]
        dest_row = destination[0]
        dest_col = destination[1]

        if dest_row > current_row:
            row_step = 1
        else:
            row_step = -1

        if dest_col > current_col:
            col_step = 1
        else:
            col_step = -1

        while current_row != dest_row:
            current_row = current_row + row_step
            path.append((current_row, current_col))

        while current_col != dest_col:
            current_col = current_col + col_step
            path.append((current_row, current_col))

        return path
```

---

## Slide 8: Using the Manhattan Class
**Test program:**
```python
manhattan = Manhattan((0, 0))

path = manhattan.compute_path((2, 3))
print("Path to (2,3):", path)

path = manhattan.compute_path((1, 1))
print("Path to (1,1):", path)
```

**Wait — second path starts from (0, 0) again!**

**Important:** compute_path always starts from self.position. If you want the robot to "move," update the position:
```python
manhattan.position = (2, 3)
path = manhattan.compute_path((0, 0))
print("Return path:", path)
```

---

## Slide 9: Your Turn!
**Activity:**
1. Type the complete Manhattan class into a new Python file
2. Test with these cases:
   - (0, 0) to (2, 3) — expected: 6 positions
   - (2, 3) to (0, 0) — expected: 6 positions (reverse)
   - (0, 0) to (0, 3) — expected: 4 positions (same row)
   - (1, 1) to (1, 1) — expected: 1 position (same spot)
3. Print each path and verify against your hand traces from Lesson 4

**Checkpoints:**
- Does your class produce the correct paths?
- Does it handle all four directions?
- Does the "same position" case return just the start?

---

## Slide 10: Connection to Next Lesson
**What you did today:**
- Implemented the Manhattan class with compute_path()
- Built paths using while loops and append()
- Handled direction with conditional step values

**Next lesson (Lesson 6):**
- Learn how to **test without a robot**
- Write systematic test programs
- Verify your class works correctly before putting it on the robot

**Key insight:** The algorithm is pure math — no motors, no sensors. We can test it on any computer!
