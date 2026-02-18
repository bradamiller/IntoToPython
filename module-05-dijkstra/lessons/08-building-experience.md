# Lesson 8: Building Experience (Updating Obstacles Over Time)

## Overview
Students extend the obstacle detection system from Lesson 7 by adding **memory** -- the ability for the robot to remember obstacles discovered during one run and use that knowledge to navigate more efficiently on subsequent runs. In Run 1, the robot starts with an empty blocked list and discovers obstacles the hard way: it drives toward them, detects them with the rangefinder, reroutes, and eventually reaches the destination. In Run 2, the robot starts with the obstacles it discovered during Run 1 already in its blocked list, so it plans a smarter initial path and encounters fewer surprises. Students measure the improvement by comparing total steps taken and number of reroutes between runs. This lesson makes the GPS/Waze analogy concrete: just as Waze learns from drivers who report accidents and construction, the robot learns from its own experience. Advanced students implement persistent storage by writing the blocked list to a file and reading it back, so the robot's knowledge survives between program restarts.

This lesson is the bridge between single-run obstacle detection (Lesson 7) and the capstone project (Lesson 9). It introduces a key idea in robotics and artificial intelligence: **systems that improve with experience**. The robot is not "smarter" in the traditional sense -- it uses the same Dijkstra algorithm every time -- but it has better data on subsequent runs, which leads to better paths. Students see that intelligence is often about having good information, not just good algorithms.

## Learning Objectives
By the end of this lesson, students will be able to:
- Explain why remembering obstacles improves navigation performance
- Implement a system where discovered obstacles persist between runs (within a single program execution)
- Compare Run 1 and Run 2 performance using step count and reroute count as metrics
- Pre-load a blocked list from a previous run's discoveries
- Explain the GPS/Waze analogy: how crowd-sourced obstacle data improves routing for everyone
- (Advanced) Write a blocked list to a file and read it back to persist data between program restarts
- Describe the general principle: systems improve when they accumulate and reuse experience

## Key Concepts
- **Obstacle memory**: Storing the list of blocked intersections discovered during navigation so it can be reused on future runs. The blocked list grows as the robot explores and never shrinks (an obstacle stays in memory until manually removed).
- **Run**: A single navigation attempt from start to destination. Run 1 starts with no prior knowledge. Run 2 starts with knowledge from Run 1. Each run may discover additional obstacles.
- **Experience-based improvement**: The principle that performance improves when past experience informs future decisions. The robot takes fewer total steps on Run 2 because it already knows where some obstacles are.
- **Persistence**: Keeping data alive beyond a single execution of the program. Within one program, a list variable persists between function calls. To persist between separate program runs, data must be saved to a file.
- **Pre-loading**: Starting a program with data from a previous session rather than starting from scratch. Pre-loading the blocked list means the robot begins with prior knowledge.
- **Metrics**: Measurable quantities used to evaluate performance. For navigation, key metrics are total steps taken, number of reroutes, and number of obstacles encountered unexpectedly.

## Materials Required
- XRP robot with ultrasonic rangefinder sensor
- Physical grid (tape on floor) -- at least 3x3, preferably 4x4
- Objects to serve as obstacles (same as Lesson 7)
- Computers with Thonny (or preferred IDE) connected to XRP
- Completed code from Lesson 7 (navigation with obstacle detection)
- Stopwatch or timer (for comparing run durations)
- Data recording worksheet (for tracking metrics across runs)
- Whiteboard for diagramming the Run 1 / Run 2 comparison

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 8 min
**For 3-hour sessions:** 10-12 min

1. **Hook: The GPS/Waze Analogy**
   - Ask: "Has anyone used Waze or Google Maps when there was traffic or a road closure? How did the app know about the problem?"
   - Discussion: Waze learns from its users. When a driver hits traffic, the app detects the slowdown and shares it with other drivers. The next person to drive that route gets rerouted BEFORE they hit the problem.
   - "Our robot is going to do the same thing -- but with itself. On Run 1, it discovers obstacles. On Run 2, it already knows where those obstacles are and plans a better route from the start."
   - Draw on the board:
     ```
     Run 1: Empty blocked list -> Discover obstacles -> Reach destination
                                  (many reroutes, many steps)

     Run 2: Pre-loaded blocked list -> Fewer surprises -> Reach destination
                                       (fewer reroutes, fewer steps)
     ```

2. **Why Memory Matters**
   - "In Lesson 7, every time we ran the program, the robot started with an empty blocked list. It had to rediscover every obstacle from scratch. That's like forgetting your commute every morning and being surprised by the same construction zone."
   - "Today we fix that. The robot remembers what it learned."
   - Key insight: The Dijkstra algorithm does not change. The Navigator does not change. Only the INPUT changes -- the blocked list starts with more information. **Better data leads to better performance.**

3. **Measuring Improvement**
   - "How do we know Run 2 is better than Run 1? We measure."
   - Metrics to track:
     - **Total steps**: How many intersections did the robot visit?
     - **Reroutes**: How many times did the robot detect an obstacle and recompute?
     - **Unexpected obstacles**: How many obstacles did the robot not know about in advance?
   - "On Run 2, we expect fewer reroutes and potentially fewer total steps."

### Guided Practice (15 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 20 min

1. **Run 1: Discover and Remember**
   - Walk through the code structure together:
     ```python
     from dijkstra import Dijkstra
     from XRPLib.rangefinder import Rangefinder

     # Obstacle memory -- starts empty for Run 1
     blocked_list = []

     # Navigation with detection (from Lesson 7)
     # ... the check-detect-update-recompute-drive loop ...

     # After reaching the destination:
     print("Run 1 complete!")
     print(f"Obstacles discovered: {blocked_list}")
     ```
   - Run the robot on the physical grid with 2-3 obstacles placed at intersections.
   - Record the results on the board:
     - Obstacles discovered
     - Total steps taken
     - Number of reroutes

2. **Run 2: Start with Prior Knowledge**
   - "Now we do Run 2. Instead of starting with an empty blocked list, we start with what we learned in Run 1."
   - Two approaches:
     - **Simple (same program execution)**: Call the navigation function again without resetting the blocked list
     - **Manual pre-load**: Copy the obstacles from Run 1's output into the initial blocked list
   - Walk through the code:
     ```python
     # Run 2: Start with obstacles from Run 1
     # blocked_list already contains obstacles from Run 1!
     print(f"\nStarting Run 2 with prior knowledge: {blocked_list}")

     # Reset position to start
     current_pos = start

     # Compute initial path WITH known obstacles
     pathfinder = Dijkstra(rows, cols, blocked_list)
     path = pathfinder.compute_path(current_pos, destination)
     print(f"Initial path (with prior knowledge): {path}")

     # Navigate again with the same check-detect loop
     # ... the check-detect-update-recompute-drive loop ...
     ```
   - Run the robot again (same obstacles in the same positions).
   - Record Run 2 results and compare to Run 1.

3. **Comparing Run 1 and Run 2**
   - Write the comparison on the board:
     ```
                        Run 1    Run 2
     Starting blocked:  0        (from Run 1)
     Reroutes:          ?        ?
     Total steps:       ?        ?
     New obstacles:     ?        ?
     ```
   - Ask: "Why did Run 2 take fewer reroutes?" (Because the robot already knew about obstacles and planned around them from the start.)
   - Ask: "Could Run 2 have MORE steps than Run 1?" (Usually no, but it depends on the grid -- the initial path in Run 2 accounts for known obstacles, which Dijkstra optimizes.)
   - Ask: "Could Run 2 discover NEW obstacles?" (Yes, if there are obstacles it did not encounter in Run 1 because it took a different route.)

4. **What If We Do Run 3?**
   - "If Run 2 discovered new obstacles, Run 3 would start with even more knowledge."
   - "Eventually, the robot knows about ALL obstacles and its path is optimal from the start. No more reroutes needed."
   - This is the concept of **convergence** -- the system's knowledge converges toward a complete map of the environment.

### Independent Practice (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

**Exercise 1: Two-Run Comparison**
- Goal: Run the navigation program twice and measure the improvement
- Steps:
  1. Set up the grid with 2-3 obstacles
  2. Run the navigation program (Run 1) and record: total steps, reroutes, obstacles found
  3. Run it again WITHOUT resetting the blocked list (Run 2) and record the same metrics
  4. Calculate the improvement: how many fewer reroutes? How many fewer steps?
- Fill in the comparison table:
  ```
  Metric           Run 1    Run 2    Improvement
  Total steps:     ___      ___      ___
  Reroutes:        ___      ___      ___
  New obstacles:   ___      ___      ___
  ```

**Exercise 2: Pre-Loading Obstacles**
- Goal: Manually pre-load a blocked list and observe the difference
- Steps:
  1. Run the program once with an empty blocked list. Note the obstacles discovered.
  2. Modify the program to start with those obstacles already in the blocked list:
     ```python
     # Pre-loaded from previous run
     blocked_list = [(1, 0), (2, 2)]  # Use YOUR discovered obstacles
     ```
  3. Run the program again and compare the initial path to Run 1's initial path
  4. Count total steps and reroutes
- Key question: Is the initial path in the pre-loaded run different from Run 1's initial path? Why?

**Exercise 3: Multiple Destinations with Memory**
- Goal: Navigate to several destinations in sequence, building up obstacle knowledge
- Steps:
  1. Define 3 destinations: e.g., (0, 3), (3, 3), (3, 0)
  2. Navigate to each destination in order, keeping the same blocked list across all three
  3. Record how many obstacles are known at the start of each leg
  4. Observe: does navigation get smoother as the robot visits more of the grid?
- The blocked list should grow as the robot covers more territory

**Exercise 4: Challenge -- Writing and Reading the Blocked List to a File**
- Goal: Persist obstacle data between separate program runs
- Steps:
  1. After Run 1, write the blocked list to a file:
     ```python
     with open("obstacles.txt", "w") as f:
         for node in blocked_list:
             f.write(f"{node[0]},{node[1]}\n")
     ```
  2. At the start of Run 2 (a completely separate program execution), read the file:
     ```python
     blocked_list = []
     try:
         with open("obstacles.txt", "r") as f:
             for line in f:
                 row, col = line.strip().split(",")
                 blocked_list.append((int(row), int(col)))
     except FileNotFoundError:
         blocked_list = []  # No prior data -- start fresh
     ```
  3. Run the program, navigate, discover new obstacles, and append them to the file
  4. Run a third time and verify the file contains obstacles from BOTH previous runs

### Assessment

**Formative (during lesson)**:
- Can students explain why Run 2 performs better than Run 1?
- Can students identify which metrics improve and why?
- Can students modify the program to pre-load a blocked list?
- Can students articulate the GPS/Waze analogy in their own words?
- Can students predict what Run 3 would look like if Run 2 discovered new obstacles?

**Summative (worksheet/exit ticket)**:
1. Explain in your own words: Why does the robot navigate better on Run 2 than on Run 1?
2. The robot discovers obstacles at (1, 0) and (2, 2) during Run 1. Write the code that starts Run 2 with these obstacles already in the blocked list.
3. On Run 1, the robot took 12 steps and rerouted 3 times. On Run 2, it took 8 steps and rerouted 0 times. Explain why these numbers changed.
4. How is the robot's obstacle memory similar to how Waze or Google Maps learns about traffic?
5. (Challenge) Write the code to save a blocked list to a file called `obstacles.txt`, with one obstacle per line in the format `row,col`.

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "The robot gets smarter on Run 2 because it learns a better algorithm" | The algorithm (Dijkstra) is identical on both runs. What changes is the DATA -- the blocked list. Better data in, better paths out. The "intelligence" is in the information, not the algorithm. |
| "Run 2 always takes fewer steps than Run 1" | Run 2 usually takes fewer steps because it avoids known obstacles from the start. However, if Run 1 happened to take a path that avoided obstacles by luck, or if Run 2 discovers new obstacles, the difference may be small. |
| "The robot remembers obstacles forever automatically" | Within a single program execution, the list variable persists. But if you stop and restart the program, the list is gone -- Python variables do not survive between runs. You need file I/O to persist data. |
| "Once the robot knows all obstacles, it never needs the rangefinder" | The rangefinder is still useful because new obstacles could appear (someone moves an object). In a real-world system, the environment can change, so sensors are always needed. |
| "Run 2 will never encounter any obstacles" | Run 2 will not encounter obstacles it already knows about, but it MAY discover NEW obstacles that were not on Run 1's path. The robot only discovers obstacles it drives toward. |
| "More runs always means better performance" | Performance improves until the robot has discovered all relevant obstacles. After that, additional runs do not improve further because there is nothing new to learn. |

## Differentiation

**For struggling students**:
- Focus on the conceptual comparison first: do Run 1 and Run 2 on paper (trace paths on a grid drawing) before coding
- Provide the two-run program as a complete file and have students run it, observe the results, and fill in the comparison table
- Use a simple 3x3 grid with only one obstacle to minimize complexity
- Walk through the pre-loading code line by line, explaining what each line does
- Pair with a partner: one student runs the robot, the other records the metrics

**For advanced students**:
- Implement the file persistence challenge (Exercise 4) and demonstrate that data survives between program restarts
- Add a "confidence" system: if the robot passes an intersection where it previously detected an obstacle and the obstacle is now gone (rangefinder reads far), remove it from the blocked list
- Calculate the theoretical minimum number of steps for a given obstacle configuration and compare to actual performance on each run
- Implement a "heat map" that tracks how many times each intersection has been visited across all runs
- Research: How do real autonomous systems (self-driving cars, delivery drones) handle changing environments? How do they share obstacle data with each other?

## Materials & Code Examples

### Two-Run Navigation with Memory
```python
# two_run_navigation.py
# Demonstrates how obstacle memory improves performance across runs

from dijkstra import Dijkstra

# Simulated obstacles (replace with rangefinder for physical robot)
ACTUAL_OBSTACLES = [(1, 0), (2, 2), (1, 3)]

# Grid setup
rows = 4
cols = 4
start = (0, 0)
destination = (3, 3)
OBSTACLE_THRESHOLD = 15  # cm

def simulate_rangefinder(current_pos, next_pos, actual_obstacles):
    """Simulate obstacle detection (replace with real rangefinder on robot)."""
    if next_pos in actual_obstacles:
        return 8.0  # Simulated close reading
    else:
        return 50.0  # Simulated far reading

def navigate_one_run(run_number, blocked_list, start, destination):
    """Navigate from start to destination, detecting obstacles along the way."""
    print(f"\n{'=' * 50}")
    print(f"RUN {run_number}")
    print(f"Starting blocked list: {blocked_list}")
    print(f"{'=' * 50}")

    # Compute initial path
    pathfinder = Dijkstra(rows, cols, blocked_list)
    path = pathfinder.compute_path(start, destination)
    print(f"Initial path: {path}")
    print(f"Initial path length: {len(path) - 1} steps")

    current_pos = start
    total_steps = 0
    reroutes = 0
    new_obstacles = 0

    while current_pos != destination:
        next_pos = path[1]

        # Check for obstacle
        distance = simulate_rangefinder(current_pos, next_pos, ACTUAL_OBSTACLES)

        if distance < OBSTACLE_THRESHOLD:
            if next_pos not in blocked_list:
                blocked_list.append(next_pos)
                new_obstacles += 1
                print(f"  NEW obstacle at {next_pos}!")

            # Recompute path
            reroutes += 1
            pathfinder = Dijkstra(rows, cols, blocked_list)
            path = pathfinder.compute_path(current_pos, destination)
            print(f"  Rerouted: {path}")
            next_pos = path[1]

        # Drive to next intersection
        current_pos = next_pos
        path = path[1:]
        total_steps += 1

    print(f"\nRun {run_number} Results:")
    print(f"  Total steps:       {total_steps}")
    print(f"  Reroutes:          {reroutes}")
    print(f"  New obstacles:     {new_obstacles}")
    print(f"  Known obstacles:   {blocked_list}")

    return total_steps, reroutes, new_obstacles


# ==========================================
# RUN 1: Start with no knowledge
# ==========================================
blocked_list = []
steps1, reroutes1, new1 = navigate_one_run(1, blocked_list, start, destination)

# ==========================================
# RUN 2: Start with knowledge from Run 1
# (blocked_list still contains Run 1's discoveries!)
# ==========================================
steps2, reroutes2, new2 = navigate_one_run(2, blocked_list, start, destination)

# ==========================================
# COMPARISON
# ==========================================
print(f"\n{'=' * 50}")
print("COMPARISON")
print(f"{'=' * 50}")
print(f"{'Metric':<25} {'Run 1':>8} {'Run 2':>8} {'Change':>8}")
print(f"{'-' * 49}")
print(f"{'Total steps':<25} {steps1:>8} {steps2:>8} {steps2 - steps1:>+8}")
print(f"{'Reroutes':<25} {reroutes1:>8} {reroutes2:>8} {reroutes2 - reroutes1:>+8}")
print(f"{'New obstacles found':<25} {new1:>8} {new2:>8} {new2 - new1:>+8}")
```

### Saving Obstacles to a File
```python
# save_obstacles.py
# Write the blocked list to a file so it persists between program runs

def save_blocked_list(blocked_list, filename="obstacles.txt"):
    """Save the blocked list to a text file."""
    with open(filename, "w") as f:
        for node in blocked_list:
            f.write(f"{node[0]},{node[1]}\n")
    print(f"Saved {len(blocked_list)} obstacles to {filename}")


def load_blocked_list(filename="obstacles.txt"):
    """Load the blocked list from a text file. Returns empty list if file not found."""
    blocked_list = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line:  # Skip empty lines
                    row, col = line.split(",")
                    blocked_list.append((int(row), int(col)))
        print(f"Loaded {len(blocked_list)} obstacles from {filename}")
    except FileNotFoundError:
        print(f"No obstacle file found. Starting with empty list.")
    return blocked_list


# Example usage:
# At the START of the program:
blocked_list = load_blocked_list()
print(f"Starting with: {blocked_list}")

# ... navigate, discover obstacles, add to blocked_list ...

# At the END of the program:
# blocked_list might now be [(1, 0), (2, 2), (1, 3)]
save_blocked_list(blocked_list)
```

### Reading the File Back
```python
# load_and_navigate.py
# Start a navigation run with previously saved obstacle data

from dijkstra import Dijkstra

def load_blocked_list(filename="obstacles.txt"):
    """Load the blocked list from a text file."""
    blocked_list = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    row, col = line.split(",")
                    blocked_list.append((int(row), int(col)))
        print(f"Loaded {len(blocked_list)} obstacles from {filename}")
    except FileNotFoundError:
        print("No saved obstacles found. Starting fresh.")
    return blocked_list

# Load prior knowledge
blocked_list = load_blocked_list()
print(f"Prior obstacles: {blocked_list}")

# Plan initial path using prior knowledge
rows = 4
cols = 4
pathfinder = Dijkstra(rows, cols, blocked_list)
path = pathfinder.compute_path((0, 0), (3, 3))
print(f"Initial path with prior knowledge: {path}")
print(f"Path length: {len(path) - 1} steps")

# Compare to path without prior knowledge
pathfinder_fresh = Dijkstra(rows, cols, [])
path_fresh = pathfinder_fresh.compute_path((0, 0), (3, 3))
print(f"\nPath without prior knowledge: {path_fresh}")
print(f"Path length: {len(path_fresh) - 1} steps")

if len(path) > len(path_fresh):
    print(f"\nPrior knowledge adds {len(path) - len(path_fresh)} steps to avoid known obstacles.")
    print("But this is BETTER because the robot won't hit those obstacles and have to reroute!")
```

### Multi-Destination Navigation with Growing Memory
```python
# multi_destination.py
# Navigate to multiple destinations, building obstacle knowledge along the way

from dijkstra import Dijkstra

ACTUAL_OBSTACLES = [(1, 0), (2, 2), (0, 2)]

rows = 4
cols = 4
blocked_list = []
OBSTACLE_THRESHOLD = 15

def simulate_rangefinder(next_pos):
    """Simulate rangefinder (replace with real sensor on robot)."""
    if next_pos in ACTUAL_OBSTACLES:
        return 8.0
    return 50.0

def navigate_to(start, destination, blocked_list):
    """Navigate from start to destination, returning the final position."""
    pathfinder = Dijkstra(rows, cols, blocked_list)
    path = pathfinder.compute_path(start, destination)
    current_pos = start
    steps = 0
    reroutes = 0

    while current_pos != destination:
        next_pos = path[1]
        distance = simulate_rangefinder(next_pos)

        if distance < OBSTACLE_THRESHOLD:
            if next_pos not in blocked_list:
                blocked_list.append(next_pos)
                print(f"    Discovered obstacle at {next_pos}")
            reroutes += 1
            pathfinder = Dijkstra(rows, cols, blocked_list)
            path = pathfinder.compute_path(current_pos, destination)
            next_pos = path[1]

        current_pos = next_pos
        path = path[1:]
        steps += 1

    return steps, reroutes

# Navigate to multiple destinations
destinations = [(0, 3), (3, 3), (3, 0), (0, 0)]
current = (0, 0)

for i, dest in enumerate(destinations):
    print(f"\nLeg {i + 1}: {current} -> {dest}")
    print(f"  Known obstacles at start: {blocked_list}")
    steps, reroutes = navigate_to(current, dest, blocked_list)
    print(f"  Steps: {steps}, Reroutes: {reroutes}")
    current = dest

print(f"\nFinal obstacle list: {blocked_list}")
print(f"Total obstacles discovered: {len(blocked_list)}")
```

## Teaching Notes
- **The GPS/Waze analogy is extremely effective.** Students immediately understand why remembering obstacles is useful when you frame it in terms of technology they use every day. Extend the analogy: "What if Waze forgot all traffic reports every time you closed the app? You'd hit the same traffic jam every day."
- **Run 1 and Run 2 should be dramatic.** Set up the grid so Run 1 has at least 2-3 reroutes. The contrast with Run 2 (which may have zero reroutes) is the "aha" moment. Display the comparison table prominently.
- **Use the simulation first, hardware second.** The `two_run_navigation.py` simulation lets students focus on the concept of memory and improvement without hardware complications. Once they understand the idea, move to the physical robot.
- **The file I/O challenge is optional but valuable.** Writing to and reading from files is a real-world programming skill that many students have not encountered. If time permits, the challenge exercise is well worth doing. If not, the in-memory approach (keeping the list between runs in the same program) teaches the same concept.
- **Discuss limitations honestly.** What if obstacles move? What if the robot's sensor was wrong? Real systems need ways to remove outdated information, not just add new data. This is a good discussion topic for advanced students.
- **Connect to AI and machine learning.** The robot is "learning" in a very simple sense: it accumulates data and uses it to make better decisions. This is the same basic principle behind machine learning, just much simpler. Students interested in AI will find this connection motivating.
- **Metrics matter.** Have students record numbers -- total steps, reroutes, new obstacles -- for every run. The quantitative comparison is much more convincing than a qualitative "it seemed faster."

## Connections to Next Lessons
- **Lesson 9** (Capstone) requires students to demonstrate improvement between Run 1 and Run 2 as a grading criterion. The obstacle memory system built in this lesson is directly assessed in the capstone.
- The capstone project combines ALL components: Dijkstra pathfinding (Lessons 3-5), shared interface and swap (Lesson 6), rangefinder detection (Lesson 7), and obstacle memory (this lesson) into one integrated system.
- The file I/O skills from the challenge exercise apply to many future programming tasks: saving game state, logging data, reading configuration files, and more.
- The concept of systems that improve with experience is foundational to machine learning and artificial intelligence -- fields students may explore in future courses.
