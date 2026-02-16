# Lesson 5 Slide Outline: Polygon Function Challenge

## Slide 1: Title & Learning Objectives
**Title:** The Polygon Function Challenge

**Learning Objectives:**
- Generalize shape functions
- Use formula: angle = 360 ÷ sides
- Create one function for ANY polygon
- Understand abstraction and mathematical thinking

**Agenda:**
- Formula review (5 min)
- Generalized function design (10 min)
- Guided: Build polygon function (10 min)
- Challenge: Test & customize (20 min)

---

## Slide 2: Hook - The Ultimate Flexibility Goal
**Imagine:** A SINGLE function that draws EVERYTHING

**Current Situation (Lesson 4):**
```
draw_triangle(size, effort)     ← Only triangles
draw_square(size, effort)       ← Only squares
draw_pentagon(size, effort)     ← Only pentagons
draw_hexagon(size, effort)      ← Only hexagons
...
```

**Better Approach:**
```
draw_polygon(sides, size, effort)    ← ALL shapes!
```

**Question:** "How can we write ONE function for infinite shapes?"
**Answer:** Use the angle formula!

---

## Slide 3: The Angle Formula Deep Dive
**Key Insight from Lesson 2:**
```
Exterior Angle = 360° ÷ Number of Sides
```

**Why it works:**
- Any polygon's exterior angles sum to 360°
- Distribute equally: 360 ÷ sides

**Examples:**
- Triangle: 360 ÷ 3 = **120°** ✓ (120+120+120=360)
- Square: 360 ÷ 4 = **90°** ✓ (90+90+90+90=360)
- Pentagon: 360 ÷ 5 = **72°** ✓ (72×5=360)
- Octagon: 360 ÷ 8 = **45°** ✓
- Decagon: 360 ÷ 10 = **36°** ✓

**Universal Truth:** Works for ANY polygon (>3 sides)

---

## Slide 4: Generalizing the Pattern
**Old Triangle Function:**
```
Define draw_triangle with parameters: size, effort
  Repeat 3 times:
    Straight(size, max_effort=effort)
    Turn(120, max_effort=effort)
```

**Old Square Function:**
```
Define draw_square with parameters: size, effort
  Repeat 4 times:
    Straight(size, max_effort=effort)
    Turn(90, max_effort=effort)
```

**Pattern:**
- Repeat: Changes from 3 to 4 to 5...
- Turn angle: Changes from 120 to 90 to 72...
- BUT: Always equals 360 ÷ number of sides

**Key:** Make both "Repeat" and "turn angle" depend on sides parameter!

---

## Slide 5: The Generalized Function
**New Polygon Function:**

```
Define draw_polygon with parameters: sides, size, effort
  Calculate angle = 360 ÷ sides
  
  Repeat sides times:
    Straight(size, max_effort=effort)
    Turn(angle, max_effort=effort)
```

**Parameters:**
- **sides:** How many sides (3=triangle, 4=square, 5=pentagon...)
- **size:** How long each side
- **effort:** How fast to move

**Program Flow:**
1. Calculate what angle should be
2. Repeat that many sides
3. Each iteration: go forward, turn

---

## Slide 6: Building the Polygon Function
**Live Demo: Create from Scratch**

**In Blockly:**
1. Create Function → Name: `draw_polygon`
2. Add parameters: `sides`, `size`, `effort`
3. Add "Calculate angle = 360 ÷ sides" block (might be variable or custom block)
4. Repeat `sides` times:
   - Straight(size, effort)
   - Turn(angle, effort)

**Result:** Universal polygon drawer!

---

## Slide 7: Testing the Function
**Triangle Test:**
```
Call draw_polygon with: 3, 25, 0.5
                        ↓  ↓   ↓
                      sides size effort
→ Calculates: angle = 360÷3 = 120°
→ Repeats 3 times: Straight(25), Turn(120°)
→ Result: TRIANGLE ✓
```

**Pentagon Test:**
```
Call draw_polygon with: 5, 20, 0.5
→ Calculates: angle = 360÷5 = 72°
→ Repeats 5 times: Straight(20), Turn(72°)
→ Result: PENTAGON ✓
```

**Octagon Test:**
```
Call draw_polygon with: 8, 15, 0.7
→ Calculates: angle = 360÷8 = 45°
→ Repeats 8 times: Straight(15), Turn(45°)
→ Result: OCTAGON ✓
```

---

## Slide 8: Power of Abstraction
**What We've Achieved:**

| Shape | Old Way | New Way |
|-------|---------|---------|
| Triangle | Special function | `draw_polygon(3, ...)` |
| Square | Special function | `draw_polygon(4, ...)` |
| Pentagon | Special function | `draw_polygon(5, ...)` |
| Hexagon | Special function | `draw_polygon(6, ...)` |
| 20-sided | Would need new function | `draw_polygon(20, ...)` |

**Benefits:**
- ✓ One function instead of many
- ✓ Mathematical pattern (360÷sides) visible in code
- ✓ Infinite shapes possible
- ✓ Changes update everything (one source of truth)

**This is abstraction:** Hide complexity, expose simplicity

---

## Slide 9: Creative Challenge
**Program 1: Polygon Art**
```
draw_polygon(3, 30, 0.5)  ← Triangle
Straight(100)
draw_polygon(4, 25, 0.5)  ← Square
Straight(100)
draw_polygon(5, 20, 0.5)  ← Pentagon
```
Creates artistic polygon progression

**Program 2: Polygon Spiral**
```
Draw 3, 4, 5, 6, 7... sided polygons in sequence
Each slightly larger or offset
```

**Program 3: Polygon Star**
```
Combine multiple polygons at different angles
Create star or mandala pattern
```

---

## Slide 10: Debugging Parameter Mismatches
**Common Error 1: Sides too small**
```
Call draw_polygon with: 2, 30, 0.5
→ Angle = 360÷2 = 180°
→ Only repeats 2 times
→ Result: Straight line (not a polygon!)
Problem: Need minimum 3 sides for polygon
```

**Common Error 2: Angle calculation wrong**
```
Call draw_polygon with: 4, 25, 0.5
→ BUT: Turn(90°) NOT Turn(angle)
→ Draws square correctly by accident
→ But formula isn't used!
Problem: Must use calculated angle, not hardcoded
```

**Testing Strategy:**
- Test with triangle (you know it should be 120°)
- Test with square (verify it's 90°)
- Test with pentagon (verify it's 72°)
- Then trust formula for unknown shapes

---

## Slide 11: Mathematical Insights
**Why 360?**
- Degrees in full rotation (historical definition)
- One complete turn

**Why exterior angles work:**
- Walk around polygon, turn at each corner
- Complete walk = face original direction
- Total turning = 360°

**Inverse Relationship:**
- More sides → smaller exterior angle
- Triangle (3 sides): 120° (big turns)
- Octagon (8 sides): 45° (small turns)
- Circle (infinite sides): ~0° (nearly straight)

---

## Slide 12: Connection to Python Functions (Lesson 8-10)
**Preview:**
- Today: Blockly polygon function with calculation
- Lesson 8: Same function written in Python syntax
- Lesson 9: Python loops (for loops, range)
- Lesson 10: Python functions (def, parameters, return)

**Key Insight:** Same logic works in both Blockly and Python
```
Python version will use:
  angle = 360 / sides
  for i in range(sides):
      ...
```

**Teaser:** "The polygon function will get even smaller in Python!"
