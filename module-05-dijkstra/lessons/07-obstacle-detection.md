# Lesson 7: Obstacle Detection with the Rangefinder

## Overview
Students learn to use the XRP ultrasonic rangefinder sensor to detect obstacles on the physical grid, then integrate obstacle detection into the navigation loop so the robot can discover blocked intersections in real time and recompute its path using Dijkstra. Until now, the blocked list has been hard-coded -- students manually typed in which intersections were blocked before running the program. In this lesson, the robot becomes autonomous: it checks the rangefinder at each intersection, determines whether the next intersection ahead is blocked based on a distance threshold, adds newly discovered obstacles to the blocked list, and asks Dijkstra to recompute the path. The core loop becomes: **check, detect, update, recompute, drive**. This is the lesson where the robot starts to feel "smart" -- it reacts to its environment rather than blindly following a pre-planned path.

This lesson is the hardware integration point for Module 5. Students already know how to build graphs (Lesson 1), represent them as dictionaries (Lesson 2), run Dijkstra's algorithm (Lesson 3), and implement the Dijkstra class (Lessons 4-5). They have tested and swapped the class into the Navigator (Lesson 6). Now they connect the last piece: real sensor data flowing into the pathfinding algorithm. The rangefinder is the robot's "eyes," and Dijkstra is its "brain." Together, they enable reactive navigation -- the same principle used by warehouse robots, autonomous vehicles, and Mars rovers.

## Learning Objectives
By the end of this lesson, students will be able to:
- Import and initialize the XRP rangefinder sensor
- Read distance values from the rangefinder using `rangefinder.distance()`
- Explain how ultrasonic rangefinders measure distance (sound pulse, echo, time calculation)
- Implement threshold logic to determine if an intersection ahead is blocked
- Add a detected obstacle to the blocked list at runtime
- Recompute the path using Dijkstra after updating the blocked list
- Integrate the check-detect-update-recompute-drive loop into the Navigator
- Test obstacle detection on the physical grid with objects placed at intersections

## Key Concepts
- **Ultrasonic rangefinder**: A sensor that measures distance by emitting a sound pulse and timing how long it takes for the echo to return. The XRP rangefinder returns the distance in centimeters as a floating-point number.
- **Distance threshold**: A cutoff value (e.g., 15 cm) used to decide whether something is "close enough" to be an obstacle. If the rangefinder reads less than the threshold, the robot concludes the next intersection is blocked.
- **Reactive navigation**: Navigation that responds to sensor data in real time, rather than following a fixed, pre-planned path. The robot adapts its route as it discovers new information about the environment.
- **Sensor integration**: Connecting hardware sensor data to software algorithms. The rangefinder provides raw distance data; the code converts that into a blocked/not-blocked decision that feeds into Dijkstra.
- **Runtime obstacle discovery**: Finding obstacles while the program is running (during navigation), as opposed to hard-coding them before the program starts. This makes the robot autonomous -- it does not need a human to tell it where obstacles are.
- **Recomputation**: Running Dijkstra again with an updated blocked list after discovering a new obstacle. The new path avoids all previously known obstacles plus the newly discovered one.

## Materials Required
- XRP robot with ultrasonic rangefinder sensor connected
- Physical grid (tape on floor) -- at least 3x3, preferably 4x4
- Objects to serve as obstacles (boxes, books, water bottles, or similar items that the rangefinder can detect)
- Computers with Thonny (or preferred IDE) connected to XRP
- Completed Dijkstra class (`dijkstra.py`) and Navigator class (`navigator.py`)
- Ruler or measuring tape (for calibrating the threshold distance)
- Whiteboard for diagramming the check-detect-update-recompute-drive loop

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 8 min
**For 3-hour sessions:** 10-12 min

1. **Hook: The Robot Gets Eyes**
   - Place an object on the grid at an intersection. Ask: "Right now, can our robot see this obstacle?" (No -- we have to tell it where obstacles are by typing them into the blocked list.)
   - "What if the robot could detect obstacles on its own? Today we give the robot 'eyes' -- the ultrasonic rangefinder."
   - Demonstrate: Hold the rangefinder up to an object and show the distance reading on screen. Move closer, move farther -- the number changes.
   - "The rangefinder sends out a sound pulse -- too high-pitched for us to hear -- and listens for the echo. The time it takes for the echo to return tells it how far away the object is."
   - "If the robot is at an intersection and the rangefinder reads a short distance, something is blocking the next intersection. The robot can add that to its blocked list and ask Dijkstra for a new path."

2. **The Five-Step Loop**
   - Write on the board:
     ```
     At each intersection:
     1. CHECK:     Read the rangefinder
     2. DETECT:    Is the distance below our threshold?
     3. UPDATE:    If yes, add the next intersection to the blocked list
     4. RECOMPUTE: Run Dijkstra with the updated blocked list
     5. DRIVE:     Follow the new path to the next intersection
     ```
   - "This loop repeats at every intersection. The robot gets smarter as it moves -- it builds up knowledge about where obstacles are."

3. **Getting Started with the Rangefinder**
   - Show the import and initialization:
     ```python
     from XRPLib.rangefinder import Rangefinder

     rangefinder = Rangefinder.get_default_rangefinder()
     distance = rangefinder.distance()  # Returns float in cm
     print(f"Distance: {distance} cm")
     ```
   - "That's it -- three lines to read the distance. The sensor does all the complicated math internally."

### Guided Practice (15 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 20 min

1. **Reading the Rangefinder**
   - Have students upload and run a simple rangefinder test:
     ```python
     from XRPLib.rangefinder import Rangefinder
     import time

     rangefinder = Rangefinder.get_default_rangefinder()

     for i in range(10):
         distance = rangefinder.distance()
         print(f"Reading {i + 1}: {distance:.1f} cm")
         time.sleep(1)
     ```
   - Students place their hand (or an object) at various distances and observe the readings.
   - Ask: "Are the readings exactly the same every time?" (No -- there is some noise/variation.)
   - Ask: "What does the sensor read when nothing is in front of it?" (A large number, often 100+ cm.)

2. **Choosing a Threshold**
   - "We need to decide: at what distance do we say 'that's an obstacle'?"
   - Have students measure: Place an object at the next intersection ahead (one grid square away). Read the rangefinder. Typical reading: 10-20 cm depending on grid spacing.
   - Remove the object. Read again. Typical reading: 50+ cm (or whatever the open distance is).
   - "We need a threshold between these two numbers. If the grid spacing gives us ~12 cm when blocked and ~50 cm when clear, a threshold of 15 cm works well."
   - Write the threshold logic:
     ```python
     OBSTACLE_THRESHOLD = 15  # cm -- adjust based on your grid

     distance = rangefinder.distance()
     if distance < OBSTACLE_THRESHOLD:
         print("OBSTACLE DETECTED!")
     else:
         print("Path is clear")
     ```

3. **Determining WHICH Intersection Is Blocked**
   - "The rangefinder tells us something is ahead, but we need to know which intersection that is."
   - Key insight: The robot knows its current position and heading. The blocked intersection is the one directly ahead of the robot.
   - Walk through the logic:
     ```python
     # If the robot is at (1, 1) facing NORTH (toward row 0):
     #   The next intersection ahead is (0, 1)
     # If facing EAST (toward higher columns):
     #   The next intersection ahead is (1, 2)
     # If facing SOUTH (toward higher rows):
     #   The next intersection ahead is (2, 1)
     # If facing WEST (toward lower columns):
     #   The next intersection ahead is (1, 0)
     ```
   - "The Navigator already knows the robot's position and heading. We use those to calculate which node is blocked."

4. **Adding to Blocked List and Recomputing**
   - Walk through the integration:
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
             pathfinder = Dijkstra(rows, cols, blocked_list)
             new_path = pathfinder.compute_path(current_pos, destination)
             print(f"New path: {new_path}")
     ```
   - "Every time we find a new obstacle, we create a fresh Dijkstra with the updated blocked list and get a new path."

### Independent Practice (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

**Exercise 1: Rangefinder Exploration**
- Goal: Get comfortable reading the rangefinder and understanding its behavior
- Steps:
  1. Write a program that reads the rangefinder every second and prints the distance
  2. Test with objects at different distances: 5 cm, 10 cm, 20 cm, 50 cm
  3. Test with different objects: hand, book, water bottle -- do they all register?
  4. Record your readings in a table and determine a good threshold for your grid
- Key question: What happens when the object is at an angle to the sensor? Does it still detect it?

**Exercise 2: Threshold Detection Program**
- Goal: Write a program that announces when an obstacle is detected
- Steps:
  1. Set a threshold based on your Exercise 1 measurements
  2. Write a loop that continuously reads the rangefinder
  3. Print "BLOCKED" when the distance is below the threshold, "CLEAR" when above
  4. Place and remove objects to test that detection is reliable
  5. Count how many times out of 10 the detection is correct (accuracy test)

**Exercise 3: Obstacle Detection with Path Recomputation**
- Goal: Integrate rangefinder detection with Dijkstra path recomputation
- Steps:
  1. Set up a Dijkstra pathfinder for your grid with an empty blocked list
  2. Compute an initial path from (0,0) to (3,3)
  3. Simulate arriving at each intersection: read the rangefinder
  4. If an obstacle is detected, add the blocked intersection to the list
  5. Recompute the path and print the updated route
  6. Test on the physical grid with one object placed at an intersection
- Success criteria: The program detects the obstacle, updates the blocked list, and prints a new path that avoids it

**Exercise 4: Full Navigation with Detection**
- Goal: Run the complete check-detect-update-recompute-drive loop on the robot
- Steps:
  1. Combine the Navigator, Dijkstra, and rangefinder into one program
  2. Place 1-2 obstacles on the grid that the robot's planned path will encounter
  3. Run the robot and observe: does it stop, detect, reroute, and continue?
  4. Print the blocked list at the end -- does it contain the correct intersections?
- Challenge: Place an obstacle that forces the robot to backtrack to a previous intersection

### Assessment

**Formative (during lesson)**:
- Can students read distance values from the rangefinder and explain what they mean?
- Can students choose an appropriate threshold for their grid spacing?
- Can students explain which intersection is blocked based on the robot's position and heading?
- Can students trace through the check-detect-update-recompute-drive loop?
- Can students modify the blocked list at runtime and trigger a path recomputation?

**Summative (worksheet/exit ticket)**:
1. Write the three lines of code needed to import, initialize, and read the XRP rangefinder.
2. The robot is at intersection (2, 1) facing NORTH (toward row 0). The rangefinder reads 8 cm, and the threshold is 15 cm. Which intersection is blocked? What should the program do next?
3. Explain in your own words: What is the difference between hard-coding an obstacle list and detecting obstacles at runtime? Why is runtime detection better?
4. Write the pseudocode for the check-detect-update-recompute-drive loop.
5. The rangefinder sometimes gives slightly different readings for the same distance. How does using a threshold help handle this variability?

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "The rangefinder can see obstacles in all directions" | The rangefinder has a narrow cone of detection and only senses what is directly in front of it. The robot must be facing an obstacle to detect it. |
| "The rangefinder returns exactly the same number every time" | Sensor readings have noise -- small variations between readings. This is why we use a threshold (e.g., < 15 cm) rather than checking for an exact distance. |
| "If the rangefinder reads 0, nothing is there" | A reading of 0 or very small values may indicate the sensor is malfunctioning, the object is too close to detect, or there is an error. Zero does not mean "no obstacle." |
| "We only need to check the rangefinder once at the start" | The robot must check at EVERY intersection, because obstacles can be anywhere on the grid. Checking only once would miss obstacles discovered later in the path. |
| "Detecting an obstacle means the robot should stop" | Detecting an obstacle means the robot should UPDATE its blocked list and RECOMPUTE the path. The robot should continue navigating -- just on a different route. Stopping is giving up; rerouting is solving the problem. |
| "The blocked intersection is the one the robot is currently at" | The blocked intersection is the NEXT one ahead -- the one the rangefinder is pointed at. The robot is at a clear intersection; the obstacle is at the adjacent one in front of it. |

## Differentiation

**For struggling students**:
- Start with just the rangefinder -- spend extra time on Exercise 1, getting comfortable with readings before moving to threshold logic
- Provide the threshold detection code and have students modify only the threshold value
- Use a simplified grid (2x2 or 3x3) with only one obstacle for the integration exercise
- Walk through the "which intersection is blocked" logic with a physical demonstration: stand at an intersection on the grid, face each direction, and point to the intersection ahead
- Provide a nearly-complete program with blanks for students to fill in the rangefinder reading and threshold check

**For advanced students**:
- Implement averaging: read the rangefinder 3-5 times and use the average to reduce noise
- Add a "confidence" system: only mark an intersection as blocked if the rangefinder reads below threshold on 2 out of 3 readings
- Handle the edge case where the obstacle blocks the ONLY path to the destination -- detect this and print "No path available"
- Implement a scan routine: at each intersection, turn the robot to face each direction and check for obstacles in all four directions before deciding which way to go
- Research: How do real autonomous vehicles combine multiple sensors (cameras, LIDAR, radar) for obstacle detection?

## Materials & Code Examples

### Basic Rangefinder Test
```python
# rangefinder_test.py
# Read the rangefinder and display distance values

from XRPLib.rangefinder import Rangefinder
import time

rangefinder = Rangefinder.get_default_rangefinder()

print("Rangefinder Test -- hold objects at various distances")
print("Press Ctrl+C to stop")
print()

while True:
    distance = rangefinder.distance()
    print(f"Distance: {distance:.1f} cm")
    time.sleep(0.5)
```

### Threshold Detection
```python
# threshold_test.py
# Detect obstacles using a distance threshold

from XRPLib.rangefinder import Rangefinder
import time

rangefinder = Rangefinder.get_default_rangefinder()
OBSTACLE_THRESHOLD = 15  # cm -- adjust for your grid spacing

print(f"Obstacle threshold: {OBSTACLE_THRESHOLD} cm")
print("Place and remove objects to test detection")
print()

for i in range(20):
    distance = rangefinder.distance()
    if distance < OBSTACLE_THRESHOLD:
        status = "BLOCKED"
    else:
        status = "CLEAR"
    print(f"Reading {i + 1}: {distance:.1f} cm -- {status}")
    time.sleep(1)
```

### Determining the Blocked Intersection
```python
# obstacle_direction.py
# Figure out which intersection is blocked based on position and heading

# Heading constants
NORTH = 0  # Toward row 0 (up)
EAST = 1   # Toward higher columns (right)
SOUTH = 2  # Toward higher rows (down)
WEST = 3   # Toward lower columns (left)

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


# Example usage:
position = (2, 1)
heading = NORTH
next_node = get_next_intersection(position, heading)
print(f"Robot at {position} facing NORTH")
print(f"Next intersection ahead: {next_node}")  # (1, 1)
```

### Full Navigation with Obstacle Detection
```python
# navigate_with_detection.py
# Complete navigation loop with rangefinder obstacle detection

from dijkstra import Dijkstra
from navigator import Navigator
from XRPLib.rangefinder import Rangefinder

# Setup
rows = 4
cols = 4
blocked_list = []
OBSTACLE_THRESHOLD = 15  # cm -- adjust for your grid

rangefinder = Rangefinder.get_default_rangefinder()

# Initial path
start = (0, 0)
destination = (3, 3)
pathfinder = Dijkstra(rows, cols, blocked_list)
path = pathfinder.compute_path(start, destination)
print(f"Initial path: {path}")

nav = Navigator()
current_pos = start

# Navigate step by step
step = 0
while current_pos != destination:
    step += 1
    print(f"\n--- Step {step} ---")
    print(f"Current position: {current_pos}")

    # CHECK: Read the rangefinder
    distance = rangefinder.distance()
    print(f"Rangefinder: {distance:.1f} cm")

    # DETECT: Is there an obstacle ahead?
    next_intersection = path[1] if len(path) > 1 else None

    if next_intersection and distance < OBSTACLE_THRESHOLD:
        print(f"OBSTACLE DETECTED at {next_intersection}!")

        # UPDATE: Add to blocked list
        if next_intersection not in blocked_list:
            blocked_list.append(next_intersection)
            print(f"Blocked list updated: {blocked_list}")

        # RECOMPUTE: Get new path from current position
        pathfinder = Dijkstra(rows, cols, blocked_list)
        path = pathfinder.compute_path(current_pos, destination)
        print(f"New path: {path}")

        if len(path) < 2:
            print("ERROR: No path to destination!")
            break

    # DRIVE: Move to the next intersection on the path
    next_pos = path[1]
    print(f"Driving to {next_pos}")
    nav.drive_to(current_pos, next_pos)

    # Update position and remaining path
    current_pos = next_pos
    path = path[1:]  # Remove the node we just left

print(f"\nNavigation complete!")
print(f"Final position: {current_pos}")
print(f"Obstacles discovered: {blocked_list}")
print(f"Total steps taken: {step}")
```

### Testing Obstacle Detection Without the Robot
```python
# test_detection_sim.py
# Simulate obstacle detection to test the logic without hardware

from dijkstra import Dijkstra

# Simulated obstacles -- pretend the rangefinder detects these
simulated_obstacles = [(1, 1), (2, 2)]

rows = 4
cols = 4
blocked_list = []
start = (0, 0)
destination = (3, 3)

# Initial path
pathfinder = Dijkstra(rows, cols, blocked_list)
path = pathfinder.compute_path(start, destination)
print(f"Initial path: {path}")
print(f"Initial steps: {len(path) - 1}")

# Simulate navigation
current_pos = start
step = 0

while current_pos != destination:
    step += 1
    next_pos = path[1]

    # Simulate rangefinder: check if next intersection has an obstacle
    if next_pos in simulated_obstacles:
        print(f"\nStep {step}: At {current_pos}, obstacle detected at {next_pos}!")
        if next_pos not in blocked_list:
            blocked_list.append(next_pos)

        # Recompute from current position
        pathfinder = Dijkstra(rows, cols, blocked_list)
        path = pathfinder.compute_path(current_pos, destination)
        print(f"  Rerouted: {path}")
        next_pos = path[1]

    # Move to next position
    print(f"Step {step}: {current_pos} -> {next_pos}")
    current_pos = next_pos
    path = path[1:]

print(f"\nArrived at {destination} in {step} steps")
print(f"Obstacles found: {blocked_list}")
```

## Teaching Notes
- **Calibrate the threshold BEFORE class if possible.** The threshold value depends on the physical grid spacing, the objects used as obstacles, and the rangefinder's characteristics. Test it yourself so you can help students who get unexpected readings. Have a recommended value ready.
- **Expect sensor variability.** Ultrasonic rangefinders are affected by the angle of the object, its surface material (soft materials absorb sound), and ambient noise. If students get inconsistent readings, this is a teaching opportunity about real-world sensor challenges.
- **The "which intersection is blocked" logic is tricky.** Students often confuse the robot's current intersection with the one that is blocked. Use physical demonstrations: stand at an intersection, face a direction, and point to the intersection ahead. That pointed-to intersection is the one the rangefinder is checking.
- **Start with the simulation test before hardware.** Have students run `test_detection_sim.py` first to verify the obstacle-detection logic works in software. Then move to the physical robot. This separates software debugging from hardware debugging.
- **The check-detect-update-recompute-drive loop is the heart of reactive robotics.** Draw it as a cycle on the board and refer back to it throughout the lesson. Every real autonomous system uses some version of this sense-plan-act loop.
- **Let students struggle with integration.** Combining the rangefinder, Dijkstra, and Navigator into one program is the most complex task so far. Give them time, and encourage them to print intermediate values to debug.
- **Place obstacles strategically for demonstrations.** Put the obstacle on the robot's initial planned path so the rerouting is visible and dramatic. An obstacle that is never encountered does not demonstrate anything.

## Connections to Next Lessons
- **Lesson 8** will build on obstacle detection by adding **memory** -- the robot will remember obstacles from previous runs and start with prior knowledge, resulting in fewer surprises and more efficient navigation.
- **Lesson 9** (Capstone) will combine rangefinder detection with obstacle memory into the final autonomous navigation system. Students will demonstrate Run 1 (discovering obstacles) and Run 2 (using prior knowledge).
- The check-detect-update-recompute-drive loop introduced here is the foundation for the capstone project's core behavior. Students who understand this loop well will have an easier time with the capstone.
- The sensor integration skills learned here (reading hardware, applying thresholds, feeding data into algorithms) apply to any robotics or IoT project beyond this course.
