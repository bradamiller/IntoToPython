# Lesson 5 Worksheet: Implementing the Manhattan Class

**Name:** ________________________
**Date:** ________________________

---

## Part 1: Code Tracing — compute_path() Step by Step

Here is the complete `compute_path` method:

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

**Trace the call:** `Manhattan((0, 0)).compute_path((2, 3))`

**Setup variables:**

| Variable | Initial Value |
|---|---|
| `self.position` | __________ |
| `current_row` | __________ |
| `current_col` | __________ |
| `dest_row` | __________ |
| `dest_col` | __________ |
| `row_step` | __________ |
| `col_step` | __________ |
| `path` (initial) | __________ |

**Row while loop — trace each iteration:**

| Iteration | current_row (before) | != dest_row? | current_row (after) | Appended to path |
|---|---|---|---|---|
| 1 | _____ | YES / NO | _____ | ________________ |
| 2 | _____ | YES / NO | _____ | ________________ |
| Check | _____ | YES / NO | — (loop ends) | — |

**Column while loop — trace each iteration:**

| Iteration | current_col (before) | != dest_col? | current_col (after) | Appended to path |
|---|---|---|---|---|
| 1 | _____ | YES / NO | _____ | ________________ |
| 2 | _____ | YES / NO | _____ | ________________ |
| 3 | _____ | YES / NO | _____ | ________________ |
| Check | _____ | YES / NO | — (loop ends) | — |

**Final returned path:** ________________________________________________________

---

## Part 2: Trace a Reverse Path

**Trace the call:** `Manhattan((2, 3)).compute_path((0, 1))`

**Setup variables:**

| Variable | Initial Value |
|---|---|
| `current_row` | __________ |
| `current_col` | __________ |
| `dest_row` | __________ |
| `dest_col` | __________ |
| `row_step` | __________ |
| `col_step` | __________ |

**Row while loop:**

| Iteration | current_row (before) | current_row (after) | Appended |
|---|---|---|---|
| 1 | _____ | _____ | ________________ |
| 2 | _____ | _____ | ________________ |

**Column while loop:**

| Iteration | current_col (before) | current_col (after) | Appended |
|---|---|---|---|
| 1 | _____ | _____ | ________________ |
| 2 | _____ | _____ | ________________ |

**Final returned path:** ________________________________________________________

---

## Part 3: Fill in the Blanks

Complete the missing parts of the Manhattan class:

```python
class Manhattan:
    def __init__(self, start):
        self.__________ = start

    def compute_path(self, destination):
        path = [__________]

        current_row = self.position[__]
        current_col = self.position[__]
        dest_row = __________[0]
        dest_col = __________[1]

        if dest_row __ current_row:
            row_step = __
        else:
            row_step = __

        if dest_col __ current_col:
            col_step = __
        else:
            col_step = __

        while current_row __ dest_row:
            current_row = current_row + __________
            path.__________((__________,  __________))

        while current_col __ dest_col:
            current_col = current_col + __________
            path.__________((__________,  __________))

        return __________
```

---

## Part 4: Predict the Output

**Program A:**
```python
manhattan = Manhattan((0, 0))
path = manhattan.compute_path((0, 3))
print(path)
print("Steps:", len(path) - 1)
```

**Predicted output:**

Line 1: ________________________________________________________

Line 2: ________________________________________________________

**What kind of edge case is this?** ____________________________

---

**Program B:**
```python
manhattan = Manhattan((2, 2))
path = manhattan.compute_path((2, 2))
print(path)
print("Steps:", len(path) - 1)
```

**Predicted output:**

Line 1: ________________________________________________________

Line 2: ________________________________________________________

**Why does the path have only one element?** ____________________________

---

**Program C:**
```python
manhattan = Manhattan((0, 0))
path1 = manhattan.compute_path((2, 3))
path2 = manhattan.compute_path((1, 1))
print("Path 1:", path1)
print("Path 2:", path2)
```

**Predicted output:**

Line 1: ________________________________________________________

Line 2: ________________________________________________________

**Do both paths start from the same position?** YES / NO

**Why?** ____________________________________________________________________

---

## Part 5: Find and Fix the Bug

Each version of `compute_path` has a bug. Identify the problem and write the fix.

**Bug 1:**
```python
def compute_path(self, destination):
    path = []                          # <-- Look here
    current_row = self.position[0]
    current_col = self.position[1]
    dest_row = destination[0]
    dest_col = destination[1]
    # ... rest of method
```

**What is wrong?** ____________________________________________________________________

**Fix:** ____________________________________________________________________

---

**Bug 2:**
```python
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

    while current_row < dest_row:          # <-- Look here
        current_row = current_row + row_step
        path.append((current_row, current_col))

    while current_col != dest_col:
        current_col = current_col + col_step
        path.append((current_row, current_col))

    return path
```

**What is wrong?** ____________________________________________________________________

**When would this bug cause a problem? Give a specific start and destination:**

Start: (_____, _____) &nbsp;&nbsp; Destination: (_____, _____)

**Fix:** ____________________________________________________________________

---

**Bug 3:**
```python
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
        path.append((current_col, current_row))    # <-- Look here

    return path
```

**What is wrong?** ____________________________________________________________________

**If start is (0, 0) and destination is (2, 3), what would the INCORRECT last three elements of the path be?**

________________________________________________________

**What should they be?**

________________________________________________________

---

## Reflection

**The compute_path() method uses while loops instead of for loops. Why is `while current_row != dest_row` better than using a for loop for this problem?**

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

---

**Next Lesson:** We'll learn how to write test programs to verify our Manhattan class works correctly -- without needing a robot!
