# Lesson 9 Slide Outline: Module 5 Capstone Project

## Slide 1: Title & Learning Objectives
**Title:** Module 5 Capstone Project

**Learning Objectives:**
- Integrate Dijkstra pathfinding, Navigator, rangefinder obstacle detection, and obstacle memory into a single program
- Design a program that visits 4 or more destinations while detecting and avoiding obstacles
- Demonstrate learning by showing improved performance across multiple runs
- Present and explain a working autonomous navigation system

**Agenda:**
- This is your graduation project! (5 min)
- Project requirements and rubric (10 min)
- Program structure walkthrough (10 min)
- Work time: build your system (40 min for 3-hour sessions / 15 min for 50-min)
- Demo format: Run 1 and Run 2 (10 min)
- Extensions for extra credit (5 min)

---

## Slide 2: Hook — This Is Your Graduation Project!
**You've built every piece of the puzzle:**

| Lesson | What You Built |
|---|---|
| Lesson 1 | Understanding the grid as a graph |
| Lesson 2 | Dictionaries to represent the graph in Python |
| Lesson 3 | Dijkstra's algorithm — the concept |
| Lessons 4-5 | The Dijkstra class with `compute_path` |
| Lesson 6 | Testing and swapping Dijkstra into Navigator |
| Lesson 7 | Obstacle detection with the rangefinder |
| Lesson 8 | Building experience — remembering obstacles across runs |

**Now you put it ALL together.** One program. Full autonomy. A robot that navigates, discovers, and learns.

---

## Slide 3: Project Requirements
**Your program must:**

1. **Visit 4 or more destinations** on the grid in sequence
2. **Use Dijkstra's algorithm** to compute paths (not Manhattan)
3. **Detect obstacles** using the ultrasonic rangefinder at each intersection
4. **Update the blocked list** when a new obstacle is discovered
5. **Recompute paths** after discovering an obstacle
6. **Save obstacles** to a file at the end of each run
7. **Load obstacles** from the file at the start of each run
8. **Demonstrate learning:** Run 2 should perform better than Run 1

**Deliverables:**
- Working Python program
- Two demonstration runs (Run 1 and Run 2)
- Brief explanation of how the system works

---

## Slide 4: Program Structure
**The overall structure of your capstone program:**

```python
from dijkstra import Dijkstra
from navigator import Navigator
from XRPLib.rangefinder import Rangefinder

# Setup
rangefinder = Rangefinder.get_default_rangefinder()
blocked_nodes = load_obstacles()
THRESHOLD = 15
step_count = 0

# Destinations to visit
destinations = [(1, 3), (3, 3), (3, 0), (0, 2)]
current = (0, 0)

# Main loop
for dest in destinations:
    print(f"Heading to {dest}...")
    arrived = False
    while not arrived:
        pathfinder = Dijkstra(current, blocked_nodes)
        path = pathfinder.compute_path(dest)
        # Navigate along path with obstacle checking
        # If obstacle found: update blocked_nodes, recompute
        # If no obstacle: drive to next intersection
        # Update current position and step_count
    print(f"Arrived at {dest}!")

# Save and report
save_obstacles(blocked_nodes)
print(f"Total steps: {step_count}")
print(f"Obstacles found: {blocked_nodes}")
```

---

## Slide 5: The Navigation Loop in Detail
**Inside the main loop — handling each segment of the path:**

```python
for dest in destinations:
    arrived = False
    while not arrived:
        pathfinder = Dijkstra(current, blocked_nodes)
        path = pathfinder.compute_path(dest)

        if len(path) == 0:
            print(f"No path to {dest}! Skipping.")
            break

        rerouted = False
        for i in range(len(path) - 1):
            # Check ahead
            distance = rangefinder.distance()
            if distance < THRESHOLD:
                blocked_nodes.append(path[i + 1])
                print(f"Blocked: {path[i + 1]}, rerouting...")
                rerouted = True
                break
            # Drive one segment
            nav.drive_segment(path[i], path[i + 1])
            current = path[i + 1]
            step_count = step_count + 1

        if not rerouted:
            arrived = True
```

**Key logic:** If an obstacle is found mid-path, break out of the path loop, recompute from the current position, and try again.

---

## Slide 6: Demo Format — Run 1 and Run 2
**Run 1: Discovery Run**
- Delete obstacles.txt (start fresh)
- Place 2-3 obstacles on the grid
- Run the program
- Watch the robot discover obstacles and reroute
- Note the total step count

**Run 2: Experience Run**
- Keep the same obstacles in place
- Run the program again (same code!)
- The robot loads saved obstacles and plans around them from the start
- Note the total step count

**What to show your teacher:**
```
Run 1: Total steps = 22, Obstacles discovered = 3, Reroutes = 3
Run 2: Total steps = 16, Obstacles discovered = 0, Reroutes = 0
```

**The difference in steps IS the learning.**

---

## Slide 7: Grading Rubric
**Total: 60 points**

| Category | Points | Criteria |
|---|---|---|
| **Dijkstra Pathfinding** | 10 | Uses Dijkstra class to compute paths; paths are correct |
| **Navigator Integration** | 10 | Robot physically drives the computed paths on the grid |
| **Obstacle Detection** | 10 | Rangefinder detects obstacles; blocked list updates correctly |
| **Path Recomputation** | 10 | Robot recomputes path after discovering obstacle; new path avoids it |
| **Experience (File I/O)** | 10 | Obstacles saved after Run 1; loaded at start of Run 2 |
| **Demonstration** | 5 | Run 1 discovers obstacles; Run 2 avoids them from the start |
| **Code Quality** | 5 | Code is readable, uses functions, has comments |

**Bonus opportunities:** See extensions on the next slide.

---

## Slide 8: Extensions for Extra Credit
**Already finished? Try these challenges:**

**Extension 1: Live obstacle detection during path execution (+5 points)**
- Check for obstacles not just at intersections, but while driving between them
- If an obstacle appears mid-segment, stop, back up, and reroute

**Extension 2: Multiple destination optimization (+5 points)**
- Instead of visiting destinations in a fixed order, find the best order
- Hint: try the nearest unvisited destination first

**Extension 3: Obstacle expiration (+5 points)**
- After 3 runs, "forget" old obstacles and re-check them
- This handles the case where an obstacle was removed

**Extension 4: Visual logging (+3 points)**
- Print a grid map after each run showing the path taken and obstacles found
- Example:
  ```
  S . . .
  . X . .
  . . X .
  . . . E
  ```

---

## Slide 9: Your Turn!
**Activity: Build Your Capstone Program**

**Step 1:** Start with your code from Lessons 7 and 8
- You should already have: Dijkstra class, Navigator, rangefinder reading, save/load functions

**Step 2:** Create the main program
1. Load obstacles from file
2. Define your list of 4+ destinations
3. Write the main navigation loop with obstacle detection
4. Save obstacles at the end

**Step 3:** Test without physical obstacles first
- Use a hard-coded blocked list to verify paths are correct
- Print paths instead of driving to check logic

**Step 4:** Test on the physical grid
- Place obstacles and run the full program
- Run it twice to demonstrate learning

**Checkpoints:**
- Does the robot visit all 4+ destinations?
- Does it detect and avoid obstacles?
- Does Run 2 perform better than Run 1?
- Is the code organized with functions and comments?

---

## Slide 10: Presentation Tips
**When you demo your project:**

1. **Explain before you run:** Tell the audience what destinations the robot will visit and where the obstacles are
2. **Narrate Run 1:** "The robot doesn't know about any obstacles yet. Watch what happens when it encounters one."
3. **Show the file:** Open obstacles.txt between runs to show what the robot learned
4. **Narrate Run 2:** "Now the robot knows about those obstacles. Watch it plan around them from the start."
5. **Show the numbers:** Compare step counts between Run 1 and Run 2

**Common demo pitfalls:**
- Battery dies mid-demo — charge fully before presenting
- Robot misaligned — recalibrate line following before demo
- Obstacle falls over — use sturdy objects and tape them down

---

## Slide 11: Connection to What's Next
**What you built in Module 5:**
- A graph representation of the grid
- Dijkstra's algorithm for shortest-path finding
- A swappable pathfinding interface
- Real-time obstacle detection
- Experience-based learning across runs

**Where these ideas appear in the real world:**
- **Self-driving cars:** Use graph algorithms and sensor fusion to navigate
- **Warehouse robots (Amazon):** Navigate grids, avoid obstacles, optimize routes
- **Game AI:** Characters find paths around walls and enemies
- **Internet routing:** Data packets find shortest paths through networks

**Congratulations!** You've built a robot that can navigate, sense, and learn. That's real robotics.
