# Lesson 4 Slide Outline: The Dijkstra Class

## Slide 1: Title & Learning Objectives
**Title:** The Dijkstra Class

**Learning Objectives:**
- Design the Dijkstra class with __init__ and build_graph methods
- Build a graph dictionary from a 4x4 grid, excluding blocked nodes
- Test graph construction by printing and inspecting the dictionary
- Understand how the Dijkstra class will share an interface with Manhattan

**Agenda:**
- Class design overview (5 min)
- The __init__ method (10 min)
- Building the graph: nested loops and neighbor checks (15 min)
- Testing graph construction (10 min)
- Practice exercise (10 min)

---

## Slide 2: Hook — From Paper to Python
**Last lesson** you traced Dijkstra's algorithm by hand on paper. You used a graph dictionary like this:

```python
graph = {
    (0,0): [(0,1), (1,0)],
    (0,1): [(0,0), (0,2)],
    ...
}
```

**Question:** "Who wants to write that dictionary by hand for a 4x4 grid with 16 nodes?"

**Nobody!** That's 16 entries, each with up to 4 neighbors. Tedious and error-prone.

**Today:** We'll write a class that **builds the graph automatically** — and handles blocked nodes for us.

---

## Slide 3: Dijkstra Class Design Overview
**The Dijkstra class needs two main capabilities:**
1. **Build a graph** from the grid, skipping blocked intersections
2. **Compute a path** from start to any destination (next lesson!)

**Class structure:**
```python
class Dijkstra:
    def __init__(self, start, blocked):
        # Store start, blocked list, and grid size
        # Build the graph automatically

    def build_graph(self):
        # Create the graph dictionary

    def compute_path(self, destination):
        # Run Dijkstra's algorithm (next lesson!)
```

**Key design decision:** `compute_path` returns a list of tuples — the **same interface** as Manhattan's `compute_path`. This means Navigator can use either one!

---

## Slide 4: The __init__ Method
**What __init__ needs to do:**
1. Store the starting position
2. Store the list of blocked intersections
3. Define the grid size (4 rows, 4 columns)
4. Call build_graph to create the graph dictionary

```python
class Dijkstra:
    def __init__(self, start, blocked):
        self.start = start
        self.blocked = blocked
        self.rows = 4
        self.cols = 4
        self.graph = self.build_graph()
```

**Usage:**
```python
d = Dijkstra((0, 0), [(1, 1), (2, 2)])
```

**Notice:** `blocked` is a list of tuples — the same format we use everywhere for grid positions.

---

## Slide 5: build_graph — The Strategy
**Goal:** Create a dictionary where each unblocked node maps to its list of unblocked neighbors.

**Strategy:**
1. Loop through every row and column in the grid
2. Skip any position that is in the blocked list
3. For the current position, check all 4 directions (up, down, left, right)
4. If a neighbor exists and is not blocked, add it to the neighbor list
5. Store the position and its neighbors in the dictionary

**The four directions:**
```python
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#             up       down     left      right
```

**Each direction is a tuple** — we add it to the current position to get the neighbor's coordinates.

---

## Slide 6: build_graph — The Code
```python
def build_graph(self):
    graph = {}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for row in range(self.rows):
        for col in range(self.cols):
            position = (row, col)

            if position in self.blocked:
                continue

            neighbors = []
            for d in directions:
                neighbor = (row + d[0], col + d[1])

                if neighbor[0] < 0 or neighbor[0] >= self.rows:
                    continue
                if neighbor[1] < 0 or neighbor[1] >= self.cols:
                    continue
                if neighbor in self.blocked:
                    continue

                neighbors.append(neighbor)

            graph[position] = neighbors

    return graph
```

**`continue` skips** to the next iteration — it means "this one doesn't qualify, move on."

---

## Slide 7: Understanding the Bounds Checks
**Why do we need bounds checking?**

Consider node (0, 0) checking the "up" direction (-1, 0):
```
neighbor = (0 + (-1), 0 + 0) = (-1, 0)
```
Row -1 doesn't exist! We must skip it.

**All the checks explained:**
| Check | Why |
|---|---|
| `neighbor[0] < 0` | Row is above the grid |
| `neighbor[0] >= self.rows` | Row is below the grid |
| `neighbor[1] < 0` | Column is left of the grid |
| `neighbor[1] >= self.cols` | Column is right of the grid |
| `neighbor in self.blocked` | Intersection is blocked |

**Edge and corner nodes naturally get fewer neighbors** because some directions fail the bounds check.

---

## Slide 8: Testing Graph Construction
**Always test your code! Print the graph and verify it makes sense.**

```python
d = Dijkstra((0, 0), [(1, 1)])
for node in d.graph:
    print(node, "->", d.graph[node])
```

**Expected output (partial):**
```
(0, 0) -> [(1, 0), (0, 1)]
(0, 1) -> [(0, 0), (0, 2)]
(1, 0) -> [(0, 0), (2, 0)]
(1, 2) -> [(0, 2), (2, 2)]
...
```

**Verify these things:**
- (1, 1) does NOT appear as a key (it's blocked)
- (1, 1) does NOT appear in any neighbor list
- (0, 0) has exactly 2 neighbors (corner node)
- (0, 1) has exactly 2 neighbors — it lost (1, 1) as a neighbor!

---

## Slide 9: Graph as a Picture
**Visualizing the graph with (1,1) blocked on a 4x4 grid:**

```
(0,0) --- (0,1) --- (0,2) --- (0,3)
  |         |         |         |
(1,0)               (1,2) --- (1,3)
  |         |         |         |
(2,0) --- (2,1) --- (2,2) --- (2,3)
  |         |         |         |
(3,0) --- (3,1) --- (3,2) --- (3,3)
```

**Count the nodes:** 15 (16 minus 1 blocked)

**Check your dictionary:** `len(d.graph)` should equal 15.

**Check a specific node:**
```python
print(d.graph[(2,1)])
# Should be: [(1, 1) is blocked!] → [(2, 0), (3, 1), (2, 2)]
```

This is a great way to catch bugs early — compare the picture to the dictionary.

---

## Slide 10: Your Turn!
**Activity: Implement the Dijkstra Class (Part 1)**

1. Create a new file called `dijkstra.py`
2. Implement the `Dijkstra` class with `__init__` and `build_graph`
3. Test with no blocked nodes:
   ```python
   d = Dijkstra((0, 0), [])
   print(len(d.graph))  # Should be 16
   print(d.graph[(0, 0)])  # Should have 2 neighbors
   print(d.graph[(1, 1)])  # Should have 4 neighbors
   ```
4. Test with blocked nodes:
   ```python
   d = Dijkstra((0, 0), [(1, 1), (2, 2)])
   print(len(d.graph))  # Should be 14
   # Verify (1,1) and (2,2) are not keys
   # Verify they don't appear in any neighbor lists
   ```

**Checkpoints:**
- Does your graph have the right number of nodes?
- Do corner nodes have 2 neighbors, edge nodes 3, and interior nodes 4?
- Are blocked nodes excluded completely — as keys AND as neighbors?

---

## Slide 11: Connection to Next Lesson
**What you did today:**
- Designed the Dijkstra class with __init__ and build_graph
- Used nested loops to build a graph dictionary from the grid
- Checked bounds and blocked nodes when finding neighbors
- Tested graph construction by printing and inspecting

**Next lesson (Lesson 5):**
- Implement `compute_path(destination)` — the heart of Dijkstra's algorithm
- Use the distances, previous, and visited data structures from Lesson 3
- Return a list of tuples — the path from start to destination

**Key insight:** Today you built the map. Next lesson, you'll navigate it.
