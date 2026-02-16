# Lesson 2 Slide Outline: Drawing Shapes

## Slide 1: Title & Learning Objectives
**Title:** Drawing Shapes with Loops

**Learning Objectives:**
- Use Repeat blocks to automate commands
- Calculate turn angles for polygons
- Draw squares, triangles, and other shapes
- Understand repetition as a programming pattern

**Agenda:**
- Geometry review (10 min)
- Repeat block introduction (5 min)
- Guided: Draw a square (10 min)
- Practice: Draw triangle & pentagon (20 min)

---

## Slide 2: Hook - How Does a Robot Draw?
**Question:** "How would the robot draw a square?"

**Show:** Video or animation of robot drawing square
- Goes forward → turns → forward → turns → ... → back to start
- Repeats same action 4 times

**Key Insight:** Computers excel at repetition

---

## Slide 3: Geometry Foundations
**Regular Polygons:**
- Same length sides
- Same angles at each corner
- Close and return to start

**Exterior Angle Formula:**
- 360° ÷ Number of Sides = Turn Angle per Side
- Why 360°? Full rotation = 360°

**Examples:**
- Triangle (3 sides): 360 ÷ 3 = **120°**
- Square (4 sides): 360 ÷ 4 = **90°**
- Pentagon (5 sides): 360 ÷ 5 = **72°**
- Hexagon (6 sides): 360 ÷ 6 = **60°**

---

## Slide 4: Introducing the Repeat Block
**What is Repeat?**
- Runs code inside it N times
- Reduces duplication
- Makes program shorter and clearer

**Blockly Appearance:**
```
Repeat [4] times:
  [Blocks inside]
```

**Why Use It?**
- Draw square: 4 times, not 4 separate blocks
- Easier to change (modify once, applies to all)
- Match polygon structure (sides)

---

## Slide 5: The Square Program
**Step-by-step:**
1. Wait for button press
2. Repeat 4 times:
   - Straight(30) at 0.5 effort
   - Turn(90°) at 0.5 effort

**Show:** Blockly screenshot with complete program

**Key Parameters:**
- 4 repeats = 4 sides
- 30 cm = side length
- 90° = exterior angle (360÷4)
- 0.5 effort = speed

---

## Slide 6: Prediction & Testing
**Before Running:**
"Predict: What shape will the robot draw?"

**Allow students to:**
- Trace path with finger
- Sketch on paper
- Discuss with partner

**Then Run:** Upload and observe

**Discussion:** Did it match your prediction? What differences?

---

## Slide 7: The Triangle Challenge
**Goal:** Draw a 3-sided shape

**Calculation:**
- Number of sides: 3
- Turn angle: 360 ÷ 3 = **120°**
- Distance: 25 cm (your choice)
- Repeat block: Repeat **3** times

**Code Structure:**
```
Repeat 3 times:
  Straight(25)
  Turn(120°)
```

---

## Slide 8: The Pentagon Challenge
**Goal:** Draw a 5-sided shape

**Calculation:**
- Number of sides: 5
- Turn angle: 360 ÷ 5 = **72°**
- Distance: 20 cm (your choice)
- Repeat block: Repeat **5** times

**Interactive:** 
- "What's the angle?" (Let students calculate)
- "Show me on your hands" (Demonstrate with hand gestures)

---

## Slide 9: Angle Calculation Deep Dive
**Why This Formula Works:**
- Robot makes same turn at each corner
- 4 corners × 90° = 360° (completes rotation)
- 6 corners × 60° = 360° (completes rotation)

**Visual:** Draw circle, show angle wedges

**Test:** "For an octagon, what's the angle?" (360÷8=45°)

---

## Slide 10: Shape Variations & Predictions
**What If You Change Parameters?**

| Change | Effect | Shape |
|---|---|---|
| Repeat 4, Distance 50 | Bigger | Still square |
| Repeat 4, Distance 20 | Smaller | Still square |
| Repeat 6, Distance 20 | Different | Hexagon |
| Repeat 4, Angle 45 | Doesn't close | Not a square |

**Key:** Sides determine shape; distance determines size

---

## Slide 11: Common Misconceptions
**"The angle should be 90°, so my square has interior angle 90°"**
- Actually: 90° is EXTERIOR angle (turn angle)
- Interior angle = 180° - 90° = 90° (different formula)
- Both happen to be 90° for squares!

**"More sides = bigger shape"**
- No! More sides = more corners, not larger perimeter
- A 20cm triangle (perimeter 60cm) vs. 10cm hexagon (perimeter 60cm)

---

## Slide 12: Connection to Functions (Lesson 3)
**Preview:**
- Today: Write three separate shape programs
- Next lesson: Write ONE function that draws any shape
- Use parameters: `draw_polygon(sides, distance)`

**Teaser:** "Imagine if you could draw ANY polygon with a single function call!"
