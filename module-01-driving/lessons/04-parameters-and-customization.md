# Lesson 4: Parameters & Customization

## Overview
Students learn to make functions flexible using **Parameters**. Instead of one function per shape size, students create a single function that accepts a parameter (like distance or effort) and adapts its behavior. This is the foundation for building a generalized Polygon function.

## Learning Objectives
By the end of this lesson, students will be able to:
- Understand what a parameter is (input variable for a function)
- Create a function with parameters in Blockly (using the gear icon)
- Pass values to a function when calling it
- Use parameter values inside the function body
- Recognize when parameters make code more flexible and reusable

## Key Concepts
- **Parameter**: Input to a function that changes its behavior
- **Argument**: The actual value passed to a function when calling it
- **Gear icon**: Used in Blockly to add parameters to a function definition
- **Scope**: Parameters only exist inside the function where they're defined
- **Default example**: `draw_square(size)` where `size` is the parameter
- **Flexibility**: One function with parameter = multiple functions with hardcoded values

## Materials Required
- XRP Robot with clear driving space
- xrpcode.wpi.edu access
- Reference: Lesson 3 function code (square, triangle, pentagon)
- Whiteboard for planning parameter values

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 5-7 min
**For 3-hour sessions:** 10-12 min

1. **Hook: Limitation Problem**:
   - Show Lesson 3 code with `draw_square()`, `draw_triangle()`, `draw_pentagon()`
   - Ask: "What if I want a BIG square? A tiny square? A medium square?"
   - Current solution: Write a new function for each size (draw_square_small, draw_square_medium, draw_square_big)
   - Problem: Lots of duplicate code, hard to maintain

2. **Introduce Parameters**:
   - Solution: "What if we give the function an instruction: 'draw a square with sides THIS long'?"
   - That instruction is a **parameter**
   - Analogy: "A recipe that says 'add THAT MUCH sugar' instead of 'add 1 cup sugar'"
   - Show: `draw_square(size)` where size is the parameter

3. **Parameter Terminology**:
   - **Parameter**: What the function requests (e.g., "I need a size")
   - **Argument**: The actual value passed (e.g., "Here's 30 cm")
   - **Variable**: The parameter acts like a variable inside the function

### Guided Practice: `draw_square(size)` Function (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 20-25 min

1. **Start from Lesson 3**:
   - Open the `draw_square()` function from Lesson 3
   - Code currently is: Repeat(4) + Straight(30) + Turn(90°)

2. **Add a Parameter**:
   - Show: Click the **gear icon** on the function definition block
   - A menu appears to add/remove parameters
   - Click **"Add Input"** and name it "size"
   - Now the function signature is: "to draw_square(size)"

3. **Use the Parameter in the Function**:
   - In the Straight block, replace the hardcoded `30` with the `size` variable
   - The block now reads: Straight(size) at 0.5 effort
   - Explanation: "Whatever size value is passed in, use it for the distance"

4. **Call the Function with Different Arguments**:
   - In the main program, replace "Call draw_square" with:
     - Call draw_square (size: 30)
     - Call draw_square (size: 50)
     - Call draw_square (size: 20)
   - Explanation: Each call passes a different size value

5. **Demo Running the Program**:
   - Upload to robot
   - Robot draws three squares: big (50cm), medium (30cm), small (20cm)
   - Discuss: Only ONE function, THREE different behaviors

6. **Reflection**:
   - "Without parameters, how many functions would we need?" (Three: draw_square_big, draw_square_medium, draw_square_small)
   - "With one parameter, how many functions do we need?" (One: draw_square)
   - "What if we wanted 10 different sizes?" (Still just one function!)

### Independent Practice: Flexible Functions (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

**Exercise 1: Triangle with Size Parameter**
- Goal: Modify `draw_triangle()` to accept a size parameter
- Steps:
  1. Open `draw_triangle()` from Lesson 3 (or create it now): Repeat(3) + Straight(25) + Turn(120°)
  2. Add a parameter named "size" using the gear icon
  3. Replace the hardcoded `25` with the `size` variable
  4. Call the function with different sizes: 20, 35, 50
- Result: Three triangles of different sizes
- Question: "Why are the shapes different sizes but still triangular?" (The angles stay the same—120°)

**Exercise 2: Effort Parameter**
- Goal: Create a function that accepts a "speed" parameter
- New function: `draw_square(size, speed)`
  - Parameters: size (distance) and speed (effort)
  - Body: Repeat(4) + Straight(size) + Turn(90°) at effort = speed
- Calls:
  - draw_square(30, 1.0) → Fast, big square
  - draw_square(30, 0.3) → Slow, big square
  - draw_square(50, 0.5) → Medium speed, bigger square
- Result: Program demonstrates flexibility in both dimensions

**Exercise 3: Challenge - Customizable Polygon**
- Goal: Create a function `draw_polygon(sides, size)` that draws any regular polygon
- Requirements:
  - Parameter 1: sides (number of sides)
  - Parameter 2: size (distance per side)
  - Angle calculation: Use a constant 360° divided by sides (requires advanced blocks)
  - This is a **preview** of Lesson 5
- Hint: Inside the function, use Repeat(sides) with Straight(size) and Turn(360/sides)
- Note: Blockly requires a Math / division block for 360/sides calculation

### Assessment

**Formative (during lesson)**:
- Can students identify and name parameters in a function?
- Do they understand the difference between defining and calling with parameters?
- Can they modify a function to accept a parameter and use it correctly?

**Summative (worksheet/exit ticket)**:
1. Look at `draw_square(size)`: If called with size=50, what distance will the robot drive in one side?
2. Write the parameter names needed for a function that draws shapes at different speeds and sizes
3. Given a function call `draw_triangle(40)`, what distance does each side travel?

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "Parameters and variables are the same" | Parameters are inputs; variables are storage—but parameters act like local variables |
| "I can use a parameter name from another function" | Parameter names are local; they only exist in their function scope |
| "More parameters = better function" | More parameters = more complex; balance flexibility with simplicity |
| "Parameters must always be numbers" | Parameters can be numbers, text, or even other values (advanced) |
| "I can change a parameter's value inside a function" | Some languages allow this, but best practice is to treat parameters as read-only |

## Differentiation

**For struggling students**:
- Provide a partially filled function with the parameter already added; ask them to use it
- Start with ONE parameter (size) before adding multiple
- Pre-draw examples of squares at different sizes on paper
- Provide a reference card: "Gear icon → Add Input → Type name → Use as variable"
- Offer a template: `draw_square(size) { Repeat(4) + Straight(size) + Turn(90) }`

**For advanced students**:
- Challenge: Create a function `draw_rectangle(length, width)` with two parameters
  - Calls: 4 sides in a rectangle pattern
  - Parameters: length (long sides) and width (short sides)
- Design task: Create a function for MULTIPLE shapes: `draw_shape(shape_type, size)`
  - Requires if/then logic (preview of Lesson 5)
  - Calls could be: draw_shape("square", 30) or draw_shape("triangle", 25)
- Data structure challenge: Create a program that stores shape data in a list and calls the function for each

## Materials & Code Examples

### Blockly Function with Parameters
```blockly
[Functions category]
"to draw_square (size)"
├── Repeat 4 times
│   ├── Straight (size) at 0.5
│   └── Turn (90°) at 0.5

[Main workspace]
Wait for button press
Call draw_square (size: 30)
Call draw_square (size: 50)
Call draw_square (size: 20)
```

### Two-Parameter Function
```blockly
[Functions category]
"to draw_square (size, effort)"
├── Repeat 4 times
│   ├── Straight (size) at (effort)
│   └── Turn (90°) at (effort)

[Main workspace]
Wait for button press
Call draw_square (size: 30, effort: 1.0)
Call draw_square (size: 30, effort: 0.3)
```

### Python Equivalent (Reference for Teachers)
```python
def draw_square(size, effort):
    for i in range(4):
        drivetrain.straight(size, max_effort=effort)
        drivetrain.turn(90, max_effort=effort)

board.wait_for_button_press()
draw_square(30, 1.0)  # Fast square
draw_square(30, 0.3)  # Slow square
draw_square(50, 0.5)  # Bigger medium-speed square
```

## Teaching Notes
- **Gear icon visibility**: Some students miss the gear icon; explicitly show where it is on the function block
- **Parameter naming**: Encourage meaningful names (size, effort, distance) over generic (x, y, a)
- **Order of parameters**: Point out that order matters—passing (50, 0.3) is different from (0.3, 50)
- **Testing**: Test with simple values first (10, 20, 30) before complex ones (45, 72)
- **Error messages**: If parameters are used incorrectly, Blockly may not generate valid Python—show error and debug together
- **Success criteria**: Function accepts parameters, uses them correctly, produces different results for different arguments

## Connections to Next Lessons
- Lesson 5 will combine parameters with logic to create the powerful **Polygon** function
- Lesson 6 introduces parameters in the context of a **Move** function (forward, backward, speed)
- Python functions in Lesson 10 will use the same parameter concepts, just with text syntax
