# Module 5: Dijkstra's Algorithm (Capstone)

## Overview

**Duration:** 3–4 weeks

**Theme:** Graph algorithms, obstacle detection, and the power of modular code

**Final Project:** Robot navigates to destinations, detects obstacles with a rangefinder, updates its "knowledge" of the grid, and reroutes dynamically. Demonstrate improved performance on subsequent runs.

## Learning Objectives

By the end of this module, students will be able to:
- Understand graphs and how a grid can be represented as a graph
- Understand Dijkstra's algorithm for finding shortest paths with obstacles
- Implement Dijkstra's algorithm in Python
- Use dictionaries to represent graphs
- Swap Dijkstra for Manhattan without changing the rest of the program (polymorphism through interface matching)
- Use the rangefinder sensor to detect obstacles
- Dynamically update the obstacle list and recompute paths
- Demonstrate "learning" over multiple runs (core of the capstone)

## Key Concepts

- **Graphs:** Nodes (intersections) and edges (paths); representing a grid as a graph
- **Graph Representation:** Using dictionaries to store neighbors
- **Dijkstra's Algorithm:** Finding shortest paths when some paths are blocked
- **Dictionaries:** Key-value pairs; using coordinates as keys
- **Nested Data Structures:** Lists of tuples as dictionary values
- **Algorithm Swapping:** Modular design allows replacing Manhattan with Dijkstra
- **Obstacle Detection:** Reading rangefinder; detecting blocked intersections
- **Dynamic Updating:** Learning over time; growing a list of blocked nodes
- **Robotics Integration:** End-to-end system combining sensing, computation, and navigation

## Module Structure

### Phase A: Graph Theory and Dictionaries (Lessons 1–3)
Students understand graphs and implement dictionaries.
- Lesson 1: The Grid as a Graph
- Lesson 2: Dictionaries
- Lesson 3: Dijkstra's Algorithm — The Concept

### Phase B: Implementing Dijkstra (Lessons 4–6)
Students code the Dijkstra class and integrate it.
- Lesson 4: The Dijkstra Class
- Lesson 5: Implementing compute_path()
- Lesson 6: Testing and Swapping (Dijkstra for Manhattan)

### Phase C: Capstone Project (Lessons 7–9)
Students add obstacle detection and demonstrate the full system.
- Lesson 7: Obstacle Detection with the Rangefinder
- Lesson 8: Building Experience (Updating Obstacles Over Time)
- Lesson 9: Module 5 Capstone Project

## Python Concepts Introduced

| Concept | Lesson | Usage |
|---|---|---|
| Dictionaries | 2 | Represent graph: `{(0,0): [(0,1), (1,0)], ...}` |
| Dictionary creation | 2 | `dict()` or `{}` syntax |
| Dictionary access | 2 | `graph[(0,0)]` to get neighbors |
| `in` keyword | 3 | Check if key in dictionary |
| Nested structures | 1–2 | Lists of tuples as dictionary values |
| Algorithm implementation | 5 | Translating algorithm to code |
| Set operations (optional) | 3 | `visited` set in Dijkstra |

## Progression

1. **Week 16:** Graph theory and Dijkstra algorithm concept — hand-tracing, understanding logic
2. **Week 17:** Implementation and testing — code Dijkstra class; verify it works with and without obstacles
3. **Week 18:** Capstone demo — add rangefinder, obstacle detection, demonstrate learning over multiple runs

**Emphasis:** Building on Module 4 structure; only the pathfinding logic changes. This demonstrates the power of good software design.

## Key Milestones

- ✓ **End of Week 16:** Dijkstra algorithm understood via hand-tracing; graph representation understood
- ✓ **Week 17 mid:** Dijkstra class implemented; tested with various obstacle sets
- ✓ **Week 17 end:** Swapped into Module 4 program; works identically to Manhattan with no obstacles
- ✓ **Week 18 early:** Rangefinder integrated; obstacle detection working
- ✓ **End of Week 18:** Capstone complete — full system working; learning demonstrated

## Assessment

Students demonstrate mastery by:
1. **Algorithm trace worksheet:** Hand-trace Dijkstra on small graph with obstacles
2. **Dijkstra class implementation:** Code works correctly; tested with multiple obstacle sets
3. **Integration test:** Swapped into Module 4 program; still works
4. **Rangefinder integration:** Detects obstacles at intersections
5. **Capstone demo:** Full system works; demonstrates learning over runs:
   - Run 1: Robot navigates, detects obstacles
   - Run 2+: Robot avoids known obstacles, more efficient path

## Debugging Notes

**Common issues:**
- **Dijkstra gives same result as Manhattan with no obstacles:** This is correct (should be identical)
- **Dijkstra hangs (infinite loop):** Check if all nodes are reachable; verify obstacle list doesn't block all paths
- **Rangefinder always detects obstacle:** Threshold too low; recalibrate sensor distance
- **Robot doesn't avoid obstacle on 2nd run:** Obstacle list not persisting between runs; check data storage
- **Program works on simulator, fails on robot:** Timing or sensor calibration; debug one piece at a time

## Resources

- Graph representation worksheet (in worksheets/)
- Algorithm hand-tracing worksheet (in worksheets/)
- `Dijkstra` class template (in code/starter/)
- Solution code (in code/solutions/)
- Rangefinder sensor examples
- Main program template for capstone

## Next Steps

After this module, students have completed the graduation course. Optional extensions:
- **Advanced:** Multi-robot navigation, A* algorithm, dynamic obstacle updates via sensors
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
- [ ] Dijkstra algorithm correctly implemented
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
