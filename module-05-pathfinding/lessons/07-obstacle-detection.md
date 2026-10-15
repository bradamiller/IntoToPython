# Lesson 7: Obstacle Detection with the Rangefinder

## Overview
Students put the planner on the robot. Until now the blocked list has been filled in by a test script (Lesson 6). In this lesson the robot fills it in itself with the ultrasonic rangefinder: it looks before it drives, and if something is in the way it calls `add_blocked()` -- the same call the paper tests made -- and asks `compute_bfs_path(position, destination)` for a new path from where it is.

The driving is Module 4's, unchanged. The whole lesson is one step added to Module 4's `drive_path()` loop, between `turn_to()` and `track_to_intersection()`: read the rangefinder. Because the robot has just turned to face `next_pos`, whatever the sensor sees is at `next_pos`; there is no heading arithmetic to work out which intersection is blocked. The planner rebuilds its graph from `BLOCKED` on every call (Lesson 4), so re-planning is one line with no "rebuild" step to forget. Students also pick up the habit the rest of the module relies on: plan, *print the path*, wait for the button, then drive -- the Lesson 6 paper test built into every run.

Detection is proven in software first with a simulated rangefinder, then on the grid with a box on an intersection of the printed path. Students who did the class extensions run the same loop with `Navigator` and `BFS` objects; nothing in the lesson changes.

## Learning Objectives
By the end of this lesson, students will be able to:
- Initialize the XRP rangefinder and read a distance with `rangefinder.distance()`
- Explain how an ultrasonic rangefinder measures distance (sound pulse, echo, time)
- Use a threshold constant, `OBSTACLE_CM`, to decide whether the intersection ahead is blocked, and explain why it is not named `THRESHOLD`
- Explain why the blocked intersection is `next_pos`: the robot just turned to face it
- Add one rangefinder check to Module 4's `drive_path()` loop, call `add_blocked(next_pos)` and re-plan with `compute_bfs_path(position, destination)` when it fires
- Explain why no separate "rebuild the graph" step is needed
- Print the planned path before `wait_for_button()` and use it as the first diagnostic
- Test the detection loop with a simulated rangefinder before the real one

## Key Concepts
- **Ultrasonic rangefinder**: Emits a sound pulse and times the echo; returns centimeters as a float. Three lines: import, `Rangefinder.get_default_rangefinder()`, `.distance()`.
- **`OBSTACLE_CM = 15`**: A threshold absorbs sensor noise; an exact-distance check would fail constantly. Named for what it measures because the file already has a `THRESHOLD` (the reflectance one from Lesson 2-8).
- **The blocked intersection is `next_pos`**: After `heading = turn_to(heading, needed)` the robot faces the next step on the path. The path already says which intersection that is.
- **One call tells the planner**: `add_blocked(next_pos)`. The planner cannot tell a sensor from a test script from a typed-in list; all three call the same function. That is why passing the Lesson 6 tests means the robot will re-plan correctly.
- **Re-plan from here**: `compute_bfs_path(position, destination)` -- Rule 1 from Lesson 4. The graph is rebuilt from `BLOCKED` inside the planner, so the wall it was just told about is already gone.
- **The robot is parked when it re-plans**: `drive_past_intersection()` runs after every track, so the wheels are over the intersection the robot re-plans from. Nothing moves during a re-plan.
- **Print-then-button-then-drive**: `print("Planned path:", path)` before `board.wait_for_button()`. If the printed path is right and the robot still goes wrong, the bug is in the driving, not the planner.
- **Simulated sensor**: `simulate_rangefinder(next_pos)` returns 8.0 for a pretend obstacle and 50.0 otherwise. Only the sensor is simulated; the planner was already tested in Lesson 6.

## Materials Required
- XRP robot with the ultrasonic rangefinder mounted facing forward
- The Module 3/4 grid, at least 3x3, preferably 4x4
- Obstacles the rangefinder can see: boxes, books, water bottles (hard, flat faces read best)
- `code/starter/lesson-07-obstacle-detection.py`; `code/solutions/lesson-07-obstacle-detection.py`
- Ruler or tape measure for calibrating `OBSTACLE_CM`

## Lesson Flow

### Introduction (10 minutes)
Open with the question: "Last lesson a test script told the planner where the walls were. Who tells it today?" Hold up the rangefinder. Three lines read it:

```python
from XRPLib.rangefinder import Rangefinder

rangefinder = Rangefinder.get_default_rangefinder()
print(rangefinder.distance())
```

Have one team run this while another student walks a box toward the robot; the numbers fall as the box approaches. Ask what number should count as "blocked". Measure with the next intersection blocked (about 12 cm on a typical grid) and clear (40-50 cm), and pick a cutoff between: `OBSTACLE_CM = 15`. Explain the name: the file already has `THRESHOLD` for the reflectance sensors, and two settings called the same thing is a bug waiting to happen.

Then the question that used to confuse students: *which* intersection is blocked? Stand on an intersection of the taped grid. Put Module 4's loop on the board:

```python
for next_pos in path:
    needed = desired_heading(position, next_pos)
    heading = turn_to(heading, needed)
    track_to_intersection()
    drive_past_intersection()
    position = next_pos
```

Turn to face the next intersection on a path, and point at it. "After `turn_to()`, I am facing `next_pos`. That is what turning to the needed heading *means*. If the sensor sees something right now, where is it?" The path already told them.

### Guided Practice (15 minutes)
Build the loop together. It is Module 4's `drive_path()` with one step inserted between turning and driving:

```python
for next_pos in path:
    needed = desired_heading(position, next_pos)
    heading = turn_to(heading, needed)

    distance = rangefinder.distance()          # NEW: look before driving
    if distance < OBSTACLE_CM:
        add_blocked(next_pos)                   # same call the tests made
        print("Obstacle at", next_pos, "! Rerouting...")
        path = compute_bfs_path(position, destination)
        print("New path:", path)
        break                                   # Lesson 8 wraps this in a loop
    else:
        track_to_intersection()
        drive_past_intersection()
        position = next_pos
```

Draw out three points. First, `add_blocked(next_pos)` is the Lesson 6 call; the planner cannot tell where a block came from. Second, re-planning is one call from the current position, and there is no "rebuild the graph" line because `compute_bfs_path()` builds its graph from `BLOCKED` every time (Lesson 4 put `build_graph()` inside the planner for exactly this moment). Third, the robot is parked over an intersection when this happens -- `drive_past_intersection()` ran after the last track -- so when the loop comes back to turn toward the new path's first step, nothing has moved.

Then add the habit: before the button, plan and print.

```python
path = compute_bfs_path(position, destination)
print("Planned path:", path)
board.wait_for_button()
```

"Read the path before you press the button. Is it what you expected?" This is the Lesson 6 paper test built into every run and the first diagnostic when something goes wrong.

### Independent Practice (20 minutes)
Students complete the TODOs in the starter: the rangefinder setup, the check inside the loop, and the print before the button.

1. **Simulate first.** Replace `rangefinder.distance()` with `simulate_rangefinder(next_pos)`:
   ```python
   simulated_obstacles = [(1, 1), (2, 2)]

   def simulate_rangefinder(next_pos):
       return 8.0 if next_pos in simulated_obstacles else 50.0
   ```
   Run with the robot on blocks (wheels off the table). Confirm on screen that `BLOCKED` grows when the robot "sees" a pretend obstacle and that the new path goes around it. Note what is being simulated: only the sensor.
2. **Then the grid.** Swap the real `rangefinder.distance()` back in. Put a box on one intersection of the *printed* path. Press the button. The robot should stop at the intersection before the box, print "Rerouting...", print the new path, and take it.
3. **Calibrate.** If the robot reroutes with nothing there, or drives into the box, adjust `OBSTACLE_CM` and record the readings that led to the new value.

Early finishers: put the box on the new path too and watch the second reroute -- then notice the loop stops after the first `break`, which is Lesson 8's problem.

### Assessment
- **Formative:** the three rangefinder lines from memory; "which intersection is blocked, and how do you know?"; the one-line reroute.
- **Exit ticket:** "Why can the planner not tell a sensor from a test script?" (Both call `add_blocked()`.) "Why is there no rebuild-the-graph step?" (The planner rebuilds from `BLOCKED` on every call.)
- **Worksheet:** `worksheets/07-obstacle-detection.md`.

## Common Misconceptions
- **"The robot's own intersection is blocked."** The robot is *on* a clear intersection; the sensor looks ahead. The blocked one is `next_pos`, the step it just turned to face.
- **"After `add_blocked()` I have to rebuild the graph."** No -- `compute_bfs_path()` does it on every call. Students who did Module 4's `build_graph()` work sometimes want to call it again; point them at Lesson 4's reason for putting it inside the planner.
- **"Re-plan from the start."** Rule 1: tell the planner where the robot *is*. Planning from (0, 0) when the robot is at (2, 1) produces a path for the wrong place.
- **"I should check the sensor before turning."** Then the reading is for whichever direction the robot happens to face, not for `next_pos`. The order is turn, look, drive.
- **"Use `THRESHOLD`."** That name is taken by the reflectance cutoff. A sensor threshold in centimeters and a reflectance threshold between 0 and 1 cannot share a name.

## Differentiation
- **Support:** Give the loop complete and have students only add the two `print()` calls and the simulation swap. Have them narrate the loop aloud with the robot in hand: turn, look, drive.
- **Extension:** Average three rangefinder readings before deciding. Or: when the sensor fires, also `print_grid()` (Lesson 5) with the new block shown, before the new path.
- **Class track:** The same loop with `navigator.turn_to(needed)` and `planner.add_blocked(next_pos)` / `planner.compute_path(navigator.position, destination)`. The rangefinder read sits in the same place.

## Materials & Code Examples

### Rangefinder test
```python
from XRPLib.rangefinder import Rangefinder
import time

rangefinder = Rangefinder.get_default_rangefinder()
OBSTACLE_CM = 15

while True:
    distance = rangefinder.distance()
    if distance < OBSTACLE_CM:
        print(distance, "cm  OBSTACLE")
    else:
        print(distance, "cm  clear")
    time.sleep(0.5)
```

### The full program
See `code/solutions/lesson-07-obstacle-detection.py`. It is the Module 5 planner toolkit (Lessons 4-5), the Module 2 sensor and line-tracking functions, Module 4's `desired_heading()` / `turn_to()`, and the loop above with the print-then-button main. Run against the fake XRPLib it prints the planned path, then one reroute.

### Expected output (box at (1, 1), start (0, 0), destination (3, 3))
```
Planned path: [(1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3)]
```
That path does not pass (1, 1), so move the box onto it -- say (2, 0):
```
At (1, 0) facing N - ahead: 9.2 cm
Obstacle at (2, 0) ! Rerouting...
New path: [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3)]
```
(BFS may pick a different equally short path; that is Lesson 6's point.)

## Teaching Notes
- Calibrate `OBSTACLE_CM` yourself before class on your grid with your obstacles. Soft or angled surfaces read inconsistently -- a good real-world-sensor talking point, not a bug.
- Put demo obstacles *on the printed path* so the reroute is visible and dramatic. A box off the path proves nothing.
- The driving functions are Module 4's, unchanged. If the robot overshoots or misses a turn here, it did in Module 4 too; tune there, not here.
- Expect the question "why stop after one reroute?" -- that is next lesson, and students who ask it have understood this one.

## Connections to Next Lessons
- **Lesson 8** turns the `break` into a `while not arrived` loop that re-plans until the robot gets there, and starts Run 2 from the obstacles Run 1 found.
- **Lesson 9** chains several destinations through that loop.
- **Module 6 (optional)** swaps in `compute_dijkstra_path`; the rangefinder loop does not change.
