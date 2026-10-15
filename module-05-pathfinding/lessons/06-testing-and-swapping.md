# Lesson 6: Testing and Swapping

## Overview
Students test `compute_bfs_path()` properly, and in doing so meet a testing idea that will outlast this course: when more than one answer is right, test what must be *true* of a correct answer instead of comparing against one expected list. Module 4's harness compared Manhattan's output to an exact path, which was fine because Manhattan's answer is unique. On an open grid BFS has many equally short paths, and an exact-match test would fail correct code. So the Lesson 6 harness checks five properties -- the first step is next to the start, the last step is the destination, every step is next to the one before, no step is blocked, and on an open grid the length is the Manhattan distance -- plus a separate no-path test for the walled-off case.

The second idea is the swap. Because every planner has the same shape, `compute_xxx_path(position, destination)`, the harness can be *handed* the planner it should test: `run_all_tests("BFS", compute_bfs_path)`. Passing a function as an argument is the one new Python idea in the lesson. Students run the same harness against Manhattan and BFS and watch Manhattan fail the two blocked tests, on paper, with the path printed: it drives straight through the wall. That is the motivation for the whole module, demonstrated by the harness rather than asserted. The same swap then appears in a tiny main program: `navigate(compute_bfs_path, ...)` works with either planner by changing one name.

The Optional Extension runs the same harness against planner *objects* (`Manhattan()`, `BFS()`), where the swap is `planner.compute_path(...)` and the harness never knows which class it holds. Module 6 adds a third planner, Dijkstra, to both versions of this harness unchanged.

## Learning Objectives
By the end of this lesson, students will be able to:
- Explain why an exact-match test is wrong for BFS and right for Manhattan
- State the five properties every correct path has, and write each as one `if`
- Explain why the walled-off case needs its own test
- Pass a function as an argument (`run_all_tests("BFS", compute_bfs_path)`) and explain what `planner(position, destination)` does inside the harness
- Run the harness against Manhattan and BFS and explain each FAIL line
- Write a main program that works with either planner by changing one name
- *(Extension)* Run the same harness against planner objects

## Key Concepts
- **Property test**: A check of something that must be true of *any* correct answer, rather than a comparison with one expected answer. Five here: starts next to the start; ends at the destination; every step is a neighbor of the previous; no step is blocked; length equals the Manhattan distance when nothing is blocked.
- **`manhattan_distance(a, b)`** and **`is_neighbor(a, b)`**: `abs(dr) + abs(dc)`, and "that equals 1". The harness's two helpers.
- **No-path test**: When the destination is walled off, the only right answer is `[]`. `check_path` cannot tell "walled off" from "forgot to look" (both are an empty path with the robot not at the destination), so this case gets its own test.
- **Passing a function**: `run_all_tests("BFS", compute_bfs_path)` hands the harness the *function itself* (no parentheses). Inside, `planner(position, destination)` calls whichever planner was handed in. Same shape, so the harness never needs to know which.
- **The swap**: One main program, one harness, any planner, one name changed. Manhattan fails the blocked tests; BFS passes them. That is why Module 5 exists.
- **`clear_blocked()`**: Each test group starts clean. Without it, blocks from one test leak into the next.

## Materials Required
- Computers with Python (no robot needed)
- `code/starter/lesson-06-testing.py`
- Lesson 5's working `compute_bfs_path()`
- Module 4's `compute_manhattan_path()` (in the starter already)

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 8 min
**For 3-hour sessions:** 12 min

1. **Hook: two right answers, one test**
   - Two students read out their Lesson 5 Test 1 paths. If they differ (they often do), great; if not, show the second shortest route from Lesson 3. "Both are 6 steps. Both are right. Now here's a test from Module 4:"
     ```python
     if actual_path == expected_path:
         print("PASS")
     ```
     "Which of these two correct paths does it mark as FAIL?" One of them, necessarily.
   - "Module 4's test was fine, because Manhattan has exactly one answer. BFS doesn't. We need a different kind of test."

2. **Test what must be true**
   - "Forget the exact list. What has to be true of *any* correct path from (0,0) to (3,3)?" Collect on the board. Steer to the five:
     1. The first step is next to the start.
     2. The last step is the destination.
     3. Every step is next to the one before it.
     4. No step is a blocked intersection.
     5. With nothing blocked, the number of steps is the Manhattan distance.
   - "Five one-line checks. Together they are stricter than an exact match -- an exact match can't tell you a path is *valid*, only that it's the one you expected -- and they allow every correct answer."

### Guided Practice (17 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

1. **The helpers**
   ```python
   def manhattan_distance(a, b):
       return abs(a[0] - b[0]) + abs(a[1] - b[1])

   def is_neighbor(a, b):
       return manhattan_distance(a, b) == 1
   ```

2. **`check_path()` returns a list of problems**
   - Write it together, one property per `if`. An empty list means the path is good. Returning *problems* rather than True/False is deliberate: a FAIL line that says "drives through blocked intersection (1, 0)" tells you what to fix.
   - The empty-path case at the top: if `path == []` and the robot isn't at the destination, that is a problem -- *unless* the destination is walled off, which this function can't know. Hence the separate no-path test.

3. **`run_test()` and the planner argument**
   ```python
   def run_test(test_name, planner, position, destination, expected_steps):
       path = planner(position, destination)
       ...
   ```
   - Stop on `path = planner(position, destination)`. "`planner` is a parameter. What is in it?" A function. "How did it get there?" `run_all_tests("BFS", compute_bfs_path)` -- the function's name, no parentheses, handed in like a number or a list. "What does `planner(position, destination)` do?" Calls whichever function was handed in.
   - This is the one new Python idea today. Make it concrete: `f = compute_bfs_path` then `f((0,0), (3,3))` at the prompt.

4. **`run_all_tests()` and the swap**
   - Open grid (four cases, expected steps = Manhattan distance), the wall (expected 7), walled off (no-path test). `clear_blocked()` between groups.
   - Run `run_all_tests("Manhattan", compute_manhattan_path)` then `run_all_tests("BFS", compute_bfs_path)`. Read the Manhattan FAIL lines aloud: `drives through blocked intersection (1, 0)`. "That is the whole reason this module exists, and the harness just proved it."

### Independent Practice (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

Starter file: `code/starter/lesson-06-testing.py`. The planners and `run_all_tests` are given; the property checks, the expected-steps check and the swap calls are TODOs.

**Exercise 1: `is_neighbor()`.** One line.

**Exercise 2: the five properties.** Fill in `check_path()` (four properties) and the `expected_steps` check in `run_test()`. Run against BFS: 6 of 6.

**Exercise 3: the swap.** Run against Manhattan. Which tests fail, and what does each FAIL line say?

**Exercise 4: the main program.** Block (2,0). Run `navigate()` twice with Manhattan, then twice with BFS, changing only the planner's name. Compare the two first legs.

**Exercise 5: break a property.** Make `compute_bfs_path` return `path[1:]` (drop the first step). Which property catches it? Then make it return `path + [destination]`. Which one catches that?

**Exercise 6 (challenge): a sixth property.** Add "no intersection appears twice in the path" to `check_path()`. Can BFS ever fail it? Could a buggy planner?

### Assessment

**Formative (during lesson)**:
- Students can name the five properties without looking
- Students can explain the difference between `compute_bfs_path` and `compute_bfs_path()` in the `run_all_tests` call
- Ask: "Why does the walled-off case need its own test?"

**Summative (worksheet/exit ticket)**:
- Worksheet Parts A-D
- Exit ticket: "A planner returns `[(0,1), (0,3)]` for (0,0) to (0,3). Which property fails, and what would the FAIL line say?"

## Common Misconceptions
- **"Property tests are weaker than checking the exact answer."** They are stronger. An exact match passes any path equal to the expected one, including a wrong expectation; the properties check validity directly, and they allow every correct answer.
- **"`run_all_tests("BFS", compute_bfs_path())` -- with parentheses."** That *calls* the planner with no arguments and hands the harness the result (an error, here). No parentheses: hand over the function.
- **"An empty path always means failure."** It is correct for "already there" and for "walled off". The harness tests both, differently.
- **"Manhattan failing is a bug in Manhattan."** It is Manhattan behaving exactly as designed: rows then columns, no idea what a wall is. The harness shows the limitation, which is the point.
- **"The harness knows which planner it's testing."** It doesn't, and must not. It is handed a function and a name for the printout, nothing more.

## Differentiation
**For struggling students**: Give `check_path()` complete; have them do Exercises 3 and 4 and *read* the FAIL lines. Understanding what the harness says matters more than writing every check.

**For advanced students**: Exercises 5 and 6, then: "Write a planner that always returns `[]` and one that returns the Manhattan path with the last step removed. Which tests catch each?"

## Materials & Code Examples

### The harness output (solution file)

```
========== Manhattan ==========
  PASS  open (0, 0) to (3, 3)  [(1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3)]
  PASS  open (0, 0) to (0, 3)  [(0, 1), (0, 2), (0, 3)]
  PASS  open (2, 1) to (0, 3)  [(1, 1), (0, 1), (0, 2), (0, 3)]
  PASS  open (1, 1) to (1, 1)  []
  FAIL  wall at (1,0),(1,1): (0,0) to (3,0)  [(1, 0), (2, 0), (3, 0)]
          - drives through blocked intersection (1, 0)
          - expected 7 steps, got 3
  FAIL  walled off: (0,0) to (3,0)  [(1, 0), (2, 0), (3, 0)]
          - there is no way through, so the path should be empty
Manhattan: 4 of 6 passed

========== BFS ==========
  PASS  open (0, 0) to (3, 3)  [(1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3)]
  PASS  open (0, 0) to (0, 3)  [(0, 1), (0, 2), (0, 3)]
  PASS  open (2, 1) to (0, 3)  [(1, 1), (0, 1), (0, 2), (0, 3)]
  PASS  open (1, 1) to (1, 1)  []
  PASS  wall at (1,0),(1,1): (0,0) to (3,0)  [(0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (3, 1), (3, 0)]
  PASS  walled off: (0,0) to (3,0)  [] (no path, correctly)
BFS: 6 of 6 passed
```

### The swap in a main program

```python
def navigate(planner, position, destination):
    path = planner(position, destination)
    print("  Path from", position, "to", destination, ":", path, " Steps:", len(path))
    return destination       # where the robot would be after driving it

add_blocked((2, 0))
position = navigate(compute_manhattan_path, (0, 0), (3, 3))   # through the wall
position = navigate(compute_bfs_path, (0, 0), (3, 3))         # around it
```

### Answer key, Exercise 5

Dropping the first step: "first step (2, 0) is not next to the start (0, 0)". Appending the destination again: "step (3, 3) is not next to (3, 3)" (an intersection is not its own neighbor) and the step count is one too many.

## Teaching Notes
- Returning a *list of problems* from `check_path()` is worth a minute: a test that says only FAIL is a test students will ignore. Every FAIL line here says what is wrong.
- Function-as-argument is new. Do the `f = compute_bfs_path` demo at the prompt before anyone writes the harness. The common slip is adding parentheses in the `run_all_tests` call.
- Let students discover the Manhattan FAIL lines themselves rather than announcing them. "Run it against Manhattan and read what it says" lands harder than any explanation.
- The property-vs-exact lesson generalizes far beyond this course. Say so.

## Connections to Next Lessons
- **Lesson 7** puts the planner on the robot. The rangefinder loop calls `add_blocked()` exactly as this harness does; the planner cannot tell the difference, which is why passing the paper tests means the robot will re-plan correctly.
- **Lesson 8** starts Run 2 from the obstacles Run 1 found, typed into `KNOWN_OBSTACLES` and fed to `add_blocked()`; the harness is how to check that list without driving.
- **Module 6 (optional)** adds `compute_dijkstra_path` as a third argument to `run_all_tests`, unchanged, plus one more property: total cost.

---

## Optional Extension: The Harness with Planner Objects

*Do this after the functions harness passes. It is not graded.*

With the `BFS` and `Manhattan` classes from Lesson 5, the harness is handed an *object* instead of a function, and calls its methods:

| Functions (required) | Class (extension) |
|---|---|
| `run_all_tests("BFS", compute_bfs_path)` | `run_all_tests("BFS", BFS())` |
| `path = planner(position, destination)` | `path = planner.compute_path(position, destination)` |
| `add_blocked((1, 0))` | `planner.add_blocked((1, 0))` |
| `clear_blocked()` | `planner.clear_blocked()` |

Everything else in the harness is identical. Because both classes have `add_blocked()`, `clear_blocked()` and `compute_path()`, the harness never needs to know which one it holds. `Manhattan.add_blocked()` does nothing, so `Manhattan()` fails the same two tests for the same reason -- which is the correct result.

One wrinkle: `check_path()` needs to know what is blocked to test property 4, and with objects the blocked list lives inside the planner. `code/solutions/lesson-06-testing-class-addon.py` keeps the harness's own small record (`block(planner, x)` calls `planner.add_blocked(x)` and notes it) so the check stays honest. Ask students why the harness shouldn't just read `planner.blocked` directly. (Manhattan has no such attribute, and the harness isn't supposed to know what is inside a planner.)
