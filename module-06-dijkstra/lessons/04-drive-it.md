# Lesson 4: Drive It

## Overview
The robot drives the slow grid twice: the same trip planned by BFS, then by Dijkstra, with the class timing both. The program is Module 4's driving toolkit plus the two planners; the only Module 6 line is which planner the name `planner` is set to (the Lesson 5-6 swap). Before the button it prints *both* plans with their steps and costs, so the comparison is on screen before either run. BFS takes fewer steps; Dijkstra arrives first; the stopwatch agrees with the cost column. Nothing in the driving changes, because `drive_path()` drives lists and never knew what a path meant.

## Learning Objectives
By the end of this lesson, students will be able to:
- Type the measured slow segment into the program with `add_slow_edge()`
- Choose the planner by assigning a function to a name, and print both plans and costs before the button
- Time two runs and relate the seconds to the costs
- Explain why the driving functions did not change

## Key Concepts
- **One name changes**: `planner = compute_dijkstra_path` or `compute_bfs_path`; `path = planner(position, destination)`.
- **Print both plans before the button**: the comparison, and the paper test, on screen first.
- **Cost predicts time**: at about 4 s a block, cost 5 is about 20 s and cost 7 about 28 s.
- **Turns cost time too**: the detour has more of them, so the measured gap is usually a little smaller than the cost gap predicts. A planner that weights turns would need the heading -- a bigger change than two lines, and out of scope.
- **Same plans = setup problem**: no slow edge typed in, or weight 3 or less.

## Materials Required
- XRP robot; the slow-segment grid; a stopwatch
- `code/starter/lesson-04-drive-it.py` (slow segment and planner choice as TODOs); `code/solutions/lesson-04-drive-it.py`
- `worksheets/04-drive-it.md`

## Lesson Flow

### Introduction (5 minutes)
Put the main program on the board. Ask which lines are new since Module 5: `add_slow_edge(...)`, and the choice of `planner`. Everything else -- `desired_heading`, `turn_to`, `drive_path`, the toolkit -- is Module 4.

### Guided Practice (15 minutes)
1. Type the Lesson 1 slow segment into `SLOW_SEGMENT`. Run with `PLANNER_NAME = "BFS"`. Read both printed plans aloud; from the costs and the per-block time, predict both run times. Press the button; stopwatch; record.
2. `PLANNER_NAME = "Dijkstra"`. Same start, same destination. Predict, run, record.
3. Fill in the table on the board:
   ```
   Planner    steps   cost   predicted s   measured s
   BFS         3       7        28           ___
   Dijkstra    5       5        20           ___
   ```

### Independent Practice (25 minutes)
Teams repeat the two runs with their own robots and a second destination of their choosing (one where the slow road is the fewest-steps route). Worksheet table. Discuss the discrepancy between predicted and measured: turns.

### Assessment
- **Formative:** the two-run table, with costs and times that agree.
- **Exit ticket:** "In one sentence, why did the 5-step route win?"

## Common Issues
- **Both plans identical**: `SLOW_SEGMENT` not typed in, or weight too small. Fix the setup, not the code.
- **Measured gap smaller than predicted**: turns cost time; expected. Count the turns in each plan.
- **Robot loses the line on the detour**: curves too tight for line following; gentler tape.

## Teaching Notes
- Make it a class event: both runs back to back, one student on the stopwatch, predictions on the board first. The robot visibly choosing the long way and arriving sooner is the module's payoff.
- `elapsed` printed by the program is a check on the stopwatch.

## Connections to Next Lessons
- **Lesson 5 (extension)**: the `Dijkstra` class and three planner objects through one harness. For everyone else the course ends here.
