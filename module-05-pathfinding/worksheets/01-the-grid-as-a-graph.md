# Lesson 1 Worksheet: The Grid as a Graph

**Name:** ________________________
**Date:** ________________________

---

## Part 1: Nodes on a 3x3 Grid

A **graph** represents locations as **nodes** and connections between them as **edges**. Our XRP grid can be thought of as a graph where each intersection is a node and each path between adjacent intersections is an edge.

Draw the 3x3 grid below as a graph. Write each node as its (row, col) coordinate inside a circle, and draw lines (edges) between neighbors.

```
Nodes:

(0,0) --- (0,1) --- (0,2)
  |         |         |
  |         |         |
(1,0) --- (1,1) --- (1,2)
  |         |         |
  |         |         |
(2,0) --- (2,1) --- (2,2)
```

**How many nodes are in a 3x3 grid graph?** __________

**How many edges are in a 3x3 grid graph?** __________

*(Hint: count each line segment once.)*

---

## Part 2: Identifying Neighbors

In a graph, two nodes are **neighbors** if they share an edge (they are directly connected).

List all neighbors for each node on the 3x3 grid:

| Node | Neighbors |
|---|---|
| (0, 0) | __________________________________________ |
| (0, 1) | __________________________________________ |
| (0, 2) | __________________________________________ |
| (1, 0) | __________________________________________ |
| (1, 1) | __________________________________________ |
| (1, 2) | __________________________________________ |
| (2, 0) | __________________________________________ |
| (2, 1) | __________________________________________ |
| (2, 2) | __________________________________________ |

**Which node has the most neighbors?** __________

**How many neighbors does a corner node have?** __________

**How many neighbors does an edge node (non-corner, on the border) have?** __________

**How many neighbors does a center node have?** __________

---

## Part 3: A 4x4 Grid Graph

Now consider a 4x4 grid. You do not need to draw the full graph, but answer these questions:

**How many nodes are in a 4x4 grid graph?** __________

List all neighbors of node **(2, 1)** on a 4x4 grid:

| Direction | Neighbor |
|---|---|
| Up | (______, ______) |
| Down | (______, ______) |
| Left | (______, ______) |
| Right | (______, ______) |

List all neighbors of node **(0, 3)** on a 4x4 grid:

| Direction | Neighbor |
|---|---|
| Up | __________________ |
| Down | (______, ______) |
| Left | (______, ______) |
| Right | __________________ |

---

## Part 4: Blocked Nodes

Sometimes intersections on the grid are **blocked** by obstacles. A blocked node cannot be visited, and its edges are effectively removed from the graph.

On the 3x3 grid below, node **(1, 1)** is blocked (marked with X). Cross out the edges that connect to the blocked node.

```
(0,0) --- (0,1) --- (0,2)
  |         |         |
  |         |         |
(1,0) --- [X X] --- (1,2)
  |         |         |
  |         |         |
(2,0) --- (2,1) --- (2,2)
```

**After blocking (1, 1), list the neighbors of (0, 1):**

____________________________________________________________________

**After blocking (1, 1), list the neighbors of (1, 0):**

____________________________________________________________________

**After blocking (1, 1), list the neighbors of (1, 2):**

____________________________________________________________________

---

## Part 5: Finding Shortest Paths by Hand

On the 3x3 grid with NO blocked nodes, find the shortest path from **(0, 0)** to **(2, 2)**.

Write your path as a sequence of nodes:

(0, 0) -> __________ -> __________ -> __________ -> (2, 2)

**How many steps (edges) does this path take?** __________

**Is there more than one shortest path?** YES / NO

**If yes, write a different shortest path:**

(0, 0) -> __________ -> __________ -> __________ -> (2, 2)

---

## Part 6: Shortest Path Around an Obstacle

Now find the shortest path from **(0, 0)** to **(2, 2)** on the 3x3 grid with **(1, 1) blocked**.

```
(0,0) --- (0,1) --- (0,2)
  |                   |
  |                   |
(1,0)     [X X]     (1,2)
  |                   |
  |                   |
(2,0) --- (2,1) --- (2,2)
```

Write the shortest path:

(0, 0) -> __________ -> __________ -> __________ -> __________ -> (2, 2)

**How many steps does this path take?** __________

**How many extra steps did the obstacle add compared to Part 5?** __________

---

## Part 7: Manhattan Distance vs. Actual Path Length

The **Manhattan distance** is the number of steps if you could walk straight through everything (no obstacles). The **actual shortest path** might be longer if obstacles are in the way.

Fill in the table for the 3x3 grid with **(1, 1) blocked**:

| Start | End | Manhattan Distance | Shortest Path Length (with obstacle) | Difference |
|---|---|---|---|---|
| (0, 0) | (2, 2) | __________ | __________ | __________ |
| (0, 0) | (2, 1) | __________ | __________ | __________ |
| (0, 0) | (1, 2) | __________ | __________ | __________ |
| (0, 1) | (2, 1) | __________ | __________ | __________ |
| (1, 0) | (1, 2) | __________ | __________ | __________ |

**When is the Manhattan distance equal to the shortest path length?**

____________________________________________________________________

**When is the shortest path length greater than the Manhattan distance?**

____________________________________________________________________

---

## Reflection

**Why is thinking of the grid as a graph helpful for finding paths around obstacles?**

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

---

**Next Lesson:** We'll learn about **dictionaries** — Python's data structure for representing graphs in code!
