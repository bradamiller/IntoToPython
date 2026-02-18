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

**4. What object does the Navigator use to physically move the robot? How does it get that object?**

____________________________________________________________________

---

## Part B: `get_needed_direction()` Exercises

Given the Navigator's current position and the next position, determine the direction (N, S, E, or W).

**Remember:**
- Row increases --> South
- Row decreases --> North
- Col increases --> East
- Col decreases --> West

| Navigator Position | Next Position | row_diff | col_diff | Direction |
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

For each scenario, determine what happens when `turn_to()` is called.

**Turn rules:**
- Same direction --> no turn (0 degrees)
- Right turn (clockwise) --> `drivetrain.turn(90)`
- Left turn (counterclockwise) --> `drivetrain.turn(-90)`
- Opposite direction --> `drivetrain.turn(180)`

| Current Heading | Needed Direction | Turn Type | Degrees | New Heading |
|---|---|---|---|---|
| N | E | Right | 90 | E |
| N | S | __________ | __________ | __________ |
| E | E | __________ | __________ | __________ |
| E | N | __________ | __________ | __________ |
| S | W | __________ | __________ | __________ |
| S | N | __________ | __________ | __________ |
| W | S | __________ | __________ | __________ |
| W | E | __________ | __________ | __________ |
| N | W | __________ | __________ | __________ |
| E | W | __________ | __________ | __________ |

**How many of the 10 scenarios above required NO turn?** __________

**How many required a 180-degree turn?** __________

---

## Part D: `drive_path()` Tracing

Trace through the entire `drive_path()` method for the given path. Fill in every column for each step.

**Path:** `[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]`
**Starting position:** (0, 0)
**Starting heading:** N

| Step (i) | next_pos | Needed Direction | Current Heading | Turn | Degrees | New Heading | New Position |
|---|---|---|---|---|---|---|---|
| 1 | (1, 0) | __________ | N | __________ | __________ | __________ | (1, 0) |
| 2 | (2, 0) | __________ | __________ | __________ | __________ | __________ | (2, 0) |
| 3 | (2, 1) | __________ | __________ | __________ | __________ | __________ | (2, 1) |
| 4 | (2, 2) | __________ | __________ | __________ | __________ | __________ | (2, 2) |

**Final position:** __________  **Final heading:** __________

---

**Now trace a second path:**

**Path:** `[(3, 3), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1)]`
**Starting position:** (3, 3)
**Starting heading:** E

| Step (i) | next_pos | Needed Direction | Current Heading | Turn | Degrees | New Heading | New Position |
|---|---|---|---|---|---|---|---|
| 1 | (3, 2) | __________ | E | __________ | __________ | __________ | (3, 2) |
| 2 | (3, 1) | __________ | __________ | __________ | __________ | __________ | (3, 1) |
| 3 | (2, 1) | __________ | __________ | __________ | __________ | __________ | (2, 1) |
| 4 | (1, 1) | __________ | __________ | __________ | __________ | __________ | (1, 1) |
| 5 | (0, 1) | __________ | __________ | __________ | __________ | __________ | (0, 1) |

**Final position:** __________  **Final heading:** __________

---

## Part E: Code Completion

Fill in the blanks to complete the Navigator class.

```python
from XRPLib.differential_drive import DifferentialDrive

class Navigator:

    def __init__(self, start, heading):
        self.position = __________
        self.heading = __________
        self.drivetrain = DifferentialDrive.get_default_differential_drive()

    def get_needed_direction(self, next_pos):
        row_diff = next_pos[____] - self.position[____]
        col_diff = next_pos[____] - self.position[____]
        if row_diff == 1:
            return "____"
        elif row_diff == -1:
            return "____"
        elif col_diff == 1:
            return "____"
        elif col_diff == -1:
            return "____"

    def turn_to(self, direction):
        right_turns = {"N": "E", "E": "S", "S": "____", "W": "____"}
        left_turns = {"N": "W", "W": "S", "S": "____", "E": "____"}

        if self.heading == direction:
            pass  # No turn needed
        elif right_turns[__________] == direction:
            self.drivetrain.turn(____)
            self.heading = __________
        elif left_turns[__________] == direction:
            self.drivetrain.turn(____)
            self.heading = __________
        else:
            self.drivetrain.turn(____)
            self.heading = __________

    def drive_path(self, path):
        for i in range(____, len(path)):
            next_pos = path[____]
            direction = self.get_needed_direction(____________)
            self.turn_to(____________)
            self.drivetrain.straight(20)
            self.position = ____________
```

**Why does the loop start at `range(1, ...)` instead of `range(0, ...)`?**

____________________________________________________________________

---

## Reflection

**The Manhattan class plans the path and the Navigator class drives the path. Why is it better to have two separate classes instead of one class that does both?**

____________________________________________________________________

____________________________________________________________________

____________________________________________________________________

---

**Next Lesson:** We combine Manhattan and Navigator into a complete multi-destination navigation program for the Final Project!

---

## Answer Key

### Part A
1. `position` (tuple) -- current (row, col) on the grid; `heading` (string) -- direction robot faces (N/S/E/W); `drivetrain` (DifferentialDrive) -- controls the robot's motors
2. `get_needed_direction(next_pos)` -- returns N/S/E/W; `turn_to(direction)` -- turns robot to face direction; `drive_path(path)` -- drives through entire path
3. The Navigator tracks its own position because it updates after each drive. The Manhattan class tracks position for path planning. Each class manages its own state.
4. It uses a `DifferentialDrive` object, obtained by calling `DifferentialDrive.get_default_differential_drive()` in `__init__`.

### Part B

| Navigator Position | Next Position | row_diff | col_diff | Direction |
|---|---|---|---|---|
| (0, 0) | (1, 0) | 1 | 0 | S |
| (2, 1) | (1, 1) | -1 | 0 | N |
| (1, 2) | (1, 3) | 0 | 1 | E |
| (3, 3) | (3, 2) | 0 | -1 | W |
| (0, 1) | (1, 1) | 1 | 0 | S |
| (2, 0) | (2, 1) | 0 | 1 | E |
| (3, 2) | (2, 2) | -1 | 0 | N |
| (1, 3) | (1, 2) | 0 | -1 | W |

### Part C

| Current Heading | Needed Direction | Turn Type | Degrees | New Heading |
|---|---|---|---|---|
| N | E | Right | 90 | E |
| N | S | 180 | 180 | S |
| E | E | None | 0 | E |
| E | N | Left | -90 | N |
| S | W | Right | 90 | W |
| S | N | 180 | 180 | N |
| W | S | Left | -90 | S |
| W | E | 180 | 180 | E |
| N | W | Left | -90 | W |
| E | W | 180 | 180 | W |

No turn: 1 scenario. 180-degree turn: 3 scenarios.

### Part D -- First Path

| Step | next_pos | Needed Direction | Current Heading | Turn | Degrees | New Heading | New Position |
|---|---|---|---|---|---|---|---|
| 1 | (1, 0) | S | N | 180 | 180 | S | (1, 0) |
| 2 | (2, 0) | S | S | None | 0 | S | (2, 0) |
| 3 | (2, 1) | E | S | Left | -90 | E | (2, 1) |
| 4 | (2, 2) | E | E | None | 0 | E | (2, 2) |

Final position: (2, 2). Final heading: E.

### Part D -- Second Path

| Step | next_pos | Needed Direction | Current Heading | Turn | Degrees | New Heading | New Position |
|---|---|---|---|---|---|---|---|
| 1 | (3, 2) | W | E | 180 | 180 | W | (3, 2) |
| 2 | (3, 1) | W | W | None | 0 | W | (3, 1) |
| 3 | (2, 1) | N | W | Right | 90 | N | (2, 1) |
| 4 | (1, 1) | N | N | None | 0 | N | (1, 1) |
| 5 | (0, 1) | N | N | None | 0 | N | (0, 1) |

Final position: (0, 1). Final heading: N.

### Part E
```python
from XRPLib.differential_drive import DifferentialDrive

class Navigator:

    def __init__(self, start, heading):
        self.position = start
        self.heading = heading
        self.drivetrain = DifferentialDrive.get_default_differential_drive()

    def get_needed_direction(self, next_pos):
        row_diff = next_pos[0] - self.position[0]
        col_diff = next_pos[1] - self.position[1]
        if row_diff == 1:
            return "S"
        elif row_diff == -1:
            return "N"
        elif col_diff == 1:
            return "E"
        elif col_diff == -1:
            return "W"

    def turn_to(self, direction):
        right_turns = {"N": "E", "E": "S", "S": "W", "W": "N"}
        left_turns = {"N": "W", "W": "S", "S": "E", "E": "N"}

        if self.heading == direction:
            pass
        elif right_turns[self.heading] == direction:
            self.drivetrain.turn(90)
            self.heading = direction
        elif left_turns[self.heading] == direction:
            self.drivetrain.turn(-90)
            self.heading = direction
        else:
            self.drivetrain.turn(180)
            self.heading = direction

    def drive_path(self, path):
        for i in range(1, len(path)):
            next_pos = path[i]
            direction = self.get_needed_direction(next_pos)
            self.turn_to(direction)
            self.drivetrain.straight(20)
            self.position = next_pos
```

The loop starts at 1 because index 0 is the starting position -- the robot is already there and does not need to drive to it.
