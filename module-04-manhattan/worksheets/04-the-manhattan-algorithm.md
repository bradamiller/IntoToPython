# Lesson 4 Worksheet: The Manhattan Algorithm

**Name:** ________________________
**Date:** ________________________

---

## Part 1: Manhattan Distance

Calculate the Manhattan distance for each pair. Remember: Manhattan distance = |row difference| + |column difference|.

| Start | Destination | Row Distance | Col Distance | Manhattan Distance |
|---|---|---|---|---|
| (0, 0) | (2, 3) | \|2 - 0\| = _____ | \|3 - 0\| = _____ | __________ |
| (3, 3) | (0, 0) | \|0 - 3\| = _____ | \|0 - 3\| = _____ | __________ |
| (1, 0) | (1, 3) | __________ | __________ | __________ |
| (0, 2) | (3, 2) | __________ | __________ | __________ |
| (2, 1) | (2, 1) | __________ | __________ | __________ |

**Which pair requires the most steps?** ____________________________

**Which pair requires zero steps? Why?** ____________________________

---

## Part 2: Write compute_path — Positive Directions Only

Write a `compute_path(start, end)` function that builds a path from `start` to `end` using two while loops. This version only needs to handle destinations that are **south and east** (row and column increase).

**Rules:**
- The path does **NOT** include the starting position (the robot is already there)
- `path = []` — start with an empty list
- Steps = `len(path)`

Fill in the blanks:

```python
def compute_path(start, end):
    path = []
    current_row, current_col = start
    dest_row, dest_col = end

    # Move south (rows increase)
    while current_row __ dest_row:
        current_row = current_row + __
        path.append((__________,  __________))

    # Move east (columns increase)
    while current_col __ dest_col:
        current_col = current_col + __
        path.append((__________,  __________))

    return path
```

**Test it:** `compute_path((0, 0), (2, 3))` should return:

________________________________________________________

**How many steps?** `len(path)` = __________

---

**Try this:** `compute_path((3, 3), (1, 0))` — what does it return?

________________________________________________________

**Why is the result wrong?** ____________________________

---

## Part 3: Write compute_path — All Directions

Fix the function by adding two more while loops for **north** and **west**. No if/else statements needed — only the loops that need to run will execute!

Fill in the blanks:

```python
def compute_path(start, end):
    path = []
    current_row, current_col = start
    dest_row, dest_col = end

    # Move south (rows increase)
    while current_row < dest_row:
        current_row = current_row + 1
        path.append((current_row, current_col))

    # Move north (rows decrease)
    while current_row __ dest_row:
        current_row = current_row __ __
        path.__________((__________,  __________))

    # Move east (columns increase)
    while current_col < dest_col:
        current_col = current_col + 1
        path.append((current_row, current_col))

    # Move west (columns decrease)
    while current_col __ dest_col:
        current_col = current_col __ __
        path.__________((__________,  __________))

    return path
```

---

## Part 4: Hand-Trace the Algorithm

For each start/end pair, trace the function. The path does NOT include the start position.

**Path 1: compute_path((0, 0), (2, 3))**

Row moves:

| Step | Action | Position Added |
|---|---|---|
| 1 | Row +1 | (_____, _____) |
| 2 | Row +1 | (_____, _____) |

Column moves:

| Step | Action | Position Added |
|---|---|---|
| 3 | Col +1 | (_____, _____) |
| 4 | Col +1 | (_____, _____) |
| 5 | Col +1 | (_____, _____) |

**Returned path:** ________________________________________________________

**len(path):** __________ &nbsp;&nbsp; **Manhattan distance:** __________  &nbsp;&nbsp; **Do they match?** YES / NO

---

**Path 2: compute_path((3, 3), (1, 0))**

Row moves:

| Step | Action | Position Added |
|---|---|---|
| 1 | Row -1 | (_____, _____) |
| 2 | Row -1 | (_____, _____) |

Column moves:

| Step | Action | Position Added |
|---|---|---|
| 3 | Col -1 | (_____, _____) |
| 4 | Col -1 | (_____, _____) |
| 5 | Col -1 | (_____, _____) |

**Returned path:** ________________________________________________________

**len(path):** __________ &nbsp;&nbsp; **Manhattan distance:** __________  &nbsp;&nbsp; **Do they match?** YES / NO

---

**Path 3: compute_path((2, 0), (2, 3))** (same row!)

**Do any row loops execute?** YES / NO &nbsp;&nbsp; **Why?** ____________________________

Column moves:

| Step | Action | Position Added |
|---|---|---|
| 1 | Col +1 | (_____, _____) |
| 2 | Col +1 | (_____, _____) |
| 3 | Col +1 | (_____, _____) |

**Returned path:** ________________________________________________________

**len(path):** __________ &nbsp;&nbsp; **Manhattan distance:** __________  &nbsp;&nbsp; **Do they match?** YES / NO

---

**Path 4: compute_path((1, 1), (1, 1))** (same position!)

**Do any loops execute?** YES / NO &nbsp;&nbsp; **Why?** ____________________________

**Returned path:** __________

**len(path):** __________

---

## Part 5: Draw the Paths on the Grid

Using the paths you traced in Part 4, draw each path on the grid below. Use arrows to show direction. Label each path with its number (1-3). Path 4 is just a dot!

```
         Col 0       Col 1       Col 2       Col 3
          |           |           |           |
Row 0 ---[0,0]------[0,1]------[0,2]------[0,3]---
          |           |           |           |
Row 1 ---[1,0]------[1,1]------[1,2]------[1,3]---
          |           |           |           |
Row 2 ---[2,0]------[2,1]------[2,2]------[2,3]---
          |           |           |           |
Row 3 ---[3,0]------[3,1]------[3,2]------[3,3]---
```

**What shape do most of the paths make?** ____________________________

**Which paths are straight lines instead of L-shapes?** ____________________________

---

## Part 6: Verify Your Understanding

1. **The Manhattan algorithm always moves __________ first, then __________.**

2. **If the destination row is SMALLER than the start row, which while loop runs?** ____________________________

3. **If the destination column is LARGER than the start column, which while loop runs?** ____________________________

4. **When the start and destination are in the same row, the row loops __________ (execute / do not execute).**

5. **When the start and destination are the same position, the path is __________ and len(path) is __________.**

6. **The number of steps in a path (len(path)) always equals the __________ __________.**

7. **Why don't we need if/else to choose direction? How do the 4 while loops handle it?**

   ____________________________________________________________________

---

## Reflection

**You wrote a function that can find a path between ANY two grid positions using just 4 while loops. In the next lesson, you will wrap this function into a class. Why is it important to get the function working correctly BEFORE putting it in a class?**

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

---

**Next Lesson:** We'll wrap `compute_path` into a Manhattan class that remembers the robot's position!
