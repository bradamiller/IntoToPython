# Course Design Decisions (2026-10-14)

The outcome of a design review of the whole course on 2026-10-13/14. It settles
how classes stay optional, what shape the pathfinding code takes, how students
test without a robot, and what Module 5 teaches. **Read this before changing
anything in Modules 2-5**, in this repo or on the site (`LearningPython`).

Each decision has a reason. Reverse one only with a better reason, and record
the history the way the older notes do, so nobody restores the previous shape by
accident.

Status of the work that follows from these decisions is in the table at the end.

---

## D1. Functions are the spine; classes are a per-student extension, gated on working code

Every module's required content is written with plain functions and
module-level variables, the skills from Module 1. Selected lessons end with an
**Optional Extension** that repackages the working functions as a class.

**What changed:** `classes-optional.md` used to say "pick one track for the
whole course before Module 2, don't mix per student." That rule is withdrawn.
The extension is now **per student, per lesson**, and the gate is not ability but
*working code*: finish the functions version, test it on the robot, and if there
is time left, do the extension. A student might reach it in 2-8, miss it in 2-9
because the P-controller fought them all period, and reach it again in 4-8.
Nobody is "the functions kid."

**Why this is safe now:** every function has the same name and (minus `self`)
the same signature as its class method. `track_to_intersection()` and
`tracker.track_to_intersection()` are the same function with a prefix. Assignments
are stated in that shared vocabulary, so one assignment serves both versions,
mixed teams can share the functions file, and a teacher debugging either student
is debugging the same loop.

**Classroom rules that make a mixed room work:**

- **Board code is always the functions version.** The class version is on the
  page, not live-coded. Translating `self.sensor.is_at_cross()` to
  `is_at_cross()` in your head is where a struggling student loses the thread.
- **The class "lecture" is 5-10 minutes, twice.** Once in 2-8 (what a class is,
  why you might want one), once in 4-8 (where owning state visibly pays off).
  Not re-taught every lesson.
- **The extension earns no points, or a small challenge credit.** If "code
  organization" on a rubric quietly rewards the class version, the extension
  becomes a requirement with extra steps and the students being protected are
  the ones penalized.
- **Every extension opens with a side-by-side:** functions on the left, class on
  the right, same names aligned row by row, then the four mechanical changes
  (functions move inside `class X:` and gain `self`; shared variables move into
  `__init__` as `self.x`; inside methods, shared values and sibling calls gain
  `self.`; outside calls go through the object). Any student can translate
  between the two by looking at it.

**What students get who never do an extension:** they have been calling
`drivetrain.straight()` and `reflectance.get_left()` since Lesson 1-8. Seeing
`LineSensor` once, even without writing it, turns those from magic into "that's
just `def`s inside a `class`." That is exposure without accountability, which is
the right outcome for a terminal course. The theory of OOP (inheritance,
polymorphism as a principle, encapsulation) belongs to a later course and is
**not taught here**, even in extensions.

## D2. Which class extensions exist

| Extension | Lesson | Why it earns its place |
|---|---|---|
| `LineSensor` | 2-8 | The simplest possible first class: two attributes, five one-line methods. Introduces `class`, `__init__`, `self`. |
| `LineTrack` | 2-9 | One object holding another (`self.sensor = LineSensor()`), shown by example. "Composition" is not taught as a vocabulary word. |
| `Navigator` | 4-8 | The one class with a *felt* reason: it owns `position` and `heading`, so the functions track's `position, heading = drive_path(path, position, heading)` threading disappears. |
| `Manhattan`, `BFS`, `Dijkstra` | 4-5, 5-5, 5-6 (ext.) | Exist so the swap demo works (D6): the same test harness and the same main program run against any planner by changing one name. `Manhattan` is a class *only* so it has the same shape as the others; `BFS`/`Dijkstra` are classes because they have setup to hold (the blocked list). Both reasons are stated plainly in the lesson. |

**Removed:** nothing is removed from the earlier extension list, but the
planner classes change shape (D3), which removes the `manhattan.position =
navigator.position` sync step from the 4-9 extension entirely.

## D3. The planner interface

Every pathfinder, function or class, has the same shape:

```python
# functions track
path = compute_manhattan_path(position, destination)
path = compute_bfs_path(position, destination)
path = compute_dijkstra_path(position, destination)      # extension
add_blocked(intersection)                                # shared

# class extension
planner = BFS()          # or Manhattan(), or Dijkstra()
path = planner.compute_path(position, destination)
planner.add_blocked(intersection)
```

Rules:

1. **`compute_path(position, destination)` takes the position as an argument.**
   Planners do not remember where the robot is. The Navigator is the single
   owner of position and heading (D4). *History:* the 2026-09-18 extension had
   `Manhattan(start)` with `self.position`, which forced the 4-9 sync step and
   was a bug paper tests could never catch, because position only drifts when
   the robot actually drives.
2. **The returned path excludes the start.** `[(0,1), (0,2)]`, not
   `[(0,0), (0,1), (0,2)]`. The Navigator is already at the start. *History:*
   M4's Manhattan excluded it and M5's included it; the 5-6 dispatch function
   hid the mismatch with `[1:]`. The site settled this the same way on
   2026-09-19 (Brad's call, so that `steps = len(path)` everywhere); this
   brings the source into line.
3. **`add_blocked(intersection)` is the primitive**, one intersection at a
   time, because that is what the robot does: see a wall, add it, re-plan,
   drive on. The paper test calls it several times. A `set_blocked(list)`
   convenience may loop over it. Blocked intersections live in a list
   (`BLOCKED` module-level in the functions track, `self.blocked` in a class);
   **the graph is built inside `compute_path` from that list on every call**,
   so the planner can never route through an intersection it was just told
   about. (On a 4x4 grid the rebuild is free. This also means the functions
   track needs no `global` for `add_blocked`: appending to a list is a
   mutation, not a reassignment.)
4. **`Manhattan` accepts `add_blocked` and ignores it**, with a one-line comment
   saying why it exists ("Manhattan cannot route around obstacles; this is here
   so every planner can be tested the same way"). Running the blocked-intersection
   test against Manhattan is how students see, on paper, why Module 5 exists:
   its printed path goes straight through the wall.
5. **Planners import nothing from XRPLib.** A planner file runs on any Python:
   a laptop, a browser REPL, at home with no robot and no grid. The moment one
   imports XRPLib the at-home testing story is gone.

## D4. The Navigator owns position and heading

In the functions track, `turn_to(heading, desired)` returns the new heading and
`drive_path(path, position, heading)` returns `(position, heading)`; the main
program catches them. In the extension, `Navigator` holds both as attributes.
Nothing else in the program tracks position. The planner is told the position
when asked for a path (D3.1).

## D5. Paper testing is structural, not a lesson

"Test without a robot" (M4 L6, M5 L6) already exists and is one of the course's
real strengths. These decisions make it complete rather than optional:

- **Every main program from 4-9 onward prints the path, then waits for the
  button, then drives it.** The student reads the list before the robot moves,
  every run. One `print`, and a paper test is built into every driving program.
- **The diagnostic students learn:** if the printed list is right and the robot
  still goes wrong, the bug is in the Navigator or the line tracker, not the
  algorithm. A planner with no hidden state (D3.1) is what makes that inference
  valid.
- **The rangefinder and the paper test call the same `add_blocked`.** In the
  test it comes from the script; on the robot it comes from the obstacle loop in
  5-7. Nothing downstream knows which. The test therefore exercises exactly the
  code the robot will run; only the source of the information is stubbed. The
  `simulate_rangefinder()` fake is needed only to test the *detection loop*,
  never the planner. Consequence: rerouting is debugged on paper in 5-6, and 5-7
  is only about detection. Two hard things, one at a time.
- **Property checks, not exact lists, once answers stop being unique.**
  Manhattan's answer is unique, so M4 L6's `actual == expected` is right. BFS
  and Dijkstra have many equally short paths on an open grid, so an exact match
  fails on correct answers. The harness checks what must be true instead:
  - starts next to `position` (first step is a neighbor of it)
  - ends at `destination`
  - every step is a neighbor of the previous one
  - no step is a blocked intersection
  - length equals the Manhattan distance when nothing is blocked
  - (extension) total cost is the lowest of any valid path
  Five one-line checks, stricter together than an exact match. The shift from
  exact-match to properties is taught as a lesson in its own right ("when more
  than one answer is right, test what must be true").

## D6. Module 5: BFS is required, Dijkstra is the extension

**Required path:** Manhattan (M4), then **breadth-first search**. Two planners,
same shape, swap demo between them. BFS reroutes around blocked intersections,
which is the capstone's payoff. The required middle of Module 5 shrinks from
three implementation lessons to one.

**Extension:** students **duplicate their BFS file, rename it `Dijkstra`, and
change two things**: take the unvisited node with the smallest distance instead
of the first in the queue, and add the edge's weight instead of `+1`. Graph
building, `add_blocked`, the `previous` dictionary and the walk-back are
untouched. They then have **three planners and one harness**, and the harness
shows BFS and Dijkstra agreeing on every test until the weighted edge, where
they split.

**Why:** the course's rule everywhere else is that students never write code
whose purpose they cannot see. The 2026-09 Module 5 had every student write the
`distances` table, the `999999` sentinel and the smallest-distance scan on a grid
where every edge is 1, so those lines did nothing observable. BFS has no such
lines; weighted Dijkstra gives them a visible reason.

**Naming:** the module keeps "Dijkstra" in its name (the word means something to
teachers, parents and transcripts; "BFS" does not). Suggested: "Module 5:
Pathfinding and Dijkstra's Algorithm", capstone unchanged.

**Weights (extension only):** the graph stays a neighbor-list dictionary; a
`weight(a, b)` function/method returns 1, or a larger number if the edge is in a
small `SLOW_EDGES` list. BFS never calls it.

**OPEN: the physical slow edge.** The extension is only honest if the weighted
edge is *physically real*, something students can time and give a number to.
Leading candidate: **one grid segment whose tape takes a winding detour** between
two adjacent intersections, so the map says one block but the drive takes about
three blocks' time. It needs nothing under the tape, does not disturb line
following, and students measure the weight with a stopwatch. Alternatives
considered: a rough surface under the tape (may disturb the reflectance sensor);
"turns cost time" (true, but makes cost depend on heading, which puts heading
into the graph state and is out of scope). **Brad to try on a real grid before
the extension lesson is written.**

**History:** Brad had considered BFS-first earlier and dropped it. Under the old
plan ("everyone ends at Dijkstra") BFS-first was pure overhead, an extra
algorithm on the way to the real one. Under this plan most students *end* at
BFS, so it is replaced time, not added time. The decision turns on how many
classrooms reach the extensions; if most do, Dijkstra-primary would be right
again.

## D7. `global` is taught in 2-8

The functions track's `set_threshold(new_value)` needs `global THRESHOLD`, and
2-8 teaches the keyword: required only when a function *reassigns* a module-level
name, never when it only reads one. Its awkwardness is then the honest motivation
for `self.threshold` in the extension (no keyword needed). *Note:* the site's
`CLAUDE.md` said "keep `global` out of the course"; that note is superseded. It
is still true that `global` is needed nowhere else, and D3.3 was shaped so
`add_blocked` does not need it either. (Default taken 2026-10-14; Brad can flip
it, in which case `set_threshold` goes and the extension is motivated by
demystifying XRPLib objects alone.)

## D8. Names are matched across tracks and the build checks it

Every class method in an extension has a function of the same name in the
primary content of the same lesson, with the same parameters minus `self`. The
site gets a build-time check (alongside `check_code_ascii.js`) that fails when
an extension defines `def name(self, ...)` with no matching `def name(...)` in
the lesson's primary code. Drift between the two copies is the real ongoing cost
of the extensions, and the check is cheaper than catching it in class.

## D9. Swap demo in both tracks

The one-name swap (D2, planners row) must exist in the functions track too, or
the idea lives only in the extension. There it is done by **passing the function
as an argument**: `run_tests(compute_manhattan_path)` then
`run_tests(compute_bfs_path)`, and `navigate(compute_bfs_path, ...)` in the
main program. Passing a function is the one new Python idea in 5-6 for the
functions track. *History:* the 2026-09 version used a
`compute_path(algorithm_name, ...)` dispatch function; it works but hides the
point, and it existed partly to paper over D3.2.

## D10. One driving vocabulary for Modules 2-5, and turns that end on a sensor

Settled 2026-10-14 against Brad's own RBE100X code (`Navigator.py`,
`linetrack.py`, `linesensors.py`), which is the reference for how the robot
should drive. Names, everywhere, in both tracks:

| Was | Is now | Note |
|---|---|---|
| `track_until_cross()` | `track_to_intersection()` | |
| `turn_right()` / `turn_left()` | `turn_clockwise()` / `turn_counterclockwise()` | unambiguous whichever way the robot faces |
| `clear_intersection()` | `drive_past_intersection()` | says what it does |
| `is_off_line()` | `is_either_on_line()` | the test a turn actually needs; `is_` kept on every boolean |
| `is_at_cross()`, `get_left()`, `get_right()`, `get_error()` | unchanged | |

**Turns end on a sensor, never on a timer.** `turn_clockwise()` makes a blind
`drivetrain.turn(-60, TURN_EFFORT)` to get both sensors off the line it was
following, then rotates in place (`arcade(0, -TURN_EFFORT)`) until
`is_either_on_line()` finds the cross street, then stops. Counterclockwise is
the same with the signs flipped. *History:* the course turned with
`set_effort(0.3, -0.3)` and `while is_off_line()`, and the site's Module 2
used `time.sleep(0.5)`; a timed turn depends on battery, floor and tape and
is never right twice.

**`drive_past_intersection()` runs after every `track_to_intersection()`,
not inside the turn.** The sensors stop *on* the cross, 8.75 cm ahead of the
axle. Driving that far puts the wheels over the intersection, so a turn
pivots on it and the next track does not see the same cross and return at
once. Doing it after the track (rather than before the turn) is what makes
rerouting safe: when Module 5 finds a wall and re-plans, the robot is
already parked on the intersection and nothing moves it again.

**`turn_to(heading, desired)` turns the short way round.**
`turns = (desired - heading) % 4`; 3 means one counterclockwise turn. Headings
stay the integers 0-3 (N, E, S, W) that Brad's `Pose` uses.

**Module 5 drives with Module 4's functions, verbatim.** L7-L9 carry the
Module 2/4 toolkit and add exactly one thing, a rangefinder read between
`turn_to()` and `track_to_intersection()`. The dead-reckoning layer
(`drivetrain.turn(90)`, `straight(20)`, string headings) is gone; see the
phase-2 history in the work-plan section for why it existed.

**`print_grid(rows, cols, blocked, numbers)`** draws the grid with `X` for
blocked intersections and a number on every other one -- ring numbers in the
BFS lessons, costs in the Dijkstra extension. Lifted from Brad's
`Dijkstra.print()`. It is the paper-test picture: students compare it with
the numbers they wrote by hand in 5-3.

---

## Work plan and status

Sequencing rule: **source first, then one port to the site.** The site already
trails the source by one reshape; porting Module 5 now and then redoing it would
convert it twice.

| Phase | What | Status |
|---|---|---|
| 1 | This document; `classes-optional.md` updated; pointer in the site's `CLAUDE.md` | done 2026-10-14 |
| 2 | **Source code** (`*/code/`). M4: stateless `Manhattan`, no sync step, print-then-drive mains. M5: `compute_bfs_path`, `add_blocked`, property harness, function-passing swap, `BFS`/`Dijkstra` class addons, weighted-edge addon. Then D10: one vocabulary and sensor-ended turns across M2-M5, M5 driving on M4's toolkit, `print_grid`. Paper tests run and passing on plain Python. | done 2026-10-14; robot files smoke-tested against a fake XRPLib only |
| 3 | **Source lessons and worksheets.** M2 L8 reframed per D1/D7; M4 L5-L9 and M5 L3-L9 rewritten around the phase-2 code; `pacing-guide.md`, `course-outline.md`, `README.md` updated; slides flagged stale, not regenerated. Brad's evaluation pass may run *as* this rewrite, lesson by lesson. | not started |
| 4 | **Site.** Optional Extension collapsible + side-by-side figure; name-parity build check (D8); port M2 L8-10, M4, M5 from the updated source in one pass. | not started |

While phase 2 is done and phase 3 is not, this repo's code and its lessons will
disagree in Modules 4-5. Commit messages say so.

**Phase 3 must-dos recorded from Brad (2026-10-14):**

- **The house analogy, part 2: an address is `self`.** The site's Lesson 2-8 now
  opens its class section with a blueprint-and-houses figure
  (`LearningPython/static/img/lesson-m2-08/class-and-objects.svg`: one plan,
  four houses, `House("red")` ... `House("green")`). At the **first constructor
  with parameters** -- today that is the `Navigator(start, heading)` extension
  in Lesson 4-8 -- bring the figure back with an *address* on each house and
  teach: the address uniquely identifies one house (two identical houses are
  still two houses); a method is a work order written once for every house,
  with a blank for the address (that is why `self` is the first parameter in
  `def`); and when you call `red_house.paint()` Python fills the blank in from
  the house you pointed at (that is why `self` is absent from the call), so the
  method works on *this* house's color, windows, `position`. Map the two
  classic errors onto it: no `self` in the `def` = a form with no address blank
  ("takes 0 positional arguments but 1 was given"); no `self.` prefix inside =
  a work order with no address attached (NameError on `color`). Say plainly
  that in Python the address *is* the house -- `self` is never a number or name
  students handle. `Navigator((0, 0), 0)` and `Navigator((3, 3), 2)` are two
  houses from one plan with different numbers on the door. Draw the second
  figure (addresses on the houses) when writing that lesson.

**RESOLVED 2026-10-14: Module 5's driving layer is now Module 4's (D10).**
*History:* the February Module 5 code had its own `Navigator` that drove by
dead reckoning (`drivetrain.turn(90)`, `drivetrain.straight(20)`, string
headings) and never used `LineTrack`; the August reshape unrolled it into
functions module by module, so the two different Navigators became two
different toolkits, and a comment called it "this module's simplified
turn+drive style" after the fact. Module 5's own Lesson 7 plan assumed
Module 4's `desired_heading()` all along.

**Not testable without a robot:** the Navigator, `LineTrack`, the rangefinder
loop and the print-then-drive main programs. (The M5 L7-L9 programs were run
here against a fake XRPLib that reports one obstacle, to check the reroute
loop; that is not a robot test.) Phase-2 changes to those are kept
minimal and marked; they need a run on an XRP before the lessons that use them
are rewritten.
