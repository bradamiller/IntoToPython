# Lesson 5: Implementing compute_bfs_path()

## Overview
Students turn the Lesson 3 hand trace into working Python. The function is about twenty lines, and every one of them is something they already did with a pencil: `previous` is the came-from table, `to_visit` is the list they kept beside the grid, `pop(0)` is "take the oldest one", the `for` loop is "look at every neighbor", `if neighbor not in previous` is "only if it has no number yet", and the walk-back is following the arrows back from the destination. The lesson is built so students write the function in three stages, run the paper tests from Lesson 3 after each, and compare the program's `print_grid()` with their own grids.

The function obeys the two rules from Lesson 4 without any special code: it is told `position`, and the walk-back stops *at* the start (`while current != position`) so the start is never appended and the path excludes it naturally. Two edge cases get tests: "already there" returns `[]` because the walk-back loop never runs, and "walled off" returns `[]` because the destination never appears in `previous`.

The Optional Extension repackages the toolkit as a `BFS` class (and gives `Manhattan` a matching class so Lesson 6's swap works with objects too). It is the same four mechanical changes as every extension so far, and it is done after the functions version passes all five paper tests.

## Learning Objectives
By the end of this lesson, students will be able to:
- Map each line of `compute_bfs_path()` to a step of the paper method
- Explain why `to_visit.pop(0)` (oldest first) matters, and what `pop()` (newest first) would do instead
- Explain why `if neighbor not in previous` is the whole "numbered once" rule
- Write the walk-back so the returned path excludes the start, and explain why "already there" gives `[]`
- Return `[]` when the destination is walled off, and say which test catches it
- Run the five paper tests and compare `print_grid()` with their own grid
- *(Extension)* Repackage the toolkit as a `BFS` class with `add_blocked()` and `compute_path(position, destination)` methods

## Key Concepts
- **`previous`**: A dictionary from each *reached* intersection to the one it was reached from. The start maps to `None`. "Reached" and "is a key in `previous`" are the same thing, so `previous` is also the record of which intersections have a number.
- **`to_visit`**: The ring being worked on, as a list. New intersections go on the end (`append`); the next one to look around comes off the front (`pop(0)`). A list used this way is a **queue**: first in, first out.
- **`pop(0)` vs `pop()`**: `pop(0)` takes the oldest item; `pop()` takes the newest. BFS needs the oldest. With the newest, the search dives down one path before finishing the ring (depth-first search) and the first path it finds is not necessarily shortest.
- **Walk-back**: `current = destination; while current != position: path.append(current); current = previous[current]`, then `path.reverse()`. Stops at the start without appending it (Rule 2).
- **No path**: if `destination not in previous` after the search, it was never reached: return `[]`. The same `[]` means "already there" when `position == destination` -- the harness in Lesson 6 tells those two cases apart.
- **`bfs_rings()` and `print_grid()`**: a version of the search that does not stop at the destination, returning every intersection's ring number, and a function that draws them on the grid with `X` for blocked. For the picture only; `compute_bfs_path()` is the planner.

## Materials Required
- Computers with Python (no robot needed)
- `code/starter/lesson-05-compute-bfs-path.py`
- Students' Lesson 3 worksheets (the paper traces are today's test cases)

## Lesson Flow

### Introduction (8 minutes)
**For 50-min classes:** 6 min
**For 3-hour sessions:** 10 min

1. **Every line is something you already did**
   - Put the Lesson 3 preview loop on the board next to a student's filled-in Part C worksheet. Go line by line and ask "which pencil step is this?"
     - `previous = {position: None}` -- the first row of the came-from table
     - `to_visit = [position]` -- the list beside the grid, with the start on it
     - `current = to_visit.pop(0)` -- take the oldest one off the front
     - `if current == destination: break` -- the destination got its number; stop
     - `for neighbor in graph[current]` -- look at each neighbor
     - `if neighbor not in previous` -- only if it has no number yet
     - `previous[neighbor] = current` -- write "came from"
     - `to_visit.append(neighbor)` -- add it to the end of the list
   - "There is no step on this board that you didn't do on Tuesday. Today you type it."

2. **What's missing**
   - The loop reaches the destination. It doesn't produce the path. "What did you do after the numbers were in?" Walked back along came-from. That's the second half.

### Guided Practice (17 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

Build the function in three stages, running after each.

1. **Stage 1: setup and the guard**
   ```python
   def compute_bfs_path(position, destination):
       graph = build_graph(ROWS, COLS, BLOCKED)
       if position not in graph or destination not in graph:
           return []
       previous = {position: None}
       to_visit = [position]
   ```
   - The guard handles a destination (or start) that is itself blocked: not in the graph, so nothing to search. Return `[]` right away.

2. **Stage 2: the search**
   ```python
       while len(to_visit) > 0:
           current = to_visit.pop(0)
           if current == destination:
               break
           for neighbor in graph[current]:
               if neighbor not in previous:
                   previous[neighbor] = current
                   to_visit.append(neighbor)
   ```
   - Run it with a `print(previous)` after the loop on the 3x3 with (1,1) blocked, (0,0) to (2,2). Compare with the Lesson 3 came-from table. They should match exactly, including the order the keys appear in.
   - Ask: "What happens to `to_visit` if the destination is walled off?" It empties out; the `while` ends; `destination` is not in `previous`.

3. **Stage 3: the walk-back**
   ```python
       if destination not in previous:
           return []
       path = []
       current = destination
       while current != position:
           path.append(current)
           current = previous[current]
       path.reverse()
       return path
   ```
   - "Why `while current != position` and not `while current is not None`?" Both would work for the search, but stopping *at* the start means the start is never appended, which is Rule 2 with no `[1:]` needed. And when `position == destination`, the loop never runs and the path is `[]` -- "already there" -- for free.
   - Run the five paper tests (in the solution file): open grid, straight line, already there, wall, walled off. Expected step counts 6, 3, 0, 7, 0.

### Independent Practice (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

Starter file: `code/starter/lesson-05-compute-bfs-path.py`, with the three stages as TODOs and the five tests commented out.

**Exercise 1: Build it in stages.** Uncomment the tests one at a time. All five must pass with the expected step counts before moving on.

**Exercise 2: Compare with paper.** Your Lesson 3 Part C path and the program's path: same number of steps? Same path? If the path differs, explain why both are right.

**Exercise 3: Break it on purpose, then fix it.**
- Change `pop(0)` to `pop()`. Run the open-grid test. Count the steps. Why is it longer? (Depth-first: it dives down one path before finishing the ring.)
- Delete `if neighbor not in previous:` (keep the two lines under it). What happens? (Intersections get overwritten with later, longer "came from" entries; the walk-back can loop forever or return a wrong path. Stop it with Ctrl-C.)
- Put both back.

**Exercise 4: The picture.** Uncomment the `print_grid(ROWS, COLS, BLOCKED, bfs_rings((0, 0)))` block with the wall at (1,0),(1,1). Compare with your Lesson 3 Part D grid.

**Exercise 5 (challenge):** Make `compute_bfs_path` print the to-visit list after every `pop(0)`, and check it against the to-visit column of the Lesson 3 trace table.

### Assessment

**Formative (during lesson)**:
- Students can point at each line and name the pencil step
- The five tests pass in order; Exercise 3's two breakages are explained, not just observed
- Ask: "Why does `[]` come back for 'already there'?" (The walk-back loop never runs.)

**Summative (worksheet/exit ticket)**:
- Worksheet Parts A-D
- Exit ticket: "Your walk-back is `while current is not None` and it appends `current` each time. What is wrong with the path it returns?" (It includes the start -- Rule 2 broken; `len(path)` is one too many.)

## Common Misconceptions
- **"`pop()` and `pop(0)` are the same."** They are opposite ends of the list. BFS lives or dies on `pop(0)`.
- **"I should stop as soon as I *see* the destination as a neighbor."** You can (it saves a few steps), but stopping when you *pop* it is simpler and the course keeps it that way. Either gives a shortest path.
- **"`previous` needs every intersection in it at the start."** No. It grows as intersections are reached; that is what makes `not in previous` mean "not reached yet". (Module 6's Dijkstra also starts `distance` with just the start, for the same reason.)
- **"The walk-back loop should run until `None`."** That includes the start. Stop at `position`.
- **"An empty path means something went wrong."** It means "already there" or "no way through". Lesson 6's harness checks which.

## Differentiation
**For struggling students**: Give Stages 1 and 2 complete; have them write only the walk-back, run the tests, and do Exercise 2.

**For advanced students**: Exercise 5, then: "Rewrite the walk-back without `reverse()` by inserting at the front (`path.insert(0, current)`). Which is clearer?" Then the Optional Extension.

## Materials & Code Examples

### The complete function

See `code/solutions/lesson-05-compute-bfs-path.py`. The planner itself:

```python
def compute_bfs_path(position, destination):
    graph = build_graph(ROWS, COLS, BLOCKED)
    if position not in graph or destination not in graph:
        return []

    previous = {position: None}
    to_visit = [position]

    while len(to_visit) > 0:
        current = to_visit.pop(0)
        if current == destination:
            break
        for neighbor in graph[current]:
            if neighbor not in previous:
                previous[neighbor] = current
                to_visit.append(neighbor)

    if destination not in previous:
        return []

    path = []
    current = destination
    while current != position:
        path.append(current)
        current = previous[current]
    path.reverse()
    return path
```

### Expected output of the five tests

```
=== Test 1: no obstacles, (0,0) to (3,3) ===
Path: [(1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3)]
Steps: 6 (expect 6)

=== Test 2: straight line, (0,0) to (0,3) ===
Path: [(0, 1), (0, 2), (0, 3)]
Steps: 3 (expect 3)

=== Test 3: already there, (2,2) to (2,2) ===
Path: []
Steps: 0 (expect 0)

=== Test 4: wall across the grid, (0,0) to (3,0) ===
Blocked: [(1, 0), (1, 1)]
Path: [(0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (3, 1), (3, 0)]
Steps: 7 (expect 7 -- around the wall)

=== Test 5: destination walled off ===
Blocked: [(1, 0), (1, 1), (1, 2), (1, 3)]
Path: []
Steps: 0 (expect 0 -- no way through)
```

Test 1's exact path may differ from a student's and still be right; the step count must match.

### `bfs_rings()` and `print_grid()`

In the solution file. `bfs_rings(position)` is the search without the `break`, keeping a `ring` dictionary instead of `previous`; `print_grid(rows, cols, blocked, numbers)` draws it. Students compare the picture with their Lesson 3 grids.

## Teaching Notes
- Three stages, run after each. Students who type the whole thing and then debug lose the mapping to the paper method, which is the whole point.
- Exercise 3 is not optional. Seeing `pop()` give a longer path is what makes "oldest first" stick; seeing the missing `not in previous` hang the program is what makes "numbered once" stick.
- Keep `distances`, `999999` and "closest first" out of the room. If anyone asks about roads that take longer, that is Module 6, and it is exactly two changes to this function.

## Connections to Next Lessons
- **Lesson 6** tests this function by properties and swaps it in for Manhattan. The five tests here become six in the harness.
- **Lesson 7** calls it from the obstacle loop every time the rangefinder finds a wall.
- **Module 6 (optional)** changes `pop(0)` to "take the closest" and `+1 step` to `+ weight` -- and nothing else.

---

## Optional Extension: Package It as a `BFS` Class

*Do this after the functions version passes all five tests. It is not graded.*

### Why wrap it?

Two reasons, and it is worth saying both out loud. `BFS` is a class because it has setup to hold: the grid size and the blocked list. `Manhattan` gets a class too, but *only* so that it has the same shape as `BFS` -- then one main program and one test harness (Lesson 6) work with either by changing one name. That second reason is the swap, and it is the point.

Neither class remembers where the robot is. Rule 1 holds for classes too: `compute_path(position, destination)` is told the position every time.

### Side by side

| Functions (required) | Class (extension) |
|---|---|
| `ROWS = 4`, `COLS = 4`, `BLOCKED = []` at the top of the file | `self.rows`, `self.cols`, `self.blocked` set in `__init__` |
| `def add_blocked(intersection):` | `def add_blocked(self, intersection):` |
| `def compute_bfs_path(position, destination):` | `def compute_path(self, position, destination):` |
| `build_graph(ROWS, COLS, BLOCKED)` | `build_graph(self.rows, self.cols, self.blocked)` |
| `add_blocked((1, 1))` | `planner.add_blocked((1, 1))` |
| `compute_bfs_path((0, 0), (3, 3))` | `planner.compute_path((0, 0), (3, 3))` |

The same four changes as every extension: the functions move inside `class BFS:` and gain `self`; the shared variables move into `__init__` as `self.x`; inside the methods they gain `self.`; from outside, calls go through the object.

```python
class BFS:
    def __init__(self, rows=4, cols=4):
        self.rows = rows
        self.cols = cols
        self.blocked = []

    def add_blocked(self, intersection):
        if intersection not in self.blocked:
            self.blocked.append(intersection)

    def compute_path(self, position, destination):
        graph = build_graph(self.rows, self.cols, self.blocked)
        ...   # the function body, unchanged
```

And `Manhattan`, with an `add_blocked()` that deliberately does nothing:

```python
class Manhattan:
    def __init__(self):
        pass        # no setup -- it is a class only to match BFS

    def add_blocked(self, intersection):
        # Manhattan cannot route around obstacles. This exists so every
        # planner can be tested the same way. It deliberately does nothing.
        pass

    def compute_path(self, position, destination):
        ...   # compute_manhattan_path, unchanged
```

### Testing it

`code/solutions/lesson-05-bfs-class-addon.py` runs the wall test against both objects. `BFS` goes around; `Manhattan` drives straight through the wall -- the same two lines of output, the same calls, different objects.

### Discussion prompt

"Why give `Manhattan` an `add_blocked()` that does nothing?" Because the harness in Lesson 6 calls `planner.add_blocked(...)` on whatever planner it is handed. If `Manhattan` didn't have one, the harness would need to know which planner it had -- and the whole point of the swap is that it doesn't.
