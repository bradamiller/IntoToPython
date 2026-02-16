# Lesson 2: Drawing Shapes

## Overview
Students learn the basics of drawing geometric shapes using the DifferentialDrive and motion blocks in Blockly. This lesson introduces the core programming pattern: repeat loops combined with drive-and-turn commands to create polygons.

## Learning Objectives
By the end of this lesson, students will be able to:
- Understand how repeated actions create geometric shapes
- Use the **Repeat** block to automate repetitive commands
- Combine `straight()` and `turn()` commands in a loop
- Calculate turn angles for regular polygons (360° ÷ sides)
- Debug programs by modifying loop counts and angles

## Key Concepts
- **Polygon**: A closed shape with straight sides and vertices
- **Repetition**: Using loops to reduce code duplication
- **Angle calculation**:360° ÷ number of sides = degrees per turn
- **Blocky Repeat block**: Executes contained code N times
- **Effort parameter**: Controls robot speed (0.5 = 50% power, default)

## Materials Required
- XRP Robot (in clear space to drive)
- USB cable or wireless connection
- xrpcode.wpi.edu access
- Whiteboard/paper for angle calculations

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 5 min
**For 3-hour sessions:** 10 min

1. **Hook**: Ask students: "How does the robot draw a square?"
   - Discuss: What commands would be needed?
   - Introduce the relationship between distance and angle
   
2. **Geometry Review**: 
   - Show a square and explain: Move forward → Right angle turn → Repeat 4 times
   - Exterior angle calculation: 360° ÷ 4 sides = 90° per turn
   - Why 360°? Because a complete rotation is one full circle

3. **Introduce Repeat Block**:
   - Show the Blockly **Repeat** block: "repeat [4] times"
   - Explain: Instead of writing the same commands 4 times, write them once and repeat
   - Demo: Simple example—"repeat 4 times: print 'hello'" → prints "hello" 4 times

### Guided Practice: Square (15 minutes)
**For 50-min classes:** 10 min
**For 3-hour sessions:** 15-20 min

1. **Demonstrate Building a Square in Blockly**:
   - Start a new Blockly program
   - Drag: **Wait for button press** (to start safely)
   - Drag: **Repeat (4) times** block
   - Inside repeat, add:
     - **Straight (30cm)** at 0.5 effort
     - **Turn (90°)** at 0.5 effort
   - Show the code generates valid Python logic
   
2. **Explain Each Block**:
   - **Straight**: "Go forward this distance" (30cm = manageable size)
   - **Turn**: "Rotate in place by this angle" (90° = perfect right angle)
   - **Effort**: "Power level—0.5 = half speed for control"
   - **Repeat**: "Do these 4 things, 4 times"

3. **Test Prediction**:
   - Ask students: "What will the robot do? Trace it with your finger in the air."
   - Upload to robot and test
   - Celebrate success or debug together

4. **Reflection**:
   - Why does it make a square? (4 sides, 90° turns)
   - What if we changed 30 to 50? (Bigger square)
   - What if we changed to 3 repeats? (Incomplete loop—triangle shape)

### Independent Practice: Explore Shapes (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

**Exercise 1: Equilateral Triangle**
- Goal: Make the robot draw a triangle
- Scaffold: 
  - Hint 1: How many sides does a triangle have? (3)
  - Hint 2: 360° ÷ 3 = ? (120°)
  - Hint 3: Use Repeat (3) with Straight (25) and Turn (120°)
- Students modify the square program: Change repeat count to 3 and angle to 120°
- Optional extension: Try different distances—does shape stay the same?

**Exercise 2: Pentagon Challenge**
- Goal: Calculate and draw a pentagon (5-sided shape)
- Problem: What's the turn angle? (360° ÷ 5 = 72°)
- Students write: Repeat (5) with Straight (20) and Turn (72°)
- Challenge: Make a star pattern (repeat 5 times with larger turns)

### Assessment
**Formative (during lesson)**:
- Can students identify the repeat count for a shape? (e.g., triangle = 3)
- Do they understand angle = 360° ÷ sides?
- Can they modify a program and predict the outcome?

**Summative (worksheet/exit ticket)**:
1. Draw the shape that would result from: Repeat (6) with Straight (20) Turn (60°)
2. Write the repeat count and turn angle needed for an octagon (8 sides)
3. Sketch the path the robot would take for Exercise 2

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "360° is arbitrary" | 360° represents a complete rotation; any polygon loops back to start |
| "More sides = larger shape" | Number of sides doesn't affect size; distance per side does |
| "Turn angle = interior angle" | Turn angle = exterior angle = 360° ÷ sides (not interior angle) |
| "Effort affects shape" | Effort only affects speed; shape determined by distance and angle |
| "I need to write 4 separate commands for a square" | Repeat blocks eliminate code duplication |

## Differentiation

**For struggling students**:
- Provide a completed square program; ask them to modify one parameter at a time
- Pre-calculate angles on a reference card (30°, 45°, 60°, 72°, 90°, 120°)
- Offer shape templates with blanks: "Repeat (__) with Straight (__) Turn (__)"
- Start with 2D paper sketches before coding

**For advanced students**:
- Challenge: Create a star or hexagon (6 sides = 60° angles)
- Research: How would the program change if robot could strafe (move sideways)?
- Extension: Combine shapes—draw a square, then a triangle from the same starting point
- Design task: Create a flag or symbol that uses 3 different shapes

## Materials & Code Examples

### Blockly Square Program (Completed)
```blockly
[START block / Control Board]
└── Wait for button press
└── Repeat 4 times
    ├── Straight (30 cm) at effort 0.5
    └── Turn (90°) at effort 0.5
```

### Python Equivalent (Reference for Teachers)
The above Blockly program generates this Python:
```python
from XRPLib.differential_drive import DifferentialDrive

drivetrain = DifferentialDrive.get_default_differential_drive()
board = Board.get_default_board()

board.wait_for_button_press()

for i in range(4):
    drivetrain.straight(30, max_effort=0.5)
    drivetrain.turn(90, max_effort=0.5)
```

## Teaching Notes
- **Physical space**: Ensure the robot has at least 5m x 5m of clear space for larger shapes
- **Angle mistakes**: Most common error is confusing interior vs. exterior angles—emphasize "exterior angle = 360 ÷ sides"
- **Effort adjustment**: If the robot trembles or overshoots, reduce effort to 0.3; if very slow, increase to 0.7
- **Wheel slip**: If shapes are distorted, check robot alignment and surface friction (carpeted vs. smooth floor)
- **Success criteria**: Program runs without errors and creates recognizable shape within ±10% accuracy

## Connections to Next Lessons
- Lesson 3 will show how to extract shape-drawing into a reusable **Function** block
- Lesson 4 will introduce **Parameters** so one function can draw any regular polygon
- These shape-drawing patterns are the foundations for Lesson 5's Polygon Challenge
