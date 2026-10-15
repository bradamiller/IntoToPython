# Lesson 5 (Optional Extension): Three Planners, One Harness

## Overview
For students who built the `Manhattan` and `BFS` classes (Lessons 4-5 and 5-5). They add the third, `Dijkstra` -- a copy of `BFS` with `self.slow_edges`, `add_slow_edge()`, `weight()`, and Lesson 3's two changes inside `compute_path()` -- give `Manhattan` and `BFS` an `add_slow_edge()` that does nothing, add the cost property to the Module 5 class harness, and run all three objects through it. The harness never finds out which class it holds. That property is named here, once, after students have used it three times: **polymorphism** -- code written against a shape (the method names a planner answers to) rather than against one class.

## Learning Objectives
By the end of this lesson, students will be able to:
- Write the `Dijkstra` class by copying `BFS` and making the two changes
- Keep the slow list inside the object and expose it through `add_slow_edge()`
- Explain why `Manhattan` and `BFS` need an `add_slow_edge()` that does nothing
- Run three planner objects through one harness and read the results
- Say what polymorphism means, pointing at the harness

## Key Concepts
- **Same shape**: `compute_path(position, destination)`, `add_blocked()`, `clear_blocked()`, `add_slow_edge()`. Told the position every call; path excludes the start.
- **`self.slow_edges`**: the planner's own knowledge of the grid, like `self.blocked`; no global.
- **The harness keeps its own record**: `slow(planner, a, b, cost)` records the edge and calls `planner.add_slow_edge()`, so the cost check uses true weights whichever planner is under test (as `block()` did for walls in Lesson 5-6).
- **An empty `add_slow_edge()`**: a planner that cannot use a piece of information still accepts it, or the harness would need an `if` per class.
- **Polymorphism**: one harness, three classes, no `if`.

## Materials Required
- Computers with Python (no robot)
- Students' Lesson 5-6 class harness and `BFS` class
- `code/solutions/lesson-05-three-planners-class-addon.py`
- `worksheets/05-three-planners-one-harness.md`

## Lesson Flow

### Introduction (5 minutes)
"You have a harness that is handed an object and calls `planner.compute_path(...)`. How many classes does it know about?" None. "So what does it take to test a third planner?" Write the class; hand it in.

### Guided Practice (20 minutes)
1. **Copy `BFS` to `Dijkstra`.** Add `self.slow_edges = []`, `add_slow_edge()`, `weight()`; make the two changes inside `compute_path()` (`closest()` as a method or a plain function). Everything else is Lesson 3 with `self.` in front.
2. **The empty method.** Add `add_slow_edge(self, a, b, cost): pass` to `Manhattan` and `BFS`. Ask why it has to exist; let students find the `if planner is BFS` they would otherwise need in the harness.
3. **The cost property in the harness.** `slow()`, `true_cost()`, `run_cost_test()`; one fresh object per planner so slow edges don't leak.

### Independent Practice (20 minutes)
Run all three:
```
Manhattan: 4 of 7 passed   (blocked tests FAIL, cost FAIL)
BFS:       6 of 7 passed   (cost FAIL)
Dijkstra:  7 of 7 passed
```
Each planner fails exactly the tests that describe what it cannot do. Worksheet: the who-fails-what table and the polymorphism questions.

### Assessment
- **Formative:** the three-planner output; the explanation of the empty `add_slow_edge()`.
- **Exit ticket:** "What would the harness need if `BFS` lacked `add_slow_edge()`?" (An `if` per class -- the thing polymorphism removes.)

## Common Misconceptions
| Misconception | Reality |
|---|---|
| "The harness should check which class it has" | Then every new planner changes the harness. The shape is the contract; the harness never looks inside. |
| "BFS should raise an error on `add_slow_edge()`" | Accepting and ignoring is the point: BFS cannot use the information, and the caller should not have to know that. |
| "Use the planner's own `weight()` in the cost check" | BFS's would return 1 everywhere and pass. The harness keeps its own record of slow edges, as it did for walls. |

## Teaching Notes
- Name polymorphism once, point at the harness, move on. A terminology lecture would undo the lightness that made the class track work.
- Students who did Lesson 3 carefully finish in half an hour.

## Connections
- This is the last lesson in the course. Three planners, one name to swap them, and a robot that plans by time.
