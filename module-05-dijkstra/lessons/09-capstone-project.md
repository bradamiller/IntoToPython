# Lesson 9: Capstone Project (Full System Integration)

## Overview
Students bring together every component they have built throughout Module 5 into a single, fully integrated autonomous navigation program. The capstone requires the robot to visit four or more destinations on the grid using Dijkstra's algorithm for pathfinding, the ultrasonic rangefinder for real-time obstacle detection, dynamic path recomputation when obstacles are discovered, and file-based persistence so the robot remembers obstacles between program runs. In Run 1 (the "discovery run"), the robot starts with no prior knowledge, encounters obstacles, reroutes around them, and saves what it learned to a file. In Run 2 (the "experience run"), the robot loads the saved obstacle data and plans smarter initial paths, resulting in fewer reroutes and fewer total steps. Students demonstrate their understanding by presenting both runs and explaining the performance improvement with concrete metrics. This project is the culmination of eight lessons of incremental skill-building: from understanding grids as graphs, to dictionaries, to Dijkstra's algorithm, to classes, to testing, to sensor integration, to experience-based learning.

The capstone is intentionally structured so that students who completed each lesson already have all the building blocks. The challenge is not writing new algorithms but rather **integrating** existing components into a cohesive system -- a skill that mirrors real-world software engineering. Students must think about program flow (what happens first, what depends on what), data flow (how the blocked list moves between functions), and error handling (what if there is no path to a destination). The grading rubric rewards each major component separately, so students who struggle with one piece (e.g., file I/O) can still earn significant credit for the other components they have working. Extensions are provided for students who finish early, including live mid-segment obstacle detection, destination optimization, obstacle expiration, and visual grid logging.

## Learning Objectives
By the end of this lesson, students will be able to:
- Integrate Dijkstra pathfinding, Navigator, rangefinder obstacle detection, and obstacle memory into a single working program
- Design a program that visits four or more destinations while detecting and avoiding obstacles
- Demonstrate learning by showing improved performance between Run 1 and Run 2
- Use file I/O to save and load obstacle data between program runs
- Present and explain a working autonomous navigation system, citing step counts and reroute counts as evidence of improvement
- Organize code into functions and classes with clear comments and readable structure
- Debug integration issues where individually working components fail to work together

## Key Concepts
- **System integration**: Combining multiple independently developed components (Dijkstra class, Navigator, rangefinder, file I/O) into a single program that works as a unified whole. Integration is often harder than building individual pieces because components must communicate correctly through shared data structures like the blocked list.
- **Navigation loop**: The core control structure of the capstone program: for each destination, repeatedly compute a path, walk along the path checking for obstacles at each intersection, and if an obstacle is found, update the blocked list and recompute. The outer loop iterates over destinations; the inner loop handles obstacle discovery and rerouting for a single destination.
- **Discovery run (Run 1)**: The first execution of the program, starting with an empty blocked list (or an empty obstacles file). The robot must discover all obstacles through direct rangefinder detection, leading to multiple reroutes and a higher step count. This run establishes the baseline performance.
- **Experience run (Run 2)**: The second execution of the program, starting with obstacles loaded from the file saved during Run 1. The robot plans initial paths that already avoid known obstacles, resulting in fewer (or zero) reroutes and a lower step count. The difference between Run 1 and Run 2 is the measurable evidence of learning.
- **Obstacle persistence**: Saving the blocked list to a text file at the end of a run and loading it at the beginning of the next run. This allows the robot's knowledge to survive between separate program executions, not just between function calls within a single execution.
- **Path recomputation**: When an obstacle is detected during path execution, the robot stops, adds the obstacle to the blocked list, creates a new Dijkstra instance with the updated blocked list, and computes a fresh path from its current position to the destination. This process may happen multiple times per destination.
- **Grading rubric**: A structured scoring guide that assigns points to each major component of the project. The rubric ensures students know exactly what is expected and allows partial credit for partially working systems.

## Materials Required
- XRP robot with ultrasonic rangefinder sensor
- Physical grid (tape on floor) -- at least 4x4
- Objects to serve as obstacles (boxes, books, or similar sturdy items)
- Computers with Thonny (or preferred IDE) connected to XRP
- Completed code from Lessons 4-8 (Dijkstra class, Navigator, obstacle detection, file I/O)
- Printed grading rubric (one per student or team)
- Stopwatch or timer (for measuring run durations)
- Data recording worksheet (for tracking metrics: steps, reroutes, obstacles discovered)
- Whiteboard or projector for displaying project requirements and demo format

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 5 min
**For 3-hour sessions:** 10 min

1. **Hook: This Is Your Graduation Project!**
   - Display the journey table on the board:
     ```
     Lesson 1:  Understanding the grid as a graph
     Lesson 2:  Dictionaries to represent the graph in Python
     Lesson 3:  Dijkstra's algorithm — the concept
     Lessons 4-5: The Dijkstra class with compute_path
     Lesson 6:  Testing and swapping Dijkstra into Navigator
     Lesson 7:  Obstacle detection with the rangefinder
     Lesson 8:  Building experience — remembering obstacles across runs
     Lesson 9:  TODAY — put it ALL together
     ```
   - "You have built every piece of the puzzle. Today you assemble the puzzle into one working program. One program. Full autonomy. A robot that navigates, discovers, and learns."
   - "This is not about writing new code from scratch. It is about INTEGRATING code you have already written and tested. That is what real software engineers do every day."

2. **Project Requirements Overview**
   - Walk through the eight requirements:
     1. Visit 4 or more destinations on the grid in sequence
     2. Use Dijkstra's algorithm to compute paths
     3. Detect obstacles using the ultrasonic rangefinder at each intersection
     4. Update the blocked list when a new obstacle is discovered
     5. Recompute paths after discovering an obstacle
     6. Save obstacles to a file at the end of each run
     7. Load obstacles from the file at the start of each run
     8. Demonstrate learning: Run 2 performs better than Run 1
   - "If you completed Lessons 4 through 8, you already have code for every single one of these requirements. Today is about connecting them."

3. **Demo Format Preview**
   - "You will demonstrate your project with two runs:"
     - Run 1: Delete obstacles.txt, place obstacles on the grid, run the program. The robot discovers obstacles, reroutes, and saves what it learned.
     - Run 2: Keep the same obstacles, run the program again. The robot loads prior knowledge and navigates more efficiently.
   - "The difference in step counts between Run 1 and Run 2 IS the learning. That is what you are demonstrating."

### Guided Practice (15 minutes)
**For 50-min classes:** 10 min
**For 3-hour sessions:** 15-20 min

1. **Program Structure Walkthrough**
   - Display the overall program structure on the board or projector:
     ```
     Step 1: Load obstacles from file
     Step 2: Define destinations
     Step 3: Main navigation loop
       For each destination:
         While not arrived:
           Compute path with Dijkstra
           Walk along path, checking rangefinder at each intersection
           If obstacle found: update blocked list, recompute
           If no obstacle: drive to next intersection
     Step 4: Save obstacles to file
     Step 5: Print results (total steps, obstacles found)
     ```
   - "This is the skeleton. Let's walk through each step and connect it to code you have already written."

2. **Step 1: File I/O Functions**
   - Review the save and load functions from Lesson 8:
     ```python
     def save_obstacles(blocked, filename="obstacles.txt"):
         f = open(filename, "w")
         for node in blocked:
             f.write(str(node[0]) + "," + str(node[1]) + "\n")
         f.close()

     def load_obstacles(filename="obstacles.txt"):
         blocked = []
         try:
             f = open(filename, "r")
             for line in f:
                 parts = line.strip().split(",")
                 blocked.append((int(parts[0]), int(parts[1])))
             f.close()
         except:
             pass
         return blocked
     ```
   - "These go at the top of your program. `load_obstacles` is called first. `save_obstacles` is called last."

3. **Step 2: Hardware Setup and Destinations**
   - Review the XRP imports and setup:
     ```python
     from XRPLib.rangefinder import Rangefinder
     from XRPLib.differential_drive import DifferentialDrive
     from XRPLib.board import Board

     rangefinder = Rangefinder.get_default_rangefinder()
     drivetrain = DifferentialDrive.get_default_differential_drive()
     board = Board.get_default_board()

     destinations = [(1, 3), (3, 3), (3, 0), (0, 2)]
     current = (0, 0)
     ```
   - "Choose four destinations that cover different areas of the grid. The more spread out, the more interesting the demo."

4. **Step 3: The Navigation Loop**
   - Walk through the main loop logic step by step:
     ```python
     for dest in destinations:
         arrived = False
         while not arrived:
             pathfinder = Dijkstra(current, blocked)
             path = pathfinder.compute_path(dest)

             if len(path) == 0:
                 print("No path to " + str(dest) + "! Skipping.")
                 break

             rerouted = False
             for i in range(len(path) - 1):
                 distance = rangefinder.distance()
                 if distance < THRESHOLD:
                     blocked.append(path[i + 1])
                     rerouted = True
                     break
                 # Drive to next intersection
                 current = path[i + 1]
                 step_count = step_count + 1

             if not rerouted:
                 arrived = True
     ```
   - Emphasize the nested loop structure: outer `for` loop over destinations, middle `while` loop for rerouting, inner `for` loop walking along a single computed path.

5. **Step 4: Connecting the Pieces**
   - "The key insight is data flow. The `blocked` list is the thread that connects everything:"
     - `load_obstacles` produces the initial `blocked` list
     - `Dijkstra.__init__` receives `blocked` and uses it to build the graph
     - Obstacle detection appends to `blocked`
     - `save_obstacles` writes the final `blocked` list to the file
   - "If the blocked list does not flow correctly between these components, the system breaks."

### Independent Practice (20 minutes)
**For 50-min classes:** 20 min (may extend across multiple class periods)
**For 3-hour sessions:** 40-50 min

**Exercise 1: Assemble the Capstone Program**
- Goal: Build the complete capstone program from components you already have
- Steps:
  1. Start with the capstone starter file
  2. Implement the `save_obstacles` and `load_obstacles` functions
  3. Complete the main navigation loop with obstacle detection
  4. Add step counting and result reporting
- Test first WITHOUT physical obstacles to verify path computation is correct

**Exercise 2: Test with Simulated Obstacles**
- Goal: Verify the program logic before using the physical robot
- Steps:
  1. Comment out the rangefinder code
  2. Hard-code a list of "actual obstacles" for simulation
  3. Write a simulate function that returns a short distance if the next position is an actual obstacle
  4. Run the full program and verify that paths are computed correctly, obstacles are detected, and the blocked list grows
  5. Verify that `obstacles.txt` is created and contains the correct data

**Exercise 3: Run on the Physical Grid**
- Goal: Execute the full capstone on the XRP robot
- Steps:
  1. Set up the 4x4 grid with tape
  2. Place 2-3 obstacles at intersections
  3. Delete `obstacles.txt` (start fresh)
  4. Run 1: Execute the program and record total steps, reroutes, and obstacles discovered
  5. Run 2: Execute the program again (same obstacles, same positions) and record the same metrics
  6. Compare Run 1 and Run 2 results

**Exercise 4: Prepare Your Demo**
- Goal: Practice the two-run demonstration
- Steps:
  1. Rehearse explaining what the program does before running it
  2. Know where to point out obstacle detection happening in real time
  3. Prepare to show `obstacles.txt` between runs
  4. Have your comparison numbers ready: "Run 1 took X steps with Y reroutes. Run 2 took A steps with B reroutes."

### Assessment

**Formative (during lesson)**:
- Can students explain the overall program structure (load, navigate, save)?
- Can students trace data flow: how does the blocked list move through the system?
- Can students identify which component is responsible for each requirement?
- Can students debug integration issues (e.g., blocked list not being passed correctly)?
- Can students explain why Run 2 outperforms Run 1?

**Summative (project rubric -- 60 points)**:

| Category | Points | Criteria |
|---|---|---|
| **Dijkstra Pathfinding** | 10 | Uses Dijkstra class to compute paths; paths are correct and shortest |
| **Navigator Integration** | 10 | Robot physically drives the computed paths on the grid |
| **Obstacle Detection** | 10 | Rangefinder detects obstacles at intersections; blocked list updates correctly |
| **Path Recomputation** | 10 | Robot recomputes path after discovering an obstacle; new path avoids the obstacle |
| **Experience (File I/O)** | 10 | Obstacles saved to file after Run 1; loaded from file at start of Run 2 |
| **Demonstration** | 5 | Run 1 discovers obstacles and reroutes; Run 2 avoids known obstacles from the start |
| **Code Quality** | 5 | Code is readable, uses functions/classes, has meaningful comments |

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "I need to write all the code from scratch for the capstone" | The capstone is an INTEGRATION project. You already have the Dijkstra class (Lessons 4-5), obstacle detection logic (Lesson 7), and file I/O functions (Lesson 8). The work is connecting these pieces together with a main navigation loop. |
| "The robot should detect obstacles while driving between intersections" | The base requirement is to check for obstacles at each intersection before moving to the next one. Mid-segment detection is an extension for extra credit, not a requirement. |
| "If Run 2 has ANY reroutes, my project is broken" | Run 2 may still encounter obstacles if the robot takes a different route than Run 1 and discovers previously unknown obstacles. What matters is that Run 2 has FEWER reroutes and/or fewer steps because it started with prior knowledge. |
| "I need to create a Navigator class with drive methods" | For the simulation/testing version, you can print the path and steps instead of physically driving. For the physical robot version, use `DifferentialDrive` methods (`.straight()`, `.turn()`) to drive between intersections. The Navigator is a wrapper that translates path coordinates into drive commands. |
| "save_obstacles and load_obstacles need to use `with open`" | Both `f = open(...)` / `f.close()` and `with open(...) as f:` work correctly. Use whichever style you are comfortable with. The important thing is that the file is written and read in the correct format. |
| "The blocked list resets between destinations" | The blocked list must persist across ALL destinations within a single run. It is a single list variable that grows as the robot discovers obstacles. Do not create a new empty list for each destination. |

## Differentiation

**For struggling students**:
- Provide the capstone starter file which has all classes complete and only requires filling in the main loop logic
- Reduce to 2 destinations instead of 4 to simplify debugging
- Use a 3x3 grid with one obstacle for initial testing
- Allow simulation-only demos (printing paths instead of driving the robot) for partial credit
- Pair with a partner: one student handles the code, the other handles the robot and grid setup
- Break the project into checkpoints: (1) paths compute correctly, (2) obstacles are detected, (3) file I/O works, (4) full integration
- Provide a working reference program to study before building their own

**For advanced students**:
- **Extension 1: Live obstacle detection during driving (+5 points)** -- Check for obstacles not just at intersections but continuously while driving between them. If an obstacle appears mid-segment, stop, back up, and reroute.
- **Extension 2: Destination optimization (+5 points)** -- Instead of visiting destinations in a fixed order, compute the nearest unvisited destination and visit that one next. This is a simplified version of the Traveling Salesman Problem.
- **Extension 3: Obstacle expiration (+5 points)** -- After 3 runs, "forget" old obstacles and re-check them. This handles the case where an obstacle has been removed from the grid.
- **Extension 4: Visual logging (+3 points)** -- After each run, print a text-based grid map showing the path taken, obstacles found, and destinations visited. Example:
  ```
  S . . D
  . X . .
  . . X .
  D . . D
  ```

## Materials & Code Examples

### Complete Capstone Program (Simulation Version)
```python
# capstone_simulation.py
# Module 5 Capstone: Full System Integration
# This version uses simulated obstacles for testing without the physical robot.

class Dijkstra:
    def __init__(self, start, blocked):
        self.position = start
        self.blocked = blocked
        self.graph = self.build_graph(4, 4)

    def build_graph(self, rows, cols):
        graph = {}
        for r in range(rows):
            for c in range(cols):
                if (r, c) in self.blocked:
                    continue
                neighbors = []
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in self.blocked:
                        neighbors.append((nr, nc))
                graph[(r, c)] = neighbors
        return graph

    def compute_path(self, destination):
        if destination not in self.graph:
            print("Destination is blocked or not in graph!")
            return []

        distances = {}
        previous = {}
        to_visit = []

        for node in self.graph:
            distances[node] = 999999
            previous[node] = None
            to_visit.append(node)

        distances[self.position] = 0

        while len(to_visit) > 0:
            current = to_visit[0]
            for node in to_visit:
                if distances[node] < distances[current]:
                    current = node

            if current == destination:
                break

            to_visit.remove(current)

            for neighbor in self.graph[current]:
                if neighbor in to_visit:
                    new_dist = distances[current] + 1
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        previous[neighbor] = current

        path = []
        current = destination
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()

        if len(path) == 0 or path[0] != self.position:
            print("No path found!")
            return []

        return path


def save_obstacles(blocked, filename="obstacles.txt"):
    f = open(filename, "w")
    for node in blocked:
        f.write(str(node[0]) + "," + str(node[1]) + "\n")
    f.close()
    print("Saved " + str(len(blocked)) + " obstacles to " + filename)


def load_obstacles(filename="obstacles.txt"):
    blocked = []
    try:
        f = open(filename, "r")
        for line in f:
            parts = line.strip().split(",")
            blocked.append((int(parts[0]), int(parts[1])))
        f.close()
        print("Loaded " + str(len(blocked)) + " obstacles from " + filename)
    except:
        print("No obstacle file found. Starting fresh.")
    return blocked


# Simulated obstacles (replace with rangefinder on physical robot)
ACTUAL_OBSTACLES = [(1, 0), (2, 2), (1, 3)]
THRESHOLD = 15

def simulate_rangefinder(next_pos):
    """Return a short distance if next_pos is an actual obstacle."""
    if next_pos in ACTUAL_OBSTACLES:
        return 8.0
    return 50.0


# ===== MAIN PROGRAM =====

# Step 1: Load obstacles from file
blocked = load_obstacles()
print("Starting blocked list: " + str(blocked))

# Step 2: Define destinations
destinations = [(0, 3), (3, 3), (3, 0), (0, 0)]
current = (0, 0)
step_count = 0
reroute_count = 0

# Step 3: Main navigation loop
for dest in destinations:
    print("\n--- Heading to " + str(dest) + " ---")
    arrived = False

    while not arrived:
        pathfinder = Dijkstra(current, blocked)
        path = pathfinder.compute_path(dest)

        if len(path) == 0:
            print("No path to " + str(dest) + "! Skipping.")
            break

        print("Path: " + str(path))

        rerouted = False
        for i in range(len(path) - 1):
            next_pos = path[i + 1]

            # Check for obstacle
            distance = simulate_rangefinder(next_pos)

            if distance < THRESHOLD:
                if next_pos not in blocked:
                    blocked.append(next_pos)
                    print("  OBSTACLE at " + str(next_pos) + "! Rerouting...")
                reroute_count = reroute_count + 1
                rerouted = True
                break

            # Move to next intersection
            current = next_pos
            step_count = step_count + 1
            print("  Moved to " + str(current))

        if not rerouted:
            arrived = True
            print("  Arrived at " + str(dest) + "!")

# Step 4: Save obstacles to file
save_obstacles(blocked)

# Step 5: Print results
print("\n===== RUN COMPLETE =====")
print("Total steps: " + str(step_count))
print("Total reroutes: " + str(reroute_count))
print("Obstacles found: " + str(blocked))
```

### File I/O Functions
```python
# save_load_obstacles.py
# Standalone file I/O functions for saving and loading obstacle data

def save_obstacles(blocked, filename="obstacles.txt"):
    """Save the blocked list to a text file, one obstacle per line."""
    f = open(filename, "w")
    for node in blocked:
        f.write(str(node[0]) + "," + str(node[1]) + "\n")
    f.close()


def load_obstacles(filename="obstacles.txt"):
    """Load the blocked list from a text file. Returns empty list if file not found."""
    blocked = []
    try:
        f = open(filename, "r")
        for line in f:
            parts = line.strip().split(",")
            blocked.append((int(parts[0]), int(parts[1])))
        f.close()
    except:
        pass
    return blocked


# Test the functions
test_blocked = [(1, 0), (2, 2), (1, 3)]
save_obstacles(test_blocked)
print("Saved:", test_blocked)

loaded = load_obstacles()
print("Loaded:", loaded)
print("Match:", test_blocked == loaded)
```

### Navigator Class with DifferentialDrive
```python
# navigator_xrp.py
# Navigator class that translates grid paths into XRP robot movements

from XRPLib.differential_drive import DifferentialDrive

class Navigator:
    def __init__(self):
        self.drivetrain = DifferentialDrive.get_default_differential_drive()
        self.heading = "north"  # Robot starts facing north (toward row 0)
        self.GRID_SPACING = 30  # cm between intersections

    def drive_path(self, path):
        """Drive the robot along a list of (row, col) positions."""
        for i in range(len(path) - 1):
            current = path[i]
            next_pos = path[i + 1]
            self.drive_segment(current, next_pos)

    def drive_segment(self, current, next_pos):
        """Drive from current intersection to an adjacent intersection."""
        dr = next_pos[0] - current[0]
        dc = next_pos[1] - current[1]

        # Determine required heading
        if dr == -1:
            target_heading = "north"
        elif dr == 1:
            target_heading = "south"
        elif dc == 1:
            target_heading = "east"
        elif dc == -1:
            target_heading = "west"

        # Turn to face the target heading
        turn_amount = self.get_turn_angle(self.heading, target_heading)
        if turn_amount != 0:
            self.drivetrain.turn(turn_amount)
        self.heading = target_heading

        # Drive forward one grid spacing
        self.drivetrain.straight(self.GRID_SPACING)

    def get_turn_angle(self, current_heading, target_heading):
        """Calculate the turn angle from current heading to target heading."""
        headings = ["north", "east", "south", "west"]
        current_idx = headings.index(current_heading)
        target_idx = headings.index(target_heading)
        diff = target_idx - current_idx

        if diff == 0:
            return 0
        elif diff == 1 or diff == -3:
            return 90
        elif diff == 2 or diff == -2:
            return 180
        elif diff == -1 or diff == 3:
            return -90
```

## Teaching Notes
- **Integration is the hard part.** Students often underestimate how difficult it is to connect components that work individually. The most common bugs are: passing the wrong variable (e.g., using an old blocked list instead of the updated one), forgetting to update `current` position after moving, and not re-creating the Dijkstra object after the blocked list changes.
- **Start with simulation.** Have ALL students get the simulation version working before touching the physical robot. The simulation lets them verify logic without hardware complications. Once paths compute correctly and the blocked list grows as expected, switching to the real rangefinder is straightforward.
- **The demo is a teaching moment.** When students present their two runs, ask them to explain WHY Run 2 is better. The answer should reference the blocked list being pre-loaded, not "the robot is smarter." The algorithm is identical; the data is better.
- **Expect integration bugs.** The most common issues are: (1) the blocked list not persisting between destinations because it gets re-created, (2) the robot's `current` position not being updated after each step, (3) the Dijkstra object not being re-created with the updated blocked list after an obstacle is found, and (4) the file I/O functions writing or reading in the wrong format.
- **Use the rubric as a checklist.** Have students self-assess against the rubric before demo day. Each rubric category maps to a specific lesson: Dijkstra (Lessons 4-5), Navigator (Lesson 6), Obstacle Detection (Lesson 7), Experience/File I/O (Lesson 8).
- **Celebrate the journey.** This is the final lesson. Take a moment to acknowledge how far students have come -- from printing "Hello World" to building an autonomous navigation system with pathfinding, sensing, and learning. That is a genuine accomplishment.
- **For 50-minute classes**, the capstone will likely span 2-3 class periods: one for assembly and simulation testing, one for physical robot testing, and one for demos. Plan accordingly.
- **For 3-hour sessions**, students should be able to complete assembly, testing, and demos in a single session. Budget at least 30 minutes for demos if the class has more than 10 students.

## Connections to Next Lessons
This is the final lesson of Module 5 and the capstone project for the entire course. Here is a summary of the complete learning journey:

- **Module 1** introduced Python fundamentals: variables, data types, input/output, and basic control flow. Students learned to write simple programs and interact with the user through text.
- **Module 2** built on those fundamentals with loops, functions, and more complex logic. Students gained the ability to write reusable code and solve multi-step problems.
- **Module 3** introduced the XRP robot and physical computing. Students connected software to hardware, controlling motors and reading sensors for the first time.
- **Module 4** introduced the Manhattan Distance algorithm and the Navigator class. Students built their first pathfinding system and learned about classes, methods, and object-oriented design. The Navigator provided a clean interface for swapping pathfinding algorithms.
- **Module 5** replaced Manhattan Distance with Dijkstra's algorithm, a real graph-based shortest-path algorithm used in GPS systems, network routing, and game AI. Students learned about graphs, dictionaries, algorithm implementation, testing, sensor integration, and experience-based learning.

The skills and concepts from this course extend into many future directions:
- **Computer Science**: Data structures, algorithms, artificial intelligence, machine learning
- **Robotics**: SLAM (Simultaneous Localization and Mapping), sensor fusion, motion planning
- **Software Engineering**: System integration, testing, modular design, file I/O
- **Real-world Applications**: GPS navigation, warehouse robots, self-driving vehicles, game development

Students who complete this capstone have demonstrated that they can design, build, test, and present a working software system that integrates multiple components. That is a skill that transfers to any field of computing.
