# Lesson 9: Capstone Project

## Overview
Every piece assembled into one autonomous system: the robot visits four or more destinations in sequence, plans each leg with BFS, drives with Module 4's toolkit, watches the rangefinder, re-plans when it finds a wall, and starts the next run knowing what this one found. Students write very little new code. The capstone's new part is the destination loop -- call `navigate_with_detection()` once per destination, assign its returned `position` and `heading` so the next leg plans from where the robot actually is, and add up steps and reroutes. The challenge is **integration**: making tested parts work together, which is what engineers spend most of their time on.

Students demonstrate with two runs. Run 1 starts with `KNOWN_OBSTACLES = []`, discovers obstacles the hard way, and prints what it found. Run 2 starts with that list typed in and reroutes less. The drop in reroutes and steps *is* the learning. Everyone simulates the full program first (Lesson 7's `simulate_rangefinder()`), then drives.

Students who did the class extensions run the same capstone with `Navigator` and `BFS` objects; the rubric does not change.

## Learning Objectives
By the end of this project, students will be able to:
- Integrate the BFS planner, Module 4's driving toolkit and rangefinder detection into one program
- Visit four or more destinations in sequence, feeding each leg's end position and heading into the next
- Explain why only the first leg's path can be printed before the button
- Start a run from `KNOWN_OBSTACLES` and report `BLOCKED` at the end
- Demonstrate learning with recorded numbers: Run 2 outperforms Run 1
- Find and fix integration bugs where individually working parts don't cooperate

## Key Concepts
- **Program skeleton**: (1) hand `KNOWN_OBSTACLES` to `add_blocked()`; (2) define `destinations`; (3) print leg 1's plan, wait for the button; (4) for each destination, `navigate_with_detection()` and add to the totals; (5) print `BLOCKED` for the next run; (6) print the totals.
- **The blocked list is the thread**: filled at the start, read by the planner on every call, added to by detection, printed at the end -- every one through `add_blocked()`.
- **Assign the return value**: `position, heading, steps, reroutes = navigate_with_detection(...)`. Forget the left-hand side and leg 2 is planned from (0, 0) while the robot sits elsewhere.
- **Only leg 1 is printable in advance**: later legs are planned from wherever the robot ends up, with whatever it has found by then.
- **Integration bugs**: clearing `BLOCKED` between legs; not assigning `position, heading`; a destination that is itself in `KNOWN_OBSTACLES` (planner returns `[]`, leg is skipped with "No path").

## Materials Required
- XRP robot with rangefinder, the grid, 3-4 obstacles
- `code/starter/lesson-09-capstone.py` (toolkit complete; destination loop and `KNOWN_OBSTACLES` as TODOs); `code/solutions/lesson-09-capstone.py`
- The rubric (below) printed per team; a demo sign-up sheet

## Lesson Flow (2-3 class periods)

### Day 1: Assemble and simulate
Introduce the mission (an autonomous delivery robot with four stops) and the two-run demo. Put the skeleton on the board and ask which earlier lesson each line comes from. Students complete the starter's TODOs:

```python
position = (0, 0)
heading = 0
destinations = [(1, 3), (3, 3), (3, 0), (0, 0)]

print("Planned path for leg 1:", compute_bfs_path(position, destinations[0]))
board.wait_for_button()

total_steps = 0
total_reroutes = 0

for i in range(len(destinations)):
    dest = destinations[i]
    print("--- Leg", i + 1, ": Heading to", dest, "---")

    position, heading, steps, reroutes = navigate_with_detection(
        position, heading, dest, rangefinder, OBSTACLE_CM
    )

    total_steps = total_steps + steps
    total_reroutes = total_reroutes + reroutes
    print("  Arrived at", dest)

print("=== FINAL REPORT ===")
print("Total steps:", total_steps)
print("Total reroutes:", total_reroutes)
print("Obstacles discovered:", BLOCKED)
```

Then simulate: `simulate_rangefinder(next_pos)` with three pretend obstacles, robot on blocks. The whole four-leg run should play out on screen, `BLOCKED` growing across legs, and the final list should be the one they would type in for Run 2. Do Run 2 in simulation too.

### Day 2: Drive
Real sensor, real obstacles on the printed path. Run 1: record reroutes and steps, copy the obstacle list into `KNOWN_OBSTACLES`. Run 2: record again. Debug with the printed paths first -- if the path is right and the robot goes wrong, it is the driving (Module 4), not the planner.

### Day 3: Demos
Each team runs twice in front of the class and states the numbers: "Run 1 took X steps with Y reroutes; Run 2 took A with B." Ask *why* Run 2 is better; listen for "better data".

### Assessment: rubric
| Category | Points | What it takes |
|---|---|---|
| BFS pathfinding | 10 | Correct shortest paths; the Lesson 6 tests pass |
| Driving integration | 10 | Robot physically drives the computed paths, leg after leg |
| Obstacle detection | 10 | Rangefinder detects and `add_blocked()` updates the list |
| Re-planning | 10 | Reroutes correctly around discovered obstacles |
| Experience | 10 | Run 1 prints what it found; Run 2 starts from that list |
| Demonstration | 5 | Run 1 discovers and reroutes; Run 2 avoids known obstacles |
| Code quality | 5 | Readable, uses functions, meaningful comments |

## Common Integration Bugs
- **Leg 2 turns the wrong way and tracks off the grid.** `navigate_with_detection()` was called without assigning `position, heading` from its return value; leg 2 was planned from (0, 0) facing north.
- **The robot forgets an obstacle between legs.** `clear_blocked()` was called, or `BLOCKED` was re-created, inside the destination loop. One list for the whole run.
- **"No path to (3, 0)!" and the leg is skipped.** The destination is in `KNOWN_OBSTACLES` (or was just detected). Move the obstacle or the destination.
- **Run 2 is no better.** `KNOWN_OBSTACLES` is still empty -- the list was printed but never typed in.

## Differentiation
- **Support:** Two destinations instead of four; `navigate_with_detection()` given complete.
- **Extension:** Visit the nearest unvisited destination next (compare path lengths from the current position). Obstacle expiration: re-check a known obstacle after N runs. `print_grid()` after each leg. A `Navigator` object that owns `position` and `heading`, so the loop has nothing to pass back and forth.
- **Class track:** `Navigator` + `BFS` objects. Same rubric.

## Teaching Notes
- Insist on the simulation before the robot, for everyone. Logic first, hardware second.
- Use the rubric as a self-assessment checklist; each row maps to a lesson.
- Mark the distance travelled: from "Hello, World" to a robot that navigates, senses and learns. Say so out loud.

## Course Wrap-up
Module 1 Python foundations; Module 2 sensors and functions; Module 3 the grid; Module 4 Manhattan pathfinding and turning at intersections; Module 5 graphs, BFS, sensing and learning. The plan-vs-drive split (a planner that is *told* where the robot is; driving functions that do not know what a path is) and the shared planner interface are ideas students will meet again in any serious software work. If there is time, **Module 6** adds Dijkstra's algorithm as a third planner behind the same interface.
