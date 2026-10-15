# Lesson 9 Worksheet: Capstone Planning and Demo Record

**Team:** ________________________
**Date:** ________________________

---

## Part A: Where does each line come from?

Next to each line of the skeleton, write the lesson it was built in (4-8, 5-4, 5-5, 5-6, 5-7, 5-8).

| Skeleton line | Lesson |
|---|---|
| `for intersection in KNOWN_OBSTACLES: add_blocked(intersection)` | ____ |
| `compute_bfs_path(position, destination)` | ____ |
| `print("Planned path for leg 1:", ...)` before `wait_for_button()` | ____ |
| `distance = rangefinder.distance()` between `turn_to()` and `track_to_intersection()` | ____ |
| `while not arrived:` with the `rerouted` flag | ____ |
| `turn_to()`, `track_to_intersection()`, `drive_past_intersection()` | ____ |

## Part B: The destination loop

```python
for i in range(len(destinations)):
    dest = destinations[i]
    ______________________________ = navigate_with_detection(
        position, heading, dest, rangefinder, OBSTACLE_CM
    )
    total_steps = total_steps + steps
    total_reroutes = total_reroutes + reroutes
```

1. Fill in the left-hand side of the assignment.

2. A team leaves the left-hand side off and just calls `navigate_with_detection(...)`. Leg 1 works. Describe what leg 2 does and why.

_______________________________________________________________

_______________________________________________________________

3. Why does the program print only leg 1's path before the button, not all four?

_______________________________________________________________

4. The blocked list is "the thread" through the program. List the four places it is filled, read, added to, or reported -- and the one function three of them use.

_______________________________________________________________

## Part C: Predict, then simulate

Destinations: `[(1, 3), (3, 3), (3, 0), (0, 0)]`. Pretend obstacles for `simulate_rangefinder`: `[(1, 0), (2, 2), (1, 3)]`.

5. One of those three obstacles is going to cause "No path!" Which one, and why?

_______________________________________________________________

6. Fix it (move the obstacle or the destination), then run the simulation. Record:

   Legs completed: ____  Total steps: ____  Reroutes: ____  Final `BLOCKED`: ______________________

7. Now type that list into `KNOWN_OBSTACLES` and simulate again. Reroutes: ____  Steps: ____

## Part D: Demo record

| | Run 1 | Run 2 |
|---|---|---|
| `KNOWN_OBSTACLES` at start | `[]` | ______________________ |
| Destinations reached | ____ / 4 | ____ / 4 |
| Reroutes | ____ | ____ |
| Total steps | ____ | ____ |
| Obstacles printed at end | ______________________ | ______________________ |

8. In one sentence, why is Run 2 better? (Not "the robot is smarter".)

_______________________________________________________________

## Part E: Integration bugs we hit

For each bug you ran into, write the symptom and the fix.

| Symptom | Cause / fix |
|---|---|
| | |
| | |
| | |

## Self-assessment against the rubric

| Category | Points | Our estimate |
|---|---|---|
| BFS pathfinding (Lesson 6 tests pass) | 10 | ____ |
| Driving integration | 10 | ____ |
| Obstacle detection | 10 | ____ |
| Re-planning | 10 | ____ |
| Experience (Run 2 starts from Run 1's list) | 10 | ____ |
| Demonstration | 5 | ____ |
| Code quality | 5 | ____ |

---

## Answer Key

**Part A:** 5-8; 5-5 (interface from 5-4); 5-7; 5-7; 5-8; 4-8.
**1.** `position, heading, steps, reroutes`
**2.** Leg 2 is planned from (0, 0) facing north, but the robot is at (1, 3) facing some other way, so it turns the wrong way and tracks off the grid (or to the wrong intersection).
**3.** Later legs are planned from wherever the previous leg actually ends, with whatever obstacles have been found by then -- neither is known before the robot moves.
**4.** Filled from `KNOWN_OBSTACLES`; read by `compute_bfs_path()` on every call; added to by the rangefinder check; printed at the end. `add_blocked()` for the first and third (and the Lesson 6 tests).
**5.** (1, 3) -- it is also the first destination. The planner returns `[]` for a blocked destination and the leg is skipped.
**8.** It started out knowing the obstacles, so its first paths already avoided them: same algorithm, better data.
