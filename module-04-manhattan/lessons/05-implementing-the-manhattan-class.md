# Lesson 5: A Reusable Manhattan Function

## Overview
Students take the `compute_path` function they wrote in Lesson 4 and turn it into a properly named, documented, reusable function: `compute_manhattan_path(position, destination)`. The algorithm itself -- four while loops that build a path list -- does not change at all; this lesson is about giving it a name specific enough to survive contact with Module 5, where a second pathfinding algorithm (breadth-first search, `compute_bfs_path`) will need its own, differently-named function. The lesson also fixes the rule the rest of the course rests on: the planner is *told* where the robot is, every call, and never remembers -- only the driving code (Lesson 8) tracks position, so there is never a second copy to fall out of date. Students test the renamed function against several start/destination pairs and confirm the output still matches their Lesson 4 hand traces.

This lesson stands on its own -- classes are never required. An **optional extension** at the end of this file shows the same function wrapped in a `Manhattan` class, for courses that also cover OOP.

## Learning Objectives
By the end of this lesson, students will be able to:
- Explain why a specific function name matters once a codebase has more than one algorithm
- Add a docstring to a function explaining its parameters and return value
- Rename a function and its parameters without changing its behavior
- Test a function against multiple start/destination pairs, including edge cases
- Confirm function output matches hand-traced results from Lesson 4

## Key Concepts
- **Naming for the future**: `compute_path` is a fine name when there's only one algorithm. Once Module 5 introduces BFS, code that calls "the Manhattan one" needs a name that says so -- `compute_manhattan_path`.
- **Docstring**: A string literal right after `def` that documents what a function does, its parameters, and its return value. Shows up in editor tooltips and `help()`.
- **Parameter naming**: `compute_manhattan_path(position, destination)` -- naming the first parameter `position` (not `start`) matches how it will be used later: the robot's *current* position, not just a one-time starting point.
- **Told, not remembered**: `position` is a parameter because the driving code owns the robot's position. A planner that stored its own copy would need a line to keep the two in sync, and the first time that line is forgotten the robot plans from a place it isn't.
- **Regression testing**: Confirming that renaming/refactoring a function didn't change its behavior, by re-running the same test cases from before the change.

## Materials Required
- Computer with VS Code and Python installed
- Working `compute_path` function from Lesson 4 (students should have this in their files)
- Hand-traced paths from Lesson 4 worksheets (for verification)
- Whiteboard or projector for live coding
- No robot needed -- all testing is done with print statements

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 8 min
**For 3-hour sessions:** 10-12 min

1. **Hook: Which Algorithm Is This?**
   - Display (or have students open) their `compute_path` function from Lesson 4
   - Ask: "In Module 5, you're going to write a second pathfinding function, breadth-first search. If both functions are named `compute_path`, what happens when you try to have both in the same file?"
   - Answer: "The second `def compute_path(...)` would silently replace the first one -- Python doesn't warn you. You'd lose access to the Manhattan version entirely."
   - Reveal: "The fix is simple -- give each algorithm a name that says which one it is: `compute_manhattan_path` and, later, `compute_dijkstra_path`."

2. **What Changes, What Stays the Same**:
   - Write on the board:
     ```
     Lesson 4:  compute_path(start, end)
     Lesson 5:  compute_manhattan_path(position, destination)
     ```
   - Ask: "What's actually different here?" (Just the name, and slightly clearer parameter names. The four while loops inside are identical.)
   - This is a deliberate, low-risk kind of change: a **rename**, not a rewrite. The algorithm students already tested in Lesson 4 doesn't need to be re-derived.

3. **Preview the Goal**:
   - Show the finished signature with a docstring:
     ```python
     def compute_manhattan_path(position, destination):
         """Compute a Manhattan path from position to destination.

         position:    a (row, col) tuple -- where the robot is now
         destination: a (row, col) tuple -- where it needs to go

         Returns a list of (row, col) tuples the robot should move to,
         not including position itself.
         """
     ```
   - Ask: "Why might a docstring matter more now than it did in Lesson 4?" (Once there are two pathfinding functions in the same program, a reader needs to be able to tell them apart at a glance -- the docstring plus the name both help.)

### Guided Practice: Renaming and Documenting (15 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 20 min

1. **Step 1: Copy and Rename**
   - Start from the working Lesson 4 function and rename it:
     ```python
     def compute_manhattan_path(position, destination):
         path = []
         current_row, current_col = position
         dest_row, dest_col = destination

         # Move south (rows increase)
         while current_row < dest_row:
             current_row = current_row + 1
             path.append((current_row, current_col))
         # Move north (rows decrease)
         while current_row > dest_row:
             current_row = current_row - 1
             path.append((current_row, current_col))
         # Move east (columns increase)
         while current_col < dest_col:
             current_col = current_col + 1
             path.append((current_row, current_col))
         # Move west (columns decrease)
         while current_col > dest_col:
             current_col = current_col - 1
             path.append((current_row, current_col))

         return path
     ```
   - Point out: "Every line inside the function is identical to Lesson 4 -- we changed the `def` line and the two variable names it unpacks from (`position`/`destination` instead of `start`/`end`)."

2. **Step 2: Add the Docstring**
   - Insert the docstring as the first line inside the function:
     ```python
     def compute_manhattan_path(position, destination):
         """Compute a Manhattan path from position to destination.

         position:    a (row, col) tuple -- where the robot is now
         destination: a (row, col) tuple -- where it needs to go

         Returns a list of (row, col) tuples the robot should move to,
         not including position itself.
         """
         path = []
         ...
     ```
   - Show `help(compute_manhattan_path)` in the Python shell, or hovering over the function name in VS Code, to see the docstring appear.

3. **Step 3: Re-run the Lesson 4 Tests**
   - The whole point of a rename is that behavior doesn't change. Prove it:
     ```python
     print("===== Regression Test =====")
     path = compute_manhattan_path((0, 0), (2, 3))
     print("(0,0) to (2,3):", path)

     path = compute_manhattan_path((3, 3), (1, 0))
     print("(3,3) to (1,0):", path)
     ```
   - Compare the output character-for-character against the Lesson 4 output. It should match exactly.
   - "This is called a **regression test** -- confirming a change didn't break anything that used to work."

### Independent Practice (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

**Exercise: Test `compute_manhattan_path()` Thoroughly**
- Students rename their own Lesson 4 function and add the docstring
- Write test code that computes and prints paths for at least 4 different position/destination pairs:

1. `(0, 0)` to `(2, 3)` -- south then east
2. `(2, 3)` to `(0, 1)` -- north then west
3. `(3, 0)` to `(1, 2)` -- north then east
4. `(1, 3)` to `(3, 1)` -- south then west

- For each test, compare the printed output to their hand-traced worksheets from Lesson 4
- Expected test program:
  ```python
  def compute_manhattan_path(position, destination):
      """Compute a Manhattan path from position to destination."""
      path = []
      current_row, current_col = position
      dest_row, dest_col = destination

      while current_row < dest_row:
          current_row = current_row + 1
          path.append((current_row, current_col))
      while current_row > dest_row:
          current_row = current_row - 1
          path.append((current_row, current_col))
      while current_col < dest_col:
          current_col = current_col + 1
          path.append((current_row, current_col))
      while current_col > dest_col:
          current_col = current_col - 1
          path.append((current_row, current_col))

      return path

  # Test 1: South then east
  path = compute_manhattan_path((0, 0), (2, 3))
  print("(0,0) to (2,3):", path)

  # Test 2: North then west
  path = compute_manhattan_path((2, 3), (0, 1))
  print("(2,3) to (0,1):", path)

  # Test 3: North then east
  path = compute_manhattan_path((3, 0), (1, 2))
  print("(3,0) to (1,2):", path)

  # Test 4: South then west
  path = compute_manhattan_path((1, 3), (3, 1))
  print("(1,3) to (3,1):", path)
  ```

- **Bonus: Test the edge cases**
  ```python
  # Same row (only column movement)
  print("(1,0) to (1,3):", compute_manhattan_path((1, 0), (1, 3)))

  # Same column (only row movement)
  print("(0,2) to (3,2):", compute_manhattan_path((0, 2), (3, 2)))

  # Same position (no movement needed)
  print("(2,1) to (2,1):", compute_manhattan_path((2, 1), (2, 1)))
  ```

## Assessment

**Formative (during lesson)**:
- Can students explain why a specific name matters once there's more than one algorithm?
- Can students identify that a docstring documents parameters and return value?
- Does the student's renamed function produce output that matches their Lesson 4 hand-traced paths exactly?

**Summative (worksheet/exit ticket)**:
1. Why did we rename `compute_path` to `compute_manhattan_path`?
2. What is a docstring, and where does it go in a function?
3. What does `current_row, current_col = position` do? What is this called?
4. If we call `compute_manhattan_path((2, 1), (2, 1))`, what does it return? Why?
5. Write the function from memory (or with minimal hints).

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "Renaming a function changes what it does" | A rename by itself changes nothing about behavior -- only what you call it. This lesson's whole point is to prove that with a regression test. |
| "The docstring is just a comment" | A docstring is a string literal, not a `#` comment -- Python and editors treat it specially (`help()`, tooltips). A regular comment does not show up that way. |
| "`compute_manhattan_path` and `compute_path` need to behave differently" | They are the same function with a new name and slightly renamed parameters. Every line of logic is identical to Lesson 4. |
| "I need to add `self` now" | No -- this stays a plain function. `self` only appears in the Optional Extension below, for courses that wrap it in a class. |

## Differentiation

**For struggling students**:
- Provide the renamed function as a handout; focus on writing the docstring and running the tests rather than retyping the whole algorithm
- Keep the Lesson 4 file open side-by-side for direct comparison
- Allow reference to the complete code on the board

**For advanced students**:
- Add a `manhattan_distance(position, destination)` helper function that returns just the distance (an integer), without computing the full path -- and confirm it equals `len(compute_manhattan_path(position, destination))`
- Write a `compute_manhattan_path_columns_first()` variant that does columns before rows, and compare the results
- Work through the Optional Extension below and compare the two versions directly

## Materials & Code Examples

### Complete Renamed Function
```python
def compute_manhattan_path(position, destination):
    """Compute a Manhattan path from position to destination.

    position:    a (row, col) tuple -- where the robot is now
    destination: a (row, col) tuple -- where it needs to go

    Returns a list of (row, col) tuples the robot should move to,
    not including position itself.
    """
    path = []
    current_row, current_col = position
    dest_row, dest_col = destination

    while current_row < dest_row:
        current_row = current_row + 1
        path.append((current_row, current_col))
    while current_row > dest_row:
        current_row = current_row - 1
        path.append((current_row, current_col))
    while current_col < dest_col:
        current_col = current_col + 1
        path.append((current_row, current_col))
    while current_col > dest_col:
        current_col = current_col - 1
        path.append((current_row, current_col))

    return path
```

### Expected Output
```
(0,0) to (2,3): [(1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]
(2,3) to (0,1): [(1, 3), (0, 3), (0, 2), (0, 1)]
(3,0) to (1,2): [(2, 0), (1, 0), (1, 1), (1, 2)]
(1,3) to (3,1): [(2, 3), (3, 3), (3, 2), (3, 1)]

(1,0) to (1,3): [(1, 1), (1, 2), (1, 3)]
(0,2) to (3,2): [(1, 2), (2, 2), (3, 2)]
(2,1) to (2,1): []
```

## Teaching Notes
- **This is a rename, not a rewrite.** Keep the cognitive load on naming and docstrings, not on re-deriving the algorithm. Students already earned that understanding in Lesson 4.
- **Regression testing is a real professional habit.** Frame the "re-run the same tests" step as something working developers actually do after every refactor, not busywork.
- **Foreshadow Module 5 explicitly.** Say out loud: "The reason we're doing this now, and not waiting, is that Module 5 will hand you a second function with a similar job. Distinct names prevent a nasty bug where one function silently overwrites the other."
- **Docstrings are new -- don't over-teach them.** A one- or two-sentence description plus a parameter list is enough. Students don't need `:param:`/`:returns:` formal docstring styles at this stage.

## Connections to Next Lessons
- **Lesson 6** will focus on systematic testing of `compute_manhattan_path()` using a `run_test()` helper -- students will compare output directly to the paths from this lesson.
- **Later lessons** will connect the computed path to actual robot movement on the physical grid.
- **Module 5** will introduce `compute_dijkstra_path()` -- a second function with a matching call shape, setting up the "swap the algorithm" lesson in Module 5 Lesson 6.

---

## Optional Extension: The `Manhattan` Class

*Do this after the functions version works. It is not graded; it is for students who did the Module 2 class extensions.*

### Why a class at all?
Not to remember the position. The rule from this lesson still holds inside a class: **the planner is told where the robot is.** `Manhattan` is a class *only* so that it has the same shape as the Module 5 and 6 planners (`BFS`, `Dijkstra`) -- then one main program and one test harness work with any of them by changing one name. Say this plainly; students who have just learned that objects hold state will expect `self.position`, and its absence is the point.

### From function to class

```python
class Manhattan:
    """The Lesson 5 planner as a class.

    It holds NO state: compute_path() is told the robot's position every
    time. Manhattan is a class only so that it has the same shape as the
    Module 5 and 6 planners -- then one main program and one test harness
    work with any of them by changing one name.
    """

    def __init__(self):
        pass        # nothing to set up

    def compute_path(self, position, destination):
        path = []
        current_row, current_col = position
        dest_row, dest_col = destination
        # ... the four while loops, unchanged ...
        return path
```

| Functions (required) | Class (extension) |
|---|---|
| `path = compute_manhattan_path((0, 0), (2, 3))` | `planner = Manhattan()` then `path = planner.compute_path((0, 0), (2, 3))` |

The function moved inside the class and gained `self`; nothing else changed. `__init__` is empty because Manhattan has nothing to set up. `BFS` in Module 5 uses its `__init__` to hold the list of blocked intersections, and that is the moment the class earns its keep.

### Discussion prompt
"Why doesn't `__init__` take a start position?" (Because then the class would have a second copy of where the robot is, and the driving code has the real one. The first time one is updated and the other is not, the robot plans from a place it isn't. Lesson 9 shows the bug that used to cause.)

### Code
`code/solutions/lesson-05-manhattan-class-addon.py` -- output identical to the function version.
