# Lesson 8 Worksheet: Driving the Path -- Answer Key

**1.** `track_to_intersection()`: both reflectance sensors see the cross. `turn_clockwise()`: the sensors find the next line. `drive_past_intersection()`: 8.75 cm have been driven.
**2.** None of them.
**3.** Sensors on the cross; wheels short of it (the sensors are mounted in front of the wheels).
**4.** It pivots about the wheels, in front of the intersection; the sensors swing down off the new line.
**5.** The sensors lead the wheels on every arrival, so the wheels are short of the cross every time. Parking them every time means every turn pivots on the cross and the next track starts past the tape -- no special case.

**Part 2.**
| Step | position | next | needed | %4 | does | after |
|---|---|---|---|---|---|---|
| 1 | (0,0) | (1,0) | 2 (S) | 2 | two clockwise, track, drive past | 2 |
| 2 | (1,0) | (1,1) | 1 (E) | 3 | one counterclockwise, track, drive past | 1 |
| 3 | (1,1) | (0,1) | 0 (N) | 3 | one counterclockwise, track, drive past | 0 |

**6.** `((0, 1), 0)`. **7.** Three and three.

**8.** `heading = turn_to(heading, needed)` and `position = next_pos`. `heading` inside `turn_to` is that function's own variable; the only way its result reaches `drive_path` is the return value.
**9.** `position` and `heading` in the main program are still `(0, 0)` and `0`, so the second path is planned from (0, 0) facing North while the robot is at (2, 2) facing some other way; it turns the wrong way and tracks to the wrong place (or off the grid). Fix: `position, heading = drive_path(path, position, heading)` on both lines.
**10.** 3, 4, 1, 5, 2 -- i.e. plan, print, button, drive, print arrival.
**11.** Driving. The planner is cleared by the correct printed path; open `turn_to` (or `desired_heading`) first.
**12.**
```
Path: [(1, 0), (1, 1)]
turn clockwise
turn clockwise
track to intersection
drive past intersection
turn counterclockwise
track to intersection
drive past intersection
```
(after the button prompt; exact wording follows the student's prints.)

**Exit ticket.** Needed 3 (W); `(3 - 1) % 4 = 2`; two clockwise turns (turn around), then track and drive past.

**E1.** "Paint the house at 48 Elm." `self` is 48 Elm -- the one house this call is about.
**E2.** The work order has no blank for the address. Python tried to fill the blank in with the navigator the method was called on and found nowhere to put it.
**E3.** It makes a new local variable and throws it away; `self.heading` never changes, so the next turn is computed from a stale heading. No house's heading was updated -- the work order named a value with no address attached.
**E4.** `position` and `heading` live at the navigator's address and `drive_path()` updates them there; the main program reads `navigator.position` whenever it wants. There is nothing to hand back.
