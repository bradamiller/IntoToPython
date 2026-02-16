# Lesson 3: Introduction to Functions

## Overview
Students learn to write reusable code using the Blockly **Function** block. Instead of repeating shape-drawing code multiple times, students create a function called `draw_square()` and call it whenever needed. This introduces abstraction and modularity—core programming concepts.

## Learning Objectives
By the end of this lesson, students will be able to:
- Understand what a function is (reusable block of code)
- Define a function using the **"to do something"** Blockly block
- Call a function from the main program
- Recognize when to use functions (reducing repeated code)
- Explain the relationship between function definition and function calls

## Key Concepts
- **Function definition**: Code block that can be used multiple times (written once, called many times)
- **Function call**: Using the function in a program
- **Reusability**: Write Straight + Turn once in a function; call it multiple times
- **Abstraction**: Hide complexity; `draw_square()` hides the repeat loop and math
- **Function body**: Commands inside the function that run when the function is called
- **Blockly "to do something" block**: Creates a new custom block in the Functions palette

## Materials Required
- XRP Robot with clear driving space
- xrpcode.wpi.edu access
- Reference: Lesson 2 shapes code (square, triangle, pentagon)
- Whiteboard for pseudo-code planning

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 5 min
**For 3-hour sessions:** 10 min

1. **Hook: Code Duplication Problem**:
   - Show code that draws 3 squares in a row WITHOUT functions:
     ```
     Wait for button press
     Repeat 4 times: Straight(30) + Turn(90°)
     
     Repeat 4 times: Straight(30) + Turn(90°)
     
     Repeat 4 times: Straight(30) + Turn(90°)
     ```
   - Ask: "What's the problem?" 
   - Student responses: "It's long," "We wrote it 3 times," "Hard to change"
   
2. **Introduce Functions**:
   - Analogy: "A function is like a recipe card. Write the steps once, use the recipe as many times as you want."
   - Show the solution: Create a `draw_square()` function, then call it 3 times
   - Benefits: Shorter code, easier to fix bugs, reusable

3. **Function Terminology**:
   - **Definition**: "Here's what draw_square does" (write once)
   - **Call**: "Do draw_square now" (use as many times as needed)
   - **Body**: The code inside the function

### Guided Practice: Creating `draw_square()` Function (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 20-25 min

1. **Start with Lesson 2 Code**:
   - Open or recreate the square program from Lesson 2 in Blockly
   - Code is: Repeat(4) + Straight(30) + Turn(90°)

2. **Introduce the Function Block**:
   - Show the "Functions" category in the Blockly palette
   - Drag: **"to do something"** block onto the workspace
   - Explain: This creates a new custom block named "do something"
   - Have students rename it to "draw square" (click the text to edit)

3. **Move Code into the Function**:
   - Select the Repeat block (and its contents)
   - Drag it INSIDE the function definition block
   - Now the function body contains: Repeat(4) + Straight(30) + Turn(90°)

4. **Create the Main Program**:
   - In the main workspace (not inside the function), add:
     - **Wait for button press**
     - **Call draw square** (the new custom block appears in the Functions palette)
   - Show: The code is now much shorter and clearer

5. **Demo Running the Program**:
   - Upload to robot and test
   - Explain: When the robot reaches "call draw square", it jumps into the function, executes the repeat loop, draws a square, then returns to the main program

6. **Reflection**:
   - Ask: "Why did we put the repeat loop in the function?" (To reuse it)
   - "What happens if we want to change the square size?" (Edit the distance in ONE place, not three)

### Independent Practice: Reusable Shapes (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

**Exercise 1: Function for Triangle**
- Goal: Create a `draw_triangle()` function
- Steps:
  1. Create a function (rename to "draw triangle")
  2. Move the triangle code from Lesson 2 into the function body: Repeat(3) + Straight(25) + Turn(120°)
  3. Call this function from main (via button press)
  4. Test the robot
- Challenge: Add a second call to `draw_triangle()` after the first—what happens?

**Exercise 2: Multiple Shape Functions**
- Goal: Create THREE functions—`draw_square()`, `draw_triangle()`, `draw_pentagon()`
- Then call them in sequence:
  ```
  Wait for button press
  Call draw_square()
  Call draw_triangle()
  Call draw_pentagon()
  Call draw_square()
  ```
- Result: Robot draws a sequence of different shapes
- Question: "How would we change this program without functions?" (Very long and repetitive)
- Challenge: Add a `Wait (2 seconds)` between each shape call so we can see them clearly

### Assessment

**Formative (during lesson)**:
- Can students identify what should go in a function vs. the main program?
- Do they understand the difference between defining and calling a function?
- Can they rename and use custom blocks correctly?

**Summative (worksheet/exit ticket)**:
1. Circle the code that should be in a function (given a problem scenario)
2. Write the function name and the code it should contain
3. Predict: If we call `draw_square()` four times, how many total sides does the robot draw? (16)

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "Defining a function runs it" | Function definition is just setup; it only runs when called |
| "I can't change the function once I use it" | Modify the function code; ALL calls use the updated version |
| "Functions are only for long code" | Functions are useful for ANY repeated code, even 2-3 lines |
| "The function name has to match the code inside" | Function name is arbitrary—choose meaningful names for clarity |
| "I need to copy the function for each call" | Define once, call many times |

## Differentiation

**For struggling students**:
- Provide a partially completed program; ask them to move the loop into the function
- Work through Exercise 1 as a whole group before independent work
- Provide a template: "to draw_square do: [drag blocks here]"
- Limit to creating ONE function first, then demonstrate calling it

**For advanced students**:
- Challenge: Create 5 different shape functions (hexagon, octagon, star)
- Design task: Create a program that draws a pattern (e.g., square-triangle-square-triangle)
- Advanced exercise: Before coding, draw the sequence on paper and label each function
- Extension: Use a variable to control which shape is drawn (e.g., "if button = 1, draw_square; else draw_triangle")

## Materials & Code Examples

### Blockly Program Structure
```blockly
[Functions category]
"to draw_square"
├── Repeat 4 times
│   ├── Straight (30) at 0.5
│   └── Turn (90°) at 0.5

[Main workspace]
Wait for button press
Call draw_square
```

### Multiple Shapes Program
```blockly
[Functions category]
"to draw_square": ...
"to draw_triangle": ...
"to draw_pentagon": ...

[Main workspace]
Wait for button press
Call draw_square
Wait 2 seconds
Call draw_triangle
Wait 2 seconds
Call draw_pentagon
```

### Python Equivalent (Reference for Teachers)
The Blockly program generates:
```python
from XRPLib.differential_drive import DifferentialDrive
import time

drivetrain = DifferentialDrive.get_default_differential_drive()
board = Board.get_default_board()

def draw_square():
    for i in range(4):
        drivetrain.straight(30, max_effort=0.5)
        drivetrain.turn(90, max_effort=0.5)

def draw_triangle():
    for i in range(3):
        drivetrain.straight(25, max_effort=0.5)
        drivetrain.turn(120, max_effort=0.5)

board.wait_for_button_press()
draw_square()
time.sleep(2)
draw_triangle()
```

## Teaching Notes
- **Vocabulary**: Use "define" and "call" consistently; avoid confused language like "make" or "use"
- **Function naming**: Encourage descriptive names (`draw_square` is better than `function1`)
- **Abstraction level**: Don't overwhelm; start with ONE function, then add more
- **Testing strategy**: Test each function individually before combining them
- **Common error**: Students sometimes duplicate function definitions instead of calling—show them the Blockly palette has a "call" block
- **Success criteria**: Code is shorter, program runs without errors, robot draws expected shapes

## Connections to Next Lessons
- Lesson 4 will show how to make functions flexible using **Parameters** (e.g., one function for any square size)
- Lesson 5 will use functions with parameters to create the powerful **Polygon** challenge
- Functions are the bridge before Python functions in Lesson 10
