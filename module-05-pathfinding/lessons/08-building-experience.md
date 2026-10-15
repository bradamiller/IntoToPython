# Lesson 8: Building Experience

## Overview
Lesson 7 detected one obstacle, re-planned once, and stopped with a `break`. This lesson finishes the job in two moves. First, the loop should *keep going*: follow the new path, re-plan again if it meets another wall, and stop only when the robot arrives. That is a `while not arrived` loop around Lesson 7's `for`, with a `rerouted` flag so the `while` can tell whether the `for` finished or broke out early. The result is `navigate_with_detection(position, heading, destination, rangefinder, obstacle_cm)`, which returns the robot's new position and heading along with step and reroute counts.

Second, the robot rediscovers every obstacle from scratch each run -- like being surprised by the same construction zone every morning. The fix is not a smarter algorithm but better data: start Run 2 knowing what Run 1 found. The program prints `BLOCKED` at the end of a run; the student types that list into `KNOWN_OBSTACLES` at the top of the program, and a two-line loop hands each one to `add_blocked()`. **The student is the memory.** This is deliberate: it keeps "same algorithm, better data" in the student's own fingers, and it keeps file I/O, `with` and `try/except` out of a module about graph search (nothing else in the course uses them). The lesson says plainly that a real system would store the list itself, and that *what* gets carried is identical either way.

Students measure the improvement -- steps and reroutes for Run 1 and Run 2 -- because "it seemed faster" is not evidence. The Waze analogy carries the idea: one driver's traffic report helps everyone behind them.

## Learning Objectives
By the end of this lesson, students will be able to:
- Wrap Lesson 7's detect-and-reroute step in a `while not arrived` loop and explain the `rerouted` flag
- Explain why `navigate_with_detection()` returns `position` and `heading`
- Explain what happens when `compute_bfs_path()` returns `[]` inside the loop and why the check matters
- Explain why remembering obstacles improves navigation without changing the algorithm
- Start a run with `KNOWN_OBSTACLES` fed to `add_blocked()`, so the planner avoids them from the first path
- Compare Run 1 and Run 2 with recorded metrics (steps, reroutes)
- Explain the GPS/Waze analogy and the idea of convergence

## Key Concepts
- **Plan, follow, plan again**: `while not arrived:` plan a path; `for next_pos in path:` turn, look, drive; if the sensor fires, `add_blocked(next_pos)`, set `rerouted = True`, `break`; after the `for`, `if not rerouted: arrived = True`.
- **The `rerouted` flag**: The only new Python idea. A `for` loop cannot tell its enclosing `while` whether it finished or broke out; a boolean set just before the `break` does.
- **Returning state**: `position` and `heading` are local inside the function. The caller needs their new values to plan the next trip (Lesson 9), so the function returns them: `return position, heading, step_count, reroute_count`.
- **The empty-path check**: If the robot is boxed in, `compute_bfs_path()` returns `[]`. Without the check the `for` runs zero times, `rerouted` stays `False`, and the robot declares itself arrived at the wrong intersection.
- **Same algorithm, better data**: Run 2 runs the identical planner on a blocked list that starts with Run 1's discoveries.
- **`KNOWN_OBSTACLES`**: The printed list from the last run, typed in, handed to `add_blocked()` one by one. The planner has now been told about walls three ways -- test script, rangefinder, typed-in list -- and all three are the same call.
- **Convergence**: Run 2 may still find something new on a route Run 1 never drove; eventually the robot knows every relevant obstacle and its first path is right.

## Materials Required
- XRP robot with rangefinder, the grid, 2-3 obstacles
- `code/starter/lesson-08-experience.py`; `code/solutions/lesson-08-experience.py`
- A results table on the board: Run 1 / Run 2, reroutes / steps, per team

## Lesson Flow

### Introduction (10 minutes)
Ask what Lesson 7's robot did after its first reroute. (It stopped -- the `break`.) Ask what it should do. (Follow the new path, and if there is another wall, re-plan again, until it arrives.) Then ask what the robot knows at the start of its second run that it did not know at the start of its first. (Nothing. `BLOCKED` starts empty every time the program starts.)

Waze: "What if Waze forgot every traffic report when you closed the app?" Same algorithm every day; what changes is the data it starts with.

### Guided Practice (15 minutes)
Trace the loop on the board with a path that hits one wall:

```python
def navigate_with_detection(position, heading, destination, rangefinder, obstacle_cm):
    step_count = 0
    reroute_count = 0

    arrived = False
    while not arrived:
        path = compute_bfs_path(position, destination)
        print("  Path from", position, ":", path)

        if len(path) == 0:
            print("No path to", destination, "!")
            return position, heading, step_count, reroute_count

        rerouted = False
        for next_pos in path:
            needed = desired_heading(position, next_pos)
            heading = turn_to(heading, needed)

            distance = rangefinder.distance()
            if distance < obstacle_cm:
                add_blocked(next_pos)
                print("  OBSTACLE at", next_pos, "! Rerouting...")
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

    return position, heading, step_count, reroute_count
```

Walk it: plan from (0, 0); follow two steps; sensor fires at the third; `add_blocked`, `rerouted = True`, `break`; back at the `while`, `arrived` is still `False`, so plan again -- from (2, 0), where the robot is parked; follow the new path to the end; the `for` finishes, `rerouted` is `False`, `arrived = True`. Then ask what would happen without the `len(path) == 0` check if the robot were boxed in.

Point at the `return`. "`position` and `heading` are variables inside this function. If the caller wants to know where the robot ended up -- and next lesson it will -- how does it find out?"

### Independent Practice (20 minutes)
1. **Complete the function** from the starter's TODOs and run it with Lesson 7's `simulate_rangefinder()` and two pretend obstacles on the printed path. Confirm two reroutes and an arrival on screen.
2. **Run 1 on the grid.** Place 2-3 obstacles on the printed path. Record reroutes and steps from the run report. Copy the `All known obstacles:` line.
3. **Carry it across.** Type that list into the top of the program:
   ```python
   KNOWN_OBSTACLES = [(1, 2), (2, 2), (3, 0)]      # what Run 1 discovered

   for intersection in KNOWN_OBSTACLES:
       add_blocked(intersection)
   ```
4. **Run 2.** Same obstacles, same destination. Record reroutes and steps. Fill in the table:
   ```
   Metric              Run 1    Run 2
   Starting obstacles    0       (from Run 1)
   Reroutes            ____     ____
   Total steps         ____     ____
   ```
5. **Discuss:** Could Run 2 find an obstacle Run 1 never did? (Yes -- its route may pass intersections Run 1 never visited.) What would Run 3 start with?

### Assessment
- **Formative:** trace the `while` loop through one reroute; explain the `rerouted` flag; pre-load a blocked list.
- **Exit ticket:** "Run 1 took 12 steps / 3 reroutes; Run 2 took 8 / 0. Explain why." Listen for "better data", not "smarter robot".
- **Worksheet:** `worksheets/08-building-experience.md`.

## Common Misconceptions
- **"Run 2 uses a better algorithm."** Identical code. Only `BLOCKED`'s starting contents differ.
- **"The robot remembers between runs."** A Python list lives only while the program runs. If `KNOWN_OBSTACLES` is empty, Run 2 is Run 1 again.
- **"The `for` loop finishing means we arrived."** Only if it finished *without* a reroute -- hence the flag. Breaking out early also ends the `for`.
- **"I can leave out the empty-path check; BFS always finds a path."** Not on a boxed-in grid. Without it the robot reports arrival without moving.
- **"Put the known obstacles in `BLOCKED` directly."** It works, but routing them through `add_blocked()` keeps the rule that everything reaches the planner the same way -- and on the class track, `BLOCKED` is inside the planner object and only `add_blocked()` can reach it.

## Differentiation
- **Support:** Give `navigate_with_detection()` complete; students do Runs 1 and 2 and the table. The point of the lesson survives.
- **Extension:** What if an obstacle *moves*? Real systems forget stale data. Have students design (not build) a rule for when to re-check a known obstacle. Or: `print_grid()` after each re-plan with `BLOCKED` shown.
- **Class track:** `Navigator` owns `position` and `heading`, so the method is `navigator.navigate_with_detection(destination, rangefinder, obstacle_cm)` and returns only the counts. Ask why the return value got shorter.

## Materials & Code Examples

### Main program (solution)
```python
OBSTACLE_CM = 15

KNOWN_OBSTACLES = []          # e.g. [(1, 2), (2, 2)] after Run 1
for intersection in KNOWN_OBSTACLES:
    add_blocked(intersection)

position = (0, 0)
heading = 0
destination = (3, 3)

print("Planned path:", compute_bfs_path(position, destination))
board.wait_for_button()

position, heading, steps, reroutes = navigate_with_detection(
    position, heading, destination, rangefinder, OBSTACLE_CM
)

print("Total steps:", steps)
print("Reroutes:", reroutes)
print("All known obstacles:", BLOCKED)
```

### Expected output, Run 1 (obstacle at (2, 0))
```
Planned path: [(1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3)]
  Path from (0, 0) : [(1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3)]
  OBSTACLE at (2, 0) ! Rerouting...
  Path from (1, 0) : [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3)]
Total steps: 6
Reroutes: 1
All known obstacles: [(2, 0)]
```
Run 2 with `KNOWN_OBSTACLES = [(2, 0)]`: one path, six steps, zero reroutes.

## Teaching Notes
- Spend the first fifteen minutes on the `while` loop. The flag is the one new idea; everything else is Lesson 7.
- Set up the grid so Run 1 has 2-3 reroutes. The contrast with a zero-reroute Run 2 is the "aha".
- Carrying the list by hand is the point, not a shortcut. If a student asks why the robot can't save it itself: good question, that is exactly what a real one does, and it changes nothing about what is carried.
- Insist on recorded numbers. The table convinces far more than "it felt faster".

## Connections to Next Lessons
- **Lesson 9** calls `navigate_with_detection()` once per destination, feeding each trip's returned position and heading into the next.
- **Module 6 (optional)** reuses this loop unchanged with `compute_dijkstra_path`.
