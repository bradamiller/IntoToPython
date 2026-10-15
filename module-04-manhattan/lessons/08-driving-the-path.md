# Lesson 8: Driving the Path

## Overview
Students turn the Lesson 7 paper design into three working functions -- `desired_heading()`, `turn_to()` and `drive_path()` -- that drive the XRP along any Manhattan path. The functions do no motor control themselves: they call the four line-tracking functions from Module 2 (`track_to_intersection()`, `turn_clockwise()`, `turn_counterclockwise()`, `drive_past_intersection()`), which is the payoff of having built a toolkit. Since a robot has one position and one heading, those two values are threaded through as parameters and handed back as return values; the caller keeps its own record straight with `position, heading = drive_path(path, position, heading)`. That assignment is the bug of the module.

The one thing the paper design did not have to care about is where the wheels stop. `track_to_intersection()` ends when the *sensors* see the cross, and the sensors sit in front of the wheels. So after every track the robot calls `drive_past_intersection()` -- 8.75 cm, the sensor-to-axle distance -- which parks the wheels over the intersection so turns pivot there, and carries the sensors past the tape so the next track starts clean. Doing it after every track, not only when going straight, removes a special case the old version of this lesson relied on.

The lesson introduces the habit the rest of the course keeps: plan, **print the path**, wait for the button, then drive. A correct printed path clears the planner; whatever went wrong is downstream.

This lesson stands on its own -- classes are never required. The **Optional Extension** at the end packages the three functions into a `Navigator` class. It is the course's first constructor with real parameters, which makes it the place to bring back Lesson 2-8's blueprint-and-houses figure with one addition -- every house has an address -- and to say what `self` actually is.

## Learning Objectives
By the end of this lesson, students will be able to:
- Name the four Module 2 functions the driving code is built on and what ends each one
- Explain why `drive_past_intersection()` follows every `track_to_intersection()`
- Implement `desired_heading()` (both differences, `raise`), `turn_to()` (`% 4`, short way round, returns the new heading) and `drive_path()` (returns `position, heading`)
- Keep `position` and `heading` up to date in the caller by assigning from the return values
- Plan, print the path, wait for the button, drive -- and use the printed path to decide which half of the program has the bug
- *(Extension)* Explain `self` as the address of the one object a method call is about

## Key Concepts
- **The Module 2 toolkit**: `track_to_intersection()` ends when both sensors see the cross; `turn_clockwise()` / `turn_counterclockwise()` end when the sensors find the next line; `drive_past_intersection()` ends after 8.75 cm. None of them know what a grid is.
- **Sensors lead the wheels**: at the end of a track the wheels are short of the cross. `drive_past_intersection()` puts them on it. Every arrival is the pair `track_to_intersection(); drive_past_intersection()`.
- **Two assignments inside `drive_path`**: `heading = turn_to(heading, needed)` and `position = next_pos`. And one outside: `position, heading = drive_path(...)`.
- **Plan, print, button, drive**: `print("Path:", path)` before `board.wait_for_button()`.
- **Desktop mode**: swap the four Module 2 calls for `print()` and run the whole program on a laptop first.
- *(Extension)* **`self` is the address**: the plan says what a method does; the address says which object. `elm.paint()` runs the plan with `self` = 48 Elm.

## Materials Required
- XRP robot, charged; the taped grid, at least 3x3
- `code/starter/lesson-08-driving-functions.py` (Module 2 functions and `compute_manhattan_path` included; the three functions as TODOs); `code/solutions/lesson-08-driving-functions.py`
- `worksheets/08-driving-the-path.md`
- Extension: `code/solutions/lesson-08-navigator-class-addon.py`; the house-address figure (`LearningPython/static/img/lesson-m4-08/house-address.svg`, also on the site page)

## Lesson Flow

### Introduction (10 minutes)
1. **The toolkit.** Put the four Module 2 functions on the board with what ends each one. Ask what is *not* in the list: rows, columns, headings, paths. "These functions know how to follow tape. They have no idea where the robot is. Today's three functions sit between the planner and the tape."
2. **Where the wheels stop.** Hold the robot up. Point at the sensors, then the wheels. "`track_to_intersection()` stops when the sensors see the cross. Where are the wheels?" Short of it. "Now turn." The robot pivots about its wheels, in front of the intersection, and the sensors swing down somewhere off the new line. So: after every track, `drive_past_intersection()`. Wheels on the cross -- the turn pivots there -- and sensors past the tape, so the next track doesn't stop on the cross it is sitting on.

### Guided Practice (20 minutes)
1. **`desired_heading()` and `turn_to()`** are Lesson 7's, typed in. The only change: `turn_to()` now calls `turn_clockwise()` and `turn_counterclockwise()` for real.
2. **`drive_path()`**, the paper version plus the wrinkle:
   ```python
   def drive_path(path, position, heading):
       for next_pos in path:
           needed = desired_heading(position, next_pos)
           heading = turn_to(heading, needed)
           track_to_intersection()
           drive_past_intersection()
           position = next_pos
       return position, heading
   ```
   Read the two assignments out loud. Then the one outside: "`position` and `heading` in here are this function's own variables. How does the main program find out where the robot ended up?" Only by `position, heading = drive_path(path, position, heading)`. Forget the left-hand side and the robot drives fine -- once.
3. **The main program.** Plan, print, button, drive:
   ```python
   board = Board.get_default_board()

   position = (0, 0)
   heading = 0
   destination = (2, 3)

   path = compute_manhattan_path(position, destination)
   print("Path:", path)

   board.wait_for_button()

   position, heading = drive_path(path, position, heading)
   print("Arrived at:", position, "facing", HEADING_NAMES[heading])
   ```
   "Read the path before you press the button. If it's right and the robot still goes wrong, which half of the program do you open?" The driving half. Two lines, and it tells you where to look.

### Independent Practice (25 minutes)
1. **Trace first.** `[(1, 0), (1, 1)]` from (0, 0) heading 0: step 1 is `(2 - 0) % 4 = 2`, two clockwise; step 2 is `(1 - 2) % 4 = 3`, one counterclockwise. Worksheet Part 2.
2. **Desktop mode.** Replace the four Module 2 calls with prints and run the program on the laptop. The sequence of turns and tracks should match the trace.
3. **One leg.** Module 2 functions back in; drive `[(1, 0)]` on the grid. Wheels on the intersection at the end?
4. **A real path.** `(0, 0)` to `(2, 3)`. Watch every arrival: wheels on the cross, turn pivoting on it.
5. **Break it on purpose.** Drop the `position, heading =` and plan a second path. Watch what happens. Put it back.

### Assessment
- **Formative:** name the four Module 2 functions and their end conditions; trace `drive_path` naming the two assignments; explain the drive-past.
- **Exit ticket:** "At (1, 2) heading 1 (E), next is (1, 1): what heading is needed, what is `(needed - heading) % 4`, what does the robot do?" (3 (W); `(3 - 1) % 4 = 2`; two clockwise turns.)
- **Worksheet:** `worksheets/08-driving-the-path.md`.

## Common Misconceptions
| Misconception | Reality |
|---|---|
| "`drive_path` updates my `position`" | It updates its own. The caller assigns from the return value or learns nothing. |
| "Only clear the intersection when going straight" | The sensors lead the wheels on every arrival. Park the wheels every time, and every turn pivots on the cross. |
| "`turn_to` turns the right amount by timing" | It turns until the sensors find the next line. Timing-based turns drift with battery and floor; sensor-ended ones don't. |
| "The start goes in the path" | No -- Lesson 5's promise 1. `desired_heading` would raise on a zero step, which is the `raise` doing its job. |
| "Print the path after driving" | Before the button. A printed path you can read before the robot moves is the diagnostic; afterwards it's a receipt. |

## Differentiation
- **Support:** Give all three functions complete; students do desktop mode, the trace and the one-leg test. Have them narrate the arrival pair with the robot in hand.
- **Extension:** Count intersections and turns in `drive_path` and print a summary. Or `print_grid()`-style ASCII of the path before the button.
- **Class track:** the Optional Extension below.

## Materials & Code Examples
`code/solutions/lesson-08-driving-functions.py` is the complete program with five tests at the bottom (paths, starting state, one drive, a second drive continuing from where the first ended, a multi-destination loop). Expected output of test 3:
```
=== Test 3: Drive (0,0) to (2,2) ===
Path: [(1, 0), (2, 0), (2, 1), (2, 2)]
Final position: (2, 2)
Final heading: E
```

## Teaching Notes
- Build and test one function at a time. Desktop mode catches most logic bugs before anyone touches a robot.
- The 8.75 cm is the XRP's sensor-to-axle distance. A robot with a different mounting needs a different number; measure it rather than tuning blind.
- Turns end on a sensor, so they tolerate battery level and floor friction. If a turn overshoots, the blind first part of Module 2's `turn_clockwise()` is the thing to shorten, not this lesson.
- Usual bugs in order: dropped return value; start in the path; `turn_to` without `return desired`.

## Connections to Next Lessons
- **Lesson 9** chains `drive_path()` across several destinations; only leg 1 can be printed before the button.
- **Module 5** uses all of this unchanged, adding one rangefinder read between `turn_to()` and `track_to_intersection()`.

---

## Optional Extension: The `Navigator` Class -- and what `self` really is

*Do this after the functions version works on the robot. It is not graded; it is for students who did the Module 2 class extensions.*

### Bring back the houses
Lesson 2-8's figure: the class is a blueprint, the objects are houses built from it. Show it again with one thing added -- **every house has an address** (the site's Lesson 4-8 has the figure: three houses, 12 Oak, 48 Elm, 7 Pine, built by `oak = House("red")`, `elm = House("yellow")`, `pine = House("blue")`).

- A method is a **work order written once for every house**, with a blank for the address. That is why `self` is the first parameter in the `def`: the blank.
- `elm.paint()` means "paint the house at 48 Elm". Python fills the blank in from the object you pointed at. That is why `self` is absent from the call.
- Inside `paint()`, `self.color` is "the color at this address" -- *this* house's color, not any other's. **`self` is the address of the one object this call is about.** In Python the address *is* the object; students never see a number.
- Two identical houses are still two houses: `Navigator((0, 0), 0)` and `Navigator((3, 3), 2)` are two objects from one plan with different numbers on the door.

Map the two classic errors onto it:
- No `self` in the `def` = a work order with no address blank. Python: `takes 0 positional arguments but 1 was given` (it tried to fill in the blank and found none).
- No `self.` prefix inside = a work order that names a color but no address. Python: `NameError: name 'color' is not defined`.

### The class
The first constructor in the course that is handed real data:
```python
class Navigator:
    def __init__(self, start, heading):
        self.position = start
        self.heading = heading
        self.line_track = LineTrack()        # the Module 2 extension class

    def desired_heading(self, next_pos):
        # ... Lesson 7's four checks and the raise, reading self.position ...

    def turn_to(self, desired):
        turns = (desired - self.heading) % 4
        if turns == 3:
            self.line_track.turn_counterclockwise()
        else:
            for i in range(turns):
                self.line_track.turn_clockwise()
        self.heading = desired

    def drive_path(self, path):
        for next_pos in path:
            needed = self.desired_heading(next_pos)
            self.turn_to(needed)
            self.line_track.track_to_intersection()
            self.line_track.drive_past_intersection()
            self.position = next_pos
```

| Functions (required) | Class (extension) |
|---|---|
| `position = (0, 0)`; `heading = 0` | `navigator = Navigator((0, 0), 0)` |
| `path = compute_manhattan_path(position, dest)` | `path = compute_manhattan_path(navigator.position, dest)` |
| `position, heading = drive_path(path, position, heading)` | `navigator.drive_path(path)` |
| `print(position)` | `print(navigator.position)` |

This is the one class in the course with a *felt* reason to exist. On the left, two values are threaded through every call and assigned back from every return -- forget once and the robot plans from the wrong place. On the right, the navigator owns them: they live at its address, `drive_path()` updates them there, and there is nothing to pass back and forth, so nothing to forget. (`turn_to` no longer returns anything, and `drive_path` doesn't either -- ask why.)

The planner is still a function (or the stateless `Manhattan` from Lesson 5). It is still told `navigator.position`; the navigator is the only thing that knows where the robot is.

### Code
`code/solutions/lesson-08-navigator-class-addon.py`: the Module 2 `LineSensor` and `LineTrack` classes, `Manhattan`, `Navigator`, and the same five tests.
