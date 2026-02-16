# Lesson 10: Python Functions

## Overview
Students learn to write reusable functions in Python, translating Blockly function blocks (Lesson 3) to Python `def` statements. This lesson emphasizes that Python functions follow the same principles as Blockly functions—define once, call many times—with the added power of parameters and return values. By the end, students will understand function design, parameter passing, and the importance of modularity in real code.

## Learning Objectives
By the end of this lesson, students will be able to:
- Write function definitions using `def` syntax
- Understand function scope and local variables
- Define and use parameters (function inputs)
- Call functions with arguments
- Return values from functions
- Design functions for reusability and clarity
- Recognize the advantages of modular code

## Key Concepts
- **Function definition**: `def function_name(param1, param2):`
- **Parameters**: Inputs to a function (local variables)
- **Arguments**: Actual values passed when calling a function
- **Return statement**: Optional output from a function
- **Scope**: Variables defined in functions only exist within function
- **Call syntax**: `function_name(arg1, arg2)`
- **Indentation**: Defines function body (like loops)
- **Docstrings**: Comments explaining function purpose (optional but recommended)

## Materials Required
- XRP Robot with clear driving space
- VS Code with Python installed
- XRPLib configured
- Reference: Lesson 3 Blockly function examples and Lesson 9 loop code
- Whiteboard for function design

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 7 min
**For 3-hour sessions:** 10-12 min

1. **Hook: Code Duplication Problem**:
   - Show repetitive code without functions:
     ```python
     # Draw square 3 times
     for i in range(4):
         drivetrain.straight(30)
         drivetrain.turn(90)
     
     for i in range(4):
         drivetrain.straight(30)
         drivetrain.turn(90)
     
     for i in range(4):
         drivetrain.straight(30)
         drivetrain.turn(90)
     ```
   - Ask: "What's wrong with this?" (Repeated code, hard to modify)

2. **Introduce Functions**:
   - Solution: Extract into a function and call it
   - Analogy: "A function is a recipe card; write it once, use it many times"
   - Show the transformation:
     ```python
     def draw_square():
         for i in range(4):
             drivetrain.straight(30)
             drivetrain.turn(90)
     
     draw_square()
     draw_square()
     draw_square()
     ```

3. **Why Functions?**:
   - Reduces code duplication (DRY: Don't Repeat Yourself)
   - Makes code easier to understand (naming abstracts complexity)
   - Easier to maintain (fix in one place)
   - Enables testing (test each function independently)
   - Prepares for larger projects

4. **Function Terminology**:
   - **Definition**: Where we write what the function does
   - **Call**: Where we use the function
   - **Parameters**: Inputs to customize behavior
   - **Return**: Output that the function produces

### Guided Practice: `draw_square()` Function (18 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 20 min

1. **Basic Function Definition**:
   - Show structure:
     ```python
     def draw_square():
         """Draw a square with 30cm sides."""
         for i in range(4):
             drivetrain.straight(30)
             drivetrain.turn(90)
     ```
   - Explain each part:
     - `def`: Keyword meaning "define function"
     - `draw_square`: Function name (should be descriptive, lowercase with underscores)
     - `()`: Parameter list (empty for now)
     - `:`: Tells Python function body follows
     - Indentation: Function body (all indented code is inside function)
     - Docstring: Optional explanation (in triple quotes)

2. **Function Scope**:
   - Explain: Variables inside function only exist inside function
   - The loop variable `i` is local to the function
   - Code outside the function can't access `i`
   - This is good for organization (no accidental variable name collisions)

3. **Calling a Function**:
   - Show call syntax: `draw_square()`
   - Explain: When called, Python jumps to function definition, runs code, returns to caller
   - Can call multiple times: `draw_square()` repeated three times draws three squares
   - Demo with print statements:
     ```python
     def draw_square():
         print("Starting square")
         for i in range(4):
             drivetrain.straight(30)
             drivetrain.turn(90)
         print("Square complete")
     
     print("Before call")
     draw_square()
     print("After call")
     ```
   - Output shows order of execution

4. **Adding Parameters**:
   - Current problem: Can only draw 30cm squares
   - Solution: Add a `size` parameter
   - Code:
     ```python
     def draw_square(size):
         """Draw a square with sides of size cm."""
         for i in range(4):
             drivetrain.straight(size)
             drivetrain.turn(90)
     
     draw_square(30)
     draw_square(50)
     draw_square(20)
     ```
   - Explanation:
     - Parameter `size` is a local variable
     - Arguments (30, 50, 20) are passed when calling
     - Each call uses different size

5. **Multiple Parameters**:
   - Extend function to accept effort:
     ```python
     def draw_square(size, effort):
         """Draw a square with custom size and speed."""
         for i in range(4):
             drivetrain.straight(size, max_effort=effort)
             drivetrain.turn(90, max_effort=effort)
     
     draw_square(30, 0.5)  # Normal square
     draw_square(50, 0.7)  # Fast, big square
     draw_square(20, 0.3)  # Slow, small square
     ```
   - Explanation:
     - Order of parameters matters
     - Parameter names are arbitrary (document them in docstrings)
     - XRPLib methods accept parameters we can pass through

6. **Return Values**:
   - Functions can return data (optional)
   - Example: Function that calculates polygon angle
     ```python
     def calculate_angle(num_sides):
         """Calculate exterior angle for regular polygon."""
         return 360 / num_sides
     
     angle = calculate_angle(4)  # Gets 90
     print(f"Square angle: {angle}")
     ```
   - Explanation:
     - `return` keyword sends value back to caller
     - Function ends when `return` is reached
     - Return value can be assigned to variable or used directly

7. **Demo & Test**:
   - Build complete program with functions:
     ```python
     from XRPLib.differential_drive import DifferentialDrive
     
     drivetrain = DifferentialDrive.get_default_differential_drive()
     
     def draw_square(size, effort):
         for i in range(4):
             drivetrain.straight(size, max_effort=effort)
             drivetrain.turn(90, max_effort=effort)
     
     def draw_triangle(size, effort):
         angle = 360 / 3
         for i in range(3):
             drivetrain.straight(size, max_effort=effort)
             drivetrain.turn(angle, max_effort=effort)
     
     draw_square(30, 0.5)
     draw_triangle(30, 0.5)
     ```
   - Upload and run
   - Observe: Robot draws square then triangle

### Independent Practice: Function Design & Development (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

**Exercise 1: Generalized Polygon Function**
- Goal: Create a function that draws any regular polygon
- Requirements:
  ```python
  def draw_polygon(num_sides, size, effort):
      """Draw a regular polygon."""
      angle = 360 / num_sides
      for i in range(num_sides):
          drivetrain.straight(size, max_effort=effort)
          drivetrain.turn(angle, max_effort=effort)
  ```
- Tests:
  - `draw_polygon(4, 30, 0.5)` → Square
  - `draw_polygon(3, 25, 0.5)` → Triangle
  - `draw_polygon(6, 20, 0.5)` → Hexagon
- Challenge: Add a fourth parameter `rotation_offset` to start at different angles?

**Exercise 2: Helper Function with Return Value**
- Goal: Create a function that calculates distance traveled
- Code:
  ```python
  def calculate_distance(num_sides, side_length):
      """Calculate total perimeter of polygon."""
      return num_sides * side_length
  
  total = calculate_distance(4, 30)
  print(f"Square perimeter: {total} cm")
  ```
- Extensions:
  - Use this in main program: Draw polygon, then print its perimeter
  - Create similar function for circle circumference: `2 * 3.14159 * radius`

**Exercise 3: Function Using Another Function** (Composition)
- Goal: Create a function that calls another function
- Code:
  ```python
  def draw_two_shapes():
      """Draw a square and triangle."""
      draw_polygon(4, 30, 0.5)
      print("Square complete")
      draw_polygon(3, 25, 0.5)
      print("Triangle complete")
  
  draw_two_shapes()
  ```
- Explanation: Functions can call other functions (composition)
- Challenge: Create a function that draws 5 different polygons with varying sizes

**Exercise 4: Function with Default Parameters** (Advanced)
- Goal: Make parameters optional with default values
- Code:
  ```python
  def draw_square(size=30, effort=0.5):
      """Draw a square (defaults: 30cm, 0.5 effort)."""
      for i in range(4):
          drivetrain.straight(size, max_effort=effort)
          drivetrain.turn(90, max_effort=effort)
  
  draw_square()              # Uses defaults: (30, 0.5)
  draw_square(50)            # Size=50, effort=0.5 (default)
  draw_square(size=40, effort=0.7)  # Named arguments
  ```
- Explanation:
  - Parameters with `=` have default values
  - Optional to provide them when calling
  - Named arguments make calls more readable
- Challenge: Use defaults effectively to reduce function calls

**Exercise 5: Debugging Function Errors**
- Scenario: Given buggy code, identify and fix errors
  - Missing parameter in function definition
  - Wrong parameter name when calling
  - Indentation error in function body
  - Return statement in wrong place
- Students practice reading error messages and fixing syntax

### Assessment

**Formative (during lesson)**:
- Can students write correct function syntax?
- Do they understand the difference between definition and call?
- Can they use parameters and return values correctly?
- Can they design functions that are reusable and clear?

**Summative (worksheet/exit ticket)**:
1. Write a function `greet(name)` that prints "Hello, [name]!"
2. Write a function `add(a, b)` that returns the sum of two numbers
3. Write a function `draw_hexagon()` that uses the polygon function from Exercise 1
4. What's wrong with this code? (Identify 2 errors):
   ```python
   def multiply(x, y)  # Missing colon
       return x * y
   ```
5. Predict output:
   ```python
   def print_numbers(n):
       for i in range(n):
           print(i)
   
   print_numbers(3)
   ```

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "Variables in functions are global" | Function variables are local; only exist in function |
| "I must use parameters called 'x' and 'y'" | Parameter names are arbitrary; choose meaningful names |
| "A function must return a value" | Functions can return nothing (perform action); return is optional |
| "I can call a function before defining it" | Must define before calling (Python reads top to bottom) |
| "Parameters and arguments are the same" | Parameters are in definition; arguments are in calls |
| "More functions = more complex code" | Good functions simplify code |

## Differentiation

**For struggling students**:
- Start with NO parameters: Just `def draw_square():`
- Provide skeleton code with blanks to fill
- Use simple examples first: `def say_hello(): print("Hello")`
- Practice on paper (pseudocode) before coding in Python
- Use meaningful parameter names: `def draw_square(side_length):` not `def draw_square(x):`

**For advanced students**:
- Design a complete library of shape functions (square, triangle, pentagon, hexagon, star, spiral)
- Implement recursive functions (function that calls itself)
- Create a main menu: `def main():` that calls different shape functions based on user input
- Research and implement keyword-only arguments
- Explore function decorators (advanced Python feature)

## Materials & Code Examples

### Basic Function
```python
def draw_square():
    """Draw a square with 30cm sides."""
    for i in range(4):
        drivetrain.straight(30)
        drivetrain.turn(90)

draw_square()
```

### Function with Parameters
```python
def draw_square(size, effort):
    """Draw a square with custom size and speed."""
    for i in range(4):
        drivetrain.straight(size, max_effort=effort)
        drivetrain.turn(90, max_effort=effort)

draw_square(30, 0.5)
draw_square(50, 0.7)
```

### Function with Return Value
```python
def calculate_angle(num_sides):
    """Calculate exterior angle for polygon."""
    return 360 / num_sides

angle = calculate_angle(6)
print(f"Hexagon angle: {angle}°")
```

### Generalized Polygon Function
```python
def draw_polygon(num_sides, size, effort):
    """Draw any regular polygon."""
    angle = 360 / num_sides
    for i in range(num_sides):
        drivetrain.straight(size, max_effort=effort)
        drivetrain.turn(angle, max_effort=effort)

draw_polygon(4, 30, 0.5)   # Square
draw_polygon(3, 25, 0.5)   # Triangle
draw_polygon(8, 15, 0.5)   # Octagon
```

### Function with Default Parameters
```python
def draw_square(size=30, effort=0.5):
    """Draw a square with optional parameters."""
    for i in range(4):
        drivetrain.straight(size, max_effort=effort)
        drivetrain.turn(90, max_effort=effort)

draw_square()              # Uses both defaults
draw_square(50)            # Custom size, default effort
draw_square(size=40, effort=0.7)  # Both custom
```

## Teaching Notes
- **Syntax errors are common**: Show how error messages point to problems
- **Indentation consistency**: Use editor that enforces consistent indentation
- **Docstrings are valuable**: Even simple ones help future readers understand intent
- **Parameter naming**: Encourage `size` and `effort` over single letters
- **Testing functions**: Test each function independently with various inputs before combining
- **Common errors**:
  - Forgetting colon after function definition
  - Calling function before definition (order matters in Python)
  - Wrong number of arguments
  - Indentation errors in function body
- **Success criteria**: Functions defined and called correctly, parameters work, return values produce expected results

## Connections to Next Lessons
- **Lesson 11: Final Project** will combine functions, loops, conditionals, and sensor input
- **Advanced lessons** will use functions for sensor reading, motion planning, and control algorithms
- **Best practices**: This lesson introduces modularity principles used in all professional software
