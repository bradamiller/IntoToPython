# Lesson 10 Slide Outline: Python Functions

## Slide 1: Title & Learning Objectives
**Title:** Python Functions

**Learning Objectives:**
- Write function definitions using def syntax
- Use parameters and arguments
- Return values from functions
- Understand scope and variable lifetime
- Apply functions to robot programming

**Agenda:**
- Function syntax (5 min)
- Parameters & arguments (8 min)
- Guided: Build polygon function (8 min)
- Practice: Write custom functions (14 min)

---

## Slide 2: Hook - Code Organization with Python
**Blockly Functions (from earlier):**
```
Define draw_triangle:
  [Blocks...]

Call draw_triangle
Call draw_triangle  ← Reuses same code
```

**Python Same Concept:**
```python
def draw_triangle():
    drivetrain.straight(30)
    drivetrain.turn(120)

draw_triangle()  # Calls it
draw_triangle()  # Reuses it
```

**Question:** "Can you organize Python code into reusable chunks?"

---

## Slide 3: Function Definition Syntax
**Basic Python Function:**

```python
def function_name():
    # Code here runs when called
    print("Hello")
    drivetrain.straight(50)
```

**Breaking it down:**
- **def** - Keyword: define a function
- **function_name** - You choose the name (lowercase, underscores)
- **()** - Empty parentheses (we'll add parameters later)
- **:** - Colon ends the def line
- **Indented code** - Body of function

**Calling it:**
```python
function_name()      # Parentheses required!
```

---

## Slide 4: Function Parameters
**Function WITH parameters:**

```python
def draw_polygon(sides, distance):
    angle = 360 / sides
    
    for i in range(sides):
        drivetrain.straight(distance)
        drivetrain.turn(angle)
```

**Parameters:**
- **sides** - How many sides
- **distance** - Length of each side

**Calling with arguments:**
```python
draw_polygon(3, 25)   # Triangle, 25cm
draw_polygon(4, 30)   # Square, 30cm
draw_polygon(5, 20)   # Pentagon, 20cm
```

**Key Rules:**
- Parameter order matters
- Argument count must match parameter count
- Python = dynamic (arguments can be numbers OR variables)

---

## Slide 5: Blockly → Python Functions
**Blockly Definition:**
```
Define draw_triangle with parameter: size
  Repeat 3 times:
    Straight(size)
    Turn(120)

Call draw_triangle with argument: 25
```

**Python Equivalent:**
```python
def draw_triangle(size):
    for i in range(3):
        drivetrain.straight(size)
        drivetrain.turn(120)

draw_triangle(25)
```

**Translation:**
- Blockly: "Define ... with parameter" → Python: `def function(parameter):`
- Blockly: "Call ... with argument" → Python: `function(argument)`

---

## Slide 6: Multiple Parameters
**Three-Parameter Function:**

```python
def draw_polygon(sides, distance, effort):
    angle = 360 / sides
    
    for i in range(sides):
        drivetrain.straight(distance, max_effort=effort)
        drivetrain.turn(angle, max_effort=effort)
```

**Parameter meanings:**
- **sides** - Integer (3, 4, 5, ...)
- **distance** - Float (25, 50, 75)
- **effort** - Float 0-1 (0.3, 0.7, 1.0)

**Calling with different arguments:**
```python
draw_polygon(4, 30, 0.5)    # Slow square
draw_polygon(4, 30, 1.0)    # Fast square
draw_polygon(8, 20, 0.7)    # Medium octagon
```

---

## Slide 7: Return Values
**Functions can send back results:**

```python
def calculate_polygon_angle(sides):
    angle = 360 / sides
    return angle

my_angle = calculate_polygon_angle(5)
print(my_angle)     # Prints: 72.0

drivetrain.turn(my_angle)
```

**Breakdown:**
- **return** keyword - Send value back to caller
- Value after return - What gets sent back
- Function call becomes the value

**With multiple processing:**
```python
def is_valid_polygon(sides):
    if sides >= 3:
        return True
    else:
        return False

if is_valid_polygon(4):
    print("Valid polygon")
```

---

## Slide 8: Function Scope
**Variables exist only where defined:**

```python
def my_function():
    x = 10          # x only exists here
    print(x)        # ✓ Works

print(x)            # ✗ Error! x doesn't exist here
```

**Scope Rules:**
- **Local scope** - Variables inside function
- **Global scope** - Variables outside function
- **Function parameters** - Treated as local variables

**Example:**
```python
def draw_polygon(sides):
    angle = 360 / sides   # Local: angle exists here
    ...

draw_polygon(5)
print(angle)              # ✗ Error: angle not defined here!
```

---

## Slide 9: Function Design Best Practices
**Good Function:**
```python
def draw_square(size):
    """Draw a square with given side length"""
    for i in range(4):
        drivetrain.straight(size)
        drivetrain.turn(90)
```

**Features:**
- ✓ Clear name (verb: "draw_")
- ✓ Single responsibility (only draws square)
- ✓ Documented with docstring
- ✓ Takes relevant parameters
- ✓ Returns nothing (or meaningful value)

**Bad Function:**
```python
def do_stuff():                    # ✗ Vague name
    drivetrain.straight(30)
    my_variable = 50
    drivetrain.turn(my_variable)   # ✗ Magic numbers
    print("done")
```

---

## Slide 10: Common Function Errors
**Error 1: Mismatched arguments/parameters**
```python
def draw_polygon(sides, distance):
    ...

draw_polygon(4)      # ✗ Only 1 argument, needs 2
→ TypeError: missing 1 required positional argument
```

**Error 2: Returning from global scope**
```python
def my_function():
    x = 10
    return x

result = my_function()
print(x)             # ✗ x is local, not accessible here
```

**Error 3: Using wrong variable**
```python
def my_function():
    angle = 360 / sides    # ✗ sides doesn't exist
    ...

my_function()
```

**Fix:** Check parameter names match usage

---

## Slide 11: Python Function Best Practices
**Testing Small Functions:**
```python
def draw_square(size):
    for i in range(4):
        drivetrain.straight(size)
        drivetrain.turn(90)

# Test with different sizes
draw_square(20)
# Verify: robot draws 20cm square
draw_square(40)
# Verify: robot draws 40cm square
```

**Combining Functions:**
```python
def draw_square(size):
    for i in range(4):
        drivetrain.straight(size)
        drivetrain.turn(90)

def draw_art():
    draw_square(20)
    drivetrain.straight(100)
    draw_square(30)
    drivetrain.straight(100)
    draw_square(40)

draw_art()  # Calls draw_art, which calls draw_square multiple times
```

---

## Slide 12: Connection to Final Project (Lesson 11)
**Preview:**
- Today: Write individual functions
- Next lesson: Combine functions into full project
- Challenge: Design comprehensive program

**Python Program Structure (coming):**
```python
def draw_polygon(sides, distance):
    angle = 360 / sides
    for i in range(sides):
        drivetrain.straight(distance)
        drivetrain.turn(angle)

def create_artwork():
    draw_polygon(3, 30)
    move_forward(50)
    draw_polygon(4, 30)
    move_forward(50)
    draw_polygon(5, 30)

# Main program
create_artwork()
```

**Teaser:** "You've mastered loops AND functions. Now combine them in a capstone project!"
