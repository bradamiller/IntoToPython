# Lesson 4 Slide Outline: The Dijkstra Functions

## Slide 1: Title & Learning Objectives
**Title:** The Dijkstra Functions

**Learning Objectives:**
- Design `build_dijkstra_graph(rows, cols, blocked)` and the `compute_dijkstra_path(position, destination, graph)` signature
- Build a graph dictionary from a 4x4 grid, excluding blocked nodes
- Test graph construction by printing and inspecting the dictionary
- Understand how `compute_dijkstra_path` will share a return shape with `compute_manhattan_path`

**Agenda:**
- Function design overview (5 min)
- Building the graph: bounds checks and blocked nodes (15 min)
- Testing graph construction (10 min)
- Practice exercise (15 min)

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

**Today:** We'll write a function that **builds the graph automatically** — and handles blocked nodes for us.

---

## Slide 3: Two Functions, Built in Stages
**Dijkstra needs two capabilities, so we write two functions:**
1. **`build_dijkstra_graph(rows, cols, blocked)`** — build the graph, skipping blocked intersections
2. **`compute_dijkstra_path(position, destination, graph)`** — compute a path from position to destination (next lesson!)

```python
def build_dijkstra_graph(rows, cols, blocked):
    # Create and return the graph dictionary

def compute_dijkstra_path(position, destination, graph):
    # Run Dijkstra's algorithm (next lesson!)
    # For now: a placeholder that returns []
```

**Key design decision:** `compute_dijkstra_path` will return a list of tuples — the **same shape** as `compute_manhattan_path`. That means `drive_path()` can use either one!

---

## Slide 4: build_dijkstra_graph — The Strategy
**Goal:** Create a dictionary where each unblocked node maps to its list of unblocked neighbors.

**Strategy:**
1. Loop through every row and column in the grid
2. Skip any position that is in the `blocked` list
3. For the current position, check all 4 directions (up, down, left, right)
4. If a neighbor exists (in bounds) and is not blocked, add it to the neighbor list
5. Store the position and its neighbors in the dictionary

**Why check bounds one direction at a time?** No `directions` list needed -- four explicit `if` checks read clearly for students who haven't seen loops-over-tuples yet.

---

## Slide 5: build_dijkstra_graph — The Code
```python
def build_dijkstra_graph(rows, cols, blocked):
    graph = {}

    for row in range(rows):
        for col in range(cols):
            # Skip blocked nodes
            if (row, col) in blocked:
                continue

            # Build neighbor list, excluding blocked neighbors
            neighbors = []
            if row > 0 and (row - 1, col) not in blocked:
                neighbors.append((row - 1, col))
            if row < rows - 1 and (row + 1, col) not in blocked:
                neighbors.append((row + 1, col))
            if col > 0 and (row, col - 1) not in blocked:
                neighbors.append((row, col - 1))
            if col < cols - 1 and (row, col + 1) not in blocked:
                neighbors.append((row, col + 1))

            graph[(row, col)] = neighbors

    return graph
```

**`continue` skips** to the next iteration — it means "this one doesn't qualify, move on."

---

## Slide 6: Understanding the Bounds Checks
**Why do we need bounds checking?**

Consider node (0, 0) checking one row up:
```
row - 1 = -1
```
Row -1 doesn't exist! The check `row > 0` protects against it.

**All the checks explained:**
| Check | Why |
|---|---|
| `row > 0` | Is there a row above? |
| `row < rows - 1` | Is there a row below? |
| `col > 0` | Is there a column to the left? |
| `col < cols - 1` | Is there a column to the right? |
| `... not in blocked` | Is that neighbor blocked? |

**Edge and corner nodes naturally get fewer neighbors** because some directions fail the bounds check.

---

## Slide 7: Testing Graph Construction
**Always test your code! Print the graph and verify it makes sense.**

```python
graph = build_dijkstra_graph(4, 4, [(1, 1)])
for node in graph:
    print(node, "->", graph[node])
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

## Slide 8: Graph as a Picture
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

**Check your dictionary:** `len(graph)` should equal 15.

**Check a specific node:**
```python
print(graph[(2,1)])
# (1, 1) is blocked, so: [(2, 0), (3, 1), (2, 2)]
```

This is a great way to catch bugs early — compare the picture to the dictionary.

---

## Slide 9: Your Turn!
**Activity: Build the Dijkstra Functions (Part 1)**

1. Create a new file called `dijkstra.py`
2. Implement `build_dijkstra_graph(rows, cols, blocked)`
3. Add a placeholder `compute_dijkstra_path(position, destination, graph)` that just prints its arguments and returns `[]`
4. Test with no blocked nodes:
   ```python
   graph = build_dijkstra_graph(4, 4, [])
   print(len(graph))       # Should be 16
   print(graph[(0, 0)])    # Should have 2 neighbors
   print(graph[(1, 1)])    # Should have 4 neighbors
   ```
5. Test with blocked nodes:
   ```python
   graph = build_dijkstra_graph(4, 4, [(1, 1), (2, 2)])
   print(len(graph))       # Should be 14
   # Verify (1,1) and (2,2) are not keys
   # Verify they don't appear in any neighbor lists
   ```

**Checkpoints:**
- Does your graph have the right number of nodes?
- Do corner nodes have 2 neighbors, edge nodes 3, and interior nodes 4?
- Are blocked nodes excluded completely — as keys AND as neighbors?

---

## Slide 10: What's Next
**Today:** You built `build_dijkstra_graph()` and the `compute_dijkstra_path()` signature — the graph builder is complete, the pathfinder is a placeholder.

**Next lesson (Lesson 5):**
- Implement `compute_dijkstra_path(position, destination, graph)` — the heart of Dijkstra's algorithm
- Use the distances, previous, and visited data structures from Lesson 3
- Return a list of tuples — the path from start to destination

**Key insight:** Today you built the map. Next lesson, you'll navigate it.

**Optional Extension:** Courses that also cover classes can package these same two functions inside a `Dijkstra` class -- see the separate "The Dijkstra Class" deck.
