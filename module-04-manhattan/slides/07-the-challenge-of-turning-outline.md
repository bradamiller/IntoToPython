# Lesson 7 Slide Outline: The Challenge of Turning

## Slide 1: Title & Learning Objectives
**Title:** The Challenge of Turning

**Learning Objectives:**
- Represent heading as a number: 0=N, 1=E, 2=S, 3=W
- Determine the needed heading from consecutive coordinates
- Count right turns by stepping clockwise from current to needed heading
- Work through turning logic on paper before coding

**Agenda:**
- What is heading? (5 min)
- Heading from coordinates (10 min)
- Counting right turns by stepping clockwise (15 min)
- Practice worksheet (15 min)

---

## Slide 2: Hook — The Algorithm Knows Where, Not How
**We have a path:** `[(0,0), (1,0), (2,0), (2,1), (2,2)]`

**The robot knows WHERE to go.** But HOW does it get there?

**Problem:** Going from (0, 0) to (1, 0) means "move one row down." But the robot needs to know:
- Which direction am I facing RIGHT NOW?
- Which direction do I NEED to face?
- Do I need to turn? How many times?

**Today:** We'll solve the turning puzzle with numbers and a simple counting approach.

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

**Key Idea:** Numbers let us count clockwise steps from one heading to another!

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

**Count clockwise steps from current heading to needed heading:**

| Result | Meaning | Physical turn |
|---|---|---|
| 0 | No turn needed | Already facing the right way |
| 1 | One right turn | 90° clockwise |
| 2 | Two right turns | 180° (turn around) |
| 3 | Three right turns | 270° clockwise |

**Examples — count clockwise from current to needed:**
- Facing 0 (N), need 1 (E): 0→1 = 1 turn
- Facing 0 (N), need 3 (W): 0→1→2→3 = 3 turns
- Facing 2 (S), need 0 (N): 2→3→0 = 2 turns (180°)
- Facing 1 (E), need 1 (E): already there = 0 turns

**Why this works:** Heading numbers go clockwise (0, 1, 2, 3), and after 3 we wrap back to 0. Each clockwise step is one right turn!

---

## Slide 6: Heading Logic in Python
**One function determines the needed heading from coordinates:**

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
```

**How it works:** Compare the two coordinates. The row/column difference tells you which of the four headings is needed.

**Counting right turns?** You already know how to do that on paper -- count clockwise steps from current to needed. In the next lesson, the Navigator class will use a while loop to turn right until the heading matches.

---

## Slide 7: Walking Through a Path
**Path: [(0,0), (1,0), (2,0), (2,1), (2,2)]**
**Starting heading: 0 (N)**

| Step | From | To | Needed | Current | Count | Turns | New Heading |
|---|---|---|---|---|---|---|---|
| 1 | (0,0) | (1,0) | 2 (S) | 0 (N) | 0→1→2 | 2 | 2 (S) |
| 2 | (1,0) | (2,0) | 2 (S) | 2 (S) | already there | 0 | 2 (S) |
| 3 | (2,0) | (2,1) | 1 (E) | 2 (S) | 2→3→0→1 | 3 | 1 (E) |
| 4 | (2,1) | (2,2) | 1 (E) | 1 (E) | already there | 0 | 1 (E) |

**Notice:**
- Step 1: Count 0→1→2 = 2 right turns (facing wrong way — equivalent to 180°)
- Step 2: 0 turns (already facing South)
- Step 3: Count 2→3→0→1 = 3 right turns (wraps around from 3 back to 0!)
- Step 4: 0 turns (continuing East)

---

## Slide 8: Updating Heading After Turning
**After turning, the heading simply becomes the needed heading.**

**In the path loop:**

```python
heading = 0  # starting heading

for i in range(len(path) - 1):
    needed = get_needed_heading(path[i], path[i+1])
    # Turn right until facing `needed` (code comes in Lesson 8!)
    # Drive forward one segment
    heading = needed  # update heading
```

**Critical:** If you forget `heading = needed`, subsequent turn calculations will be wrong!

**Next lesson:** The Navigator class will implement `turn_to()` with a while loop that turns right until the heading matches.

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
- Can you count clockwise steps from the current heading to the needed heading?
- Do you update the heading after each step?

---

## Slide 10: Connection to Next Lesson
**What you did today:**
- Represented heading as a number (0=N, 1=E, 2=S, 3=W)
- Determined needed heading from coordinate differences
- Counted right turns by stepping clockwise from current to needed heading
- Walked through complete paths updating heading at each step

**Next lesson (Lesson 8):**
- Implement the **Navigator class** in Python
- Code `turn_to()` with a while loop that turns right until the heading matches
- Code `drive_path()` that uses `turn_to()` and drives for each step
- Connect the turning logic to actual robot movement

**Key insight:** The hard part is the LOGIC, not the code. You solved the logic today -- tomorrow you'll translate it into Python.
