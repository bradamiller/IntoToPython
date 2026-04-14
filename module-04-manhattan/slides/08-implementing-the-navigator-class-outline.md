# Lesson 8 Slide Outline: Implementing the Navigator Class

## Slide 1: Title & Learning Objectives
**Title:** Implementing the Navigator Class

**Learning Objectives:**
- Build the Navigator class with `self.position` and `self.heading`
- Translate the three methods from Lesson 7 into Python: `desired_heading`, `turn_to`, `drive_path`
- Reuse `LineTrack` from Module 2 for physical movement
- Run the full Manhattan + Navigator program on the robot

**Agenda:**
- Class skeleton (5 min)
- Method 1: `desired_heading` (5 min)
- Method 2: `turn_to` (5 min)
- Method 3: `drive_path` (10 min)
- Run it on the robot (20 min)

---

## Slide 2: From Paper to Python
Yesterday you designed three methods on paper. Today you type them in and run them on the robot.

- **desired_heading(current, next_pos)** — which of the 4 cases, 0/1/2/3
- **turn_to(desired)** — turn right, wrap 4→0, stop when aligned
- **drive_path(path)** — for each intersection: turn, then drive forward one

Nothing new to design. Just translate.

---

## Slide 3: Class Skeleton
Navigator needs two pieces of state and a robot to drive.

```python
from line_track import LineTrack

HEADING_NAMES = ["N", "E", "S", "W"]

class Navigator:
    def __init__(self, start, heading):
        self.position = start
        self.heading = heading
        self.line_track = LineTrack()
```

**Usage:**
```python
nav = Navigator((0, 0), 0)   # at (0,0), facing North
```

Place the robot on the grid facing North so its physical direction matches `heading = 0`.

---

## Slide 4: Method 1 — desired_heading
Exactly the function from Lesson 7, now as a method on Navigator that uses `self.position`:

```python
def desired_heading(self, next_pos):
    row_diff = next_pos[0] - self.position[0]
    col_diff = next_pos[1] - self.position[1]
    if row_diff == -1: return 0   # North
    if col_diff ==  1: return 1   # East
    if row_diff ==  1: return 2   # South
    if col_diff == -1: return 3   # West
```

---

## Slide 5: Method 2 — turn_to
Same while loop from Lesson 7, now calling the real robot:

```python
def turn_to(self, desired):
    while self.heading != desired:
        self.line_track.turn_right()
        self.heading = self.heading + 1
        if self.heading == 4:
            self.heading = 0
```

Each pass turns the robot right by 90° and updates `self.heading`. The `if self.heading == 4` line wraps back to 0.

---

## Slide 6: Method 3 — drive_path
For each intersection in the path: turn to face it, then drive forward one intersection.

```python
def drive_path(self, path):
    for next_pos in path:
        desired = self.desired_heading(next_pos)
        if self.heading == desired:
            self.line_track.drivetrain.straight(8)   # clear the cross
        self.turn_to(desired)
        self.line_track.track_until_cross()          # drive to the next
        self.position = next_pos
```

**Why the `if`?** If we need to turn, the turn itself moves the robot off the crossing line. If we're already facing the right way, we need to drive 8 cm first — otherwise `track_until_cross()` would re-detect the cross we're already sitting on.

---

## Slide 7: Run It
```python
from XRPLib.board import Board

board = Board.get_default_board()
manhattan = Manhattan((0, 0))
nav = Navigator((0, 0), 0)

board.wait_for_button()

path = manhattan.compute_path((2, 2))
print("Path:", path)

nav.drive_path(path)
print("Arrived facing", HEADING_NAMES[nav.heading])
```

Three classes working together: **Manhattan** plans, **Navigator** decides turns, **LineTrack** moves.

---

## Slide 8: Your Turn!
1. Type in the Navigator class with all three methods
2. Test a straight path first: `(0, 0) → (2, 0)` — no turns needed
3. Then a path with turns: `(0, 0) → (2, 2)`
4. Print `self.heading` inside `turn_to` so you can see the wrap 4→0 happen

**Checkpoints:**
- Does the robot turn the right number of times at each step?
- Does it land on each intersection (not before, not after)?
- Does `self.position` match the real robot at the end?

---

## Slide 9: What's Next
**Today:** You built the Navigator — three methods, each a direct translation of yesterday's paper design.

**Next lesson (Lesson 9 — Final Project):** Drive to a **list** of destinations in sequence, computing a fresh path for each one.
