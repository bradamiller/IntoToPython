# Lesson 5: Implementing compute_dijkstra_path()

## Overview
Students implement the full `compute_dijkstra_path` function, translating the hand-traced algorithm from Lesson 3 into working Python code. The function initializes three data structures -- a `distances` dictionary (all nodes start at 999999 except the start node at 0), a `previous` dictionary (tracks the path), and a `visited` list (nodes already finalized). The main loop repeatedly finds the unvisited node with the smallest distance, updates the distances of its unvisited neighbors, records each neighbor's predecessor, and marks the current node as visited. When the destination enters the visited list, the loop stops and the function reconstructs the path by tracing backward through the `previous` dictionary and reversing the result. Students verify their implementation by comparing output against the hand traces from Lesson 3.

This is the culmination of the first five lessons of Module 5. Students have built up to this moment through understanding graphs (Lesson 1), learning dictionaries (Lesson 2), hand-tracing the algorithm (Lesson 3), and designing the function structure (Lesson 4). Now they combine all of that knowledge into a single working function. The implementation uses only concepts students already know: dictionaries, lists, tuples, for loops, while loops, if statements, and the `in` keyword. There are no new Python concepts -- only the challenge of putting familiar pieces together into a precise algorithm.

This lesson stands on its own -- classes are never required. An **optional extension** at the end of this file shows the completed algorithm inside a `Dijkstra` class, for courses that also cover OOP.

## Learning Objectives
By the end of this lesson, students will be able to:
- Initialize the distances, previous, and visited data structures in Python code
- Implement the "find minimum unvisited node" step using a for loop
- Implement the "update neighbors" step using the graph dictionary
- Write the main Dijkstra loop with the correct termination condition
- Reconstruct the shortest path by tracing backward through the previous dictionary
- Reverse the reconstructed path to produce the correct start-to-destination order
- Test `compute_dijkstra_path` with no blocked nodes and verify it matches Manhattan's path length
- Test `compute_dijkstra_path` with blocked nodes and verify it matches hand-traced results from Lesson 3

## Key Concepts
- **Infinity representation**: Using a very large number (999999) to represent "distance unknown" in the distances dictionary. Any real path distance will be less than this value, so the first path found to a node will always be an improvement over the initial value.
- **Find minimum unvisited**: A linear scan through all nodes in the distances dictionary, skipping visited nodes, to find the one with the smallest distance. This is the core decision step of the algorithm -- always visit the closest unvisited node next.
- **Neighbor update**: For each unvisited neighbor of the current node, calculate the new distance (current distance + 1). If this new distance is less than the neighbor's current distance, update both the distance and the previous node. This is how the algorithm discovers shorter paths.
- **Termination condition**: The main loop runs `while destination not in visited`. Once the destination is visited, its shortest distance is finalized and the path can be reconstructed. If the destination is unreachable, the loop must also handle this edge case.
- **Path reconstruction**: Building the path by starting at the destination, following `previous` pointers back to the start, collecting each node into a list, and then reversing the list. Unlike `compute_manhattan_path`, this reconstruction naturally includes the starting position in the returned path (since it's the last node appended before the loop stops) -- keep this in mind when comparing step counts between the two algorithms.

## Materials Required
- Computers with Python installed (or XRP MicroPython environment)
- Dijkstra functions file from Lesson 4 (with `build_dijkstra_graph` and the `compute_dijkstra_path` placeholder)
- Hand-traced examples from Lesson 3 (for verifying code output)
- `compute_manhattan_path` file from Module 4 (for comparison testing)
- Whiteboard or projector for code walkthrough

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 8 min
**For 3-hour sessions:** 10-12 min

1. **Hook: Teaching the Computer Your Paper Trace**
   - "In Lesson 3, you traced Dijkstra's algorithm by hand. You picked the unvisited node with the smallest distance, updated its neighbors, marked it visited, and traced back through `previous` to get the path."
   - Ask: "Can you describe those steps precisely enough that someone who has never seen the algorithm could follow them?"
   - "If you can, you can write the code. Programming is writing precise instructions."
   - "Today you'll turn your paper trace into Python -- the `compute_dijkstra_path` function."

2. **Review: Where We Left Off**
   - Open the Dijkstra functions from Lesson 4:
     ```python
     def build_dijkstra_graph(rows, cols, blocked):
         # ... (implemented in Lesson 4)

     def compute_dijkstra_path(position, destination, graph):
         # TODO: Implement Dijkstra's algorithm
         return []
     ```
   - "`build_dijkstra_graph` is done. The graph is ready. Now we need to fill in `compute_dijkstra_path`."

3. **Connecting to the Paper Trace**
   - Show the Lesson 3 tracing table side by side with the code we'll write:
     - Paper: "Set start distance to 0" maps to `distances[position] = 0`
     - Paper: "Find smallest unvisited" maps to a for loop scanning distances
     - Paper: "Update neighbors" maps to a for loop over `graph[current]`
     - Paper: "Mark visited" maps to `visited.append(current)`
     - Paper: "Trace backward" maps to a while loop following `previous`
   - "Every line of code corresponds to a step you already know."

### Guided Practice (15 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

1. **Step 1: Setting Up the Data Structures**
   - Write the beginning of `compute_dijkstra_path`:
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
   - Explain each line:
     - `distances = {}` -- empty dictionary, then filled with 999999 for every node in the graph
     - `distances[position] = 0` -- the start node is 0 steps from itself
     - `previous[position] = None` -- nothing comes before the start
     - "Why 999999? It represents infinity. We haven't found a path yet, so the distance is 'as far as possible.' Any real distance will be less than this."

2. **Step 2: Finding the Minimum-Distance Unvisited Node**
   - "This is the trickiest part. We need to scan all nodes and find the unvisited one with the smallest distance."
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
   - Walk through the logic:
     - Start with no candidate and a huge distance
     - Check every node in the distances dictionary
     - Skip nodes already in the visited list
     - If this node's distance is smaller than our best so far, it becomes the new best
     - After the loop, `current` holds the closest unvisited node

3. **Step 3: Updating Neighbors**
   - "Once we have the current node, we update all its unvisited neighbors."
     ```python
     for neighbor in graph[current]:
         if neighbor not in visited:
             new_distance = distances[current] + 1

             if new_distance < distances[neighbor]:
                 distances[neighbor] = new_distance
                 previous[neighbor] = current
     ```
   - Walk through each line:
     - `graph[current]` gives us the list of neighbors from our graph dictionary
     - Skip neighbors already visited -- we're done with those
     - `new_distance = distances[current] + 1` -- one step between adjacent nodes
     - Only update if this new path is SHORTER than what we had before
     - Record that we reached this neighbor FROM the current node
   - After updating neighbors: `visited.append(current)`

4. **Step 4: The Complete Main Loop**
   - "Wrap the find-minimum and update-neighbors steps in a loop:"
     ```python
     while destination not in visited:
         # Find unvisited node with smallest distance
         current = None
         current_distance = 999999
         for node in distances:
             if node not in visited:
                 if distances[node] < current_distance:
                     current = node
                     current_distance = distances[node]

         # If no node found, destination is unreachable
         if current is None:
             print(f"No path to {destination}!")
             return []

         # Update neighbors
         for neighbor in graph[current]:
             if neighbor not in visited:
                 new_distance = distances[current] + 1
                 if new_distance < distances[neighbor]:
                     distances[neighbor] = new_distance
                     previous[neighbor] = current

         visited.append(current)
     ```
   - "The loop stops when the destination has been visited -- we've found the shortest path!"
   - "The `if current is None` check handles the case where the destination is unreachable (surrounded by blocked nodes)."

5. **Step 5: Reconstructing the Path**
   - "The `previous` dictionary tells us how to trace from destination back to start:"
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
   - Walk through:
     - Start at the destination
     - Look up `previous[current]` to find where we came from
     - Add each node to the path list
     - Stop when `current` is `None` -- that's the start node, which gets appended one last time before the loop stops
     - Reverse the list because we built it backwards (destination to start)
   - "The return value is a list of tuples -- exactly what `drive_path()` expects! Note this list includes `position` itself, unlike `compute_manhattan_path`'s output."

### Independent Practice (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25-30 min

**Exercise 1: Implement compute_dijkstra_path**
- Goal: Complete `compute_dijkstra_path` in your Dijkstra functions file
- Steps:
  1. Open your `dijkstra.py` file from Lesson 4
  2. Replace the placeholder with the full implementation from guided practice
  3. Save and run without errors
- Success criteria: No syntax errors, function is callable

**Exercise 2: Test with No Blocked Nodes**
- Goal: Verify that Dijkstra matches Manhattan's path length on a clear grid
- Steps:
  1. Build a graph with no blocked nodes: `graph = build_dijkstra_graph(4, 4, [])`
  2. Test these destinations:
     ```python
     print(compute_dijkstra_path((0, 0), (3, 3), graph))  # Should be 7 nodes (6 steps)
     print(compute_dijkstra_path((0, 0), (0, 3), graph))  # Should be 4 nodes (3 steps)
     print(compute_dijkstra_path((0, 0), (3, 0), graph))  # Should be 4 nodes (3 steps)
     print(compute_dijkstra_path((0, 0), (0, 0), graph))  # Should be [(0, 0)] — already there!
     ```
  3. Verify each path length (`len(path) - 1`, since the start node is included) equals the Manhattan distance
- Success criteria: All path lengths match Manhattan distances

**Exercise 3: Test with Blocked Nodes**
- Goal: Verify that Dijkstra routes around obstacles correctly
- Steps:
  1. Build a graph with one blocked node: `graph = build_dijkstra_graph(4, 4, [(1, 1)])`
  2. Compute path to (2, 2): `print(compute_dijkstra_path((0, 0), (2, 2), graph))`
  3. Verify the path does NOT include (1, 1)
  4. Compare to your hand trace from Lesson 3 -- does the path match?
  5. Try with more blocked nodes: `graph = build_dijkstra_graph(4, 4, [(1, 0), (1, 1)])`
  6. Compute path to (3, 0) and verify it goes around both blocked nodes
- Success criteria: Paths avoid all blocked nodes and match hand-traced results

**Exercise 4: Compare Manhattan and Dijkstra**
- Goal: Run both pathfinders and compare results
- Steps:
  ```python
  destinations = [(3, 3), (0, 3), (3, 0), (2, 1)]
  graph = build_dijkstra_graph(4, 4, [])

  for dest in destinations:
      m_path = compute_manhattan_path((0, 0), dest)
      d_path = compute_dijkstra_path((0, 0), dest, graph)
      print(f"To {dest}:")
      print(f"  Manhattan: {m_path}  ({len(m_path)} steps)")
      print(f"  Dijkstra:  {d_path}  ({len(d_path)-1} steps)")
      print(f"  Same length? {len(m_path) == len(d_path)-1}")
      print()
  ```
- Expected: Same number of steps for every destination. The actual nodes may differ. **Watch the `-1`** -- Dijkstra's path includes the start position, Manhattan's doesn't, so the step-count formulas are different even though the step counts themselves should match.

**Exercise 5: Challenge -- Edge Cases**
- Goal: Test unusual situations
- Tests:
  1. Start equals destination: `compute_dijkstra_path((0, 0), (0, 0), graph)` -- should return `[(0, 0)]`
  2. Adjacent destination: `compute_dijkstra_path((0, 0), (0, 1), graph)` -- should return `[(0, 0), (0, 1)]`
  3. Block all paths to destination: What happens? Does the `current is None` check work?
  4. Block a node that is not on the shortest path -- does the path length change? (It shouldn't.)

### Assessment

**Formative (during lesson)**:
- Can students explain what each of the three data structures stores?
- Can students trace through the "find minimum" code with concrete values?
- Can students explain why we check `if new_distance < distances[neighbor]`?
- Can students explain why `visited.append(current)` comes AFTER updating neighbors?
- Can students trace through path reconstruction with concrete previous dictionary values?
- Can students explain why the path must be reversed?

**Summative (worksheet/exit ticket)**:
1. In `compute_dijkstra_path`, why do we initialize all distances to 999999? Why is the start node set to 0?
2. Write the code that finds the unvisited node with the smallest distance. Explain each line.
3. When updating a neighbor's distance, why do we check `if new_distance < distances[neighbor]`? What would happen if we always updated?
4. What does the `while destination not in visited` loop do? When does it stop?
5. Given the previous dictionary `{(0,0): None, (0,1): (0,0), (0,2): (0,1), (1,2): (0,2), (2,2): (1,2)}`, write the code to reconstruct the path from (0, 0) to (2, 2). What list does it produce?

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "999999 is the actual distance to unreachable nodes" | 999999 is a placeholder representing infinity -- it means "we haven't found a path yet." If a node stays at 999999 after the algorithm finishes, it truly is unreachable. But for reachable nodes, this value gets replaced by the actual shortest distance. |
| "We should update ALL neighbors, even visited ones" | Visited nodes have their final shortest distance. Updating them would be wasted work and could introduce bugs. Always skip visited neighbors in the update step. |
| "The order of the path list is correct before reversing" | The reconstruction traces BACKWARD from destination to start. Without reversing, the path goes the wrong direction. Always reverse after reconstruction. |
| "compute_dijkstra_path's output should exclude the start position, like compute_manhattan_path's does" | This implementation's path reconstruction naturally includes the start position. That's a real difference between the two functions -- not a bug -- and something Lesson 6 addresses directly when comparing step counts. |
| "compute_dijkstra_path modifies the graph" | `compute_dijkstra_path` only reads from `graph`. The distances, previous, and visited structures are local to the function and created fresh each call. The graph itself is never changed. |
| "The algorithm visits every node before returning" | The algorithm stops as soon as the destination is visited. It may not visit every node in the graph. However, all nodes with shorter distances than the destination will have been visited. |

## Differentiation

**For struggling students**:
- Provide the complete `compute_dijkstra_path` code and have students add print statements at each step to trace execution, then compare the printed output to their Lesson 3 hand trace
- Break the implementation into smaller functions: `find_minimum(distances, visited)` and `update_neighbors(current, distances, previous, visited, graph)` -- then combine them in `compute_dijkstra_path`
- Start with a 2x2 grid (4 nodes) so there are fewer steps to trace through in the debugger
- Pair with a student who completed Exercise 1 and have them explain each section of code
- Provide a debugging checklist: (1) check distances after initialization, (2) check which node is selected as current, (3) check which neighbors get updated, (4) check visited list after each iteration

**For advanced students**:
- Add a `show_steps` parameter to `compute_dijkstra_path` that, when True, prints the state of distances, previous, and visited after each iteration
- Implement a check for unreachable destinations that returns a meaningful error message
- Research and explain: Why does Dijkstra's algorithm work correctly? Why is the shortest distance to a visited node guaranteed to be final?
- Optimize: Instead of scanning all nodes to find the minimum, keep a sorted list. How does this change the code?
- Work through the Optional Extension below and compare the two versions directly

## Materials & Code Examples

### Complete Dijkstra Functions (Lessons 4 + 5)
```python
def build_dijkstra_graph(rows, cols, blocked):
    graph = {}

    for row in range(rows):
        for col in range(cols):
            if (row, col) in blocked:
                continue

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


def compute_dijkstra_path(position, destination, graph):
    distances = {}
    previous = {}
    visited = []

    # Initialize all distances to "infinity"
    for node in graph:
        distances[node] = 999999

    # Start node is distance 0
    distances[position] = 0
    previous[position] = None

    # Main loop
    while destination not in visited:
        # Find unvisited node with smallest distance
        current = None
        current_distance = 999999
        for node in distances:
            if node not in visited:
                if distances[node] < current_distance:
                    current = node
                    current_distance = distances[node]

        # If no node found, destination is unreachable
        if current is None:
            print(f"No path to {destination}!")
            return []

        # Update neighbors
        for neighbor in graph[current]:
            if neighbor not in visited:
                new_distance = distances[current] + 1
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current

        visited.append(current)

    # Reconstruct path
    path = []
    current = destination
    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()
    return path
```

### Testing Script
```python
# Test 1: No blocked nodes
print("=== Test 1: No blocked nodes ===")
graph = build_dijkstra_graph(4, 4, [])
path = compute_dijkstra_path((0, 0), (3, 3), graph)
print(f"Path to (3,3): {path}")
print(f"Steps: {len(path) - 1}")  # Should be 6
print()

# Test 2: With blocked nodes — compare to Lesson 3 hand trace
print("=== Test 2: (1,1) blocked ===")
graph = build_dijkstra_graph(4, 4, [(1, 1)])
path = compute_dijkstra_path((0, 0), (2, 2), graph)
print(f"Path to (2,2): {path}")
print(f"Steps: {len(path) - 1}")
print(f"Path avoids (1,1): {(1, 1) not in path}")
print()

# Test 3: Start equals destination
print("=== Test 3: Start = Destination ===")
graph = build_dijkstra_graph(4, 4, [])
path = compute_dijkstra_path((0, 0), (0, 0), graph)
print(f"Path: {path}")  # Should be [(0, 0)]
```

## Teaching Notes
- **This is the most important lesson in Module 5.** Everything before this was preparation, and everything after uses the result. If students don't have a working `compute_dijkstra_path` by the end of this lesson, they can't proceed. Budget extra time and have a working solution file ready for students who get stuck.
- **Build the code in stages, exactly as shown in guided practice.** Don't show the complete function at once. Write the initialization, test it with prints. Add the find-minimum block, test it. Add neighbor updates, test it. Add the full loop, test it. Add reconstruction, test it. Each stage should be verified before moving on.
- **Connect every line of code to the paper trace.** Have the Lesson 3 tracing table visible on the board. As you write each code section, point to the corresponding column in the trace table.
- **The find-minimum loop is where students struggle most.** The pattern of "start with a bad value, scan everything, keep track of the best" is a general programming technique. If students haven't seen it before, practice it in isolation: "Given a list of numbers, find the smallest." Then apply it to the distances dictionary.
- **Flag the path-includes-start difference explicitly.** Unlike `compute_manhattan_path`, this function's returned path includes the starting position. Point this out clearly now so it doesn't confuse students in Lesson 6's step-count comparisons.
- **The `current is None` check prevents infinite loops.** Without this check, if the destination is unreachable, the algorithm would loop forever (or crash trying to access `graph[None]`). Show students what happens with and without this safety check.
- **Have students run their code on the EXACT same examples they traced by hand in Lesson 3.** This is the verification step that closes the loop between conceptual understanding and implementation.

## Connections to Next Lessons
- **Lesson 6** will test this implementation side by side with `compute_manhattan_path` and confront the parameter-shape and path-format differences directly.
- **Lesson 7** will call `compute_dijkstra_path` multiple times within a single run as the robot discovers new obstacles and recomputes paths.
- **Lesson 8** will use `compute_dijkstra_path` across multiple runs, with the blocked list growing as the robot builds experience.
- **Lesson 9** (capstone) combines `compute_dijkstra_path` with the driving functions, rangefinder, and file I/O into a complete autonomous navigation system.

---

## Optional Extension: The Completed `Dijkstra` Class

*For courses that also cover classes/objects -- builds on the Lesson 4 Optional Extension. Skip this section entirely otherwise.*

```python
class Dijkstra:
    def __init__(self, start, blocked):
        self.position = start
        self.blocked = blocked
        self.graph = self.build_graph()

    def build_graph(self):
        rows = 4
        cols = 4
        graph = {}

        for row in range(rows):
            for col in range(cols):
                if (row, col) in self.blocked:
                    continue
                neighbors = []
                if row > 0 and (row - 1, col) not in self.blocked:
                    neighbors.append((row - 1, col))
                if row < rows - 1 and (row + 1, col) not in self.blocked:
                    neighbors.append((row + 1, col))
                if col > 0 and (row, col - 1) not in self.blocked:
                    neighbors.append((row, col - 1))
                if col < cols - 1 and (row, col + 1) not in self.blocked:
                    neighbors.append((row, col + 1))
                graph[(row, col)] = neighbors

        return graph

    def compute_path(self, destination):
        distances = {}
        previous = {}
        visited = []

        for node in self.graph:
            distances[node] = 999999
        distances[self.position] = 0
        previous[self.position] = None

        while destination not in visited:
            current = None
            current_distance = 999999
            for node in distances:
                if node not in visited and distances[node] < current_distance:
                    current = node
                    current_distance = distances[node]

            if current is None:
                print(f"No path to {destination}!")
                return []

            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    new_distance = distances[current] + 1
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        previous[neighbor] = current

            visited.append(current)

        path = []
        current = destination
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()
        return path
```

Every step maps directly to the functions version -- `self.graph` replaces the `graph` parameter, `self.position` replaces `position`, and the algorithm body is character-for-character the same.

### Worksheet
See the "Optional Extension" section at the end of the Lesson 5 worksheet for matching exercises.
