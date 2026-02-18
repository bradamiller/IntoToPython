# Lesson 1: The Grid as a Graph

## Overview
Students learn to see the familiar grid of intersections as a **graph** -- a collection of nodes connected by edges. This is a conceptual lesson with no Python coding. Students work with paper, pencils, and the physical grid to understand graph terminology (nodes, edges, neighbors), discover why the Manhattan algorithm from Module 4 fails when intersections are blocked, and practice finding shortest paths by hand around obstacles. By the end of the lesson, students can draw any grid as a graph, remove blocked nodes, and trace shortest paths that detour around obstacles.

This lesson is the bridge between Module 4's Manhattan pathfinding and Module 5's Dijkstra's algorithm. Students already know how to navigate a clear grid using (row, column) coordinates, tuples, lists, and the Manhattan class. Now they confront the reality that real-world grids have obstacles -- and they need a new way of thinking about the grid to handle them. The graph perspective introduced here is the foundation for dictionaries (Lesson 2), Dijkstra's algorithm (Lesson 3), and the Dijkstra class (Lessons 4-5).

## Learning Objectives
By the end of this lesson, students will be able to:
- Define graph terminology: node, edge, and neighbor
- Explain why a grid of intersections is a graph
- Draw a grid as a graph with nodes and edges on paper
- Identify why the Manhattan algorithm fails when intersections are blocked
- Remove a blocked node and all its edges from a graph drawing
- Find the shortest path by hand on a graph with blocked nodes
- Count the number of steps in a path and compare to Manhattan distance

## Key Concepts
- **Graph**: A collection of **nodes** (points) connected by **edges** (lines between points). A graph describes what connects to what.
- **Node (vertex)**: A single point in the graph. On our grid, each intersection is a node. A node is identified by its coordinate, such as (1, 2).
- **Edge**: A connection between two adjacent nodes. On our grid, an edge exists between any two intersections that are directly next to each other (up, down, left, or right -- no diagonals).
- **Neighbors**: The nodes directly connected to a given node by an edge. On a grid interior, a node has 4 neighbors. On an edge, 3. On a corner, 2.
- **Blocked node**: An intersection that is impassable. When a node is blocked, it is removed from the graph along with all its edges, meaning no paths can pass through it.
- **Unweighted graph**: A graph where every edge has the same cost (1 step). Our grid is unweighted because moving from any intersection to an adjacent one always costs 1 step.

## Materials Required
- Grid worksheets (blank 3x3 and 4x4 grids for drawing graphs)
- Pencils, erasers, and colored markers
- Whiteboard or projector for demonstrations
- Hand-traced path worksheets from Module 4, Lesson 4 (for comparison)
- Optional: physical grid (tape on floor) with some intersections marked as blocked
- No computers needed -- this is a paper lesson

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 8 min
**For 3-hour sessions:** 10-12 min

1. **Hook: What If the Road Is Closed?**
   - Ask: "You're driving to school and your usual route is blocked by construction. What do you do?"
   - Discussion: You find a detour. GPS apps like Google Maps reroute you automatically. The robot needs to do the same thing.
   - Reveal the problem: "Our Manhattan algorithm always goes rows first, then columns. What happens if an intersection on that path is blocked?"
   - Show on the board:
     ```
     Manhattan path from (0,0) to (2,2):
     (0,0) -> (1,0) -> (2,0) -> (2,1) -> (2,2)
                ^
           What if (1,0) is BLOCKED?
     ```
   - Ask: "Can the Manhattan algorithm go around the obstacle?" (No. It only knows one strategy: rows first, then columns. It has no concept of obstacles.)
   - "Today we'll learn a new way to think about the grid that lets us handle obstacles. It's called a **graph**."

2. **What Is a Graph?**
   - A graph is a collection of **nodes** connected by **edges**.
   - Real-world examples students already know:
     - **Road map**: Intersections are nodes, streets are edges
     - **Social network**: People are nodes, friendships are edges
     - **Airline routes**: Airports are nodes, flights are edges
   - Key insight: A graph describes *what connects to what*. It doesn't care about exact physical positions -- only connections.
   - "Our grid IS a graph. Every intersection is a node. Every path between adjacent intersections is an edge. We just need to see it that way."

3. **Graph Vocabulary**
   - Write on the board:
     - **Node** (also called vertex): A point in the graph. For us, an intersection like (1, 2).
     - **Edge**: A connection between two adjacent nodes. For us, the line between (0, 0) and (0, 1).
     - **Neighbors**: The nodes directly connected to a given node by edges.
   - Quick check: "If (1, 1) is a node on a 3x3 grid, what are its neighbors?" Answer: (0, 1), (2, 1), (1, 0), (1, 2) -- up, down, left, right.

### Guided Practice (15 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 20 min

1. **Drawing a 3x3 Grid as a Graph**
   - Draw the following on the board:
     ```
     (0,0) --- (0,1) --- (0,2)
       |         |         |
     (1,0) --- (1,1) --- (1,2)
       |         |         |
     (2,0) --- (2,1) --- (2,2)
     ```
   - Point out: Each `---` and `|` is an edge. Each coordinate is a node.
   - Ask students to count:
     - "How many nodes?" (9)
     - "How many neighbors does (0,0) have?" (2 -- right and below)
     - "How many neighbors does (1,1) have?" (4 -- up, down, left, right)
     - "How many neighbors does (0,1) have?" (3 -- left, right, below)
   - Rule: Corner nodes have 2 neighbors, edge nodes have 3, interior nodes have 4.

2. **Blocking a Node**
   - "When an intersection is blocked, we remove it from the graph. That means we erase the node AND all its edges."
   - Block node (1, 1) on the 3x3 grid:
     ```
     (0,0) --- (0,1) --- (0,2)
       |                   |
     (1,0)               (1,2)
       |                   |
     (2,0) --- (2,1) --- (2,2)
     ```
   - Ask: "What changed?"
     - Node (1, 1) is gone
     - (0, 1) lost a neighbor -- it used to connect down to (1, 1), now it only connects to (0, 0) and (0, 2)
     - (1, 0) lost a neighbor -- now only connects to (0, 0) and (2, 0)
     - (2, 1) lost a neighbor -- now only connects to (2, 0) and (2, 2)
     - (1, 2) lost a neighbor -- now only connects to (0, 2) and (2, 2)

3. **Finding a Path Around the Obstacle**
   - "Find the shortest path from (0,0) to (2,2) with (1,1) blocked."
   - Manhattan would try: (0,0) -> (1,0) -> (2,0) -> (2,1) -> (2,2) -- 4 steps. This actually works because it does not pass through (1, 1).
   - But ask: "What about from (0,0) to (2,2) going the other way -- through (0,1)?"
     - (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -- also 4 steps
   - Now block (1,0) instead:
     ```
     (0,0) --- (0,1) --- (0,2)
                |         |
              (1,1) --- (1,2)
       |        |         |
     (2,0) --- (2,1) --- (2,2)
     ```
   - "Find the shortest path from (0,0) to (2,0)."
     - Manhattan path: (0,0) -> (1,0) -> (2,0) -- BLOCKED at (1,0)!
     - Graph path: (0,0) -> (0,1) -> (1,1) -> (2,1) -> (2,0) -- 4 steps, goes around
   - Key insight: Manhattan distance from (0,0) to (2,0) is 2, but with the obstacle the actual shortest path is 4. **Obstacles make paths longer.**

4. **Weighted vs. Unweighted**
   - Briefly mention: In some graphs, edges have different costs (a highway might be faster than a side street). These are called **weighted** graphs.
   - Our grid is **unweighted**: every edge costs 1 step. Moving from (0,0) to (0,1) costs the same as (1,1) to (2,1).
   - This makes our problem simpler, but Dijkstra's algorithm works on both.

### Independent Practice (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

**Exercise 1: Draw a 4x4 Grid as a Graph**
- Goal: Draw all 16 nodes and their connecting edges on paper
- Steps:
  1. Draw the 4x4 grid as a graph with nodes (0,0) through (3,3) and all edges
  2. Count the total number of nodes (16)
  3. Label one corner node, one edge node, and one interior node
  4. Write the neighbor list for each: how many neighbors does each have?
- Success criteria: All 16 nodes are correctly placed with appropriate edges connecting adjacent nodes

**Exercise 2: Block Nodes and Redraw**
- Goal: Remove blocked nodes and find paths around them
- Steps:
  1. On your 4x4 grid, mark (1,1) and (2,2) as blocked
  2. Redraw the graph with those nodes and their edges removed
  3. List the neighbors of (1,0) after blocking. How many did it lose?
  4. List the neighbors of (2,1) after blocking. How many did it lose?
- Success criteria: Blocked nodes are fully removed, no edges connect to or from blocked nodes

**Exercise 3: Find Shortest Paths by Hand**
- Goal: Trace shortest paths around obstacles on the modified 4x4 grid
- Using the graph from Exercise 2 (with (1,1) and (2,2) blocked), find the shortest path:
  1. From (0,0) to (3,3) -- List every node visited and count the steps
  2. From (0,0) to (2,1) -- List every node visited and count the steps
  3. From (3,0) to (0,3) -- List every node visited and count the steps
- For each path, also calculate the Manhattan distance (without obstacles) and compare
- Key question: Is the path with obstacles longer than the Manhattan distance? Why?

**Exercise 4: Challenge**
- Goal: Discover when obstacles force a longer path and when they do not
- Questions:
  1. On the 4x4 grid with (1,1) and (2,2) blocked, find a start/destination pair where the shortest path is the SAME length as the Manhattan distance
  2. Find a start/destination pair where the shortest path is LONGER than the Manhattan distance
  3. Can blocking a node ever make a path SHORTER? Why or why not?

### Assessment

**Formative (during lesson)**:
- Can students correctly identify nodes, edges, and neighbors on a grid graph?
- Can students remove a blocked node and all its edges from a drawing?
- Can students trace a path that avoids blocked nodes?
- Can students count the number of steps in a path correctly?
- Can students explain why Manhattan pathfinding fails with obstacles?

**Summative (worksheet/exit ticket)**:
1. Define: What is a node? What is an edge? What is a neighbor?
2. On a 3x3 grid, how many neighbors does the node (0, 2) have? Name them.
3. If (1, 0) is blocked on a 3x3 grid, which nodes lose a neighbor? How do their neighbor counts change?
4. Why can't the Manhattan algorithm handle blocked intersections?
5. Draw the shortest path from (0, 0) to (2, 0) on a 3x3 grid with (1, 0) blocked. How many steps does it take?

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "A graph is like a bar chart or line chart" | In computer science, a graph is a network of nodes and edges -- completely different from a data visualization chart. The word has two different meanings. |
| "Blocked means the node is still there but you can't use it" | A blocked node is completely removed from the graph, along with ALL its edges. It does not exist. No node lists it as a neighbor. |
| "Removing a blocked node only affects that node" | Removing a node also removes all edges connected to it, which reduces the neighbor count of every adjacent node. Blocking one node affects its neighbors too. |
| "The shortest path around an obstacle is always 2 steps longer" | The extra distance depends on where the obstacle is relative to the path. Sometimes it adds 2 steps, sometimes more, and sometimes the obstacle is not on the shortest path at all so it adds nothing. |
| "Manhattan distance still tells you the shortest path with obstacles" | Manhattan distance is the shortest possible distance with NO obstacles. With blocked nodes, the actual shortest path may be longer. Manhattan distance becomes a lower bound, not the answer. |
| "Diagonal connections exist on the grid" | Nodes connect only to nodes directly above, below, left, or right. There are no diagonal edges. This is the same constraint as Module 4. |

## Differentiation

**For struggling students**:
- Start with a 2x2 grid (only 4 nodes) to practice drawing nodes and edges before moving to 3x3 or 4x4
- Provide pre-drawn graph diagrams and ask students to identify nodes, edges, and neighbors rather than drawing from scratch
- Use color coding: one color for nodes, another for edges, a third to cross out blocked nodes and their edges
- Pair with a stronger student for the pathfinding exercises
- Provide a step-by-step checklist: (1) draw all nodes, (2) draw all edges, (3) cross out blocked nodes, (4) erase edges to blocked nodes, (5) find the path

**For advanced students**:
- Work with a larger grid (5x5 or 6x6) and multiple blocked nodes
- Challenge: Is there a grid configuration where blocking nodes makes it impossible to reach the destination? Draw one.
- Research: What are some other famous graph algorithms besides Dijkstra's? (BFS, DFS, A*)
- Think ahead: How would you represent this graph in Python? What data structure could store "node X connects to nodes Y and Z"? (This previews dictionaries in Lesson 2.)
- Calculate: On a 4x4 grid, how many total edges exist? (24 edges on the full grid)

## Materials & Code Examples

### 3x3 Grid as a Graph (for Board Drawing)
```
(0,0) --- (0,1) --- (0,2)
  |         |         |
(1,0) --- (1,1) --- (1,2)
  |         |         |
(2,0) --- (2,1) --- (2,2)
```

Each intersection is a **node**. Each line is an **edge**.

### 3x3 Grid with (1,1) Blocked
```
(0,0) --- (0,1) --- (0,2)
  |                   |
(1,0)               (1,2)
  |                   |
(2,0) --- (2,1) --- (2,2)
```

Node (1,1) and all its edges are removed.

### 4x4 Grid as a Graph (for Worksheet)
```
(0,0) --- (0,1) --- (0,2) --- (0,3)
  |         |         |         |
(1,0) --- (1,1) --- (1,2) --- (1,3)
  |         |         |         |
(2,0) --- (2,1) --- (2,2) --- (2,3)
  |         |         |         |
(3,0) --- (3,1) --- (3,2) --- (3,3)
```

### Neighbor Count Reference
```
Node Type       Example   Neighbors   Count
---------       -------   ---------   -----
Corner          (0,0)     (0,1), (1,0)                    2
Edge            (0,1)     (0,0), (0,2), (1,1)             3
Interior        (1,1)     (0,1), (2,1), (1,0), (1,2)     4
```

### Path Comparison: Manhattan vs. Graph Path
```
3x3 grid, (1,0) blocked.  Start: (0,0)  Destination: (2,0)

Manhattan path (no obstacles): (0,0) -> (1,0) -> (2,0)         = 2 steps
Manhattan path (with obstacle): FAILS at (1,0)!

Graph path (around obstacle):  (0,0) -> (0,1) -> (1,1) -> (2,1) -> (2,0) = 4 steps

Manhattan distance: 2
Actual shortest path with obstacle: 4
```

### Preview: Representing Graphs in Python (show but do not code)
```python
# Next lesson, we'll store this graph in Python using a dictionary:
graph = {
    (0, 0): [(0, 1), (1, 0)],
    (0, 1): [(0, 0), (0, 2)],
    # ... one entry per node, listing its neighbors
}
# Then we can ask: "What are the neighbors of (0,0)?"
print(graph[(0, 0)])    # [(0, 1), (1, 0)]
```

## Teaching Notes
- **This lesson is the "why" for Dijkstra's algorithm.** Before students can appreciate Dijkstra's, they need to feel the limitation of Manhattan pathfinding. Spend time on the hook -- make the failure of Manhattan vivid and concrete.
- **Draw big, clear graphs.** Use the entire whiteboard. Have students come up and draw edges, cross out blocked nodes, and trace paths with colored markers. The physical act of drawing reinforces the concepts.
- **Emphasize that a graph is about connections, not positions.** Students may think a graph is just another way to draw a grid. Help them see that the graph captures WHICH nodes connect to which -- and that removing a node changes those connections for its neighbors.
- **The word "graph" is confusing.** Students know "graph" from math class as a bar chart or scatter plot. Clarify immediately that in computer science, "graph" means a network of nodes and edges. These are completely different uses of the same word.
- **Let students struggle with pathfinding.** When they try to find paths around obstacles, resist the urge to give the answer. Let them explore, backtrack, and discover for themselves. This struggle motivates the need for an algorithm (Dijkstra's) that does it systematically.
- **Connect to GPS.** Students use Google Maps and Waze every day. These apps use graph algorithms similar to Dijkstra's to find routes around traffic and road closures. This is not an abstract concept -- it powers technology they rely on.
- **Save the worksheets.** Students will reference their hand-drawn graphs and paths in Lesson 3 when they hand-trace Dijkstra's algorithm, and in Lessons 4-5 when they verify their code output.

## Connections to Next Lessons
- **Lesson 2** will introduce **dictionaries** -- Python's key-value data structure that can represent a graph in code. The graph students drew on paper today will become a Python dictionary: `{(0,0): [(0,1), (1,0)], ...}`
- **Lesson 3** will teach **Dijkstra's algorithm** -- the systematic method for finding shortest paths on a graph with obstacles. Students will hand-trace the algorithm on the same grids they drew today.
- **Lessons 4-5** will implement Dijkstra's algorithm as a Python class with the same `compute_path` interface as the Manhattan class from Module 4, so the Navigator class works with both.
- The graph vocabulary introduced here (nodes, edges, neighbors) is used in every remaining lesson of Module 5.
