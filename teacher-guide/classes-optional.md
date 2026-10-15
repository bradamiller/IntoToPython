# Classes Are Optional

> Updated 2026-10-14. The reasoning behind the current shape, the planner interface, paper testing and the Module 5 change are in **`course-design-decisions.md`**; this file is the lesson-by-lesson map.

This course can be taught two ways:

- **Functions-only (default)**: Students never see `class` or `self`. Every module's core content -- sensors, control loops, grid navigation, pathfinding, obstacle detection -- is built using plain functions and global variables, the same skills introduced in Module 1.
- **With classes**: Selected lessons include an **Optional Extension** section at the end that repackages the same working code as a class, for courses that also want to cover OOP.

Both produce robots that behave identically and reach the same capstones.

**The extension is per student, per lesson -- not a course-wide track (changed 2026-10-14).** The gate is working code, not ability: finish the functions version, test it on the robot, and if there is time left, do the extension. Because every function has the same name and (minus `self`) the same signature as its class method, one assignment serves both versions, mixed teams can share the functions file, and the teacher debugging either student is debugging the same loop. The classroom rules that make a mixed room work (board code is always the functions version; the class lecture is 5-10 minutes, twice; the extension earns no points; every extension opens with a side-by-side) are in `course-design-decisions.md`, D1.

*History:* this file used to say "pick one for the whole course before Module 2 begins -- don't mix per-student, since later modules assume every student's toolkit already exists and behaves the same way." That concern was real when function and method names differed; with matched names the difference between the two students' code is a `tracker.` prefix, and the rule was withdrawn.

## Why it's built this way

Classes stop being optional the moment they become *architecture* rather than *a topic*. In the original design, this course built each module's code as reusable objects, and every later module drove the robot through method calls on instances of those objects -- there was no way to "skip the classes lesson" and continue into Module 3 unmodified.

The current shape fixes that by making functions the primary spine everywhere, with classes presented only as a **refactor of code students already have working** -- never as the primary way a topic is introduced. This also matches how the Module 4-5 algorithms actually want to be taught: `compute_manhattan_path` and `compute_dijkstra_path` are naturally pure functions (state in, state out), so there was never a good reason to make classes co-equal with functions for that content.

An earlier draft tried two full, symmetric lesson tracks (a dedicated Classes-first path alongside a Functions-only path) built as separate parallel files per lesson. Building the first pair (Module 2, Lessons 8-9) that way surfaced a real problem: the two files were about 70% identical prose, with the actual differences confined to a handful of code-construction steps. The single-lesson-plus-addon shape used now avoids that duplication.

## Where classes show up as an Optional Extension

Only where a class would actually wrap something students already built -- never as the primary way a topic is introduced.

| Lesson | Primary content (required) | Optional Extension |
|---|---|---|
| M2 L8 -- sensor functions | `module-02-line-tracking/lessons/08-sensor-functions.md` | Refactor into a `LineSensor` class |
| M2 L9 -- line-tracking functions | `module-02-line-tracking/lessons/09-line-tracking-functions.md` | Refactor into a `LineTrack` class (object composition) |
| M2 L10 -- final project | `module-02-line-tracking/lessons/10-module-2-final-project.md` | Combine the two Optional Extension classes |
| M3 L1-4 -- grid driving | `module-03-grid-driving/lessons/*.md` | None needed -- these lessons only *call* the Lesson 9 toolkit, never build a class. A one-line callout notes the `tracker.method()` syntax for classes-track teachers. |
| M4 L0 -- module overview | `module-04-manhattan/lessons/00-module-overview.md` | Mentioned in passing; the roadmap itself stays functions-first |
| M4 L5 -- Manhattan function | `module-04-manhattan/lessons/05-implementing-the-manhattan-class.md` | Refactor `compute_manhattan_path` into a `Manhattan` class. **Stateless since 2026-10-14:** `compute_path(position, destination)` takes the position; the class holds nothing. It is a class only so it has the same shape as `BFS`/`Dijkstra`, and the lesson says so. |
| M4 L8 -- driving the path | `module-04-manhattan/lessons/08-driving-the-path.md` | Package `desired_heading`/`turn_to`/`drive_path` as a `Navigator` class that composes `LineTrack`. The Navigator is the single owner of position and heading. First constructor with real parameters: the house-address picture of `self` lives here. |
| M4 L9 -- final project | `module-04-manhattan/lessons/09-final-project.md` | Full class-based main program (`Manhattan` + `Navigator`). *The `manhattan.position = navigator.position` sync step is gone* -- the planner no longer tracks position. |
| M5 L4-5 -- BFS functions | `module-05-pathfinding/lessons/04-*.md`, `05-*.md` | Refactor `compute_bfs_path`/`add_blocked` into a `BFS` class |
| M5 L6 -- testing and swapping | `module-05-pathfinding/lessons/06-testing-and-swapping.md` | Matching `compute_path(position, destination)` methods on `Manhattan`/`BFS`: two planners, one harness, swap by changing one name. The functions track gets the same demo by passing the function as an argument (`run_all_tests("BFS", compute_bfs_path)`), not via a dispatch function. |
| **M6 (optional module)** L3, L5 -- Dijkstra | `module-06-dijkstra/` | Dijkstra is a separate optional *module* (2026-10-14), not an extension: a copy of BFS with two changes. Its own optional extension (L5) is the `Dijkstra` class, three planners through the Module 5 class harness. |
| M5 L7-9 -- obstacle detection, experience, capstone | `module-05-pathfinding/lessons/07-09*.md` | No dedicated extension section -- these lessons call the Lesson 4-5 functions directly; a one-line callout per lesson notes the class-call equivalent for classes-track teachers |

Everything else (Module 1 entirely, M2 Lessons 1-7, M4 Lessons 1-4 and 6-7, M5 Lessons 1-3) needs no extension -- it never touches class syntax either way.

**Not yet updated:** the pre-existing PowerPoint slide decks and slide outlines for M2 L8-9 (`module-02-line-tracking/slides/08-introduction-to-classes-outline.md`, `09-object-composition-outline.md`, and the `.pptx` generator scripts at the repo root), and the `.html`/`.pdf` renders of worksheets and answer keys across Modules 4-5. These still reflect the pre-reshape framing or need regenerating from the updated `.md` source through the existing pandoc/Chrome pipeline. Content (lessons, worksheets, exercises, answer keys, starter/solution code) is fully reshaped; production artifacts derived from that content are not.

## How to use it

- **Teaching without classes:** Use only the primary lesson content. Stop before any "Optional Extension" heading.
- **Teaching with classes:** Teach the primary content first (functions), then continue into the Optional Extension in the same lesson period, or push it to the next class session -- it's short by design, since the underlying logic doesn't change, only its packaging.
- **Choosing a track:** Functions-only if you want the same robotics and algorithm content in less time, or if this is a terminal course. With classes if your course has room for `self`/`__init__` as a real topic, or students are headed into a follow-on CS course where OOP will matter.
