# Module 1: Learning How to Drive the Robot

## Overview

**Duration:** 3–4 weeks

**Theme:** Get comfortable with the robot and transition from visual block-based programming (Blockly) to Python text-based programming

**Final Project:** A Python program using a polygon function to draw multiple shapes on the whiteboard

## Learning Objectives

By the end of this module, students will be able to:
- Understand how the XRP robot works (hardware, motors, basic commands)
- Write and modify programs in Blockly (visual blocks)
- Transition to writing Python code for robot control
- Understand and use variables, loops, and functions in Python
- Write a polygon-drawing function and call it with different parameters
- Debug simple programs and understand control flow

## Key Concepts

- **Sequencing:** Ordering commands (drive, turn, drive, turn)
- **Loops:** Repeating instructions without rewriting them (`for` loops, repeat blocks)
- **Functions:** Creating reusable code blocks with parameters
- **Parameters:** Making functions flexible by passing in different values (e.g., size, number of sides)
- **Variables:** Storing and using values (distance, angle, repetitions)
- **Text-Based Programming:** Translating Blockly blocks to Python syntax

## Module Structure

### Phase A: Blockly (Lessons 1–5)
Get comfortable with the robot using visual blocks.
- Lesson 1: Meet the XRP
- Lesson 2: Drawing Shapes
- Lesson 3: Functions
- Lesson 4: Parameters
- Lesson 5: Generalizing with the Polygon Function

### Phase B: Driving Challenges (Lessons 6–7)
Apply Blockly skills to precision driving.
- Lesson 6: Differential Drive and Circles
- Lesson 7: Driving Challenges

### Phase C: Transition to Python (Lessons 8–11)
Move from Blockly to Python text-based programming.
- Lesson 8: Hello, Python
- Lesson 9: Loops in Python
- Lesson 10: Functions in Python
- Lesson 11: Module 1 Final Project

## Python Concepts Introduced

| Concept | Lesson | Usage |
|---|---|---|
| Variables | 8 | Storing values like distance or angle |
| `print()` | 8 | Displaying output |
| `for` loops | 9 | Repeating commands (e.g., drawing sides of a polygon) |
| `range()` | 9 | Creating a sequence of numbers (e.g., `range(4)` for 4 sides) |
| `def` (defining functions) | 10 | Creating reusable code blocks |
| Parameters | 10 | Passing values into functions |
| Function calls | 10 | Running a function with arguments |
| Basic XRP API | 8–11 | `drivetrain.straight()`, `drivetrain.turn()` |

## Progression

1. **Weeks 1–2:** Blockly foundation — students build confidence with the robot without worrying about syntax
2. **Weeks 3–4:** Python transition — students move to text-based programming, comparing Blockly blocks to Python code side-by-side

**No prior programming experience assumed.**

## Key Milestones

- ✓ **End of Week 1:** Robot drives forward and backward reliably
- ✓ **End of Week 2:** Polygon function works in Blockly; students can call it with different parameters
- ✓ **End of Week 3:** Comfortable with Python syntax; `for` loops and `range()` understood
- ✓ **End of Week 4:** Final project complete — Python polygon function draws multiple shapes

## Assessment

Students demonstrate mastery by:
1. **Exercise completion:** Each lesson has 2–3 hands-on exercises
2. **Code functionality:** Programs run and produce correct output
3. **Final project:** Polygon function works correctly; multiple shapes drawn successfully

## Resources

- XRP documentation and API reference (in code/solutions/)
- Blockly environment (via XRP IDE)
- Python interactive shell for testing small code snippets
- Whiteboard for debugging and discussing logic

## Troubleshooting Tips

- **Robot doesn't drive straight:** Wheels may be misaligned; check mounting and wheel positions
- **Blockly blocks not connecting:** Ensure block types match (number blocks for numbers, logic blocks for conditions)
- **Python syntax errors:** Review indentation carefully; use starter code as reference
- **Timing issues:** Some commands may need `time.sleep()` between them; covered in lessons

## Next Module

Module 2 builds on these foundational skills by introducing **sensors** and **control loops**, using the classes you've built here to follow lines and make decisions based on sensor input.

---

## Lesson-Lesson Details

For detailed plans on each lesson, see the `lessons/` folder. Each lesson includes:
- Learning objectives
- Key concepts explained
- Worked examples
- Exercises with starter code
- Extensions and differentiation strategies

---

**Questions?** See the Module 1 lesson plans or check the course README for support options.
