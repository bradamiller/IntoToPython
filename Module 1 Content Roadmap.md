# Module 1: Learning How to Drive the Robot — Content Development Roadmap

## Overview

This document outlines what content needs to be created for Module 1, in detail. It serves as a checklist and planning tool for building out all lessons, exercises, code examples, and templates.

---

## Content Checklist

### Phase A: Blockly Lessons (Lessons 1–5)
- [ ] Lesson 1: Meet the XRP (Hardware & Blockly intro)
- [ ] Lesson 2: Drawing Shapes (Sequencing, angles)
- [ ] Lesson 3: Functions in Blockly (Creating reusable blocks)
- [ ] Lesson 4: Parameters (Making functions flexible)
- [ ] Lesson 5: Polygon Function (360 ÷ sides logic)

### Phase B: Driving Challenges (Lessons 6–7)
- [ ] Lesson 6: Differential Drive and Circles
- [ ] Lesson 7: Driving Challenges (Basketball drills, parking)

### Phase C: Python Transition (Lessons 8–11)
- [ ] Lesson 8: Hello, Python (Blockly vs. Python side-by-side)
- [ ] Lesson 9: Loops in Python (`for`, `range()`)
- [ ] Lesson 10: Functions in Python (`def`, parameters)
- [ ] Lesson 11: Final Project (Polygon in Python)

### For Each Lesson
- [ ] Lesson plan (detailed or outline + both)
- [ ] Slide outline
- [ ] 2–3 exercises with descriptions
- [ ] Worksheets (algorithm tracing or calculations)
- [ ] Starter code for exercises
- [ ] Solution code for exercises

### Supporting Materials
- [ ] XRPLib API reference (✓ DONE)
- [ ] Module 1 README (✓ DONE)
- [ ] Code templates:
  - [ ] Hello World (drive forward + backward)
  - [ ] Shape drawing (square, triangle)
  - [ ] Polygon function template
  - [ ] Main program template

---

## Lesson Details & Content Requirements

### Lesson 1: Meet the XRP

**Goal:** Get comfortable with robot hardware; first Blockly program

**Duration:** ~50–60 minutes (adjusted for 3-hour class: ~25–30 min)

#### Content to Create

**Lesson Plan** should include:
- Objectives (3–4 bullet points)
- Key concepts (hardware parts, basic commands)
- Lesson flow (hardware tour 15 min, Blockly 25 min, exercise 15 min)
- Worked example: "Drive forward 30 cm and back" in Blockly (with screenshots)
- Exercise 1: Drive forward 20 cm, stop, beep
- Assessment idea: Robot drives forward correctly; student explains what each block does

**Slide Outline** should have:
- Title: "Meet the XRP"
- Slide 2: What is XRP? (2-wheeler, motors, sensors, controller board)
- Slide 3: Key parts (highlight motors, wheels, controller)
- Slide 4: Blockly blocks overview (drive, turn, wait, loop)
- Slide 5: First program walkthrough
- Slide 6: Key takeaway + next lesson preview

**Exercises** (2):
1. *Warm-up*: Drive forward 20 cm, back 20 cm, stop
2. *Challenge*: Drive forward, wait 2 seconds, beep, stop

**Worksheet** (optional): Diagram of robot labeling parts

**Code**:
- Starter: Blockly skeleton (just the "Start" and "Stop" blocks with drive/turn library)
- Solution: Full "drive forward and back" program in Blockly (visual blocks)

---

### Lesson 2: Drawing Shapes

**Goal:** Understand sequencing; draw shapes on whiteboard

**Duration:** ~50–60 minutes (25–30 min in 3-hour class)

#### Content to Create

**Lesson Plan**:
- Objectives: Sequence commands correctly; calculate exterior angles; use angles in Blockly
- Key concepts: Sequencing, 360° exterior angle logic, relative turns
- Lesson flow: Review turns/angles (10 min), draw square on paper (10 min), Blockly challenge (20 min)
- Worked example: Square (4 sides, 90° turns) with Blockly blocks shown
- Exercise 1: Draw a square (with or without help)
- Exercise 2: Draw a triangle (requires calculating 120° exterior angle)
- Assessment: Student draws both shapes; explains turn angles

**Slide Outline**:
- Title: "Drawing Shapes"
- Slide 2: What is an exterior angle? (diagram: explain 360÷4 = 90°)
- Slide 3: Square example (drive 30 cm, turn 90°, repeat 4 times)
- Slide 4: Triangle (drive 30 cm, turn 120°, repeat 3 times)
- Slide 5: Activity: Draw on whiteboard before coding
- Slide 6: From whiteboard to Blockly

**Exercises** (2):
1. Draw a square (30 cm sides, 90° turns)
2. Draw a triangle (30 cm sides, 120° exterior angle turns)

**Worksheet**: Worksheet with shape diagrams; students calculate angles for different polygons (pentagon, hexagon, etc.)

**Code**:
- Starter: Blockly with some blocks filled in (e.g., "drive 30 cm" and "turn" blocks, but student fills in angles and count)
- Solution: Full square and triangle programs

---

### Lesson 3: Functions in Blockly

**Goal:** Introduce the concept of functions; create a reusable triangle function

**Duration:** ~50–60 minutes (25–30 min in 3-hour class)

#### Content to Create

**Lesson Plan**:
- Objectives: Create functions in Blockly; call functions; understand reuse
- Key concepts: Functions, reuse, reducing repetition
- Lesson flow: Why functions? (10 min), make a triangle function (20 min), call it multiple times (15 min)
- Worked example: "draw_triangle()" function in Blockly
- Exercise 1: Create and call draw_triangle 3 times, each time the robot draws a triangle
- Assessment: Robot draws 3 triangles; student explains what the function does

**Slide Outline**:
- Title: "Functions—Write Once, Use Many Times"
- Slide 2: Why functions? (avoid repeating code)
- Slide 3: How to create a function in Blockly (show "Make a Block" option)
- Slide 4: Triangle function anatomy
- Slide 5: Calling a function—how to reuse it
- Slide 6: Activity: Make your own function

**Exercises** (2):
1. Create a draw_triangle() function; call it 3 times
2. *Stretch*: Create a draw_square() function; call both square and triangle in one program

**Worksheet**: Pseudocode worksheet – "Write in English what the function should do before building in Blockly"

**Code**:
- Starter: Blockly skeleton with function definition started
- Solution: Full function definition + calls

---

### Lesson 4: Parameters

**Goal:** Make functions flexible by adding parameters

**Duration:** ~50–60 minutes (25–30 min in 3-hour class)

#### Content to Create

**Lesson Plan**:
- Objectives: Add parameters to functions; pass values into functions; understand flexibility
- Key concepts: Parameters, arguments, function flexibility
- Lesson flow: What are parameters? (10 min), modify triangle function to take a size parameter (20 min), call with different sizes (15 min)
- Worked example: triangle_with_size(size_in_cm) in Blockly
- Exercise 1: Modify draw_triangle to accept a "size" parameter; call with 20, 30, 40 cm
- Assessment: Robot draws 3 triangles of different sizes

**Slide Outline**:
- Title: "Parameters—Making Functions Flexible"
- Slide 2: What are parameters? (inputs to a function)
- Slide 3: Triangle with size parameter (pseudocode)
- Slide 4: How to add parameters in Blockly ("create variable" approach + function input)
- Slide 5: Calling with different arguments
- Slide 6: Activity: Try different sizes

**Exercises** (2):
1. Create draw_triangle(size) with one parameter; call 3 times with different sizes
2. *Stretch*: Create draw_square(size) with parameter; call both functions with same size

**Worksheet**: Worksheet with examples – "If I call draw_triangle(10), draw_triangle(20), what will happen?"

**Code**:
- Starter: Blockly function with parameter skeleton
- Solution: Full parameterized function + calls

---

### Lesson 5: Polygon Function (Generalization)

**Goal:** Generalize to any polygon (n sides)

**Duration:** ~50–60 minutes (25–30 min in 3-hour class)

#### Content to Create

**Lesson Plan**:
- Objectives: Understand polygon generalization; use `sides` as a parameter; grasp the power of abstraction
- Key concepts: Generalization, calculation (360÷sides), loops within functions
- Lesson flow: How to generalize (10 min), polygon function logic (20 min), call for triangle/square/pentagon/hexagon (15 min)
- Worked example: polygon(sides, size) in Blockly with calculation of turn angle
- Exercise 1: Create polygon(sides, size); call for 3, 4, 5, 6 sides
- Exercise 2: *Bonus*: Draw multiple different polygons in sequence with one function
- Assessment: Robot draws 4 different shapes using one function

**Slide Outline**:
- Title: "The Power of Generalization—The Polygon Function"
- Slide 2: One function for all shapes (triangle, square, pentagon, …)
- Slide 3: The math: 360 ÷ sides = turn angle per side
- Slide 4: Polygon function in pseudocode
- Slide 5: How to use it: polygon(4, 30) for square, polygon(5, 20) for pentagon
- Slide 6: Activity: Draw multiple shapes with one function

**Exercises** (2):
1. Create polygon(sides, size) function; call for sides=3,4,5,6
2. Create a main program that calls polygon 4+ times to draw different shapes

**Worksheet**: Worksheet – "For each call, calculate the turn angle using 360÷sides"
- polygon(3, 30) → turn angle = ?
- polygon(6, 15) → turn angle = ?
- etc.

**Code**:
- Starter: Blockly function skeleton with loop
- Solution: Full polygon function + main program calling it multiple times

---

### Lesson 6: Differential Drive and Circles

**Goal:** Understand differential steering; draw circles

**Duration:** ~50–60 minutes

#### Content to Create

**Lesson Plan**:
- Objectives: Understand how two wheels with different speeds create curves; draw circles
- Key concepts: Differential drive, wheel speed ratio, curves vs. circles
- Lesson flow: How differential drive works (15 min), experiment with speed ratios (20 min), draw circles (15 min)
- Worked example: Left/right motor speed commands creating a circle
- Exercise 1: Drive a circle by setting wheel speeds
- Exercise 2: Draw circles of different sizes by varying speed ratio
- Assessment: Robot draws a recognizable circle without drifting off

**Slide Outline**:
- Title: "Differential Drive & Circles"
- Slide 2: How two wheels create direction (diagram: left slow, right fast → turn right)
- Slide 3: Same speed = straight; different speeds = curve
- Slide 4: Drawing circles (constant speed ratio)
- Slide 5: Speed ratio math (if left=50%, right=30%, robot turns right)
- Slide 6: Activity: Experiment with speed ratios

**Exercises** (2):
1. Draw a circle by setting left/right motor speeds
2. Draw circles of different sizes by changing speed ratios

**Worksheet**: Worksheet – "Predict the direction: Left motor at X, right motor at Y, which way will robot turn?"

**Code**:
- Starter: Blockly with set_effort blocks and loop duration/distance
- Solution: Circle-drawing program with adjustable speed ratios

---

### Lesson 7: Driving Challenges

**Goal:** Apply skills to precision challenges

**Duration:** ~50–60 minutes

#### Content to Create

**Lesson Plan**:
- Objectives: Precise driving; sequential challenges; debugging on hardware
- Key concepts: Precision, timing, testing on hardware
- Lesson flow: Intro challenges (5 min), basketball drill 1 (20 min), parking challenge (25 min)
- Worked example: Drive forward 30 cm, stop, back up 30 cm
- Exercise 1: Basketball drill—drive 30, back 30; drive 40, back 40; drive 50, back 50
- Exercise 2: Parking challenge—drive forward, turn, park in a space
- Assessment: Students demonstrate challenges working correctly

**Slide Outline**:
- Title: "Precision Driving Challenges"
- Slide 2: Challenge 1—Basketball Drills
- Slide 3: Challenge 2—Parking
- Slide 4: How to debug (measure actual vs. expected distance)
- Slide 5: Tips for precise driving
- Slide 6: Activity: Try both challenges

**Exercises** (2):
1. Basketball drill: drive 30, back 30; then 40, back 40; then 50, back 50
2. Parking: drive to a "parking spot" within a marked area

**Worksheet**: None (hands-on only)

**Code**:
- Starter: Blockly with some distances filled in
- Solution: Full programs for both challenges

---

### Lesson 8: Hello, Python

**Goal:** Introduction to Python; transition from Blockly

**Duration:** ~50–60 minutes (25–30 min in 3-hour class)

#### Content to Create

**Lesson Plan**:
- Objectives: Read and understand Python syntax; understand how Blockly blocks map to Python code; write first Python program
- Key concepts: Syntax, indentation, functions (from libraries), print()
- Lesson flow: Python intro (15 min), Blockly↔Python comparison (20 min), write hello world + drive (15 min)
- Worked example: "drive forward 30 cm" in Blockly vs. Python side-by-side
- Exercise 1: Rewrite "drive forward and back" in Python (with starter code)
- Exercise 2: Print messages to debug; use print() to show what's happening
- Assessment: Python program runs; robot drives forward and back correctly

**Slide Outline**:
- Title: "Hello, Python"
- Slide 2: What is Python? Text-based programming language
- Slide 3: Blockly block → Python code mapping (3–4 examples)
- Slide 4: Syntax rules (indentation, colons, capitalization)
- Slide 5: How to import XRPLib (from XRPLib.differential_drive import DifferentialDrive)
- Slide 6: First Python program walkthrough
- Slide 7: Debugging with print()
- Slide 8: Activity: Write your first Python program

**Exercises** (2):
1. Rewrite the "drive forward and back" program from Lesson 1 in Python
2. Add print() statements to show progress ("Driving forward", "Driving back", "Done!")

**Worksheet**: Side-by-side Blockly blocks vs. Python code; students match them

**Code**:
- Starter: Python skeleton with imports and basic structure
```python
from XRPLib.differential_drive import DifferentialDrive

drivetrain = DifferentialDrive.get_default_differential_drive()

# Your code here
drivetrain.straight(30)
drivetrain.straight(-30)

print("Done!")
```
- Solution: Full program with print statements

---

### Lesson 9: Loops in Python

**Goal:** Understand for loops and range(); rewrite square/polygon in Python

**Duration:** ~50–60 minutes

#### Content to Create

**Lesson Plan**:
- Objectives: Write for loops; understand range(); iterate correctly; rewrite Blockly repeat logic in Python
- Key concepts: for loops, range(), iteration, indentation
- Lesson flow: How loops work (15 min), for and range() explained (15 min), practice (15 min)
- Worked example: "for i in range(4): ... draw side, turn"
- Exercise 1: Draw a square using a for loop (4 sides with fixed distance/angle)
- Exercise 2: Draw multiple different shapes in sequence using nested loops
- Assessment: Square is drawn correctly; logic is sound

**Slide Outline**:
- Title: "Loops in Python—The for Loop"
- Slide 2: What is a loop? (repeat without rewriting)
- Slide 3: Blockly repeat block → Python for loop
- Slide 4: range() function (range(4) = 0,1,2,3)
- Slide 5: for loop anatomy and indentation
- Slide 6: Worked example: Draw a square with for loop
- Slide 7: Activity: Try drawing different shapes

**Exercises** (2):
1. Draw a square (4 sides, 30 cm, 90° turns) using a for loop
2. Draw a triangle and square in sequence, each using a separate for loop

**Worksheet**: Fill-in-the-blank for loops; trace execution by hand

**Code**:
- Starter: Python with for loop skeleton
```python
drivetrain = DifferentialDrive.get_default_differential_drive()

for i in range(4):
    # Your code here
    drivetrain.straight(30)
    # Turn 90°
```
- Solution: Full square-drawing program

---

### Lesson 10: Functions in Python

**Goal:** Write functions in Python; understand def, parameters, return

**Duration:** ~50–60 minutes

#### Content to Create

**Lesson Plan**:
- Objectives: Write Python functions; call functions with arguments; understand function organization
- Key concepts: def, parameters, function calls, code reuse
- Lesson flow: Functions review (10 min), Python functions explained (15 min), practice (20 min)
- Worked example: `def draw_square(size):` with side-by-side Blockly comparison
- Exercise 1: Write draw_triangle(size) function; call it 3 times
- Exercise 2: Write polygon(sides, size) function; call for different shapes
- Assessment: Functions work correctly; code is organized

**Slide Outline**:
- Title: "Functions in Python"
- Slide 2: What is a function? (named block of code you can reuse)
- Slide 3: Blockly function → Python def
- Slide 4: Function anatomy (def, parameters, indentation, body, call)
- Slide 5: Parameters vs. arguments
- Slide 6: Worked example: draw_triangle(size)
- Slide 7: Activity: Write your own function

**Exercises** (2):
1. Create draw_triangle(size) function; call with 20, 30, 40
2. Create draw_polygon(sides, size) function; call for 3,4,5,6 sides

**Worksheet**: Match function definitions to function calls; trace execution

**Code**:
- Starter: Python function skeleton
```python
def draw_square(size):
    # Your code here
    for i in range(4):
        drivetrain.straight(size)
        drivetrain.turn(90)

# Call the function
draw_square(30)
```
- Solution: Full parameterized functions for multiple shapes

---

### Lesson 11: Final Project

**Goal:** Bring it all together; create a complete program using polygon function

**Duration:** ~50–60 minutes (this may span multiple class sessions)

#### Content to Create

**Lesson Plan**:
- Objectives: Write a complete program combining functions, loops, and parameters; demonstrate to class
- Key concepts: Program organization, function decomposition, main program
- Lesson flow: Review requirements (5 min), building time (40 min), testing (10 min)
- Worked example: Complete polygon drawer with multiple shapes
- Exercise: Final Project—A main program that:
  1. Imports XRPLib
  2. Defines draw_polygon(sides, size)
  3. Calls draw_polygon with at least 4 different shapes
  4. Uses print() to describe what it's doing
  5. Runs without errors on the robot
- Assessment: Program runs; at least 4 shapes drawn; code is readable

**Slide Outline**:
- Title: "Module 1 Final Project"
- Slide 2: Project requirements (4+ shapes, organized code, comments)
- Slide 3: Program organization (imports, function defs, main code)
- Slide 4: Example skeleton
- Slide 5: Debugging tips
- Slide 6: Presentation prep

**Project Requirements**:
```
Write a Python program that:
- Imports XRPLib.DifferentialDrive
- Defines a draw_polygon(sides, size) function
- In main code, calls draw_polygon at least 4 times with different sides/sizes
- Includes print() statements showing progress
- Runs on the robot without errors
- Draws recognizable shapes on the whiteboard

Example calls:
- draw_polygon(3, 30)   # Triangle
- draw_polygon(4, 25)   # Square
- draw_polygon(5, 20)   # Pentagon
- draw_polygon(6, 15)   # Hexagon
```

**Rubric** (for grading):
- [ ] Code runs without errors (10 pts)
- [ ] draw_polygon function correctly calculates angle and uses loop (20 pts)
- [ ] At least 4 correct function calls (20 pts)
- [ ] Code is organized and readable (10 pts)
- [ ] print() statements included (5 pts)
- [ ] Robot draws recognizable shapes (20 pts)
- [ ] Bonus: Interesting extension or creative addition (5 pts)

**Code**:
- Starter: Skeleton with imports, function definition stub, and main program outline
```python
from XRPLib.differential_drive import DifferentialDrive

drivetrain = DifferentialDrive.get_default_differential_drive()

def draw_polygon(sides, size):
    # Your code here

# Main program
print("Starting polygon drawer...")
# Your calls to draw_polygon here

print("All done!")
```
- Solution: Full program drawing multiple shapes

---

## Supporting Code Templates to Create

For easier student setup and to ensure consistency:

1. **hello_world.py** — Simplest program (drive forward, stop)
```python
from XRPLib.differential_drive import DifferentialDrive

drivetrain = DifferentialDrive.get_default_differential_drive()
drivetrain.straight(30)
print("Done!")
```

2. **square_with_loop.py** — Using a for loop
```python
drivetrain = DifferentialDrive.get_default_differential_drive()

for i in range(4):
    drivetrain.straight(30)
    drivetrain.turn(90)
```

3. **polygon_function.py** — Full parameterized function
```python
def draw_polygon(sides, size):
    angle = 360 / sides
    for i in range(sides):
        drivetrain.straight(size)
        drivetrain.turn(angle)

draw_polygon(4, 30)  # Square
draw_polygon(3, 25)  # Triangle
```

4. **main_program_template.py** — Full structure with organization

---

## Blockly vs. Python Mapping Table

Create a reference document showing:
- Blockly "Drive" block → `drivetrain.straight(distance)`
- Blockly "Turn" block → `drivetrain.turn(degrees)`
- Blockly "Repeat" block → `for i in range(n):`
- Blockly "function" block → `def function_name(params):`
- etc.

---

## Implementation Priority

**Phase 1 (Foundation):**
1. Lesson 1 plan + slides + exercises + code
2. Lesson 8 plan + slides + exercises + code (Python intro)

**Phase 2 (Blockly):**
3. Lessons 2-5 (shape drawing, functions, parameters, generalization)
4. Lessons 6-7 (advanced driving challenges)

**Phase 3 (Python & Integration):**
5. Lessons 9-11 (loops, functions, final project)
6. Blockly ↔ Python mapping guide

**Phase 4 (Polish):**
7. Worksheets for each lesson
8. Solution code review & testing
9. Module 1 assessment strategy document

---

## Notes for Content Creation

- **Pacing**: Remember this is meant for 1 3-hour class per week for 3-4 weeks, OR 45-min classes 3x/week
- **Blockly IDE**: Use XRP Code (xrpcode.wpi.edu) for all Blockly lessons; include screenshots for reference
- **Python IDE**: VS Code with XRPLib installed; include setup instructions
- **Hands-On Testing**: Assume every lesson will be tested on actual hardware; include debugging tips
- **Differentiation**: Provide "challenge" and "support" variants for each exercise
- **Code Comments**: All code should be heavily commented for learners
- **Learning Objectives**: Start each lesson with 3-4 clear, achievable objectives

---

## Files to Create

### Lesson Plans
- module-01-driving/lessons/01-meet-the-xrp.md
- module-01-driving/lessons/02-drawing-shapes.md
- ... (through 11)

### Slide Outlines
- module-01-driving/slides/01-meet-the-xrp-slides.md
- ... (through 11)

### Exercises
- module-01-driving/exercises/01-drive-forward-and-back.md
- modules-01-driving/exercises/02-drawing-shapes.md
- ... (multiple per lesson)

### Code
- module-01-driving/code/starter/hello_world.py
- module-01-driving/code/starter/draw_square_loop.py
- module-01-driving/code/starter/draw_polygon_function.py
- module-01-driving/code/starter/final_project_template.py
- (+ corresponding solution files)

### Worksheets
- module-01-driving/worksheets/01-robot-parts-labels.md
- module-01-driving/worksheets/02-angle-calculations.md
- ... (through 11)

---

**Total estimated content**: 
- 11 lesson plans (detailed guide)
- 11 slide outlines
- 22–33 exercises (2–3 per lesson)
- 11 worksheets
- 15–20 code files (starter + solutions)

This is substantial but doable! Start with Lessons 1 and 8 (two "bookends"), then fill in the middle.
