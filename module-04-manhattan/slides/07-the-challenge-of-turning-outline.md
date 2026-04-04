# Lesson 7 Slide Outline: The Challenge of Turning

## Slide 1: Title & Learning Objectives
**Title:** The Challenge of Turning

**Learning Objectives:**
- Represent heading as a number: 0=N, 1=E, 2=S, 3=W
- Determine the needed heading from consecutive coordinates
- Use modular arithmetic to calculate the number of right turns
- Work through turning logic on paper before coding

**Agenda:**
- What is heading? (5 min)
- Heading from coordinates (10 min)
- Counting right turns with a formula (15 min)
- Practice worksheet (15 min)

---

## Slide 2: Hook — The Algorithm Knows Where, Not How
**We have a path:** `[(0,0), (1,0), (2,0), (2,1), (2,2)]`

**The robot knows WHERE to go.** But HOW does it get there?

**Problem:** Going from (0, 0) to (1, 0) means "move one row down." But the robot needs to know:
- Which direction am I facing RIGHT NOW?
- Which direction do I NEED to face?
- Do I need to turn? How many times?

**Today:** We'll solve the turning puzzle with numbers and a simple formula.

---

## Slide 3: Heading as a Number
**Heading:** The direction the robot is currently facing, represented as a number 0-3.

**Four headings — arranged clockwise:**

| Number | Direction | Meaning | Row change | Col change |
|---|---|---|---|---|
| 0 | North | Facing up (row decreases) | -1 | 0 |
| 1 | East | Facing right (col increases) | 0 | +1 |
| 2 | South | Facing down (row increases) | +1 | 0 |
| 3 | West | Facing left (col decreases) | 0 | -1 |

**For display:** `HEADING_NAMES = ["N", "E", "S", "W"]`

**Key Idea:** Numbers let us do math with headings — one formula handles all cases!

---

## Slide 4: Heading from Coordinates
**Given two consecutive coordinates, what heading does the robot need?**

```python
current = (0, 0)
next_pos = (1, 0)

row_diff = next_pos[0] - current[0]   # 1 - 0 = 1
col_diff = next_pos[1] - current[1]   # 0 - 0 = 0
```

**Rules:**

| row_diff | col_diff | Heading |
|---|---|---|
| -1 | 0 | 0 — North (moving up) |
| 0 | +1 | 1 — East (moving right) |
| +1 | 0 | 2 — South (moving down) |
| 0 | -1 | 3 — West (moving left) |

**Example:** (2, 0) to (2, 1) → row_diff=0, col_diff=+1 → heading 1 (East)

---

## Slide 5: How Many Right Turns?
**The key insight: we only need right turns!**

**The formula:** `turns = (needed - current) % 4`

| Result | Meaning | Physical turn |
|---|---|---|
| 0 | No turn needed | Already facing the right way |
| 1 | One right turn | 90° clockwise |
| 2 | Two right turns | 180° (turn around) |
| 3 | Three right turns | 270° clockwise |

**Examples:**
- Facing 0 (N), need 1 (E): `(1 - 0) % 4 = 1` → one right turn
- Facing 0 (N), need 3 (W): `(3 - 0) % 4 = 3` → three right turns
- Facing 2 (S), need 0 (N): `(0 - 2) % 4 = 2` → two right turns (180°)
- Facing 1 (E), need 1 (E): `(1 - 1) % 4 = 0` → no turn needed

**Why this works:** Python's `%` wraps negative numbers around, so `-2 % 4 = 2`, not `-2`.

---

## Slide 6: The Formula in Python
**Two simple functions — clean and complete!**

```python
HEADING_NAMES = ["N", "E", "S", "W"]

def get_needed_heading(current_pos, next_pos):
    row_diff = next_pos[0] - current_pos[0]
    col_diff = next_pos[1] - current_pos[1]
    if row_diff == -1:
        return 0    # North
    elif col_diff == 1:
        return 1    # East
    elif row_diff == 1:
        return 2    # South
    elif col_diff == -1:
        return 3    # West

def count_right_turns(current, needed):
    return (needed - current) % 4
```

**That's it!** Two functions, one formula, and every possible turn is covered.

---

## Slide 7: Walking Through a Path
**Path: [(0,0), (1,0), (2,0), (2,1), (2,2)]**
**Starting heading: 0 (N)**

| Step | From | To | Needed | Current | Formula | Turns | New Heading |
|---|---|---|---|---|---|---|---|
| 1 | (0,0) | (1,0) | 2 (S) | 0 (N) | (2-0)%4 | 2 | 2 (S) |
| 2 | (1,0) | (2,0) | 2 (S) | 2 (S) | (2-2)%4 | 0 | 2 (S) |
| 3 | (2,0) | (2,1) | 1 (E) | 2 (S) | (1-2)%4 | 3 | 1 (E) |
| 4 | (2,1) | (2,2) | 1 (E) | 1 (E) | (1-1)%4 | 0 | 1 (E) |

**Notice:**
- Step 1: 2 right turns (facing wrong way — equivalent to 180°)
- Step 2: 0 turns (already facing South)
- Step 3: 3 right turns (changing from rows to columns)
- Step 4: 0 turns (continuing East)

---

## Slide 8: Updating Heading After Turning
**After turning, the heading update is trivial:**

```python
heading = needed
```

**That's it!** Once the robot finishes turning to face the needed direction, the new heading IS the needed heading.

**In the path loop:**

```python
heading = 0  # starting heading

for i in range(len(path) - 1):
    needed = get_needed_heading(path[i], path[i+1])
    turns = count_right_turns(heading, needed)
    # Robot turns right `turns` times
    # Robot drives forward one segment
    heading = needed  # update heading
```

**Critical:** If you forget `heading = needed`, subsequent turn counts will be wrong!

---

## Slide 9: Your Turn!
**Activity: Work Through Turning Logic on Paper**

**Path 1:** [(0,0), (0,1), (0,2), (1,2), (2,2)], starting heading: 1 (E)
- What are the right-turn counts at each step?
- What is the heading after each step?

**Path 2:** [(2,3), (1,3), (0,3), (0,2), (0,1), (0,0)], starting heading: 2 (S)
- This path goes up and then left — multiple heading changes!

**Path 3:** [(1,1), (1,2), (1,3), (2,3), (3,3)], starting heading: 0 (N)
- How many right turns for the first step?

**Checkpoints:**
- Can you compute `get_needed_heading()` from two coordinates?
- Can you apply `(needed - current) % 4` to count right turns?
- Do you update the heading after each step?

---

## Slide 10: Connection to Next Lesson
**What you did today:**
- Represented heading as a number (0=N, 1=E, 2=S, 3=W)
- Determined needed heading from coordinate differences
- Used `(needed - current) % 4` to count right turns
- Walked through complete paths updating heading at each step

**Next lesson (Lesson 8):**
- Implement the **Navigator class** in Python
- Code `drive_path()` that turns right N times and drives for each step
- Connect the turning logic to actual robot movement

**Key insight:** The hard part is the LOGIC, not the code. You solved the logic today — tomorrow you'll just translate it into Python.
