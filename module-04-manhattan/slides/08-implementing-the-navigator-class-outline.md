# Lesson 8 Slide Outline: Driving the Path

## Slide 1: Title & Learning Objectives
**Title:** Driving the Path

**Learning Objectives:**
- Thread `position` and `heading` through parameters and return values
- Translate the three functions from Lesson 7 into Python: `desired_heading`, `turn_to`, `drive_path`
- Reuse the driving toolkit from Module 2/3 for physical movement
- Run the full Manhattan + driving-functions program on the robot

**Agenda:**
- Why no class is needed (5 min)
- Function 1: `desired_heading` (5 min)
- Function 2: `turn_to` (5 min)
- Function 3: `drive_path` (10 min)
- Run it on the robot (20 min)

---

## Slide 2: From Paper to Python
Yesterday you designed three functions on paper. Today you type them in and run them on the robot.

- **desired_heading(position, next_pos)** — which of the 4 cases, 0/1/2/3
- **turn_to(heading, desired)** — turn right, wrap 4→0, return the new heading
- **drive_path(path, position, heading)** — for each intersection: turn, drive forward, return the final position/heading

Nothing new to design. Just translate.

---

## Slide 3: Why No Class Is Needed
There's only ever one robot -- one position, one heading. No need to store that on an object.

```python
HEADING_NAMES = ["N", "E", "S", "W"]

position = (0, 0)
heading = 0   # facing North
```

**The pattern:**
```python
position, heading = drive_path(path, position, heading)
```

Same tuple-unpacking pattern from Module 4 Lesson 2 -- just returning **two** values instead of one. Place the robot on the grid facing North so its physical direction matches `heading = 0`.

---

## Slide 4: Function 1 — desired_heading
The exact function from Lesson 7 -- `position` is a parameter, not `self.position`:

```python
def desired_heading(position, next_pos):
    row_diff = next_pos[0] - position[0]
    col_diff = next_pos[1] - position[1]
    if row_diff == -1: return 0   # North
    if col_diff ==  1: return 1   # East
    if row_diff ==  1: return 2   # South
    if col_diff == -1: return 3   # West
```

---

## Slide 5: Function 2 — turn_to
Same while loop from Lesson 7, now calling the real robot -- and returning the updated heading:

```python
def turn_to(heading, desired):
    while heading != desired:
        turn_right()
        heading = heading + 1
        if heading == 4:
            heading = 0
    return heading
```

Each pass turns the robot right by 90° and updates the local `heading`. Forgetting `return heading` is the #1 bug in this lesson -- the caller's heading would never update.

---

## Slide 6: Function 3 — drive_path
For each intersection in the path: turn to face it, then drive forward one intersection.

```python
def drive_path(path, position, heading):
    for next_pos in path:
        needed = desired_heading(position, next_pos)
        if heading == needed:
            clear_intersection()          # already facing right way
        heading = turn_to(heading, needed)
        track_until_cross()               # drive to the next
        position = next_pos
    return position, heading
```

**Why the `if`?** If we need to turn, the turn itself moves the robot off the crossing line. If we're already facing the right way, we call `clear_intersection()` first -- otherwise `track_until_cross()` would re-detect the cross we're already sitting on.

---

## Slide 7: Run It
```python
from XRPLib.board import Board

board = Board.get_default_board()
position = (0, 0)
heading = 0

board.wait_for_button()

path = compute_manhattan_path(position, (2, 2))
print("Path:", path)

position, heading = drive_path(path, position, heading)
print("Arrived facing", HEADING_NAMES[heading])
```

Three toolkits working together: the **Manhattan function** plans, **drive_path** decides turns, the **driving toolkit** moves.

---

## Slide 8: Your Turn!
1. Type in all three functions: `desired_heading`, `turn_to`, `drive_path`
2. Test a straight path first: `(0, 0) → (2, 0)` — no turns needed
3. Then a path with turns: `(0, 0) → (2, 2)`
4. Print `heading` inside `turn_to` so you can see the wrap 4→0 happen

**Checkpoints:**
- Does the robot turn the right number of times at each step?
- Does it land on each intersection (not before, not after)?
- Did you remember `position, heading = drive_path(...)` to capture the result?

---

## Slide 9: What's Next
**Today:** You built the driving functions — three functions, each a direct translation of yesterday's paper design, threading position and heading through parameters and return values instead of storing them on an object.

**Next lesson (Lesson 9 — Final Project):** Drive to a **list** of destinations in sequence, computing a fresh path for each one.

**Optional Extension:** Courses that also cover classes can package these same three functions as a `Navigator` class that composes `LineTrack` -- see the lesson document.
