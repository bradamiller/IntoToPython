# Module 6: Dijkstra's Algorithm (Optional)

## Overview

**Duration:** 1–2 weeks
**Status:** optional. The course is complete at the end of Module 5; this module is
for classes that have time, or for a second semester. Nothing later depends on it.
**Prerequisite:** Module 5 (BFS, `add_blocked`, the paper-test harness).
**Theme:** the same algorithm with one upgrade — when the fewest steps is not the
fastest route.

**Final activity:** on a grid with one deliberately slow segment, the robot takes
the route that is longer in steps but shorter in time, next to a BFS run on the
same grid that does not.

## Why this is a separate module

Module 5's BFS finds the path with the fewest steps, and on a grid where every
block takes the same time that is the fastest path. Dijkstra's algorithm is BFS
with two changes that let it handle a grid where some segments are slower than
others. Everything students built in Module 5 — the graph, `add_blocked()`, the
`previous` dictionary, the walk-back, the harness — is reused as is.

It is its own module rather than an extension because it needs the **physical
grid to change** (a slow segment that the whole class shares), which is a class
decision, not a per-student one; and because a module is the unit teachers plan
by, so it can be dropped cleanly.

## Learning Objectives

By the end of this module, students will be able to:
- Explain why the shortest path in steps is not always the fastest, and measure it
- Represent a slow segment as an edge weight
- Add a cost check to the Module 5 harness and show that BFS fails it
- Turn their BFS into Dijkstra's algorithm by making two changes to a copy
- Read a cost grid (`print_grid`) and explain each number
- Run three planners through one harness and say where they agree and disagree

## Lessons

| # | Lesson | Core idea | Code |
|---|---|---|---|
| 1 | When Fewest Steps Isn't Fastest | Time a normal block and the slow segment with a stopwatch; a weight is "how many normal blocks' worth of time". Hand-compute the cost of two routes. | paper |
| 2 | Weights in the Graph | `SLOW_EDGES`, `add_slow_edge(a, b, cost)`, `weight(a, b)`; `path_cost()` as a new harness property; BFS fails it. The limitation, on paper. | `code/solutions/lesson-02-weights.py` |
| 3 | From BFS to Dijkstra | Duplicate `compute_bfs_path`, rename, two changes (closest-first instead of oldest-first; `+ weight` and keep the cheaper total). `print_grid` of costs. Three planners, one harness. | `code/solutions/lesson-03-from-bfs-to-dijkstra.py` |
| 4 | Drive It | The robot on the slow-segment grid: BFS run, then Dijkstra run, both plans printed before the button, both timed. | `code/solutions/lesson-04-drive-it.py` |
| 5 | *Optional extension:* the `Dijkstra` class | Three planner classes through the Module 5 class harness. | `code/solutions/lesson-05-three-planners-class-addon.py` |

## Physical setup (open — Brad to try on a real grid)

The module is only honest if the slow segment is *physically real*: something
students can time and give a number to. Leading candidate: **one grid segment
whose tape takes a winding detour** between two adjacent intersections, so the
map says one block but the drive takes four or five blocks' time (exactly three ties with the detour round it). It needs nothing
under the tape, does not disturb line following, and students measure the weight
with a stopwatch. Alternatives considered and set aside: a rough surface under the
tape (may disturb the reflectance sensors); "turns cost time" (true, but it makes
cost depend on heading, which is out of scope).

## Status

- **Code:** Lessons 2, 3, 4 and 5 exist and run (2, 3, 5 on plain Python; 4 against
  the fake XRPLib). Starters for 2-4 in `code/starter/`.
- **Lessons and worksheets:** written 2026-10-14 for all five lessons; the site
  pages (`module-06-dijkstra/lesson-0x-*.mdx`) carry the same content.
- **Slides:** not written. `_source-material/` holds the old Dijkstra-first Module 5
  lessons, worksheets and slides; seed material only.
- **Physical setup:** still open (above). The lessons assume the winding-detour
  segment and a measured weight of 4 or more; a weight of exactly 3 ties with the
  three-block detour round one segment, which Lesson 1 teaches on purpose.
- See `teacher-guide/course-design-decisions.md`, D6, for the reasoning.
