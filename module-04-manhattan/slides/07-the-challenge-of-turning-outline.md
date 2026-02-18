# Lesson 7 Slide Outline: The Challenge of Turning

## Slide 1: Title & Learning Objectives
**Title:** The Challenge of Turning

**Learning Objectives:**
- Understand heading as a direction the robot faces (N, S, E, W)
- Determine the required direction from consecutive coordinates
- Calculate what turn is needed given current heading and desired direction
- Work through turning logic on paper before coding

**Agenda:**
- What is heading? (5 min)
- Direction from coordinates (10 min)
- Turn logic (15 min)
- Practice worksheet (15 min)

---

## Slide 2: Hook — The Algorithm Knows Where, Not How
**We have a path:** `[(0,0), (1,0), (2,0), (2,1), (2,2)]`

**The robot knows WHERE to go.** But HOW does it get there?

**Problem:** Going from (0, 0) to (1, 0) means "move one row down." But the robot needs to know:
- Which direction am I facing RIGHT NOW?
- Which direction do I NEED to face?
- Do I need to turn? Which way?

**Today:** We'll solve the turning puzzle.

---

## Slide 3: What Is Heading?
**Heading:** The direction the robot is currently facing

**Four cardinal directions:**

| Heading | Meaning | Row change | Col change |
|---|---|---|---|
| North | Facing up (row decreases) | -1 | 0 |
| South | Facing down (row increases) | +1 | 0 |
| East | Facing right (col increases) | 0 | +1 |
| West | Facing left (col decreases) | 0 | -1 |

**We'll use strings:** `"N"`, `"S"`, `"E"`, `"W"`

**Key Idea:** The robot always starts facing a known direction (e.g., "N" or "E").

---

## Slide 4: Direction from Coordinates
**Given two consecutive coordinates, what direction is the robot moving?**

```python
current = (0, 0)
next_pos = (1, 0)

row_diff = next_pos[0] - current[0]   # 1 - 0 = 1
col_diff = next_pos[1] - current[1]   # 0 - 0 = 0
```

**Rules:**

| row_diff | col_diff | Direction |
|---|---|---|
| +1 | 0 | South (moving down) |
| -1 | 0 | North (moving up) |
| 0 | +1 | East (moving right) |
| 0 | -1 | West (moving left) |

**Example:** (2, 0) to (2, 1) → row_diff=0, col_diff=+1 → East

---

## Slide 5: What Turn Is Needed?
**The turn depends on: current heading AND needed direction.**

**Example 1:** Facing North, need to go East → Turn RIGHT

**Example 2:** Facing North, need to go West → Turn LEFT

**Example 3:** Facing North, need to go South → Turn AROUND (180°)

**Example 4:** Facing East, need to go East → NO TURN

**Turn table (current heading → needed direction → turn):**

| Current | Need N | Need S | Need E | Need W |
|---|---|---|---|---|
| N | None | 180° | Right | Left |
| S | 180° | None | Left | Right |
| E | Left | Right | None | 180° |
| W | Right | Left | 180° | None |

---

## Slide 6: Turn Logic in Python
**One way to code it:**

```python
def get_turn(current_heading, needed_direction):
    if current_heading == needed_direction:
        return "none"

    right_turns = {"N": "E", "E": "S", "S": "W", "W": "N"}
    left_turns = {"N": "W", "W": "S", "S": "E", "E": "N"}

    if right_turns[current_heading] == needed_direction:
        return "right"
    elif left_turns[current_heading] == needed_direction:
        return "left"
    else:
        return "around"
```

**This encodes the turn table from the previous slide!**

---

## Slide 7: Walking Through a Path
**Path: [(0,0), (1,0), (2,0), (2,1), (2,2)]**
**Starting heading: North**

| Step | From | To | Direction | Heading | Turn | New Heading |
|---|---|---|---|---|---|---|
| 1 | (0,0) | (1,0) | South | North | 180° | South |
| 2 | (1,0) | (2,0) | South | South | None | South |
| 3 | (2,0) | (2,1) | East | South | Left | East |
| 4 | (2,1) | (2,2) | East | East | None | East |

**Notice:**
- Step 1 requires a 180° turn (facing wrong way)
- Step 2 requires no turn (already facing right direction)
- Step 3 requires a left turn (changing from rows to columns)
- Step 4 requires no turn (continuing same direction)

---

## Slide 8: Updating Heading After Turning
**After each turn, the heading changes:**

```python
# After turning right
if turn == "right":
    right_turns = {"N": "E", "E": "S", "S": "W", "W": "N"}
    heading = right_turns[heading]

# After turning left
elif turn == "left":
    left_turns = {"N": "W", "W": "S", "S": "E", "E": "N"}
    heading = left_turns[heading]

# After turning around
elif turn == "around":
    around = {"N": "S", "S": "N", "E": "W", "W": "E"}
    heading = around[heading]
```

**Critical:** If you forget to update heading, subsequent turns will be wrong!

---

## Slide 9: Your Turn!
**Activity: Work Through Turning Logic on Paper**

**Path 1:** [(0,0), (0,1), (0,2), (1,2), (2,2)], starting heading: East
- What turns are needed at each step?
- What is the heading after each step?

**Path 2:** [(2,3), (1,3), (0,3), (0,2), (0,1), (0,0)], starting heading: South
- This path goes up and then left — multiple direction changes!

**Path 3:** [(1,1), (1,2), (1,3), (2,3), (3,3)], starting heading: North
- What's the first turn needed?

**Checkpoints:**
- Can you determine direction from two coordinates?
- Can you look up the correct turn in the turn table?
- Do you update the heading after each turn?

---

## Slide 10: Connection to Next Lesson
**What you did today:**
- Understood heading as a direction concept
- Determined direction from coordinate differences
- Used a turn table to find the right turn
- Walked through complete paths updating heading

**Next lesson (Lesson 8):**
- Implement the **Navigator class** in Python
- Code `drive_path()` that turns and drives for each step
- Connect the turning logic to actual robot movement

**Key insight:** The hard part is the LOGIC, not the code. You solved the logic today — tomorrow you'll just translate it into Python.
