# Lesson 2: Dictionaries

## Overview
Students learn about Python **dictionaries** -- the key-value data structure that will represent the grid graph in code. In Lesson 1, students drew graphs on paper with nodes and edges. Now they translate that paper representation into Python using dictionaries where each key is a (row, col) tuple representing a node, and each value is a list of neighbor tuples representing that node's edges. Students start with the basics of dictionary syntax -- creating dictionaries with curly braces, adding key-value pairs, and accessing values by key. They then learn to check if a key exists using the `in` keyword. The lesson culminates in building a `build_grid_graph(rows, cols)` function that programmatically generates the full graph dictionary for any grid size, and then removing blocked nodes from the graph. By the end of the lesson, students can represent any grid (with or without blocked nodes) as a Python dictionary ready for Dijkstra's algorithm.

This lesson is the bridge between the conceptual graph understanding from Lesson 1 and the algorithmic work in Lessons 3-5. Students need dictionaries to store the graph that Dijkstra's algorithm will traverse. The dictionary structure also reinforces the tuple and list concepts from Module 4, since keys are tuples and values are lists of tuples. Understanding how to build and modify the graph dictionary is essential -- the Dijkstra class in Lessons 4-5 will use `build_grid_graph` as a core method, and obstacle handling depends on being able to remove nodes and their edges from the dictionary.

## Learning Objectives
By the end of this lesson, students will be able to:
- Explain what a dictionary is: a collection of key-value pairs
- Create a dictionary using curly braces `{}`
- Add key-value pairs to a dictionary
- Access a value by its key using square bracket notation
- Check if a key exists in a dictionary using the `in` keyword
- Build a dictionary that represents a grid graph where keys are (row, col) tuples and values are lists of neighbor tuples
- Write a `build_grid_graph(rows, cols)` function that generates the full graph
- Remove blocked nodes from a graph dictionary

## Key Concepts
- **Dictionary**: A Python data structure that stores **key-value pairs** inside curly braces `{}`. Each key maps to exactly one value. You look up values by their key, similar to looking up a word's definition in a real dictionary. Example: `graph = {(0, 0): [(0, 1), (1, 0)]}` maps the node (0, 0) to its list of neighbors.
- **Key**: The identifier used to look up a value in a dictionary. In our graph, keys are (row, col) tuples representing intersections. Keys must be unique -- each key appears at most once in a dictionary.
- **Value**: The data associated with a key. In our graph, values are lists of neighbor tuples. A value can be any Python object -- a number, string, list, or even another dictionary.
- **Key-Value Pair**: A single entry in a dictionary consisting of a key and its associated value, written as `key: value`. Example: `(1, 1): [(0, 1), (2, 1), (1, 0), (1, 2)]` means node (1, 1) connects to four neighbors.
- **The `in` keyword**: An operator that checks whether a key exists in a dictionary. Returns `True` or `False`. Example: `(1, 1) in graph` returns `True` if node (1, 1) is in the graph. This is essential for checking whether a node is blocked (not in the graph).
- **Graph dictionary**: A dictionary where every node in the graph is a key, and each key's value is a list of that node's neighbors. This is the Python representation of the graph students drew on paper in Lesson 1.

## Materials Required
- Computers with Python installed (or XRP MicroPython environment)
- Graph drawings from Lesson 1 (for reference)
- Whiteboard or projector for demonstrations
- Printed reference: dictionary syntax cheat sheet
- Grid worksheets from Lesson 1 (for checking neighbor lists)

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 8 min
**For 3-hour sessions:** 10-12 min

1. **Hook: From Paper to Code**
   - Hold up a student's graph drawing from Lesson 1
   - Ask: "You drew this graph on paper. How would you describe it to someone who can't see it?"
   - Students might say: "Node (0,0) connects to (0,1) and (1,0). Node (0,1) connects to (0,0), (0,2), and (1,1)..."
   - "You're listing each node and its neighbors. That's EXACTLY what a dictionary does -- it stores a label (the node) and its information (the neighbor list)."
   - "Today we'll learn Python's dictionary data structure so we can represent this graph in code."

2. **What Is a Dictionary?**
   - A dictionary stores **key-value pairs** inside curly braces `{}`
   - Real-world analogy: A real dictionary maps **words** (keys) to **definitions** (values). A phone book maps **names** (keys) to **phone numbers** (values).
   - Python dictionaries map **any key** to **any value**
   - For our graph: **nodes** (tuple keys) map to **neighbor lists** (list values)

3. **Why Not Just Use Lists?**
   - In Module 4, we used lists to store paths: `[(0,0), (1,0), (2,0)]`
   - Lists are ordered by position (index 0, 1, 2...)
   - But we need to look up by CONTENT: "What are the neighbors of (1, 1)?"
   - Lists would require searching through every element. Dictionaries let us jump directly to the answer.

### Guided Practice (15 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 20-25 min

1. **Creating a Dictionary**
   - Show the syntax:
     ```python
     # Empty dictionary
     graph = {}

     # Dictionary with initial data
     scores = {"Alice": 95, "Bob": 87, "Carol": 92}
     ```
   - Explain: Keys are on the left of the colon, values on the right. Pairs are separated by commas.

2. **Adding Key-Value Pairs**
   - Show how to add entries to an existing dictionary:
     ```python
     graph = {}
     graph[(0, 0)] = [(0, 1), (1, 0)]
     graph[(0, 1)] = [(0, 0), (0, 2), (1, 1)]
     graph[(0, 2)] = [(0, 1), (1, 2)]
     print(graph)
     ```
   - Point out: The key is a tuple `(0, 0)`, and the value is a list of tuples `[(0, 1), (1, 0)]`
   - Ask: "What does this dictionary represent?" (The top row of a 3x3 grid graph -- each node and its neighbors.)

3. **Accessing Values by Key**
   - Show how to look up a value:
     ```python
     neighbors = graph[(0, 0)]
     print(neighbors)  # [(0, 1), (1, 0)]

     print(graph[(0, 1)])  # [(0, 0), (0, 2), (1, 1)]
     ```
   - Ask: "How many neighbors does (0, 0) have?" Answer: `len(graph[(0, 0)])` returns 2.
   - Important: If you try to access a key that doesn't exist, Python raises a `KeyError`. This is why the `in` keyword is useful.

4. **Checking If a Key Exists**
   - Show the `in` keyword:
     ```python
     print((0, 0) in graph)  # True
     print((2, 2) in graph)  # False -- we haven't added it yet

     if (1, 1) in graph:
         print("Node (1,1) is in the graph")
     else:
         print("Node (1,1) is NOT in the graph")
     ```
   - "This will be crucial for checking whether a node is blocked. If a node is blocked, it won't be in the graph dictionary. So `(1, 1) in graph` tells us whether (1, 1) is accessible."

5. **Building the Full 3x3 Graph by Hand**
   - Walk through adding all 9 nodes:
     ```python
     graph = {}
     graph[(0, 0)] = [(0, 1), (1, 0)]
     graph[(0, 1)] = [(0, 0), (0, 2), (1, 1)]
     graph[(0, 2)] = [(0, 1), (1, 2)]
     graph[(1, 0)] = [(0, 0), (1, 1), (2, 0)]
     graph[(1, 1)] = [(0, 1), (1, 0), (1, 2), (2, 1)]
     graph[(1, 2)] = [(0, 2), (1, 1), (2, 2)]
     graph[(2, 0)] = [(1, 0), (2, 1)]
     graph[(2, 1)] = [(2, 0), (1, 1), (2, 2)]
     graph[(2, 2)] = [(2, 1), (1, 2)]
     ```
   - "That's a lot of typing for just 9 nodes. Imagine a 10x10 grid -- that's 100 nodes! We need a function to build this automatically."

### Independent Practice (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25-30 min

**Exercise 1: Dictionary Basics**
- Goal: Practice creating and using dictionaries
- Steps:
  1. Create an empty dictionary called `my_dict`
  2. Add three key-value pairs where keys are (row, col) tuples and values are lists of neighbor tuples
  3. Print the value for one of the keys
  4. Check if `(5, 5)` is in the dictionary (should be False)
  5. Check if one of your keys is in the dictionary (should be True)
- Success criteria: All operations work without errors

**Exercise 2: Build a 3x3 Graph Manually**
- Goal: Represent the full 3x3 grid as a dictionary
- Steps:
  1. Create an empty dictionary called `graph`
  2. Add all 9 nodes with their correct neighbor lists
  3. Print `graph[(1, 1)]` and verify it shows 4 neighbors
  4. Print `graph[(0, 0)]` and verify it shows 2 neighbors
  5. Verify: `len(graph)` should equal 9
- Compare your dictionary to your paper graph from Lesson 1 -- do they match?

**Exercise 3: Write `build_grid_graph(rows, cols)`**
- Goal: Automate the graph-building process
- Steps:
  1. Write a function that takes `rows` and `cols` as parameters
  2. Use nested for loops to iterate over every (row, col) position
  3. For each position, calculate its neighbors (up, down, left, right) -- only include neighbors that are within the grid bounds
  4. Add each node and its neighbor list to the dictionary
  5. Return the completed dictionary
- Test with:
  ```python
  graph = build_grid_graph(3, 3)
  print(graph[(1, 1)])  # Should show 4 neighbors
  print(graph[(0, 0)])  # Should show 2 neighbors
  print(len(graph))     # Should be 9

  graph = build_grid_graph(4, 4)
  print(len(graph))     # Should be 16
  ```
- Success criteria: Function works for any grid size

**Exercise 4: Remove Blocked Nodes**
- Goal: Modify the graph to handle obstacles
- Steps:
  1. Build a 4x4 graph using `build_grid_graph(4, 4)`
  2. Write code to remove node (1, 1) from the graph:
     - Delete the key `(1, 1)` from the dictionary using `del graph[(1, 1)]`
     - For every remaining node, remove `(1, 1)` from its neighbor list if present
  3. Verify: `(1, 1) in graph` should be `False`
  4. Verify: `graph[(0, 1)]` should NOT include `(1, 1)` in its neighbor list
  5. Repeat for blocking node (2, 2)

### Assessment

**Formative (during lesson)**:
- Can students create a dictionary with correct syntax?
- Can students add key-value pairs where keys are tuples?
- Can students look up values using a tuple as a key?
- Can students use `in` to check for key existence?
- Can students explain what each key and value represents in the graph dictionary?
- Can students correctly identify which neighbors a node should have?

**Summative (worksheet/exit ticket)**:
1. What is a dictionary? How is it different from a list?
2. Write code to create a dictionary with two key-value pairs where keys are tuples and values are lists.
3. Given `graph = {(0,0): [(0,1), (1,0)], (0,1): [(0,0)]}`, what does `graph[(0,0)]` return?
4. Write code that checks if `(2, 2)` is a key in `graph` and prints "found" or "not found".
5. If node (1, 1) is blocked, what two things must you do to the graph dictionary? (Remove the key AND remove (1, 1) from all neighbor lists.)

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "Dictionaries are ordered by index like lists" | Dictionaries are accessed by KEY, not by position. There is no "first" or "second" element in the way lists have index 0, 1, 2. You look up data by its key. |
| "Keys can be duplicated" | Each key in a dictionary is unique. If you assign a value to an existing key, it OVERWRITES the old value. `graph[(0,0)] = [A]` then `graph[(0,0)] = [B]` results in the value being `[B]`. |
| "Removing a blocked node means just deleting the key" | You must ALSO remove the blocked node from all neighbor lists. Otherwise, other nodes will still think they can reach the blocked node. It's a two-step process: delete the key AND clean up neighbor lists. |
| "Any value can be a key" | Keys must be immutable (unchangeable). Tuples work as keys, but lists do not. This is why we use (row, col) tuples, not [row, col] lists, as keys. |
| "Accessing a missing key returns None" | Accessing a key that doesn't exist raises a `KeyError` crash. Always check with `in` first, or use the `.get()` method. |
| "The graph dictionary IS the graph" | The dictionary is a REPRESENTATION of the graph. The graph is the abstract concept of nodes and edges. The dictionary is one way to store it in code. |

## Differentiation

**For struggling students**:
- Start with simple non-graph dictionaries: `{"name": "Alice", "age": 15}` to learn syntax before tuples
- Provide the neighbor lists on paper (from Lesson 1) so students only need to type them into the dictionary
- Give a partially completed `build_grid_graph` function with blanks to fill in
- Use print statements after each dictionary operation to show the current state
- Pair with a stronger student for Exercise 3 (the function)

**For advanced students**:
- Write a `remove_blocked` function that takes a graph and a list of blocked nodes and returns a new graph with all blocked nodes removed (both keys and neighbor references)
- Add error handling to `build_grid_graph`: what if rows or cols is 0 or negative?
- Explore dictionary methods: `.keys()`, `.values()`, `.items()` -- how could these be useful for graph operations?
- Research: What is the time complexity of looking up a key in a dictionary vs. searching a list? Why does this matter for large graphs?
- Write a function `print_grid_graph(graph, rows, cols)` that prints the graph in a visual format similar to the paper drawings from Lesson 1

## Materials & Code Examples

### Dictionary Basics
```python
# Creating an empty dictionary
graph = {}

# Adding key-value pairs
graph[(0, 0)] = [(0, 1), (1, 0)]
graph[(0, 1)] = [(0, 0), (0, 2), (1, 1)]

# Accessing a value by key
neighbors = graph[(0, 0)]
print(neighbors)          # [(0, 1), (1, 0)]
print(len(neighbors))     # 2

# Checking if a key exists
print((0, 0) in graph)    # True
print((5, 5) in graph)    # False

# Safe access pattern
node = (1, 1)
if node in graph:
    print(f"Neighbors of {node}: {graph[node]}")
else:
    print(f"{node} is not in the graph")
```

### Full 3x3 Grid Graph
```python
graph = {
    (0, 0): [(0, 1), (1, 0)],
    (0, 1): [(0, 0), (0, 2), (1, 1)],
    (0, 2): [(0, 1), (1, 2)],
    (1, 0): [(0, 0), (1, 1), (2, 0)],
    (1, 1): [(0, 1), (1, 0), (1, 2), (2, 1)],
    (1, 2): [(0, 2), (1, 1), (2, 2)],
    (2, 0): [(1, 0), (2, 1)],
    (2, 1): [(2, 0), (1, 1), (2, 2)],
    (2, 2): [(2, 1), (1, 2)]
}

# Verify
print(f"Total nodes: {len(graph)}")            # 9
print(f"Neighbors of (1,1): {graph[(1, 1)]}")  # 4 neighbors
print(f"Neighbors of (0,0): {graph[(0, 0)]}")  # 2 neighbors
```

### build_grid_graph Function
```python
def build_grid_graph(rows, cols):
    graph = {}
    for row in range(rows):
        for col in range(cols):
            neighbors = []
            # Check up
            if row > 0:
                neighbors.append((row - 1, col))
            # Check down
            if row < rows - 1:
                neighbors.append((row + 1, col))
            # Check left
            if col > 0:
                neighbors.append((row, col - 1))
            # Check right
            if col < cols - 1:
                neighbors.append((row, col + 1))
            graph[(row, col)] = neighbors
    return graph

# Test it
graph = build_grid_graph(3, 3)
print(f"Total nodes: {len(graph)}")
for node in graph:
    print(f"  {node}: {graph[node]}")
```

### Removing Blocked Nodes
```python
def remove_blocked(graph, blocked_nodes):
    # Step 1: Remove blocked nodes as keys
    for node in blocked_nodes:
        if node in graph:
            del graph[node]

    # Step 2: Remove blocked nodes from all neighbor lists
    for node in graph:
        new_neighbors = []
        for neighbor in graph[node]:
            if neighbor not in blocked_nodes:
                new_neighbors.append(neighbor)
        graph[node] = new_neighbors

    return graph

# Test it
graph = build_grid_graph(3, 3)
print("Before blocking:")
print(f"  (1,1) in graph: {(1, 1) in graph}")
print(f"  Neighbors of (0,1): {graph[(0, 1)]}")

graph = remove_blocked(graph, [(1, 1)])
print("After blocking (1,1):")
print(f"  (1,1) in graph: {(1, 1) in graph}")
print(f"  Neighbors of (0,1): {graph[(0, 1)]}")
```

### Verifying Against Lesson 1 Paper Graph
```python
# Build the same graph you drew on paper in Lesson 1
graph = build_grid_graph(3, 3)

# Block node (1, 0) -- same as Lesson 1 example
graph = remove_blocked(graph, [(1, 0)])

# Check: (0,0) should now only have 1 neighbor: (0,1)
print(f"Neighbors of (0,0): {graph[(0, 0)]}")  # [(0, 1)]

# Check: (2,0) should now only have 1 neighbor: (2,1)
print(f"Neighbors of (2,0): {graph[(2, 0)]}")  # [(2, 1)]

# Check: (1,0) should not be in the graph
print(f"(1,0) in graph: {(1, 0) in graph}")    # False
```

## Teaching Notes
- **Start with simple dictionaries.** Before jumping to graph dictionaries with tuple keys and list values, show students a plain dictionary like `{"name": "Alice", "age": 15}`. Let them get comfortable with the syntax before adding complexity.
- **Connect explicitly to Lesson 1.** Have students open their graph drawings from Lesson 1. For each node they drew, ask: "What would the key be? What would the value be?" This makes the translation from paper to code concrete.
- **The `build_grid_graph` function is the core deliverable.** Students will copy this function into their Dijkstra class in Lesson 4. Make sure every student has a working version by the end of the lesson.
- **Emphasize the two-step removal process.** The most common bug in later lessons will be removing a blocked node's key but forgetting to remove it from neighbor lists. Spend extra time on this. Draw it on the board: "Delete the key -- but now (0, 1) still thinks (1, 1) is its neighbor. We need to clean that up."
- **Use print statements liberally.** After every dictionary operation, print the dictionary or specific entries so students can see what changed. This is especially important when removing blocked nodes.
- **The `in` keyword is new but essential.** Students will use `in` constantly in Lessons 3-5 (checking visited lists, checking if nodes exist in the graph). Make sure they understand it well here.

## Connections to Next Lessons
- **Lesson 3** will use the graph dictionary to hand-trace Dijkstra's algorithm. Students will look up neighbors in the dictionary as they step through the algorithm on paper.
- **Lesson 4** will incorporate `build_grid_graph` as a method of the Dijkstra class. The class constructor will call this method and then remove blocked nodes.
- **Lesson 5** will implement `compute_path`, which iterates over the graph dictionary to find shortest paths. Every line of that method depends on understanding how to access and check dictionary keys.
- The `remove_blocked` pattern introduced here is the foundation for obstacle handling throughout the rest of Module 5.
