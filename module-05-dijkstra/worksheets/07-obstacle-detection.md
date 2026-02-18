# Lesson 7 Worksheet: Obstacle Detection

**Name:** ________________________
**Date:** ________________________

---

## Part A: Rangefinder Basics

The XRP robot has a rangefinder (ultrasonic distance sensor) that measures how far away objects are.

**1. What does `rangefinder.distance()` return?**

____________________________________________________________________

**2. What units does the rangefinder use?**

____________________________________________________________________

**3. If the rangefinder reads `5.0`, what does that mean?**

____________________________________________________________________

**4. If the rangefinder reads `50.0`, what does that mean?**

____________________________________________________________________

**5. Fill in the import and setup code:**

```python
from XRPLib.__________ import __________

rangefinder = Rangefinder.__________()
distance = rangefinder.__________()
print("Distance:", distance)
```

---

## Part B: Threshold Logic

We use a **threshold** to decide if a rangefinder reading means "obstacle" or "clear." For example, if our threshold is 15 cm, anything less than 15 cm is an obstacle.

**Given threshold = 15 cm, fill in the table:**

| Rangefinder Reading (cm) | Obstacle? (Yes/No) | Explanation |
|---|---|---|
| 5.2 | __________ | __________________________________________ |
| 14.9 | __________ | __________________________________________ |
| 15.0 | __________ | __________________________________________ |
| 15.1 | __________ | __________________________________________ |
| 30.0 | __________ | __________________________________________ |
| 2.0 | __________ | __________________________________________ |

**Write the Python condition that checks if a distance reading indicates an obstacle:**

```python
threshold = 15
distance = rangefinder.distance()

if __________________________________________:
    print("Obstacle detected!")
else:
    print("Path is clear")
```

**Why do we use a threshold instead of checking for exactly 0?**

____________________________________________________________________

____________________________________________________________________

---

## Part C: Scenario Walkthrough

The robot is navigating a 4x4 grid. It has reached intersection (1, 1) and needs to check for obstacles before moving forward.

**Scenario 1:** Robot is at (1, 1), facing right (toward (1, 2)). Rangefinder reads 8.3 cm. Threshold = 15 cm.

- Is (1, 2) blocked? __________
- Should the robot add (1, 2) to the blocked list? __________
- What should the robot do next? __________________________________________

**Scenario 2:** Robot is at (1, 1), facing right (toward (1, 2)). Rangefinder reads 42.0 cm. Threshold = 15 cm.

- Is (1, 2) blocked? __________
- Should the robot add (1, 2) to the blocked list? __________
- What should the robot do next? __________________________________________

**Scenario 3:** Robot is at (0, 0), facing down (toward (1, 0)). Rangefinder reads 10.5 cm. Threshold = 15 cm.

- Which cell is potentially blocked? __________
- The robot adds (1, 0) to blocked list. Now blocked = [(1, 0)].
- The robot needs to reach (3, 0). What should it do?

____________________________________________________________________

____________________________________________________________________

**Scenario 4:** Robot arrives at (2, 1). It checks ahead (toward (2, 2)) and reads 7.1 cm. It already has blocked = [(1, 1)].

- Updated blocked list: __________________________________________
- Should the robot recompute its path? __________
- Why? ____________________________________________________________________

---

## Part D: Code Completion

Fill in the blanks to complete the obstacle detection function.

```python
from XRPLib.rangefinder import Rangefinder

rangefinder = Rangefinder.get_default_rangefinder()

def check_for_obstacle(current_position, facing_direction, blocked_list, threshold=15):
    """
    Check if there is an obstacle in the direction the robot is facing.

    Parameters:
        current_position: tuple (row, col) where the robot is now
        facing_direction: tuple (dr, dc) indicating direction faced
        blocked_list: list of blocked (row, col) tuples
        threshold: distance in cm below which we call it an obstacle

    Returns:
        True if obstacle detected and added, False otherwise
    """
    # Step 1: Read the rangefinder
    distance = __________________________________________

    # Step 2: Check if the reading indicates an obstacle
    if __________ __________ __________:
        # Step 3: Calculate the position of the obstacle
        row, col = current_position
        dr, dc = __________________________________________
        obstacle_position = (__________, __________)

        # Step 4: Add to blocked list if not already there
        if obstacle_position __________ __________:
            __________.append(__________)
            print("Obstacle detected at", obstacle_position)
            return __________

    return __________
```

**Test your understanding:** If the robot is at (1, 1) facing right (direction = (0, 1)) and the rangefinder reads 6.0 cm:

- What is `obstacle_position`? __________
- Is it added to blocked_list? __________

---

## Answer Key

### Part A:
1. A floating-point number representing the distance to the nearest object
2. Centimeters (cm)
3. There is an object 5.0 cm away from the sensor
4. There is an object 50.0 cm away (or nothing nearby)
5. `from XRPLib.rangefinder import Rangefinder`, `Rangefinder.get_default_rangefinder()`, `rangefinder.distance()`

### Part B:
| Reading | Obstacle? | Explanation |
|---|---|---|
| 5.2 | Yes | 5.2 < 15 |
| 14.9 | Yes | 14.9 < 15 |
| 15.0 | No | 15.0 is not less than 15 |
| 15.1 | No | 15.1 > 15 |
| 30.0 | No | 30.0 > 15 |
| 2.0 | Yes | 2.0 < 15 |

Condition: `if distance < threshold:`

Threshold because sensors are not perfect — objects have varying distances, and we need a cutoff to distinguish "something close" from "nothing there."

### Part C:
1. Yes blocked, yes add, recompute path using Dijkstra to avoid (1,2)
2. Not blocked, don't add, continue on current path
3. (1,0) is potentially blocked. Robot should use Dijkstra to compute a new path from (0,0) to (3,0) with blocked=[(1,0)], which will go around via column 1.
4. blocked = [(1,1), (2,2)]. Yes recompute — the blocked list changed so the previous path may go through (2,2).

### Part D:
```python
distance = rangefinder.distance()
if distance < threshold:
    dr, dc = facing_direction
    obstacle_position = (row + dr, col + dc)
    if obstacle_position not in blocked_list:
        blocked_list.append(obstacle_position)
        return True
return False
```

Test: obstacle_position = (1, 2), yes it is added.
