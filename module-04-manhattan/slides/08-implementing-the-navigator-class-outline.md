# Lesson 8 Slide Outline: Implementing the Navigator Class

## Slide 1: Title & Learning Objectives
**Title:** Implementing the Navigator Class

**Learning Objectives:**
- Design the Navigator class with position and heading
- Implement drive_path() to turn and drive through a path
- Track and update heading as the robot moves
- Integrate with LineTrack for physical movement (reusing Module 2!)

**Agenda:**
- Class design overview (5 min)
- Implementing helper methods (10 min)
- Building drive_path() (15 min)
- Testing on the robot (15 min)

---

## Slide 2: Hook — From Algorithm to Action
**We have TWO pieces working:**
1. Manhattan class computes the path (list of tuples)
2. Heading logic tells us what direction is needed

**Missing piece:** Something that actually DRIVES the robot!

```python
path = [(0,0), (1,0), (2,0), (2,1), (2,2)]
# How does this become real robot movement?
```

**Today:** Build the Navigator class that turns and drives through any path — reusing LineTrack from Module 2.

---

## Slide 3: Navigator Class Design
**What does the Navigator need?**

**Data (stored in __init__):**
- `self.position` — current (row, col) tuple
- `self.heading` — current heading number (0=N, 1=E, 2=S, 3=W)
- `self.line_track` — the LineTrack object from Module 2

**Methods:**
- `get_needed_heading(next_pos)` — what heading number to face
- `turn_to(needed_heading)` — turn robot using right turns
- `drive_path(path)` — drive the entire path

**Key idea:** We already know how to follow lines and detect crossings — LineTrack does that. Navigator just decides WHEN to turn and WHEN to go straight.

---

## Slide 4: The __init__ Method
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
nav = Navigator((0, 0), 0)
print("Position:", nav.position)                    # (0, 0)
print("Heading:", HEADING_NAMES[nav.heading])        # N
```

**Note:** Heading 0 means the robot faces North — make sure to place it that way on the grid!

**Reuse:** LineTrack() gives us `track_until_cross()` and `turn_right()` for free.

---

## Slide 5: get_needed_heading()
**Determine heading number from current position to next position:**

```python
def get_needed_heading(self, next_pos):
    row_diff = next_pos[0] - self.position[0]
    col_diff = next_pos[1] - self.position[1]

    if row_diff == -1:
        return 0      # North
    elif col_diff == 1:
        return 1      # East
    elif row_diff == 1:
        return 2      # South
    elif col_diff == -1:
        return 3      # West
```

**Example:**
```python
nav = Navigator((0, 0), 0)
needed = nav.get_needed_heading((1, 0))
print(HEADING_NAMES[needed])   # "S" — need heading 2 (row increases)
```

---

## Slide 6: turn_to() — Modular Arithmetic
**Turn the robot using right turns only:**

```python
def turn_to(self, needed_heading):
    turns = (needed_heading - self.heading) % 4
    for i in range(turns):
        self.line_track.turn_right()
    self.heading = needed_heading
```

**Why this works:**
- `(needed - current) % 4` always gives 0, 1, 2, or 3
- 0 turns = already facing right way
- 1 turn = one right turn (90 degrees)
- 2 turns = two right turns (180 degrees)
- 3 turns = three right turns (270 degrees = one left turn)

**No dictionaries needed!** One formula handles every case.

---

## Slide 7: drive_path()
**The main method — drive through every step in the path:**

```python
def drive_path(self, path):
    for i in range(1, len(path)):
        next_pos = path[i]
        needed = self.get_needed_heading(next_pos)
        turns = (needed - self.heading) % 4
        if turns == 0:
            self.line_track.drivetrain.straight(8)
        self.turn_to(needed)
        self.line_track.track_until_cross()
        self.position = next_pos
```

**Why `straight(8)` when turns == 0?**
- Robot is sitting on the crossing line from the previous step
- `track_until_cross()` would immediately re-detect it!
- Drive 8 cm forward to clear the intersection first

**When turning:** `turn_right()` already moves the robot off the crossing line, so no extra clearing needed.

---

## Slide 8: Putting It All Together
**Complete test program:**

```python
from line_track import LineTrack
from XRPLib.board import Board

HEADING_NAMES = ["N", "E", "S", "W"]

class Manhattan:
    # ... (from Lesson 5)

class Navigator:
    # ... (from this lesson)

# Main program
board = Board.get_default_board()
manhattan = Manhattan((0, 0))
nav = Navigator((0, 0), 0)

board.wait_for_button()

# Compute and drive a path
destination = (2, 2)
path = manhattan.compute_path(destination)
print("Path:", path)

nav.drive_path(path)
print("Arrived at", HEADING_NAMES[nav.heading])
```

---

## Slide 9: Your Turn!
**Activity:**
1. Implement the Navigator class with all three methods
2. Test with a simple path first: (0, 0) to (2, 0) — straight line south
3. Then try: (0, 0) to (2, 2) — requires a direction change mid-path
4. Watch how the robot clears intersections when going straight vs. turning

**Debugging tips:**
- Print the heading and turn count at each step
- Start with a 2-step path before trying longer ones
- Make sure the robot's physical starting heading matches heading 0 (North)

**Checkpoints:**
- Does the robot turn correctly at each step?
- Does it arrive at the right intersection?
- Does `straight(8)` properly clear the intersection when going straight?

---

## Slide 10: Connection to Next Lesson
**What you did today:**
- Implemented the Navigator class with drive_path()
- Reused LineTrack from Module 2 — composition in action!
- Used modular arithmetic for elegant turn calculations

**Next lesson (Lesson 9 — Final Project):**
- Integrate Manhattan + Navigator into a complete program
- Navigate to a LIST of destinations (not just one)
- Test with 4+ destinations on the grid

**Key achievement:** You now have THREE classes working together — Manhattan computes paths, Navigator decides turns, and LineTrack handles physical movement. That's separation of concerns in action!
