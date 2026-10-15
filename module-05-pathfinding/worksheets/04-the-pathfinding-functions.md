# Lesson 4 Worksheet: The Pathfinding Functions

**Name:** ________________________
**Date:** ________________________

---

## Part A: The two rules

**1.** Rule 1 says a planner is **told** the robot's position every time, and never remembers one. Who *does* keep track of where the robot is?

_______________________________________________________________

**2.** Give one thing that could go wrong if the planner kept its own copy of the robot's position.

_______________________________________________________________

_______________________________________________________________

**3.** Rule 2 says the path is the list of intersections to drive **to**. Fill in what these should return once Lesson 5 is finished (no obstacles):

| Call | Returns | Steps |
|---|---|---|
| `compute_bfs_path((0, 0), (0, 2))` | | |
| `compute_bfs_path((2, 2), (2, 2))` | | |
| `compute_bfs_path((1, 0), (0, 0))` | | |

**4.** Why is it useful that `len(path)` equals the number of steps?

_______________________________________________________________

---

## Part B: The shared list

```python
ROWS = 4
COLS = 4
BLOCKED = []
```

**5.** `BLOCKED` is written in capital letters, like `THRESHOLD` in Lesson 2-8, but it changes during the program. How is it allowed to change? (Through which function?)

_______________________________________________________________

**6.** Write `add_blocked()`. It must not add the same intersection twice.

```python
def add_blocked(intersection):



```

**7.** `set_threshold()` in Lesson 2-8 needed the line `global THRESHOLD`. `add_blocked()` does not need `global BLOCKED`. Why not? (Hint: one of them *reassigns* a name; the other *changes* a list.)

_______________________________________________________________

_______________________________________________________________

**8.** Who will call `add_blocked()`? Name all three you know of from this module's plan.

- Lesson 6: ________________________________
- Lesson 7: ________________________________
- Lesson 8: ________________________________

---

## Part C: `build_graph()`

In Lesson 2 you built the graph with `build_grid_graph()` and then removed blocked intersections with `remove_blocked()`. Now one function does both.

**9.** `build_graph()` checks `in blocked` in **two** places. What does each check do?

- First check (`if (r, c) in blocked: continue`): _____________________________________

- Second check (`... and (nr, nc) not in blocked`): _____________________________________

**10.** Suppose someone wrote the first check but forgot the second. `(1, 1)` is blocked. What would `graph[(0, 1)]` wrongly contain?

_______________________________________________________________

**11.** The neighbor directions are checked in this order: `(-1, 0)`, `(1, 0)`, `(0, -1)`, `(0, 1)`. Write what each one means:

| `(dr, dc)` | Direction |
|---|---|
| `(-1, 0)` | |
| `(1, 0)` | |
| `(0, -1)` | |
| `(0, 1)` | |

**12.** For a 4×4 grid with `(1, 1)` blocked, fill in:

- Number of keys in the graph: ______
- `(1, 1) in graph` → ______
- `graph[(0, 1)]` → ______________________________
- `graph[(2, 1)]` → ______________________________

---

## Part D: Rebuilt every time

```python
def compute_bfs_path(position, destination):
    graph = build_graph(ROWS, COLS, BLOCKED)
    ...
```

**13.** The graph is built *inside* the planner, every time it is called, instead of once at the top of the file. In Lesson 7 the robot will find a wall at step 2 of a 5-step path and ask for a new path. Explain what would go wrong if the graph had been built only once.

_______________________________________________________________

_______________________________________________________________

**14.** On a 4×4 grid, is rebuilding the graph on every call a problem for speed? ______ Roughly how many intersections does it visit to do so? ______

---

## Part E: Run it

Run your `lesson-04-pathfinding-functions.py`.

**15.** After `add_blocked((1, 1))` and a rebuild, copy the line the program prints for the neighbors of `(0, 1)`:

_______________________________________________________________

**16.** What does the placeholder `compute_bfs_path()` return right now? ______ What message does it print?

_______________________________________________________________

---

## Exit ticket

In one sentence each: what is Rule 1, and what is Rule 2?

_______________________________________________________________

_______________________________________________________________
