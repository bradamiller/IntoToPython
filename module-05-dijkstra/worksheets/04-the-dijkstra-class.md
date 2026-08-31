# Lesson 4 Worksheet: The Dijkstra Functions

**Name:** ________________________
**Date:** ________________________

---

## Part A: Function Design

We are going to build `build_dijkstra_graph()` and `compute_dijkstra_path()` -- two functions that work together to find shortest paths on our grid.

**1. What information does `build_dijkstra_graph()` need to know to build the graph?**

List at least 3 things:

- ____________________________________________________________________
- ____________________________________________________________________
- ____________________________________________________________________

**2. Fill in the blanks for `build_dijkstra_graph()`'s signature and first line:**

```python
def build_dijkstra_graph(__________, __________, __________):
    graph = __________
```

**3. What do the two Dijkstra functions do?**

| Function Name | What It Does |
|---|---|
| `build_dijkstra_graph(rows, cols, blocked)` | __________________________________ |
| `compute_dijkstra_path(position, destination, graph)` | __________________________________ |

**4. Why does `compute_dijkstra_path()` take `graph` as a parameter instead of building it itself?**

____________________________________________________________________

____________________________________________________________________

---

## Part B: build_dijkstra_graph() Exercises

`build_dijkstra_graph()` creates a dictionary where each key is a node `(row, col)` and each value is a list of that node's neighbors.

**1. For a 2x2 grid with NO blocked cells, what does `build_dijkstra_graph(2, 2, [])` return?**

```python
graph = {
    (0, 0): [__________________________________________],
    (0, 1): [__________________________________________],
    (1, 0): [__________________________________________],
    (1, 1): [__________________________________________],
}
```

**2. For a 2x2 grid with (0, 1) blocked, what does `build_dijkstra_graph(2, 2, [(0, 1)])` return?**

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

## Part C: Testing the Functions — Predict Output

Given this code:

```python
def build_dijkstra_graph(rows, cols, blocked):
    graph = {}
    for r in range(rows):
        for c in range(cols):
            if (r, c) in blocked:
                continue
            neighbors = []
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in blocked:
                    neighbors.append((nr, nc))
            graph[(r, c)] = neighbors
    return graph

def compute_dijkstra_path(position, destination, graph):
    return []  # Placeholder for now
```

**Program 1:**

```python
graph = build_dijkstra_graph(4, 4, [])
print(len(graph))
```

**Predicted output:** __________

**Why?** ____________________________________________________________________

**Program 2:**

```python
graph = build_dijkstra_graph(4, 4, [(1, 1)])
print((1, 1) in graph)
print(graph[(0, 1)])
```

**Predicted output:**

```
__________
__________
```

**Program 3:**

```python
graph = build_dijkstra_graph(4, 4, [(0, 1), (1, 0)])
print(graph[(0, 0)])
```

**Predicted output:** __________

**Why?** ____________________________________________________________________

**Program 4:**

```python
graph = build_dijkstra_graph(4, 4, [(1, 1), (1, 2), (2, 1)])
print(len(graph[(2, 2)]))
```

**Predicted output:** __________

---

## Answer Key

### Part A:
1. Grid size (rows and columns), list of blocked cells
2. `def build_dijkstra_graph(rows, cols, blocked):` / `graph = {}`
3. `build_dijkstra_graph` — Creates the graph dictionary from the grid; `compute_dijkstra_path` — Finds shortest path to destination
4. Building it once and passing it in avoids rebuilding it every single call. The caller only needs to rebuild the graph when the blocked list actually changes.

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
- Program 4: `1` — Three of (2,2)'s neighbors are blocked. Only (2,3) remains, so length is 1.

---

## Part D (Optional Extension): Wrap It in a Class

*Skip this section if your course doesn't cover classes.*

**1. Fill in the blanks:**

```python
class Dijkstra:
    def __init__(self, start, blocked):
        self.position = __________    # Where the robot is now
        self.blocked = __________     # List of blocked cells
        self.graph = self.__________  # Build the graph
```

**2. Which functions-version parameter disappears when you switch to the class version, and why?**

____________________________________________________________________
