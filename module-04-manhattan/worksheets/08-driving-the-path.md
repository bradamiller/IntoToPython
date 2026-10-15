# Lesson 8 Worksheet: Driving the Path

**Name:** ________________________
**Date:** ________________________

---

## Part 1: The toolkit and the wrinkle

1. Fill in what ends each Module 2 function:

| Function | Ends when... |
|---|---|
| `track_to_intersection()` | ______________________________________ |
| `turn_clockwise()` | ______________________________________ |
| `drive_past_intersection()` | ______________________________________ |

2. Which of these functions knows the robot's row and column? ______________________

3. At the moment `track_to_intersection()` stops, where are the sensors? ______________ Where are the wheels? ______________

4. The robot turns without calling `drive_past_intersection()` first. Where does it pivot, and where do the sensors end up?

_______________________________________________________________

5. Why is `drive_past_intersection()` called after *every* track, not just when the robot is going straight on?

_______________________________________________________________

## Part 2: Trace `drive_path`

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

Path `[(1, 0), (1, 1), (0, 1)]`, start (0, 0) heading 0 (N).

| Step | position | next_pos | needed | `(needed - heading) % 4` | robot does | heading after |
|---|---|---|---|---|---|---|
| 1 | (0, 0) | (1, 0) | _____ | _____ | __________________ | _____ |
| 2 | ______ | (1, 1) | _____ | _____ | __________________ | _____ |
| 3 | ______ | (0, 1) | _____ | _____ | __________________ | _____ |

6. What does the function return? `( ________ , ____ )`

7. How many times is `track_to_intersection()` called? ____ `drive_past_intersection()`? ____

## Part 3: The two assignments, and the one outside

8. Circle the two lines inside `drive_path` that keep `heading` and `position` up to date. Why does `turn_to` have to `return desired` for the first one to work?

_______________________________________________________________

9. A classmate's main program:

```python
path = compute_manhattan_path(position, (2, 2))
drive_path(path, position, heading)
path = compute_manhattan_path(position, (0, 2))
drive_path(path, position, heading)
```

The first path drives perfectly. Describe what the second one does and why.

_______________________________________________________________

_______________________________________________________________

Fix the two `drive_path` lines:

```python
_______________________________________________

_______________________________________________
```

## Part 4: Plan, print, button, drive

10. Put these lines in the right order (number them 1-5):

____ `board.wait_for_button()`
____ `position, heading = drive_path(path, position, heading)`
____ `path = compute_manhattan_path(position, destination)`
____ `print("Arrived at:", position)`
____ `print("Path:", path)`

11. The printed path is `[(1, 0), (2, 0), (2, 1)]`, which is right. The robot drives to (1, 0), then turns around and drives back to (0, 0). Which half of the program has the bug -- planner or driving -- and what is the first function you would open?

_______________________________________________________________

## Part 5: Desktop mode

12. You replace the four Module 2 calls with `print()` calls and run the program on your laptop. Write the output for path `[(1, 0), (1, 1)]` from (0, 0) heading 0:

```
Path: [(1, 0), (1, 1)]




```

## Exit ticket

At (1, 2) heading 1 (E), the next intersection is (1, 1). What heading is needed, what is `(needed - heading) % 4`, and what does the robot do?

_______________________________________________________________

---

## Optional Extension: `self` is the address

E1. In the house figure, what does `elm.paint()` mean in words? Inside `paint()`, what is `self`?

_______________________________________________________________

E2. A student writes `def turn_to(desired):` inside the `Navigator` class (no `self`). Python says `takes 1 positional argument but 2 were given`. Explain the error using the work-order picture.

_______________________________________________________________

E3. Another writes `heading = desired` inside `turn_to` instead of `self.heading = desired`. What goes wrong, and which house's heading got updated?

_______________________________________________________________

E4. In the class version, `drive_path(self, path)` returns nothing. Why doesn't the main program need a return value any more?

_______________________________________________________________
