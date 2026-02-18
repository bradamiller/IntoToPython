# Lesson 5 Slide Outline: Implementing compute_path()

## Slide 1: Title & Learning Objectives
**Title:** Implementing compute_path()

**Learning Objectives:**
- Initialize the distances, visited, and previous data structures in code
- Implement the main Dijkstra loop: find minimum, update neighbors, mark visited
- Reconstruct the shortest path by tracing back through the previous dictionary
- Test compute_path with and without blocked nodes

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

**Today:** You'll turn your paper trace into Python — the `compute_path` method.

---

## Slide 3: Setting Up the Data Structures
**Inside compute_path, we first initialize our three data structures:**

```python
def compute_path(self, destination):
    distances = {}
    previous = {}
    visited = []

    # Set all nodes to a very large distance
    for node in self.graph:
        distances[node] = 999999

    # Start node is distance 0
    distances[self.start] = 0
    previous[self.start] = None
```

**Why 999999?** It represents "infinity" — we haven't found a path yet. Any real distance will be shorter.

**Why is start set to 0?** The distance from start to itself is zero steps.

**Why previous[start] = None?** The start node has no node before it.

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
for neighbor in self.graph[current]:
    if neighbor not in visited:
        new_distance = distances[current] + 1

        if new_distance < distances[neighbor]:
            distances[neighbor] = new_distance
            previous[neighbor] = current
```

**Line by line:**
- `self.graph[current]` gives us the list of neighbors from our graph dictionary
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
def compute_path(self, destination):
    distances = {}
    previous = {}
    visited = []

    for node in self.graph:
        distances[node] = 999999
    distances[self.start] = 0
    previous[self.start] = None

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
        for neighbor in self.graph[current]:
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

**The return value is a list of tuples** — exactly what Navigator expects!

Example: `[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]`

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

## Slide 9: Testing compute_path
**Test 1: No blocked nodes**
```python
d = Dijkstra((0, 0), [])
path = d.compute_path((3, 3))
print(path)
print("Steps:", len(path) - 1)  # Should be 6 (Manhattan distance)
```

**Test 2: With blocked nodes**
```python
d = Dijkstra((0, 0), [(1, 1), (2, 2)])
path = d.compute_path((3, 3))
print(path)
# Path should go around both blocked nodes
```

**Test 3: Compare with Manhattan**
```python
m = Manhattan((0, 0))
d = Dijkstra((0, 0), [])

m_path = m.compute_path((2, 2))
d_path = d.compute_path((2, 2))

print("Manhattan:", m_path)
print("Dijkstra: ", d_path)
print("Same length?", len(m_path) == len(d_path))  # Should be True
```

---

## Slide 10: Your Turn!
**Activity: Implement and Test compute_path**

1. Add the `compute_path` method to your Dijkstra class from Lesson 4
2. Run these tests and verify the output:
   ```python
   # Test with no obstacles
   d = Dijkstra((0, 0), [])
   print(d.compute_path((3, 3)))  # Should be 6 steps

   # Test with obstacles
   d = Dijkstra((0, 0), [(1, 0), (1, 1)])
   print(d.compute_path((3, 3)))  # Should route around row 1

   # Test short path
   d = Dijkstra((0, 0), [])
   print(d.compute_path((0, 1)))  # Should be [(0,0), (0,1)]
   ```
3. Try creating a situation where many nodes are blocked. Can Dijkstra still find a path?

**Checkpoints:**
- Does compute_path return a list of tuples starting with start and ending with destination?
- With no blocked nodes, is the path length equal to the Manhattan distance?
- With blocked nodes, does the path successfully go around them?
- What happens if you block all paths to the destination?

---

## Slide 11: Connection to Next Lesson
**What you did today:**
- Initialized distances, visited, and previous data structures
- Implemented the main Dijkstra loop with minimum-finding and neighbor updates
- Reconstructed the shortest path by tracing back through previous
- Tested compute_path with and without obstacles

**Next lesson (Lesson 6):**
- Test Dijkstra and Manhattan side by side
- Swap Dijkstra into your Module 4 robot program
- See both pathfinders work with the same Navigator class

**Key insight:** Dijkstra's compute_path returns the same format as Manhattan's compute_path — a list of tuples. This shared interface is the power of good class design.
