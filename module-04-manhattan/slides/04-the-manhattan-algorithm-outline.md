# Lesson 4 Slide Outline: The Manhattan Algorithm

## Slide 1: Title & Learning Objectives
**Title:** The Manhattan Algorithm

**Learning Objectives:**
- Understand how Manhattan distance pathfinding works
- Trace the algorithm by hand for given start/destination pairs
- Explain the "rows first, then columns" strategy
- Handle paths in all four directions (up, down, left, right)

**Agenda:**
- What is Manhattan distance? (10 min)
- The algorithm: rows first, then columns (10 min)
- Hand-tracing examples (15 min)
- Practice worksheet (10 min)

---

## Slide 2: Hook — How Do You Walk in a City?
**Question:** "If you're at 1st Street & 1st Avenue and need to get to 4th Street & 3rd Avenue, how do you walk?"

**You can't cut diagonally through buildings!**
- Walk along streets (rows) and avenues (columns)
- Go north/south first, then east/west — or vice versa

**This is Manhattan distance** — named after the grid layout of Manhattan, New York City.

**Our robot has the same constraint:** It drives along grid lines, not diagonally.

---

## Slide 3: Manhattan Distance
**Manhattan distance:** The total number of row steps + column steps between two points.

**Example:**
- Start: (0, 0)
- Destination: (2, 3)
- Row distance: |2 - 0| = 2 steps
- Column distance: |3 - 0| = 3 steps
- Manhattan distance: 2 + 3 = 5 steps

**Compare to straight-line distance:**
- Straight line: about 3.6 (Pythagorean theorem)
- Manhattan: 5 (along grid lines)
- Manhattan is always >= straight line

---

## Slide 4: The Algorithm — Rows First, Then Columns
**Strategy:** Move along rows until correct row, then move along columns.

**Example: (0, 0) to (2, 3)**

**Step 1: Move along rows (0 → 2)**
- (0, 0) → (1, 0) → (2, 0)

**Step 2: Move along columns (0 → 3)**
- (2, 0) → (2, 1) → (2, 2) → (2, 3)

**Full path:**
```
(0,0) → (1,0) → (2,0) → (2,1) → (2,2) → (2,3)
```

**Total: 5 steps (matches Manhattan distance!)**

---

## Slide 5: Tracing on the Grid
**Visual: (0, 0) to (2, 3)**

| | Col 0 | Col 1 | Col 2 | Col 3 |
|---|---|---|---|---|
| Row 0 | START | | | |
| Row 1 | ↓ | | | |
| Row 2 | ↓ | → | → | END |

**The path makes an "L" shape:**
- Down 2 rows, then right 3 columns
- Always goes rows first, then columns

---

## Slide 6: Direction Matters
**What if the destination is UP or LEFT?**

**Example: (2, 3) to (0, 1)**
- Row: go from 2 to 0 (decrease — move UP)
- Column: go from 3 to 1 (decrease — move LEFT)

**Path:**
```
(2,3) → (1,3) → (0,3) → (0,2) → (0,1)
```

**How to determine direction:**
- If destination row > current row → move DOWN (row increases)
- If destination row < current row → move UP (row decreases)
- If destination col > current col → move RIGHT (col increases)
- If destination col < current col → move LEFT (col decreases)

---

## Slide 7: The Step Value
**Use +1 or -1 to control direction:**

```
If destination row > start row:
    row_step = +1    (moving down)
Else:
    row_step = -1    (moving up)

If destination col > start col:
    col_step = +1    (moving right)
Else:
    col_step = -1    (moving left)
```

**Example: (3, 0) to (1, 2)**
- Row: 3 → 1, so row_step = -1
- Col: 0 → 2, so col_step = +1
- Path: (3,0) → (2,0) → (1,0) → (1,1) → (1,2)

---

## Slide 8: More Practice — Hand Trace
**Trace these paths by hand:**

**Path 1: (0, 0) to (3, 2)**
- Row steps: 0 → 3 (step = +1): (0,0), (1,0), (2,0), (3,0)
- Col steps: 0 → 2 (step = +1): (3,1), (3,2)
- Full: (0,0) → (1,0) → (2,0) → (3,0) → (3,1) → (3,2)

**Path 2: (2, 2) to (0, 0)**
- Row steps: 2 → 0 (step = -1): (2,2), (1,2), (0,2)
- Col steps: 2 → 0 (step = -1): (0,1), (0,0)
- Full: (2,2) → (1,2) → (0,2) → (0,1) → (0,0)

**Path 3: (1, 0) to (1, 3)**
- Row steps: 1 → 1 (none needed — already on correct row!)
- Col steps: 0 → 3 (step = +1): (1,1), (1,2), (1,3)
- Full: (1,0) → (1,1) → (1,2) → (1,3)

---

## Slide 9: Edge Cases
**Same row — only column movement:**
- (2, 0) to (2, 3): just move right
- Path: (2,0) → (2,1) → (2,2) → (2,3)

**Same column — only row movement:**
- (0, 1) to (3, 1): just move down
- Path: (0,1) → (1,1) → (2,1) → (3,1)

**Same position — no movement:**
- (1, 1) to (1, 1): path is just [(1, 1)]
- Manhattan distance = 0

**All of these should work with our algorithm!**

---

## Slide 10: Your Turn!
**Activity: Hand-Trace the Algorithm**
1. Trace the path from (0, 0) to (2, 2)
2. Trace the path from (3, 3) to (0, 1)
3. Trace the path from (1, 3) to (1, 0)
4. Trace the path from (0, 2) to (3, 2)

**For each path:**
- Write out every coordinate in the path
- Count the total number of steps
- Verify: steps = |row difference| + |col difference|

**Checkpoints:**
- Can you trace a path in all four directions?
- Do your step counts match the Manhattan distance?
- Can you handle the "same row" and "same column" cases?

---

## Slide 11: Connection to Next Lesson
**What you did today:**
- Learned the Manhattan distance concept
- Traced the "rows first, then columns" algorithm by hand
- Handled all four directions with step values

**Next lesson (Lesson 5):**
- Implement the Manhattan algorithm as a **Python class**
- Write `compute_path(destination)` that returns a list of tuples
- The computer does the tracing for you!

**Key insight:** You traced by hand today. Next lesson, you'll teach the computer to do the same thing.
