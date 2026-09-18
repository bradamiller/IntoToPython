# Lesson 9 Worksheet: Final Project Planning

**Name:** ________________________
**Date:** ________________________

---

## Part A: System Design

**1. How do `compute_manhattan_path()` and `drive_path()` work together? Fill in the diagram:**

```
  +------------------------------+          +------------------------------+
  | compute_manhattan_path(      |          | drive_path(                  |
  |   position, destination)     |  path    |   path, position, heading)   |
  |-------------------------------| -------> |-------------------------------|
  | returns _____                |          | calls _______                |
  |                               |          | calls _______                |
  |                               |          | returns (_____, _____)       |
  +------------------------------+          +------------------------------+
```

**What does `compute_manhattan_path()` return?** ____________________________________

**What two things does `drive_path()` do at each step?**
1. ____________________________________
2. ____________________________________

**2. After `drive_path()` returns, what must you do with its return value in the main program? Why?**

____________________________________________________________________

____________________________________________________________________

**3. Draw the flow of the main program:**

```
position = (__, __)
heading = ____
         |
         v
  +---> Get next destination
  |      |
  |      v
  |   Compute _________ using compute_manhattan_path
  |      |
  |      v
  |   Drive the path, capturing new _________ and _________
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

| Step | From | To | Desired Heading | Current Heading | `turn_to` heading values | New Heading |
|---|---|---|---|---|---|---|
| 1 | (__, __) | (__, __) | __________ | __________ | __________ | __________ |
| 2 | (__, __) | (__, __) | __________ | __________ | __________ | __________ |
| 3 | (__, __) | (__, __) | __________ | __________ | __________ | __________ |
| 4 | (__, __) | (__, __) | __________ | __________ | __________ | __________ |
| 5 | (__, __) | (__, __) | __________ | __________ | __________ | __________ |
| 6 | (__, __) | (__, __) | __________ | __________ | __________ | __________ |

*Headings: 0 = North, 1 = East, 2 = South, 3 = West*
*`turn_to` each pass: turn right, add 1 to heading, wrap 4 → 0. Stop when heading == desired.*

(Add more rows if needed on the back of this page.)

**After this leg:**
- New position: (__, __)
- New heading: ____
- What line of code captures these in the main program? `position, heading = _______________________`

**What heading will the robot have at the START of leg 2?** ____

(This is important -- the heading carries over from the previous leg, because `heading` is the very same variable used throughout the loop!)

---

## Part D: Testing Checklist

Check off each test as you complete it. **Do them in order!**

### Level 1: Path Computation Only (No Robot)
- [ ] Set `position = (0, 0)`
- [ ] Tested `compute_manhattan_path()` for destination 1: path looks correct
- [ ] Tested `compute_manhattan_path()` for destination 2 (from destination 1): path looks correct
- [ ] Tested all 4 legs with print statements
- [ ] Updated `position` after each leg (in the test loop)

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
- [ ] Robot followed the line to the next intersection
- [ ] Robot arrived at the correct cell

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

Complete the main program below. `compute_manhattan_path()` and the driving functions are provided for you.

```python
from XRPLib.board import Board

HEADING_NAMES = ["N", "E", "S", "W"]


def compute_manhattan_path(position, destination):
    path = []
    current_row, current_col = position
    dest_row, dest_col = destination
    while current_row < dest_row:
        current_row = current_row + 1
        path.append((current_row, current_col))
    while current_row > dest_row:
        current_row = current_row - 1
        path.append((current_row, current_col))
    while current_col < dest_col:
        current_col = current_col + 1
        path.append((current_row, current_col))
    while current_col > dest_col:
        current_col = current_col - 1
        path.append((current_row, current_col))
    return path


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


# ===== YOUR MAIN PROGRAM =====

# TODO: Create a Board object for wait_for_button()
board = _______________________________________________

# TODO: Set up starting position and heading
position = _______________________________________________
heading = _______________________________________________

# TODO: Define your list of 4+ destinations
destinations = _______________________________________________

print("=== XRP Grid Navigation: Final Project ===")
print("Starting at:", position)
print("Destinations:", destinations)
print()

# TODO: Wait for button press before starting
_______________________________________________

# TODO: Write a for loop that goes through each destination
for __________ in __________:
    print("--- Navigating to", __________, "---")

    # TODO: Compute the path
    path = _______________________________________________

    print("Path:", path)
    print("Steps:", len(path))

    # TODO: Drive the path, capturing the new position and heading
    _______________________________________________

    print("Arrived at:", position)
    print("Heading:", HEADING_NAMES[heading])
    print()

print("=== All destinations reached! ===")
print("Final position:", position)
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

---

## Part F (Optional Extension): The Class Version

*Skip this section if your course doesn't cover classes.*

1. **In the class version, `drive_path()` is a method that updates `self.position` and `self.heading` in place, and doesn't return anything. What line does the main program need after calling `navigator.drive_path(path)` that the functions version does NOT need?**

   _________________________________________________________________

2. **Why is that line ("keep two objects in sync") a common source of bugs, compared to the functions version's single `position` variable?**

   _________________________________________________________________

   _________________________________________________________________

3. **Rewrite this functions-version snippet using the `Manhattan`/`Navigator` classes:**

   Functions version:
   ```python
   path = compute_manhattan_path(position, dest)
   position, heading = drive_path(path, position, heading)
   ```

   Class version:
   ```python
   path = _______________________________________________
   _______________________________________________
   _______________________________________________
   ```
