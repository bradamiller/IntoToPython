# Lesson 7 Worksheet: The Challenge of Turning

**Name:** ________________________
**Date:** ________________________

---

## Part 1: Direction from Coordinates

Given two consecutive coordinates, determine the direction the robot must travel (N, S, E, or W).

**Remember:**
- Row increases by 1 --> South (moving down)
- Row decreases by 1 --> North (moving up)
- Col increases by 1 --> East (moving right)
- Col decreases by 1 --> West (moving left)

| Current Position | Next Position | row_diff | col_diff | Direction |
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

## Part 2: The Turn Table

Fill in the complete turn table. For each combination of current heading and needed direction, write the turn: **None**, **Right 90**, **Left 90**, or **180**.

**Hints:**
- Right turns go clockwise: N --> E --> S --> W --> N
- Left turns go counterclockwise: N --> W --> S --> E --> N

| Current Heading | Need N | Need S | Need E | Need W |
|---|---|---|---|---|
| N | __________ | __________ | __________ | __________ |
| S | __________ | __________ | __________ | __________ |
| E | __________ | __________ | __________ | __________ |
| W | __________ | __________ | __________ | __________ |

**How many cells say "None"?** __________  **Why?** ____________________________

**How many cells say "180"?** __________  **What pattern do you notice about where they appear?**

____________________________________________________________________

---

## Part 3: Determine the Turn

For each scenario, use the turn table from Part 2 to determine what turn the robot must make.

| Scenario | Current Heading | Needed Direction | Turn |
|---|---|---|---|
| 1 | N | E | __________ |
| 2 | E | E | __________ |
| 3 | S | N | __________ |
| 4 | W | S | __________ |
| 5 | E | N | __________ |
| 6 | N | W | __________ |
| 7 | S | W | __________ |
| 8 | W | E | __________ |

---

## Part 4: Trace a Path with Heading Updates

**Path:** [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]
**Starting heading:** North

For each step, determine the needed direction, the turn, and the new heading after turning.

| Step | From | To | Needed Direction | Current Heading | Turn | New Heading |
|---|---|---|---|---|---|---|
| 1 | (0, 0) | (1, 0) | __________ | N | __________ | __________ |
| 2 | (1, 0) | (2, 0) | __________ | __________ | __________ | __________ |
| 3 | (2, 0) | (2, 1) | __________ | __________ | __________ | __________ |
| 4 | (2, 1) | (2, 2) | __________ | __________ | __________ | __________ |
| 5 | (2, 2) | (2, 3) | __________ | __________ | __________ | __________ |

**How many turns were needed?** __________

**How many times was no turn needed?** __________

**At which step did the robot change from row movement to column movement?** Step __________

---

## Part 5: Trace a Second Path

**Path:** [(2, 3), (1, 3), (0, 3), (0, 2), (0, 1), (0, 0)]
**Starting heading:** South

| Step | From | To | Needed Direction | Current Heading | Turn | New Heading |
|---|---|---|---|---|---|---|
| 1 | (2, 3) | (1, 3) | __________ | S | __________ | __________ |
| 2 | (1, 3) | (0, 3) | __________ | __________ | __________ | __________ |
| 3 | (0, 3) | (0, 2) | __________ | __________ | __________ | __________ |
| 4 | (0, 2) | (0, 1) | __________ | __________ | __________ | __________ |
| 5 | (0, 1) | (0, 0) | __________ | __________ | __________ | __________ |

**What is the robot's final heading after completing this path?** __________

---

## Part 6: Trace a Third Path

**Path:** [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3)]
**Starting heading:** North

| Step | From | To | Needed Direction | Current Heading | Turn | New Heading |
|---|---|---|---|---|---|---|
| 1 | (1, 1) | (1, 2) | __________ | N | __________ | __________ |
| 2 | (1, 2) | (1, 3) | __________ | __________ | __________ | __________ |
| 3 | (1, 3) | (2, 3) | __________ | __________ | __________ | __________ |
| 4 | (2, 3) | (3, 3) | __________ | __________ | __________ | __________ |

**What is the robot's final heading?** __________

**Does the first step require a turn? Why?**

____________________________________________________________________

---

## Part 7: Robot Orientation Diagrams

For each scenario, draw an arrow inside the box showing which way the robot is facing. Then draw a curved arrow showing the turn it needs to make, and draw the final facing direction.

**Scenario A:** Facing North, need to go East

```
  Before turn:        After turn:
  +-------+           +-------+
  |       |           |       |
  |  [?]  |           |  [?]  |
  |       |           |       |
  +-------+           +-------+
  Turn: __________
```

**Scenario B:** Facing East, need to go South

```
  Before turn:        After turn:
  +-------+           +-------+
  |       |           |       |
  |  [?]  |           |  [?]  |
  |       |           |       |
  +-------+           +-------+
  Turn: __________
```

**Scenario C:** Facing West, need to go East

```
  Before turn:        After turn:
  +-------+           +-------+
  |       |           |       |
  |  [?]  |           |  [?]  |
  |       |           |       |
  +-------+           +-------+
  Turn: __________
```

**Scenario D:** Facing South, need to go South

```
  Before turn:        After turn:
  +-------+           +-------+
  |       |           |       |
  |  [?]  |           |  [?]  |
  |       |           |       |
  +-------+           +-------+
  Turn: __________
```

---

## Part 8: Turn Logic in Code

Fill in the blanks to complete the turn logic:

```python
right_turns = {"N": "___", "E": "___", "S": "___", "W": "___"}
left_turns  = {"N": "___", "W": "___", "S": "___", "E": "___"}

def get_turn(current_heading, needed_direction):
    if current_heading == needed_direction:
        return "________"
    elif right_turns[__________] == needed_direction:
        return "________"
    elif left_turns[__________] == needed_direction:
        return "________"
    else:
        return "________"
```

**Test your understanding -- what does `get_turn("E", "N")` return?** __________

**What does `get_turn("W", "W")` return?** __________

**What does `get_turn("N", "S")` return?** __________

---

## Reflection

**The Manhattan algorithm tells the robot WHERE to go, but the turning logic tells it HOW to get there. Why do you think we separated these two problems instead of solving them together?**

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

---

**Next Lesson:** We'll implement the turning logic in a **Navigator class** that can drive the robot along any path!
