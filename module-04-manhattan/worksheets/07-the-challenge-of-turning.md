# Lesson 7 Worksheet: The Challenge of Turning

**Name:** ________________________
**Date:** ________________________

---

## Part 1: Heading from Coordinates

Given two consecutive coordinates, determine the **heading number** the robot needs. We use numbers for headings:

| Heading Number | Direction | row_diff | col_diff |
|---|---|---|---|
| 0 | North (up) | -1 | 0 |
| 1 | East (right) | 0 | +1 |
| 2 | South (down) | +1 | 0 |
| 3 | West (left) | 0 | -1 |

**`HEADING_NAMES = ["N", "E", "S", "W"]`** — index 0 is North, 1 is East, etc.

| Current Position | Next Position | row_diff | col_diff | Heading (number and name) |
|---|---|---|---|---|
| (0, 0) | (1, 0) | 1 - 0 = _____ | 0 - 0 = _____ | __________ |
| (2, 3) | (1, 3) | 1 - 2 = _____ | 3 - 3 = _____ | __________ |
| (1, 1) | (1, 2) | _____ | _____ | __________ |
| (3, 2) | (3, 1) | _____ | _____ | __________ |
| (0, 3) | (1, 3) | _____ | _____ | __________ |
| (2, 0) | (2, 1) | _____ | _____ | __________ |
| (3, 1) | (2, 1) | _____ | _____ | __________ |
| (0, 2) | (0, 1) | _____ | _____ | __________ |

---

## Part 2: The Right Turns Table

Using only right turns, how many right turns does it take to go from the current heading to the needed heading? Fill in each cell with **0**, **1**, **2**, or **3**.

**The formula:** `turns = (needed - current) % 4`

| Current \ Needed | 0 (N) | 1 (E) | 2 (S) | 3 (W) |
|---|---|---|---|---|
| **0 (N)** | _____ | _____ | _____ | _____ |
| **1 (E)** | _____ | _____ | _____ | _____ |
| **2 (S)** | _____ | _____ | _____ | _____ |
| **3 (W)** | _____ | _____ | _____ | _____ |

**How many cells have 0 right turns?** __________  **Why?** ____________________________

**What does 2 right turns mean physically?** ____________________________

**Do you notice a pattern in the table?** ____________________________

---

## Part 3: Determine the Number of Right Turns

For each scenario, use the formula `turns = (needed - current) % 4` to calculate the number of right turns.

| Scenario | Current Heading | Needed Heading | (needed - current) | % 4 | Right Turns |
|---|---|---|---|---|---|
| 1 | 0 (N) | 1 (E) | 1 - 0 = _____ | _____ % 4 = _____ | _____ |
| 2 | 1 (E) | 1 (E) | 1 - 1 = _____ | _____ % 4 = _____ | _____ |
| 3 | 2 (S) | 0 (N) | 0 - 2 = _____ | _____ % 4 = _____ | _____ |
| 4 | 3 (W) | 2 (S) | 2 - 3 = _____ | _____ % 4 = _____ | _____ |
| 5 | 1 (E) | 0 (N) | 0 - 1 = _____ | _____ % 4 = _____ | _____ |
| 6 | 0 (N) | 3 (W) | 3 - 0 = _____ | _____ % 4 = _____ | _____ |
| 7 | 2 (S) | 3 (W) | 3 - 2 = _____ | _____ % 4 = _____ | _____ |
| 8 | 3 (W) | 1 (E) | 1 - 3 = _____ | _____ % 4 = _____ | _____ |

**Why does the `% 4` make negative numbers work correctly?** ____________________________

---

## Part 4: Trace a Path with Heading Updates

**Path:** [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]
**Starting heading:** 0 (N)

For each step, determine the needed heading, the number of right turns, and the new heading.

| Step | From | To | Needed Heading | Current Heading | Right Turns | New Heading |
|---|---|---|---|---|---|---|
| 1 | (0, 0) | (1, 0) | __________ | 0 (N) | __________ | __________ |
| 2 | (1, 0) | (2, 0) | __________ | __________ | __________ | __________ |
| 3 | (2, 0) | (2, 1) | __________ | __________ | __________ | __________ |
| 4 | (2, 1) | (2, 2) | __________ | __________ | __________ | __________ |
| 5 | (2, 2) | (2, 3) | __________ | __________ | __________ | __________ |

**How many steps required turning?** __________

**How many steps required zero turns?** __________

**At which step did the robot change from row movement to column movement?** Step __________

---

## Part 5: Trace a Second Path

**Path:** [(2, 3), (1, 3), (0, 3), (0, 2), (0, 1), (0, 0)]
**Starting heading:** 2 (S)

| Step | From | To | Needed Heading | Current Heading | Right Turns | New Heading |
|---|---|---|---|---|---|---|
| 1 | (2, 3) | (1, 3) | __________ | 2 (S) | __________ | __________ |
| 2 | (1, 3) | (0, 3) | __________ | __________ | __________ | __________ |
| 3 | (0, 3) | (0, 2) | __________ | __________ | __________ | __________ |
| 4 | (0, 2) | (0, 1) | __________ | __________ | __________ | __________ |
| 5 | (0, 1) | (0, 0) | __________ | __________ | __________ | __________ |

**What is the robot's final heading after completing this path?** __________

---

## Part 6: Trace a Third Path

**Path:** [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3)]
**Starting heading:** 0 (N)

| Step | From | To | Needed Heading | Current Heading | Right Turns | New Heading |
|---|---|---|---|---|---|---|
| 1 | (1, 1) | (1, 2) | __________ | 0 (N) | __________ | __________ |
| 2 | (1, 2) | (1, 3) | __________ | __________ | __________ | __________ |
| 3 | (1, 3) | (2, 3) | __________ | __________ | __________ | __________ |
| 4 | (2, 3) | (3, 3) | __________ | __________ | __________ | __________ |

**What is the robot's final heading?** __________

**Does the first step require turning? Why?**

____________________________________________________________________

---

## Part 7: Robot Orientation Diagrams

For each scenario, draw an arrow inside the box showing which way the robot is facing. Then draw a curved arrow showing the turn(s) it needs to make, and draw the final facing direction.

**Scenario A:** Facing 0 (N), need heading 1 (E)

```
  Before turn:        After turn:
  +-------+           +-------+
  |       |           |       |
  |  [?]  |           |  [?]  |
  |       |           |       |
  +-------+           +-------+
  Right turns needed: __________
```

**Scenario B:** Facing 1 (E), need heading 2 (S)

```
  Before turn:        After turn:
  +-------+           +-------+
  |       |           |       |
  |  [?]  |           |  [?]  |
  |       |           |       |
  +-------+           +-------+
  Right turns needed: __________
```

**Scenario C:** Facing 3 (W), need heading 1 (E)

```
  Before turn:        After turn:
  +-------+           +-------+
  |       |           |       |
  |  [?]  |           |  [?]  |
  |       |           |       |
  +-------+           +-------+
  Right turns needed: __________
```

**Scenario D:** Facing 2 (S), need heading 2 (S)

```
  Before turn:        After turn:
  +-------+           +-------+
  |       |           |       |
  |  [?]  |           |  [?]  |
  |       |           |       |
  +-------+           +-------+
  Right turns needed: __________
```

---

## Part 8: Heading and Turning Logic in Code

Fill in the blanks to complete the heading and turning functions:

```python
HEADING_NAMES = ["N", "E", "S", "W"]

def get_needed_heading(current_pos, next_pos):
    row_diff = next_pos[0] - current_pos[0]
    col_diff = next_pos[1] - current_pos[1]

    if row_diff == -1:
        return _____      # North
    elif col_diff == _____:
        return _____      # East
    elif row_diff == _____:
        return _____      # South
    elif col_diff == _____:
        return _____      # West

def count_right_turns(current, needed):
    return (__________ - __________) % _____
```

**Test your understanding -- what does `count_right_turns(1, 0)` return?** __________

**What does `count_right_turns(3, 3)` return?** __________

**What does `count_right_turns(0, 2)` return?** __________

---

## Reflection

**The Manhattan algorithm tells the robot WHERE to go, but the turning logic tells it HOW to get there. Why is using numbers and a formula better than using strings and dictionaries?**

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

---

**Next Lesson:** We'll implement the turning logic in a **Navigator class** that can drive the robot along any path!
