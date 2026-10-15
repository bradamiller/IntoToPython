# Lesson 7: The Challenge of Turning

## Overview
Students confront the problem that their robot has a **heading** -- a direction it is currently facing -- and that moving to the next grid intersection may require turning first. Two insights carry the lesson: (1) between adjacent intersections either the row OR the column changes, never both, which gives exactly four cases that map to the four compass directions; and (2) storing the heading as a number 0-3 turns "how many quarter turns?" into arithmetic: `(desired - heading) % 4`. Students design three functions on paper: `desired_heading(position, next_pos)` (which of the four cases is this step?), `turn_to(heading, desired)` (count quarter turns and take the short way round), and `drive_path(path, position, heading)` (for each intersection, turn and drive forward one). Code comes in Lesson 8.

The lesson also carries the course's one use of `raise`. `desired_heading()` checks *both* differences in every case, and if none of the four matches -- the positions are diagonal, identical or far apart -- it raises `ValueError` with both positions in the message. Without that, the function hands back `None`, `turn_to()` falls over doing arithmetic on it, and the error appears in a function that is correct. "When a function is asked something it cannot answer, say so immediately and loudly" is the debugging habit this lesson teaches.

## Learning Objectives
By the end of this lesson, students will be able to:
- Explain why only the row or the column changes between adjacent intersections, giving four cases
- Represent heading as a number: 0 = N, 1 = E, 2 = S, 3 = W, clockwise
- Write `desired_heading(position, next_pos)` with both differences checked in each case, ending in `raise`
- Explain why the `raise` makes a bug easier to find than a silent `None`
- Compute quarter turns with `(desired - heading) % 4`, including the negative cases, and explain why 3 clockwise becomes 1 counterclockwise
- Trace `drive_path` through a multi-step path, keeping `position` and `heading` up to date

## Key Concepts
- **One change at a time**: Adjacent intersections differ by exactly one in the row or the column, never both. Four cases, four directions.
- **Row 0 is at the top**: Moving down the grid increases the row. Down is South. This is the number-one confusion; draw it.
- **Heading as a number**: 0 = N, 1 = E, 2 = S, 3 = W. Each clockwise turn adds 1; `% 4` is the odometer wrap written as arithmetic.
- **`desired_heading(position, next_pos)`**: Each case checks both differences (`col_diff == 0 and row_diff == -1` is North). Anything else raises `ValueError(str(position) + " and " + str(next_pos) + " are not neighbors")`.
- **Say so when you can't answer**: A missing `raise` returns `None` silently; the failure shows up later in correct code with a message that names no positions. Raising reports the problem where it was found, with the values that caused it.
- **`(desired - heading) % 4`**: Quarter turns clockwise. Python's `%` takes the sign of the divisor, so `-1 % 4` is 3 and `-3 % 4` is 1 -- exactly what walking round the compass gives.
- **The short way round**: 3 clockwise is 1 counterclockwise. `turn_to()` has that single special case.
- **Told, not remembered**: `turn_to()` returns the new heading; `drive_path()` returns `position, heading`. The caller keeps its own record up to date by assigning from the returns -- the same rule as the planner.

## Materials Required
- XRP robot (for demonstration only in this lesson)
- Grid mat or taped grid from previous lessons
- `worksheets/07-the-challenge-of-turning.md`
- Whiteboard; a compass rose with 0-3 marked clockwise
- `code/starter/lesson-07-turning.py` (desktop only; no robot code yet)

## Lesson Flow

### Introduction (10 minutes)
1. **Hook: the robot that went sideways.** Place the robot on the grid facing East. "If I want the robot to go to the intersection directly below it, can I just drive forward?" Driving forward goes East. The robot needs to turn first. "The robot knows WHERE to go. Today is HOW to face the right way."
2. **One change at a time.** Draw two adjacent intersections. "What can change between them?" Either the row or the column, by one -- never both.
   ```
   row -1  -->  North     col +1  -->  East
   row +1  -->  South     col -1  -->  West
   ```
3. **Heading as a number.** Compass rose, 0 at the top, 1, 2, 3 clockwise. Rotate the robot and have students call out the number. "Why numbers? Because each clockwise turn adds 1 -- and when you'd reach 4, you wrap back to 0, like an odometer."

### Guided Practice (25 minutes)
1. **`desired_heading`.** Write it on the board with both differences in every condition:
   ```python
   def desired_heading(position, next_pos):
       row_diff = next_pos[0] - position[0]
       col_diff = next_pos[1] - position[1]
       if col_diff == 0 and row_diff == -1: return 0   # North
       if row_diff == 0 and col_diff ==  1: return 1   # East
       if col_diff == 0 and row_diff ==  1: return 2   # South
       if row_diff == 0 and col_diff == -1: return 3   # West
       raise ValueError(str(position) + " and " + str(next_pos) + " are not neighbors")
   ```
   "Why does row +1 mean South?" Row 0 is at the top; going down increases the row.

2. **The last line.** Ask what the function returns if none of the four matches and the `raise` is missing. (`None`, silently.) Then trace where `None` goes: into `turn_to(heading, None)`, which subtracts it from a number -- Python stops there, with an error about `NoneType` and `int`, pointing at a line in `turn_to`. "So you open `turn_to`. It is perfectly correct. The message says nothing about which positions caused it." With the `raise`: the program stops on the line that *noticed*, with both positions printed. Same bug, ten seconds instead of an afternoon. State the rule: **when a function is asked something it cannot answer, say so immediately and loudly.**

   Why both differences in each case: an earlier draft checked one (`if row_diff == -1: return 0`), which calls (2,1)->(3,3) "South" and never reaches the `raise`. A check with a hole in it buys confidence it hasn't earned.

3. **Counting turns.** "How many clockwise quarter turns from heading 2 (S) to heading 1 (E)?" Walk it physically: 2 -> 3 -> 0 -> 1, three turns. "And how many if we subtract: 1 - 2?" Minus one. Put the table on the board and fill it with the class:

   | heading | desired | `desired - heading` | `% 4` |
   |---|---|---|---|
   | 0 | 1 | 1 | 1 |
   | 2 | 1 | -1 | 3 |
   | 1 | 1 | 0 | 0 |
   | 3 | 0 | -3 | 1 |
   | 0 | 2 | 2 | 2 |

   `% 4` is the wrap. In Python `-1 % 4` is 3 (the result takes the sign of the 4); show it in the REPL, because students who know other languages expect -1.

4. **The short way round.** "Three clockwise turns gets you there. Is there a faster way?" One counterclockwise. So:
   ```python
   def turn_to(heading, desired):
       turns = (desired - heading) % 4
       if turns == 3:
           turn_counterclockwise()
       else:
           for i in range(turns):
               turn_clockwise()
       return desired
   ```
   Point at `return desired`: `heading` is the function's own variable, so the caller writes `heading = turn_to(heading, needed)` to keep its record straight. (`turn_clockwise()` and `turn_counterclockwise()` are the Module 2 functions; Lesson 8 wires them in. Today they are words on the board.)

5. **`drive_path`.**
   ```python
   def drive_path(path, position, heading):
       for next_pos in path:
           needed = desired_heading(position, next_pos)
           heading = turn_to(heading, needed)
           drive_forward_one()           # Lesson 8 replaces this with the real thing
           position = next_pos
       return position, heading
   ```
   Trace `[(1,0), (2,0), (2,1), (2,2)]` from (0,0) heading 0:
   ```
   At (0,0) N, next (1,0): want S(2). (2-0)%4 = 2: two clockwise.  Drive to (1,0).
   At (1,0) S, next (2,0): want S(2). (2-2)%4 = 0: no turn.        Drive to (2,0).
   At (2,0) S, next (2,1): want E(1). (1-2)%4 = 3: one ccw.        Drive to (2,1).
   At (2,1) E, next (2,2): want E(1). (1-1)%4 = 0: no turn.        Drive to (2,2).
   ```
   Students call out each line before you write it. Step 3 is the one to dwell on: facing South, needing East, a quarter turn to the left.

### Independent Practice (15 minutes)
Worksheet Parts 1-5: coordinate change to heading; the `% 4` table including negative rows; two path traces; the planted not-neighbors call. Fast finishers: Part 6 (what the error message says, and where the program stops).

### Assessment
- **Formative:** map a coordinate change to a heading; fill a `% 4` row with a negative difference; trace a path.
- **Exit ticket:** "Heading 3 (W), desired 1 (E) -- what is `(desired - heading) % 4`, and what does the robot do?" (`(1 - 3) % 4 = 2`; two clockwise turns, i.e. turn around.) "What does `desired_heading((1,1), (2,2))` do?" (Raises: not neighbors.)

## Common Misconceptions
| Misconception | Reality |
|---|---|
| "Row +1 means North because numbers go up" | The row index increasing means moving DOWN the grid. Down is South. |
| "`-1 % 4` is -1" | In Python the result takes the sign of the divisor: `-1 % 4` is 3. Check it in the REPL. |
| "Just always turn clockwise; it's simpler" | It works, but three sensor-ended turns take three times as long and give the sensors three chances to miss a line. One special case buys a lot. |
| "The `raise` is for errors in `desired_heading`" | It's for errors *elsewhere* -- whatever handed in two positions that aren't neighbors. The function is the first place that can notice. |
| "Checking one difference is enough" | (2,1)->(3,3) has `row_diff == 1`. A one-difference check calls that South. Both differences, every case. |
| "`turn_to` changes `heading`" | It changes its own copy. The caller must assign from the return value. |

## Differentiation
- **Support:** A printed compass the student can rotate. Do North/South only first. Let them count turns by stepping round the compass before trusting the subtraction.
- **Extension:** Prove `(desired - heading) % 4` is always 0-3. Eight headings (add NE, NW...): what changes in `desired_heading`, and what would `% 8` mean for the short-way rule? Write the trace printer in `code/solutions/lesson-07-turning.py` for an arbitrary path.

## Materials & Code Examples
`code/solutions/lesson-07-turning.py` runs on a laptop with no robot: `desired_heading()` with the `raise`, a table of `% 4` results, and a trace of a full path printing each turn. Expected output for the trace above:
```
  At (0, 0) heading N, need S: 2 turn(s) clockwise
  At (1, 0) heading S, need S: no turn
  At (2, 0) heading S, need E: 1 turn counterclockwise
  At (2, 1) heading E, need E: no turn
  Arrived at (2, 2) facing E
```

## Teaching Notes
- Paper-heavy on purpose. Students who have filled the `% 4` table by hand, negative rows included, have no trouble with Lesson 8. Students who skipped to code debug the wrap for a week.
- Get them standing and turning. 0, 1, 2, 3, 0 out loud. Then "from South to East, which way is shorter?" -- they feel the 270-vs-90 answer before the code says it.
- `raise` is new here, but nothing about it needs teaching beyond "the program stops and prints your message". Students never write `try`/`except` in this course. Don't turn it into a detour on exception handling; the point is where the program stops.
- If someone asks whether the error can really happen: with `compute_manhattan_path` feeding it, no. It becomes reachable the moment they call `desired_heading` by hand in a test, or wire it into their own Lesson 9 project. That is exactly when a good message is worth the most.

## Connections to Next Lessons
- **Lesson 8** replaces `drive_forward_one()` with Module 2's `track_to_intersection()` plus one wrinkle about where the wheels stop, and wires `turn_clockwise()` / `turn_counterclockwise()` into `turn_to()`.
- **Lesson 9** chains `drive_path()` across several destinations; the `position, heading =` assignment is the line that decides whether leg 2 works.
- **Module 5** reuses all three functions unchanged.
