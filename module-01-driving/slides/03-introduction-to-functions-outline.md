# Lesson 3 Slide Outline: Introduction to Functions

## Slide 1: Title & Learning Objectives
**Title:** Introduction to Functions

**Learning Objectives:**
- Understand what a function is
- Recognize when to use functions
- Create and call your own functions
- See code reusability in action

**Agenda:**
- Functions in real life (5 min)
- Function definition vs. call (10 min)
- Guided: Create draw_triangle function (10 min)
- Practice: Create and use functions (20 min)

---

## Slide 2: Hook - Repetitive Code Problem
**Scenario:** You want to draw 3 different triangles in your program

**Bad Approach:**
```
Straight(25) → Turn(120) → Straight(25) → Turn(120) → Straight(25) → Turn(120)
Straight(25) → Turn(120) → Straight(25) → Turn(120) → Straight(25) → Turn(120)
Straight(25) → Turn(120) → Straight(25) → Turn(120) → Straight(25) → Turn(120)
```
(Repeat 6 times in the program!)

**Question:** "What if you had to draw 10 triangles? Or change the distance?"

---

## Slide 3: What is a Function?
**Definition:**
- Reusable block of code
- Has a name you give it
- You define it ONCE
- You use it MANY TIMES

**Real-World Analogy:**
- **No function:** Writing recipe steps every time you cook
- **Function:** Write recipe in cookbook, refer to it each time
- Or: "Make a sandwich" command vs. listing all steps each time

**Benefits:**
- Less code duplication
- Easier to change (fix once, applies everywhere)
- Easier to read and understand

---

## Slide 4: Defining vs. Calling
**Define (Create):**
- "Here's what this function does" 
- Write code inside function
- Do this ONCE

**Call (Use):**
- " Actually do that thing"
- Use function name
- Do this MANY TIMES

**Blockly:**
- "Create Function" → name it → add blocks inside
- "Call Function" → choose name from dropdown

---

## Slide 5: Function Structure
**Anatomy of a Function (in Blockly):**

```
[Define Function] draw_triangle
  Repeat 3 times:
    Straight(25)
    Turn(120)
```

**Parts:**
- **Name:** `draw_triangle` (what you call it)
- **Code inside:** The steps to repeat
- **When to define:** Once at the beginning
- **When to call:** Anywhere you need it

---

## Slide 6: Creating Your First Function
**Live Demo: Create draw_triangle**

**Steps:**
1. Go to Functions category
2. Click "Create Function"
3. Name it: `draw_triangle`
4. Drag Repeat + Straight/Turn blocks inside
5. Set to: Repeat 3, Straight(25), Turn(120)

**Result:**
- New function available in "Call function" dropdown
- Can now use `draw_triangle` block

---

## Slide 7: Multiple Function Calls
**Program:**
```
Wait for button press
Call draw_triangle
Straight(50)
Call draw_triangle
Turn(90)
Call draw_triangle
```

**What Happens:**
1. Button pressed
2. Robot draws triangle
3. Goes forward 50 cm
4. Draws triangle (same code, no rewriting!)
5. Turns 90°
6. Draws triangle (again!)

**Benefits:**
- 3 triangles drawn with 3 lines
- Could change `draw_triangle` → all 3 update automatically

---

## Slide 8: Function vs. Non-Function Comparison
**Without Function (17 blocks):**
```
Repeat 3: Straight(25), Turn(120)
Straight(50)
Repeat 3: Straight(25), Turn(120)  [DUPLICATED]
Turn(90)
Repeat 3: Straight(25), Turn(120)  [DUPLICATED]
```

**With Function (5 blocks + 1 definition):**
```
Define draw_triangle:
  Repeat 3: Straight(25), Turn(120)

Call draw_triangle
Straight(50)
Call draw_triangle
Turn(90)
Call draw_triangle
```

**Comparison Chart:**
| Measure | No Function | With Function |
|---------|-------------|----------------|
| Main program blocks | 17 | 5 |
| Repetition | 3 copies | 1 copy |
| To change distance | Change 3 places | Change 1 place |
| Readability | Hard to see structure | Clear: "draw triangle" |

---

## Slide 9: When to Use Functions
**Use a function when:**
1. ✓ Same code appears multiple times
2. ✓ Code does one clear task
3. ✓ You might change it later
4. ✓ Name makes code clearer

**Don't use a function when:**
1. ✗ Only used once
2. ✗ Very simple (1-2 blocks)
3. ✗ No clear, simple name

**Examples:**
- ✓ `draw_triangle` → Clear purpose, reusable
- ✓ `draw_square` → Clear purpose, reusable
- ✗ `Do stuff` → Vague purpose
- ✗ Single `Straight` block → Too simple for function

---

## Slide 10: Common Misconceptions
**"Functions are magical - they're different than regular code"**
- Not true! Functions are just organized code blocks
- They work exactly like normal code, just stored for reuse

**"I should make a function for everything"**
- No! Only when code repeats or needs clarity
- One-time-only, simple code doesn't need functions

**"Once I define a function, I can't change the main code"**
- False! You define functions, then use them as much as you want
- Changes to definition automatically apply everywhere

---

## Slide 11: Practice Challenges
**Challenge 1:** Create a `draw_square` function
- 4 sides, 90° turns, 30 cm distance
- Call it 3 times in main program

**Challenge 2:** Create a `wiggle` function
- Small back-and-forth movement
- Use it to make robot "dance"

**Challenge 3:** Create TWO functions
- `draw_triangle` and `draw_square`
- Call them both in creative pattern

---

## Slide 12: Connection to Parameters (Lesson 4)
**Preview:**
- Today: Fixed functions (triangle always same size)
- Next lesson: Flexible functions with parameters
- Example: `draw_shape(size)` → change size without rewriting

**Teaser:** "What if you could make draw_triangle customizable? That's coming next!"
