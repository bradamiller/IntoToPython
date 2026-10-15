# Lesson 1 Slide Outline: The Grid as a Graph

## Slide 1: Title & Learning Objectives
**Title:** The Grid as a Graph

**Learning Objectives:**
- Understand graph terminology: nodes, edges, neighbors
- Represent a grid of intersections as a graph
- Identify why Manhattan pathfinding fails with blocked intersections
- Find shortest paths by hand on a graph with obstacles

**Agenda:**
- Why Manhattan isn't enough (5 min)
- Graph terminology (10 min)
- Drawing the grid as a graph (10 min)
- Blocked nodes and pathfinding by hand (10 min)
- Practice exercise (10 min)

---

## Slide 2: Hook — What If the Road Is Closed?
**Question:** "You're driving to school and your usual route is blocked by construction. What do you do?"

**Discussion:**
- You find a detour — go around the blocked road
- GPS apps (Google Maps, Waze) reroute you automatically
- The robot needs to do the same thing!

**Problem:** Our Manhattan algorithm goes rows-first, then columns. What if an intersection on that path is blocked?

```
(0,0) → (1,0) → (2,0) → (2,1) → (2,2)
                   ^
              BLOCKED! Now what?
```

**Today:** We'll learn a new way to think about the grid that handles obstacles.

---

## Slide 3: Why Manhattan Fails with Obstacles
**Manhattan always takes the same L-shaped path:**

| | Col 0 | Col 1 | Col 2 |
|---|---|---|---|
| Row 0 | START | | |
| Row 1 | ↓ | | |
| Row 2 | ↓ | → | END |

**But what if (1, 0) is blocked?**

| | Col 0 | Col 1 | Col 2 |
|---|---|---|---|
| Row 0 | START | | |
| Row 1 | BLOCKED | | |
| Row 2 | | | END |

- Manhattan doesn't know about obstacles
- It can't reroute — it only knows "rows first, then columns"
- We need a smarter approach that can go AROUND blocked intersections

---

## Slide 4: What Is a Graph?
**Graph:** A collection of **nodes** connected by **edges**

**Key terms:**
- **Node** (also called vertex): A point in the graph — for us, an intersection
- **Edge**: A connection between two nodes — for us, a path between adjacent intersections
- **Neighbors**: Nodes directly connected by an edge

**Real-world examples of graphs:**
- Road map: intersections are nodes, streets are edges
- Social network: people are nodes, friendships are edges
- Airline routes: airports are nodes, flights are edges

**Our grid IS a graph.** We just need to see it that way.

---

## Slide 5: The Grid as a Graph
**Each intersection is a node. Each path between adjacent intersections is an edge.**

**A 3x3 grid:**
```
(0,0) --- (0,1) --- (0,2)
  |         |         |
(1,0) --- (1,1) --- (1,2)
  |         |         |
(2,0) --- (2,1) --- (2,2)
```

**Node (1,1) has 4 neighbors:** (0,1), (2,1), (1,0), (1,2)

**Corner node (0,0) has 2 neighbors:** (0,1), (1,0)

**Edge node (0,1) has 3 neighbors:** (0,0), (0,2), (1,1)

**Key Idea:** Each node connects only to nodes directly above, below, left, or right — no diagonals!

---

## Slide 6: Weighted vs. Unweighted Graphs
**Weighted graph:** Edges have different costs (distances, times, etc.)

```
A ---5--- B ---2--- C
|                   |
3                   7
|                   |
D -------4-------- E
```

**Unweighted graph:** All edges cost the same (cost = 1)

```
A ---1--- B ---1--- C
|                   |
1                   1
|                   |
D -------1-------- E
```

**Our grid is unweighted:**
- Every move from one intersection to the next costs 1 step
- Moving from (0,0) to (0,1) costs the same as (1,1) to (2,1)
- This makes things simpler!

---

## Slide 7: Blocking Nodes — Removing from the Graph
**A blocked intersection = remove that node and all its edges**

**3x3 grid with (1,0) blocked:**
```
(0,0) --- (0,1) --- (0,2)
            |         |
          (1,1) --- (1,2)
  |         |         |
(2,0) --- (2,1) --- (2,2)
```

**What changed:**
- Node (1,0) is gone
- (0,0) lost a neighbor — now only connects to (0,1)
- (2,0) lost a neighbor — now only connects to (2,1)

**Now find a path from (0,0) to (2,0):**
- Manhattan path: (0,0) → (1,0) → (2,0) — BLOCKED!
- Graph path: (0,0) → (0,1) → (1,1) → (2,1) → (2,0) — goes around!

---

## Slide 8: Finding Paths by Hand
**Strategy: Explore outward from start, one step at a time**

**Find path from (0,0) to (2,2) with (1,1) blocked:**
```
(0,0) --- (0,1) --- (0,2)
  |                   |
(1,0)               (1,2)
  |                   |
(2,0) --- (2,1) --- (2,2)
```

**Trace outward:**
- From (0,0): can reach (0,1) and (1,0)
- From (0,1): can reach (0,2)
- From (1,0): can reach (2,0)
- From (0,2): can reach (1,2)
- From (2,0): can reach (2,1)
- From (1,2) or (2,1): can reach (2,2)

**Shortest path:** (0,0) → (0,1) → (0,2) → (1,2) → (2,2) — 4 steps

**Note:** Without the blocked node, Manhattan distance would also be 4. But the PATH is different!

---

## Slide 9: Your Turn!
**Activity: Draw the Grid as a Graph and Find Paths**

1. Draw a 4x4 grid as a graph (nodes and edges)
2. Mark these intersections as blocked: (1,1) and (2,2)
3. Redraw the graph with blocked nodes removed
4. Find the shortest path by hand:
   - From (0,0) to (3,3)
   - From (0,0) to (2,1)
   - From (3,0) to (0,3)
5. For each path, count the total number of steps

**Checkpoints:**
- Can you draw a grid as nodes and edges?
- Can you remove blocked nodes and their edges?
- Can you find a path that goes around obstacles?
- Is your path the shortest possible?

---

## Slide 10: Connection to Next Lesson
**What you did today:**
- Learned graph vocabulary: nodes, edges, neighbors
- Drew the grid as a graph
- Found paths by hand that go around blocked intersections

**Next lesson (Lesson 2):**
- Learn about **dictionaries** — Python's key-value data structure
- Represent the graph in Python code
- Store which nodes connect to which neighbors: `{(0,0): [(0,1), (1,0)], ...}`

**Key insight:** Today you drew the graph on paper. Next lesson, you'll build it in Python so the robot can use it.
