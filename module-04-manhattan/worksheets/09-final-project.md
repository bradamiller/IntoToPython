# Lesson 9 Worksheet: Final Project Planning

**Name:** ________________________
**Date:** ________________________

---

## Part A: System Design

**1. How do the Manhattan class and Navigator class work together? Fill in the diagram:**

```
  +-----------------+          +-----------------+
  |   Manhattan     |          |   Navigator     |
  |-----------------|          |-----------------|
  | .position       |          | .position       |
  |                 |          | .heading        |
  |                 |          | .drivetrain     |
  |-----------------|          |-----------------|
  | .compute_path() | -------> | .drive_path()   |
  |   returns _____ |  path    |   calls _______ |
  |                 |          |   calls _______ |
  +-----------------+          +-----------------+
```

**What does `compute_path()` return?** ____________________________________

**What two things does `drive_path()` do at each step?**
1. ____________________________________
2. ____________________________________

**2. After the Navigator drives one leg, what must you update in the main program? Why?**

____________________________________________________________________

____________________________________________________________________

**3. Draw the flow of the main program:**

```
Create Manhattan at (__, __)
Create Navigator at (__, __) heading ____
         |
         v
  +---> Get next destination
  |      |
  |      v
  |   Compute _________ using Manhattan
  |      |
  |      v
  |   Drive _________ using Navigator
  |      |
  |      v
  |   Update manhattan._________ = navigator._________
  |      |
  |      v
  +-- More destinations? (loop back)
         |
         No
         v
       Done!
```

---

## Part B: Destination Planning

**Your robot starts at (0, 0) facing North on a 4x4 grid. Choose 4 or more destinations.**

**Grid (mark your destinations with numbers 1, 2, 3, 4):**

```
        Col 0     Col 1     Col 2     Col 3
       +-------- +-------- +-------- +--------+
Row 0  |         |         |         |        |
       |  (0,0)  |  (0,1)  |  (0,2)  |  (0,3) |
       +-------- +-------- +-------- +--------+
Row 1  |         |         |         |        |
       |  (1,0)  |  (1,1)  |  (1,2)  |  (1,3) |
       +-------- +-------- +-------- +--------+
Row 2  |         |         |         |        |
       |  (2,0)  |  (2,1)  |  (2,2)  |  (2,3) |
       +-------- +-------- +-------- +--------+
Row 3  |         |         |         |        |
       |  (3,0)  |  (3,1)  |  (3,2)  |  (3,3) |
       +-------- +-------- +-------- +--------+
```

**Destination List:**

| Order | Destination | Description (optional) |
|---|---|---|
| Start | (0, 0) | Home base |
| 1 | (__, __) | ________________________ |
| 2 | (__, __) | ________________________ |
| 3 | (__, __) | ________________________ |
| 4 | (__, __) | ________________________ |
| 5 (optional) | (__, __) | ________________________ |

**Write your destinations list as Python code:**

```python
destinations = [________________________________________]
```

**How many total grid cells will your robot travel across all legs? (Count the steps, not the path length)**

Leg 1: _____ steps. Leg 2: _____ steps. Leg 3: _____ steps. Leg 4: _____ steps.

Total: _____ steps.

---

## Part C: Hand-Trace One Leg

**Choose your first leg (Start to Destination 1) and trace it completely.**

**From:** (__, __)  **To:** (__, __)

**Computed path (write the list of tuples):**

`[_______________________________________________]`

**Trace each step:**

| Step | From | To | Needed Direction | Current Heading | Turn | Degrees | New Heading |
|---|---|---|---|---|---|---|---|
| 1 | (__, __) | (__, __) | __________ | __________ | __________ | __________ | __________ |
| 2 | (__, __) | (__, __) | __________ | __________ | __________ | __________ | __________ |
| 3 | (__, __) | (__, __) | __________ | __________ | __________ | __________ | __________ |
| 4 | (__, __) | (__, __) | __________ | __________ | __________ | __________ | __________ |
| 5 | (__, __) | (__, __) | __________ | __________ | __________ | __________ | __________ |
| 6 | (__, __) | (__, __) | __________ | __________ | __________ | __________ | __________ |

(Add more rows if needed on the back of this page.)

**After this leg:**
- Navigator position: (__, __)
- Navigator heading: ____
- Manhattan position must be updated to: (__, __)

**What heading will the Navigator have at the START of leg 2?** ____

(This is important -- the heading carries over from the previous leg!)

---

## Part D: Testing Checklist

Check off each test as you complete it. **Do them in order!**

### Level 1: Manhattan Only (No Robot)
- [ ] Created Manhattan object at (0, 0)
- [ ] Tested `compute_path()` for destination 1: path looks correct
- [ ] Tested `compute_path()` for destination 2 (from destination 1): path looks correct
- [ ] Tested all 4 legs with print statements
- [ ] Updated `manhattan.position` after each leg

**Sample output for Level 1 (paste or write here):**

```
_____________________________________________
_____________________________________________
_____________________________________________
_____________________________________________
```

### Level 2: Single Leg on Robot
- [ ] Placed robot at (0, 0) facing North on the grid
- [ ] Ran program with only destination 1
- [ ] Robot turned correctly at each step
- [ ] Robot arrived at the correct cell
- [ ] Adjusted `straight()` distance if needed. Distance used: _____ cm

### Level 3: Full Sequence
- [ ] Ran program with all 4+ destinations
- [ ] Robot visited all destinations in order
- [ ] Robot ended at the final destination
- [ ] Console output matches expected paths

**Issues encountered and how you fixed them:**

____________________________________________________________________

____________________________________________________________________

____________________________________________________________________

---

## Part E: Code Template

Complete the main program below. The Manhattan and Navigator classes are provided for you.

```python
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board


class Manhattan:
    def __init__(self, start):
        self.position = start

    def compute_path(self, destination):
        path = [self.position]
        current_row = self.position[0]
        current_col = self.position[1]
        dest_row = destination[0]
        dest_col = destination[1]
        if dest_row > current_row:
            row_step = 1
        else:
            row_step = -1
        if dest_col > current_col:
            col_step = 1
        else:
            col_step = -1
        while current_row != dest_row:
            current_row = current_row + row_step
            path.append((current_row, current_col))
        while current_col != dest_col:
            current_col = current_col + col_step
            path.append((current_row, current_col))
        return path


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


# ===== YOUR MAIN PROGRAM =====

# TODO: Create a Board object for wait_for_button()
board = _______________________________________________

# TODO: Create a Manhattan object starting at (0, 0)
manhattan = _______________________________________________

# TODO: Create a Navigator object starting at (0, 0) heading North
navigator = _______________________________________________

# TODO: Define your list of 4+ destinations
destinations = _______________________________________________

print("=== XRP Grid Navigation: Final Project ===")
print("Starting at:", manhattan.position)
print("Destinations:", destinations)
print()

# TODO: Wait for button press before starting
_______________________________________________

# TODO: Write a for loop that goes through each destination
for __________ in __________:
    print("--- Navigating to", __________, "---")

    # TODO: Compute the path using manhattan
    path = _______________________________________________

    print("Path:", path)
    print("Steps:", len(path) - 1)

    # TODO: Drive the path using navigator
    _______________________________________________

    # TODO: Update manhattan's position to match navigator's position
    _______________________________________________

    print("Arrived at:", navigator.position)
    print("Heading:", navigator.heading)
    print()

print("=== All destinations reached! ===")
print("Final position:", navigator.position)
```

---

## Reflection

**What was the hardest part of putting the whole system together? What strategies helped you debug it?**

____________________________________________________________________

____________________________________________________________________

____________________________________________________________________

____________________________________________________________________

---

**Congratulations! You have built a complete autonomous grid navigation system from scratch!**
