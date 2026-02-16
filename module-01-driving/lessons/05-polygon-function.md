# Lesson 5: The Polygon Function Challenge

## Overview
Students synthesize Lessons 2-4 to create a powerful, reusable Polygon function that draws ANY regular polygon. Given a number of sides and a side length, the function calculates the turn angle and draws the shape. This is a major milestone—students will have created a general-purpose geometric drawing tool and understand how one function can solve many problems.

## Learning Objectives
By the end of this lesson, students will be able to:
- Combine repeat loops, functions, and parameters to solve a complex problem
- Calculate interior and exterior angles for any regular polygon
- Implement angle calculation in Blockly using math blocks
- Test and debug a function across multiple test cases
- Explain how abstraction (polygon function) reduces code complexity

## Key Concepts
- **Angle formula**: Exterior angle = 360° ÷ number of sides
- **Regular polygon**: All sides equal, all angles equal
- **Function design**: One function, many test cases (square, triangle, pentagon, hexagon, etc.)
- **Modularity**: The polygon function is a building block for future designs
- **Math block**: Division operator in Blockly to calculate 360 ÷ sides
- **Test-driven development**: Write function, then test with multiple inputs

## Materials Required
- XRP Robot with large clear driving space (5m x 5m minimum)
- xrpcode.wpi.edu access
- Reference: Lessons 2-4 code (shapes, functions, parameters)
- Whiteboard for angle calculations (pre-calculated chart helpful)
- Rulers or measuring tape to verify robot shapes match expectations

## Lesson Flow

### Introduction & Design (10 minutes)
**For 50-min classes:** 7 min
**For 3-hour sessions:** 12-15 min

1. **Hook: The Power of Generalization**:
   - Show: Three separate functions (draw_square, draw_triangle, draw_pentagon) with 3-4 lines each
   - Ask: "What if the pattern continues? Draw_hexagon, draw_septagon, draw_octagon... How many functions?"
   - Introduce the problem: "Design ONE function that handles all regular polygons"

2. **Angle Math Review**:
   - Polygon property: Turn angles sum to 360°
   - Formula: Turn angle per side = 360° ÷ number of sides
   - Examples:
     - Square (4 sides): 360 ÷ 4 = 90°
     - Triangle (3 sides): 360 ÷ 3 = 120°
     - Hexagon (6 sides): 360 ÷ 6 = 60°
     - Octagon (8 sides): 360 ÷ 8 = 45°

3. **Function Signature Design**:
   - Discuss: What parameters do we need?
     - Number of sides (required)
     - Side length / distance (required)
     - Effort / speed (optional, default 0.5)
   - Proposed: `draw_polygon(sides, distance, effort)`
   - User story: "I want to call draw_polygon(8, 25, 0.5) and see the robot draw an octagon"

4. **Algorithm Planning**:
   - Pseudocode on board:
     ```
     function draw_polygon(sides, distance, effort):
         angle = 360 ÷ sides
         repeat sides times:
             straight(distance) at effort
             turn(angle°) at effort
     ```
   - Discuss: What are the three steps when drawing any shape? (Move, Turn, Repeat)

### Guided Practice: Building `draw_polygon()` (25 minutes)
**For 50-min classes:** 20 min
**For 3-hour sessions:** 30 min

1. **Create Function Definition**:
   - In Blockly, add a new function (Functions → "to do something")
   - Rename to "draw polygon"
   - Add three parameters using gear icon: sides, distance, effort
   - Function signature: "to draw polygon(sides, distance, effort)"

2. **Add the Repeat Loop**:
   - Inside the function, add: **Repeat (sides) times**
   - Explanation: "Repeat as many times as there are sides"

3. **Add Straight Command**:
   - Inside repeat: **Straight(distance)** at effort = effort
   - Explanation: "Each side travels the specified distance"

4. **Calculate and Add Turn Angle** (Most Complex Part):
   - Inside repeat, after Straight: **Turn (angle)** at effort = effort
   - But wait—we need to calculate the angle!
   - Show: **Math category → Division block**
   - Drag: **360 ÷ sides** into the Turn angle parameter
   - Result: Turn((360 ÷ sides)°) at effort

5. **Verify the Code Structure**:
   ```blockly
   "to draw_polygon(sides, distance, effort)"
   Repeat sides times:
       Straight(distance) at effort
       Turn(360 ÷ sides) at effort
   ```
   - Total lines of code: ~5 Blockly blocks
   - Covers: Squares, triangles, pentagons, hexagons, octagons, any n-gon

6. **Create the Main Program**:
   - Wait for button press
   - Call draw_polygon(4, 30, 0.5)  → Square
   - Call draw_polygon(3, 30, 0.5)  → Triangle
   - Call draw_polygon(6, 25, 0.5)  → Hexagon

7. **Test and Debug**:
   - Upload first square test only
   - Verify it draws a recognizable square before moving to multiple shapes
   - Check: Does the robot return to starting position? (Should, since 360° total turn)
   - Common issues:
     - Angle in degrees vs. radians (Blockly uses degrees, correct)
     - Accumulated rounding errors (acceptable for this activity)
     - Off-by-one errors (sides = 4 means 4 repeats ✓)

### Independent Practice: Polygon Tests (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

**Exercise 1: Test Different Polygons**
- Goal: Test draw_polygon with multiple shape types
- Test cases:
  1. Square (sides=4, distance=30, effort=0.5)
  2. Triangle (sides=3, distance=30, effort=0.5)
  3. Hexagon (sides=6, distance=20, effort=0.5)
  4. Octagon (sides=8, distance=15, effort=0.5)
- For each: Measure one side, verify angle math, check closure (returns to start)
- Observation: As sides increase, shapes approach circles

**Exercise 2: Scaling & Speed Variations**
- Goal: Use the same function with parameter variations
- Calls:
  - draw_polygon(4, 10, 0.3) → Small slow square
  - draw_polygon(4, 40, 0.7) → Large fast square
  - draw_polygon(6, 30, 0.5) → Medium hexagon
- Question: "Why does changing distance change size but not shape?" (Angles stay constant)

**Exercise 3: Challenge - Star Pattern**
- Goal: Creative extension—use polygon function to create a star or mandala
- Idea: Draw multiple polygons with rotating starting positions
- Example:
  ```
  Call draw_polygon(5, 20, 0.5)  → Pentagon
  Turn(72°)                       → Rotate halfway
  Call draw_polygon(5, 20, 0.5)  → Overlapping pentagon
  ```
- Result: 5-pointed star or mandala-like pattern
- Challenge: Predict the pattern before testing

**Exercise 4: Error Investigation (Teacher-Led Debrief)** **
- Scenario: Robot draws a hexagon, but it looks "off" (not quite closed or rotated)
- Debugging questions:
  1. Is the formula correct? (360 ÷ 6 = 60°? Yes)
  2. Are the parameters right? (sides=6 passed?)
  3. Could it be wheel slip or surface friction? (Possible—not code error)
  4. If effort is very low, is turning accurate? (Harder to turn precisely at low effort)
- Resolution: Test with medium effort (0.5) to isolate code issues from physics issues

### Assessment

**Formative (during lesson)**:
- Can students identify each parameter and its role?
- Do they understand the angle calculation formula and its implementation?
- Can they test the function with different inputs?
- Can they debug when results don't match predictions?

**Summative (worksheet/exit ticket)**:
1. What parameters does `draw_polygon()` need, and why?
2. Calculate: For a 12-sided polygon, what's the turn angle? (360 ÷ 12 = 30°)
3. Predict: If `draw_polygon(8, 25, 0.5)` draws an octagon 1.5m around, what would `draw_polygon(8, 50, 0.5)` do? (Octagon 3m around)
4. Explain: Why is `draw_polygon()` better than having separate functions for each shape?

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "I need to calculate angles manually for each shape" | The formula 360÷sides handles all polygons automatically |
| "Division in Blockly is hard" | Math blocks are straightforward; drag 360, drag ÷, drag sides |
| "More parameters make functions worse" | Three parameters (sides, distance, effort) balance flexibility with complexity |
| "The robot must be perfectly closed" | Minor gaps due to wheel slip or surface friction are acceptable; code is correct |
| "I can't test without the robot" | Blockly's "View Python" lets you check code logic before uploading |

## Differentiation

**For struggling students**:
- Provide a skeleton: `draw_polygon(sides, distance, effort)` with Repeat block in place
- Ask them to add just the Straight and Turn blocks
- Pre-calculate angles and provide on a reference card
- Work through one test case (square) with the whole group
- Simplify to two parameters first: `draw_polygon(sides, distance)` with effort = 0.5 fixed

**For advanced students**:
- Challenge: Modify to create a "spiral polygon" that gradually increases distance: 
  - Straight(distance) → Straight(distance + 5) → Straight(distance + 10)...
  - Results in spiral rather than closed shape
- Design task: Create a function `draw_star(points, size)` using polygon as a building block
- Research: Investigate how fractals work (Koch snowflake, Sierpinski triangle)
- Extension: Add a fourth parameter `repetitions` to draw the polygon multiple times with rotation

## Materials & Code Examples

### Blockly Polygon Function (Complete)
```blockly
[Functions category]
"to draw_polygon(sides, distance, effort)"
Repeat sides times:
    Straight(distance) at effort
    Turn(360 ÷ sides) at effort

[Main workspace]
Wait for button press
Call draw_polygon(4, 30, 0.5)
Wait 2 seconds
Call draw_polygon(3, 30, 0.5)
Wait 2 seconds
Call draw_polygon(8, 15, 0.5)
```

### Reference Test Cases with Expected Angles
| Sides | Shape | Angle | Notes |
|---|---|---|---|
| 3 | Triangle | 120° | 360 ÷ 3 |
| 4 | Square | 90° | 360 ÷ 4 |
| 5 | Pentagon | 72° | 360 ÷ 5 |
| 6 | Hexagon | 60° | 360 ÷ 6 |
| 8 | Octagon | 45° | 360 ÷ 8 |
| 12 | Dodecagon | 30° | 360 ÷ 12 |

### Python Equivalent (Reference for Teachers)
```python
def draw_polygon(sides, distance, effort):
    angle = 360 / sides
    for i in range(sides):
        drivetrain.straight(distance, max_effort=effort)
        drivetrain.turn(angle, max_effort=effort)

board.wait_for_button_press()
draw_polygon(4, 30, 0.5)  # Square
import time
time.sleep(2)
draw_polygon(3, 30, 0.5)  # Triangle
```

## Teaching Notes
- **Division precision**: Blockly division may return decimals (72.5 vs. 72°)—this is fine; robot can handle fractional degrees
- **Large polygons and space**: Polygons with many sides need less space (octagon with 15cm sides ≈ 2m diameter)
- **Time management**: Full test suite (4+ polygons) takes 10-15 minutes to run
- **Closure verification**: Have students mark starting point or use tape to verify robot returns to approximate start
- **Common errors**:
  - Forgetting angle calculation (hardcoding 90° only works for squares)
  - Using sides parameter for repeat count but forgetting it's also used in angle calculation  
  - Not resetting encoders between tests
- **Success criteria**: Function runs without errors, tests pass for at least 3 different polygon types, student can explain the angle formula

## Connections to Next Lessons
- Lesson 6 will introduce **Differential Drive** blocks—moving in straight lines and turning without the abstraction of `straight()` and `turn()`
- Lesson 7 will combine polygon function with more complex challenges (obstacles, multiple robots)
- Python Lesson 10 will implement the same polygon function in text syntax
