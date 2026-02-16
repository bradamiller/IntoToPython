# Lesson 7 Slide Outline: Blockly Challenges & Synthesis

## Slide 1: Title & Learning Objectives
**Title:** Blockly Challenges & Synthesis

**Learning Objectives:**
- Synthesize all Blockly concepts (loops, functions, parameters, motors)
- Debug complex programs
- Solve open-ended design challenges
- Prepare for transition to Python

**Agenda:**
- Concept review (5 min)
- Challenge 1: Navigation task (25 min)
- Challenge 2: Creative design (30 min)
- Debrief & reflection (5 min)

---

## Slide 2: Hook - The Ultimate Challenge
**Scenario:** You're the lead programmer for a robot competition

**Challenge:** Design a robot program that:
1. Draws a specific pattern OR
2. Navigates an obstacle course OR
3. Responds to sensors (if available)

**Requirements:**
- Use at least 2 different concepts
- Work reliably on your XRP
- Document your code with comments

**Question:** "Can you bring together everything you've learned?"

---

## Slide 3: Blockly Concepts Review
**Loops (Lesson 2):**
- Repeat blocks reduce code duplication
- Essential for patterns and shapes

**Functions (Lesson 3):**
- Reusable code blocks
- Cleaner, more readable programs

**Parameters (Lesson 4):**
- Customize function behavior
- Flexible, powerful functions

**Special: Polygon Function (Lesson 5):**
- Mathematical abstraction
- One function, infinite shapes

**Motors (Lesson 6):**
- set_effort for low-level control
- Differential drive steering

---

## Slide 4: Program Architecture Patterns
**Pattern 1: Sequence**
```
Straight
Turn
Straight
Turn
→ Simple linear execution
```

**Pattern 2: Loops**
```
Repeat 4 times:
  Straight
  Turn
→ Repeats sequence
```

**Pattern 3: Functions**
```
Call draw_triangle
Call draw_square
→ Organized, reusable blocks
```

**Pattern 4: Combination**
```
Repeat 3 times:
  Call draw_polygon(5, 25, 0.5)
  Straight(50)
→ Nested abstractions
```

---

## Slide 5: Debugging Strategies
**Error Type 1: Robot doesn't move**
- Check: Motor effort > 0?
- Check: Wait blocks present?
- Check: Robot turned on?

**Error Type 2: Wrong shape**
- Check: Turn angle correct? (360÷sides)
- Check: Repeat count correct? (number of sides)
- Check: Distance correct?

**Error Type 3: Program crashes**
- Check: Parameter values reasonable? (not -1 sides!)
- Check: Function names spelled correctly?
- Check: All blocks connected?

**Strategy:** Change ONE thing, test, observe

---

## Slide 6: Challenge 1 - Navigation Task (25 min)
**Objective:** Precision navigation in defined space

**Available Spaces:**
- Option A: 4m × 4m open area
- Option B: Classroom with obstacles
- Option C: Marked course with defined waypoints

**Task:** Design a program that:
1. Navigate from start to finish without sensors
2. Demonstrate at least 3 movement types
3. Complete 3 trials with consistency

**Demonstration Elements:**
- Straight lines (use Straight blocks)
- Turns (90°, 45°, custom angles)
- Optional: Polygonal path (use draw_polygon)

---

## Slide 7: Challenge 1 Exemplar Program
**Sample Solution:**
```
Define navigate_to_finish
  Straight(100)           ← Move forward 1m
  Turn(90)                ← Turn right
  Straight(150)           ← Move forward 1.5m
  Turn(-90)               ← Turn left
  Straight(100)           ← Final straight to finish
  
Call navigate_to_finish
```

**What Makes This Work:**
- ✓ Clear, linear path
- ✓ Predictable turns (90° angles)
- ✓ Uses Straight for known distances
- ✓ Wrapped in function (optional but good practice)

**Possible Enhancements:**
- Repeat the path multiple times
- Add variable for distance (parameter)
- Add comments explaining each move

---

## Slide 8: Challenge 2 - Creative Design (30 min)
**Objective:** Free-form creative programming

**Choose One:**

**Option A: Polygon Artist**
- Use draw_polygon(sides, distance, effort)
- Create artistic composition
- 3+ different polygons at different scales

**Option B: Pattern Maker**
- Design abstract pattern with loops
- Spirals, zigzags, or repeating elements
- Demonstrate mathematical beauty

**Option C: Sensor Integration** (if sensors available)
- React to range, reflectance, or button sensors
- Stop when obstacle detected
- Change pattern based on sensor input

**Evaluation Criteria:**
- Creative Use multiple concepts (functions, loops, parameters)
- Technical: Code runs without errors
- Polish: Clean, readable, well-structured

---

## Slide 9: Challenge 2 Exemplar Programs
**Exemplar A: Polygon Artist**
```
draw_polygon(3, 40, 0.5)   ← Triangle
Straight(80)
draw_polygon(4, 35, 0.5)   ← Square
Straight(80)
draw_polygon(5, 30, 0.5)   ← Pentagon
→ Creates progression of shapes
```

**Exemplar B: Spiral Pattern**
```
Repeat 8 times:
  Straight(50)
  Turn(45)
→ Creates 8-pointed star-like pattern
```

**Exemplar C: Dancing Robot**
```
Define wiggle
  Turn(20)
  Wait(0.5)
  Turn(-40)
  Wait(0.5)
  Turn(20)
  
Repeat 5: Call wiggle
→ Rhythmic back-and-forth movement
```

---

## Slide 10: Reflection & Documentation
**After Challenge:**

**Reflection Questions:**
1. What worked? What didn't?
2. Which concept (loops, functions, parameters) was most useful?
3. What would you do differently next time?
4. How could you extend this program?

**Program Documentation:**
- Add comments explaining complex sections
- Describe purpose of each function
- List parameters and what they control

**Example:**
```
// Navigation program: Go in rectangle, return to start
// Demonstrates: Straight, Turn, Sequence

Define navigate_rectangle with parameter: speed
  // North side
  Straight(200, max_effort=speed)
  Turn(90, max_effort=speed)
  
  // East side (continued...)
```

---

## Slide 11: Peer Review & Sharing
**Gallery Walk:**
1. Load your program on robot
2. Demo for classmates
3. Explain design choices
4. Discuss challenges encountered

**Feedback Questions for Peers:**
- What interesting concepts did they use?
- How creative/effective was the design?
- What would improve the program?
- Could you build on this program?

**Presentation (if group):**
- What was your goal?
- How did you approach it?
- What did you learn?

---

## Slide 12: Bridge to Python (Lesson 8+)
**Key Insights from Blockly:**
- ✓ Loops & patterns are powerful
- ✓ Functions reduce complexity
- ✓ Parameters add flexibility
- ✓ Motor control enables creative movement

**Transition Coming:**
- Lesson 8: Hello Python (syntax introduction)
- Lesson 9: Python loops (same concepts, text syntax)
- Lesson 10: Python functions (same concepts, text syntax)
- Lesson 11: Python final project (larger capstone)

**Key Realization:**
"Every concept you've mastered in Blockly lives on in Python. The blocks disappear, but the thinking stays the same."
