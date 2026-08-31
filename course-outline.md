# XRP Python Programming Course — Detailed Outline

## Course Overview

This course teaches high school students Python programming through hands-on robotics using XRP robots. Students begin with visual block-based programming, transition to Python, and progressively build reusable toolkits of functions that culminate in autonomous grid navigation using pathfinding algorithms. Every Python concept is introduced just-in-time — at the moment students need it to accomplish something concrete with their robot.

**Capstone goal:** The robot navigates a taped grid to a series of destinations using pathfinding algorithms (Manhattan, then Dijkstra), detecting and avoiding obstacles, and building "experience" over multiple runs.

**Prerequisites:** None beyond basic computer literacy. No prior programming experience required.

**Classes are optional.** Every module's core content is taught with plain functions — the same skill set as Module 1. Selected lessons include an Optional Extension that repackages the working functions as a class, for courses that also want to cover OOP. See `teacher-guide/classes-optional.md` for the full breakdown of where these appear and why.

---

## Python Concepts by Module

| Concept | Introduced | Reinforced |
|---|---|---|
| Variables, assignment | Module 1 | All modules |
| `print()` | Module 1 | All modules |
| Basic syntax, indentation | Module 1 | All modules |
| `for` loops | Module 1 | Modules 2–5 |
| Functions (`def`, parameters, return) | Module 1 | All modules |
| `while` loops | Module 2 | Modules 3–5 |
| `if`/`elif`/`else` | Module 2 | Modules 3–5 |
| Comparison and logical operators | Module 2 | Modules 3–5 |
| `import`, using libraries | Module 2 | Modules 3–5 |
| `random` module | Module 2 | — |
| Global variables, function toolkits | Module 2 | Modules 3–5 |
| *(Optional)* Classes (`class`, `__init__`, `self`) | Module 2 | Modules 3–5 |
| *(Optional)* Methods | Module 2 | Modules 3–5 |
| *(Optional)* Object composition (class uses class) | Module 2 | Modules 3–5 |
| Program structure (main program + reusable functions) | Module 3 | Modules 4–5 |
| Tuples | Module 4 | Module 5 |
| Lists, `append()`, iteration | Module 4 | Module 5 |
| Separation of concerns / interfaces | Module 4 | Module 5 |
| Dictionaries | Module 5 | — |
| Algorithm design | Module 5 | — |

---

## Module 1: Learning How to Drive the Robot

**Duration:** ~3–4 weeks
**Theme:** Get comfortable with the robot and transition from blocks to Python
**Final project:** A Python program using a polygon function to draw multiple shapes

### Phase A: Blockly (Lessons 1–5)

**Lesson 1: Meet the XRP**
- What is the XRP robot? Hardware tour (motors, wheels, sensors)
- Setting up the development environment
- First Blockly program: drive forward, drive backward
- *Exercise:* Make the robot drive forward 30 cm and stop

**Lesson 2: Drawing Shapes**
- Sequencing commands: drive, turn, drive, turn
- Understanding angles and distances
- *Exercise:* Draw a square on the whiteboard
- *Exercise:* Draw a triangle (understanding 120° exterior angles)

**Lesson 3: Functions**
- Why repeat yourself? Introducing functions in Blockly
- Creating a reusable "draw triangle" function
- *Exercise:* Make a function that draws a triangle, call it multiple times

**Lesson 4: Parameters**
- Making functions flexible with inputs
- Adding a size parameter to the triangle function
- *Exercise:* Draw triangles of three different sizes using one function

**Lesson 5: Generalizing with the Polygon Function**
- The relationship between number of sides and turn angle (360 ÷ sides)
- A single function that draws any polygon
- *Exercise:* Create a polygon function with a parameter for number of sides
- *Exercise:* Use it to draw a triangle, square, pentagon, and hexagon

### Phase B: Driving Challenges (Lessons 6–7)

**Lesson 6: Differential Drive and Circles**
- How two-wheel drive works: same speed vs. different speeds
- `set_effort()` and `set_speed()` for differential steering
- *Exercise:* Draw a circle by setting different wheel speeds
- *Exercise:* Draw circles of different sizes by varying the speed ratio

**Lesson 7: Driving Challenges**
- Combining skills: sequencing, precision, timing
- *Exercise:* Basketball drills — drive forward 30 cm and back, then 40 cm and back, then 50 cm and back
- *Exercise:* Navigate the fixed-course driving and parking challenge

### Phase C: Transition to Python (Lessons 8–11)

**Lesson 8: Hello, Python**
- What is Python? Why text-based programming?
- Side-by-side comparison: Blockly blocks vs. Python code
- Variables, `print()`, basic XRP commands in Python
- *Exercise:* Rewrite the "drive forward and stop" program in Python

**Lesson 9: Loops in Python**
- The `for` loop: `for i in range(n)`
- How the Blockly repeat block maps to `for`
- *Exercise:* Rewrite the square-drawing program in Python

**Lesson 10: Functions in Python**
- `def`, parameters, calling functions
- How Blockly functions map to Python `def`
- *Exercise:* Rewrite the triangle function in Python with a size parameter

**Lesson 11: Module 1 Final Project**
- Bringing it all together: the polygon function in Python
- Writing a main program that calls the function to draw multiple shapes
- *Exercise:* Write a `draw_polygon(sides, size)` function and a main program that draws at least 4 different shapes

### Python Concepts Introduced
Variables, `print()`, `for` loops, `range()`, `def`, parameters, function calls, basic XRP API (`drivetrain.straight()`, `drivetrain.turn()`)

---

## Module 2: Line Tracking

**Duration:** ~4–5 weeks
**Theme:** Sensors, control loops, and organizing code into reusable toolkits
**Final project:** Robot follows a circle with a cross, reversing direction 4 times using the sensor and driving toolkits

### Phase A: Understanding Sensors (Lessons 1–4)

**Lesson 1: The Reflectance Sensor**
- How reflectance sensors work (light vs. dark surfaces)
- Reading sensor values in Python with `print()`
- *Exercise:* Measure and record sensor values for: on the line, off the line, on the edge of the line. Save these values — you'll use them later.

**Lesson 2: Drive to the Edge and Stop**
- Introduction to `while` loops — keep doing something until a condition is met
- Comparison operators (`<`, `>`, `==`)
- *Exercise:* Start inside a taped circle, drive forward until a sensor detects the line, then stop

**Lesson 3: Bounce Driving**
- `if`/`else` — making decisions
- Turning the robot around when it hits an edge
- *Exercise:* Drive straight until hitting the circle edge, turn around, repeat continuously

**Lesson 4: Random Turns**
- `import random`, `random.randint()`
- Why deterministic bounce driving gets stuck (back and forth on the same line)
- *Exercise:* Modify the bounce program so the robot turns a random amount to avoid repetitive paths

### Phase B: Line Following (Lessons 5–7)

**Lesson 5: Proportional Control with One Sensor**
- What is a setpoint? Using the edge reading from Lesson 1
- Error = setpoint − sensor reading
- Steering correction proportional to error
- *Exercise:* Follow the edge of the circle using a single sensor and proportional control

**Lesson 6: Two-Sensor Line Following**
- Using left and right sensors together
- Steering value = left sensor − right sensor
- Why two sensors give smoother tracking
- *Exercise:* Follow the line using two sensors with differential steering

**Lesson 7: Detecting Intersections**
- What does a cross (intersection) look like to two sensors? Both sensors on the line.
- Adding the taped cross to the circle
- *Exercise:* Follow the circle and, upon reaching the cross, turn around and continue in the opposite direction

### Phase C: Building Reusable Toolkits (Lessons 8–10)

**Lesson 8: Sensor Functions**
- Why organize code into functions? Grouping related logic together
- Global variables shared across functions, functions calling functions
- *Exercise:* Build a sensor toolkit with:
  - `get_error()` — returns left − right sensor value
  - `is_at_cross()` — returns True when both sensors detect the line
  - `is_off_line()` — returns True when neither sensor detects the line
- *Optional Extension:* Refactor the toolkit into a `LineSensor` class (`class`, `__init__()`, `self`, methods)

**Lesson 9: Line-Tracking Functions**
- One toolkit calling into another
- The driving toolkit calls the Lesson 8 sensor functions
- *Exercise:* Build a driving toolkit with:
  - `track_until_cross()` — follows the line until an intersection is detected
  - `turn_right()` — turns right until detecting the line again
  - `turn_left()` — turns left until detecting the line again
- *Optional Extension:* Refactor into a `LineTrack` class that composes a `LineSensor` object

**Lesson 10: Module 2 Final Project**
- Combining both toolkits in a main program
- *Exercise:* Write a program that uses the sensor and driving toolkits to:
  1. Follow the circle until hitting the cross
  2. Turn around
  3. Continue following
  4. Repeat for 4 reversals, then stop

### Python Concepts Introduced
`while` loops, `if`/`elif`/`else`, comparison operators (`<`, `>`, `<=`, `>=`, `==`), logical operators (`and`, `or`, `not`), `import`, `random` module, global variables, function toolkits, `True`/`False`/booleans. *Optional:* classes (`class`, `__init__`, `self`), methods, object composition.

---

## Module 3: Relative Driving on the Grid

**Duration:** ~1–2 weeks
**Theme:** Using your toolkit on the grid and verifying it works
**Final project:** Robot drives a square pattern on the grid (2 intersections per side)

### Lessons

**Lesson 1: Introduction to the Grid**
- The physical setup: taped lines forming a grid on whiteboard material
- How intersections relate to the cross detection from Module 2
- Reviewing the driving toolkit functions: `track_until_cross()`, `turn_right()`, `turn_left()`
- *Exercise:* Place the robot on the grid and use the toolkit to drive to the next intersection and stop

**Lesson 2: Driving Multiple Intersections**
- Driving past an intersection: what happens after detecting a cross?
- Sequencing: drive to intersection → drive past it → drive to next intersection
- `for` loops for repetition
- *Exercise:* Drive forward exactly 2 intersections (drive to cross, continue past, drive to next cross)

**Lesson 3: Turning on the Grid**
- Using `turn_right()` at an intersection to make a 90° turn onto a perpendicular line
- Program structure: sequence of drive-and-turn operations
- *Exercise:* Drive 2 intersections forward, then turn right. Verify the robot is lined up on the new path.

**Lesson 4: Module 3 Final Project**
- Putting it together: the square pattern
- *Exercise:* Write a program that repeats 4 times:
  1. Drive forward 2 intersections (drive to cross, past it, to next cross)
  2. Turn right
- The robot should end up back where it started

### Python Concepts Reinforced
Reusing existing functions, `for` loops, sequential program structure, debugging/testing physical systems

---

## Module 4: Manhattan Navigation

**Duration:** ~3–4 weeks
**Theme:** Coordinate systems, data structures, and separating algorithm from action
**Final project:** Robot navigates to a list of destinations using Manhattan pathfinding

### Phase A: Data Structures (Lessons 1–3)

**Lesson 1: Coordinates on the Grid**
- The grid as a coordinate system: (row, column)
- How the robot's position maps to coordinates
- Counting intersections to determine position
- *Exercise:* Map out the physical grid with coordinates. Identify at least 5 positions by (row, col).

**Lesson 2: Tuples**
- What is a tuple? Immutable pair of values: `(row, col)`
- Creating, accessing elements (`position[0]`, `position[1]`)
- Why tuples for coordinates (they don't change)
- *Exercise:* Write code that stores positions as tuples and prints them

**Lesson 3: Lists**
- What is a list? Ordered, mutable collection
- Creating lists, `append()`, iterating with `for`
- A path is a list of coordinate tuples
- *Exercise:* Create a list of coordinate tuples representing a path and print each step

### Phase B: The Manhattan Function (Lessons 4–6)

**Lesson 4: The Manhattan Algorithm**
- How Manhattan distance works: move along rows first, then columns
- Walking through examples on paper: given start (0,0) and destination (2,3), the path is (0,0)→(1,0)→(2,0)→(2,1)→(2,2)→(2,3)
- *Exercise:* Work out paths by hand for several start/destination pairs (worksheet)

**Lesson 5: A Reusable Manhattan Function**
- Naming the algorithm for reuse: `compute_manhattan_path(position, destination)` returns a list of tuples
- Adding a docstring; regression-testing against Lesson 4's output
- *Optional Extension:* wrap it in a `Manhattan` class
- *Exercise:* Rename and document `compute_manhattan_path`, test it against 4+ destination pairs

**Lesson 6: Testing Without a Robot**
- Writing a test program: call `compute_manhattan_path` with various destinations, print the paths
- Verifying the output matches hand-calculated paths from Lesson 4
- *Exercise:* Write a test main program that checks at least 4 different destination pairs and prints results

### Phase C: Driving the Path (Lessons 7–9)

**Lesson 7: The Challenge of Turning**
- The robot needs to face the right direction before driving to the next intersection
- The turn depends on two things: where the next intersection is relative to current position AND which way the robot is currently facing
- Working through the logic on paper with diagrams
- *Exercise:* Worksheet — given a current position, current heading, and next coordinate, determine what turn (if any) is needed

**Lesson 8: Driving the Path**
- `desired_heading()`, `turn_to()`, and `drive_path(path, position, heading)` -- position/heading threaded through parameters and return values
- Reusing the Module 2/3 driving toolkit (`turn_right()`, `track_until_cross()`, `clear_intersection()`) directly
- *Optional Extension:* package it as a `Navigator` class that composes `LineTrack`
- *Exercise:* Implement `desired_heading()`, `turn_to()`, and `drive_path()`

**Lesson 9: Module 4 Final Project**
- Integration: main program that calls `compute_manhattan_path()` and `drive_path()` in a loop
- A single `position`/`heading` pair carried through the loop -- no separate objects to keep in sync
- *Exercise:* Integrate your functions to drive to a series of at least 4 destinations on the grid

### Python Concepts Introduced
Tuples (creating, indexing), lists (`append()`, iteration, list of tuples), functions with docstrings, threading state through parameters and return values, separation of concerns (algorithm vs. physical driving), testing strategy (test without hardware). *Optional:* wrapping the same logic in `Manhattan`/`Navigator` classes.

---

## Module 5: Dijkstra's Algorithm (Capstone)

**Duration:** ~3–4 weeks
**Theme:** Graph algorithms, obstacle detection, and the power of modular code
**Final project:** Robot detects blocked intersections and dynamically reroutes using Dijkstra's algorithm

### Phase A: Graph Theory and Dictionaries (Lessons 1–3)

**Lesson 1: The Grid as a Graph**
- Nodes = intersections, edges = paths between adjacent intersections
- Weighted vs. unweighted graphs (our grid is unweighted, all edges cost 1)
- Why Manhattan distance doesn't help when intersections are blocked
- *Exercise:* Draw the grid as a graph on paper. Mark some nodes as blocked. Try to find the shortest path by hand.

**Lesson 2: Dictionaries**
- What is a dictionary? Key-value pairs
- Creating dictionaries, accessing values, checking membership
- Using dictionaries to represent a graph: keys are node coordinates, values are lists of neighbor coordinates
- *Exercise:* Write code to represent the grid as a dictionary of neighbors. Print all neighbors for a given intersection.

**Lesson 3: Dijkstra's Algorithm — The Concept**
- Walk-through of the algorithm step by step using the grid graph
- Visited set, distances, previous-node tracking
- Tracing the algorithm on paper with blocked nodes
- *Exercise:* Worksheet — trace Dijkstra's algorithm by hand on a small grid with blocked intersections. Record each step.

### Phase B: Implementing Dijkstra (Lessons 4–6)

**Lesson 4: The Dijkstra Functions**
- `build_dijkstra_graph(rows, cols, blocked)` builds the graph, excluding blocked nodes
- `compute_dijkstra_path(position, destination, graph)` -- same first-two-parameter shape as `compute_manhattan_path`
- *Optional Extension:* package both as a `Dijkstra` class
- *Exercise:* Implement `build_dijkstra_graph()` and the `compute_dijkstra_path()` placeholder

**Lesson 5: Implementing compute_dijkstra_path()**
- Translating the hand-traced algorithm into Python
- Using a list as a simple priority queue (or sorted list)
- Reconstructing the path from the previous-node dictionary
- *Exercise:* Complete `compute_dijkstra_path()`. Test with known blocked intersections and verify output matches hand-traced results.

**Lesson 6: Testing and Swapping**
- Testing Dijkstra independently: build a graph, request paths, print results
- The shape mismatch: `compute_dijkstra_path` needs an extra `graph` argument and includes the start in its output; a `compute_path(algorithm, ...)` dispatch function normalizes both
- *Optional Extension:* true polymorphism via matching `compute_path(destination)` methods on `Manhattan`/`Dijkstra` classes, no dispatch function needed
- *Exercise:* Build the dispatch function. Swap the algorithm argument to route around obstacles.

### Phase C: Capstone Project (Lessons 7–9)

**Lesson 7: Obstacle Detection with the Rangefinder**
- The ultrasonic rangefinder: how it works, reading distance values
- Detecting a physical obstacle at an intersection
- *Exercise:* Write code to detect whether an object is blocking the intersection ahead. Print the result.

**Lesson 8: Building Experience**
- Maintaining a list of known blocked intersections that grows over time
- On each run: attempt to navigate, detect new obstacles, add to blocked list, rebuild the graph and recompute the path
- *Exercise:* Write a program that attempts to drive to a destination, and if it encounters a blocked intersection, adds it to the blocked list, recalculates the path using `compute_dijkstra_path()`, and tries again.

**Lesson 9: Module 5 Capstone Project**
- The teacher sets up the grid with physical obstacles at several intersections
- Students program the robot to:
  1. Navigate to a series of destinations
  2. Detect blocked intersections using the rangefinder
  3. Add blocked intersections to the blocked list
  4. Rebuild the graph and recompute paths on subsequent runs
  5. Demonstrate the robot getting better with "experience" — each run is more efficient as the map of blocked nodes grows

### Python Concepts Introduced
Dictionaries (creation, access, `in` keyword, nested structures), graph representation, algorithm implementation, dispatch functions for swappable behavior, dynamic data (growing blocked list across runs). *Optional:* true polymorphism via matching class method signatures.

---

## Proposed Folder Structure

```
xrp-python-course/
├── README.md
├── course-outline.md
│
├── module-01-driving/
│   ├── README.md
│   ├── lessons/
│   │   ├── 01-meet-the-xrp.md
│   │   ├── 02-drawing-shapes.md
│   │   ├── 03-functions-in-blockly.md
│   │   ├── 04-parameters.md
│   │   ├── 05-polygon-function.md
│   │   ├── 06-differential-drive.md
│   │   ├── 07-driving-challenges.md
│   │   ├── 08-hello-python.md
│   │   ├── 09-loops-in-python.md
│   │   ├── 10-functions-in-python.md
│   │   └── 11-final-project.md
│   ├── slides/
│   │   └── (one .pptx per lesson)
│   ├── exercises/
│   │   └── (activity guide .md per exercise)
│   ├── worksheets/
│   │   └── (.md worksheets)
│   └── code/
│       ├── starter/
│       └── solutions/
│
├── module-02-line-tracking/
│   ├── README.md
│   ├── lessons/
│   ├── slides/
│   ├── exercises/
│   ├── worksheets/
│   └── code/
│       ├── starter/
│       └── solutions/
│
├── module-03-grid-driving/
│   ├── README.md
│   ├── lessons/
│   ├── slides/
│   ├── exercises/
│   ├── worksheets/
│   └── code/
│       ├── starter/
│       └── solutions/
│
├── module-04-manhattan/
│   ├── README.md
│   ├── lessons/
│   ├── slides/
│   ├── exercises/
│   ├── worksheets/
│   └── code/
│       ├── starter/
│       └── solutions/
│
├── module-05-dijkstra/
│   ├── README.md
│   ├── lessons/
│   ├── slides/
│   ├── exercises/
│   ├── worksheets/
│   ├── code/
│   │   ├── starter/
│   │   └── solutions/
│   ├── rubric.md
│   └── project-milestones.md
│
├── teacher-guide/
│   ├── pacing-guide.md
│   ├── differentiation.md
│   ├── assessment-strategy.md
│   └── xrp-setup-guide.md
│
└── templates/
    ├── lesson-template.md
    ├── exercise-template.md
    ├── worksheet-template.md
    └── slide-outline-template.md
```

---

## Suggested Pacing (18-week semester)

| Weeks | Module | Notes |
|---|---|---|
| 1–4 | Module 1: Driving | Blockly first, Python transition in weeks 3–4 |
| 5–9 | Module 2: Line Tracking | Heaviest module — sensors, control, and first reusable toolkits |
| 10–11 | Module 3: Grid Driving | Short module, mostly applying existing code to the grid |
| 12–15 | Module 4: Manhattan | Data structures + two new functions/toolkits |
| 16–18 | Module 5: Dijkstra (Capstone) | Algorithm + obstacle detection + capstone demo |

---

## Notes for Content Development

- **Templates first:** Before writing any module content, establish consistent templates for lessons, exercises, and worksheets. This ensures uniform quality and makes bulk creation faster.
- **Code builds across modules:** The sensor toolkit → driving toolkit → `drive_path` → `compute_manhattan_path`/`compute_dijkstra_path` chain means earlier code must be solid. Include solution code at each stage so students who fall behind have working functions to build on.
- **Test without robots:** Modules 4 and 5 emphasize testing path computation without hardware. This is both a practical concern (limited robots, debugging time) and a teaching opportunity (separation of concerns).
- **Worksheets for algorithms:** Modules 4 and 5 benefit from paper-based algorithm tracing before writing code. These worksheets are important scaffolding.
