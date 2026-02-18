# Lesson 5 Worksheet: Implementing compute_path

**Name:** ________________________
**Date:** ________________________

---

## Part A: Algorithm Steps Review

Dijkstra's algorithm finds the shortest path from a start node to a destination. Fill in the blanks to complete the algorithm description.

**Step 1: Setup**

- Set the distance of every node to __________ (a very large number).
- Set the distance of the __________ node to 0.
- Set the "previous" node for every node to __________.
- Add every node to the __________ list.

**Step 2: Main Loop**

- While the to_visit list is not __________:
  - Find the node in to_visit with the __________ distance. Call it `current`.
  - If `current` is the __________, stop the loop.
  - Remove `current` from the __________ list.
  - For each __________ of `current`:
    - If the neighbor is still in __________:
      - Calculate `new_dist` = distance to `current` + __________.
      - If `new_dist` is __________ than the neighbor's current distance:
        - Update the neighbor's distance to __________.
        - Set the neighbor's "previous" to __________.

**Step 3: Reconstruct Path**

- Start at the __________ node.
- Follow the __________ pointers back to the start.
- __________ the path so it goes from start to destination.

---

## Part B: Trace compute_path Step by Step

**Grid:** 3x3 with (1, 1) blocked

```
(0,0) --- (0,1) --- (0,2)
  |                   |
(1,0)     [X X]     (1,2)
  |                   |
(2,0) --- (2,1) --- (2,2)
```

**Start:** (0, 0)    **Destination:** (2, 2)

Trace the algorithm using the tables below.

**Initial State:**

| Node | Distance | Previous | In to_visit? |
|---|---|---|---|
| (0, 0) | 0 | None | Yes |
| (0, 1) | 999999 | None | Yes |
| (0, 2) | 999999 | None | Yes |
| (1, 0) | 999999 | None | Yes |
| (1, 2) | 999999 | None | Yes |
| (2, 0) | 999999 | None | Yes |
| (2, 1) | 999999 | None | Yes |
| (2, 2) | 999999 | None | Yes |

**Iteration 1:**

Current node (smallest distance in to_visit): __________

| Neighbor | new_dist | Update? | New Distance | New Previous |
|---|---|---|---|---|
| __________ | __________ | __________ | __________ | __________ |
| __________ | __________ | __________ | __________ | __________ |

Remove __________ from to_visit.

**Iteration 2:**

Current node: __________

| Neighbor | new_dist | Update? | New Distance | New Previous |
|---|---|---|---|---|
| __________ | __________ | __________ | __________ | __________ |
| __________ | __________ | __________ | __________ | __________ |

Remove __________ from to_visit.

**Iteration 3:**

Current node: __________

| Neighbor | new_dist | Update? | New Distance | New Previous |
|---|---|---|---|---|
| __________ | __________ | __________ | __________ | __________ |
| __________ | __________ | __________ | __________ | __________ |

Remove __________ from to_visit.

**Iteration 4:**

Current node: __________

| Neighbor | new_dist | Update? | New Distance | New Previous |
|---|---|---|---|---|
| __________ | __________ | __________ | __________ | __________ |

Remove __________ from to_visit.

**Iteration 5:**

Current node: __________

| Neighbor | new_dist | Update? | New Distance | New Previous |
|---|---|---|---|---|
| __________ | __________ | __________ | __________ | __________ |

Remove __________ from to_visit.

**Iteration 6:**

Current node: __________ — Is this the destination? __________

**Path Reconstruction:**

Start at destination (2, 2), follow previous pointers:

(2, 2) <- previous = __________
__________ <- previous = __________
__________ <- previous = __________
__________ <- previous = __________

Reversed path: __________ -> __________ -> __________ -> __________ -> __________

---

## Part C: Code Reading

Read each section of the `compute_path` method and describe what it does.

**Section 1:**
```python
if destination not in self.graph:
    print("Destination is blocked!")
    return []
```

What does this section do? ____________________________________________________

Why is this check needed? ____________________________________________________

**Section 2:**
```python
distances = {}
previous = {}
to_visit = []

for node in self.graph:
    distances[node] = 999999
    previous[node] = None
    to_visit.append(node)

distances[self.position] = 0
```

What does this section do? ____________________________________________________

Why is the start distance set to 0? ____________________________________________________

**Section 3:**
```python
current = to_visit[0]
for node in to_visit:
    if distances[node] < distances[current]:
        current = node
```

What does this section do? ____________________________________________________

Why not just pick the first node in to_visit? ____________________________________________________

**Section 4:**
```python
for neighbor in self.graph[current]:
    if neighbor in to_visit:
        new_dist = distances[current] + 1
        if new_dist < distances[neighbor]:
            distances[neighbor] = new_dist
            previous[neighbor] = current
```

What does this section do? ____________________________________________________

Why do we add 1 for each step? ____________________________________________________

Why do we check `if new_dist < distances[neighbor]`? ____________________________________________________

**Section 5:**
```python
path = []
current = destination
while current is not None:
    path.append(current)
    current = previous[current]
path.reverse()
```

What does this section do? ____________________________________________________

Why do we need to reverse the path? ____________________________________________________

---

## Part D: Bug Finding

Each code snippet below has a bug. Find it and explain what goes wrong.

**Bug 1:**
```python
def compute_path(self, destination):
    distances = {}
    for node in self.graph:
        distances[node] = 999999
    # Missing: distances[self.position] = 0
```

What is the bug? ____________________________________________________

What happens? ____________________________________________________

**Bug 2:**
```python
current = to_visit[0]
for node in to_visit:
    if distances[node] > distances[current]:  # Wrong comparison!
        current = node
```

What is the bug? ____________________________________________________

What happens? ____________________________________________________

**Bug 3:**
```python
path = []
current = destination
while current is not None:
    path.append(current)
    current = previous[current]
# Missing: path.reverse()
return path
```

What is the bug? ____________________________________________________

What happens? ____________________________________________________

**Bug 4:**
```python
for neighbor in self.graph[current]:
    new_dist = distances[current] + 1
    if new_dist < distances[neighbor]:
        distances[neighbor] = new_dist
        previous[neighbor] = current
```

What is the bug? ____________________________________________________

*(Hint: What if the neighbor has already been visited?)*

What happens? ____________________________________________________

---

## Answer Key

### Part A:
- Step 1: 999999 (infinity), start, None, to_visit
- Step 2: empty, smallest, destination, to_visit, neighbor, to_visit, 1, less, new_dist, current
- Step 3: destination, previous, reverse

### Part B:
- Iteration 1: Current = (0,0). Neighbors: (0,1) new_dist=1 (update), (1,0) new_dist=1 (update). Remove (0,0).
- Iteration 2: Current = (0,1) [distance=1]. Neighbors: (0,0) not in to_visit, (0,2) new_dist=2 (update). Remove (0,1).
- Iteration 3: Current = (1,0) [distance=1]. Neighbors: (0,0) not in to_visit, (2,0) new_dist=2 (update). Remove (1,0).
- Iteration 4: Current = (0,2) [distance=2]. Neighbors: (0,1) not in to_visit, (1,2) new_dist=3 (update). Remove (0,2).
- Iteration 5: Current = (2,0) [distance=2]. Neighbors: (2,1) new_dist=3 (update). Remove (2,0).
- Iteration 6: Current = (1,2) or (2,1) [distance=3]. E.g., (1,2): neighbor (2,2) new_dist=4 (update). Then next iteration reaches (2,2).
- Path reconstruction: (2,2) <- (1,2) <- (0,2) <- (0,1) <- (0,0). Reversed: (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2).

### Part C:
1. Checks if destination is blocked before running the algorithm. Needed because a blocked destination has no path.
2. Initializes distances (all infinity), previous pointers (all None), and the to_visit list. Start is 0 because we are already there.
3. Finds the unvisited node with the smallest distance. We need the closest unvisited node, not just any node.
4. Updates neighbor distances if the new path through current is shorter. We add 1 because each edge has weight 1. We check less-than to only update when we found a shorter path.
5. Reconstructs the path from destination to start using previous pointers, then reverses it. We reverse because we traced backwards.

### Part D:
1. The start node distance is never set to 0, so it stays at 999999. The algorithm picks a random node first and never finds the correct shortest paths.
2. Uses `>` instead of `<`. This finds the node with the LARGEST distance instead of smallest, so it explores the wrong nodes first.
3. The path is built from destination to start but never reversed. The returned path goes backwards.
4. Missing `if neighbor in to_visit` check. Already-visited nodes could have their distances incorrectly updated, potentially creating wrong paths.
