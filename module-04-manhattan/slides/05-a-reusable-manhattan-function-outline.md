# Lesson 5 Slide Outline: A Reusable Manhattan Function

## Slide 1: Title & Learning Objectives
**Title:** A Reusable Manhattan Function

**Learning Objectives:**
- Explain why a specific function name matters once there's more than one algorithm
- Add a docstring documenting parameters and return value
- Rename a function without changing its behavior
- Regression-test the renamed function against Lesson 4's output

**Agenda:**
- Which algorithm is this? (5 min)
- Rename and document (10 min)
- Regression test (10 min)
- Practice: test 4+ destination pairs (15 min)

---

## Slide 2: Hook — Which Algorithm Is This?

**In Module 5, you'll write a SECOND pathfinding function: Dijkstra's algorithm.**

```python
def compute_path(start, end):   # <- Lesson 4's name
    ...

def compute_path(position, destination):   # <- Module 5's Dijkstra, same name!
    ...
```

**What happens if both are named `compute_path`?** The second `def` silently replaces the first -- no warning. You'd lose the Manhattan version entirely.

**The fix:** name each algorithm specifically -- `compute_manhattan_path` and (later) `compute_dijkstra_path`.

---

## Slide 3: What Changes, What Stays the Same

```
Lesson 4:   compute_path(start, end)
Lesson 5:   compute_manhattan_path(position, destination)
```

**A rename, not a rewrite:** every line of logic inside the function is identical to Lesson 4 -- only the `def` line and parameter names change.

**Why `position` instead of `start`?** It matches how the function gets used later: the robot's *current* position, called again and again as it moves, not just a one-time starting point.

---

## Slide 4: Adding a Docstring

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

A docstring is a string literal right after `def` -- shows up in `help()` and editor tooltips. Once there are two pathfinding functions in the same program, a reader needs to tell them apart at a glance.

---

## Slide 5: Regression Test

**The whole point of a rename is that behavior doesn't change. Prove it:**

```python
print("===== Regression Test =====")
path = compute_manhattan_path((0, 0), (2, 3))
print("(0,0) to (2,3):", path)

path = compute_manhattan_path((3, 3), (1, 0))
print("(3,3) to (1,0):", path)
```

Compare the output character-for-character against Lesson 4's output. It should match exactly.

**This is called a regression test** — confirming a change didn't break anything that used to work.

---

## Slide 6: The Complete Renamed Function

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
```

---

## Slide 7: Your Turn!

1. Rename your Lesson 4 function to `compute_manhattan_path(position, destination)`
2. Add the docstring
3. Regression-test against your Lesson 4 hand traces
4. Test at least 4 position/destination pairs:
   - `(0, 0)` to `(2, 3)` — south then east
   - `(2, 3)` to `(0, 1)` — north then west
   - `(3, 0)` to `(1, 2)` — north then east
   - `(1, 3)` to `(3, 1)` — south then west
5. Bonus: test the edge cases (same row, same column, same position)

---

## Slide 8: What's Next

**Today:** Renamed and documented `compute_manhattan_path` -- same algorithm, a name specific enough to survive Module 5.

**Next lesson (Lesson 6 — Testing Without a Robot):** Systematic testing with a `run_test()` helper, comparing output to hand traces.

**Optional Extension:** Courses that also cover classes can wrap this same function in a `Manhattan` class -- see the separate "Implementing the Manhattan Class" deck.
