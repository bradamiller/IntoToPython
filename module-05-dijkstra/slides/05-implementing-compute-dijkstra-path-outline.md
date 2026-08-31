# Lesson 5 Slide Outline: Implementing compute_dijkstra_path()

## Slide 1: Title & Learning Objectives
**Title:** Implementing compute_dijkstra_path()

**Learning Objectives:**
- Initialize the distances, visited, and previous data structures in code
- Implement the main Dijkstra loop: find minimum, update neighbors, mark visited
- Reconstruct the shortest path by tracing back through the previous dictionary
- Test `compute_dijkstra_path` with and without blocked nodes

**Agenda:**
- Review: the three data structures (5 min)
- Initializing data structures in code (5 min)
- The main loop (15 min)
- Path reconstruction (10 min)
- Tracing through an example (10 min)
- Practice exercise (10 min)

---

## Slide 2: Hook — Teaching the Computer Your Paper Trace
**Remember Lesson 3?** You traced Dijkstra's algorithm by hand:
- Picked the unvisited node with the smallest distance
- Updated its neighbors' distances
- Marked it visited
- Traced back through `previous` to get the path

**Question:** "Can you describe those steps precisely enough that someone who has never seen the algorithm could follow them?"

If you can, you can write the code. **Programming is writing precise instructions.**

**Today:** You'll turn your paper trace into Python — filling in the `compute_dijkstra_path` placeholder from Lesson 4.

---

## Slide 3: Setting Up the Data Structures
**Inside `compute_dijkstra_path`, we first initialize our three data structures:**

```python
def compute_dijkstra_path(position, destination, graph):
    distances = {}
    previous = {}
    visited = []

    # Set all nodes to a very large distance
    for node in graph:
        distances[node] = 999999

    # Start node is distance 0
    distances[position] = 0
    previous[position] = None
```

**Why 999999?** It represents "infinity" — we haven't found a path yet. Any real distance will be shorter.

**Why is `position` set to 0?** The distance from position to itself is zero steps.

**Why `previous[position] = None`?** The start node has no node before it.

---

## Slide 4: Finding the Minimum-Distance Unvisited Node
**This is the trickiest part. We need to scan all nodes and find the unvisited one with the smallest distance.**

```python
# Find unvisited node with smallest distance
current = None
current_distance = 999999

for node in distances:
    if node not in visited:
        if distances[node] < current_distance:
            current = node
            current_distance = distances[node]
```

**How this works:**
1. Start with no candidate (`current = None`) and a huge distance
2. Check every node in the distances dictionary
3. Skip nodes already in the visited list
4. If this node's distance is smaller than our best so far, it becomes the new best
5. After the loop, `current` holds the closest unvisited node

**This is a simple linear scan** — not the fastest approach, but easy to understand and correct.

---

## Slide 5: Updating Neighbors
**Once we have the current node, we update all its unvisited neighbors:**

```python
for neighbor in graph[current]:
    if neighbor not in visited:
        new_distance = distances[current] + 1

        if new_distance < distances[neighbor]:
            distances[neighbor] = new_distance
            previous[neighbor] = current
```

**Line by line:**
- `graph[current]` gives us the list of neighbors from our graph dictionary
- Skip neighbors already visited — we're done with those
- `new_distance` = distance to current + 1 (one step between adjacent nodes)
- Only update if this new path is **shorter** than what we had before
- Record that we reached this neighbor **from** the current node

**After updating neighbors, mark current as visited:**
```python
visited.append(current)
```

---

## Slide 6: The Complete Main Loop
**Wrap the find-minimum and update-neighbors steps in a loop:**

```python
def compute_dijkstra_path(position, destination, graph):
    distances = {}
    previous = {}
    visited = []

    for node in graph:
        distances[node] = 999999
    distances[position] = 0
    previous[position] = None

    while destination not in visited:
        # Find unvisited node with smallest distance
        current = None
        current_distance = 999999
        for node in distances:
            if node not in visited:
                if distances[node] < current_distance:
                    current = node
                    current_distance = distances[node]

        # Update neighbors
        for neighbor in graph[current]:
            if neighbor not in visited:
                new_distance = distances[current] + 1
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current

        visited.append(current)
```

**The loop stops** when the destination has been visited — we've found the shortest path!

---

## Slide 7: Reconstructing the Path
**The `previous` dictionary tells us how to trace from destination back to start:**

```python
    # Reconstruct path
    path = []
    current = destination
    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()
    return path
```

**How this works:**
1. Start at the destination
2. Look up `previous[current]` to find where we came from
3. Add each node to the path list
4. Stop when `current` is `None` — that's the start node
5. Reverse the list because we built it backwards (destination to start)

**The return value is a list of tuples** — including `position` itself, unlike `compute_manhattan_path`.

Example: `[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]`

**Note this difference for Lesson 6:** Dijkstra's raw path starts with `position`; Manhattan's doesn't.

---

## Slide 8: Tracing with an Example
**3x3 grid, (1,1) blocked, find path from (0,0) to (2,2):**

| Step | Current | Distance | Neighbors Updated | Visited |
|---|---|---|---|---|
| 1 | (0,0) | 0 | (0,1)=1, (1,0)=1 | [(0,0)] |
| 2 | (0,1) | 1 | (0,2)=2 | [(0,0),(0,1)] |
| 3 | (1,0) | 1 | (2,0)=2 | [(0,0),(0,1),(1,0)] |
| 4 | (0,2) | 2 | (1,2)=3 | [...,(0,2)] |
| 5 | (2,0) | 2 | (2,1)=3 | [...,(2,0)] |
| 6 | (1,2) | 3 | (2,2)=4 | [...,(1,2)] |
| 7 | (2,1) | 3 | (none new) | [...,(2,1)] |
| 8 | (2,2) | 4 | — | [...,(2,2)] DONE |

**Reconstruct:** (2,2) <- (1,2) <- (0,2) <- (0,1) <- (0,0)

**Reverse:** `[(0,0), (0,1), (0,2), (1,2), (2,2)]`

**This matches our paper trace from Lesson 3!**

---

## Slide 9: Testing compute_dijkstra_path
**Test 1: No blocked nodes**
```python
graph = build_dijkstra_graph(4, 4, [])
path = compute_dijkstra_path((0, 0), (3, 3), graph)
print(path)
print("Steps:", len(path) - 1)  # Should be 6 (Manhattan distance)
```

**Test 2: With blocked nodes**
```python
graph = build_dijkstra_graph(4, 4, [(1, 1), (2, 2)])
path = compute_dijkstra_path((0, 0), (3, 3), graph)
print(path)
# Path should go around both blocked nodes
```

**Test 3: Compare with Manhattan**
```python
graph = build_dijkstra_graph(4, 4, [])

m_path = compute_manhattan_path((0, 0), (2, 2))
d_path = compute_dijkstra_path((0, 0), (2, 2), graph)

print("Manhattan:", m_path)
print("Dijkstra: ", d_path)
print("Same length?", len(m_path) == len(d_path) - 1)  # Should be True
```

---

## Slide 10: Your Turn!
**Activity: Implement and Test compute_dijkstra_path**

1. Fill in the `compute_dijkstra_path` placeholder from Lesson 4
2. Run these tests and verify the output:
   ```python
   # Test with no obstacles
   graph = build_dijkstra_graph(4, 4, [])
   print(compute_dijkstra_path((0, 0), (3, 3), graph))  # Should be 6 steps

   # Test with obstacles
   graph = build_dijkstra_graph(4, 4, [(1, 0), (1, 1)])
   print(compute_dijkstra_path((0, 0), (3, 3), graph))  # Should route around row 1

   # Test short path
   graph = build_dijkstra_graph(4, 4, [])
   print(compute_dijkstra_path((0, 0), (0, 1), graph))  # Should be [(0,0), (0,1)]
   ```
3. Try creating a situation where many nodes are blocked. Can Dijkstra still find a path?

**Checkpoints:**
- Does `compute_dijkstra_path` return a list of tuples starting with position and ending with destination?
- With no blocked nodes, is the path length equal to the Manhattan distance?
- With blocked nodes, does the path successfully go around them?
- What happens if you block all paths to the destination?

---

## Slide 11: What's Next
**Today:** You initialized distances/visited/previous, implemented the main loop, reconstructed the path, and tested `compute_dijkstra_path` with and without obstacles.

**Next lesson (Lesson 6):**
- Test Dijkstra and Manhattan side by side
- Confront the shape mismatch: Dijkstra's path includes `position`, Manhattan's doesn't
- Build a `compute_path(algorithm, ...)` dispatch function and swap it into the Module 4 robot program

**Key insight:** `compute_dijkstra_path` returns almost the same shape as `compute_manhattan_path` — a list of tuples. Almost is the interesting part; next lesson deals with the difference.

**Optional Extension:** Courses that also cover classes can see this same algorithm completed inside the `Dijkstra` class from the Lesson 4 Optional Extension -- see the separate "The Completed Dijkstra Class" deck.
