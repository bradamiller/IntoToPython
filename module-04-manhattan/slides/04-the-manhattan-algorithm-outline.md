# Lesson 4 Slide Outline: The Manhattan Algorithm

## Slide 1: Title & Learning Objectives
**Title:** The Manhattan Algorithm

**Learning Objectives:**
- Understand how Manhattan distance pathfinding works
- Write a `compute_path(start, end)` function using while loops
- Build up from positive directions only to all four directions
- Test your function with edge cases

**Agenda:**
- What is Manhattan distance? (5 min)
- The algorithm: rows first, then columns (5 min)
- Part 1: Write `compute_path` for south/east only (15 min)
- Part 2: Add north/west loops (15 min)
- Edge cases and testing (5 min)

---

## Slide 2: Hook — How Do You Walk in a City?
**Question:** "If you're at 1st Street & 1st Avenue and need to get to 4th Street & 3rd Avenue, how do you walk?"

**You can't cut diagonally through buildings!**
- Walk along streets (rows) and avenues (columns)
- Go south first, then east — or vice versa

**This is Manhattan distance** — named after the grid layout of Manhattan, New York City.

**Our robot has the same constraint:** It drives along grid lines, not diagonally.

---

## Slide 3: Manhattan Distance
**Manhattan distance:** The total number of row steps + column steps between two points.

**Example:**
- Start: (0, 0)
- End: (2, 3)
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
- (1, 0) → (2, 0)

**Step 2: Move along columns (0 → 3)**
- (2, 1) → (2, 2) → (2, 3)

**Full path (not including start):**
```
[(1,0), (2,0), (2,1), (2,2), (2,3)]
```

**Steps = len(path) = 5 (matches Manhattan distance!)**

---

## Slide 5: Part 1 — Positive Directions Only
**Goal:** Write `compute_path(start, end)` that works when the destination is south and/or east of the start.

**Key ideas:**
- `path = []` — the path does NOT include the starting position
- Use tuple unpacking: `current_row, current_col = start`
- Two while loops: one for south (rows increase), one for east (columns increase)

**Code:**
```python
def compute_path(start, end):
    path = []
    current_row, current_col = start
    dest_row, dest_col = end

    # Move south (rows increase)
    while current_row < dest_row:
        current_row = current_row + 1
        path.append((current_row, current_col))

    # Move east (columns increase)
    while current_col < dest_col:
        current_col = current_col + 1
        path.append((current_row, current_col))

    return path
```

**Main program:**
```python
path = compute_path((0, 0), (2, 3))
print("(0,0) to (2,3):", path)
print("Steps:", len(path))
```

---

## Slide 6: Trace Part 1
**Trace: `compute_path((0, 0), (2, 3))`**

| Variable | Value |
|---|---|
| current_row, current_col | 0, 0 |
| dest_row, dest_col | 2, 3 |

**South loop** (current_row < dest_row):
- current_row = 1, append (1, 0)
- current_row = 2, append (2, 0)
- 2 < 2 is False — loop stops

**East loop** (current_col < dest_col):
- current_col = 1, append (2, 1)
- current_col = 2, append (2, 2)
- current_col = 3, append (2, 3)
- 3 < 3 is False — loop stops

**Result:** `[(1,0), (2,0), (2,1), (2,2), (2,3)]` — 5 steps

---

## Slide 7: Part 1 Works... But Not Everywhere
**Try:** `compute_path((3, 3), (1, 0))`

**South loop:** `while 3 < 1` — False! Loop never runs.
**East loop:** `while 3 < 0` — False! Loop never runs.

**Result:** `[]` — That's wrong! The path should have 5 steps.

**The problem:** Our while loops only handle increasing values. We need loops for the other directions too.

---

## Slide 8: Part 2 — Add North and West Loops
**Fix:** Add two more while loops. No if/else needed — only the loops that apply will run.

```python
def compute_path(start, end):
    path = []
    current_row, current_col = start
    dest_row, dest_col = end

    # Move south (rows increase)
    while current_row < dest_row:
        current_row = current_row + 1
        path.append((current_row, current_col))

    # Move north (rows decrease)
    while current_row > dest_row:
        current_row = current_row - 1
        path.append((current_row, current_col))

    # Move east (columns increase)
    while current_col < dest_col:
        current_col = current_col + 1
        path.append((current_row, current_col))

    # Move west (columns decrease)
    while current_col > dest_col:
        current_col = current_col - 1
        path.append((current_row, current_col))

    return path
```

**Why no if/else?** If current_row < dest_row, the north loop's condition (`current_row > dest_row`) is automatically False. Only the correct loop runs!

---

## Slide 9: Trace Part 2
**Trace: `compute_path((3, 3), (1, 0))`**

**South loop:** `while 3 < 1` — False, skipped.

**North loop** (current_row > dest_row):
- current_row = 2, append (2, 3)
- current_row = 1, append (1, 3)
- 1 > 1 is False — loop stops

**East loop:** `while 3 < 0` — False, skipped.

**West loop** (current_col > dest_col):
- current_col = 2, append (1, 2)
- current_col = 1, append (1, 1)
- current_col = 0, append (1, 0)
- 0 > 0 is False — loop stops

**Result:** `[(2,3), (1,3), (1,2), (1,1), (1,0)]` — 5 steps

---

## Slide 10: Edge Cases
**Same row — only column movement:**
- `compute_path((2, 0), (2, 3))` → `[(2,1), (2,2), (2,3)]`
- Both row loops skip, east loop runs. 3 steps.

**Same column — only row movement:**
- `compute_path((0, 2), (3, 2))` → `[(1,2), (2,2), (3,2)]`
- South loop runs, both column loops skip. 3 steps.

**Same position — no movement:**
- `compute_path((1, 1), (1, 1))` → `[]`
- All four loops skip. 0 steps.

**All of these work with our four-loop function!**

---

## Slide 11: Connection to Next Lesson
**What you did today:**
- Learned the Manhattan distance concept
- Wrote `compute_path` with 2 while loops (south/east only)
- Extended it to 4 while loops (all directions)
- Tested edge cases: same row, same column, same position

**Next lesson (Lesson 5):**
- Build a `Navigator` class that uses `compute_path` to plan routes
- The navigator will turn the path into driving instructions for the robot

**Key insight:** Four simple while loops — no if/else needed — handle all four directions.
