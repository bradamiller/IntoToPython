# Lesson 7 Worksheet: The Challenge of Turning

**Name:** ________________________
**Date:** ________________________

---

## Part 1: Desired heading from the coordinate change

Between two adjacent intersections, **either the row OR the column changes -- never both**. Four cases, four directions:

| row/col change | Direction | Heading number |
|---|---|---|
| row -1 (and col unchanged) | North | 0 |
| col +1 (and row unchanged) | East | 1 |
| row +1 (and col unchanged) | South | 2 |
| col -1 (and row unchanged) | West | 3 |

`HEADING_NAMES = ["N", "E", "S", "W"]` -- index 0 is North, 1 is East, and so on.

| Position | Next | row_diff | col_diff | What changed | Desired heading |
|---|---|---|---|---|---|
| (0, 0) | (1, 0) | 1 - 0 = _____ | 0 - 0 = _____ | __________ | __________ |
| (2, 3) | (1, 3) | 1 - 2 = _____ | 3 - 3 = _____ | __________ | __________ |
| (1, 1) | (1, 2) | _____ | _____ | __________ | __________ |
| (3, 2) | (3, 1) | _____ | _____ | __________ | __________ |
| (3, 1) | (2, 1) | _____ | _____ | __________ | __________ |
| (0, 2) | (0, 1) | _____ | _____ | __________ | __________ |
| (1, 1) | (2, 2) | _____ | _____ | __________ | __________ |

**The last row is different. What does `desired_heading((1, 1), (2, 2))` do, and what does the message say?**

____________________________________________________________________

**A classmate's version checks only one difference: `if row_diff == 1: return 2`. What does it return for the last row, and why is that worse than an error?**

____________________________________________________________________

____________________________________________________________________

---

## Part 2: Counting quarter turns

Each clockwise turn adds 1 to the heading, and 4 wraps to 0. Written as arithmetic:

```python
turns = (desired - heading) % 4
```

Fill in the table. Remember that in Python `-1 % 4` is `3`, not `-1`.

| heading | desired | `desired - heading` | `% 4` | What the robot does |
|---|---|---|---|---|
| 0 (N) | 1 (E) | 1 | _____ | ______________________ |
| 1 (E) | 1 (E) | _____ | _____ | ______________________ |
| 2 (S) | 0 (N) | _____ | _____ | ______________________ |
| 3 (W) | 2 (S) | _____ | _____ | ______________________ |
| 1 (E) | 0 (N) | _____ | _____ | ______________________ |
| 0 (N) | 3 (W) | _____ | _____ | ______________________ |
| 2 (S) | 3 (W) | _____ | _____ | ______________________ |
| 3 (W) | 1 (E) | _____ | _____ | ______________________ |

**Which rows come out to 3, and what does the robot actually do in those cases?**

____________________________________________________________________

**Why is one counterclockwise turn better than three clockwise turns, when both end facing the same way?**

____________________________________________________________________

---

## Part 3: The `turn_to` function

```python
def turn_to(heading, desired):
    turns = (desired - heading) % 4
    if turns == 3:
        turn_counterclockwise()
    else:
        for i in range(turns):
            turn_clockwise()
    return desired
```

**Why does the function end with `return desired`? What must the caller do with it?**

____________________________________________________________________

**Trace `turn_to(2, 1)`: what is `turns`, which branch runs, and how many times?**

____________________________________________________________________

---

## Part 4: Trace a path

**Path:** `[(1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]`
**Start:** position (0, 0), heading 0 (N)

| Step | Position | Next | Desired | Heading before | `% 4` | Robot does | Heading after |
|---|---|---|---|---|---|---|---|
| 1 | (0, 0) | (1, 0) | ______ | 0 (N) | ____ | ______________ | ______ |
| 2 | (1, 0) | (2, 0) | ______ | ______ | ____ | ______________ | ______ |
| 3 | (2, 0) | (2, 1) | ______ | ______ | ____ | ______________ | ______ |
| 4 | (2, 1) | (2, 2) | ______ | ______ | ____ | ______________ | ______ |
| 5 | (2, 2) | (2, 3) | ______ | ______ | ____ | ______________ | ______ |

**How many steps needed a turn?** ______  **Which step turned counterclockwise?** ______

---

## Part 5: A second path, starting mid-grid

**Path:** `[(1, 3), (0, 3), (0, 2), (0, 1), (0, 0)]`
**Start:** position (2, 3), heading 2 (S)

| Step | Position | Next | Desired | Heading before | `% 4` | Robot does | Heading after |
|---|---|---|---|---|---|---|---|
| 1 | (2, 3) | (1, 3) | ______ | 2 (S) | ____ | ______________ | ______ |
| 2 | (1, 3) | (0, 3) | ______ | ______ | ____ | ______________ | ______ |
| 3 | (0, 3) | (0, 2) | ______ | ______ | ____ | ______________ | ______ |
| 4 | (0, 2) | (0, 1) | ______ | ______ | ____ | ______________ | ______ |
| 5 | (0, 1) | (0, 0) | ______ | ______ | ____ | ______________ | ______ |

**Final position:** ______  **Final heading:** ______

---

## Part 6: Where does the program stop?

Suppose the `raise` line were missing from `desired_heading`, and a bug somewhere else handed it `(1, 1)` and `(2, 2)`.

**What does `desired_heading` return?** ______

**That value goes into `turn_to(heading, ...)`. Which line of `turn_to` fails, and what does the error message mention?**

____________________________________________________________________

**Now put the `raise` back. Which line stops the program, and what does its message tell you that the other one didn't?**

____________________________________________________________________

---

## Reflection

The planner says WHERE to go; `turn_to` handles HOW to face the right way. In one or two sentences, explain why `(desired - heading) % 4` is enough to handle every case, and what the one special case is.

_________________________________________________________________

_________________________________________________________________

---

**Next lesson:** these three functions become real code on the robot, built on the Module 2 line-tracking functions.
