# Lesson 4 Worksheet: Module 3 Final Project — Square Pattern

**Name:** ________________________
**Date:** ________________________

---

## Part 1: Planning the Square

Draw your square path on this grid. Mark the start with "S", draw arrows for the path, and mark each intersection you pass through.

```
+ --- + --- + --- + --- +
|     |     |     |     |
+ --- + --- + --- + --- +
|     |     |     |     |
+ --- + --- + --- + --- +
|     |     |     |     |
+ --- + --- + --- + --- +
|     |     |     |     |
+ --- + --- + --- + --- +
```

**Starting position (row, col):** __________

**Starting direction (which way is the robot facing?):** __________

**Number of intersections per side:** __________

**Number of sides:** __________

**Total intersections the robot will pass through:** __________

---

## Part 2: Loop Tracing

Trace through the square loop and fill in what happens on each iteration:

```python
for leg in range(4):
    drive_intersections(tracker, 2)
    tracker.turn_right()
```

| leg | drive_intersections(2) does... | turn_right() does... | Robot now facing... |
|---|---|---|---|
| 0 | Drives forward __ intersections | Turns ___° | __________ |
| 1 | Drives forward __ intersections | Turns ___° | __________ |
| 2 | Drives forward __ intersections | Turns ___° | __________ |
| 3 | Drives forward __ intersections | Turns ___° | __________ |

**After 4 iterations, is the robot back at the start?** __________

**How many total right turns?** __________

**Total degrees turned:** ____ × 90° = ____°

---

## Part 3: Code Review

This is a student's attempt at the square pattern. Find and circle the errors:

```python
board.wait_for_button()

for leg in range(3):
    drive_intersections(tracker, 2)
    tracker.drivetrain.set_effort(0.3, 0.3)
    time.sleep(0.3)
    tracker.turn_right()
```

**Error 1:** ______________________________________________________________

**Error 2:** ______________________________________________________________

**Write the corrected code:**

```python
board.wait_for_button()

_______________________________________________
_______________________________________________
_______________________________________________
```

---

## Part 4: Testing Log

Record each test run:

| Test # | What you tested | Result | What you changed |
|---|---|---|---|
| 1 | One side (2 intersections) | __________ | __________ |
| 2 | One side + turn | __________ | __________ |
| 3 | Two sides (half square) | __________ | __________ |
| 4 | Full square (4 sides) | __________ | __________ |
| 5 | (if needed) | __________ | __________ |

**Did the robot return to its starting position?** __________

**If not, what was off?** ______________________________________________________________

---

## Part 5: Extension Challenge

**Choose one extension and plan it:**

- [ ] **Bigger square** (3 intersections per side)
- [ ] **Rectangle** (2 and 3 intersections alternating)
- [ ] **Left-turn square** (using turn_left)
- [ ] **Your own shape:** ______________

**Plan your extension:**

Number of sides/legs: __________

For each leg, how many intersections and which turn?

| Leg | Intersections | Turn direction |
|---|---|---|
| 1 | __________ | __________ |
| 2 | __________ | __________ |
| 3 | __________ | __________ |
| 4 | __________ | __________ |

**Write the code for your extension:**

```python
________________________________________
________________________________________
________________________________________
________________________________________
________________________________________
```

---

## Part 6: Reflection

**What was the hardest part of getting the square to work?**

______________________________________________________________

**How did the for loop help (compared to writing each side separately)?**

______________________________________________________________

**What concept from Module 2 was most important for this project?**

______________________________________________________________

**How is this different from the polygon shapes in Module 1?**

______________________________________________________________
