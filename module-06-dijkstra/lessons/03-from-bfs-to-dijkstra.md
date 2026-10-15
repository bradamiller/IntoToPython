# Lesson 3: From BFS to Dijkstra

## Overview
Students turn their BFS into Dijkstra's algorithm by copying `compute_bfs_path()`, renaming the copy `compute_dijkstra_path()`, and changing two things in the middle: take the **closest** intersection off `to_visit` instead of the oldest (`closest()` over a new `distance` dictionary, replacing `pop(0)`), and add the segment's **weight** instead of counting a step, keeping the cheaper total -- and overwriting `previous` -- when an intersection is reached again by a better route. The graph, `add_blocked()`, `previous` and the walk-back are untouched. Students run the harness after each change, print the cost grid with `print_grid()` and explain its one cell that differs from BFS's rings, and run Manhattan, BFS and Dijkstra through one harness. No robot. No priority queue: `closest()` is a linear scan, which is instant on a 4x4 grid and keeps the two ideas visible.

## Learning Objectives
By the end of this lesson, students will be able to:
- Copy and rename BFS and confirm the copy behaves identically
- Make change 1 and explain why BFS could take the oldest entry and Dijkstra cannot
- Make change 2 and explain why `previous[neighbor]` may be overwritten
- Explain each number in the cost grid, in particular the one that differs from BFS
- Run three planners through `run_all_tests()` and say where each fails and why

## Key Concepts
- **Copy first.** A working thing, duplicated, changed in two marked places, tested after each.
- **`distance`**: the cheapest cost found so far to each intersection; starts `{position: 0}`.
- **Change 1 -- closest first**: `current = closest(to_visit, distance); to_visit.remove(current)`. BFS's rings are rings of steps and of cost at once; weights break that.
- **Change 2 -- weight, and keep the cheaper**: `new_distance = distance[current] + weight(current, neighbor)`; `if neighbor not in distance or new_distance < distance[neighbor]:` update `distance`, `previous`, and append if not waiting.
- **The cost grid**: `print_grid(ROWS, COLS, BLOCKED, dijkstra_distances((0,0)))`. Every cell is a BFS ring number except where the slow segment is on the direct route.
- **Three planners, one harness**: walls split Manhattan from BFS; weights split BFS from Dijkstra; on an open grid all three agree.

## Materials Required
- Computers with Python (no robot)
- `code/starter/lesson-03-from-bfs-to-dijkstra.py` (`closest()` body and the two changes as TODOs; BFS complete for comparison); `code/solutions/lesson-03-from-bfs-to-dijkstra.py`
- Students' Lesson 5-6 harness file with Lesson 2's cost check added
- `worksheets/03-from-bfs-to-dijkstra.md`

## Lesson Flow

### Introduction (10 minutes)
"BFS fails the cost check because it never looks at a weight. We are not writing a new algorithm. We are copying BFS and changing two lines." Copy, rename, run the harness: the copy fails the same test. Now there is a safe place to work.

### Guided Practice (25 minutes)
1. **Change 1.** Why can BFS take the oldest entry? With every step costing 1, the oldest is always among the closest. Draw a case where that breaks: an intersection reached early by the slow road is further, in cost, than one reached later round the detour. Add `distance = {position: 0}`, write `closest()` (a minimum-finding loop, Module 1 shape), swap `pop(0)` for `closest()` + `remove()`. Harness: Module 5 properties still pass.
2. **Change 2.** Put the BFS neighbor loop and the Dijkstra one side by side:
   ```python
   # BFS                                   # Dijkstra
   for neighbor in graph[current]:         for neighbor in graph[current]:
       if neighbor not in previous:            new_distance = distance[current] + weight(current, neighbor)
           previous[neighbor] = current        if neighbor not in distance or new_distance < distance[neighbor]:
           to_visit.append(neighbor)               distance[neighbor] = new_distance
                                                   previous[neighbor] = current
                                                   if neighbor not in to_visit:
                                                       to_visit.append(neighbor)
   ```
   The new idea: `previous` can be overwritten when a cheaper way turns up. Harness: the cost check passes.
3. **The cost grid.**
   ```
          0  1  2  3
       -------------
    0 |   0  1  4  5
    1 |   1  2  3  4
    2 |   2  3  4  5
    3 |   3  4  5  6
   ```
   Students point at the one cell that is not a BFS ring number -- (0, 2) is 4, not 2 -- and explain it before being told (1 + 5 = 6 along the row; 4 round through row 1; the cheaper is kept).

### Independent Practice (15 minutes)
Complete the starter; run the three-planner harness; fill in the worksheet's who-fails-what table. Extension: a second slow edge, and a destination where the slow road is still the cheapest.

Expected:
```
--- (0,0) to (0,3), slow edge (0,1)-(0,2) weight 5 ---
  BFS       steps: 3  cost: 7   [(0, 1), (0, 2), (0, 3)]
  Dijkstra  steps: 5  cost: 5   [(1, 0), (1, 1), (1, 2), (0, 2), (0, 3)]
```

### Assessment
- **Formative:** point to the two changed regions; explain `closest()`; explain the (0, 2) cell.
- **Exit ticket:** "Why does Dijkstra sometimes overwrite `previous[neighbor]`, when BFS never does?"

## Common Misconceptions
| Misconception | Reality |
|---|---|
| "Dijkstra is a different algorithm" | It is BFS with two changes; 90% of the code is identical and students can diff it. |
| "`closest()` must be a priority queue" | A linear scan is correct and instant here. A priority queue is a faster way to do the same thing; that is the whole answer. |
| "Once an intersection is in `previous`, it's done" | In Dijkstra a cheaper way may turn up later; `distance` and `previous` are overwritten. That is change 2. |
| "Dijkstra always avoids the slow segment" | It takes the slow segment when the detour costs more. Weight, not wall. |

## Differentiation
- **Support:** give `closest()` complete; students make only the two changes in `compute_path`.
- **Extension:** `dijkstra_distances()` for a different start; a grid with two slow edges where the cheapest route uses one of them; count how many times `previous` is overwritten.

## Teaching Notes
- Copy first, change second, stop at two changes. Students who write Dijkstra fresh get lost in bookkeeping; students who diff BFS have it in twenty minutes and can explain both changes.
- The cost grid is where understanding shows. Ask before telling.

## Connections to Next Lessons
- **Lesson 4** drives the slow grid with both planners and times the runs.
- **Lesson 5 (extension)** is the same two changes inside a `Dijkstra` class, through the Module 5 class harness.
