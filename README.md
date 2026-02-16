# XRP Python Programming Course

A comprehensive, project-based robotics course teaching high school students Python programming using XRP robots. Students progress from visual block-based programming through sophisticated algorithm design, culminating in autonomous grid navigation with obstacle avoidance using Dijkstra's algorithm.

## Course Overview

**Duration:** 18 weeks (5 modules)

**Prerequisites:** None—basic computer literacy only

**Objectives:**
- Transition from visual block-based programming to Python text-based programming
- Master fundamental programming concepts (loops, conditionals, functions, classes, data structures)
- Apply programming to solve real-world robotics challenges
- Understand and implement algorithms (Manhattan distance, Dijkstra's pathfinding)
- Develop problem-solving and debugging skills in a hands-on environment

**Capstone Goal:** Students program their robot to autonomously navigate a taped grid to multiple destinations, detecting obstacles and dynamically rerouting in real-time using Dijkstra's algorithm.

### Key Features

- **Just-in-Time Learning:** Python concepts are introduced when students need them to accomplish concrete robot tasks
- **Progressive Complexity:** Starts with simple driving, builds to sophisticated algorithm implementation
- **Reusable Code:** Students build classes across modules that they use and extend
- **Emphasis on Testing:** Especially in later modules, students learn to test code without hardware
- **Balance of Theory and Practice:** Worksheets and hand-tracing activities ground algorithm understanding before coding

## Course Structure

### Module 1: Learning How to Drive the Robot (3–4 weeks)
- **Theme:** Visual programming → Python transition
- **Concepts:** Variables, loops, functions, basic XRP API
- **Final Project:** Python program using a polygon function to draw multiple shapes

### Module 2: Line Tracking (4–5 weeks)
- **Theme:** Sensors, control loops, and your first classes
- **Concepts:** `while` loops, conditionals, `import`, classes, object composition
- **Final Project:** Robot follows a circle with a cross, reversing direction 4 times

### Module 3: Relative Driving on the Grid (1–2 weeks)
- **Theme:** Applying existing code to the grid
- **Concepts:** Using classes on a real grid, sequential driving
- **Final Project:** Robot drives a square pattern (2 intersections per side)

### Module 4: Manhattan Navigation (3–4 weeks)
- **Theme:** Coordinate systems, data structures, and algorithm thinking
- **Concepts:** Tuples, lists, Manhattan distance, separation of concerns
- **Final Project:** Robot navigates to a series of destinations using Manhattan pathfinding

### Module 5: Dijkstra's Algorithm (3–4 weeks)
- **Theme:** Graph algorithms, obstacle detection, dynamic rerouting
- **Concepts:** Dictionaries, graphs, Dijkstra's algorithm, rangefinder sensor
- **Final Project:** Robot detects obstacles and dynamically reroutes using Dijkstra's algorithm

## Folder Structure

- 📁 `module-01-driving/` through `module-05-dijkstra/` — Each module contains:
  - `lessons/` — Detailed lesson plans
  - `slides/` — Presentation outlines
  - `exercises/` — Hands-on activity guides
  - `worksheets/` — Pencil-and-paper activities (especially for algorithms)
  - `code/starter/` — Starter code templates for students
  - `code/solutions/` — Complete solution code
  - `README.md` — Module overview

- 📁 `teacher-guide/` — Pacing guide, differentiation strategies, assessment approach, XRP setup

- 📁 `templates/` — Reusable templates for creating lessons, exercises, worksheets, and slide outlines

- 📄 `course-outline.md` — High-level outline of all modules, concepts, and structure

## How to Use This Course

### For Instructors

1. **Start here:** Read `course-outline.md` and the pacing guide in `teacher-guide/`
2. **Per module:** Read the module README and familiarize yourself with the lessons
3. **Before each lesson:** Review the lesson plan, slides, and exercises
4. **During class:** Use the slide outline and guided practice activities
5. **Differentiation:** See `teacher-guide/differentiation.md` for supporting different learning levels
6. **Assessment:** Find rubrics and strategies in `teacher-guide/assessment-strategy.md`

### For Students

Each module builds progressively. Start with Module 1 and work through in order. Each lesson includes:
- Clear learning objectives
- Worked examples
- Independent exercises with starter code and solutions
- Reflection questions

## Getting Started

### Prerequisites

- XRP Robot kit (or access to simulation environment)
- Python 3.8+ installed
- A code editor (VS Code recommended)
- XRP robotics framework and libraries (see `teacher-guide/xrp-setup-guide.md`)

### Quick Start

1. Ensure XRP hardware/simulator is set up (see teacher guide)
2. Complete Module 1, Lessons 1–5 with Blockly to get comfortable with the robot
3. Transition to Python in Module 1, Lessons 8–11
4. Proceed through remaining modules in sequence

## Python Concepts Covered

| Concept | Introduced | Modules |
|---|---|---|
| Variables, assignment | Module 1 | All |
| Loops (`for`, `while`) | Module 1, 2 | All |
| Functions | Module 1 | All |
| Conditionals (`if`/`else`) | Module 2 | 2–5 |
| Classes and objects | Module 2 | 2–5 |
| Lists and tuples | Module 4 | 4–5 |
| Dictionaries | Module 5 | 5 |
| Algorithms (Manhattan, Dijkstra) | Modules 4–5 | 4–5 |

## Support & Resources

- **XRP Documentation:** [XRP Robotics Documentation](https://www.xrpcode.org/)
- **Python Resources:** Official [Python.org](https://python.org) documentation
- **Algorithm Visualization:** Khan Academy and other online resources

## Contribution & Customization

This course is designed to be adaptable. You can:
- Modify lesson pacing based on student needs
- Add or substitute exercises
- Adjust the grid complexity for the capstone
- Include additional sensors or challenges

## Teachers' Philosophy

This course is built on the principle that students learn programming best when:
1. They have a concrete, engaging goal (making a robot move and navigate)
2. Programming concepts are introduced just-in-time (when needed to accomplish something)
3. They build reusable, tested code that they use across projects (progressive class development)
4. They understand algorithms before implementing them (worksheets and hand-tracing)
5. They have time to debug and experiment

## License & Attribution

[Add your license and attribution information here]

---

**Questions or feedback?** Please contact [instructor email or repository maintainer]
