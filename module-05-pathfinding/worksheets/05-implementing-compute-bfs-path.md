# Lesson 5 Worksheet: Implementing compute_bfs_path()

**Name:** ________________________
**Date:** ________________________

---

## Part A: Every line is a pencil step

Here is the search loop. Next to each line, write the step you did by hand in Lesson 3.

```python
previous = {position: None}          # A ______________________________
to_visit = [position]                # B ______________________________

while len(to_visit) > 0:
    current = to_visit.pop(0)        # C ______________________________
    if current == destination:
        break                        # D ______________________________
    for neighbor in graph[current]:  # E ______________________________
        if neighbor not in previous: # F ______________________________
            previous[neighbor] = current     # G ______________________
            to_visit.append(neighbor)        # H ______________________
```

**1.** `previous` is a dictionary. What are its keys, and what are its values?

Keys: ______________________________ Values: ______________________________

**2.** "An intersection has been reached" and "an intersection is a key in `previous`" -- are these the same thing? ______ Explain.

_______________________________________________________________

---

## Part B: Oldest first

**3.** `to_visit.pop(0)` takes the item at the ______________ of the list. `to_visit.pop()` takes the item at the ______________.

**4.** Trace the first four values of `current` on the open 3×3 grid starting at (0,0), with neighbors checked up, down, left, right.

| Pop # | `current` | `to_visit` afterward |
|---|---|---|
| 1 | (0,0) | |
| 2 | | |
| 3 | | |
| 4 | | |

**5.** Now suppose the line were `to_visit.pop()` instead. What would the *second* value of `current` be? ______ Which ring is it in? ______ What rule from Lesson 3 does this break?

_______________________________________________________________

---

## Part C: The walk-back

```python
path = []
current = destination
while current != position:
    path.append(current)
    current = previous[current]
path.reverse()
return path
```

**6.** `previous` is `{(0,0): None, (1,0): (0,0), (0,1): (0,0), (2,0): (1,0), (2,1): (2,0), (2,2): (2,1), ...}`. Trace the walk-back from (2,2) to (0,0):

| Loop pass | `current` at the top | `path` after append |
|---|---|---|
| 1 | (2,2) | |
| 2 | | |
| 3 | | |
| 4 | | |
| stops because | | |

After `reverse()`: `path = ______________________________________`

**7.** The loop stops when `current` equals the start, *before* appending it. Which of the two planner rules does this take care of? ______ What would be wrong with the path if the loop ran "until `None`" instead?

_______________________________________________________________

**8.** `position == destination`. How many times does the walk-back loop run? ______ What is returned? ______

**9.** The destination was walled off and never reached. Which line returns `[]` in that case, and what does it check?

_______________________________________________________________

---

## Part D: Run it and break it

Finish the function in the starter file and run the five tests.

**10.** Fill in the step counts the program printed:

| Test | Steps |
|---|---|
| 1 open grid (0,0)→(3,3) | |
| 2 straight line (0,0)→(0,3) | |
| 3 already there | |
| 4 wall at (1,0),(1,1), (0,0)→(3,0) | |
| 5 walled off | |

**11.** Test 4's path from the program: ______________________________________________

Your Lesson 3 Part D path: ______________________________________________

Same path? ______ Same number of steps? ______

**12.** Change `pop(0)` to `pop()`. Run Test 1. Steps: ______ Why is it different?

_______________________________________________________________

**13.** Put `pop(0)` back. Now delete the line `if neighbor not in previous:` (keep the two lines under it, un-indented one level). Run Test 1. What happens? (If it never stops, press Ctrl-C.)

_______________________________________________________________

Why? (What does that `if` protect?)

_______________________________________________________________

**14.** Put it back. Run the `print_grid` block for the wall at (1,0),(1,1). Copy the ring number the program put on (3,0): ______ Does it match your Lesson 3 Part D grid? ______

---

## Exit ticket

A classmate's walk-back is:

```python
current = destination
while current is not None:
    path.append(current)
    current = previous[current]
path.reverse()
```

Their Test 2 prints `Steps: 4`. What is in their path that should not be, and which rule is it breaking?

_______________________________________________________________
