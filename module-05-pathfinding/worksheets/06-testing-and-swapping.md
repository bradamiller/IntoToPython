# Lesson 6 Worksheet: Testing and Swapping

**Name:** ________________________
**Date:** ________________________

---

## Part A: Why not just compare with the right answer?

**1.** Here are two paths from (0,0) to (3,3) on an open grid:

- `[(1,0), (2,0), (3,0), (3,1), (3,2), (3,3)]`
- `[(0,1), (0,2), (0,3), (1,3), (2,3), (3,3)]`

Are both correct? ______ How many steps does each have? ______

**2.** Module 4's test was `if actual_path == expected_path:`. If `expected_path` is the first one above and a planner returns the second, what does the test print? ______ Is the planner wrong? ______

**3.** Why was an exact-match test fine for Manhattan in Module 4 but not for BFS?

_______________________________________________________________

---

## Part B: The five properties

For a correct path from `position` to `destination`:

| # | Property | Write it as one `if` that adds a problem |
|---|---|---|
| 1 | The first step is next to the start | `if not is_neighbor(position, path[0]):` |
| 2 | The last step is the destination | |
| 3 | Every step is next to the one before it | |
| 4 | No step is a blocked intersection | |
| 5 | With nothing blocked, the number of steps is the Manhattan distance | |

**4.** Write `is_neighbor(a, b)` in one line, using `manhattan_distance()`:

```python
def is_neighbor(a, b):
    return ______________________________________
```

**5.** For each wrong path below, say which property catches it and what the FAIL line would say. All are "from (0,0) to (0,3), nothing blocked".

| Returned path | Property # | FAIL line says |
|---|---|---|
| `[(0,2), (0,3)]` | | |
| `[(0,1), (0,2)]` | | |
| `[(0,1), (0,3)]` | | |
| `[(0,1), (0,2), (0,3), (0,3)]` | | |

**6.** The destination is walled off and the planner correctly returns `[]`. Why can't `check_path()` tell this apart from a planner that returned `[]` because it is broken?

_______________________________________________________________

What does the harness do about it?

_______________________________________________________________

---

## Part C: Handing over the planner

```python
def run_test(test_name, planner, position, destination, expected_steps):
    path = planner(position, destination)
    ...

run_all_tests("BFS", compute_bfs_path)
```

**7.** In `run_all_tests("BFS", compute_bfs_path)`, what is being passed as the second argument -- the *result* of running the planner, or the *planner itself*? ______________ How can you tell from the code?

_______________________________________________________________

**8.** Inside `run_test`, `planner` is a parameter. When the harness was called with `compute_bfs_path`, what does the line `path = planner(position, destination)` do?

_______________________________________________________________

**9.** A classmate writes `run_all_tests("BFS", compute_bfs_path())`. What goes wrong?

_______________________________________________________________

**10.** Why does the harness never need an `if` that asks which planner it was given?

_______________________________________________________________

---

## Part D: Run it

Run the harness against both planners.

**11.** BFS: ______ of 6 passed. Manhattan: ______ of 6 passed.

**12.** Copy one of Manhattan's FAIL lines, including the "- " reason under it:

_______________________________________________________________

_______________________________________________________________

**13.** Is Manhattan failing because of a bug in `compute_manhattan_path()`? ______ Explain.

_______________________________________________________________

**14.** In the "Same main program, different planner" section, (2,0) is blocked. Write the first-leg path each planner produced:

Manhattan: ______________________________________________

BFS: ______________________________________________

What is the *only* thing that changed in the code between the two runs?

_______________________________________________________________

---

## Exit ticket

A planner returns `[(0,1), (0,3)]` for (0,0) to (0,3). Which property fails, and what does the FAIL line say?

_______________________________________________________________
