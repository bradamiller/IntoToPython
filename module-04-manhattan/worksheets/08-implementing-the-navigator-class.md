# Lesson 8 Worksheet: Driving the Path

**Name:** ________________________
**Date:** ________________________

---

## Part A: Driving Function Design

The driving functions control the robot's movement along a Manhattan path. Answer the following questions about their design.

**1. List the two pieces of state that get threaded through the driving functions (as parameters and return values):**

| State | Type | Purpose |
|---|---|---|
| __________________ | __________________ | __________________ |
| __________________ | __________________ | __________________ |

**2. List the three driving functions:**

| Function Name | Input | Output |
|---|---|---|
| __________________ | __________________ | __________________ |
| __________________ | __________________ | __________________ |
| __________________ | __________________ | __________________ |

**3. Why do `turn_to()` and `drive_path()` need to `return` their updated values, instead of just changing a variable inside the function?**

____________________________________________________________________

____________________________________________________________________

**4. What functions does `drive_path()` call to physically move the robot? Where do they come from?**

____________________________________________________________________

---

## Part B: `desired_heading()` Exercises

Given the robot's current position and the next position, determine the desired heading number.

**Heading numbers:** 0 = N, 1 = E, 2 = S, 3 = W

**Remember:**
- Row increases --> South (heading 2)
- Row decreases --> North (heading 0)
- Col increases --> East (heading 1)
- Col decreases --> West (heading 3)

| Position | Next Position | row_diff | col_diff | Desired Heading |
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

## Part C: Trace `turn_to()` by Hand

```python
def turn_to(heading, desired):
    while heading != desired:
        turn_right()
        heading = heading + 1
        if heading == 4:
            heading = 0
    return heading
```

Each pass: turn right, add 1, wrap 4 → 0. Stop when `heading == desired`, then return it. List the heading values the loop produces. Write "already there" if the loop runs zero times.

| Current | Desired | heading values during turn_to | Total Turns | Returned |
|---|---|---|---|---|
| 0 (N) | 1 (E) | 0 → ___ | _____ | _____ |
| 0 (N) | 2 (S) | 0 → ___ → ___ | _____ | _____ |
| 1 (E) | 1 (E) | __________ | _____ | _____ |
| 1 (E) | 0 (N) | 1 → ___ → ___ → ___ (wrap) | _____ | _____ |
| 2 (S) | 3 (W) | 2 → ___ | _____ | _____ |
| 2 (S) | 0 (N) | 2 → ___ → ___ (wrap) | _____ | _____ |
| 3 (W) | 2 (S) | 3 → ___ (wrap) → ___ → ___ | _____ | _____ |
| 3 (W) | 1 (E) | 3 → ___ (wrap) → ___ | _____ | _____ |
| 0 (N) | 3 (W) | 0 → ___ → ___ → ___ | _____ | _____ |
| 1 (E) | 3 (W) | 1 → ___ → ___ | _____ | _____ |

**How many of the 10 scenarios ran the while loop zero times?** __________

**Which scenarios triggered the wrap from 4 back to 0?** __________

**What would go wrong if `turn_to()` were missing its `return heading` line?**

____________________________________________________________________

---

## Part D: `drive_path()` Tracing

Trace through the entire `drive_path()` function for the given path. For each step, list the heading values produced by `turn_to` (or "already there" if no turn).

**Path:** `[(1, 0), (2, 0), (2, 1), (2, 2)]`
**Starting position:** (0, 0)
**Starting heading:** 0 (N)

| Step | next_pos | Desired | Current | `turn_to` heading values | New Heading | New Position |
|---|---|---|---|---|---|---|
| 1 | (1, 0) | __________ | 0 (N) | __________ | __________ | (1, 0) |
| 2 | (2, 0) | __________ | __________ | __________ | __________ | (2, 0) |
| 3 | (2, 1) | __________ | __________ | __________ | __________ | (2, 1) |
| 4 | (2, 2) | __________ | __________ | __________ | __________ | (2, 2) |

**What does `drive_path()` return after this trace?** `(__________, __________)`

---

**Now trace a second path:**

**Path:** `[(3, 2), (3, 1), (2, 1), (1, 1), (0, 1)]`
**Starting position:** (3, 3)
**Starting heading:** 1 (E)

| Step | next_pos | Desired | Current | `turn_to` heading values | New Heading | New Position |
|---|---|---|---|---|---|---|
| 1 | (3, 2) | __________ | 1 (E) | __________ | __________ | (3, 2) |
| 2 | (3, 1) | __________ | __________ | __________ | __________ | (3, 1) |
| 3 | (2, 1) | __________ | __________ | __________ | __________ | (2, 1) |
| 4 | (1, 1) | __________ | __________ | __________ | __________ | (1, 1) |
| 5 | (0, 1) | __________ | __________ | __________ | __________ | (0, 1) |

**What does `drive_path()` return after this trace?** `(__________, __________)`

---

## Part E: Code Completion

Fill in the blanks to complete the driving functions.

```python
HEADING_NAMES = ["N", "E", "S", "W"]

def desired_heading(position, next_pos):
    row_diff = next_pos[____] - position[____]
    col_diff = next_pos[____] - position[____]
    if row_diff == -1:
        return ____
    elif col_diff == 1:
        return ____
    elif row_diff == 1:
        return ____
    elif col_diff == -1:
        return ____

def turn_to(heading, desired):
    while heading != __________:
        ______________()
        heading = heading + __________
        if heading == __________:
            heading = __________
    return __________

def drive_path(path, position, heading):
    for next_pos in ____________:
        needed = desired_heading(____________, ____________)
        if heading == ____________:
            ______________()
        heading = turn_to(____________, ____________)
        track_until_cross()
        position = ____________
    return ____________, ____________
```

**Why does `drive_path()` call `clear_intersection()` only when the robot is already facing the right way?**

____________________________________________________________________

**Why does the loop iterate directly with `for next_pos in path:` instead of skipping elements?**

____________________________________________________________________

---

## Reflection

**`drive_path()` reuses your Module 2/3 driving toolkit (`turn_right()`, `track_until_cross()`, `clear_intersection()`) instead of controlling motors directly. Why is this a good design choice?**

____________________________________________________________________

____________________________________________________________________

____________________________________________________________________

---

**Next Lesson:** We combine `compute_manhattan_path()` and `drive_path()` into a complete multi-destination navigation program for the Final Project!

---

## Answer Key

### Part A
1. `position` (tuple) -- current (row, col) on the grid; `heading` (int) -- direction robot faces (0=N, 1=E, 2=S, 3=W)
2. `desired_heading(position, next_pos)` -- returns heading number 0-3; `turn_to(heading, desired)` -- turns right until heading matches desired, returns the new heading; `drive_path(path, position, heading)` -- drives through the entire path, returns `(position, heading)`
3. Because `position` and `heading` are local variables inside each function -- changes made to a parameter inside a function do not affect anything outside it. The only way the caller can see the updated values is if the function returns them and the caller reassigns its own variables from that return value.
4. It calls `turn_right()`, `track_until_cross()`, and `clear_intersection()` -- the driving toolkit built in Module 2 and reused in Module 3.

### Part B

| Position | Next Position | row_diff | col_diff | Desired Heading |
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

| Current | Desired | heading values during turn_to | Total Turns | Returned |
|---|---|---|---|---|
| 0 (N) | 1 (E) | 0 → **1** | **1** | **1** |
| 0 (N) | 2 (S) | 0 → **1** → **2** | **2** | **2** |
| 1 (E) | 1 (E) | **already there** | **0** | **1** |
| 1 (E) | 0 (N) | 1 → **2** → **3** → **0 (wrap)** | **3** | **0** |
| 2 (S) | 3 (W) | 2 → **3** | **1** | **3** |
| 2 (S) | 0 (N) | 2 → **3** → **0 (wrap)** | **2** | **0** |
| 3 (W) | 2 (S) | 3 → **0 (wrap)** → **1** → **2** | **3** | **2** |
| 3 (W) | 1 (E) | 3 → **0 (wrap)** → **1** | **2** | **1** |
| 0 (N) | 3 (W) | 0 → **1** → **2** → **3** | **3** | **3** |
| 1 (E) | 3 (W) | 1 → **2** → **3** | **2** | **3** |

- Zero-turn scenarios: **1** (the `1 (E) → 1 (E)` row)
- Wrap-triggering scenarios: the four rows where the loop crosses 3 → 0
- Without `return heading`, the caller's `heading` variable would never update -- the function would compute the correct value internally and then discard it, and every subsequent call to `turn_to` would start from the wrong heading.

### Part D -- First Path

| Step | next_pos | Desired | Current | `turn_to` heading values | New Heading | New Position |
|---|---|---|---|---|---|---|
| 1 | (1, 0) | 2 (S) | 0 (N) | 0 → 1 → 2 | 2 (S) | (1, 0) |
| 2 | (2, 0) | 2 (S) | 2 (S) | already there | 2 (S) | (2, 0) |
| 3 | (2, 1) | 1 (E) | 2 (S) | 2 → 3 → 0 (wrap) → 1 | 1 (E) | (2, 1) |
| 4 | (2, 2) | 1 (E) | 1 (E) | already there | 1 (E) | (2, 2) |

`drive_path()` returns `((2, 2), 1)`.

### Part D -- Second Path

| Step | next_pos | Desired | Current | `turn_to` heading values | New Heading | New Position |
|---|---|---|---|---|---|---|
| 1 | (3, 2) | 3 (W) | 1 (E) | 1 → 2 → 3 | 3 (W) | (3, 2) |
| 2 | (3, 1) | 3 (W) | 3 (W) | already there | 3 (W) | (3, 1) |
| 3 | (2, 1) | 0 (N) | 3 (W) | 3 → 0 (wrap) | 0 (N) | (2, 1) |
| 4 | (1, 1) | 0 (N) | 0 (N) | already there | 0 (N) | (1, 1) |
| 5 | (0, 1) | 0 (N) | 0 (N) | already there | 0 (N) | (0, 1) |

`drive_path()` returns `((0, 1), 0)`.

### Part E
```python
HEADING_NAMES = ["N", "E", "S", "W"]

def desired_heading(position, next_pos):
    row_diff = next_pos[0] - position[0]
    col_diff = next_pos[1] - position[1]
    if row_diff == -1:
        return 0
    elif col_diff == 1:
        return 1
    elif row_diff == 1:
        return 2
    elif col_diff == -1:
        return 3

def turn_to(heading, desired):
    while heading != desired:
        turn_right()
        heading = heading + 1
        if heading == 4:
            heading = 0
    return heading

def drive_path(path, position, heading):
    for next_pos in path:
        needed = desired_heading(position, next_pos)
        if heading == needed:
            clear_intersection()
        heading = turn_to(heading, needed)
        track_until_cross()
        position = next_pos
    return position, heading
```

**Blanks (in order):** `0`, `0`, `1`, `1`, `0`, `1`, `2`, `3` (desired_heading's row_diff/col_diff indices and return values) — `desired`, `turn_right`, `1`, `4`, `0`, `heading` (turn_to) — `path`, `position, next_pos`, `needed`, `clear_intersection`, `heading, needed`, `next_pos`, `position, heading` (drive_path)

`clear_intersection()` is called only when the robot is already facing the right direction. In that case no turn happens, so the robot is still sitting on the previous intersection. It drives forward 8 cm to clear the cross before `track_until_cross()` starts looking for the next crossing line. When a turn does happen, the turning motion itself clears the intersection (via `turn_right()`'s own call to `clear_intersection()`).

The loop iterates directly with `for next_pos in path:` because the path does not include the starting position -- every element is a new cell to drive to.

---

## Part F (Optional Extension): The Navigator Class

*Skip this section if your course doesn't cover classes.*

1. **Fill in the blanks to turn the driving functions into a `Navigator` class:**

   ```python
   class Navigator:

       def __init__(self, start, heading):
           self.position = __________
           self.heading = __________
           self.line_track = __________

       def desired_heading(self, next_pos):
           row_diff = next_pos[0] - self.__________[0]
           col_diff = next_pos[1] - self.__________[1]
           # ... same four if/elif branches

       def turn_to(self, desired):
           while self.heading != desired:
               self.line_track.__________()
               self.heading = self.heading + 1
               if self.heading == 4:
                   self.heading = 0
           # Note: no return statement needed here. Why not?
           # _________________________________________________

       def drive_path(self, path):
           for next_pos in path:
               needed = self.desired_heading(next_pos)
               if self.heading == needed:
                   self.line_track.clear_intersection()
               self.__________(needed)
               self.line_track.track_until_cross()
               self.position = next_pos
   ```

2. **In the functions version, the caller writes:**
   ```python
   position, heading = drive_path(path, position, heading)
   ```
   **What does the equivalent class-version call look like?**

   ```python
   _______________________________________________
   ```

3. **Why doesn't the class version's `drive_path` need a `return` statement, while the functions version does?**

   _________________________________________________________________
