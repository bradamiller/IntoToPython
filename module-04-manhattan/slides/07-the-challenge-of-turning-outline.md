# Lesson 7 Slide Outline: The Challenge of Turning

## Slide 1: Title & Learning Objectives
**Title:** The Challenge of Turning

**Learning Objectives:**
- See that between intersections, either the row OR the column changes — never both
- Map each of the 4 cases to one of 4 directions: N, E, S, W
- Represent heading as a number: 0=N, 1=E, 2=S, 3=W
- Design three Navigator methods: compute desired heading, turn to it, drive the path

---

## Slide 2: One Change at a Time
**Between two adjacent intersections, exactly one thing changes:**

- The **row** changes by +1 or -1, OR
- The **column** changes by +1 or -1

**Never both.** That gives us exactly **4 cases**, and each case has one direction:

| What changed | Direction |
|---|---|
| row goes down (+1) | South |
| row goes up (-1) | North |
| column goes up (+1) | East |
| column goes down (-1) | West |

That's the whole puzzle. Four cases, four directions.

---

## Slide 3: Heading as a Number
**Heading:** the direction the robot is currently facing, as a number 0-3.

| Number | Direction |
|---|---|
| 0 | North |
| 1 | East |
| 2 | South |
| 3 | West |

**For display:** `HEADING_NAMES = ["N", "E", "S", "W"]`

**Why numbers?** Because the robot only turns **right**, and each right turn adds 1 to the heading. When it reaches 4, reset to 0.

---

## Slide 4: Method 1 — Compute the Desired Heading
Given the current intersection and the next intersection, which of the 4 cases is it?

```python
def desired_heading(current, next_pos):
    row_diff = next_pos[0] - current[0]
    col_diff = next_pos[1] - current[1]
    if row_diff == -1: return 0   # North
    if col_diff ==  1: return 1   # East
    if row_diff ==  1: return 2   # South
    if col_diff == -1: return 3   # West
```

**Input:** two intersections. **Output:** a heading number 0-3.

---

## Slide 5: Method 2 — Turn Until Facing the Desired Heading
Keep turning right, adding 1 to the heading each time. If heading reaches 4, reset to 0. Stop when it equals the desired heading.

```python
def turn_to(self, desired):
    while self.heading != desired:
        self.robot.turn_right()
        self.heading = self.heading + 1
        if self.heading == 4:
            self.heading = 0
```

**That's it.** No counting turns ahead of time. No math tricks. Just turn right until you're pointing the right way.

---

## Slide 6: Method 3 — Drive the Path
Walk through the list of intersections. For each one: turn to face it, then drive forward one intersection.

```python
def drive_path(self, path):
    for next_pos in path:
        desired = desired_heading(self.position, next_pos)
        self.turn_to(desired)
        self.robot.drive_forward_one()
        self.position = next_pos
```

**Three methods, working together:**
1. `desired_heading` — which way should I face?
2. `turn_to` — turn right until I'm facing that way
3. `drive_path` — do that for every intersection in the list

---

## Slide 7: Walking Through a Path
**Path:** `[(1,0), (2,0), (2,1), (2,2)]`, start at `(0,0)` facing 0 (N)

| Step | From | To | Change | Desired | Turns right until heading = desired |
|---|---|---|---|---|---|
| 1 | (0,0) | (1,0) | row +1 | 2 (S) | 0→1→2 |
| 2 | (1,0) | (2,0) | row +1 | 2 (S) | already 2 |
| 3 | (2,0) | (2,1) | col +1 | 1 (E) | 2→3→0→1 (wraps 4→0) |
| 4 | (2,1) | (2,2) | col +1 | 1 (E) | already 1 |

The wrap from 3 back to 0 is exactly the `if self.heading == 4: self.heading = 0` line.

---

## Slide 8: Your Turn!
**On paper, trace `turn_to` for each step:**

**Path 1:** `[(0,1), (0,2), (1,2), (2,2)]`, start `(0,0)`, heading 1 (E)

**Path 2:** `[(1,3), (0,3), (0,2), (0,1), (0,0)]`, start `(2,3)`, heading 2 (S)

**Path 3:** `[(1,2), (1,3), (2,3), (3,3)]`, start `(1,1)`, heading 0 (N)

**For each step write:**
- Did the row or the column change? → desired heading
- Each value of `self.heading` as the while loop runs
- Final heading after the step

---

## Slide 9: Connection to Next Lesson
**Today:** Three methods on paper.
- `desired_heading(current, next_pos)` — picks one of 0, 1, 2, 3
- `turn_to(desired)` — turns right, wraps 4 back to 0
- `drive_path(path)` — ties it all together

**Next lesson:** Build the full Navigator class in Python and run it on the robot.
