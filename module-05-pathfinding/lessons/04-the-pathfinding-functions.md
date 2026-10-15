# Lesson 4: The Pathfinding Functions

## Overview
Students organize the pathfinding code into a small toolkit of functions, the way Lesson 2-8 organized the sensor code and Lesson 2-9 the driving code. The toolkit has one job: answer "how do I get from here to there?" while remembering which intersections are blocked. Today it gets its shape -- the shared grid settings, a `BLOCKED` list with `add_blocked()` and `clear_blocked()`, a `build_graph()` that leaves blocked intersections out, and a `compute_bfs_path(position, destination)` that is only a placeholder. Lesson 5 fills the placeholder in with the ripples method from Lesson 3.

The lesson is less about new Python than about two design rules every planner in this course follows, which are stated here and never broken afterwards: a planner is *told* the robot's position every time it is asked for a path (it never remembers one -- the driving code owns that), and the path it returns is the list of intersections to drive *to*, so the start is not in it and `len(path)` is the number of steps. Students also meet the reason the blocked list lives at the top of the file as a shared variable: in Lesson 7 the robot will discover obstacles *while driving*, one at a time, and the planner must remember them between calls. `add_blocked()` is the single way anyone tells it -- a paper test in Lesson 6, the rangefinder in Lesson 7, a saved file in Lesson 8.

## Learning Objectives
By the end of this lesson, students will be able to:
- Write `add_blocked(intersection)` so that it records an intersection once, even if told twice
- Write `build_graph(rows, cols, blocked)` so that blocked intersections are neither keys nor anyone's neighbor (one function doing what Lesson 2's `build_grid_graph` and `remove_blocked` did in two)
- State the two planner rules: the position is passed in; the path excludes the start
- Explain why the blocked list is shared at the top of the file and why the graph is rebuilt from it on every call
- Call the placeholder `compute_bfs_path(position, destination)` and read its (empty) result

## Key Concepts
- **Toolkit**: A group of functions that share a few variables at the top of the file and together do one job. The sensor toolkit (Lesson 2-8) shares `reflectance` and `THRESHOLD`; this one shares `ROWS`, `COLS` and `BLOCKED`.
- **`BLOCKED`**: The list of intersections the robot must not drive through. It starts empty and grows as obstacles are found. It is a list, so `add_blocked()` can append to it without the `global` keyword (appending changes the list; it does not reassign the name).
- **`add_blocked(intersection)`**: The one way to tell the planner about an obstacle. Checks `if intersection not in BLOCKED` first, because the robot may see the same wall twice.
- **`build_graph(rows, cols, blocked)`**: Builds the neighbor dictionary for the grid, skipping blocked intersections entirely: they are not keys, and they are left out of every neighbor list. Nothing in the graph connects to them.
- **Rebuilt every call**: `compute_bfs_path()` calls `build_graph(ROWS, COLS, BLOCKED)` itself, every time. On a 4x4 grid this costs nothing, and it means a wall the robot just found is already missing from the graph the next path is planned on. No "forgot to rebuild" bug is possible.
- **The two planner rules**: (1) `compute_xxx_path(position, destination)` -- the planner is told where the robot is. (2) The returned path excludes the start, so `len(path)` is the number of steps and "already there" is `[]`. `compute_manhattan_path` followed both in Module 4.

## Materials Required
- Computers with Python (no robot needed)
- `code/starter/lesson-04-pathfinding-functions.py`
- Lesson 2 code (`build_grid_graph`, `remove_blocked`) for comparison
- Whiteboard

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 8 min
**For 3-hour sessions:** 12 min

1. **Hook: where does the robot keep what it has learned?**
   - "In Lesson 7 the robot is going to drive, see a box in the way with its rangefinder, and have to plan a new route. Where does it write down that the box is there?"
   - Let students propose. Someone will say "pass the blocked list to the function." Push: "The robot finds obstacles one at a time, in the middle of driving. Who keeps the list between one path and the next?"
   - Land on: a list at the top of the file that every function can see, like `reflectance` and `THRESHOLD` in Lesson 2-8. One function adds to it. Every planner reads it.

2. **Two rules we will never break**
   - Write them on the board and leave them there all module:
     - **Rule 1.** `compute_xxx_path(position, destination)`. The planner is *told* where the robot is. It never remembers.
     - **Rule 2.** The path is the list of intersections to drive *to*. The start is not in it.
   - "Module 4's `compute_manhattan_path` already follows both. Check: `compute_manhattan_path((0,0), (0,2))` returns `[(0,1), (0,2)]` -- two steps, no start."
   - Why Rule 1? "The driving code already knows where the robot is. If the planner kept its own copy, the two could disagree, and a planner that thinks the robot is somewhere it isn't will plan from the wrong place. One owner." (Students who did the Navigator extension in Module 4 have seen exactly this.)

### Guided Practice (15 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

1. **The shared variables**
   ```python
   ROWS = 4
   COLS = 4
   BLOCKED = []
   ```
   - "Capital letters because they are settings, not things that change in the middle of a calculation" -- the same convention as `THRESHOLD`. `BLOCKED` does grow, but only through `add_blocked()`.

2. **`add_blocked()` -- write it together**
   ```python
   def add_blocked(intersection):
       if intersection not in BLOCKED:
           BLOCKED.append(intersection)
   ```
   - Ask: "Why the `if`?" (The robot may see the same wall twice; a list with `(2,0)` in it twice is harmless but untidy, and `print_grid` would be confusing.)
   - Ask: "Does this need `global BLOCKED`?" No -- `append` changes the list that `BLOCKED` already names; it does not assign a new value to the name `BLOCKED`. Connect to Lesson 2-8's `set_threshold()`, which *did* need `global` because `THRESHOLD = new_value` is a reassignment.
   - `clear_blocked()` empties the list in place for the same reason (`pop()` until empty), and exists so tests can start fresh.

3. **`build_graph()` -- Lesson 2's two functions become one**
   - Show Lesson 2's `build_grid_graph(rows, cols)` and `remove_blocked(graph, blocked)` side by side. "Today we do both in one pass: while building, skip anything blocked."
   ```python
   def build_graph(rows, cols, blocked):
       graph = {}
       for r in range(rows):
           for c in range(cols):
               if (r, c) in blocked:
                   continue
               neighbors = []
               for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                   nr, nc = r + dr, c + dc
                   if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in blocked:
                       neighbors.append((nr, nc))
               graph[(r, c)] = neighbors
       return graph
   ```
   - Two `in blocked` checks: one skips the intersection as a key, one keeps it out of its neighbors' lists. "Both are needed. Miss the second and the graph still has edges *into* the wall."
   - The four `(dr, dc)` pairs are up, down, left, right -- in that order. Lesson 3's trace used the same order, which is why the printed path matched.

4. **The placeholder**
   ```python
   def compute_bfs_path(position, destination):
       graph = build_graph(ROWS, COLS, BLOCKED)
       print("compute_bfs_path is not written yet!")
       return []
   ```
   - "Notice it builds the graph itself, from `BLOCKED`, every time it is called. Why not build it once at the top?" Discuss: a wall found at step 3 must be gone from the graph used at step 4. Rebuilding on every call makes that automatic. On a 4x4 grid it takes no time worth measuring.

### Independent Practice (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

Starter file: `code/starter/lesson-04-pathfinding-functions.py`.

**Exercise 1: `add_blocked()`.** Fill in the body. Test: add `(1, 1)` twice; `BLOCKED` should hold it once.

**Exercise 2: `build_graph()`.** Fill in the two `in blocked` checks. Test on the open 4x4: 16 keys; `(0, 0)` has 2 neighbors, `(1, 1)` has 4.

**Exercise 3: Block and rebuild.** `add_blocked((1, 1))`, rebuild. Check three things: 15 keys; `(1, 1) in graph` is `False`; `graph[(0, 1)]` no longer lists `(1, 1)`.

**Exercise 4: Rule 2 by hand.** Without running anything, write what `compute_bfs_path((0, 0), (0, 2))` *should* return once Lesson 5 is done, and what `compute_bfs_path((2, 2), (2, 2))` should return. (`[(0, 1), (0, 2)]` and `[]`.)

**Exercise 5 (challenge): a wall.** `add_blocked((1, 0))`, `add_blocked((1, 1))`. Rebuild and print the whole graph. Which intersections in row 0 can still reach row 2, and through what?

### Assessment

**Formative (during lesson)**:
- Can students say the two rules without looking?
- Ask: "If `BLOCKED` were rebuilt into the graph only once at the top of the file, what would go wrong in Lesson 7?" (New obstacles would never affect planning.)
- Watch for a `build_graph` that skips blocked keys but still lists them as neighbors.

**Summative (worksheet/exit ticket)**:
- Exercises 1-4 complete and checked against the expected outputs
- Exit ticket: "Why does `add_blocked()` not need `global`, when `set_threshold()` in Lesson 2-8 did?"

## Common Misconceptions
- **"The planner should remember where the robot is."** It must not. The driving code owns position; the planner is told it. Two owners of the same fact is how robots end up planning from an intersection they left three steps ago.
- **"`BLOCKED.append(...)` needs `global BLOCKED`."** No. `global` is needed to *reassign* a module-level name. Appending to a list changes the list, not the name.
- **"Build the graph once; it's wasteful to rebuild."** On this grid it is free, and rebuilding is what makes a freshly found obstacle count. Correctness first.
- **"A blocked intersection is in the graph with no neighbors."** It is not in the graph at all. Not a key, not in any list. That is why BFS never has to check for it.
- **"The path starts with the start."** Rule 2. The robot is already there.

## Differentiation
**For struggling students**: Give `build_graph` complete and have them do only `add_blocked` and Exercises 3-4. The rules matter more than the loops.

**For advanced students**: Exercise 5, then: "Write `is_reachable(a, b)` that returns True if there is *any* route from a to b, using only `build_graph` and Lesson 3's idea." They will write most of BFS a lesson early; that is fine.

## Materials & Code Examples

### The complete toolkit (Lesson 4 version)

See `code/solutions/lesson-04-pathfinding-functions.py`: `ROWS`, `COLS`, `BLOCKED`, `add_blocked()`, `clear_blocked()`, `build_graph()`, and the placeholder `compute_bfs_path()`, with a test program that builds the graph, blocks `(1, 1)`, and shows the intersection vanishing from its neighbors' lists.

### Expected output, Exercise 3

```
Blocked: [(1, 1)]
Number of intersections: 15
(1,1) in graph? False
Neighbors of (0,1): [(0, 0), (0, 2)]  <- (1,1) is gone from the list
Blocked after adding (1,1) again: [(1, 1)]
```

### `global` or not: the comparison students should see

```python
THRESHOLD = 0.5
BLOCKED = []

def set_threshold(new_value):     # Lesson 2-8
    global THRESHOLD              # needed: this line REASSIGNS the name
    THRESHOLD = new_value

def add_blocked(intersection):    # Lesson 5-4
    if intersection not in BLOCKED:
        BLOCKED.append(intersection)   # not needed: this CHANGES the list
```

## Teaching Notes
- Keep the two rules on the board for the rest of the module. Every later lesson -- the harness in Lesson 6, the rangefinder loop in Lesson 7, the saved file in Lesson 8 -- leans on them.
- The "one owner of position" argument lands best as a story: the robot finds a wall at step 2 of a 5-step path, re-plans, and the planner that remembered the *destination* as its position now plans from a place the robot never reached. Students who did Module 4's Navigator extension will recognize it.
- Do not rush the `global` comparison. It is the one place in the course where the keyword comes up twice, and the contrast (reassign vs. change in place) is the whole explanation.

## Connections to Next Lessons
- **Lesson 5** replaces the placeholder with the ripples method: `previous`, `to_visit`, the walk-back.
- **Lesson 6** tests the planner by properties and swaps it in for Manhattan. `clear_blocked()` is what lets each test start clean.
- **Lesson 7** calls `add_blocked()` from the rangefinder loop -- the same call the tests make.
- **Lesson 8** calls it again for every line of a saved file.
