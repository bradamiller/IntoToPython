# Lesson 2: Weights in the Graph

## Overview
The weight from Lesson 1 goes into the program. Students add `SLOW_EDGES` beside `BLOCKED` with `add_slow_edge(a, b, cost)`, write `weight(a, b)` (the slow cost in either direction, 1 otherwise) and `path_cost(position, path)` (walk the path from the start, summing weights), and then add a sixth property to the Module 5 harness: the path's cost equals the cheapest possible. BFS, unchanged, passes everything else and fails that -- on paper, with the offending path printed. The lesson names BFS's limitation precisely: it minimizes steps, and it never looks at a weight. No robot.

## Learning Objectives
By the end of this lesson, students will be able to:
- Store a slow segment as `(a, b, cost)` and add one with `add_slow_edge()`
- Write `weight(a, b)` with the either-direction match and the default of 1
- Write `path_cost(position, path)` starting from `position`, not `path[0]`
- Add `check_cost()` to the harness, work out the expected cost by hand, and read a FAIL line
- State what BFS failed and why

## Key Concepts
- **A second list**: `SLOW_EDGES`, fed by `add_slow_edge()`, exactly as `BLOCKED` is fed by `add_blocked()`. A slow segment is a property of the edge, so the entry holds both ends.
- **`weight(a, b)`**: `(a == x and b == y) or (a == y and b == x)` -- slow both ways. Return 1 for anything not in the list.
- **`path_cost(position, path)`**: `here` starts at `position` and moves forward; the first segment, start to `path[0]`, counts.
- **The cost property**: expected cost worked out by hand (Lesson 4-6: the expectation comes from you, not the program).
- **BFS's limitation, exactly**: it minimizes steps. The path is valid, connected, unblocked, shortest in steps -- and not cheapest.

## Materials Required
- Computers with Python (no robot)
- `code/starter/lesson-02-weights.py` (`weight()`, `path_cost()` and the expected cost as TODOs); `code/solutions/lesson-02-weights.py`
- `worksheets/02-weights-in-the-graph.md`; the weight from Lesson 1

## Lesson Flow

### Introduction (10 minutes)
"The planner needs to know about the slow segment. Where does it already keep what it knows about the grid?" `BLOCKED`, through `add_blocked()`. Slow segments get the same treatment: a list and a function to add to it. Ask what an entry must hold -- both intersections and the weight, because slowness belongs to the edge, not an endpoint.

### Guided Practice (20 minutes)
1. **`add_slow_edge()` and `weight()`.** Write `weight()` together. Ask what `weight((0,2), (0,1))` should return when the entry was added as `((0,1), (0,2), 5)`. The `or` in the `if` is the answer; plant the bug of leaving it out and watch the cost depend on direction.
2. **`path_cost()`.** Trace it on `[(0,1), (0,2), (0,3)]` from (0,0): 1 + 5 + 1 = 7. Ask what happens if `here` starts at `path[0]` instead of `position` (the first segment is skipped; every cost is one too small).
3. **`check_cost()`.** Add it to the harness. Work out the cheapest cost for (0,0) to (0,3) on the slow grid by hand -- round through row 1, five blocks, 5 -- and type it in. Run:
   ```
   PASS: open row - cost 3
   FAIL: slow row - cost 7 but the cheapest route costs 5
         path: [(0, 1), (0, 2), (0, 3)]
   ```
   "Not a crash. Not a wrong turn on the floor. A FAIL line with the path, at a desk."

### Independent Practice (15 minutes)
Complete the starter's TODOs; run the two checks; then add a second slow edge of your own, work out the expected cost by hand, and check BFS again. Worksheet Parts 2-4.

### Assessment
- **Formative:** `weight()` with the `or`; `path_cost()` traced; a FAIL line read aloud.
- **Exit ticket:** "Why does BFS pass the open-grid cost check and fail the slow one?"

## Common Misconceptions
| Misconception | Reality |
|---|---|
| "Mark the slow intersections as blocked" | The segment is slow, not closed, and sometimes still the best route. Blocking it would be wrong in both directions. |
| "`weight()` only needs to match one order" | The robot may drive the segment either way. Without the `or`, the cost depends on direction. |
| "Start `path_cost()` at `path[0]`" | The path excludes the start (Lesson 4-5, promise 1). The first segment is from `position`. |
| "Let the program tell me the expected cost" | Then the test tests nothing. Trace the cheapest route by hand. |

## Differentiation
- **Support:** give `weight()` complete; students write `path_cost()` and the expected cost.
- **Extension:** a one-way slow segment (drop the `or` on purpose and say when that would be right); a `print_grid()` of path cost for every destination from (0,0) using BFS -- the cells where BFS is wrong stand out.

## Teaching Notes
- This is Lesson 5-6's idea doing its job a second time. Make students write the expected cost before running the check.
- Say the limitation precisely and without blame: *BFS minimizes steps; it never looks at a weight.* The next lesson keeps 90% of it.

## Connections to Next Lessons
- **Lesson 3** copies `compute_bfs_path`, renames it, and changes two lines; the FAIL becomes a PASS.
