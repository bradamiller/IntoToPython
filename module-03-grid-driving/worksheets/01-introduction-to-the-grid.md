# Lesson 1 Worksheet: Introduction to the Grid

**Name:** ________________________
**Date:** ________________________

---

## Part 1: Grid vs. Circle

How does the grid compare to the circle from Module 2?

| Feature | Circle (Module 2) | Grid (Module 3) |
|---|---|---|
| Shape of the track | __________ | __________ |
| Number of crosses/intersections | __________ | __________ |
| Method to follow the line | __________ | __________ |
| Method to detect a cross | __________ | __________ |
| What happens at a cross? | __________ | __________ |

**Question:** Do you need to change your LineTrack class for the grid? Why or why not?

______________________________________________________________

______________________________________________________________

---

## Part 2: Grid Mapping

Label each intersection on this 4×4 grid with "+" and draw the lines connecting them:

```
   Col 0   Col 1   Col 2   Col 3

Row 0  ___  ---  ___  ---  ___  ---  ___

       |         |         |         |

Row 1  ___  ---  ___  ---  ___  ---  ___

       |         |         |         |

Row 2  ___  ---  ___  ---  ___  ---  ___

       |         |         |         |

Row 3  ___  ---  ___  ---  ___  ---  ___
```

**How many intersections are on this grid?** __________

**How many lines connect them?** __________

---

## Part 3: Code Matching

Match each LineTrack method to what it does on the grid:

| Method | What it does on the grid |
|---|---|
| `track_until_cross()` | A. Turns left onto the perpendicular line at an intersection |
| `turn_right()` | B. Follows the line until the robot reaches the next intersection |
| `turn_left()` | C. Turns right onto the perpendicular line at an intersection |

`track_until_cross()` → ____

`turn_right()` → ____

`turn_left()` → ____

---

## Part 4: Predict the Behavior

For each program, predict what the robot will do:

**Program 1:**
```python
tracker.track_until_cross()
```
What happens? ______________________________________________________________

**Program 2:**
```python
tracker.track_until_cross()
tracker.turn_right()
```
What happens? ______________________________________________________________

**Program 3:**
```python
tracker.track_until_cross()
tracker.turn_right()
tracker.track_until_cross()
```
What happens? ______________________________________________________________

---

## Part 5: Observation Log

Place the robot on the grid and run each program. Record what happens:

**Test 1: Drive to first intersection**

| | Expected | Actual |
|---|---|---|
| Robot follows line? | __________ | __________ |
| Robot stops at intersection? | __________ | __________ |
| Robot position after stopping? | __________ | __________ |

**Test 2: Drive to intersection and turn right**

| | Expected | Actual |
|---|---|---|
| Robot reaches intersection? | __________ | __________ |
| Robot turns onto perpendicular line? | __________ | __________ |
| Robot lined up after turn? | __________ | __________ |

**Any issues? What did you adjust?**

______________________________________________________________

______________________________________________________________
