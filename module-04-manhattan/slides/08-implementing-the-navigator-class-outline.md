# Lesson 8 Slide Outline: Implementing the Navigator Class

## Slide 1: Title & Learning Objectives
**Title:** Implementing the Navigator Class

**Learning Objectives:**
- Design the Navigator class with position and heading
- Implement drive_path() to turn and drive through a path
- Track and update heading as the robot moves
- Integrate with DifferentialDrive for physical movement

**Agenda:**
- Class design overview (5 min)
- Implementing helper methods (10 min)
- Building drive_path() (15 min)
- Testing on the robot (15 min)

---

## Slide 2: Hook — From Algorithm to Action
**We have TWO pieces working:**
1. Manhattan class computes the path (list of tuples)
2. Turning logic tells us what turns are needed

**Missing piece:** Something that actually DRIVES the robot!

```python
path = [(0,0), (1,0), (2,0), (2,1), (2,2)]
# How does this become real robot movement?
```

**Today:** Build the Navigator class that turns and drives through any path.

---

## Slide 3: Navigator Class Design
**What does the Navigator need?**

**Data (stored in __init__):**
- `self.position` — current (row, col) tuple
- `self.heading` — current direction ("N", "S", "E", "W")
- `self.drivetrain` — the DifferentialDrive object

**Methods:**
- `get_needed_direction(next_pos)` — what direction to face
- `turn_to(direction)` — turn the robot to face that direction
- `drive_one_step()` — drive forward one intersection
- `drive_path(path)` — drive the entire path

---

## Slide 4: The __init__ Method
```python
from XRPLib.differential_drive import DifferentialDrive

class Navigator:
    def __init__(self, start, heading):
        self.position = start
        self.heading = heading
        self.drivetrain = DifferentialDrive.get_default_differential_drive()
```

**Usage:**
```python
nav = Navigator((0, 0), "N")
print("Position:", nav.position)   # (0, 0)
print("Heading:", nav.heading)     # N
```

**Note:** The starting heading must match how you physically place the robot!

---

## Slide 5: get_needed_direction()
**Determine direction from current position to next position:**

```python
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
```

**Example:**
```python
nav = Navigator((0, 0), "N")
direction = nav.get_needed_direction((1, 0))
print(direction)   # "S" — need to go south (row increases)
```

---

## Slide 6: turn_to()
**Turn the robot to face the desired direction:**

```python
def turn_to(self, direction):
    if self.heading == direction:
        return   # Already facing the right way

    right_turns = {"N": "E", "E": "S", "S": "W", "W": "N"}
    left_turns = {"N": "W", "W": "S", "S": "E", "E": "N"}

    if right_turns[self.heading] == direction:
        self.drivetrain.turn(90)
        self.heading = direction
    elif left_turns[self.heading] == direction:
        self.drivetrain.turn(-90)
        self.heading = direction
    else:
        # 180 degree turn
        self.drivetrain.turn(180)
        self.heading = direction
```

**Key:** Updates self.heading after turning!

---

## Slide 7: drive_path()
**The main method — drive through every step in the path:**

```python
def drive_path(self, path):
    for next_pos in path:
        if next_pos == self.position:
            continue   # Skip the starting position

        # 1. Figure out which way to face
        direction = self.get_needed_direction(next_pos)

        # 2. Turn if needed
        self.turn_to(direction)

        # 3. Drive forward one intersection
        self.drivetrain.straight(30)

        # 4. Update position
        self.position = next_pos
        print("Arrived at", self.position)
```

**The loop:** For each coordinate in the path, turn to face it, drive forward, update position.

**Note:** `straight(30)` assumes 30 cm between intersections — adjust for your grid!

---

## Slide 8: Putting It All Together
**Complete test program:**

```python
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board

class Manhattan:
    # ... (from Lesson 5)

class Navigator:
    # ... (from this lesson)

# Main program
board = Board.get_default_board()
manhattan = Manhattan((0, 0))
nav = Navigator((0, 0), "N")

board.wait_for_button()

# Compute and drive a path
destination = (2, 2)
path = manhattan.compute_path(destination)
print("Path:", path)

nav.drive_path(path)
print("Arrived at destination!")
```

---

## Slide 9: Your Turn!
**Activity:**
1. Implement the Navigator class with all four methods
2. Test with a simple path first: (0, 0) to (2, 0) — straight line, may need one turn
3. Then try: (0, 0) to (2, 2) — requires a direction change mid-path
4. Adjust the `straight(30)` distance to match your grid spacing

**Debugging tips:**
- Print the heading and turn at each step
- Start with a 2-step path before trying longer ones
- Make sure the robot's physical starting heading matches `"N"` (or whichever you chose)

**Checkpoints:**
- Does the robot turn correctly at each step?
- Does it arrive at the right intersection?
- Does the heading update properly?

---

## Slide 10: Connection to Next Lesson
**What you did today:**
- Implemented the Navigator class with drive_path()
- Integrated turning logic with physical robot movement
- Tested on real paths

**Next lesson (Lesson 9 — Final Project):**
- Integrate Manhattan + Navigator into a complete program
- Navigate to a LIST of destinations (not just one)
- Test with 4+ destinations on the grid

**Key achievement:** You now have TWO classes working together — one computes, one drives. That's separation of concerns in action!
