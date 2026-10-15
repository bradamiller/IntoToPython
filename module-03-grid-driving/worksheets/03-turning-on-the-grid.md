# Lesson 3 Worksheet: Turning on the Grid

**Name:** ________________________
**Date:** ________________________

---

## Part 1: Sequencing Drives and Turns

For each path description, write the sequence of function calls:

**Path A: Drive 2 forward, turn right, drive 1 forward**

```python
_________________________________
_________________________________
_________________________________
```

**Path B: Drive 1 forward, turn left, drive 3 forward**

```python
_________________________________
_________________________________
_________________________________
```

**Path C: Drive 2 forward, turn right, drive 2 forward, turn right, drive 2 forward**

```python
_________________________________
_________________________________
_________________________________
_________________________________
_________________________________
```

---

## Part 2: Drawing Paths

On this grid, draw the path for each sequence of commands. Mark the start with "S" and end with "E".

**Grid:**
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

**Sequence 1:** (starting at top-left, facing right)
```python
drive_intersections(3)
turn_clockwise()
drive_intersections(2)
```
Where does the robot end up? Row ____ Col ____

**Sequence 2:** (starting at top-left, facing down)
```python
drive_intersections(2)
turn_counterclockwise()
drive_intersections(1)
```
Where does the robot end up? Row ____ Col ____

---

## Part 3: True or False

| Statement | T/F | Explanation |
|---|---|---|
| After `turn_clockwise()`, you need another step before the next drive | ____ | __________ |
| The robot must be parked on an intersection to turn | ____ | __________ |
| `drive_intersections()` leaves the robot with its wheels on the last intersection | ____ | __________ |
| You can turn in the middle of a line segment | ____ | __________ |
| If you turn right after `track_to_intersection()` but before `drive_past_intersection()`, the turn pivots in the wrong place | ____ | __________ |
| After turning, a sensor is on the perpendicular line | ____ | __________ |

**In one sentence: what does `drive_past_intersection()` do for the turn that comes after it?**

______________________________________________________________

---

## Part 4: Path Planning

**Your challenge:** Plan a path that starts at one corner of the grid and ends at the opposite corner.

**Starting position:** Top-left corner, facing right

**Ending position:** Bottom-right corner

**Draw your planned path on the grid above.**

**Write the code sequence:**

```python
________________________________________
________________________________________
________________________________________
________________________________________
________________________________________
```

**How many total intersections does the robot pass through?** __________

**How many turns?** __________

---

## Part 5: Testing Log

Test your L-shape path on the robot:

| Test # | Path | Expected End | Actual End | Passed? |
|---|---|---|---|---|
| 1 | 2 forward, right, 2 forward | __________ | __________ | ____ |
| 2 | Your planned path from Part 4 | __________ | __________ | ____ |
| 3 | __________ | __________ | __________ | ____ |

**What adjustments did you make?**

______________________________________________________________

______________________________________________________________
