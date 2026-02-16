# Lesson 7: Blockly Challenges & Synthesis

## Overview
Students apply all skills from Lessons 1-6 to solve creative challenges and synthesize their learning. This capstone Blockly lesson combines loops, functions, parameters, motor control, and geometric thinking. Students will develop two challenge projects: a precision navigation task and a creative design project.

## Learning Objectives
By the end of this lesson, students will be able to:
- Combine multiple Blockly programming concepts in a single program
- Design and debug complex programs with multiple functions and parameters
- Solve open-ended challenges with multiple valid solutions
- Transition from guided to independent problem-solving
- Prepare for Python programming (Lessons 8-11) by seeing Blockly's limits

## Key Concepts
- **Integration**: Using loops, functions, parameters, and motor control together
- **Debugging process**: Predict → Test → Observe → Adjust
- **Design trade-offs**: Precision vs. Simplicity, Automation vs. Control
- **Open-ended problem-solving**: Multiple correct solutions
- **Readiness for Python**: Recognizing when text-based programming becomes necessary

## Materials Required
- XRP Robot with large clear driving space
- xrpcode.wpi.edu access
- Challenge course setup (optional markers, obstacles, targets)
- Rulers/measuring tape for verification
- Teams of 2-3 students recommended

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 7 min
**For 3-hour sessions:** 10-12 min

1. **Hook: The Integration Problem**:
   - Show: A complex task—"Robot must draw a house shape (square + triangle roof), park in a garage, then signal completion"
   - Ask: "What tools do we need?"
   - Students identify: Loops (for shapes), Functions (for reusable pieces), Motor control (for precision), Parameters (for flexibility)

2. **Review Key Concepts**:
   - **Loops**: Repeat for efficiency
   - **Functions**: Reusable code blocks
   - **Parameters**: Flexible inputs
   - **Motor control**: Direct movement
   - **Debugging**: Systematic problem-solving

3. **Challenge Philosophy**:
   - Multiple valid solutions (engineer mindset)
   - Constraints & trade-offs (real-world thinking)
   - Iteration & improvement (not "perfect on first try")
   - Collaboration & peer feedback (teamwork)

4. **Preview Challenges**:
   - Challenge 1: Precision Navigation (guided complexity)
   - Challenge 2: Creative Design (open-ended)

### Challenge 1: Precision Navigation Task (25 minutes)
**For 50-min classes:** 20 min
**For 3-hour sessions:** 30-35 min

**Scenario**: "Your robot is a delivery vehicle that must:
1. Navigate through a marked course (straight sections and turns)
2. Reach a target location within ±30cm accuracy
3. Signal arrival (LED or print message)"

**Course Layout** (marked with tape or cones):
- Start point
- Straight path: 150cm forward
- Right turn: 90°
- Straight path: 100cm forward
- Left turn: 45°
- Straight path: 50cm forward
- Target location (stop here)

**Planning Phase** (5 minutes):
1. Measure course dimensions
2. Discuss strategies:
   - **Precision approach**: Use `straight()` and `turn()` with measured distances
   - **Speed approach**: Navigate quickly, accept ±50cm error
   - **Robustness approach**: Use set_effort, adjust timing for varied surfaces
3. Choose and sketch the approach on whiteboard

**Implementation Phase** (15 minutes):
1. **Build Program Structure**:
   ```blockly
   Wait for button press
   
   Function: navigate_course()
   - Straight(150) + Turn(90)
   - Straight(100) + Turn(-45)
   - Straight(50)
   - Print "Arrived at target"
   
   Call navigate_course()
   ```

2. **Code Options**:
   - **Option A (Simple)**: Linear program without functions
   - **Option B (Recommended)**: One function that sequences all moves
   - **Option C (Advanced)**: Multiple functions, each responsible for one segment

3. **Testing Strategy**:
   - Test each segment individually first
   - Combine segments and test again
   - Measure final position vs. target
   - Adjust distances if off target

4. **Common Adjustments**:
   - If overshoots: Reduce distance by 5-10cm
   - If undershoots: Increase distance by 5-10cm
   - If turns are imprecise: Check IMU calibration or surface
   - If accumulating error: Break task into more segments, measure between each

**Debrief** (5 minutes):
- Which solution was most precise? Why?
- What was the hardest part? (Measuring accurately, predicting wheels behavior?)
- What trade-offs did you make? (Speed vs. Precision, Simplicity vs. Flexibility)
- Could you improve? How?

### Challenge 2: Creative Design Project (30 minutes)
**For 50-min classes:** 25 min
**For 3-hour sessions:** 35-40 min

**Scenario**: "Design and implement your own robotic choreography—a creative sequence of movements that tells a story or creates art."

**Concept Options** (choose one or design your own):
1. **Labyrinth Explorer**: Navigate a maze drawn with tape
   - Combines turning, straight paths, wall-following concepts
   - Goal: Reach center without hitting walls
   
2. **Multi-Shape Artist**: Draw a complex geometric design
   - Combines polygon function with creative layout
   - Example: Pentagon-hexagon-octagon arranged in a pattern
   - Goal: Complete design quickly and accurately
   
3. **Precision Parking**: Park the robot in a marked garage perfectly centered
   - Combines straight line with fine motor adjustment
   - Uses set_effort for slow, precise final positioning
   - Goal: Stop with robot centered ±5cm
   
4. **Chase & Evade Dance** (Requires 2 robots or imaginary opponent):
   - First robot moves, second "follows" (or AI imagined)
   - Combination of curves, spirals, quick turns
   - Goal: Creative, expressive movement
   
5. **Performance Art**: Use LED, motors, and movements together
   - Coordinates motor movement with LED signals
   - Tells a short story (e.g., robot wakes up, explores, goes to sleep)
   - Goal: Entertaining 30-second performance

**Planning Phase** (8 minutes):
1. **Brainstorm** (2 min): Sketch design on paper
2. **Identify Functions** (3 min): Break design into reusable pieces
   - Example for artist: `draw_circle_arc()`, `move_between_shapes()`, `spiral_in()`
3. **Write Pseudocode** (3 min): Outline structure before coding
   - Helps plan parameters and identify bottlenecks

**Implementation Phase** (15 minutes):
1. **Build Core Functions First**:
   - Identify 2-3 key functions needed
   - Test each independently
   - Debug movement before combining
   
2. **Assemble Main Program**:
   - Call functions in sequence with waits
   - Test partial program (first few calls) before full run
   - Add delays if needed for observation/photo opportunities

3. **Iterate & Refine** (5 minutes):
   - Run full program
   - Observe timing, precision, creativity
   - Make small adjustments (effort, duration, angles)
   - Prepare for peer showcase

4. **Documentation** (2 minutes):
   - Write a brief "story" or description of what the robot is doing
   - Identify one thing you'd improve if you had more time

**Showcase & Reflection** (10 minutes):
- 2-3 students present their design
- For each: "What was your goal? What functions did you use? What was the hardest part?"
- Peer feedback: "What did you like about this design? What would you change?"
- Class discussion: "Which approach was most clever? Most efficient? Most creative?"

### Assessment

**Formative (during challenges)**:
- Can students plan program structure before coding?
- Do they test iteratively (small pieces first, then combined)?
- Can they debug by making predictions and testing hypotheses?
- Are they using functions and parameters effectively?

**Summative (at end of lesson)**:
- Complete Challenge 1 with ≤30cm error
- Complete Challenge 2 with a working, creative program
- Written reflection (1-2 paragraphs):
  1. Describe what you built and how it works
  2. Which Blockly concepts (loops, functions, parameters) did you use, and why?
  3. What was the biggest challenge, and how did you solve it?
  4. What would you change if you could improve the program?

## Common Misconceptions & Debugging Guide

| Problem | Possible Causes | Solutions |
|---|---|---|
| Program runs but robot doesn't move | Missing `wait for button press` or motors stopped | Check block structure; verify wait_for_button_press is first |
| Robot moves but stops before finishing | Effort too low or surface friction | Increase effort to 0.7; test on different surface |
| Repeated actions are inconsistent | Wheel slip or battery voltage changing | Clean wheels; replace batteries; use encoders instead of timing |
| Complex program is hard to debug | Too many blocks in one function | Break into smaller functions; test each independently |
| Shape is distorted or off-axis | Accumulated rounding errors or uneven surfaces | Check if surface is level; verify IMU is calibrated |

## Differentiation

**For struggling students**:
- Provide a partial code template for Challenge 1 (moves already laid out, just adjust distances)
- Choose Challenge 2 Option 1 (Labyrinth) or Option 3 (Parking)—more structured than art
- Pair with a stronger partner for peer support
- Allow extra time for testing and iteration
- Provide a debugging checklist ("Did I start with wait_for_button_press? Did I stop motors?")

**For advanced students**:
- Challenge to complete Challenge 1 with <15cm error
- Design Challenge 2 to include multiple robots (with imaginary collision detection)
- Add constraints: "Complete in <60 seconds" or "Use only 3 functions maximum"
- Ask to optimize: "Can you reduce your code by 30% while keeping the same behavior?"
- Propose extensions: "Add color sensor logic to detect and stop at obstacles"

## Materials & Code Examples

### Challenge 1 Solution Template
```blockly
[Main]
Wait for button press
Call navigate_course()

[Function: navigate_course]
Straight(150) at 0.5
Turn(90) at 0.5
Straight(100) at 0.5
Turn(-45) at 0.5
Straight(50) at 0.5
Print "Arrived!"
```

### Challenge 2 Example: Multi-Shape Artist
```blockly
[Functions]
"to draw_polygon(sides, distance, effort)"
"to move_to_next(distance)"  ← Helper function
"to reset_position"           ← Optional, return to start

[Main]
Wait for button press
Call draw_polygon(5, 20, 0.5)
Call move_to_next(30)
Call draw_polygon(6, 20, 0.5)
Call move_to_next(30)
Call draw_polygon(8, 15, 0.5)
Print "Artwork complete!"
```

## Teaching Notes
- **Classroom management**: Have students present solutions without revealing code (encourages collaboration over copying)
- **Time management**: Set "stop coding" time 5 min early to allow showcase & reflection
- **Encourage documentation**: Commented code is more valuable than clever code
- **Celebrate effort**: Even if solution isn't perfect, value the problem-solving process
- **Connect to career**: Highlight real-world parallels—engineers solve open-ended problems too
- **Prepare for Python**: Point out that Lesson 8 converts Blockly to Python—same logic, just new syntax

## Assessment Rubric

### Challenge 1: Navigation (10 points)
- Correct route planning (3 pts): Identifies all course segments correctly
- Implementation (4 pts): Program runs, robot follows course, achieves ±30cm accuracy
- Debugging approach (3 pts): Shows evidence of testing, adjusting, re-testing

### Challenge 2: Creative Design (10 points)
- Planning & design (3 pts): Clear goal, identified functions, sketched plan
- Implementation (4 pts): Program runs, functions work, creative design is visible
- Reflection (3 pts): Written or verbal explanation of approach and process

### Overall Lesson (5 bonus points)
- Collaboration (2 pts): Worked effectively with peers, shared ideas
- Improvement mindset (3 pts): Iterated, debugged, adjusted based on feedback

## Connections to Next Lessons
- **Lesson 8: Hello, Python** will convert these Blockly programs to Python syntax
- **Lessons 9-11: Python Functions and Loops** will extend these concepts further
- This lesson is the capstone of **Blockly mastery** and the launch point for **Python learning**
