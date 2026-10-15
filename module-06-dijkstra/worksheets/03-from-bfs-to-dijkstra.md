# Lesson 3 Worksheet: From BFS to Dijkstra

**Name:** ________________________
**Date:** ________________________

---

## Part 1: What stays the same

You copied `compute_bfs_path()` and renamed it. Tick everything that is **unchanged** in `compute_dijkstra_path()`:

[ ] `build_graph(ROWS, COLS, BLOCKED)`   [ ] the `position not in graph` check   [ ] `previous = {position: None}`
[ ] `to_visit = [position]`   [ ] how `to_visit` is emptied   [ ] what is added for each neighbor   [ ] the walk-back at the end

## Part 2: Change 1 -- closest first

```python
def closest(intersections, distance):
    best = intersections[0]
    for node in intersections:
        if distance[node] < distance[best]:
            best = node
    return best
```

1. `to_visit = [(0, 2), (1, 1), (1, 0)]` and `distance = {(0, 2): 6, (1, 1): 2, (1, 0): 1, ...}`. What does `closest()` return? ______

2. BFS would have taken `to_visit.pop(0)`, which is ______. Why is that the wrong one to expand next when there are weights?

______________________________________________________________

3. Why could BFS get away with oldest-first when every step costs 1?

______________________________________________________________

## Part 3: Change 2 -- add the weight, keep the cheaper

```python
for neighbor in graph[current]:
    new_distance = distance[current] + weight(current, neighbor)
    if neighbor not in distance or new_distance < distance[neighbor]:
        distance[neighbor] = new_distance
        previous[neighbor] = current
        if neighbor not in to_visit:
            to_visit.append(neighbor)
```

Slow edge (0,1)-(0,2) weight 5. The planner is at `current = (0, 1)` with `distance[(0,1)] = 1`, and `(0, 2)` is not yet in `distance`.

4. `new_distance` for neighbor (0, 2) = ____ + ____ = ______. It is recorded: `distance[(0,2)] = ______`, `previous[(0,2)] = ______`.

5. Later the planner is at `current = (1, 2)` with `distance[(1,2)] = 3`. `new_distance` for (0, 2) = ____ + ____ = ______. Is it smaller than what is recorded? ______ What happens to `distance[(0,2)]` and `previous[(0,2)]`?

______________________________________________________________

6. Why can BFS never need to overwrite `previous[neighbor]`?

______________________________________________________________

## Part 4: The cost grid

```
       0  1  2  3
    -------------
 0 |   0  1  4  5
 1 |   1  2  3  4
 2 |   2  3  4  5
 3 |   3  4  5  6
```

7. Circle the one cell that is not a BFS ring number. Explain its value:

______________________________________________________________

8. Why is (0, 3) a 5 and not a 7?

______________________________________________________________

## Part 5: Three planners, one harness

| Test | Manhattan | BFS | Dijkstra |
|---|---|---|---|
| open grid, shortest length | ______ | ______ | ______ |
| wall at (1,0),(1,1) | ______ | ______ | ______ |
| walled off: `[]` | ______ | ______ | ______ |
| slow edge, cheapest cost | ______ | ______ | ______ |

9. In one sentence each: what separates Manhattan from BFS? ______________________________ What separates BFS from Dijkstra? ______________________________

## Exit ticket

Why does Dijkstra sometimes overwrite `previous[neighbor]`, when BFS never does?

______________________________________________________________
