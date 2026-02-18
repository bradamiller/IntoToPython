# Lesson 4: The Dijkstra Class

## Overview
Students design and build the **Dijkstra class** -- a Python class that encapsulates the graph representation and shortest-path computation. This lesson focuses on the class structure: the `__init__` constructor (which accepts a start position and a list of blocked nodes), instance variables (`self.position`, `self.blocked`, `self.graph`), the `build_graph` method (which creates the grid graph dictionary and removes blocked nodes), and the `compute_path` method signature. Students implement everything except the body of `compute_path`, which is saved for Lesson 5. By the end of this lesson, students have a Dijkstra class that can build a correct graph with blocked nodes removed, and a `compute_path` method that is ready to be filled in.

This lesson is where the conceptual work of Lessons 1-3 becomes real Python code. Students translate their understanding of graphs (Lesson 1), dictionaries (Lesson 2), and the algorithm concept (Lesson 3) into a class design. The class mirrors the Manhattan class from Module 4 -- same `compute_path` method name, same return type (list of tuples) -- so that the Navigator class can use either pathfinder interchangeably. This shared interface is a key design principle that students explore more in Lesson 6. Building the class in stages (structure now, algorithm next lesson) prevents students from being overwhelmed by implementing everything at once.

## Learning Objectives
By the end of this lesson, students will be able to:
- Design a Python class with `__init__`, instance variables, and methods
- Write the `__init__` method for the Dijkstra class with `start` and `blocked` parameters
- Store instance variables using `self.position`, `self.blocked`, and `self.graph`
- Implement `build_graph` using the `build_grid_graph` logic from Lesson 2
- Remove blocked nodes from the graph inside `build_graph`
- Write the `compute_path` method signature with a placeholder body
- Test the class by creating instances and verifying the graph is correct
- Explain how Dijkstra's interface matches Manhattan's interface

## Key Concepts
- **Class**: A blueprint for creating objects that bundles data (instance variables) and behavior (methods) together. The Dijkstra class bundles the graph, start position, and blocked list (data) with the `build_graph` and `compute_path` methods (behavior).
- **Constructor (`__init__`)**: The special method that runs when a new object is created. It sets up the initial state of the object. For Dijkstra, the constructor takes `start` and `blocked` as parameters, stores them as instance variables, and calls `build_graph` to create the graph.
- **Instance variable (`self.___`)**: A variable that belongs to a specific object and is accessed using `self`. Instance variables persist for the lifetime of the object. Example: `self.graph` stores the graph dictionary so that `compute_path` can use it later.
- **Method**: A function defined inside a class that operates on the object's data. Methods always take `self` as the first parameter. Example: `build_graph(self)` creates the graph using `self.blocked` to know which nodes to remove.
- **Shared interface**: When two different classes have a method with the same name and return type, they can be used interchangeably. Manhattan and Dijkstra both have `compute_path(destination)` returning a list of tuples, so Navigator works with either one.

## Materials Required
- Computers with Python installed (or XRP MicroPython environment)
- Completed graph dictionary code from Lesson 2 (`build_grid_graph` function)
- Hand-traced examples from Lesson 3 (for testing graph correctness)
- Manhattan class code from Module 4 (for interface comparison)
- Whiteboard or projector for class design diagram

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 8 min
**For 3-hour sessions:** 10-12 min

1. **Hook: Building a Toolbox**
   - "In Module 4, you built a Manhattan class -- a toolbox that could compute paths on a clear grid. Now you're building a better toolbox: the Dijkstra class."
   - "The Dijkstra class will be a drop-in replacement for Manhattan. Same method name, same return type. But it can handle obstacles."
   - Show the Manhattan class structure for reference:
     ```python
     class Manhattan:
         def __init__(self, start):
             self.position = start

         def compute_path(self, destination):
             # Returns a list of tuples
             ...
     ```
   - "Our Dijkstra class will have the same shape, with two additions: a blocked list and a graph."

2. **Class Design Overview**
   - Draw the class structure on the board:
     ```
     Dijkstra
     --------
     Data:
       self.position   -- current start position (tuple)
       self.blocked    -- list of blocked nodes (list of tuples)
       self.graph      -- graph dictionary (built by build_graph)

     Methods:
       __init__(start, blocked)  -- constructor
       build_graph()             -- creates the graph, removes blocked nodes
       compute_path(destination) -- finds shortest path (Lesson 5)
     ```
   - "Today we'll implement `__init__` and `build_graph`. Next lesson, we'll implement `compute_path`."

3. **Why a Class?**
   - "Why not just write functions? Because the graph, start position, and blocked list are all related. A class keeps them together."
   - "When Navigator calls `pathfinder.compute_path(dest)`, it doesn't need to pass the graph or the blocked list. The Dijkstra object already has them stored as instance variables."

### Guided Practice (15 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 20-25 min

1. **Writing the Constructor**
   - Walk through each line:
     ```python
     class Dijkstra:
         def __init__(self, start, blocked):
             self.position = start
             self.blocked = blocked
             self.graph = self.build_graph()
     ```
   - Explain each instance variable:
     - `self.position = start` -- stores where the robot is (a tuple like (0, 0))
     - `self.blocked = blocked` -- stores the list of blocked nodes (a list of tuples)
     - `self.graph = self.build_graph()` -- builds the graph immediately when the object is created
   - "Notice that the constructor CALLS `build_graph()`. This means the graph is ready to use as soon as you create a Dijkstra object."
   - Compare to Manhattan's constructor: Manhattan only takes `start`. Dijkstra also takes `blocked`.

2. **Writing the `build_graph` Method**
   - "This is the `build_grid_graph` function from Lesson 2, adapted as a class method that also removes blocked nodes."
     ```python
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
     ```
   - Walk through the key differences from Lesson 2:
     - `self.blocked` instead of a separate parameter -- the class stores the blocked list
     - `if (row, col) in self.blocked: continue` -- skip blocked nodes entirely
     - Each neighbor check also verifies the neighbor is not blocked
     - This is a single-pass approach: we build the graph and handle blocked nodes at the same time
   - "This is more efficient than building the full graph and then removing blocked nodes in a second pass."

3. **Writing the `compute_path` Placeholder**
   - "We'll implement this fully in Lesson 5. For now, let's put in a placeholder:"
     ```python
     def compute_path(self, destination):
         # TODO: Implement Dijkstra's algorithm (Lesson 5)
         # Should return a list of tuples from self.position to destination
         print(f"compute_path from {self.position} to {destination}")
         print(f"Graph has {len(self.graph)} nodes")
         return []
     ```
   - "The placeholder prints useful debugging information and returns an empty list. This lets us test the constructor and `build_graph` right now without needing the algorithm yet."

4. **Testing the Class**
   - Walk through creating instances and checking the graph:
     ```python
     # Test 1: No blocked nodes
     d = Dijkstra((0, 0), [])
     print(f"Nodes in graph: {len(d.graph)}")       # Should be 16
     print(f"Neighbors of (1,1): {d.graph[(1,1)]}")  # Should be 4 neighbors

     # Test 2: With blocked nodes
     d = Dijkstra((0, 0), [(1, 1)])
     print(f"Nodes in graph: {len(d.graph)}")         # Should be 15
     print(f"(1,1) in graph: {(1, 1) in d.graph}")    # Should be False
     print(f"Neighbors of (0,1): {d.graph[(0, 1)]}")  # Should NOT include (1,1)
     ```

### Independent Practice (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25-30 min

**Exercise 1: Build the Dijkstra Class**
- Goal: Create the complete class file with `__init__`, `build_graph`, and `compute_path` placeholder
- Steps:
  1. Create a new file called `dijkstra.py`
  2. Write the `class Dijkstra:` declaration
  3. Implement `__init__` with `start` and `blocked` parameters
  4. Implement `build_graph` using the code from guided practice
  5. Add the `compute_path` placeholder
- Success criteria: File runs without errors when imported

**Exercise 2: Test with No Blocked Nodes**
- Goal: Verify the graph is built correctly for a clear grid
- Steps:
  1. Create a Dijkstra object: `d = Dijkstra((0, 0), [])`
  2. Verify `len(d.graph)` equals 16 (4x4 grid)
  3. Check that corner nodes have 2 neighbors
  4. Check that edge nodes have 3 neighbors
  5. Check that interior nodes have 4 neighbors
  6. Print the complete graph and compare to your Lesson 2 output
- Success criteria: All node counts and neighbor lists match the expected values

**Exercise 3: Test with Blocked Nodes**
- Goal: Verify blocked node removal works correctly
- Steps:
  1. Create a Dijkstra object: `d = Dijkstra((0, 0), [(1, 1), (2, 2)])`
  2. Verify `len(d.graph)` equals 14 (16 - 2 blocked)
  3. Verify `(1, 1) not in d.graph` is True
  4. Verify `(2, 2) not in d.graph` is True
  5. Check neighbors of (0, 1) -- should NOT include (1, 1)
  6. Check neighbors of (1, 2) -- should NOT include (1, 1) or (2, 2)
  7. Compare to your blocked graph drawings from Lesson 1
- Success criteria: Blocked nodes are completely absent from the graph and from all neighbor lists

**Exercise 4: Test the Interface Match**
- Goal: Verify that Dijkstra has the same interface as Manhattan
- Steps:
  1. Create a Manhattan object: `m = Manhattan((0, 0))`
  2. Create a Dijkstra object: `d = Dijkstra((0, 0), [])`
  3. Call `m.compute_path((3, 3))` -- note the return type
  4. Call `d.compute_path((3, 3))` -- note the return type (empty list for now, but same type!)
  5. Both return lists of tuples. Navigator can use either one.
- Discussion: What would need to change in Navigator to use Dijkstra instead of Manhattan?

**Exercise 5: Challenge -- Flexible Grid Size**
- Goal: Make `build_graph` work with any grid size
- Modify the class to accept `rows` and `cols` as constructor parameters:
  ```python
  def __init__(self, start, blocked, rows=4, cols=4):
      self.position = start
      self.blocked = blocked
      self.rows = rows
      self.cols = cols
      self.graph = self.build_graph()
  ```
- Update `build_graph` to use `self.rows` and `self.cols` instead of hard-coded 4
- Test with different grid sizes: 3x3, 4x4, 5x5, 3x5

### Assessment

**Formative (during lesson)**:
- Can students explain what each instance variable stores?
- Can students trace through the constructor to explain when `build_graph` is called?
- Can students explain why `self` is the first parameter of every method?
- Can students predict the number of nodes in the graph given a list of blocked nodes?
- Can students verify that blocked nodes don't appear in any neighbor lists?
- Can students explain why Dijkstra and Manhattan having the same method name matters?

**Summative (worksheet/exit ticket)**:
1. What are the three instance variables of the Dijkstra class? What does each store?
2. Write the constructor for the Dijkstra class. Include all three instance variables.
3. If you create `d = Dijkstra((0, 0), [(1, 0), (2, 1)])` on a 4x4 grid, how many nodes will `d.graph` contain? (14)
4. In `build_graph`, why do we check `if (row, col) in self.blocked: continue`? What would happen if we didn't?
5. Why is it important that Dijkstra's `compute_path` returns the same type (list of tuples) as Manhattan's `compute_path`?

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "self.position and the start parameter are different things" | `self.position = start` copies the start parameter into an instance variable. They hold the same value. The instance variable lets other methods access it later using `self.position`. |
| "build_graph needs to be called separately after creating the object" | The constructor calls `self.build_graph()` automatically. The graph is ready as soon as the object is created. You don't need to call it yourself. |
| "The graph is rebuilt every time compute_path is called" | The graph is built ONCE in the constructor and stored in `self.graph`. The `compute_path` method uses the existing graph without rebuilding it. |
| "blocked nodes should be in the graph with empty neighbor lists" | Blocked nodes should NOT be in the graph at all. They are completely excluded -- no key, no presence in any neighbor list. This is cleaner and prevents the algorithm from accidentally visiting them. |
| "self is a parameter you pass when calling a method" | `self` is automatically passed by Python when you call a method on an object. You write `d.compute_path(dest)`, not `d.compute_path(d, dest)`. Python fills in `self = d` for you. |
| "The class needs to know the grid size at compile time" | The grid size (rows, cols) can be set in the constructor, either as hard-coded values or as parameters. The `build_graph` method uses whatever size is stored in the object. |

## Differentiation

**For struggling students**:
- Provide a class template with blanks to fill in (constructor signature, instance variable names, method signatures)
- Start by having students write `build_graph` as a standalone function first, then move it into the class
- Use print statements at the end of `__init__` to show the object's state: `print(f"Created Dijkstra at {self.position} with {len(self.blocked)} blocked nodes and {len(self.graph)} graph nodes")`
- Provide a testing script that students can run to check their implementation
- Review Module 4's class syntax before starting -- ensure students remember `class`, `def`, `self`

**For advanced students**:
- Add a `__str__` method that prints a visual representation of the graph
- Add input validation: What if start is in the blocked list? What if start is outside the grid?
- Make the class accept a custom graph dictionary instead of always building a grid -- this makes Dijkstra work on any graph, not just grids
- Add a `reset` method that allows changing the start position or blocked list and rebuilds the graph
- Think about: Why do we store `self.blocked` as an instance variable? When might we need it after `build_graph` finishes?

## Materials & Code Examples

### Complete Dijkstra Class (Lesson 4 Version)
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
                # Skip blocked nodes
                if (row, col) in self.blocked:
                    continue

                # Build neighbor list, excluding blocked neighbors
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
        # Should return a list of tuples from self.position to destination
        print(f"compute_path from {self.position} to {destination}")
        print(f"Graph has {len(self.graph)} nodes")
        return []
```

### Testing Script
```python
from dijkstra import Dijkstra

# Test 1: No blocked nodes
print("=== Test 1: No blocked nodes ===")
d = Dijkstra((0, 0), [])
print(f"Total nodes: {len(d.graph)}")                  # 16
print(f"Neighbors of (0,0): {d.graph[(0, 0)]}")        # 2 neighbors
print(f"Neighbors of (1,1): {d.graph[(1, 1)]}")        # 4 neighbors
print(f"Neighbors of (0,1): {d.graph[(0, 1)]}")        # 3 neighbors
print()

# Test 2: One blocked node
print("=== Test 2: Block (1,1) ===")
d = Dijkstra((0, 0), [(1, 1)])
print(f"Total nodes: {len(d.graph)}")                  # 15
print(f"(1,1) in graph: {(1, 1) in d.graph}")          # False
print(f"Neighbors of (0,1): {d.graph[(0, 1)]}")        # Should NOT include (1,1)
print(f"Neighbors of (1,0): {d.graph[(1, 0)]}")        # Should NOT include (1,1)
print(f"Neighbors of (2,1): {d.graph[(2, 1)]}")        # Should NOT include (1,1)
print(f"Neighbors of (1,2): {d.graph[(1, 2)]}")        # Should NOT include (1,1)
print()

# Test 3: Multiple blocked nodes
print("=== Test 3: Block (1,1) and (2,2) ===")
d = Dijkstra((0, 0), [(1, 1), (2, 2)])
print(f"Total nodes: {len(d.graph)}")                  # 14
print(f"(1,1) in graph: {(1, 1) in d.graph}")          # False
print(f"(2,2) in graph: {(2, 2) in d.graph}")          # False
print()

# Test 4: compute_path placeholder
print("=== Test 4: compute_path placeholder ===")
d = Dijkstra((0, 0), [(1, 1)])
path = d.compute_path((3, 3))
print(f"Returned: {path}")                              # []
```

### Side-by-Side: Manhattan vs. Dijkstra
```python
# Manhattan class (from Module 4)
class Manhattan:
    def __init__(self, start):
        self.position = start

    def compute_path(self, destination):
        path = [self.position]
        current_row, current_col = self.position
        dest_row, dest_col = destination
        while current_row != dest_row:
            if current_row < dest_row:
                current_row = current_row + 1
            else:
                current_row = current_row - 1
            path.append((current_row, current_col))
        while current_col != dest_col:
            if current_col < dest_col:
                current_col = current_col + 1
            else:
                current_col = current_col - 1
            path.append((current_row, current_col))
        return path

# Dijkstra class (from this lesson)
class Dijkstra:
    def __init__(self, start, blocked):
        self.position = start
        self.blocked = blocked
        self.graph = self.build_graph()

    def build_graph(self):
        # ... (as shown above)
        pass

    def compute_path(self, destination):
        # ... (Lesson 5)
        return []

# Both work with Navigator!
# Navigator only calls: pathfinder.compute_path(destination)
# It doesn't care which class it's using.
```

## Teaching Notes
- **Build incrementally.** Don't show the full class at once. Write `__init__` first, test it. Then add `build_graph`, test it. Then add the `compute_path` placeholder. This mirrors how real programmers work.
- **Test after every addition.** After writing `__init__`, create an object and print its instance variables. After writing `build_graph`, check the graph. Students should develop the habit of testing incrementally.
- **The Module 4 connection is crucial.** If students struggled with classes in Module 4, this is a chance to reinforce the concepts. Spend time comparing the Manhattan and Dijkstra class structures side by side.
- **The placeholder `compute_path` is intentional.** Students often want to implement everything at once. Resist this urge. The placeholder lets them test the class structure now and focus on the algorithm in Lesson 5. This separation reduces cognitive load.
- **`build_graph` is doing two jobs.** It both creates the graph AND removes blocked nodes. Walk through an example where you show what would happen if you forgot the blocked-node checks (a node that shouldn't be accessible would appear as a neighbor, leading to wrong paths).
- **The `self` keyword trips up many students.** If students forget `self` in method definitions or when accessing instance variables, they'll get confusing errors. A common mistake is writing `position = start` instead of `self.position = start`. Show what happens when `self` is omitted.

## Connections to Next Lessons
- **Lesson 5** will fill in the `compute_path` method body with the full Dijkstra algorithm. Students will use `self.graph` to look up neighbors and `self.position` as the start node.
- **Lesson 6** will test the completed Dijkstra class alongside Manhattan and swap it into the Navigator class. The identical `compute_path` interface makes this a two-line change.
- **Lessons 7-8** will extend the class's usage by dynamically updating the blocked list based on rangefinder readings and saving/loading obstacles across runs.
- The class design pattern used here (constructor builds internal state, methods operate on it) is the same pattern used throughout the XRP library.
