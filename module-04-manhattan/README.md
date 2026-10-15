# Module 4: Manhattan Navigation

## Overview

**Duration:** 3–4 weeks

**Theme:** Coordinate systems, data structures, and separating algorithm from action

**Final Project:** Robot navigates to a list of destinations using Manhattan pathfinding

## Learning Objectives

By the end of this module, students will be able to:
- Understand and use coordinate systems (row, column) on the grid
- Create and manipulate tuples and lists in Python
- Understand how the Manhattan distance algorithm works
- Implement the Manhattan algorithm to compute paths
- Write driving functions (`desired_heading`, `turn_to`, `drive_path`) that drive computed paths on the Module 2 line-tracking toolkit
- Test algorithms without hardware (crucial for later modules)
- Use separation of concerns (algorithm logic separate from driving logic)

## Key Concepts

- **Coordinate Systems:** Representing positions as (row, col) tuples
- **Tuples:** Immutable pairs of values; perfect for coordinates
- **Lists:** Ordered, mutable collections; used for storing paths
- **Algorithms:** Step-by-step procedures for solving problems
- **Manhattan Distance:** A pathfinding algorithm that moves along rows first, then columns
- **Separation of Concerns:** Algorithm (computing path) is separate from action (driving path)
- **Testing Without Hardware:** Verifying algorithm correctness before deploying to robot

## Module Structure

### Phase A: Data Structures (Lessons 1–3)
Students learn coordinates, tuples, and lists.
- Lesson 1: Coordinates on the Grid
- Lesson 2: Tuples
- Lesson 3: Lists

### Phase B: The Planner (Lessons 4–6)
Students implement Manhattan pathfinding as a function that is told where the robot is.
- Lesson 4: The Manhattan Algorithm
- Lesson 5: A Reusable Planner Function (optional extension: the `Manhattan` class)
- Lesson 6: Testing Without a Robot

### Phase C: Driving (Lessons 7–9)
Students design the turning logic on paper, then drive paths on the robot.
- Lesson 7: The Challenge of Turning (headings, `% 4`, `raise`)
- Lesson 8: Driving the Path (optional extension: the `Navigator` class, and `self` as an address)
- Lesson 9: Module 4 Final Project

## Python Concepts Introduced

| Concept | Lesson | Usage |
|---|---|---|
| Tuples | 2 | Represent coordinates as immutable (row, col) |
| Indexing tuples | 2 | Access row with `position[0]`, col with `position[1]` |
| Lists | 3 | Store multiple coordinates as a path |
| `append()` | 3 | Add coordinates to a path |
| List iteration | 3 | Loop through path coordinates |
| Arithmetic & logic | 4–5 | Implementing algorithm |
| Docstrings and `raise` | 5, 7 | Writing a function's promise down; stopping where a problem is found |
| Classes (optional) | 5, 8 | `Manhattan` and `Navigator` extensions for students who did Module 2's |

## Progression

1. **Week 12:** Data structures — tuples and lists; understanding coordinates
2. **Week 13:** Manhattan algorithm — hand-tracing, then the planner function
3. **Week 14:** Driving — turning logic and integration
4. **Week 15:** Full integration and testing on the robot

**Key emphasis:** Separate testing from deployment. Students test the planner with print statements before ever touching the robot.

## Key Milestones

- ✓ **End of Week 12:** Coordinate system understood; can index and create tuples/lists
- ✓ **End of Week 13:** `compute_manhattan_path` implemented; tested without hardware; outputs verified
- ✓ **Week 14 mid:** Turning logic understood; tested on paper
- ✓ **Week 14 end:** driving functions complete; turns tested with robot
- ✓ **End of Week 15:** Final project complete — robot navigates to 4+ destinations

## Assessment

Students demonstrate mastery by:
1. **Coordinate mapping exercise:** Map grid positions correctly
2. **Algorithm trace worksheet:** Hand-trace Manhattan algorithm on paper
3. **Planner test:** `compute_manhattan_path` outputs verified against expected paths
4. **Driving integration:** Turns work correctly on the grid; wheels on the cross at every arrival
5. **Final project demo:** Robot reaches all destinations in correct order

## Debugging Notes

**Common issues:**
- **Tuple indexing confusion:** Remember `position[0]` is row, `position[1]` is column
- **List empty when expected to have values:** Check that `append()` is inside the loop
- **Algorithm produces backward paths:** Check row/column increment logic (could increase or decrease)
- **Robot turns wrong direction:** Check heading calculation and turn commands
- **Leg 1 works, leg 2 goes wrong:** The return value of `drive_path` was dropped; the second path was planned from the start
- **Path works without hardware, fails on robot:** The printed path is right, so the bug is in the driving functions or Module 2's tuning -- turns end on a sensor, not a timer, so check the blind part of the turn and `drive_past_intersection`'s distance

## Resources

- Coordinate mapping worksheet (in worksheets/)
- Algorithm hand-tracing worksheet (in worksheets/)
- Starter files with the toolkit complete and the lesson's functions as TODOs (in code/starter/)
- Solution code, plus `*-class-addon.py` files for the optional class extensions (in code/solutions/)

## Next Module

Module 5 replaces the Manhattan algorithm with **Dijkstra's algorithm**, allowing the robot to handle **blocked intersections** and compute optimal paths around obstacles. The Navigator and overall structure stay the same—only the pathfinding logic changes.

---

## Quick Start

1. **Start with coordinates:** Have students map the physical grid by hand (Lesson 1)
2. **Practice tuples/lists:** Use Python interactive shell to create and manipulate coordinates
3. **Hand-trace the algorithm:** Use the worksheet before coding
4. **Test without hardware:** Run Manhattan.compute_path() with known inputs, verify outputs match
5. **Integrate with robot:** Once confident, drive the paths on the grid
6. **Iterate:** Fix heading/turning logic based on robot behavior

---

**Note:** This module shifts focus from "make the robot move" to "think algorithmically." The separation of algorithm from hardware is powerful and will pay off in Module 5. Don't rush these concepts.
