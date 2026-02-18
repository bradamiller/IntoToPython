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

## Part 2: Determine the Step Values

For each start/destination pair, determine whether the row step is +1 or -1, and whether the column step is +1 or -1.

**Rule:**
- If destination row > start row: row_step = +1 (moving down)
- If destination row < start row: row_step = -1 (moving up)
- If destination col > start col: col_step = +1 (moving right)
- If destination col < start col: col_step = -1 (moving left)

| Start | Destination | row_step | col_step |
|---|---|---|---|
| (0, 0) | (3, 2) | __________ | __________ |
| (3, 3) | (0, 1) | __________ | __________ |
| (1, 3) | (3, 0) | __________ | __________ |
| (2, 0) | (0, 3) | __________ | __________ |
| (0, 0) | (0, 3) | __________ | __________ |

**For the last row, the start row and destination row are the same. Does the value of row_step matter? Why or why not?**

____________________________________________________________________

---

## Part 3: Hand-Trace the Algorithm

For each start/destination pair, trace the Manhattan algorithm (rows first, then columns). Write every position in the path.

**Path 1: (0, 0) to (3, 2)**

- row_step = _____,  col_step = _____

Row moves:

| Step | Action | Position |
|---|---|---|
| Start | — | (0, 0) |
| 1 | Row _____ | (_____, _____) |
| 2 | Row _____ | (_____, _____) |
| 3 | Row _____ | (_____, _____) |

Column moves:

| Step | Action | Position |
|---|---|---|
| 4 | Col _____ | (_____, _____) |
| 5 | Col _____ | (_____, _____) |

**Complete path:** ________________________________________________________

**Total steps:** __________ &nbsp;&nbsp; **Manhattan distance:** __________  &nbsp;&nbsp; **Do they match?** YES / NO

---

**Path 2: (3, 3) to (0, 1)**

- row_step = _____,  col_step = _____

Row moves:

| Step | Action | Position |
|---|---|---|
| Start | — | (3, 3) |
| 1 | Row _____ | (_____, _____) |
| 2 | Row _____ | (_____, _____) |
| 3 | Row _____ | (_____, _____) |

Column moves:

| Step | Action | Position |
|---|---|---|
| 4 | Col _____ | (_____, _____) |
| 5 | Col _____ | (_____, _____) |

**Complete path:** ________________________________________________________

**Total steps:** __________ &nbsp;&nbsp; **Manhattan distance:** __________  &nbsp;&nbsp; **Do they match?** YES / NO

---

**Path 3: (1, 3) to (3, 0)**

- row_step = _____,  col_step = _____

Row moves:

| Step | Action | Position |
|---|---|---|
| Start | — | (1, 3) |
| 1 | Row _____ | (_____, _____) |
| 2 | Row _____ | (_____, _____) |

Column moves:

| Step | Action | Position |
|---|---|---|
| 3 | Col _____ | (_____, _____) |
| 4 | Col _____ | (_____, _____) |
| 5 | Col _____ | (_____, _____) |

**Complete path:** ________________________________________________________

**Total steps:** __________ &nbsp;&nbsp; **Manhattan distance:** __________  &nbsp;&nbsp; **Do they match?** YES / NO

---

**Path 4: (2, 2) to (2, 0)** (same row!)

- row_step = _____,  col_step = _____

**Does the row loop execute?** YES / NO &nbsp;&nbsp; **Why?** ____________________________

Column moves:

| Step | Action | Position |
|---|---|---|
| Start | — | (2, 2) |
| 1 | Col _____ | (_____, _____) |
| 2 | Col _____ | (_____, _____) |

**Complete path:** ________________________________________________________

**Total steps:** __________ &nbsp;&nbsp; **Manhattan distance:** __________  &nbsp;&nbsp; **Do they match?** YES / NO

---

**Path 5: (0, 1) to (3, 1)** (same column!)

- row_step = _____,  col_step = _____

**Does the column loop execute?** YES / NO &nbsp;&nbsp; **Why?** ____________________________

Row moves:

| Step | Action | Position |
|---|---|---|
| Start | — | (0, 1) |
| 1 | Row _____ | (_____, _____) |
| 2 | Row _____ | (_____, _____) |
| 3 | Row _____ | (_____, _____) |

**Complete path:** ________________________________________________________

**Total steps:** __________ &nbsp;&nbsp; **Manhattan distance:** __________  &nbsp;&nbsp; **Do they match?** YES / NO

---

## Part 4: Draw the Paths on the Grid

Using the paths you traced in Part 3, draw each path on the grid below. Use arrows to show direction. Label each path with its number (1-5).

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

## Part 5: Verify Your Understanding

1. **The Manhattan algorithm always moves __________ first, then __________.**

2. **If the destination row is SMALLER than the start row, the robot moves __________ (up/down).**

3. **If the destination column is LARGER than the start column, the robot moves __________ (left/right).**

4. **When the start and destination are in the same row, the row loop __________ (executes / does not execute).**

5. **When the start and destination are the same position, the path contains __________ position(s).**

6. **The number of steps in a path always equals the __________ __________.**

---

## Reflection

**You traced 5 different paths by hand today. In the next lesson, you will write a Python class that does this automatically. Why is it important to trace the algorithm by hand BEFORE writing code?**

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

---

**Next Lesson:** We'll implement the Manhattan algorithm as a Python class with a `compute_path()` method!
