# Lesson 3 Slide Outline: Dijkstra's Algorithm — The Concept

## Slide 1: Title & Learning Objectives
**Title:** Dijkstra's Algorithm — The Concept

**Learning Objectives:**
- Describe the three key data structures used by Dijkstra's algorithm
- Trace the algorithm step by step on a small grid
- Reconstruct a shortest path from the previous-node dictionary
- Compare Dijkstra's output to Manhattan's output with and without obstacles

**Agenda:**
- The big idea: exploring outward (5 min)
- Key data structures (10 min)
- Step-by-step walkthrough on a 3x3 grid (15 min)
- Reconstructing the path (5 min)
- Manhattan vs. Dijkstra comparison (5 min)
- Paper tracing exercise (10 min)

---

## Slide 2: Hook — How Does GPS Find the Fastest Route?
**Question:** "When Google Maps gives you directions, how does it know the shortest route — especially with road closures?"

**It doesn't try every possible route.** That would take forever on a real map with millions of roads.

**Instead it uses an algorithm similar to Dijkstra's:**
1. Start at your location
2. Explore nearby intersections first
3. Spread outward, always picking the closest unvisited intersection
4. Stop when you reach the destination

**Edsger Dijkstra** invented this algorithm in 1956 — and variations of it still power navigation today.

---

## Slide 3: The Three Key Data Structures
**Dijkstra's algorithm uses three dictionaries/collections:**

| Data Structure | Type | Purpose |
|---|---|---|
| `distances` | dictionary | Shortest known distance from start to each node |
| `previous` | dictionary | Which node we came from to reach each node |
| `visited` | list | Nodes we've finished processing |

**Initial setup (starting from (0,0)):**
```python
distances = {(0,0): 0}      # Start node is distance 0
previous  = {(0,0): None}   # Start node has no previous
visited   = []               # Nothing visited yet
```

**Every other node starts with no entry** — meaning distance is unknown (infinity).

---

## Slide 4: The Algorithm — One Sentence
**Repeat:** Pick the unvisited node with the smallest distance, visit its neighbors, mark it visited.

**In more detail:**
1. From all unvisited nodes that have a known distance, pick the one with the **smallest** distance
2. For each of that node's **neighbors**:
   - If the neighbor hasn't been visited AND the new distance is shorter (or first time seen):
     - Update its distance
     - Record where we came from (previous)
3. Mark the current node as **visited** (done with it)
4. Repeat until the destination is visited (or no nodes left)

---

## Slide 5: Walkthrough — Setup
**3x3 grid with (1, 1) blocked. Find shortest path from (0,0) to (2,2).**

```
(0,0) --- (0,1) --- (0,2)
  |                   |
(1,0)               (1,2)
  |                   |
(2,0) --- (2,1) --- (2,2)
```

**Graph dictionary:**
```python
graph = {
    (0,0): [(0,1), (1,0)],
    (0,1): [(0,0), (0,2)],
    (0,2): [(0,1), (1,2)],
    (1,0): [(0,0), (2,0)],
    (1,2): [(0,2), (2,2)],
    (2,0): [(1,0), (2,1)],
    (2,1): [(2,0), (2,2)],
    (2,2): [(2,1), (1,2)]
}
```

**Starting state:**
```
distances: {(0,0): 0}
previous:  {(0,0): None}
visited:   []
```

---

## Slide 6: Walkthrough — Steps 1-3
**Step 1: Visit (0,0) — distance 0**
- Neighbors: (0,1) and (1,0)
- (0,1): distance = 0 + 1 = 1, previous = (0,0)
- (1,0): distance = 0 + 1 = 1, previous = (0,0)
- Mark (0,0) visited

```
distances: {(0,0): 0, (0,1): 1, (1,0): 1}
previous:  {(0,0): None, (0,1): (0,0), (1,0): (0,0)}
visited:   [(0,0)]
```

**Step 2: Visit (0,1) — distance 1** (pick either node with distance 1)
- Neighbors: (0,0) already visited, (0,2) unseen
- (0,2): distance = 1 + 1 = 2, previous = (0,1)
- Mark (0,1) visited

```
distances: {(0,0): 0, (0,1): 1, (1,0): 1, (0,2): 2}
visited:   [(0,0), (0,1)]
```

**Step 3: Visit (1,0) — distance 1**
- Neighbors: (0,0) already visited, (2,0) unseen
- (2,0): distance = 1 + 1 = 2, previous = (1,0)
- Mark (1,0) visited

```
distances: {..., (0,2): 2, (2,0): 2}
visited:   [(0,0), (0,1), (1,0)]
```

---

## Slide 7: Walkthrough — Steps 4-6
**Step 4: Visit (0,2) — distance 2**
- Neighbors: (0,1) visited, (1,2) unseen
- (1,2): distance = 2 + 1 = 3, previous = (0,2)
- Mark (0,2) visited

**Step 5: Visit (2,0) — distance 2**
- Neighbors: (1,0) visited, (2,1) unseen
- (2,1): distance = 2 + 1 = 3, previous = (2,0)
- Mark (2,0) visited

**Step 6: Visit (1,2) — distance 3** (pick either node with distance 3)
- Neighbors: (0,2) visited, (2,2) unseen
- (2,2): distance = 3 + 1 = 4, previous = (1,2)
- Mark (1,2) visited

**(2,2) is our destination! We could stop here, but let's see the full result.)**

**Final distances from (0,0):**
```
(0,0): 0    (0,1): 1    (0,2): 2
(1,0): 1                (1,2): 3
(2,0): 2    (2,1): 3    (2,2): 4
```

---

## Slide 8: Reconstructing the Path
**The `previous` dictionary tells us how to trace back from destination to start:**

```python
previous = {
    (0,0): None,
    (0,1): (0,0),
    (0,2): (0,1),
    (1,0): (0,0),
    (1,2): (0,2),
    (2,0): (1,0),
    (2,1): (2,0),
    (2,2): (1,2)
}
```

**Trace back from (2,2):**
- (2,2) came from (1,2)
- (1,2) came from (0,2)
- (0,2) came from (0,1)
- (0,1) came from (0,0)
- (0,0) has previous = None — we're at the start!

**Reverse it to get the path:**
```
(0,0) → (0,1) → (0,2) → (1,2) → (2,2)
```

**This is the shortest path around the blocked node (1,1)!** Total: 4 steps.

---

## Slide 9: Manhattan vs. Dijkstra
**No obstacles — same result:**

| | Manhattan | Dijkstra |
|---|---|---|
| (0,0) to (2,2) | (0,0)→(1,0)→(2,0)→(2,1)→(2,2) | Could find same or different 4-step path |
| Steps | 4 | 4 |
| Result | Same shortest distance | Same shortest distance |

**With (1,1) blocked — different paths:**

| | Manhattan | Dijkstra |
|---|---|---|
| (0,0) to (2,2) | (0,0)→(1,0)→ **STUCK at (1,1)!** | (0,0)→(0,1)→(0,2)→(1,2)→(2,2) |
| Steps | Cannot complete | 4 |
| Result | Fails | Finds shortest path around obstacle |

**Key design insight:** Dijkstra's `compute_path` returns a list of tuples — the **same format** as Manhattan's `compute_path`. So our Navigator class doesn't need to change!

---

## Slide 10: Your Turn!
**Activity: Trace Dijkstra by Hand**

**Use this 3x3 grid with (0, 1) blocked. Find the shortest path from (0, 0) to (0, 2).**

```
(0,0)           (0,2)
  |               |
(1,0) --- (1,1) --- (1,2)
  |         |       |
(2,0) --- (2,1) --- (2,2)
```

**Fill in this table as you trace:**

| Step | Visit Node | Distance | Update Neighbors | Visited So Far |
|---|---|---|---|---|
| 1 | (0,0) | 0 | | |
| 2 | | | | |
| 3 | | | | |
| ... | | | | |

**Then reconstruct the path using the previous dictionary.**

**Checkpoints:**
- Can you pick the correct next node (smallest distance, unvisited)?
- Can you update neighbor distances correctly?
- Can you trace back through the previous dictionary to build the path?
- How many steps does the path take?

---

## Slide 11: Connection to Next Lesson
**What you did today:**
- Learned the three data structures: distances, previous, visited
- Traced Dijkstra's algorithm step by step on a grid
- Reconstructed the shortest path from the previous dictionary
- Compared Dijkstra to Manhattan pathfinding

**Next lesson (Lesson 4):**
- Implement Dijkstra's algorithm as a **Python class**
- Write `compute_path(destination)` that returns a list of tuples
- Same interface as Manhattan — so Navigator works with both!

**Key insight:** You traced the algorithm by hand today. Next lesson, you'll teach the computer to do the exact same steps.
