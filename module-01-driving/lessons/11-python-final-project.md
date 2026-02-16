# Lesson 11: Python Final Project

## Overview
Students synthesize all Module 1 concepts—loops, functions, parameters, motor control, and geometric thinking—to design and implement their own Python robot programs. This capstone lesson serves as both a comprehensive assessment and a portfolio piece. Students will work in teams or individually to create a complete, documented Python program that demonstrates mastery of the course.

## Learning Objectives
By the end of this lesson, students will be able to:
- Design a complete Python program from problem statement to deployment
- Synthesize loops, functions, parameters, and conditionals in a single project
- Write well-documented, professional-quality Python code
- Debug and test programs systematically
- Present and explain their work to peers
- Reflect on learning and identify areas for growth

## Key Concepts
- **Full software lifecycle**: Design → Code → Test → Debug → Deploy → Document
- **Modularity**: Breaking complex problems into manageable functions
- **Code documentation**: Comments, docstrings, clear naming for future readers
- **Debugging methodology**: Predict → Test → Observe → Adjust
- **Testing strategy**: Unit testing (individual functions) → Integration testing (full program)
- **Professional standards**: Clean code, proper structure, error handling
- **Reflection**: Learning from mistakes and planning improvements

## Materials Required
- XRP Robot with large clear driving space (prefer 5m x 5m or larger)
- VS Code with Python installed and XRPLib configured
- Project rubric (provided below)
- Peer feedback forms
- Optional: Measuring tape, markers, obstacles for course building
- Documentation: Reference all previous lesson code

## Lesson Flow

### Introduction & Project Selection (15 minutes)
**For 50-min classes:** 12 min
**For 3-hour sessions:** 15-20 min

1. **Module Reflection**:
   - Review: What have we learned? (Blockly → Python, loops, functions, geometry, motor control)
   - Celebrate: "You know enough to build something cool"
   - Connect: Real robots use these same concepts

2. **Project Options** (Students choose one or design their own):

   **Option A: Polygon Artist** (Recommended for beginners)
   - Goal: Draw a series of polygons and create a geometric art piece
   - Requirements:
     - Define `draw_polygon(sides, distance, effort)` function
     - Define helper function for calculation or movement
     - Read number of sides from user or hardcode a sequence
     - Draw at least 3 different polygons
     - Add decorative movement (spacing between shapes, spiral pattern, etc.)
   - Example output: Concentric hexagons, star pattern, or symmetrical design
   - Difficulty: Medium (uses Lesson 5 concepts in Python)

   **Option B: Precision Navigation System** (Medium difficulty)
   - Goal: Navigate a complex course with waypoints
   - Requirements:
     - Define functions for each course segment
     - Implement turn calibration (measure actual vs. expected angles)
     - Handle obstacles or course adaptations
     - Return robot to starting position
     - Track and report position accuracy
   - Example: Delivery robot that visits multiple locations and returns home
   - Difficulty: Medium-Hard (uses Lessons 1-6 concepts)

   **Option C: Sensor-Based Behavior** (Advanced)
   - Goal: Robot responds to its environment
   - Requirements:
     - Use rangefinder to detect obstacles
     - Use reflectance sensors to detect surface changes
     - Implement conditional movement based on sensor input
     - Multiple behaviors (wall-following, object avoidance, line-tracing)
     - Graceful error handling and recovery
   - Example: Autonomous robot that explores a room, avoids obstacles, reports findings
   - Difficulty: Hard (requires sensor library integration)

   **Option D: Creative Project** (Design your own)
   - Any Python project using XRP that demonstrates course mastery
   - Examples: Race timer, swarm choreography, musical robot, etc.
   - Approval needed: Brief description to instructor
   - Difficulty: Variable

3. **Team Formation** (Optional):
   - Teams of 2-3 students recommended (encourages collaboration, reduces workload)
   - Individual projects allowed but more demanding
   - Teams select role assignments: Lead Programmer, Tester, Documentor (rotate roles?)

4. **Project Brief & Timeline**:
   - Project deadline, checkpoints, presentation date
   - Today: Planning (30 min)
   - Days 2-3: Development (2-3 hours total)
   - Day 3-4: Testing & Refinement (1-2 hours)
   - End of Day 4: Presentation & Reflection (1 hour)

### Planning Phase: Design & Pseudocode (25 minutes)
**For 50-min classes:** 20 min
**For 3-hour sessions:** 30 min

1. **Problem Breakdown**:
   - Identify sub-problems: What are the discrete tasks?
   - Example (Navigation): Start → Segment 1 → Segment 2 → Return → Report
   - Example (Artist): Load shapes → Draw each → Add effects → Finish

2. **Function Inventory**:
   - List required functions: Names, parameters, return values
   - Example:
     ```python
     def draw_polygon(sides, distance, effort) → void
     def navigate_segment(distance, direction) → bool
     def calculate_angle(sides) → float
     def sensor_check() → dict
     ```
   - Separate utilities from main logic

3. **Data & Variables**:
   - What data does the program need? (Course data, shape list, sensor readings)
   - How will data flow? (Functions pass data via parameters/return)
   - Constants: Should distances be hardcoded or parameterized?

4. **Pseudocode on Paper**:
   - Write outline in plain English (not Python syntax)
   ```
   Main:
       Initialize robot
       Load shape configuration
       For each shape:
           Calculate parameters
           Call draw_shape()
           Report status
       Return to start
   ```
   - Advantages: Clarify logic before coding, easy to discuss with team

5. **Risk Assessment**:
   - What could go wrong? (Hardware failures, timing issues, sensor errors)
   - Backup plans? (Retry mechanisms, fallback behaviors, error messages)
   - Dependencies? (Does option C need sensor library installed?)

6. **Deliverable**:
   - Written plan (1-2 pages): Problem statement, approach, function list, pseudocode
   - Pseudocode diagram (optional): Visual representation of flow
   - Sign-off: Team lead confirms plan is feasible

### Implementation: Coding & Testing (45 minutes for 3-hour; 40 min for 50-min)
**For 50-min classes:** 35 min (continued next session)
**For 3-hour sessions:** 45-50 min

1. **Development Environment Setup**:
   - Create new Python file: `module_1_final_project_[teamname].py`
   - Import required libraries:
     ```python
     from XRPLib.differential_drive import DifferentialDrive
     from XRPLib.sensors.rangefinder import Rangefinder  # If needed
     from XRPLib.sensors.reflectance import Reflectance  # If needed
     from XRPLib.board import Board
     import time
     ```

2. **Incremental Development**:
   - Build ONE function at a time (don't write entire program)
   - Test each function independently before combining
   - Example order:
     1. Write `draw_polygon()` function, test with one call
     2. Write `navigate_segment()`, test independently
     3. Write `main()`, integrate functions
     4. Test full program

3. **Code Structure Template**:
   ```python
   """
   Module 1 Final Project: [Project Name]
   Team: [Team Members]
   Description: [2-3 sentence overview]
   """
   
   from XRPLib.differential_drive import DifferentialDrive
   import time
   
   # Global initialization
   drivetrain = DifferentialDrive.get_default_differential_drive()
   
   # ===== HELPER FUNCTIONS =====
   def calculate_angle(num_sides):
       """Calculate exterior angle for regular polygon."""
       return 360 / num_sides
   
   # ===== MAIN FUNCTIONS =====
   def draw_polygon(num_sides, size, effort):
       """Draw a regular polygon."""
       angle = calculate_angle(num_sides)
       for i in range(num_sides):
           drivetrain.straight(size, max_effort=effort)
           drivetrain.turn(angle, max_effort=effort)
   
   def main():
       """Main program flow."""
       print("Starting project...")
       draw_polygon(4, 30, 0.5)
       draw_polygon(6, 25, 0.5)
       print("Project complete!")
   
   # ===== RUN =====
   if __name__ == "__main__":
       main()
   ```

4. **Testing & Debugging Cycle**:
   - **Unit test** (single function): Call function with various inputs, observe behavior
   - **Integration test** (multiple functions): Call functions in sequence, check flow
   - **Full test** (complete program): Run end-to-end, check final result
   - **Instrumentation**: Use `print()` statements to debug:
     ```python
     print(f"Drawing polygon with {sides} sides at angle {angle}°")
     print(f"Position after segment: X={x}, Y={y}")
     ```

5. **Common Issues & Solutions**:
   - **Program won't start**: Check syntax, indentation, imports
   - **Robot doesn't move**: Check motor control, device connection
   - **Inconsistent behavior**: Check wheel slip, battery voltage, surface
   - **Code is hard to read**: Add comments, improve function names, refactor

6. **Deliverable** (at end of Day 2-3):
   - Working Python file (runs without errors)
   - Each team member has contributed code
   - Basic testing completed (all functions individually tested)
   - Code comments on complex sections

### Refinement & Documentation (30 minutes)
**For 50-min classes:** 25 min (continued next session)
**For 3-hour sessions:** 30-35 min

1. **Testing Intensive**:
   - Run program multiple times (test variability)
   - Measure accuracy (compare actual vs. expected)
   - Document any quirks or limitations
   - Adjust parameters if needed

2. **Code Quality**:
   - Add docstrings to all functions:
     ```python
     def draw_polygon(num_sides, size, effort):
         """
         Draw a regular polygon.
         
         Args:
             num_sides (int): Number of sides (3-8)
             size (float): Length of each side in cm (10-50)
             effort (float): Motor power 0.0-1.0
         
         Returns:
             None
         """
     ```
   - Clean up debug print statements (or move to optional verbose mode)
   - Remove unused variables or imports
   - Check indentation consistency

3. **Error Handling** (Optional but professional):
   ```python
   def draw_polygon(num_sides, size, effort):
       """Draw a polygon with validation."""
       if num_sides < 3:
           print("Error: Polygon must have at least 3 sides")
           return False
       
       try:
           # Drawing code here
       except Exception as e:
           print(f"Error while drawing: {e}")
           return False
       
       return True
   ```

4. **Code Review** (Peer feedback):
   - Team A reviews Team B's code
   - Feedback on: Readability, function design, documentation, testing
   - Constructive suggestions for improvement

5. **Documentation Package**:
   - **README.md**: Overview, how to run, what to expect
   - **CODE.md**: Function descriptions, parameters, example usage
   - **TESTING.md**: Test cases, results, known limitations
   - **LESSONS_LEARNED.md**: What went well, what was hard, improvements

6. **Deliverable** (at end of Day 3):
   - Final, polished Python file
   - Complete written documentation
   - Test log (what was tested, results)
   - Team reflection (brief notes on process)

### Presentation & Reflection (20 minutes)
**For 50-min classes:** 15-20 min (follow-up session)
**For 3-hour sessions:** 20-25 min (end of session)

1. **Live Demo**:
   - Each team demonstrates their robot program
   - 3-4 minutes per team: "What did you build? What does it do?"
   - Show robot in action (if possible) or video playback
   - Peers watch and take notes

2. **Technical Q&A** (2 min per team):
   - Explain one challenging part of the code
   - Describe how you debugged a problem
   - Discuss one design decision

3. **Peer Feedback** (5 min):
   - Peers write encouraging and constructive comments
   - Use structured form: "What worked well? What surprised you? One suggestion for improvement?"
   - Share feedback with team

4. **Individual Reflection** (Written, ~500 words):
   - Describe your final project and what it does
   - Analyze: Which programming concepts did you use? Why?
   - Reflect: What was the biggest challenge? How did you solve it?
   - Evaluate: On a scale 1-10, how successful was your project? Why?
   - Project: If you had more time, what would you add or change?
   - Synthesize: What's the most important thing you learned in Module 1?

### Assessment

**Project Rubric** (50 points total)

**Design & Planning** (10 points)
- Problem understanding (3 pts): Clear problem statement, well-scoped
- Function design (4 pts): Appropriate functions, reusable code, good separation
- Pseudocode (3 pts): Clear structure, logical flow

**Implementation** (15 points)
- Code quality (5 pts): Clean, readable, well-commented, no syntax errors
- Functionality (7 pts): Program runs, achieves stated goal, handles normal cases
- Robustness (3 pts): Handles edge cases, error recovery, graceful failures

**Testing & Debugging** (10 points)
- Unit testing (3 pts): Each function tested independently
- Integration testing (4 pts): Tested as complete system, multiple runs
- Problem-solving (3 pts): Evidence of debugging, iteration, adaptation

**Documentation & Presentation** (10 points)
- Code documentation (3 pts): Docstrings, comments, clear naming
- Written documentation (4 pts): README, test log, lessons learned
- Presentation (3 pts): Clear explanation, confidence, answers to questions

**Reflection** (5 points)
- Honest self-assessment (2 pts): Realistic evaluation of success
- Learning insights (3 pts): Thoughtful analysis of programming concepts learned

## Differentiation

**For struggling students**:
- Assign Option A (Polygon Artist) with pre-written helper functions
- Provide code skeleton with blanks to fill
- Work in team with stronger programmer (assign documentor/tester role)
- Offer simplified version: Draw 2 shapes instead of 5
- Extend deadline by 1-2 days

**For advanced students**:
- Encourage Option C (Sensor-based) or custom project
- Challenge: Optimize code for performance (minimums loops, efficient algorithms)
- Research: Implement complex algorithms (star polygon, fractal, recursive patterns)
- Leadership: Lead a team, mentor struggling students, do code review
- Extension: Add features not in requirements (logging, parameter validation, etc.)

## Materials & Code Examples

### Project Template (Polygon Artist)
```python
"""
Module 1 Final Project: Geometric Art Creator
Team: [Names]
Description: Draws a series of geometric shapes to create abstract art
"""

from XRPLib.differential_drive import DifferentialDrive
import time

drivetrain = DifferentialDrive.get_default_differential_drive()

def draw_polygon(num_sides, size, effort):
    """Draw a regular polygon."""
    angle = 360 / num_sides
    for i in range(num_sides):
        drivetrain.straight(size, max_effort=effort)
        drivetrain.turn(angle, max_effort=effort)

def main():
    """Create geometric art."""
    print("Starting Geometric Art Creator...")
    
    # Concentric shapes
    draw_polygon(3, 30, 0.5)  # Triangle
    time.sleep(1)
    draw_polygon(4, 30, 0.5)  # Square
    time.sleep(1)
    draw_polygon(6, 25, 0.5)  # Hexagon
    
    print("Art complete!")

if __name__ == "__main__":
    main()
```

### Project Template (Navigation)
```python
"""
Module 1 Final Project: Autonomous Delivery Robot
Team: [Names]
Description: Navigate course, deliver to waypoints, return home
"""

from XRPLib.differential_drive import DifferentialDrive
import time

drivetrain = DifferentialDrive.get_default_differential_drive()

def navigate_to_waypoint(distance, angle):
    """Move to waypoint at distance and turn to angle."""
    drivetrain.straight(distance, max_effort=0.5)
    drivetrain.turn(angle, max_effort=0.5)
    return True

def main():
    """Main navigation sequence."""
    print("Starting delivery mission...")
    
    # Navigate waypoints
    navigate_to_waypoint(100, 90)
    print("Reached checkpoint 1")
    
    navigate_to_waypoint(75, -90)
    print("Reached checkpoint 2")
    
    print("Mission complete!")

if __name__ == "__main__":
    main()
```

## Teaching Notes
- **This is the capstone**: Emphasize the journey (Blockly → Python) students have completed
- **Collaboration is valuable**: Encourage team discussion, peer learning, shared responsibility
- **Process over perfection**: A "good enough" working program that was well-designed beats a "perfect" program that was hacked together
- **Celebrate effort**: Recognize problem-solving, iteration, debugging—not just final grade
- **Documentation matters**: Professional code is documented; encourage this habit early
- **Reflection is learning**: Written reflection is valuable for metacognition (thinking about thinking)

## Connections to Future Learning
- **Module 2**: Sensor-focused projects (line-following, obstacle avoidance)
- **Module 3**: Advanced control algorithms (PID, navigation planning)
- **Module 4**: Multi-robot coordination, swarm behaviors
- **Beyond course**: Computer science, robotics competitions, embedded systems, software engineering
