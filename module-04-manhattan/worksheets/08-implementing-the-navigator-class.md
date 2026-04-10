# Lesson 8 Worksheet: Implementing the Navigator Class

**Name:** ________________________
**Date:** ________________________

---

## Part A: Navigator Class Design

The Navigator class controls the robot's movement along a Manhattan path. Answer the following questions about its design.

**1. List the three attributes the Navigator class needs to store:**

| Attribute | Type | Purpose |
|---|---|---|
| __________________ | __________________ | __________________ |
| __________________ | __________________ | __________________ |
| __________________ | __________________ | __________________ |

**2. List the three main methods the Navigator class needs (not counting `__init__`):**

| Method Name | Input | Output / Action |
|---|---|---|
| __________________ | __________________ | __________________ |
| __________________ | __________________ | __________________ |
| __________________ | __________________ | __________________ |

**3. Why does the Navigator class store its own `position` instead of getting it from the Manhattan class?**

____________________________________________________________________

____________________________________________________________________

**4. What object does the Navigator use to physically move the robot? Where does that object come from?**

____________________________________________________________________

---

## Part B: `get_needed_heading()` Exercises

Given the Navigator's current position and the next position, determine the needed heading number.

**Heading numbers:** 0 = N, 1 = E, 2 = S, 3 = W

**Remember:**
- Row increases --> South (heading 2)
- Row decreases --> North (heading 0)
- Col increases --> East (heading 1)
- Col decreases --> West (heading 3)

| Navigator Position | Next Position | row_diff | col_diff | Heading |
|---|---|---|---|---|
| (0, 0) | (1, 0) | 1 - 0 = ____ | 0 - 0 = ____ | __________ |
| (2, 1) | (1, 1) | 1 - 2 = ____ | 1 - 1 = ____ | __________ |
| (1, 2) | (1, 3) | ____ | ____ | __________ |
| (3, 3) | (3, 2) | ____ | ____ | __________ |
| (0, 1) | (1, 1) | ____ | ____ | __________ |
| (2, 0) | (2, 1) | ____ | ____ | __________ |
| (3, 2) | (2, 2) | ____ | ____ | __________ |
| (1, 3) | (1, 2) | ____ | ____ | __________ |

---

## Part C: `turn_to()` Exercises

For each scenario, count clockwise steps from current heading to needed heading to find the number of right turns. Headings go clockwise: 0(N) -> 1(E) -> 2(S) -> 3(W) -> back to 0(N).

| Current Heading | Needed Heading | Clockwise Steps | Right Turns | New Heading |
|---|---|---|---|---|
| 0 (N) | 1 (E) | 0->1 = 1 | 1 | 1 (E) |
| 0 (N) | 2 (S) | 0->1->2 = ____ | __________ | __________ |
| 1 (E) | 1 (E) | already there = ____ | __________ | __________ |
| 1 (E) | 0 (N) | 1->2->3->0 = ____ | __________ | __________ |
| 2 (S) | 3 (W) | 2->3 = ____ | __________ | __________ |
| 2 (S) | 0 (N) | 2->3->0 = ____ | __________ | __________ |
| 3 (W) | 2 (S) | 3->0->1->2 = ____ | __________ | __________ |
| 3 (W) | 1 (E) | 3->0->1 = ____ | __________ | __________ |
| 0 (N) | 3 (W) | 0->1->2->3 = ____ | __________ | __________ |
| 1 (E) | 3 (W) | 1->2->3 = ____ | __________ | __________ |

**How many of the 10 scenarios above required 0 right turns?** __________

**How many required 2 right turns (a 180)?** __________

---

## Part D: `drive_path()` Tracing

Trace through the entire `drive_path()` method for the given path. Fill in every column for each step.

**Path:** `[(1, 0), (2, 0), (2, 1), (2, 2)]`
**Starting position:** (0, 0)
**Starting heading:** 0 (N)

| Step | next_pos | Needed Heading | Current Heading | Right Turns | New Heading | New Position |
|---|---|---|---|---|---|---|
| 1 | (1, 0) | __________ | 0 (N) | __________ | __________ | (1, 0) |
| 2 | (2, 0) | __________ | __________ | __________ | __________ | (2, 0) |
| 3 | (2, 1) | __________ | __________ | __________ | __________ | (2, 1) |
| 4 | (2, 2) | __________ | __________ | __________ | __________ | (2, 2) |

**Final position:** __________  **Final heading:** __________

---

**Now trace a second path:**

**Path:** `[(3, 2), (3, 1), (2, 1), (1, 1), (0, 1)]`
**Starting position:** (3, 3)
**Starting heading:** 1 (E)

| Step | next_pos | Needed Heading | Current Heading | Right Turns | New Heading | New Position |
|---|---|---|---|---|---|---|
| 1 | (3, 2) | __________ | 1 (E) | __________ | __________ | (3, 2) |
| 2 | (3, 1) | __________ | __________ | __________ | __________ | (3, 1) |
| 3 | (2, 1) | __________ | __________ | __________ | __________ | (2, 1) |
| 4 | (1, 1) | __________ | __________ | __________ | __________ | (1, 1) |
| 5 | (0, 1) | __________ | __________ | __________ | __________ | (0, 1) |

**Final position:** __________  **Final heading:** __________

---

## Part E: Code Completion

Fill in the blanks to complete the Navigator class.

```python
from line_track import LineTrack

HEADING_NAMES = ["N", "E", "S", "W"]

class Navigator:

    def __init__(self, start, heading):
        self.position = __________
        self.heading = __________
        self.line_track = __________

    def get_needed_heading(self, next_pos):
        row_diff = next_pos[____] - self.position[____]
        col_diff = next_pos[____] - self.position[____]
        if row_diff == -1:
            return ____
        elif col_diff == 1:
            return ____
        elif row_diff == 1:
            return ____
        elif col_diff == -1:
            return ____

    def turn_to(self, needed_heading):
        while self.heading != __________:
            self.line_track.______________()
            self.heading = self.heading + __________
            if self.heading == __________:
                self.heading = __________

    def drive_path(self, path):
        for next_pos in ____________:
            needed = self.get_needed_heading(____________)
            if self.heading == ____________:
                self.line_track.drivetrain.straight(____)
            self.turn_to(____________)
            self.line_track.track_until_cross()
            self.position = ____________
```

**Why does `drive_path()` call `self.line_track.drivetrain.straight(8)` when the robot is already facing the right way?**

____________________________________________________________________

**Why does the loop iterate directly with `for next_pos in path:` instead of skipping elements?**

____________________________________________________________________

---

## Reflection

**The Navigator class reuses your LineTrack class from Module 2. Why is this a good design choice?**

____________________________________________________________________

____________________________________________________________________

____________________________________________________________________

---

**Next Lesson:** We combine Manhattan and Navigator into a complete multi-destination navigation program for the Final Project!

---

## Answer Key

### Part A
1. `position` (tuple) -- current (row, col) on the grid; `heading` (int) -- direction robot faces (0=N, 1=E, 2=S, 3=W); `line_track` (LineTrack) -- controls robot movement using line tracking from Module 2
2. `get_needed_heading(next_pos)` -- returns heading number 0-3; `turn_to(needed_heading)` -- turns robot using right turns; `drive_path(path)` -- drives through entire path
3. The Navigator tracks its own position because it updates after each drive. The Manhattan class tracks position for path planning. Each class manages its own state.
4. It uses a `LineTrack` object, created by calling `LineTrack()` in `__init__`. The LineTrack class (from Module 2) provides `turn_right()` and `track_until_cross()` for physical movement.

### Part B

| Navigator Position | Next Position | row_diff | col_diff | Heading |
|---|---|---|---|---|
| (0, 0) | (1, 0) | 1 | 0 | 2 (S) |
| (2, 1) | (1, 1) | -1 | 0 | 0 (N) |
| (1, 2) | (1, 3) | 0 | 1 | 1 (E) |
| (3, 3) | (3, 2) | 0 | -1 | 3 (W) |
| (0, 1) | (1, 1) | 1 | 0 | 2 (S) |
| (2, 0) | (2, 1) | 0 | 1 | 1 (E) |
| (3, 2) | (2, 2) | -1 | 0 | 0 (N) |
| (1, 3) | (1, 2) | 0 | -1 | 3 (W) |

### Part C

| Current Heading | Needed Heading | Clockwise Steps | Right Turns | New Heading |
|---|---|---|---|---|
| 0 (N) | 1 (E) | 0->1 = 1 | 1 | 1 (E) |
| 0 (N) | 2 (S) | 0->1->2 = 2 | 2 | 2 (S) |
| 1 (E) | 1 (E) | already there = 0 | 0 | 1 (E) |
| 1 (E) | 0 (N) | 1->2->3->0 = 3 | 3 | 0 (N) |
| 2 (S) | 3 (W) | 2->3 = 1 | 1 | 3 (W) |
| 2 (S) | 0 (N) | 2->3->0 = 2 | 2 | 0 (N) |
| 3 (W) | 2 (S) | 3->0->1->2 = 3 | 3 | 2 (S) |
| 3 (W) | 1 (E) | 3->0->1 = 2 | 2 | 1 (E) |
| 0 (N) | 3 (W) | 0->1->2->3 = 3 | 3 | 3 (W) |
| 1 (E) | 3 (W) | 1->2->3 = 2 | 2 | 3 (W) |

0 right turns: 1 scenario. 2 right turns (180): 4 scenarios.

### Part D -- First Path

| Step | next_pos | Needed Heading | Current Heading | Right Turns | New Heading | New Position |
|---|---|---|---|---|---|---|
| 1 | (1, 0) | 2 (S) | 0 (N) | count 0->1->2 = 2 | 2 (S) | (1, 0) |
| 2 | (2, 0) | 2 (S) | 2 (S) | already there = 0 | 2 (S) | (2, 0) |
| 3 | (2, 1) | 1 (E) | 2 (S) | count 2->3->0->1 = 3 | 1 (E) | (2, 1) |
| 4 | (2, 2) | 1 (E) | 1 (E) | already there = 0 | 1 (E) | (2, 2) |

Final position: (2, 2). Final heading: 1 (E).

### Part D -- Second Path

| Step | next_pos | Needed Heading | Current Heading | Right Turns | New Heading | New Position |
|---|---|---|---|---|---|---|
| 1 | (3, 2) | 3 (W) | 1 (E) | count 1->2->3 = 2 | 3 (W) | (3, 2) |
| 2 | (3, 1) | 3 (W) | 3 (W) | already there = 0 | 3 (W) | (3, 1) |
| 3 | (2, 1) | 0 (N) | 3 (W) | count 3->0 = 1 | 0 (N) | (2, 1) |
| 4 | (1, 1) | 0 (N) | 0 (N) | already there = 0 | 0 (N) | (1, 1) |
| 5 | (0, 1) | 0 (N) | 0 (N) | already there = 0 | 0 (N) | (0, 1) |

Final position: (0, 1). Final heading: 0 (N).

### Part E
```python
from line_track import LineTrack

HEADING_NAMES = ["N", "E", "S", "W"]

class Navigator:

    def __init__(self, start, heading):
        self.position = start
        self.heading = heading
        self.line_track = LineTrack()

    def get_needed_heading(self, next_pos):
        row_diff = next_pos[0] - self.position[0]
        col_diff = next_pos[1] - self.position[1]
        if row_diff == -1:
            return 0
        elif col_diff == 1:
            return 1
        elif row_diff == 1:
            return 2
        elif col_diff == -1:
            return 3

    def turn_to(self, needed_heading):
        while self.heading != needed_heading:
            self.line_track.turn_right()
            self.heading = self.heading + 1
            if self.heading == 4:
                self.heading = 0

    def drive_path(self, path):
        for next_pos in path:
            needed = self.get_needed_heading(next_pos)
            if self.heading == needed:
                self.line_track.drivetrain.straight(8)
            self.turn_to(needed)
            self.line_track.track_until_cross()
            self.position = next_pos
```

**Blanks:** **path**, **next_pos**, **needed**, **8**, **needed**, **next_pos**

`straight(8)` is called when the robot is already facing the right direction but is still sitting on the previous intersection. It needs to drive forward 8 cm to clear the intersection before `track_until_cross()` starts looking for the next crossing line.

The loop iterates directly with `for next_pos in path:` because the path does not include the starting position -- every element is a new cell to drive to.
