# Lesson 4 Slide Outline: Parameters & Customization

## Slide 1: Title & Learning Objectives
**Title:** Parameters & Customization

**Learning Objectives:**
- Add parameters to functions
- Use parameters to customize function behavior
- Pass arguments when calling functions
- Understand parameter order matters

**Agenda:**
- Parameters vs. arguments (5 min)
- Adding parameters to functions (10 min)
- Guided: Create customizable function (10 min)
- Practice: Parameters in action (20 min)

---

## Slide 2: Hook - The Customization Problem
**Scenario:** You created `draw_triangle` in Lesson 3

**Question:** "What if you want to draw triangles of DIFFERENT SIZES?"

**Existing Problem:**
- `draw_triangle` always draws 25 cm sides
- To draw 50 cm triangle, need a NEW function: `draw_big_triangle`
- To draw 15 cm triangle, need ANOTHER function: `draw_small_triangle`
- This creates code duplication!

**Solution:** Parameters let ONE function be flexible

---

## Slide 3: Parameters vs. Arguments
**Parameter:**
- Placeholder in function definition
- "This function needs a SIZE value"
- Like a variable for the function

**Argument:**
- Actual value you pass when calling
- "Here's the size: 30"
- The value you provide

**Analogy:**
- **Parameter:** Recipe says "Add X cups of flour"
- **Argument:** When cooking, you decide X=2

**Code Example (Blockly):**
```
Define draw_triangle with parameter: size
  Repeat 3 times:
    Straight(size)          ← Uses parameter
    Turn(120)

Call draw_triangle with argument: 25   ← You provide value
Call draw_triangle with argument: 50   ← Different value, same function!
```

---

## Slide 4: Adding Parameters to Functions
**In Blockly:**

**Step 1:** Create Function → Name: `draw_triangle`

**Step 2:** Add "parameter" button
- Adds placeholder to function

**Step 3:** Name parameter: `size`

**Step 4:** Use `size` in blocks instead of fixed number
- Before: `Straight(25)`
- After: `Straight(size)`

**Result:** Function now accepts any size value

---

## Slide 5: Calling with Different Arguments
**Same function, different sizes:**

```
Call draw_triangle with argument: 25
Call draw_triangle with argument: 50
Call draw_triangle with argument: 15
```

**What Happens:**
- 1st call: `size=25` → draws 25cm triangle
- 2nd call: `size=50` → draws 50cm triangle
- 3rd call: `size=15` → draws 15cm triangle

**One function, three different triangles!**

---

## Slide 6: Multiple Parameters
**Add effort parameter for speed control:**

```
Define draw_triangle with parameters: size, effort
  Repeat 3 times:
    Straight(size, max_effort=effort)
    Turn(120, max_effort=effort)
```

**Now you can control:**
- **size:** How big the triangle is
- **effort:** How fast the robot moves

**Calling:**
```
Call draw_triangle with arguments: 25, 0.3
Call draw_triangle with arguments: 50, 0.8
```

---

## Slide 7: Parameter Order Matters
**Definition:**
```
Define draw_triangle with parameters: size, effort
```

**Calling (CORRECT):**
```
Call draw_triangle with: 30, 0.5
                         ↓   ↓
                       size effort
```

**Calling (WRONG):**
```
Call draw_triangle with: 0.5, 30
                         ↓    ↓
           effort where size goes! Disaster!
```

**Rule:** Arguments must match parameter order

**Real Example:**
- Correct: `draw_triangle(25, 0.5)` = 25cm triangle at 0.5 speed ✓
- Wrong: `draw_triangle(0.5, 25)` = tries to go 0.5cm at 25 effort ✗

---

## Slide 8: Parameter Types & Ranges
**Valid values for parameters:**

**Distance Parameters:**
- 0 to 1000 cm (typical robot distances)
- 25, 50, 75, 100 all reasonable

**Effort Parameters:**
- 0.0 to 1.0 (0% to 100% power)
- 0.3 (30%, slow), 0.7 (70%, fast)

**Angle Parameters:**
- 0 to 360 degrees
- 90, 120, 72 common for shapes

**Count Parameters:**
- Positive integers
- 3, 4, 5, 6 sides

---

## Slide 9: Flexible Shape Function
**Create a more general function:**

```
Define draw_shape with parameters: distance, effort
  Repeat 4 times:
    Straight(distance, max_effort=effort)
    Turn(90, max_effort=effort)
```

**Note:** Still draws squares (4 sides, 90° turn)

**Callsites:**
```
Call draw_shape with: 30, 0.5    ← 30cm square, slow
Call draw_shape with: 50, 0.8    ← 50cm square, fast
```

**Flexibility gains:**
- ✓ One function, many sizes
- ✓ One function, many speeds
- ✗ Still only draws squares

---

## Slide 10: Comparison: Fixed vs. Parameterized
**Without Parameters:**
```
Define draw_small_triangle:
  Repeat 3: Straight(20), Turn(120)

Define draw_medium_triangle:
  Repeat 3: Straight(35), Turn(120)

Define draw_large_triangle:
  Repeat 3: Straight(50), Turn(120)

Three functions, lots of duplication!
```

**With Parameters:**
```
Define draw_triangle with parameter: size
  Repeat 3: Straight(size), Turn(120)

Call draw_triangle with: 20
Call draw_triangle with: 35
Call draw_triangle with: 50

One function, infinite sizes!
```

---

## Slide 11: Common Misconceptions
**"Parameters are different than normal variables"**
- Not quite! Parameters ARE variables
- They're just defined in function header
- Scope limited to inside the function

**"I can rearrange argument order"**
- NO! Order is fixed by parameter order
- `draw_triangle(30, 0.5)` ≠ `draw_triangle(0.5, 30)`
- First argument always goes to first parameter

**"Parameters must be numbers"**
- True for robot functions (distances, angles, efforts)
- In advanced Python, could be text or other types

---

## Slide 12: Connection to Polygon Challenge (Lesson 5)
**Preview:**
- Today: Flexible triangle and square functions
- Next lesson: Even more flexible - POLYGON function
- `draw_polygon(sides, distance, effort)`
  - Draw ANY number of sides
  - With ANY distance
  - At ANY speed

**Teaser:** "With 3 parameters, you can draw infinite shapes!"
