# Lesson 4 Worksheet: The Dijkstra Class

**Name:** ________________________
**Date:** ________________________

---

## Part A: Class Design

We are going to build a `Dijkstra` class that knows how to find shortest paths on our grid.

**1. What information does the Dijkstra pathfinder need to know when it is created?**

List at least 3 things:

- ____________________________________________________________________
- ____________________________________________________________________
- ____________________________________________________________________

**2. Fill in the blanks for the `__init__` method:**

```python
class Dijkstra:
    def __init__(self, start, blocked):
        self.position = __________    # Where the robot is now
        self.blocked = __________     # List of blocked cells
        self.graph = self.__________  # Build the graph
```

**3. What methods should the Dijkstra class have?**

| Method Name | What It Does |
|---|---|
| `__init__` | Initializes the pathfinder with start position and blocked list |
| `__________` | Creates the graph dictionary from the grid |
| `__________` | Finds the shortest path from current position to a destination |

**4. Why do we build the graph inside the class instead of passing it in?**

____________________________________________________________________

____________________________________________________________________

---

## Part B: build_graph() Exercises

The `build_graph()` method creates a dictionary where each key is a node `(row, col)` and each value is a list of that node's neighbors.

**1. For a 2x2 grid with NO blocked cells, what does `build_graph(2, 2)` return?**

```python
graph = {
    (0, 0): [__________________________________________],
    (0, 1): [__________________________________________],
    (1, 0): [__________________________________________],
    (1, 1): [__________________________________________],
}
```

**2. For a 2x2 grid with (0, 1) blocked, what does `build_graph(2, 2)` return?**

```python
graph = {
    (0, 0): [__________________________________________],
    (1, 0): [__________________________________________],
    (1, 1): [__________________________________________],
}
```

**Why is (0, 1) not a key?** __________________________________________

**Why is (0, 1) not in any neighbor list?** __________________________________________

**3. For a 3x3 grid with (1, 0) and (1, 2) blocked, list the graph entries:**

```python
graph = {
    (0, 0): [__________________________________________],
    (0, 1): [__________________________________________],
    (0, 2): [__________________________________________],
    (1, 1): [__________________________________________],
    (2, 0): [__________________________________________],
    (2, 1): [__________________________________________],
    (2, 2): [__________________________________________],
}
```

**4. How many nodes are in the graph from question 3?** __________

**5. Which node in question 3 has the fewest neighbors?** __________

---

## Part C: Testing the Class — Predict Output

Given this code:

```python
class Dijkstra:
    def __init__(self, start, blocked):
        self.position = start
        self.blocked = blocked
        self.graph = self.build_graph(4, 4)

    def build_graph(self, rows, cols):
        graph = {}
        for r in range(rows):
            for c in range(cols):
                if (r, c) in self.blocked:
                    continue
                neighbors = []
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in self.blocked:
                        neighbors.append((nr, nc))
                graph[(r, c)] = neighbors
        return graph

    def compute_path(self, destination):
        return []  # Placeholder for now
```

**Program 1:**

```python
pathfinder = Dijkstra((0, 0), [])
print(len(pathfinder.graph))
```

**Predicted output:** __________

**Why?** ____________________________________________________________________

**Program 2:**

```python
pathfinder = Dijkstra((0, 0), [(1, 1)])
print((1, 1) in pathfinder.graph)
print(pathfinder.graph[(0, 1)])
```

**Predicted output:**

```
__________
__________
```

**Program 3:**

```python
pathfinder = Dijkstra((0, 0), [(0, 1), (1, 0)])
print(pathfinder.graph[(0, 0)])
```

**Predicted output:** __________

**Why?** ____________________________________________________________________

**Program 4:**

```python
pathfinder = Dijkstra((2, 2), [(1, 1), (1, 2), (2, 1)])
print(pathfinder.position)
print(len(pathfinder.graph[(2, 2)]))
```

**Predicted output:**

```
__________
__________
```

---

## Answer Key

### Part A:
1. Start position, list of blocked cells, grid size (rows and columns)
2. `self.position = start`, `self.blocked = blocked`, `self.graph = self.build_graph(4, 4)`
3. `build_graph` — Creates the graph dictionary from the grid; `compute_path` — Finds shortest path to destination
4. The graph depends on which cells are blocked, which the class knows about. Building it inside keeps everything together and ensures the graph is always consistent with the blocked list.

### Part B:
1. `(0,0): [(1,0),(0,1)]`, `(0,1): [(1,1),(0,0)]`, `(1,0): [(0,0),(1,1)]`, `(1,1): [(0,1),(1,0)]`
2. `(0,0): [(1,0)]`, `(1,0): [(0,0),(1,1)]`, `(1,1): [(1,0)]` — (0,1) is not a key because blocked nodes are skipped. (0,1) is not in neighbor lists because the code checks if the neighbor is blocked.
3. `(0,0): [(0,1)]`, `(0,1): [(0,0),(0,2)]`, `(0,2): [(0,1)]`, `(1,1): [(0,1),(2,1)]`, `(2,0): [(2,1)]`, `(2,1): [(1,1),(2,0),(2,2)]`, `(2,2): [(2,1)]`
4. 7 nodes
5. (0,0), (0,2), (2,0), or (2,2) — each has only 1 neighbor

### Part C:
- Program 1: `16` — A 4x4 grid with no blocked cells has 16 nodes.
- Program 2: `False` then `[(0, 0), (0, 2)]` — (1,1) is blocked so not in graph. (0,1)'s neighbors skip (1,1).
- Program 3: `[]` — Both neighbors of (0,0) are blocked, so it has an empty neighbor list.
- Program 4: `(2, 2)` then `1` — Three of (2,2)'s neighbors are blocked. Only (2,3) remains, so length is 1.
