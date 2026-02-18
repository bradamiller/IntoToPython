# Lesson 3 Worksheet: Dijkstra's Algorithm — The Concept

**Name:** ________________________
**Date:** ________________________

---

## Part A: Graph Vocabulary

Define each term in your own words and give an example from a 3x3 grid.

**1. Node:**

____________________________________________________________________

Example: ____________________

**2. Edge:**

____________________________________________________________________

Example: ____________________

**3. Neighbor:**

____________________________________________________________________

Example: ____________________

**4. Blocked Node:**

____________________________________________________________________

Example: ____________________

**5. True or False:**

| Statement | T/F |
|---|---|
| A blocked node can be visited by the robot | __________ |
| Two diagonal nodes are neighbors on our grid | __________ |
| A corner node has exactly 2 neighbors | __________ |
| Removing a blocked node also removes its edges | __________ |
| Every node on a 3x3 grid has 4 neighbors | __________ |

---

## Part B: Hand-Trace Dijkstra on a 3x3 Grid (No Obstacles)

Dijkstra's algorithm finds the shortest path by visiting the closest unvisited node first, updating distances to its neighbors, and repeating until the destination is reached.

**Grid (no obstacles):**

```
(0,0) --- (0,1) --- (0,2)
  |         |         |
(1,0) --- (1,1) --- (1,2)
  |         |         |
(2,0) --- (2,1) --- (2,2)
```

**Start:** (0, 0)    **Destination:** (2, 2)

**Initial distances** (all nodes start at infinity except the start node which is 0):

| Node | Distance |
|---|---|
| (0, 0) | 0 |
| (0, 1) | INF |
| (0, 2) | INF |
| (1, 0) | INF |
| (1, 1) | INF |
| (1, 2) | INF |
| (2, 0) | INF |
| (2, 1) | INF |
| (2, 2) | INF |

**Trace the algorithm step by step.** At each step, pick the unvisited node with the smallest distance, mark it visited, and update its neighbors.

**Step 1:** Visit node __________ (distance = __________)

Neighbors to update: __________________________________________

Updated distances:

| Node | Distance | Previous |
|---|---|---|
| (0, 1) | __________ | __________ |
| (1, 0) | __________ | __________ |

**Step 2:** Visit node __________ (distance = __________)

*(There may be a tie. Pick either one.)*

Neighbors to update: __________________________________________

Updated distances: __________________________________________

**Step 3:** Visit node __________ (distance = __________)

Neighbors to update: __________________________________________

Updated distances: __________________________________________

**Step 4:** Visit node __________ (distance = __________)

Neighbors to update: __________________________________________

Updated distances: __________________________________________

**Continue until you reach (2, 2).**

**Step 5:** Visit node __________ (distance = __________)

**Final shortest path:** (0, 0) -> __________ -> __________ -> __________ -> (2, 2)

**Path length (number of edges):** __________

---

## Part C: Hand-Trace Dijkstra on a 3x3 Grid with (1,1) Blocked

**Grid with (1,1) blocked:**

```
(0,0) --- (0,1) --- (0,2)
  |                   |
(1,0)     [X X]     (1,2)
  |                   |
(2,0) --- (2,1) --- (2,2)
```

**Start:** (0, 0)    **Destination:** (2, 2)

**Nodes in graph (8 nodes — (1,1) is excluded):**

Fill in the initial distance table:

| Node | Distance | Visited? |
|---|---|---|
| (0, 0) | __________ | __________ |
| (0, 1) | __________ | __________ |
| (0, 2) | __________ | __________ |
| (1, 0) | __________ | __________ |
| (1, 2) | __________ | __________ |
| (2, 0) | __________ | __________ |
| (2, 1) | __________ | __________ |
| (2, 2) | __________ | __________ |

**Step 1:** Visit node __________ (distance = __________)

Update neighbors: __________________________________________

**Step 2:** Visit node __________ (distance = __________)

Update neighbors: __________________________________________

**Step 3:** Visit node __________ (distance = __________)

Update neighbors: __________________________________________

**Step 4:** Visit node __________ (distance = __________)

Update neighbors: __________________________________________

**Step 5:** Visit node __________ (distance = __________)

Update neighbors: __________________________________________

**Step 6:** Visit node __________ (distance = __________)

**Final shortest path:**

(0, 0) -> __________ -> __________ -> __________ -> __________ -> (2, 2)

**Path length:** __________

---

## Part D: Compare Manhattan and Dijkstra Paths

Fill in the table for the 3x3 grid with **(1, 1) blocked**:

| Start | Dest | Manhattan Path | Manhattan Length | Dijkstra Path | Dijkstra Length | Same? |
|---|---|---|---|---|---|---|
| (0,0) | (2,2) | __________________________ | ______ | __________________________ | ______ | ______ |
| (0,0) | (2,1) | __________________________ | ______ | __________________________ | ______ | ______ |
| (0,1) | (2,1) | __________________________ | ______ | __________________________ | ______ | ______ |
| (1,0) | (1,2) | __________________________ | ______ | __________________________ | ______ | ______ |

**1. When does Manhattan give the same path as Dijkstra?**

____________________________________________________________________

**2. When does Manhattan fail or give a longer path?**

____________________________________________________________________

**3. Why is Dijkstra better when there are obstacles?**

____________________________________________________________________

---

## Answer Key

### Part A:
1. **Node:** A point/location on the graph. Example: (0, 0) on a 3x3 grid.
2. **Edge:** A connection between two adjacent nodes. Example: The connection between (0, 0) and (0, 1).
3. **Neighbor:** A node directly connected by an edge. Example: (0, 1) is a neighbor of (0, 0).
4. **Blocked Node:** A node that cannot be visited; it and its edges are removed. Example: (1, 1) with an obstacle.
5. True/False: F, F, T, T, F

### Part B:
- Step 1: Visit (0,0), distance=0. Update (0,1)->1, (1,0)->1
- Step 2: Visit (0,1) or (1,0), distance=1. E.g., visit (0,1), update (0,2)->2, (1,1)->2
- Step 3: Visit (1,0), distance=1. Update (2,0)->2, (1,1)->2 (already 2)
- Step 4: Visit (0,2) or (1,1) or (2,0), distance=2. E.g., visit (1,1), update (1,2)->3, (2,1)->3
- Step 5: Visit (0,2) or (2,0), distance=2. Continue until (2,2) reached with distance=4
- Path: (0,0) -> (0,1) -> (1,1) -> (2,1) -> (2,2) or (0,0) -> (1,0) -> (1,1) -> (1,2) -> (2,2), length = 4

### Part C:
- Initial: (0,0)=0, all others=INF, none visited
- Step 1: Visit (0,0) d=0. Update (0,1)->1, (1,0)->1
- Step 2: Visit (0,1) d=1. Update (0,2)->2 (no (1,1) in graph)
- Step 3: Visit (1,0) d=1. Update (2,0)->2
- Step 4: Visit (0,2) d=2. Update (1,2)->3
- Step 5: Visit (2,0) d=2. Update (2,1)->3
- Step 6: Visit (1,2) or (2,1) d=3. Update (2,2)->4
- Path: (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2), length = 4

### Part D:
| Start | Dest | Manhattan Length | Dijkstra Length | Same? |
|---|---|---|---|---|
| (0,0) | (2,2) | 4 | 4 | Yes |
| (0,0) | (2,1) | 3 | 3 | Yes |
| (0,1) | (2,1) | 2 | 4 (must go around) | No |
| (1,0) | (1,2) | 2 | 4 (must go around) | No |

1. When the obstacle is not in the Manhattan path.
2. When the obstacle blocks the direct Manhattan route — Manhattan would try to go through (1,1).
3. Dijkstra considers the actual graph structure and finds paths around obstacles.
