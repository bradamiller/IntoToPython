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
| Function to follow the line | __________ | __________ |
| Function to detect a cross | __________ | __________ |
| What happens at a cross? | __________ | __________ |

**Question:** Do you need to change your Module 2 toolkit for the grid? Why or why not?

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

Match each toolkit function to what it does on the grid, and write what ends it:

| Function | What it does on the grid | Ends when... |
|---|---|---|
| `track_to_intersection()` | A. Turns left onto the perpendicular line | |
| `drive_past_intersection()` | B. Follows the line until the sensors reach the next intersection | |
| `turn_clockwise()` | C. Drives 8.75 cm so the wheels are on the intersection and the sensors are past it | |
| `turn_counterclockwise()` | D. Turns right onto the perpendicular line | |

`track_to_intersection()` -> ____   `drive_past_intersection()` -> ____   `turn_clockwise()` -> ____   `turn_counterclockwise()` -> ____

**Which of these four functions knows the robot is on a grid?** ______________________

---

## Part 4: Predict the Behavior

For each program, predict what the robot will do and where its wheels end up:

**Program 1:**
```python
track_to_intersection()
```
What happens? ______________________________________________________________
Where are the wheels? _______________________________

**Program 2:**
```python
track_to_intersection()
drive_past_intersection()
```
What happens? ______________________________________________________________
Where are the wheels? _______________________________

**Program 3:**
```python
track_to_intersection()
drive_past_intersection()
turn_clockwise()
track_to_intersection()
```
What happens? ______________________________________________________________

**Program 4 (the robot starts sitting ON an intersection):**
```python
track_to_intersection()
```
What happens, and why? ______________________________________________________________

---

## Part 5: Observation Log

Place the robot on the grid and run each program. Record what happens:

**Test 1: Arrive at the first intersection (Program 2)**

| | Expected | Actual |
|---|---|---|
| Robot follows line? | __________ | __________ |
| Robot stops after the drive-past? | __________ | __________ |
| Wheels over the intersection? | __________ | __________ |

**Test 2: Arrive and turn clockwise**

| | Expected | Actual |
|---|---|---|
| Robot reaches intersection? | __________ | __________ |
| Robot pivots on the intersection? | __________ | __________ |
| A sensor on the new line after the turn? | __________ | __________ |

**Any issues? What did you adjust?**

______________________________________________________________

______________________________________________________________
