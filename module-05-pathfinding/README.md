# Module 5: Pathfinding Around Obstacles (Capstone)

## Overview

**Duration:** 3–4 weeks

**Theme:** Graph algorithms, obstacle detection, and the power of modular code

**Final Project:** Robot navigates to destinations, detects obstacles with a rangefinder, updates its "knowledge" of the grid, and reroutes dynamically. Demonstrate improved performance on subsequent runs.

**Planner:** breadth-first search (BFS) — the "ripples out from the start" algorithm. It finds the path with the fewest steps around any blocked intersections. Dijkstra's algorithm, which handles segments that are slower than others, is the optional **Module 6**: the same code with two changes.

> **Reshaped 2026-10-14.** The code under `code/` is current. Lessons 3–5 were the
> Dijkstra-first versions and have moved to `module-06-dijkstra/_source-material/`;
> their BFS replacements are to be written from the code (see
> `teacher-guide/course-design-decisions.md`, D6 and the phase-3 plan). Lessons 6–9
> still describe the old shape in places.

## Learning Objectives

By the end of this module, students will be able to:
- Understand graphs and how a grid can be represented as a graph
- Use dictionaries to represent graphs
- Trace breadth-first search by hand and explain why it finds a shortest path
- Implement `compute_bfs_path(position, destination)` and `add_blocked(intersection)`
- Test a planner on paper with property checks, with no robot and no grid
- Swap BFS for Manhattan without changing the rest of the program (pass the planner function)
- Use the rangefinder sensor to detect obstacles and feed them to the planner with `add_blocked()`
- Dynamically update the obstacle list and recompute paths
- Demonstrate "learning" over multiple runs (core of the capstone)

## Key Concepts

- **Graphs:** Nodes (intersections) and edges (paths); representing a grid as a graph
- **Graph Representation:** Using dictionaries to store neighbors
- **Breadth-first search:** Finding a shortest path when some intersections are blocked
- **Dictionaries:** Key-value pairs; using coordinates as keys
- **Nested Data Structures:** Lists of tuples as dictionary values
- **Testing by properties:** When more than one answer is right, test what must be true
- **Algorithm Swapping:** Modular design allows replacing Manhattan with BFS (and, in Module 6, Dijkstra)
- **Obstacle Detection:** Reading rangefinder; detecting blocked intersections
- **Dynamic Updating:** Learning over time; growing a list of blocked nodes
- **Robotics Integration:** End-to-end system combining sensing, computation, and navigation

## Module Structure

### Phase A: Graphs and Dictionaries (Lessons 1–3)
- Lesson 1: The Grid as a Graph
- Lesson 2: Dictionaries
- Lesson 3: Breadth-First Search — The Concept (hand trace; ring numbers on the grid)

### Phase B: Implementing BFS (Lessons 4–6)
- Lesson 4: The Pathfinding Functions (`build_graph`, `add_blocked`, placeholder planner)
- Lesson 5: Implementing `compute_bfs_path()`
- Lesson 6: Testing and Swapping (property checks; BFS for Manhattan)

### Phase C: Capstone Project (Lessons 7–9)
- Lesson 7: Obstacle Detection with the Rangefinder
- Lesson 8: Building Experience (drive until you arrive; start Run 2 from Run 1's obstacles)
- Lesson 9: Module 5 Capstone Project

**After this module:** Module 6 (optional) upgrades BFS to Dijkstra's algorithm for grids with slow segments.

## Python Concepts Introduced

| Concept | Lesson | Usage |
|---|---|---|
| Dictionaries | 2 | Represent graph: `{(0,0): [(0,1), (1,0)], ...}` |
| Dictionary creation | 2 | `dict()` or `{}` syntax |
| Dictionary access | 2 | `graph[(0,0)]` to get neighbors |
| `in` keyword | 3 | Check if an intersection has been reached (`previous`) |
| Nested structures | 1–2 | Lists of tuples as dictionary values |
| Algorithm implementation | 5 | Translating the hand trace to code |
| Passing a function as an argument | 6 | `run_all_tests("BFS", compute_bfs_path)` |

## Progression

1. **Week 16:** Graphs, dictionaries and the BFS hand trace
2. **Week 17:** Implement `compute_bfs_path()`; paper tests with and without obstacles; swap it in for Manhattan
3. **Week 18:** Capstone demo — add rangefinder, obstacle detection, demonstrate learning over multiple runs

**Emphasis:** Building on Module 4 structure; only the pathfinding logic changes. This demonstrates the power of good software design.

## Key Milestones

- ✓ **End of Week 16:** BFS understood via hand-tracing; graph representation understood
- ✓ **Week 17 mid:** `compute_bfs_path()` implemented; harness passes with various obstacle sets
- ✓ **Week 17 end:** Swapped into Module 4 program; works identically to Manhattan with no obstacles
- ✓ **Week 18 early:** Rangefinder integrated; obstacle detection working
- ✓ **End of Week 18:** Capstone complete — full system working; learning demonstrated

## Assessment

Students demonstrate mastery by:
1. **Algorithm trace worksheet:** Hand-trace BFS (ring numbers) on a small grid with obstacles
2. **`compute_bfs_path()` implementation:** passes the Lesson 6 harness with multiple obstacle sets
3. **Integration test:** Swapped into Module 4 program; still works
4. **Rangefinder integration:** Detects obstacles at intersections
5. **Capstone demo:** Full system works; demonstrates learning over runs:
   - Run 1: Robot navigates, detects obstacles
   - Run 2+: Robot avoids known obstacles, more efficient path

## Debugging Notes

**Common issues:**
- **BFS gives the same number of steps as Manhattan with no obstacles:** This is correct (the exact route may differ; the harness checks properties, not one expected list)
- **BFS returns an empty path:** either the robot is already there, or the destination is walled off -- check `print_grid` and the blocked list
- **Rangefinder always detects obstacle:** Threshold too low; recalibrate sensor distance
- **Robot doesn't avoid obstacle on 2nd run:** Obstacle list not persisting between runs; check data storage
- **Program works on simulator, fails on robot:** Timing or sensor calibration; debug one piece at a time

## Resources

- Graph representation worksheet (in worksheets/)
- Algorithm hand-tracing worksheet (in worksheets/)
- `compute_bfs_path()` template (in code/starter/)
- Solution code (in code/solutions/)
- Rangefinder sensor examples
- Main program template for capstone

## Next Steps

After this module, students have completed the graduation course. Optional extensions:
- **Module 6 (optional):** Dijkstra's algorithm for grids with slow segments -- BFS with two changes
- **Advanced:** Multi-robot navigation, A* algorithm
- **Different domains:** Apply pathfinding to different graphs (not robots); challenge problems
- **Optimization:** Minimize time, energy, or path length under constraints

---

## Capstone Demonstration Guidelines

### Setup
- Physical grid with marked obstacles
- 4–6 destinations for robot to navigate to
- Multiple runs to demonstrate learning

### Student Tasks
1. **Program the robot** to navigate to all destinations
2. **First run:** Robot may encounter unexpected obstacles
3. **Detect and log** obstacles encountered
4. **Subsequent runs:** Robot avoids logged obstacles; demonstrate shorter paths or fewer collisions
5. **Present:** Explain algorithm, results, and lessons learned

### Grading Rubric
- [ ] BFS correctly implemented (passes the paper harness)
- [ ] Rangefinder detects obstacles at intersections
- [ ] Obstacle list updates and persists across runs
- [ ] Robot reaches all destinations (eventually)
- [ ] Demonstrates improvement on subsequent runs
- [ ] Code is well-organized and commented
- [ ] Student can explain design decisions

---

## Quick Start

1. **Build on Module 4:** Use Manhattan and Navigator as starting point
2. **Hand-trace first:** Use worksheet to understand Dijkstra before coding
3. **Test without obstacles:** Verify Dijkstra == Manhattan when no obstacles
4. **Add obstacles gradually:** Test with 0, 1, 2, ... obstacles
5. **Integrate rangefinder:** Add obstacle detection step-by-step
6. **Demo and iterate:** Run on robot, fix issues, demo again

---

**Note:** This capstone is the culmination of the course. The modular design (separating algorithm from hardware) pays off. Celebrate student progress—they've gone from "make the robot move" to "implement sophisticated algorithms." That's remarkable growth.
