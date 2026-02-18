# Lesson 6 Worksheet: Testing and Swapping Pathfinders

**Name:** ________________________
**Date:** ________________________

---

## Part A: Predict Dijkstra Output

For each scenario, predict the path returned by `compute_path()`.

**Setup:**
```python
pathfinder = Dijkstra(start, blocked)
path = pathfinder.compute_path(destination)
print(path)
```

**Scenario 1:** 4x4 grid, start = (0, 0), blocked = [], destination = (3, 3)

Predicted path: ____________________________________________________________________

Path length: __________

**Scenario 2:** 4x4 grid, start = (0, 0), blocked = [(1, 1)], destination = (2, 2)

Predicted path: ____________________________________________________________________

Path length: __________

**Scenario 3:** 4x4 grid, start = (0, 0), blocked = [(0, 1), (1, 0)], destination = (0, 2)

Predicted path: ____________________________________________________________________

Explanation: ____________________________________________________________________

**Scenario 4:** 4x4 grid, start = (1, 1), blocked = [(0, 1), (1, 0), (1, 2), (2, 1)], destination = (3, 3)

Predicted path: ____________________________________________________________________

Explanation: ____________________________________________________________________

**Scenario 5:** 4x4 grid, start = (0, 0), blocked = [(0, 1), (1, 0)], destination = (0, 0)

Predicted path: ____________________________________________________________________

Explanation: ____________________________________________________________________

---

## Part B: Compare Manhattan vs Dijkstra Paths

The Manhattan pathfinder moves in straight lines (all rows first, then all columns, or vice versa). Dijkstra finds the true shortest path around obstacles.

Fill in the table for a **4x4 grid**:

| Start | Dest | Blocked | Manhattan Path | Man. Length | Dijkstra Path | Dijk. Length | Winner |
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

## Part C: Swapping Pathfinders

Below is a program that uses the Manhattan pathfinder. Mark which lines would need to change to swap to Dijkstra.

```python
# Line 1:  from manhattan import Manhattan
# Line 2:
# Line 3:  blocked = [(1, 1), (2, 2)]
# Line 4:  pathfinder = Manhattan((0, 0))
# Line 5:  path = pathfinder.compute_path((3, 3))
# Line 6:  print("Path:", path)
# Line 7:  print("Steps:", len(path) - 1)
```

**Which lines change?** Circle the line numbers: 1  2  3  4  5  6  7

**Rewrite the lines that change:**

Line ___: ____________________________________________________________________

Line ___: ____________________________________________________________________

**Which lines stay exactly the same?** ____________________

**Why can we swap pathfinders without changing most of the code?**

____________________________________________________________________

____________________________________________________________________

**What do both pathfinders have in common?**

| Feature | Manhattan | Dijkstra |
|---|---|---|
| Has `compute_path()` method? | __________ | __________ |
| Takes destination as argument? | __________ | __________ |
| Returns a list of (row, col)? | __________ | __________ |
| Considers obstacles? | __________ | __________ |
| Finds shortest path around obstacles? | __________ | __________ |

---

## Part D: Edge Cases

**1. What happens when the destination is blocked?**

```python
pathfinder = Dijkstra((0, 0), [(2, 2)])
path = pathfinder.compute_path((2, 2))
```

What does `compute_path` return? __________

What message is printed? ____________________________________________________

**2. What happens when the start is blocked?**

Think about this: if `(0, 0)` is in the blocked list, what happens when we create the Dijkstra object?

```python
pathfinder = Dijkstra((0, 0), [(0, 0)])
```

Is `(0, 0)` in `pathfinder.graph`? __________

What happens when `compute_path` tries to set `distances[self.position] = 0`?

____________________________________________________________________

**3. What happens when there is no path?**

```python
# All neighbors of (0,0) are blocked, but destination is not blocked
pathfinder = Dijkstra((0, 0), [(0, 1), (1, 0)])
path = pathfinder.compute_path((3, 3))
```

What happens? ____________________________________________________________________

**4. What happens when start equals destination?**

```python
pathfinder = Dijkstra((0, 0), [])
path = pathfinder.compute_path((0, 0))
```

What does `compute_path` return? __________

Is this the correct result? __________

Why? ____________________________________________________________________

---

## Answer Key

### Part A:
1. `[(0,0), (0,1), (0,2), (0,3), (1,3), (2,3), (3,3)]` or equivalent shortest path, length = 6
2. `[(0,0), (0,1), (0,2), (1,2), (2,2)]` or `[(0,0), (1,0), (2,0), (2,1), (2,2)]`, length = 4
3. `[]` with "No path found!" — (0,0) has no unblocked neighbors, so no path exists to (0,2). Actually (0,0) is isolated but still in the graph. The algorithm will not reach (0,2) and return empty.
4. (1,1) is surrounded by blocked cells, so it cannot reach any neighbor. Path = [] with "No path found!"
5. `[(0,0)]` — Start and destination are the same. The algorithm immediately finds current == destination and returns a path of length 0.

### Part B:
1. When there are no obstacles in the Manhattan path, both give the same length (6 steps).
2. When obstacles block the Manhattan route but an alternative path exists.
3. No. Dijkstra always finds the true shortest path. Manhattan might match it but can never beat it.

### Part C:
- Lines that change: 1 and 4
- Line 1: `from dijkstra import Dijkstra`
- Line 4: `pathfinder = Dijkstra((0, 0), blocked)`
- Lines 3, 5, 6, 7 stay the same
- Both pathfinders have the same interface: `compute_path()` method that takes a destination and returns a list of (row, col) tuples.

| Feature | Manhattan | Dijkstra |
|---|---|---|
| Has compute_path()? | Yes | Yes |
| Takes destination? | Yes | Yes |
| Returns list of (row,col)? | Yes | Yes |
| Considers obstacles? | No | Yes |
| Finds shortest around obstacles? | No | Yes |

### Part D:
1. Returns `[]`, prints "Destination is blocked!"
2. (0,0) is not in the graph. `distances[self.position] = 0` will cause a KeyError because (0,0) is not a key in distances.
3. The algorithm runs but never reaches (3,3) from (0,0) because (0,0) has no neighbors. The path reconstruction produces a path not starting at (0,0), so it prints "No path found!" and returns [].
4. Returns `[(0,0)]` — a path containing just the start/destination. This is correct; you are already there.
