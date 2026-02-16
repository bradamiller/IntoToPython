# Lesson 5 Worksheet: The Polygon Function Challenge

**Name:** __________________ **Date:** __________________ **Team:** __________________

## Part 1: Angle Formula Practice

Complete the table using the formula: **Turn Angle = 360° ÷ Number of Sides**

| Polygon | Number of Sides | Angle Calculation | Turn Angle | Check |
|---|---|---|---|---|
| Triangle | 3 | 360 ÷ 3 = | ___°  | ✓ |
| Square | 4 | 360 ÷ ___ = | 90° | ✓ |
| Pentagon | 5 | 360 ÷ ___ = | ___ ° | ✓ |
| Hexagon | 6 | 360 ÷ ___ = | ___ ° | ✓ |
| Heptagon | 7 | 360 ÷ ___ = | ~51° | ✓ |
| Octagon | 8 | 360 ÷ ___ = | ___ ° | ✓ |
| Decagon | 10 | 360 ÷ ___ = | ___ ° | ✓ |
| Dodecagon | 12 | 360 ÷ ___ = | ___ ° | ✓ |

## Part 2: Polygon Function Design

You're designing a function that draws ANY regular polygon. Fill in the blanks:

```
Function: draw_polygon(_______, _______, _______)
  angle = 360 ÷ _______
  Repeat _______ times:
    Straight(_______)
    Turn(_______ degrees)
```

**Parameter names and meanings:**
- Parameter 1: __________ (controls how many sides)
- Parameter 2: __________ (controls how long each side is)
- Parameter 3: __________ (controls how fast the robot moves)

## Part 3: Test Your Function

Predict what shape is created for each function call:

```
draw_polygon(3, 30, 0.5)   → Shape: ____________  Description: ________________

draw_polygon(4, 25, 0.5)   → Shape: ____________  Description: ________________

draw_polygon(6, 20, 0.5)   → Shape: ____________  Description: ________________

draw_polygon(8, 15, 0.5)   → Shape: ____________  Description: ________________

draw_polygon(5, 25, 0.7)   → Shape: ____________  Description: ________________
```

## Part 4: Predict & Verify

**Program A:**
```blockly
draw_polygon(4, 30, 0.5)
```

Draw your prediction of the shape:

[Drawing space]

**Measurement prediction:** Side length = _____ cm, Total perimeter = _____ cm

**After running on robot, actual measurements:**
Side length = _____ cm, Total perimeter = _____ cm

## Part 5: Parameter Variations

What happens when you change each parameter?

**Change sides from 4 to 6:**
- Shape changes from __________ to __________
- Same side length (30 cm), but has more sides
- Robot makes _____ turns instead of 4

**Change distance from 30 to 50:**
- Shape remains a __________
- But becomes a __________ square (50 cm per side instead of 30)
- Same _____ degree angles

**Change effort from 0.5 to 0.9:**
- Shape remains the same
- Robot moves __________ (faster / slower)
- The geometry doesn't change

## Part 6: Calculation Challenge

**A pentagon with 25cm sides:**
- Turn angle: 360 ÷ 5 = _____°
- Total perimeter: 5 × 25 = _____ cm
- Robot makes _____ full rotations (total turns = 360° × 1 = 360°)

**A decagon with 15cm sides:**
- Turn angle: 360 ÷ 10 = _____°
- Total perimeter: 10 × 15 = _____ cm
- Robot makes _____ full rotations

## Part 7: Real-World Application

If you wanted to create a square landing pad with 1-meter (100cm) sides:

**Code:**
```
draw_polygon(_____, _____, _____)
```

**Reasoning:**
- Number of sides needed: _____
- Side length: _____cm
- Effort (speed): _____ (your choice, explain why you chose it)

## Part 8: Debugging Challenge

These programs have errors. Fix them!

**Error 1:**
```blockly
draw_polygon(4, 30, 0.5)
draw_polygon(3, 30, 0.5)
draw_polygon(4, 30, 0.5)  ← Drawing 4-sided shape 3 times!
```

Problem: ________________________________________________________________

Better approach: ________________________________________________________


**Error 2:**
```blockly
For i in range(3):
  draw_polygon(4, 30, 0.5)
```

Problem: ________________________________________________________________

What shapes does it draw? ________________________________________________

**Error 3:**
```blockly
angle = 360 ÷ 4
draw_polygon(4, 30, 0.5)
draw_polygon(4, 50, 0.5)  ← Only right if angle is 90°!
```

Problem: ________________________________________________________________

Why is this thinking flawed? ______________________________________________

## Part 9: Generalization

**Without the polygon function, how many separate functions would you need to draw squares, triangles, hexagons, octagons, and pentagons?**

Answer: _____ functions

**With the polygon function, how many functions do you need?**

Answer: _____ function(s)

**What's the advantage of one generalized function?**

_________________________________________________________________

## Reflection

**What was the hardest part of the polygon challenge?**

_________________________________________________________________

**How did you verify your polygon was correct?**

_________________________________________________________________

**If you had to explain the polygon function to someone who missed this lesson, how would you describe it?**

_________________________________________________________________

_________________________________________________________________
