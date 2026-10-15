# Lesson 7 Slide Outline: Obstacle Detection with the Rangefinder

## Slide 1: Title & Learning Objectives
**Title:** Obstacle Detection with the Rangefinder

**Learning Objectives:**
- Read distance measurements from the XRP ultrasonic rangefinder
- Determine whether an intersection is blocked using a distance threshold
- Update a blocked-nodes list based on live sensor readings
- Recompute a Dijkstra path after discovering a new obstacle

**Agenda:**
- What if the map is wrong? (5 min)
- The ultrasonic rangefinder (10 min)
- Reading distance at intersections (10 min)
- Threshold logic: blocked or clear? (5 min)
- Updating the blocked list and re-routing (10 min)
- Practice exercise (10 min)

---

## Slide 2: Hook — What If the Robot Finds a Wall That Wasn't on the Map?
**Question:** "You gave the robot a list of blocked intersections before it started. But what if there's an obstacle the robot didn't know about?"

**The problem:**
- So far, we hard-code the blocked list before the run
- In the real world, obstacles appear unexpectedly
- Construction, fallen objects, other robots — things change!

**The solution:** Give the robot a **sensor** so it can detect obstacles on its own.

**Today:** We'll use the XRP's ultrasonic rangefinder to detect obstacles at each intersection and reroute on the fly.

---

## Slide 3: The Ultrasonic Rangefinder
**How it works:** Sends out an ultrasonic pulse and measures how long the echo takes to return.

```python
from XRPLib.rangefinder import Rangefinder

rangefinder = Rangefinder.get_default_rangefinder()
distance = rangefinder.distance()  # returns distance in cm
```

**Key facts:**
| Property | Value |
|---|---|
| Returns | Distance in centimeters (float) |
| Range | ~2 cm to ~400 cm |
| Update speed | Very fast — can read many times per second |
| Mounted on | Front of the XRP robot |

**What it detects:** Any solid object in front of the robot — walls, boxes, other robots, your hand.

---

## Slide 4: Reading Distance at Intersections
**Strategy: Check for obstacles BEFORE driving into the next intersection.**

```python
# At each intersection, before moving forward:
distance = rangefinder.distance()
print(f"Distance ahead: {distance} cm")
```

**When to check:**
- After arriving at an intersection
- Before deciding to drive to the next one
- The robot is pointing in the direction it wants to go

**What the readings mean:**
```
distance > 30 cm  → Path ahead is clear
distance < 15 cm  → Something is blocking the path
15-30 cm           → Gray zone — might be an obstacle approaching
```

---

## Slide 5: Threshold Logic — Is It Blocked?
**We pick a threshold distance. If the reading is below the threshold, treat the intersection as blocked.**

```python
THRESHOLD = 15  # centimeters

distance = rangefinder.distance()

if distance < THRESHOLD:
    print("Obstacle detected! Path is blocked.")
    is_blocked = True
else:
    print("Path is clear.")
    is_blocked = False
```

**Why 15 cm?**
- Close enough that the obstacle is definitely in the robot's path
- Far enough that the robot has time to stop and reroute
- You may need to adjust based on your grid spacing

**Important:** The threshold depends on how far apart your intersections are. Test and tune!

---

## Slide 6: Updating the Blocked List
**When the robot detects an obstacle, add that intersection to the blocked list.**

```python
blocked_nodes = []  # starts empty — robot discovers obstacles

# At intersection (1, 2), robot checks ahead toward (1, 3):
distance = rangefinder.distance()

if distance < THRESHOLD:
    next_intersection = (1, 3)
    if next_intersection not in blocked_nodes:
        blocked_nodes.append(next_intersection)
        print(f"Added {next_intersection} to blocked list")
```

**The blocked list grows as the robot explores:**
```
Run starts:    blocked_nodes = []
After check 1: blocked_nodes = [(1, 3)]
After check 2: blocked_nodes = [(1, 3), (2, 1)]
```

**Key idea:** The robot builds its own map of obstacles through experience.

---

## Slide 7: Which Intersection Is Ahead?
**Before we can add to the blocked list, we need to know which intersection the rangefinder is pointed at.**

```python
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

def get_next_intersection(current_pos, heading):
    """Return the intersection directly ahead of the robot."""
    row, col = current_pos
    if heading == NORTH:
        return (row - 1, col)
    elif heading == EAST:
        return (row, col + 1)
    elif heading == SOUTH:
        return (row + 1, col)
    elif heading == WEST:
        return (row, col - 1)
```

**We already have `desired_heading()` from Module 4 Lesson 8 doing the reverse of this.** Here we just need the forward version: given position and heading, what's ahead?

---

## Slide 8: Re-routing After Detection
**After discovering a new obstacle, rebuild the graph and recompute the path using the updated blocked list.**

```python
# At each intersection, before driving to the next one:
distance = rangefinder.distance()

if distance < OBSTACLE_THRESHOLD:
    blocked_node = get_next_intersection(current_pos, heading)
    if blocked_node not in blocked_list:
        blocked_list.append(blocked_node)
        print(f"Obstacle detected at {blocked_node}!")
        print(f"Blocked list is now: {blocked_list}")

        # Recompute the path with updated blocked list
        graph = build_dijkstra_graph(rows, cols, blocked_list)
        new_path = compute_dijkstra_path(current_pos, destination, graph)
        print(f"New path: {new_path}")
```

**The flow:**
1. Robot arrives at intersection
2. Check rangefinder for obstacle ahead
3. If blocked: add to blocked list, rebuild the graph, recompute path from current position
4. If clear: continue on current path
5. Drive to next intersection
6. Repeat

---

## Slide 9: Your Turn!
**Activity: Add Obstacle Detection to Your Navigation Program**

1. Set up the rangefinder:
   ```python
   from XRPLib.rangefinder import Rangefinder
   rangefinder = Rangefinder.get_default_rangefinder()
   ```
2. Before each move, read the distance and print it
3. Choose a threshold (start with 15 cm and adjust)
4. If an obstacle is detected:
   - Add the blocked intersection to your blocked list
   - Recompute the path using Dijkstra
   - Print the new path
5. Test by placing an object on the grid and watching the robot reroute

**Checkpoints:**
- Can the robot read distance values from the rangefinder?
- Does the robot correctly identify when an intersection is blocked?
- Does the blocked list update when a new obstacle is found?
- Does the robot recompute and follow a new path around the obstacle?

---

## Slide 10: Debugging Tips
**Common issues and how to fix them:**

| Problem | Likely Cause | Fix |
|---|---|---|
| Distance always reads 0 | Rangefinder not connected | Check wiring and port |
| Robot detects "obstacles" that aren't there | Threshold too high | Lower the threshold value |
| Robot misses real obstacles | Threshold too low | Raise the threshold value |
| Robot gets stuck in a loop | Re-routing leads back to same blocked node | Make sure blocked list persists across recomputations |
| Path recomputation is wrong | Using old position as start | Use current intersection, not original start |

**Pro tip:** Print the distance reading and blocked list at every intersection so you can see what the robot "sees."

---

## Slide 11: Connection to Next Lesson
**What you did today:**
- Used the ultrasonic rangefinder to detect obstacles
- Applied a threshold to decide if an intersection is blocked
- Updated the blocked list dynamically during a run
- Recomputed paths on the fly using Dijkstra

**Next lesson (Lesson 8):**
- Make the robot **remember** obstacles across multiple runs
- First run: discover obstacles and save them
- Second run: start with knowledge from the first run
- The robot gets smarter with experience!

**Key insight:** Today the robot discovers obstacles during a single run. Next lesson, it will carry that knowledge forward so it starts smarter each time.
