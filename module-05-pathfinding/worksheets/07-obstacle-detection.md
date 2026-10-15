# Lesson 7 Worksheet: Obstacle Detection

**Name:** ________________________
**Date:** ________________________

---

## Part A: Rangefinder basics

1. Write the three lines that import the rangefinder, get the default one, and read a distance into a variable called `distance`.

```python
_______________________________________________

_______________________________________________

_______________________________________________
```

2. In one sentence, how does an ultrasonic rangefinder measure distance?

_______________________________________________________________

3. You measured 11.8 cm, 12.4 cm and 11.5 cm with a box on the next intersection, and 46 cm, 51 cm and 48 cm with it clear. Circle a good value for `OBSTACLE_CM`:   5   15   30   45

   Why not 12?  _______________________________________________

4. Why is the constant called `OBSTACLE_CM` and not `THRESHOLD`?

_______________________________________________________________

## Part B: Which intersection is blocked?

Here is Module 4's driving loop with the new line added.

```python
for next_pos in path:
    needed = desired_heading(position, next_pos)
    heading = turn_to(heading, needed)
    distance = rangefinder.distance()          # <-- new
    ...
```

5. The robot is at (2, 1). Its path is `[(1, 1), (0, 1), (0, 2)]`. On the first time through the loop, after `turn_to()`, which intersection is the robot facing? ________

6. The rangefinder reads 9 cm. Which intersection is blocked? ________ Which function do you call, with what argument?

   `__________________( __________ )`

7. Your partner moved the `rangefinder.distance()` line *above* `turn_to()`. Explain what goes wrong.

_______________________________________________________________

_______________________________________________________________

## Part C: Re-planning

8. After `add_blocked(next_pos)`, write the one line that asks for a new path from where the robot is.

```python
path = _________________________________________
```

9. Your partner adds `graph = build_graph(ROWS, COLS, BLOCKED)` before that line "so the planner knows about the new wall". Is it needed? Why or why not?

_______________________________________________________________

10. Why is the robot sitting exactly over an intersection when it re-plans? (Which Module 4 function guarantees it?)

_______________________________________________________________

## Part D: Trace

Grid 3x3, start (0, 0), destination (2, 2), `BLOCKED` empty. The planner prints `Planned path: [(1, 0), (2, 0), (2, 1), (2, 2)]`. There is a box on (2, 0).

11. Fill in what happens, step by step:

| Loop pass | position | next_pos | reading | action |
|---|---|---|---|---|
| 1 | (0, 0) | (1, 0) | 50 cm | track, drive past, position = (1, 0) |
| 2 | ________ | ________ | 9 cm | ______________________________ |

12. After the reroute, `BLOCKED` is `________________` and the new path is planned from `________`. Write one possible new path: `______________________________`

## Part E: Simulate first

13. Complete the fake sensor:

```python
simulated_obstacles = [(2, 0)]

def simulate_rangefinder(next_pos):
    if next_pos in simulated_obstacles:
        return ________
    else:
        return ________
```

14. What is being simulated -- the sensor, the planner, or both? Why doesn't the planner need simulating?

_______________________________________________________________

## Exit ticket

Why can the planner not tell whether a wall was reported by the Lesson 6 test script or by the rangefinder?

_______________________________________________________________

---

## Answer Key

**1.** `from XRPLib.rangefinder import Rangefinder` / `rangefinder = Rangefinder.get_default_rangefinder()` / `distance = rangefinder.distance()`
**2.** Sends a sound pulse and times the echo; the round-trip time gives the distance.
**3.** 15. 12 sits inside the blocked readings' noise (11.5-12.4), so a real box would sometimes read as clear.
**4.** `THRESHOLD` is already the reflectance cutoff (0-1) from Lesson 2-8; two settings with one name is a bug waiting to happen.
**5.** (1, 1). **6.** (1, 1); `add_blocked((1, 1))`.
**7.** The reading is taken facing whatever direction the robot happened to be left in, not `next_pos`; a clear (or blocked) reading gets blamed on the wrong intersection.
**8.** `compute_bfs_path(position, destination)`
**9.** Not needed. `compute_bfs_path()` calls `build_graph()` from `BLOCKED` on every call (Lesson 4), so the new wall is already gone from the graph it uses.
**10.** `drive_past_intersection()` runs after every `track_to_intersection()`, parking the wheels over the intersection.
**11.** Pass 2: position (1, 0), next_pos (2, 0), 9 cm: `add_blocked((2, 0))`, re-plan from (1, 0), break.
**12.** `[(2, 0)]`; (1, 0); e.g. `[(1, 1), (1, 2), (2, 2)]` or `[(1, 1), (2, 1), (2, 2)]`.
**13.** 8.0 (anything under `OBSTACLE_CM`) and 50.0.
**14.** Only the sensor. The planner was tested on paper in Lesson 6 and is unchanged.
**Exit ticket:** Both call `add_blocked()`; the planner only ever reads `BLOCKED`.
