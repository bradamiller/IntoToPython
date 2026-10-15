# Lesson 8 Worksheet: Building Experience

**Name:** ________________________
**Date:** ________________________

---

## Part A: From `break` to "until you arrive"

```python
arrived = False
while not arrived:
    path = compute_bfs_path(position, destination)
    if len(path) == 0:
        print("No path!")
        return position, heading, step_count, reroute_count

    rerouted = False
    for next_pos in path:
        needed = desired_heading(position, next_pos)
        heading = turn_to(heading, needed)
        distance = rangefinder.distance()
        if distance < obstacle_cm:
            add_blocked(next_pos)
            reroute_count = reroute_count + 1
            rerouted = True
            break
        else:
            track_to_intersection()
            drive_past_intersection()
            position = next_pos
            step_count = step_count + 1

    if not rerouted:
        arrived = True
```

1. A `for` loop ends in two different ways in this code. Name both.

   a) ______________________________   b) ______________________________

2. What is the job of the `rerouted` variable? Why can't the `while` loop tell on its own?

_______________________________________________________________

3. Cross out the `if len(path) == 0:` block in your head. The robot is boxed in and `compute_bfs_path()` returns `[]`. How many times does the `for` loop run? ______ What is `rerouted` afterward? ______ What does the robot report? ______________________

4. `position` and `heading` are variables *inside* the function. Why does the function return them?

_______________________________________________________________

## Part B: Trace a run

Grid 4x4, start (0, 0), destination (3, 3), `BLOCKED` empty. Boxes on (2, 0) and (1, 2). The first plan is `[(1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3)]`.

5. Fill in each pass of the `while` loop. (BFS may choose a different equally short path; use the one given or your own.)

| `while` pass | planned from | path | what happens |
|---|---|---|---|
| 1 | (0, 0) | `[(1,0),(2,0),(3,0),(3,1),(3,2),(3,3)]` | drive to (1,0); box seen at (2,0); reroute |
| 2 | ________ | `[(1,1),(1,2),(1,3),(2,3),(3,3)]` | ______________________________________ |
| 3 | ________ | ______________________________ | ______________________________________ |

6. Final `BLOCKED`: `____________________`   Reroutes: ____   Steps: ____

## Part C: Carry it across

7. The program prints `All known obstacles: [(2, 0), (1, 2)]`. You close it and run it again with no changes. What does `BLOCKED` contain when the second run starts? ________ Why?

_______________________________________________________________

8. Write the lines that go at the top of the program so Run 2 starts knowing both obstacles. Use `add_blocked()`.

```python
KNOWN_OBSTACLES = _______________________________

_______________________________________________

    _______________________________________________
```

9. For Run 2 from the same start to the same destination with the same boxes: how many reroutes do you predict? ____ Will the first planned path differ from Run 1's? How?

_______________________________________________________________

10. The planner has now been told about walls in three different ways across Lessons 6, 7 and 8. Name them, and name the one function all three call.

_______________________________________________________________

## Part D: Evidence

11. Fill in from your own two runs:

| Metric | Run 1 | Run 2 |
|---|---|---|
| Starting obstacles | 0 | ____ |
| Reroutes | ____ | ____ |
| Total steps | ____ | ____ |

12. Your partner says "Run 2 used a smarter algorithm." Correct them in one sentence.

_______________________________________________________________

13. Can Run 2 discover an obstacle Run 1 never found? Explain.

_______________________________________________________________

## Exit ticket

Run 1 took 12 steps with 3 reroutes; Run 2 took 8 steps with 0. Explain why.

_______________________________________________________________

---

## Answer Key

**1.** Running off the end of `path`; `break` after a detection.
**2.** It tells the `while` whether the `for` finished or broke out. A `for` finishing looks the same either way; the flag is set only on the `break` path.
**3.** Zero times; `False`; it sets `arrived = True` and reports arrival without moving.
**4.** The caller needs the robot's actual end position and heading to plan the next trip (Lesson 9); local variables are not visible outside the function.
**5.** Pass 2: from (1, 0); drive to (1, 1); box seen at (1, 2); reroute. Pass 3: from (1, 1); e.g. `[(2,1),(3,1),(3,2),(3,3)]` or `[(2,1),(2,2),(2,3),(3,3)]`; drives it, no reroute, arrived.
**6.** `[(2, 0), (1, 2)]`; 2; 6.
**7.** Empty -- a list lives only while the program runs.
**8.** `KNOWN_OBSTACLES = [(2, 0), (1, 2)]` / `for intersection in KNOWN_OBSTACLES:` / `add_blocked(intersection)`
**9.** 0; yes -- it avoids both boxes from the start, e.g. `[(1,0),(1,1),(2,1),(3,1),(3,2),(3,3)]`.
**10.** Test script (L6), rangefinder (L7), typed-in `KNOWN_OBSTACLES` (L8); all call `add_blocked()`.
**12.** Same code; only the starting contents of `BLOCKED` changed.
**13.** Yes -- a different route can pass intersections Run 1 never drove toward.
**Exit ticket:** Run 2 started knowing the three obstacles, so its first path already avoided them: no reroutes, and no wasted steps toward walls.
