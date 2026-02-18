# Lesson 3: Dijkstra's Algorithm — The Concept

## Overview
Students learn the conceptual foundation of Dijkstra's algorithm before writing any code. This is a paper-and-pencil lesson where students hand-trace the algorithm step by step on small grids, building intuition for how it works. The algorithm maintains three data structures: a `distances` dictionary (shortest known distance from start to each node), a `previous` dictionary (which node we came from to reach each node), and a `visited` list (nodes we have finished processing). At each step, the algorithm picks the unvisited node with the smallest known distance, updates the distances of its unvisited neighbors, records where each neighbor was reached from, and marks the current node as visited. After the algorithm finishes, the shortest path is reconstructed by tracing backward through the `previous` dictionary from destination to start and then reversing the result.

Students already understand graphs (Lesson 1) and can represent them as dictionaries (Lesson 2). Now they need an algorithm that systematically finds the shortest path on a graph -- especially when obstacles block the direct route. This lesson introduces Dijkstra's algorithm as that systematic method. By hand-tracing the algorithm on grids with and without blocked nodes, students internalize the mechanics before implementing them in Python in Lessons 4 and 5. The hand traces from this lesson will serve as test cases to verify their code output later.

## Learning Objectives
By the end of this lesson, students will be able to:
- Name the three data structures used by Dijkstra's algorithm: distances, previous, and visited
- Explain the purpose of each data structure
- Trace the algorithm step by step on a 3x3 grid by hand
- Pick the correct next node to visit (smallest distance, unvisited)
- Update neighbor distances correctly
- Reconstruct the shortest path from the previous dictionary
- Trace the algorithm on a grid with blocked nodes
- Compare Dijkstra's output to Manhattan's output for the same start and destination

## Key Concepts
- **Dijkstra's algorithm**: A systematic method for finding the shortest path from a starting node to any other node in a graph. It works by exploring outward from the start, always visiting the nearest unvisited node next, and updating distances as it goes. Invented by Edsger Dijkstra in 1956.
- **Distances dictionary**: A dictionary that stores the shortest known distance from the start node to every other node. Initially, the start node has distance 0 and all other nodes have distance infinity (or a very large number like 999999). Distances get updated as the algorithm discovers shorter paths.
- **Previous dictionary**: A dictionary that stores, for each node, which node we came from to reach it on the shortest path. Used to reconstruct the actual path after the algorithm finishes. The start node has `previous = None` because nothing comes before it.
- **Visited list**: A list of nodes that have been fully processed. Once a node is visited, its shortest distance is finalized and will not change. The algorithm only considers unvisited nodes when picking the next node to process.
- **Path reconstruction**: The process of building the actual shortest path by starting at the destination, looking up `previous[destination]` to find the node before it, and repeating until reaching the start (where `previous = None`). The resulting list is then reversed to go from start to destination.

## Materials Required
- Printed tracing worksheets (3x3 and 4x4 grids with tables for distances, previous, and visited)
- Pencils, erasers, and colored markers
- Graph drawings and dictionaries from Lessons 1 and 2 (for reference)
- Whiteboard or projector for step-by-step demonstration
- Optional: large magnetic whiteboard grid for classroom demonstration
- No computers needed -- this is a paper lesson

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 8 min
**For 3-hour sessions:** 10-12 min

1. **Hook: How Does GPS Find the Fastest Route?**
   - Ask: "When Google Maps gives you directions, how does it know the shortest route -- especially with road closures?"
   - Discussion: It doesn't try every possible route -- that would take forever on a real map with millions of roads. Instead, it uses an algorithm similar to what we'll learn today.
   - "The algorithm is called **Dijkstra's algorithm**, named after Edsger Dijkstra, who invented it in 1956. Variations of it still power GPS navigation today."
   - Show the basic idea: Start at your location. Explore nearby intersections first. Spread outward, always picking the closest unvisited intersection. Stop when you reach the destination.

2. **Why Manhattan Isn't Enough (Revisited)**
   - Quick reminder from Lesson 1: Manhattan always goes rows-first, columns-second. It cannot handle obstacles.
   - "In Lesson 1, you found paths around obstacles by hand. But your method was intuition -- you looked at the whole grid and guessed. We need a method so precise that a computer can follow it."
   - "That precise method is Dijkstra's algorithm. Today you'll learn it by tracing it step by step on paper. No code yet -- just the algorithm."

3. **The Three Key Data Structures**
   - Write on the board:
     - **`distances`** dictionary: Shortest known distance from start to each node
     - **`previous`** dictionary: Which node we came from to reach each node
     - **`visited`** list: Nodes we've finished processing
   - Initial setup (starting from (0, 0)):
     ```
     distances = {(0,0): 0}       -- start is distance 0
     previous  = {(0,0): None}    -- start has no previous
     visited   = []                -- nothing visited yet
     ```
   - "Every other node starts with no entry -- meaning we haven't discovered it yet."

### Guided Practice (15 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

1. **The Algorithm in One Sentence**
   - "Repeat: Pick the unvisited node with the smallest distance, visit its neighbors, mark it visited."
   - More precisely:
     1. From all unvisited nodes that have a known distance, pick the one with the **smallest** distance
     2. For each of that node's **neighbors**: if the neighbor hasn't been visited AND the new distance is shorter (or first time seen), update its distance and record where we came from
     3. Mark the current node as **visited** (done with it)
     4. Repeat until the destination is visited (or no nodes left)

2. **Walkthrough on a 3x3 Grid with (1, 1) Blocked**
   - Draw on the board:
     ```
     (0,0) --- (0,1) --- (0,2)
       |                   |
     (1,0)               (1,2)
       |                   |
     (2,0) --- (2,1) --- (2,2)
     ```
   - Goal: Find shortest path from (0, 0) to (2, 2)
   - Write the graph dictionary on the board for reference:
     ```
     (0,0): [(0,1), (1,0)]
     (0,1): [(0,0), (0,2)]
     (0,2): [(0,1), (1,2)]
     (1,0): [(0,0), (2,0)]
     (1,2): [(0,2), (2,2)]
     (2,0): [(1,0), (2,1)]
     (2,1): [(2,0), (2,2)]
     (2,2): [(2,1), (1,2)]
     ```
   - **Step 1: Visit (0, 0) -- distance 0**
     - Neighbors: (0, 1) and (1, 0)
     - (0, 1): distance = 0 + 1 = 1, previous = (0, 0)
     - (1, 0): distance = 0 + 1 = 1, previous = (0, 0)
     - Mark (0, 0) visited
     - State: distances = {(0,0): 0, (0,1): 1, (1,0): 1}, visited = [(0,0)]
   - **Step 2: Visit (0, 1) -- distance 1** (pick either node with distance 1)
     - Neighbors: (0, 0) already visited, (0, 2) unseen
     - (0, 2): distance = 1 + 1 = 2, previous = (0, 1)
     - Mark (0, 1) visited
   - **Step 3: Visit (1, 0) -- distance 1**
     - Neighbors: (0, 0) already visited, (2, 0) unseen
     - (2, 0): distance = 1 + 1 = 2, previous = (1, 0)
     - Mark (1, 0) visited
   - **Step 4: Visit (0, 2) -- distance 2**
     - Neighbors: (0, 1) visited, (1, 2) unseen
     - (1, 2): distance = 2 + 1 = 3, previous = (0, 2)
     - Mark (0, 2) visited
   - **Step 5: Visit (2, 0) -- distance 2**
     - Neighbors: (1, 0) visited, (2, 1) unseen
     - (2, 1): distance = 2 + 1 = 3, previous = (2, 0)
     - Mark (2, 0) visited
   - **Step 6: Visit (1, 2) -- distance 3** (pick either node with distance 3)
     - Neighbors: (0, 2) visited, (2, 2) unseen
     - (2, 2): distance = 3 + 1 = 4, previous = (1, 2)
     - Mark (1, 2) visited
   - **(2, 2) now has a distance. We could stop after visiting it, but let's see the result.**
   - Final distances: (0,0): 0, (0,1): 1, (0,2): 2, (1,0): 1, (1,2): 3, (2,0): 2, (2,1): 3, (2,2): 4

3. **Reconstructing the Path**
   - "The `previous` dictionary tells us how to trace back from destination to start."
   - previous: {(0,0): None, (0,1): (0,0), (0,2): (0,1), (1,0): (0,0), (1,2): (0,2), (2,0): (1,0), (2,1): (2,0), (2,2): (1,2)}
   - Trace back from (2, 2):
     - (2, 2) came from (1, 2)
     - (1, 2) came from (0, 2)
     - (0, 2) came from (0, 1)
     - (0, 1) came from (0, 0)
     - (0, 0) has previous = None -- we're at the start!
   - Backward list: [(2,2), (1,2), (0,2), (0,1), (0,0)]
   - Reverse it: [(0,0), (0,1), (0,2), (1,2), (2,2)]
   - "This is the shortest path around the blocked node (1, 1). Total: 4 steps."

4. **Comparing to Manhattan**
   - Without obstacles: Manhattan from (0,0) to (2,2) = (0,0) -> (1,0) -> (2,0) -> (2,1) -> (2,2) = 4 steps
   - With (1,1) blocked: Manhattan's path still works by coincidence (it goes rows-first, which avoids (1,1))
   - But try (0,0) to (2,2) with (1,0) blocked instead: Manhattan goes (0,0) -> (1,0) -- BLOCKED. Dijkstra finds (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) = 4 steps.
   - Key insight: When no obstacles exist, Dijkstra finds a path of the same LENGTH as Manhattan. The actual path may differ, but the step count matches. When obstacles exist, Dijkstra finds the best detour.

### Independent Practice (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

**Exercise 1: Trace Dijkstra on a 3x3 Grid with (0, 1) Blocked**
- Goal: Trace the full algorithm from (0, 0) to (0, 2)
- Grid:
  ```
  (0,0)           (0,2)
    |               |
  (1,0) --- (1,1) --- (1,2)
    |         |       |
  (2,0) --- (2,1) --- (2,2)
  ```
- Fill in a step-by-step table:

  | Step | Visit Node | Distance | Neighbors Updated | Visited So Far |
  |---|---|---|---|---|
  | 1 | (0,0) | 0 | (1,0)=1 | [(0,0)] |
  | 2 | | | | |
  | 3 | | | | |
  | ... | | | | |

- Then reconstruct the path from (0, 0) to (0, 2) using the previous dictionary
- Count the steps and compare to Manhattan distance

**Exercise 2: Trace Dijkstra on a 3x3 Grid with No Blocked Nodes**
- Goal: Verify that Dijkstra produces a path of the same length as Manhattan when nothing is blocked
- Use the full 3x3 grid (no blocks)
- Find shortest path from (0, 0) to (2, 2)
- Compare: Manhattan distance is 4 steps. Does Dijkstra also find 4 steps?
- Note: The actual path may be different, but the length should be the same

**Exercise 3: Trace with Multiple Blocked Nodes**
- Goal: Handle a more complex obstacle configuration
- Use a 4x4 grid with (1, 1) and (2, 2) blocked
- Find shortest path from (0, 0) to (3, 3)
- This requires more steps -- use a larger table
- What is the shortest path length? Is it longer than the Manhattan distance of 6?

**Exercise 4: Challenge -- When Is a Destination Unreachable?**
- Goal: Discover what happens when the algorithm cannot reach the destination
- On a 3x3 grid, find a set of blocked nodes that makes (2, 2) unreachable from (0, 0)
- What happens to the algorithm? (It runs out of unvisited nodes with known distances before reaching the destination)
- How many nodes do you need to block? (Hint: think about which nodes are "chokepoints")

### Assessment

**Formative (during lesson)**:
- Can students name the three data structures and explain their purposes?
- Can students pick the correct next node (smallest distance among unvisited)?
- Can students correctly update neighbor distances (current distance + 1)?
- Can students skip already-visited nodes when updating neighbors?
- Can students reconstruct the path by tracing backward through the previous dictionary?
- Can students explain why the path must be reversed?

**Summative (worksheet/exit ticket)**:
1. Name the three data structures used by Dijkstra's algorithm and explain what each stores.
2. In Dijkstra's algorithm, how do you decide which node to visit next?
3. On a 3x3 grid with (1, 0) blocked, trace Dijkstra from (0, 0) to (2, 0). Show the state of distances and visited after each step.
4. Given this previous dictionary: `{(0,0): None, (0,1): (0,0), (1,1): (0,1), (2,1): (1,1)}`, reconstruct the path from (0, 0) to (2, 1).
5. Why does Dijkstra find the same path length as Manhattan when there are no obstacles?

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "Dijkstra tries every possible path" | Dijkstra is efficient: it visits each node at most once. It explores outward from the start, always choosing the nearest unvisited node. It does NOT generate all possible paths and compare them. |
| "You visit the node closest to the destination" | You visit the unvisited node with the smallest DISTANCE FROM THE START, not the one closest to the destination. The algorithm has no concept of "distance to destination" -- it only knows distances from the start. |
| "If two nodes have the same distance, the algorithm fails" | If two unvisited nodes have the same distance, you can pick either one. The algorithm still works correctly. The final path length will be the same regardless of which you pick first. |
| "Blocked nodes have distance infinity in the distances dictionary" | Blocked nodes are NOT in the graph at all. They don't appear in the graph dictionary, so the algorithm never encounters them. They don't have a distance -- they simply don't exist. |
| "The previous dictionary gives you the path in order" | The previous dictionary gives you the path BACKWARD. You must trace from destination to start and then REVERSE the list to get the correct forward path. |
| "Dijkstra always finds a shorter path than Manhattan" | When there are no obstacles, Dijkstra finds a path of the SAME length as Manhattan. Dijkstra's advantage is that it works WITH obstacles, not that it finds shorter paths on clear grids. |

## Differentiation

**For struggling students**:
- Provide pre-filled tables with the first two steps already completed -- students continue from there
- Use a 2x2 grid (only 4 nodes) for the first trace to minimize complexity
- Color-code the data structures: blue for distances, green for previous, red for visited
- Work through the guided practice a second time with a different blocked node before starting independent work
- Provide a step-by-step checklist: (1) find smallest unvisited, (2) check each neighbor, (3) update if shorter, (4) mark visited
- Allow students to work in pairs on the tracing exercises

**For advanced students**:
- Trace Dijkstra on a 5x5 grid with 3+ blocked nodes
- Think about efficiency: How many times does the algorithm look at each node? How could you make the "find minimum" step faster? (This previews priority queues, which they don't need to implement)
- Research: What is A* search, and how does it improve on Dijkstra's by considering distance to the destination?
- Consider: What would change if edges had different weights (costs)? How would the distance update step change?
- Prove: Why is it safe to mark a node as "visited" permanently? Why will we never find a shorter path to it later? (Because we always visit the minimum-distance node first)

## Materials & Code Examples

### Tracing Table Template
```
Grid: 3x3 with (1,1) blocked
Start: (0,0)  Destination: (2,2)

Graph:
(0,0) --- (0,1) --- (0,2)
  |                   |
(1,0)               (1,2)
  |                   |
(2,0) --- (2,1) --- (2,2)

Step | Visit    | Dist | Update Neighbors          | distances                    | visited
-----|----------|------|---------------------------|------------------------------|--------
  1  | (0,0)    |  0   | (0,1)=1, (1,0)=1         | (0,0):0 (0,1):1 (1,0):1     | [(0,0)]
  2  | (0,1)    |  1   | (0,2)=2                   | ... (0,2):2                  | [(0,0),(0,1)]
  3  | (1,0)    |  1   | (2,0)=2                   | ... (2,0):2                  | [...,(1,0)]
  4  | (0,2)    |  2   | (1,2)=3                   | ... (1,2):3                  | [...,(0,2)]
  5  | (2,0)    |  2   | (2,1)=3                   | ... (2,1):3                  | [...,(2,0)]
  6  | (1,2)    |  3   | (2,2)=4                   | ... (2,2):4                  | [...,(1,2)]
  7  | (2,1)    |  3   | (none new)                | (no changes)                 | [...,(2,1)]
  8  | (2,2)    |  4   | DONE - destination visited | final                        | [...,(2,2)]

Previous dictionary:
(0,0): None
(0,1): (0,0)
(0,2): (0,1)
(1,0): (0,0)
(1,2): (0,2)
(2,0): (1,0)
(2,1): (2,0)
(2,2): (1,2)

Path reconstruction:
(2,2) <- (1,2) <- (0,2) <- (0,1) <- (0,0)
Reverse: (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2)
Steps: 4
```

### Comparison: Manhattan vs. Dijkstra
```
3x3 grid, (1,0) blocked.  Start: (0,0)  Destination: (2,0)

Manhattan path: (0,0) -> (1,0) -> (2,0)  -- FAILS at (1,0)!

Dijkstra path:  (0,0) -> (0,1) -> (1,1) -> (2,1) -> (2,0)  = 4 steps

Manhattan distance (no obstacles): 2
Dijkstra shortest path (with obstacle): 4
```

### Blank Tracing Table (for student worksheets)
```
Grid: ___x___ with _______ blocked
Start: _______  Destination: _______

Step | Visit    | Dist | Update Neighbors          | Visited So Far
-----|----------|------|---------------------------|----------------------------
  1  |          |      |                           |
  2  |          |      |                           |
  3  |          |      |                           |
  4  |          |      |                           |
  5  |          |      |                           |
  6  |          |      |                           |
  7  |          |      |                           |
  8  |          |      |                           |

Previous dictionary:
_____________
_____________
_____________

Path reconstruction:
_____ <- _____ <- _____ <- _____ <- _____
Reverse: _____ -> _____ -> _____ -> _____ -> _____
Steps: ____
```

### Preview: What the Code Will Look Like (show but do not implement)
```python
# This is what you'll build in Lessons 4 and 5:
class Dijkstra:
    def __init__(self, start, blocked):
        self.start = start
        self.blocked = blocked
        self.graph = self.build_graph()

    def compute_path(self, destination):
        # Initialize distances, previous, visited
        # Main loop: find min, update neighbors, mark visited
        # Reconstruct and return path
        pass
```

## Teaching Notes
- **This is the hardest conceptual lesson in Module 5.** Take it slow. The algorithm has multiple moving parts, and students need to see each step clearly before moving on. If you have a 3-hour session, spend extra time on the guided practice walkthrough.
- **Use the board extensively.** Write out the full state (distances, previous, visited) after EVERY step. Students need to see how the data structures change. Use colored markers: one color for the node being visited, another for updated distances, another for the path being traced.
- **Ask "which node do we visit next?" at every step.** Make students answer before you proceed. This is the core decision in the algorithm, and they need to practice it.
- **The "find minimum" step is the trickiest.** Students often want to visit the node closest to the destination, or the most recently updated node. Reinforce: we visit the unvisited node with the smallest distance FROM THE START.
- **Emphasize that blocked nodes simply don't exist.** They're not in the graph dictionary, so the algorithm never encounters them. It doesn't "skip" them -- they're just absent. This connects back to the `remove_blocked` function from Lesson 2.
- **Path reconstruction can feel backwards.** Some students find it confusing that we trace from destination to start and then reverse. Walk through it slowly and connect it to real life: "If you asked someone 'how did you get here?' they'd tell you their steps. You'd hear the end first and the beginning last."
- **Save the completed traces.** Students will use these as test cases in Lessons 4 and 5 to verify their code produces the same results.
- **The comparison to Manhattan is important for motivation.** Students should see that Dijkstra is not "better" than Manhattan -- it's "more capable." When the grid is clear, both find the same-length path. Dijkstra's advantage is handling obstacles.

## Connections to Next Lessons
- **Lesson 4** will design the Dijkstra class with `__init__`, `build_graph`, and a `compute_path` method signature. Students will structure the class but not yet implement the full algorithm.
- **Lesson 5** will implement `compute_path` -- translating the hand-traced steps from this lesson into Python code. Students will verify their code by comparing output to their hand traces.
- **Lesson 6** will test Dijkstra alongside Manhattan and swap it into the Navigator class. The shared `compute_path` interface means Navigator works with both pathfinders.
- The three data structures introduced here (distances, previous, visited) map directly to Python variables in the implementation.
