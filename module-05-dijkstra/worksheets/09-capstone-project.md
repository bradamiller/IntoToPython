# Lesson 9 Worksheet: Capstone Project

**Name:** ________________________
**Date:** ________________________

---

## Part A: System Architecture

The capstone project combines everything from this module. Draw arrows to show how the components connect.

**Components:**

1. **Dijkstra class** — Finds shortest paths on the grid graph
2. **Navigator class** — Drives the robot along a path (turn + drive)
3. **Rangefinder** — Detects obstacles ahead of the robot
4. **Obstacle memory** (blocked list) — Remembers discovered obstacles
5. **Main program** — Coordinates everything

**Fill in the connections:**

```
Main Program
    |
    |--- Creates __________ with start position and blocked list
    |
    |--- Creates __________ to drive the robot
    |
    |--- Uses __________ to check for obstacles
    |
    |--- Maintains __________ across multiple destinations
```

**Describe the main loop of the capstone program:**

1. Choose next __________ from the list
2. Use __________ to compute path to destination
3. For each step in the path:
   a. Check for __________ using rangefinder
   b. If obstacle found, update __________ and __________ path
   c. Use __________ to drive to next intersection
4. Repeat for next __________

**What happens if an obstacle is detected mid-path?**

____________________________________________________________________

____________________________________________________________________

---

## Part B: Destination Planning

On the 4x4 grid below, choose 4 destinations for your robot to visit in order. Mark them with numbers 1-4. The robot starts at (0, 0).

```
     Col 0   Col 1   Col 2   Col 3
Row 0:  S  ---  .  ---  .  ---  .
        |       |       |       |
Row 1:  .  ---  .  ---  .  ---  .
        |       |       |       |
Row 2:  .  ---  .  ---  .  ---  .
        |       |       |       |
Row 3:  .  ---  .  ---  .  ---  .
```

S = Start (0, 0)

**My destinations (in order):**

| Order | Destination (row, col) | Why I chose this |
|---|---|---|
| 1 | (______, ______) | __________________________________________ |
| 2 | (______, ______) | __________________________________________ |
| 3 | (______, ______) | __________________________________________ |
| 4 | (______, ______) | __________________________________________ |

**Total Manhattan distance for all 4 trips:** __________

*(Add up the Manhattan distance from start to dest 1, dest 1 to dest 2, dest 2 to dest 3, dest 3 to dest 4)*

---

## Part C: Predict Paths

Assume the grid has obstacles at **(1, 1)** and **(2, 3)**.

```
     Col 0   Col 1   Col 2   Col 3
Row 0:  S  ---  .  ---  .  ---  .
        |               |       |
Row 1:  .     [X X]     .  ---  .
        |               |       |
Row 2:  .  ---  .  ---  .     [X X]
        |       |       |
Row 3:  .  ---  .  ---  .  ---  .
```

Using your destinations from Part B, hand-trace the Dijkstra paths:

**Trip 1:** (0, 0) to destination 1 = (______, ______)

Path: ____________________________________________________________________

Length: __________

**Trip 2:** destination 1 to destination 2 = (______, ______) to (______, ______)

Path: ____________________________________________________________________

Length: __________

**Trip 3:** destination 2 to destination 3 = (______, ______) to (______, ______)

Path: ____________________________________________________________________

Length: __________

**Trip 4:** destination 3 to destination 4 = (______, ______) to (______, ______)

Path: ____________________________________________________________________

Length: __________

**Total steps for all 4 trips:** __________

**How does this compare to your Manhattan estimate from Part B?**

____________________________________________________________________

---

## Part D: Testing Checklist

Before running your capstone on the actual robot, verify each item:

**Code checks:**

| Check | Done? |
|---|---|
| Dijkstra class has `__init__`, `build_graph`, `compute_path` | ______ |
| `build_graph` correctly excludes blocked nodes | ______ |
| `compute_path` returns a list of (row, col) tuples | ______ |
| `compute_path` handles blocked destinations | ______ |
| Navigator class can follow a path of (row, col) tuples | ______ |
| Rangefinder setup uses correct import and initialization | ______ |
| Obstacle detection uses a reasonable threshold | ______ |
| Blocked list is updated when obstacles are found | ______ |
| Path is recomputed after discovering an obstacle | ______ |
| Multiple destinations are visited in order | ______ |

**Test scenarios to run in code (without robot):**

| Test | Expected Result | Actual Result |
|---|---|---|
| Path with no obstacles | Shortest direct path | ________________ |
| Path with one obstacle on route | Path goes around | ________________ |
| Path to a blocked destination | Returns empty list | ________________ |
| Start = destination | Returns [start] | ________________ |
| Multiple destinations in sequence | Correct paths for each | ________________ |

**Robot tests:**

| Test | Pass? |
|---|---|
| Robot drives straight between two adjacent intersections | ______ |
| Robot turns correctly at an intersection | ______ |
| Rangefinder detects an obstacle placed on the grid | ______ |
| Robot stops and recomputes when obstacle found | ______ |
| Robot successfully visits all 4 destinations | ______ |

---

## Part E: Reflection Questions

**1. What was the most challenging part of this module?**

____________________________________________________________________

____________________________________________________________________

**2. How does Dijkstra's algorithm compare to how you would find a path yourself?**

____________________________________________________________________

____________________________________________________________________

**3. What would you need to change to use a larger grid (e.g., 8x8)?**

____________________________________________________________________

____________________________________________________________________

**4. What other information could the robot remember between runs besides obstacles?**

____________________________________________________________________

____________________________________________________________________

**5. If two paths have the same length, how does Dijkstra decide which one to use?**

____________________________________________________________________

____________________________________________________________________

**6. Real-world GPS navigation uses algorithms similar to Dijkstra. What is different about real roads compared to our grid?**

____________________________________________________________________

____________________________________________________________________

____________________________________________________________________

**7. What would you add to this project if you had more time?**

____________________________________________________________________

____________________________________________________________________

____________________________________________________________________

---

**Congratulations!** You have completed the Dijkstra's Algorithm module. You built a pathfinding system that can navigate around obstacles and learn from experience.
