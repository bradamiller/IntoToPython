# Lesson 7 Worksheet: The Challenge of Turning -- Answer Key

## Part 1
| Position | Next | row_diff | col_diff | What changed | Desired |
|---|---|---|---|---|---|
| (0,0) | (1,0) | 1 | 0 | row +1 | 2 (S) |
| (2,3) | (1,3) | -1 | 0 | row -1 | 0 (N) |
| (1,1) | (1,2) | 0 | 1 | col +1 | 1 (E) |
| (3,2) | (3,1) | 0 | -1 | col -1 | 3 (W) |
| (3,1) | (2,1) | -1 | 0 | row -1 | 0 (N) |
| (0,2) | (0,1) | 0 | -1 | col -1 | 3 (W) |
| (1,1) | (2,2) | 1 | 1 | both -- not neighbors | raises |

- `desired_heading((1,1), (2,2))` raises `ValueError: (1, 1) and (2, 2) are not neighbors` and the program stops on that line.
- The one-difference version returns 2 (South) for a diagonal step: a confident wrong answer that travels on into `turn_to` and the drive. An error stops the program where the problem is; a wrong heading sends the robot off the grid with nothing printed.

## Part 2
| heading | desired | diff | %4 | does |
|---|---|---|---|---|
| 0 | 1 | 1 | 1 | one clockwise |
| 1 | 1 | 0 | 0 | nothing |
| 2 | 0 | -2 | 2 | two clockwise (turn around) |
| 3 | 2 | -1 | 3 | one counterclockwise |
| 1 | 0 | -1 | 3 | one counterclockwise |
| 0 | 3 | 3 | 3 | one counterclockwise |
| 2 | 3 | 1 | 1 | one clockwise |
| 3 | 1 | -2 | 2 | two clockwise (turn around) |

- Rows 4, 5 and 6 give 3: the robot makes one counterclockwise turn.
- One sensor-ended turn takes a third of the time of three, and gives the sensors one chance to miss a line instead of three.

## Part 3
- `heading` inside the function is the function's own variable; the caller writes `heading = turn_to(heading, needed)` to keep its record up to date.
- `turn_to(2, 1)`: `turns = (1 - 2) % 4 = 3`; the `if turns == 3` branch runs once: one counterclockwise turn. Returns 1.

## Part 4
| Step | Desired | Before | %4 | Does | After |
|---|---|---|---|---|---|
| 1 | 2 (S) | 0 | 2 | two clockwise | 2 |
| 2 | 2 (S) | 2 | 0 | nothing | 2 |
| 3 | 1 (E) | 2 | 3 | one counterclockwise | 1 |
| 4 | 1 (E) | 1 | 0 | nothing | 1 |
| 5 | 1 (E) | 1 | 0 | nothing | 1 |

Two steps needed a turn; step 3 was counterclockwise.

## Part 5
| Step | Desired | Before | %4 | Does | After |
|---|---|---|---|---|---|
| 1 | 0 (N) | 2 | 2 | two clockwise | 0 |
| 2 | 0 (N) | 0 | 0 | nothing | 0 |
| 3 | 3 (W) | 0 | 3 | one counterclockwise | 3 |
| 4 | 3 (W) | 3 | 0 | nothing | 3 |
| 5 | 3 (W) | 3 | 0 | nothing | 3 |

Final position (0, 0), heading 3 (W).

## Part 6
- `None`.
- `turns = (desired - heading) % 4` fails: `TypeError: unsupported operand type(s) for -: 'NoneType' and 'int'`. The message names the types, not the positions, and points at `turn_to`, which is correct.
- The `raise` line in `desired_heading` stops the program, and its message names both positions: `(1, 1) and (2, 2) are not neighbors`.

## Reflection
Headings go clockwise 0-3, so the number of clockwise quarter turns is the difference, and `% 4` wraps negative or large differences into 0-3. The one special case: 3 clockwise is the long way round, so the robot makes 1 counterclockwise turn instead.
