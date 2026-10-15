# Lesson 4: Module 3 Final Project -- The Square

## Overview
The robot drives a closed square on the grid: two intersections per side, a clockwise turn at each of four corners, back to the start. The whole square is a four-pass `for` loop whose body is `drive_intersections(sides)` then `turn_clockwise()`; students write that loop, test one side, then two, then four, and tune until the path closes. No new Python -- the Module 2 toolkits unchanged, Lesson 2's helper, and Lesson 3's ordering rule.

## Learning Objectives
By the end of this project, students will be able to:
- Design a program that drives a closed square path on the grid
- Use a `for` loop to repeat a drive-and-turn sequence
- Test incrementally and tune a real robot until the path closes
- Verify the robot returns to its starting intersection and heading

## Key Concepts
- **One loop, four sides**: each pass drives one side and turns the corner. Four clockwise turns are 360 degrees, so the robot returns to its starting heading as well as its starting intersection.
- **Nothing between the drive and the turn**: `drive_intersections()` parks the robot on the corner; the turn pivots there.
- **Incremental testing**: one side, two sides (predict the shape), four.
- **Tuning is the engineering**: the blind turn angle and `TURN_EFFORT` (square drifts open), the drive-past distance (sensor-to-axle), `BASE_EFFORT` (overshoots a corner).

## Materials Required
- XRP robot; the grid, at least 3x3 so a 2x2 square fits
- `code/starter/lesson-04-final-project.py` (toolkits and helper complete; the loop as TODOs); `code/solutions/lesson-04-final-project.py`
- `worksheets/04-final-project.md`; the rubric

## Lesson Flow (2 class periods)

### Day 1: Plan, build, test one side
1. **The mission.** Square, two intersections a side, clockwise at every corner, end where you began. Program must: use the toolkits unchanged, drive the square with a `for` loop (not four copied blocks), print progress, return to start.
2. **Sketch the loop body in English first.** What happens once per side? Two calls and a print. If a student's body is longer, ask what the extra lines are for.
3. **The program** (teacher copy; students write their own):
   ```python
   board = Board.get_default_board()

   board.wait_for_button()
   print("Module 3 Final Project - Square Pattern!")

   sides = 2  # intersections per side

   for leg in range(4):
       print("Side", leg + 1, "of 4")
       drive_intersections(sides)
       print("  Turning right...")
       turn_clockwise()

   print("Square complete! Back at start.")
   ```
4. **One side.** Comment out the loop; run one `drive_intersections(2)` + `turn_clockwise()`. Wheels on the corner? Sensor on the new side's line?

### Day 2: Two sides, four sides, demo
1. **Two sides** -- `range(2)`. Predict the shape before running.
2. **Four sides** -- does it close? Mark the start intersection with a sticker and measure the miss.
3. **Tune and record.** Which of the three settings fixed what.
4. **Demo** and reflect: hardest part, why the loop beats four copies, how this differs from Module 1's polygon (there you set distances and angles; here you count intersections and follow real lines).

### Extensions
- Larger square: `sides = 3`.
- Rectangle: `[2, 3, 2, 3]` indexed by `leg`.
- Mirror: `turn_counterclockwise()`.

### Assessment: rubric (50 points)
| Category | Points | What it takes |
|---|---|---|
| Toolkit reuse | 10 | Module 2 functions unchanged; `drive_intersections()` from Lesson 2 |
| Loop | 10 | One `for` loop, body is the drive and the turn |
| Four sides | 10 | All four legs drive and turn |
| Returns to start | 10 | Ends on the starting intersection (approximately is success) |
| Progress prints and testing log | 10 | Prints per side; the worksheet's testing log filled in |

## Common Issues
- **Square drifts open**: turns not quite 90 -- the blind part too long or `TURN_EFFORT` too high, so the sensor-ended finish spins past the line. Tune in Lesson 2-9's terms.
- **Robot overshoots a corner**: `BASE_EFFORT` too high; or a second `drive_past_intersection()` crept in before the turn.
- **`range(3)`**: three sides is not a square. Walk the loop.
- **Robot turns short of the corner**: a bare `track_to_intersection()` without its drive-past replaced the helper somewhere.

## Teaching Notes
- Insist on one side before two before four. Students who run four first can't tell which corner went wrong.
- Returning approximately to start is success; a perfectly closed square on real tape is a bonus. Two clean sides already show the concept.
- This is the last hard-coded path. Module 4 has the robot compute the drives and turns from coordinates.
