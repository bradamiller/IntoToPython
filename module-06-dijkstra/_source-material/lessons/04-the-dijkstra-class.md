# Lesson 4: The Dijkstra Functions

## Overview
Students design and build the **Dijkstra pathfinding functions** -- `build_dijkstra_graph()` and `compute_dijkstra_path()` -- that encapsulate the graph representation and shortest-path computation. This lesson focuses on `build_dijkstra_graph(rows, cols, blocked)`, which creates the grid graph dictionary while excluding blocked nodes, and the `compute_dijkstra_path(position, destination, graph)` function signature. Students implement the graph-building function fully and leave `compute_dijkstra_path`'s body as a placeholder, saved for Lesson 5. By the end of this lesson, students have a working graph builder and a `compute_dijkstra_path` function that is ready to be filled in.

This lesson is where the conceptual work of Lessons 1-3 becomes real Python code. Students translate their understanding of graphs (Lesson 1), dictionaries (Lesson 2), and the algorithm concept (Lesson 3) into working functions. `compute_dijkstra_path` mirrors `compute_manhattan_path` from Module 4 -- same first two parameters (`position`, `destination`), same return type (list of tuples) -- so that `drive_path()` can drive the output of either one. This shared shape is a key design principle that students explore more in Lesson 6. Building the functions in stages (graph builder now, algorithm next lesson) prevents students from being overwhelmed by implementing everything at once.

This lesson stands on its own -- classes are never required. An **optional extension** at the end of this file shows the same functions packaged into a `Dijkstra` class, for courses that also cover OOP.

## Learning Objectives
By the end of this lesson, students will be able to:
- Design a pair of functions that work together: one to build a graph, one to search it
- Write `build_dijkstra_graph(rows, cols, blocked)` that creates the grid graph, excluding blocked nodes
- Write the `compute_dijkstra_path(position, destination, graph)` function signature with a placeholder body
- Test the functions by building graphs and verifying they are correct
- Explain how `compute_dijkstra_path`'s shape matches `compute_manhattan_path`'s shape

## Key Concepts
- **Two functions, one job each**: `build_dijkstra_graph` builds the map once; `compute_dijkstra_path` searches it. Keeping them separate means the (potentially expensive) graph-building step only has to happen when the blocked list actually changes.
- **Parameters instead of stored state**: Where a class would store `self.blocked` and `self.graph` once and reuse them, the functions version passes `graph` in explicitly every time it's needed. Nothing is remembered between calls -- every call gets everything it needs as an argument.
- **Matching shapes**: When two functions share a first-two-parameters shape (`position`, `destination`) and the same return type (list of tuples), code that calls one can be adapted to call the other with minimal changes. `compute_manhattan_path(position, destination)` and `compute_dijkstra_path(position, destination, graph)` are almost, but not quite, interchangeable -- Lesson 6 explores this gap directly.

## Materials Required
- Computers with Python installed (or XRP MicroPython environment)
- Completed graph dictionary code from Lesson 2 (`build_grid_graph` function)
- Hand-traced examples from Lesson 3 (for testing graph correctness)
- `compute_manhattan_path` code from Module 4 (for shape comparison)
- Whiteboard or projector for function design diagram

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 8 min
**For 3-hour sessions:** 10-12 min

1. **Hook: Building a Toolbox**
   - "In Module 4, you built `compute_manhattan_path` -- a tool that could compute paths on a clear grid. Now you're building a better tool: Dijkstra pathfinding."
   - "It'll be a drop-in-ish replacement for Manhattan. Same first two parameters, same return type. But it can handle obstacles."
   - Show `compute_manhattan_path` for reference:
     ```python
     def compute_manhattan_path(position, destination):
         # Returns a list of tuples
         ...
     ```
   - "Our Dijkstra functions will have a similar shape, with one addition: they need a graph to search, and that graph has to account for blocked nodes."

2. **Function Design Overview**
   - Draw the two-function structure on the board:
     ```
     build_dijkstra_graph(rows, cols, blocked)
       -- builds the graph dictionary, excluding blocked nodes
       -- returns: graph

     compute_dijkstra_path(position, destination, graph)
       -- finds shortest path (Lesson 5)
       -- returns: list of tuples
     ```
   - "Today we'll implement `build_dijkstra_graph`. Next lesson, we'll implement `compute_dijkstra_path`."

3. **Why Split Them?**
   - "Why not build the graph fresh inside `compute_dijkstra_path` every single call? Because the graph only changes when the blocked list changes -- which might be much less often than we compute paths. Building it once and passing it in avoids repeating that work."
   - "When the main program calls `compute_dijkstra_path(position, dest, graph)`, it just hands over the graph it already has. No rebuilding needed unless a new obstacle shows up."

### Guided Practice (15 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 20-25 min

1. **Writing `build_dijkstra_graph`**
   - "This is the `build_grid_graph` function from Lesson 2, extended to skip blocked nodes."
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
     ```
   - Walk through the key differences from Lesson 2:
     - `blocked` is a parameter now, passed in by whoever calls the function
     - `if (row, col) in blocked: continue` -- skip blocked nodes entirely
     - Each neighbor check also verifies the neighbor is not blocked
     - This is a single-pass approach: build the graph and handle blocked nodes at the same time
   - "This is more efficient than building the full graph and then removing blocked nodes in a second pass."

2. **Writing the `compute_dijkstra_path` Placeholder**
   - "We'll implement this fully in Lesson 5. For now, let's put in a placeholder:"
     ```python
     def compute_dijkstra_path(position, destination, graph):
         # TODO: Implement Dijkstra's algorithm (Lesson 5)
         # Should return a list of tuples from position to destination
         print(f"compute_dijkstra_path from {position} to {destination}")
         print(f"Graph has {len(graph)} nodes")
         return []
     ```
   - "The placeholder prints useful debugging information and returns an empty list. This lets us test `build_dijkstra_graph` right now without needing the algorithm yet."

3. **Testing the Functions**
   - Walk through building graphs and checking them:
     ```python
     # Test 1: No blocked nodes
     graph = build_dijkstra_graph(4, 4, [])
     print(f"Nodes in graph: {len(graph)}")       # Should be 16
     print(f"Neighbors of (1,1): {graph[(1,1)]}")  # Should be 4 neighbors

     # Test 2: With blocked nodes
     graph2 = build_dijkstra_graph(4, 4, [(1, 1)])
     print(f"Nodes in graph: {len(graph2)}")         # Should be 15
     print(f"(1,1) in graph: {(1, 1) in graph2}")    # Should be False
     print(f"Neighbors of (0,1): {graph2[(0, 1)]}")  # Should NOT include (1,1)
     ```

### Independent Practice (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25-30 min

**Exercise 1: Build the Dijkstra Functions**
- Goal: Create the complete functions file with `build_dijkstra_graph` and the `compute_dijkstra_path` placeholder
- Steps:
  1. Create a new file called `dijkstra.py`
  2. Implement `build_dijkstra_graph` using the code from guided practice
  3. Add the `compute_dijkstra_path` placeholder
- Success criteria: File runs without errors when imported

**Exercise 2: Test with No Blocked Nodes**
- Goal: Verify the graph is built correctly for a clear grid
- Steps:
  1. Call `graph = build_dijkstra_graph(4, 4, [])`
  2. Verify `len(graph)` equals 16 (4x4 grid)
  3. Check that corner nodes have 2 neighbors
  4. Check that edge nodes have 3 neighbors
  5. Check that interior nodes have 4 neighbors
  6. Print the complete graph and compare to your Lesson 2 output
- Success criteria: All node counts and neighbor lists match the expected values

**Exercise 3: Test with Blocked Nodes**
- Goal: Verify blocked node removal works correctly
- Steps:
  1. Call `graph = build_dijkstra_graph(4, 4, [(1, 1), (2, 2)])`
  2. Verify `len(graph)` equals 14 (16 - 2 blocked)
  3. Verify `(1, 1) not in graph` is True
  4. Verify `(2, 2) not in graph` is True
  5. Check neighbors of (0, 1) -- should NOT include (1, 1)
  6. Check neighbors of (1, 2) -- should NOT include (1, 1) or (2, 2)
  7. Compare to your blocked graph drawings from Lesson 1
- Success criteria: Blocked nodes are completely absent from the graph and from all neighbor lists

**Exercise 4: Test the Shape Match**
- Goal: Verify that `compute_dijkstra_path` and `compute_manhattan_path` share the same first two parameters and return type
- Steps:
  1. Call `m_path = compute_manhattan_path((0, 0), (3, 3))` -- note the return type
  2. Build a graph and call `d_path = compute_dijkstra_path((0, 0), (3, 3), graph)` -- note the return type (empty list for now, but same type!)
  3. Both return lists of tuples
- Discussion: What's different about calling these two functions? What would `drive_path()` need to know to call either one?

**Exercise 5: Challenge -- Flexible Grid Size**
- Goal: Confirm `build_dijkstra_graph` already works for any grid size
- Test with different grid sizes: 3x3, 4x4, 5x5, 3x5
  ```python
  print(len(build_dijkstra_graph(3, 3, [])))  # 9
  print(len(build_dijkstra_graph(5, 5, [])))  # 25
  print(len(build_dijkstra_graph(3, 5, [])))  # 15
  ```

### Assessment

**Formative (during lesson)**:
- Can students explain why the graph-building step is separated from the path-searching step?
- Can students explain why `blocked` is a parameter rather than something remembered automatically?
- Can students predict the number of nodes in the graph given a list of blocked nodes?
- Can students verify that blocked nodes don't appear in any neighbor lists?
- Can students explain how `compute_dijkstra_path`'s shape compares to `compute_manhattan_path`'s?

**Summative (worksheet/exit ticket)**:
1. What are the parameters of `build_dijkstra_graph`? What does each one control?
2. Write the call that builds a graph for a 4x4 grid with (1, 0) and (2, 1) blocked. How many nodes will it contain? (14)
3. In `build_dijkstra_graph`, why do we check `if (row, col) in blocked: continue`? What would happen if we didn't?
4. Why is it useful that `compute_dijkstra_path` returns the same type (list of tuples) as `compute_manhattan_path`?
5. Why does `compute_dijkstra_path` take a `graph` parameter instead of building the graph itself?

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "The graph needs to be rebuilt every time compute_dijkstra_path is called" | The graph is built once by `build_dijkstra_graph` and passed in as a parameter. `compute_dijkstra_path` only reads from it -- it doesn't rebuild it. |
| "blocked nodes should be in the graph with empty neighbor lists" | Blocked nodes should NOT be in the graph at all. They are completely excluded -- no key, no presence in any neighbor list. This is cleaner and prevents the algorithm from accidentally visiting them. |
| "The functions need to know the grid size automatically" | Grid size (`rows`, `cols`) is passed explicitly as parameters to `build_dijkstra_graph` every time -- there's no stored default to remember. |
| "compute_manhattan_path and compute_dijkstra_path are interchangeable" | They're close, but `compute_dijkstra_path` needs an extra `graph` argument. Lesson 6 addresses exactly this gap when it comes time to "swap" between them. |

## Differentiation

**For struggling students**:
- Provide a function template with blanks to fill in (parameter names, the neighbor-check pattern)
- Use print statements after building a graph to show its state: `print(f"Built graph with {len(graph)} nodes and blocked={blocked}")`
- Provide a testing script that students can run to check their implementation
- Review Lesson 2's `build_grid_graph` before starting -- ensure students remember dictionary syntax

**For advanced students**:
- Write a `print_graph(graph, rows, cols)` function that prints a visual representation
- Add input validation: What if `blocked` contains a node outside the grid?
- Think about: What would change if `build_dijkstra_graph` needed to support diagonal movement?
- Work through the Optional Extension below and compare the two versions directly

## Materials & Code Examples

### Complete Dijkstra Functions (Lesson 4 Version)
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


def compute_dijkstra_path(position, destination, graph):
    # TODO: Implement Dijkstra's algorithm (Lesson 5)
    # Should return a list of tuples from position to destination
    print(f"compute_dijkstra_path from {position} to {destination}")
    print(f"Graph has {len(graph)} nodes")
    return []
```

### Testing Script
```python
# Test 1: No blocked nodes
print("=== Test 1: No blocked nodes ===")
graph = build_dijkstra_graph(4, 4, [])
print(f"Total nodes: {len(graph)}")                  # 16
print(f"Neighbors of (0,0): {graph[(0, 0)]}")        # 2 neighbors
print(f"Neighbors of (1,1): {graph[(1, 1)]}")        # 4 neighbors
print(f"Neighbors of (0,1): {graph[(0, 1)]}")        # 3 neighbors
print()

# Test 2: One blocked node
print("=== Test 2: Block (1,1) ===")
graph = build_dijkstra_graph(4, 4, [(1, 1)])
print(f"Total nodes: {len(graph)}")                  # 15
print(f"(1,1) in graph: {(1, 1) in graph}")          # False
print(f"Neighbors of (0,1): {graph[(0, 1)]}")        # Should NOT include (1,1)
print()

# Test 3: Multiple blocked nodes
print("=== Test 3: Block (1,1) and (2,2) ===")
graph = build_dijkstra_graph(4, 4, [(1, 1), (2, 2)])
print(f"Total nodes: {len(graph)}")                  # 14
print()

# Test 4: compute_dijkstra_path placeholder
print("=== Test 4: compute_dijkstra_path placeholder ===")
graph = build_dijkstra_graph(4, 4, [(1, 1)])
path = compute_dijkstra_path((0, 0), (3, 3), graph)
print(f"Returned: {path}")                              # []
```

### Side-by-Side: Manhattan vs. Dijkstra Shapes
```python
# Manhattan (from Module 4) -- does NOT include position in the result
def compute_manhattan_path(position, destination):
    path = []
    current_row, current_col = position
    dest_row, dest_col = destination
    while current_row < dest_row:
        current_row = current_row + 1
        path.append((current_row, current_col))
    while current_row > dest_row:
        current_row = current_row - 1
        path.append((current_row, current_col))
    while current_col < dest_col:
        current_col = current_col + 1
        path.append((current_row, current_col))
    while current_col > dest_col:
        current_col = current_col - 1
        path.append((current_row, current_col))
    return path

# Dijkstra (from this lesson) -- raw output DOES include position
def build_dijkstra_graph(rows, cols, blocked):
    # ... (as shown above)
    pass

def compute_dijkstra_path(position, destination, graph):
    # ... (Lesson 5)
    return []

# Both return lists of tuples, but they don't quite match: Dijkstra's
# raw path starts with position, Manhattan's doesn't. Lesson 6 builds
# a dispatch function that irons out this difference so drive_path()
# never has to care which algorithm computed the path.
```

## Teaching Notes
- **Build incrementally.** Don't show both functions at once. Write `build_dijkstra_graph` first, test it. Then add the `compute_dijkstra_path` placeholder. This mirrors how real programmers work.
- **Test after every addition.** After writing `build_dijkstra_graph`, build a graph and print it. Students should develop the habit of testing incrementally.
- **The Module 4 connection is crucial.** If students struggled with `compute_manhattan_path` in Module 4, this is a chance to reinforce the concepts. Spend time comparing the two functions' parameter lists side by side.
- **The placeholder `compute_dijkstra_path` is intentional.** Students often want to implement everything at once. Resist this urge. The placeholder lets them test the graph builder now and focus on the algorithm in Lesson 5. This separation reduces cognitive load.
- **`build_dijkstra_graph` is doing two jobs.** It both creates the graph AND removes blocked nodes. Walk through an example where you show what would happen if you forgot the blocked-node checks (a node that shouldn't be accessible would appear as a neighbor, leading to wrong paths).

## Connections to Next Lessons
- **Lesson 5** will fill in the `compute_dijkstra_path` function body with the full Dijkstra algorithm.
- **Lesson 6** will test the completed functions alongside `compute_manhattan_path` and confront the gap between their parameter shapes directly.
- **Lessons 7-8** will extend the functions' usage by dynamically updating the blocked list based on rangefinder readings and saving/loading obstacles across runs.

---

## Optional Extension: Package It as a `Dijkstra` Class

*For courses that also cover classes/objects. Skip this section entirely otherwise -- nothing later in the course depends on it.*

### Why Wrap It?
`build_dijkstra_graph` and `compute_dijkstra_path` both need `graph`/`blocked` passed in every call. A class lets an object hold onto that state so callers don't have to keep re-supplying it:

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
        # TODO: Implement Dijkstra's algorithm (Lesson 5)
        print(f"compute_path from {self.position} to {destination}")
        print(f"Graph has {len(self.graph)} nodes")
        return []
```

### Testing It
```python
d = Dijkstra((0, 0), [(1, 1)])
print(f"Total nodes: {len(d.graph)}")
print(f"(1,1) in graph: {(1, 1) in d.graph}")
```

### Discussion Prompt
"The constructor calls `self.build_graph()` automatically. What's the functions-version equivalent of that automatic call?" (There isn't one -- the caller must explicitly call `build_dijkstra_graph(rows, cols, blocked)` and hang onto the result themselves. The class does that bookkeeping for you; the functions version makes it visible.)

### Worksheet
See the "Optional Extension" section at the end of the Lesson 4 worksheet for matching exercises.
