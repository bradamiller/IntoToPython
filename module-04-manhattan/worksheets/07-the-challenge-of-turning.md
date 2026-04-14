# Lesson 7 Worksheet: The Challenge of Turning

**Name:** ________________________
**Date:** ________________________

---

## Part 1: Desired Heading from Coordinate Change

Between two adjacent intersections, **either the row OR the column changes — never both**. That gives 4 cases, each mapping to one direction:

| row/col change | Direction | Heading Number |
|---|---|---|
| row -1 | North | 0 |
| col +1 | East | 1 |
| row +1 | South | 2 |
| col -1 | West | 3 |

**`HEADING_NAMES = ["N", "E", "S", "W"]`** — index 0 is North, 1 is East, etc.

| Current Position | Next Position | row_diff | col_diff | What Changed | Desired Heading |
|---|---|---|---|---|---|
| (0, 0) | (1, 0) | 1 - 0 = _____ | 0 - 0 = _____ | __________ | __________ |
| (2, 3) | (1, 3) | 1 - 2 = _____ | 3 - 3 = _____ | __________ | __________ |
| (1, 1) | (1, 2) | _____ | _____ | __________ | __________ |
| (3, 2) | (3, 1) | _____ | _____ | __________ | __________ |
| (0, 3) | (1, 3) | _____ | _____ | __________ | __________ |
| (2, 0) | (2, 1) | _____ | _____ | __________ | __________ |
| (3, 1) | (2, 1) | _____ | _____ | __________ | __________ |
| (0, 2) | (0, 1) | _____ | _____ | __________ | __________ |

---

## Part 2: The `turn_to` While Loop

Here is the code we will put in the Navigator class in Lesson 8:

```python
def turn_to(self, desired):
    while self.heading != desired:
        self.robot.turn_right()
        self.heading = self.heading + 1
        if self.heading == 4:
            self.heading = 0
```

**Each pass through the loop:** turn the robot right, add 1 to heading. If heading hits 4, reset to 0. Stop when heading equals desired.

**In your own words, what does the line `if self.heading == 4: self.heading = 0` do, and why is it necessary?**

____________________________________________________________________

____________________________________________________________________

---

## Part 3: Trace `turn_to` by Hand

For each scenario, list the value of `self.heading` after each pass through the while loop, ending when the loop stops. Write "already there" if the loop runs zero times.

| Scenario | Current Heading | Desired Heading | heading values during turn_to | Total Turns |
|---|---|---|---|---|
| 1 | 0 (N) | 1 (E) | 0 → ___ | _____ |
| 2 | 1 (E) | 1 (E) | __________ | _____ |
| 3 | 2 (S) | 0 (N) | 2 → ___ → ___ | _____ |
| 4 | 3 (W) | 2 (S) | 3 → ___ → ___ → ___ | _____ |
| 5 | 1 (E) | 0 (N) | 1 → ___ → ___ → ___ | _____ |
| 6 | 0 (N) | 3 (W) | 0 → ___ → ___ → ___ | _____ |
| 7 | 2 (S) | 3 (W) | 2 → ___ | _____ |
| 8 | 3 (W) | 1 (E) | 3 → ___ → ___ | _____ |

**Which scenarios above trigger the wrap from 4 back to 0?** ____________________________

**What is the maximum number of turns the loop can ever run?** ____________________________

---

## Part 4: Trace a Path with Heading Updates

**Path:** [(1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]
**Starting position:** (0, 0) &nbsp;&nbsp; **Starting heading:** 0 (N)

For each step, determine the desired heading, trace `turn_to`, and record the final heading.

| Step | Position | Next | Desired | Current Heading | `turn_to` heading values | New Heading |
|---|---|---|---|---|---|---|
| 1 | (0, 0) | (1, 0) | __________ | 0 (N) | __________ | __________ |
| 2 | (1, 0) | (2, 0) | __________ | __________ | __________ | __________ |
| 3 | (2, 0) | (2, 1) | __________ | __________ | __________ | __________ |
| 4 | (2, 1) | (2, 2) | __________ | __________ | __________ | __________ |
| 5 | (2, 2) | (2, 3) | __________ | __________ | __________ | __________ |

**How many steps required turning?** __________

**How many steps ran the while loop zero times (no turn)?** __________

**At which step did the robot change from row movement to column movement?** Step __________

---

## Part 5: Trace a Second Path

**Path:** [(1, 3), (0, 3), (0, 2), (0, 1), (0, 0)]
**Starting position:** (2, 3) &nbsp;&nbsp; **Starting heading:** 2 (S)

| Step | Position | Next | Desired | Current Heading | `turn_to` heading values | New Heading |
|---|---|---|---|---|---|---|
| 1 | (2, 3) | (1, 3) | __________ | 2 (S) | __________ | __________ |
| 2 | (1, 3) | (0, 3) | __________ | __________ | __________ | __________ |
| 3 | (0, 3) | (0, 2) | __________ | __________ | __________ | __________ |
| 4 | (0, 2) | (0, 1) | __________ | __________ | __________ | __________ |
| 5 | (0, 1) | (0, 0) | __________ | __________ | __________ | __________ |

**What is the robot's final heading after completing this path?** __________

---

## Part 6: Trace a Third Path

**Path:** [(1, 2), (1, 3), (2, 3), (3, 3)]
**Starting position:** (1, 1) &nbsp;&nbsp; **Starting heading:** 0 (N)

| Step | Position | Next | Desired | Current Heading | `turn_to` heading values | New Heading |
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

**Scenario A:** Facing 0 (N), desired 1 (E)

```
  Before turn:        After turn:
  +-------+           +-------+
  |       |           |       |
  |  [?]  |           |  [?]  |
  |       |           |       |
  +-------+           +-------+
  turn_to loop runs this many times: __________
```

**Scenario B:** Facing 1 (E), desired 2 (S)

```
  Before turn:        After turn:
  +-------+           +-------+
  |       |           |       |
  |  [?]  |           |  [?]  |
  |       |           |       |
  +-------+           +-------+
  turn_to loop runs this many times: __________
```

**Scenario C:** Facing 3 (W), desired 1 (E)

```
  Before turn:        After turn:
  +-------+           +-------+
  |       |           |       |
  |  [?]  |           |  [?]  |
  |       |           |       |
  +-------+           +-------+
  turn_to loop runs this many times: __________ (wrap triggered? ___)
```

**Scenario D:** Facing 2 (S), desired 2 (S)

```
  Before turn:        After turn:
  +-------+           +-------+
  |       |           |       |
  |  [?]  |           |  [?]  |
  |       |           |       |
  +-------+           +-------+
  turn_to loop runs this many times: __________
```

---

## Part 8: Heading Logic in Code

Fill in the blanks to complete the `desired_heading` function:

```python
HEADING_NAMES = ["N", "E", "S", "W"]

def desired_heading(current_pos, next_pos):
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
```

**Test your understanding:**

**What does `desired_heading((0,0), (1,0))` return?** __________

**What does `desired_heading((2,3), (2,2))` return?** __________

**What does `desired_heading((1,1), (0,1))` return?** __________

*In the next lesson, you will type `turn_to` and `desired_heading` into the Navigator class and run them on the robot.*

---

## Reflection

**The Manhattan algorithm tells the robot WHERE to go; the `turn_to` while loop handles HOW to face the right direction. In one or two sentences, explain why adding 1 and wrapping 4 → 0 is enough to handle every turning case.**

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

---

**Next Lesson:** We'll build the **Navigator class** around these three methods and drive the robot along any path!
