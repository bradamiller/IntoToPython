# Lesson 6 Worksheet: Testing and Swapping Pathfinders

**Name:** ________________________
**Date:** ________________________

---

## Part A: Predict Dijkstra Output

For each scenario, predict the path returned by `compute_dijkstra_path()`.

**Setup:**
```python
graph = build_dijkstra_graph(4, 4, blocked)
path = compute_dijkstra_path(position, destination, graph)
print(path)
```

**Scenario 1:** 4x4 grid, position = (0, 0), blocked = [], destination = (3, 3)

Predicted path: ____________________________________________________________________

Path length: __________

**Scenario 2:** 4x4 grid, position = (0, 0), blocked = [(1, 1)], destination = (2, 2)

Predicted path: ____________________________________________________________________

Path length: __________

**Scenario 3:** 4x4 grid, position = (0, 0), blocked = [(0, 1), (1, 0)], destination = (0, 2)

Predicted path: ____________________________________________________________________

Explanation: ____________________________________________________________________

**Scenario 4:** 4x4 grid, position = (1, 1), blocked = [(0, 1), (1, 0), (1, 2), (2, 1)], destination = (3, 3)

Predicted path: ____________________________________________________________________

Explanation: ____________________________________________________________________

**Scenario 5:** 4x4 grid, position = (0, 0), blocked = [(0, 1), (1, 0)], destination = (0, 0)

Predicted path: ____________________________________________________________________

Explanation: ____________________________________________________________________

---

## Part B: Compare Manhattan vs Dijkstra Paths

`compute_manhattan_path` moves in straight lines (all rows first, then all columns, or vice versa). `compute_dijkstra_path` finds the true shortest path around obstacles.

Fill in the table for a **4x4 grid**:

| Position | Dest | Blocked | Manhattan Path | Man. Length | Dijkstra Path | Dijk. Length | Winner |
|---|---|---|---|---|---|---|---|
| (0,0) | (3,3) | none | __________________ | ______ | __________________ | ______ | ______ |
| (0,0) | (3,3) | (1,1),(2,2) | __________________ | ______ | __________________ | ______ | ______ |
| (0,0) | (0,3) | (0,1) | __________________ | ______ | __________________ | ______ | ______ |
| (0,0) | (2,0) | (1,0) | __________________ | ______ | __________________ | ______ | ______ |

**1. When do Manhattan and Dijkstra give the same result?**

____________________________________________________________________

**2. When does Dijkstra give a shorter path?**

____________________________________________________________________

**3. Can Manhattan ever give a shorter path than Dijkstra?** YES / NO

Why? ____________________________________________________________________

---

## Part C: Swapping Algorithms

Below is a program that uses `compute_manhattan_path`. Mark which lines would need to change to swap to `compute_dijkstra_path` using the `compute_path()` dispatch function.

```python
# Line 1:  blocked = [(1, 1), (2, 2)]
# Line 2:  path = compute_path("manhattan", (0, 0), (3, 3), blocked)
# Line 3:  print("Path:", path)
# Line 4:  print("Steps:", len(path))
```

**Which line changes?** Circle the line number: 1  2  3  4

**Rewrite the line that changes:**

Line ___: ____________________________________________________________________

**Which lines stay exactly the same?** ____________________

**Why can we swap algorithms without changing most of the code?**

____________________________________________________________________

____________________________________________________________________

**What does `compute_path()` normalize between the two algorithms?**

| Feature | compute_manhattan_path | compute_dijkstra_path | compute_path() dispatch |
|---|---|---|---|
| Parameters | __________ | __________ | __________ |
| Includes start in output? | __________ | __________ | __________ |
| Considers obstacles? | __________ | __________ | __________ |

---

## Part D: Edge Cases

**1. What happens when the destination is blocked?**

```python
graph = build_dijkstra_graph(4, 4, [(2, 2)])
path = compute_dijkstra_path((0, 0), (2, 2), graph)
```

What does `compute_dijkstra_path` return? __________

What message is printed? ____________________________________________________

**2. What happens when the start is blocked?**

Think about this: if `(0, 0)` is in the blocked list, what happens when we build the graph?

```python
graph = build_dijkstra_graph(4, 4, [(0, 0)])
path = compute_dijkstra_path((0, 0), (3, 3), graph)
```

Is `(0, 0)` in `graph`? __________

What happens when `compute_dijkstra_path` tries to set `distances[position] = 0`?

____________________________________________________________________

**3. What happens when there is no path?**

```python
# All neighbors of (0,0) are blocked, but destination is not blocked
graph = build_dijkstra_graph(4, 4, [(0, 1), (1, 0)])
path = compute_dijkstra_path((0, 0), (3, 3), graph)
```

What happens? ____________________________________________________________________

**4. What happens when start equals destination?**

```python
graph = build_dijkstra_graph(4, 4, [])
path = compute_dijkstra_path((0, 0), (0, 0), graph)
```

What does `compute_dijkstra_path` return? __________

Is this the correct result? __________

Why? ____________________________________________________________________

---

## Answer Key

### Part A:
1. `[(0,0), (0,1), (0,2), (0,3), (1,3), (2,3), (3,3)]` or equivalent shortest path, length = 6
2. `[(0,0), (0,1), (0,2), (1,2), (2,2)]` or `[(0,0), (1,0), (2,0), (2,1), (2,2)]`, length = 4
3. `[]` with "No path found!" — (0,0) has no unblocked neighbors, so no path exists to (0,2).
4. (1,1) is surrounded by blocked cells, so it cannot reach any neighbor. Path = [] with "No path found!"
5. `[(0,0)]` — Start and destination are the same. The algorithm immediately finds current == destination and returns a path of length 0.

### Part B:
1. When there are no obstacles in the Manhattan path, both give the same length (6 steps).
2. When obstacles block the Manhattan route but an alternative path exists.
3. No. Dijkstra always finds the true shortest path. Manhattan might match it but can never beat it.

### Part C:
- Line that changes: 2
- Line 2: `path = compute_path("dijkstra", (0, 0), (3, 3), blocked)`
- Lines 1, 3, 4 stay the same
- Both branches of `compute_path()` return the same shape of result -- a list of tuples not including position -- so the calling code never needs to know which algorithm ran.

| Feature | compute_manhattan_path | compute_dijkstra_path | compute_path() dispatch |
|---|---|---|---|
| Parameters | position, destination | position, destination, graph | algorithm, position, destination, blocked |
| Includes start in output? | No | Yes | No (normalized) |
| Considers obstacles? | No | Yes | Depends on algorithm chosen |

### Part D:
1. Returns `[]`, prints "Destination is blocked!"
2. (0,0) is not in the graph. `distances[position] = 0` will cause a KeyError because (0,0) is not a key in distances.
3. The algorithm runs but never reaches (3,3) from (0,0) because (0,0) has no neighbors. The path reconstruction produces a path not starting at (0,0), so it prints "No path found!" and returns [].
4. Returns `[(0,0)]` — a path containing just the start/destination. This is correct; you are already there.

---

## Part E (Optional Extension): True Polymorphism

*Skip this section if your course doesn't cover classes.*

**1. With the `Manhattan`/`Dijkstra` classes from the Optional Extension, rewrite Part C's Line 2 without a dispatch function:**

```python
pathfinder = _______________________________________________
path = pathfinder.compute_path((3, 3))
```

**2. Why doesn't this version need an `if algorithm == "manhattan"` check anywhere?**

____________________________________________________________________
