# Lesson 1: When Fewest Steps Isn't Fastest

## Overview
Module 5's BFS finds the path with the fewest steps, and on a grid where every block takes the same time that is also the fastest path. This lesson breaks that assumption physically: one segment of the grid has been re-taped as a long winding detour between two adjacent intersections, so the map says one step and the drive takes several blocks' worth of time. Students time a normal block and the slow segment with a stopwatch, turn the ratio into a **weight** -- how many normal blocks' worth of time the segment costs -- add up the cost of two routes by hand, and predict that BFS will choose the slow road. No code changes today; the lesson produces a number the next lesson types in.

The lesson also establishes the one geometric fact the module depends on: going round one segment on an open grid costs exactly three normal blocks, so a slow segment of weight 3 *ties* with its detour. The physical slow segment has to be clearly worse than that (weight 4 or more) for BFS and Dijkstra to disagree.

## Learning Objectives
By the end of this lesson, students will be able to:
- Explain why the shortest path in steps is not always the fastest in time
- Time a normal block and the slow segment, and compute the weight as a ratio rounded to a whole number
- Add up a route's cost as the sum of its edge weights
- Predict which route BFS picks and whether it is the faster one
- Explain why a weight of exactly 3 is not slow enough

## Key Concepts
- **Slow segment**: one edge of the grid whose tape takes a long detour. Line following still works; the drive takes longer.
- **Weight**: slow time / normal time, rounded. Measured in blocks, not seconds, so it is independent of robot speed.
- **Cost of a route**: the sum of its edge weights; 1 per normal block.
- **BFS counts steps**: `build_graph()` has no way to say an edge is long, and `compute_bfs_path()` counts edges. It will pick the slow road whenever it has fewer steps.
- **The tie at 3**: the detour round one segment is 3 blocks; weight 3 breaks even.

## Materials Required
- The Module 5 grid with one segment re-taped as a winding detour (see Physical setup in the module README); test it with `track_to_intersection()` before class
- XRP robot; a stopwatch (phone)
- `worksheets/01-when-fewest-steps-isnt-fastest.md`; grid paper

## Lesson Flow

### Introduction (10 minutes)
1. **Show the grid.** Point at the re-taped segment. "To the robot's sensors, is this still a line? Yes. To the Module 5 graph, is it still one edge? Yes. Is it still one block's worth of driving?" No.
2. **What BFS will do.** From (0, 0) to (0, 3) with the slow segment between (0, 1) and (0, 2): BFS picks the straight row, three steps, because it counts edges and nothing in the graph says an edge is long.

### Guided Practice (15 minutes): measure it
1. Time the robot driving one normal block with `track_to_intersection()` -- three runs, average.
2. Time the slow segment the same way -- three runs, average.
3. Divide. Round. That is the weight. Write it on the board; it is the number Lesson 2 uses.
   ```
   Normal block:   4.1  4.0  4.2   avg 4.1 s
   Slow segment:  19.8 20.5 20.1   avg 20.1 s
   weight = 20.1 / 4.1 = 4.9 -> 5
   ```

### Independent Practice (15 minutes): cost on paper
Worksheet Parts 2-4: add up Route A (straight, 3 steps) and Route B (round through row 1, 5 steps) with the measured weight; predict BFS's choice; repeat with weight 3 and discover the tie; repeat for a second start/destination pair.

### Assessment
- **Formative:** compute a weight from two timings; add up two routes; say which BFS picks.
- **Exit ticket:** "Weight 4, (0,0) to (0,3): cost of each route, and which is faster?" (A: 6, B: 5; B.)

## Common Misconceptions
| Misconception | Reality |
|---|---|
| "The weight is the number of seconds" | It is the ratio to a normal block. Seconds change with battery and speed; the ratio does not. |
| "BFS is broken" | BFS does exactly what it promises: fewest steps. Cost is information it never had. |
| "Any slow segment will do" | Weight 3 ties with the detour. The segment must be clearly worse: 4 or more. |
| "The planner should just avoid the slow segment" | Sometimes it is still the best route -- when the detour is longer than the weight. That is why it is a weight, not a block. |

## Differentiation
- **Support:** give the two routes drawn; students only add up.
- **Extension:** find a start/destination pair where the slow segment *is* still the best route, and one where it ties.

## Teaching Notes
- Set the grid up first and make the detour long -- weight 5 makes every number in the module unambiguous. Keep the curves gentle enough for line following and the two end intersections reading as crosses.
- The stopwatch is the point. A weight students measured is a fact; a weight the teacher announces is arithmetic.
- **Physical setup is still being tried on a real grid.** The winding detour needs nothing under the tape and does not disturb the reflectance sensors. Alternatives were set aside (rough surface disturbs sensors; "turns cost time" makes cost depend on heading). Record what works in the module README.

## Connections to Next Lessons
- **Lesson 2** types the weight into the program and adds a cost check to the harness; BFS fails it on paper.
- **Lesson 4** drives both routes and times them.
