# Lesson 5 Worksheet: Implementing the Manhattan Class

**Name:** ________________________
**Date:** ________________________

---

## Part 1: Code Tracing — compute_path() Step by Step

Here is the complete Manhattan class with the 4-while-loop `compute_path` method:

```python
class Manhattan:
    def __init__(self, start):
        self.position = start

    def compute_path(self, destination):
        path = []
        current_row, current_col = self.position
        dest_row, dest_col = destination

        # Move south (rows increase)
        while current_row < dest_row:
            current_row = current_row + 1
            path.append((current_row, current_col))

        # Move north (rows decrease)
        while current_row > dest_row:
            current_row = current_row - 1
            path.append((current_row, current_col))

        # Move east (columns increase)
        while current_col < dest_col:
            current_col = current_col + 1
            path.append((current_row, current_col))

        # Move west (columns decrease)
        while current_col > dest_col:
            current_col = current_col - 1
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
| `path` (initial) | __________ |

**South while loop — trace each iteration:**

| Iteration | current_row (before) | < dest_row? | current_row (after) | Appended to path |
|---|---|---|---|---|
| 1 | _____ | YES / NO | _____ | ________________ |
| 2 | _____ | YES / NO | _____ | ________________ |
| Check | _____ | YES / NO | — (loop ends) | — |

**North while loop:** Does it execute? YES / NO &nbsp;&nbsp; **Why?** ____________________________

**East while loop — trace each iteration:**

| Iteration | current_col (before) | < dest_col? | current_col (after) | Appended to path |
|---|---|---|---|---|
| 1 | _____ | YES / NO | _____ | ________________ |
| 2 | _____ | YES / NO | _____ | ________________ |
| 3 | _____ | YES / NO | _____ | ________________ |
| Check | _____ | YES / NO | — (loop ends) | — |

**West while loop:** Does it execute? YES / NO &nbsp;&nbsp; **Why?** ____________________________

**Final returned path:** ________________________________________________________

**len(path):** __________

---

## Part 2: Trace a Reverse Path

**Trace the call:** `Manhattan((3, 3)).compute_path((1, 0))`

**Setup variables:**

| Variable | Initial Value |
|---|---|
| `current_row` | __________ |
| `current_col` | __________ |
| `dest_row` | __________ |
| `dest_col` | __________ |

**Which two while loops execute?** __________ and __________

**North while loop:**

| Iteration | current_row (before) | current_row (after) | Appended |
|---|---|---|---|
| 1 | _____ | _____ | ________________ |
| 2 | _____ | _____ | ________________ |

**West while loop:**

| Iteration | current_col (before) | current_col (after) | Appended |
|---|---|---|---|
| 1 | _____ | _____ | ________________ |
| 2 | _____ | _____ | ________________ |
| 3 | _____ | _____ | ________________ |

**Final returned path:** ________________________________________________________

**len(path):** __________

---

## Part 3: Fill in the Blanks

Complete the missing parts of the Manhattan class:

```python
class Manhattan:
    def __init__(self, start):
        self.__________ = start

    def compute_path(self, destination):
        path = __

        current_row, current_col = self.__________
        dest_row, dest_col = __________

        # Move south
        while current_row __ dest_row:
            current_row = current_row + __
            path.__________((__________,  __________))

        # Move north
        while current_row __ dest_row:
            current_row = current_row - __
            path.__________((__________,  __________))

        # Move east
        while current_col __ dest_col:
            current_col = current_col + __
            path.__________((__________,  __________))

        # Move west
        while current_col __ dest_col:
            current_col = current_col - __
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
print("Steps:", len(path))
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
print("Steps:", len(path))
```

**Predicted output:**

Line 1: ________________________________________________________

Line 2: ________________________________________________________

**Why is the path empty?** ____________________________

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
    path = [self.position]                 # <-- Look here
    current_row, current_col = self.position
    dest_row, dest_col = destination
    # ... rest of method (4 while loops)
```

**What is wrong?** ____________________________________________________________________

**Fix:** ____________________________________________________________________

---

**Bug 2:**
```python
def compute_path(self, destination):
    path = []
    current_row, current_col = self.position
    dest_row, dest_col = destination

    while current_row < dest_row:
        current_row = current_row + 1
        path.append((current_row, current_col))

    while current_row > dest_row:
        current_row = current_row - 1
        path.append((current_row, current_col))

    while current_col < dest_col:
        current_col = current_col + 1
        path.append((current_row, current_col))

    while current_col > dest_col:
        current_col = current_col + 1          # <-- Look here
        path.append((current_row, current_col))
```

**What is wrong?** ____________________________________________________________________

**What would happen if you called `compute_path((2, 3))` from start (3, 3)?**

____________________________________________________________________

**Fix:** ____________________________________________________________________

---

**Bug 3:**
```python
def compute_path(self, destination):
    path = []
    current_row, current_col = self.position
    dest_row, dest_col = destination

    while current_row < dest_row:
        current_row = current_row + 1
        path.append((current_row, current_col))

    while current_row > dest_row:
        current_row = current_row - 1
        path.append((current_row, current_col))

    while current_col < dest_col:
        current_col = current_col + 1
        path.append((current_col, current_row))    # <-- Look here

    while current_col > dest_col:
        current_col = current_col - 1
        path.append((current_row, current_col))
```

**What is wrong?** ____________________________________________________________________

**If start is (0, 0) and destination is (2, 3), what would the INCORRECT last three elements of the path be?**

________________________________________________________

**What should they be?**

________________________________________________________

---

## Reflection

**The compute_path() method uses 4 separate while loops instead of if/else statements with 2 while loops. Why does this simpler approach work? (Hint: think about what happens when a while loop's condition is already false.)**

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

---

**Next Lesson:** We'll learn how to write test programs to verify our Manhattan class works correctly -- without needing a robot!
