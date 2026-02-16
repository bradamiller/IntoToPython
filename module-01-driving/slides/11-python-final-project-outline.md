# Lesson 11 Slide Outline: Python Final Project

## Slide 1: Title & Learning Objectives
**Title:** Python Final Project Capstone

**Learning Objectives:**
- Synthesize all Module 1 concepts (loops, functions, parameters, motors)
- Design a project from concept to completion
- Debug and refine Python code
- Present and reflect on learning

**Agenda:**
- Project options overview (5 min)
- Planning phase (15 min)
- Implementation (30 min)
- Testing & refinement (20 min)
- Reflection & sharing (5 min)

---

## Slide 2: Hook - Bringing It All Together
**Where You Started (Lesson 1):**
- Learned about the XRP robot
- Ran first Blockly program

**What You've Built (Lessons 2-10):**
- ✓ Loops (Blockly & Python)
- ✓ Functions (Blockly & Python)
- ✓ Parameters and customization
- ✓ Motor control (differential drive)
- ✓ Mathematical thinking (polygon angles)

**Today's Challenge:** "Use EVERYTHING for one final project"

---

## Slide 3: Module 1 Concept Review
**Programming Concepts:**
- **Loops:** Repeat code efficiently (for, while, range)
- **Functions:** Create reusable code blocks (def)
- **Parameters:** Make functions flexible (arguments)
- **Variables:** Store and use values

**Python Syntax:**
```python
for i in range(n):
    # loop body

def function_name(parameter1, parameter2):
    # compute
    return result
```

**Robot Concepts:**
- **Straight:** Move forward/backward by distance
- **Turn:** Rotate by angle
- **set_effort:** Direct motor control
- **Differential drive:** How steering works

---

## Slide 4: Project Options
**Choose ONE project option:**

**Option A: Polygon Artist (Recommended for beginners)**
- Use polygon function to create artwork
- Combine different polygon shapes
- Create a visually interesting pattern

**Option B: Navigation Challenge (Recommended for intermediate)**
- Design a path robot must navigate
- Use math to calculate distances/angles
- Test reliability across multiple runs

**Option C: Sensor-Based Behavior (Recommended for advanced)**
- Use sensors (rangefinder, reflectance, button)
- Program robot to respond intelligently
- Create autonomous behavior

**Option D: Custom Project (For creative minds)**
- Your own idea!
- Must use loops AND functions
- Must demonstrate Module 1 concepts

---

## Slide 5: Project Planning Phase (15 min)
**Step 1: Choose your option & goal**
- What will your robot create/do?
- Why is this interesting?
- What part of Module 1 will you focus on?

**Step 2: Sketch in pseudocode**
```python
# Pseudocode (not real Python yet):
def create_design():
    # Draw first polygon
    # Move to new position
    # Draw second polygon
    # Move to new position
    # Draw third polygon
```

**Step 3: Identify needed functions**
- List all functions you'll write
- What parameters does each need?
- What will each function do?

**Step 4: Outline main program**
- What sequence calls which functions?
- What's the overall flow?

---

## Slide 6: Project Option A Deep Dive - Polygon Artist
**Goal:** Create artistic polygon composition

**Implementation Path:**
```python
def draw_polygon(sides, distance, effort=0.5):
    angle = 360 / sides
    for i in range(sides):
        drivetrain.straight(distance, max_effort=effort)
        drivetrain.turn(angle, max_effort=effort)

def create_artwork():
    # Triangle
    draw_polygon(3, 30)
    drivetrain.straight(80)
    
    # Square
    draw_polygon(4, 25)
    drivetrain.straight(80)
    
    # Pentagon
    draw_polygon(5, 20)

# Run it
create_artwork()
```

**Expansion Ideas:**
- Vary polygon sizes in pattern
- Change effort (speed) for visual rhythm
- Add spacing/movement between polygons
- Create repeating tile pattern

---

## Slide 7: Project Option B Deep Dive - Navigation Challenge
**Goal:** Reliable path navigation using calculated movements

**Implementation Path:**
```python
def move_forward(distance, effort=0.5):
    drivetrain.straight(distance, max_effort=effort)

def navigate_path():
    # Define waypoints
    move_forward(100)
    drivetrain.turn(90)
    move_forward(150)
    drivetrain.turn(-90)
    move_forward(100)
    # Now at finish

# Run multiple times to test reliability
navigate_path()
```

**Challenge Elements:**
- Design path that tests precision
- Use only Straight & Turn (no sensors)
- Test multiple times (consistency)
- Measure error (how far off from goal?)

---

## Slide 8: Project Option C Deep Dive - Sensor-Based Behavior
**Goal:** Robot responds to environment using sensors

**Implementation Path (conceptual):**
```python
def obstacle_avoidance():
    while True:  # Keep running
        distance = rangefinder.distance()
        
        if distance < 30:  # Obstacle close
            drivetrain.turn(90)
        else:
            drivetrain.straight(20)

# Run until user presses button
obstacle_avoidance()
```

**Types of Behavior:**
- ✓ Stop when obstacle detected
- ✓ Follow line using reflectance sensor
- ✓ Seek light/change based on environment
- ✓ React to button press

**Challenges:**
- Sensor calibration
- Decision logic (if/else)
- Testing and tuning

---

## Slide 9: Implementation Phase (30 min)
**Guidelines:**

**Step 1: Start with function definitions**
- Write all your def functions first
- Don't worry if Python interpretation isn't perfect yet

**Step 2: Write main program**
- Call your functions in sequence
- Verify structure before testing on robot

**Step 3: Test incrementally**
- Upload to robot one function at a time
- Verify each works before adding next
- Don't try whole program at once!

**Step 4: Debug and refine**
- Does robot move as expected?
- Are calculations correct?
- Any off-by-one errors? (angle calculations)

---

## Slide 10: Testing & Refinement Phase (20 min)
**Testing Checklist:**
- ✓ Code uploads without syntax errors
- ✓ Robot moves when expected
- ✓ All functions call correctly
- ✓ Parameters have reasonable values
- ✓ Program completes without crashing

**Debugging Process:**
1. **Does one part work?** Test minimal program
2. **Where does it fail?** Comment out sections
3. **What's wrong?** Read error messages
4. **How to fix?** Change code, test again

**Refinement Ideas:**
- Improve efficiency (combine repeated code)
- Add comments explaining logic
- Handle edge cases (what if sides < 3?)
- Make it more creative/interesting

---

## Slide 11: Documentation & Reflection
**Document Your Work:**

**Code Comments:**
```python
def draw_polygon(sides, distance, effort=0.5):
    """Draw a regular polygon shape.
    
    Args:
        sides: Number of sides (3+)
        distance: Length of each side in cm
        effort: Motor effort 0.0 to 1.0
    """
    angle = 360 / sides
    for i in range(sides):
        drivetrain.straight(distance, max_effort=effort)
        drivetrain.turn(angle, max_effort=effort)
```

**Reflection Questions:**
1. What concept was most challenging?
2. What are you most proud of?
3. How would you extend this project?
4. What would you do differently?
5. Which part of Module 1 did you use most?

---

## Slide 12: Presentation & Celebration
**Demo Your Project:**
- Show your code on screen
- Explain design choices
- Run program (let robot demonstrate)
- Discuss what you learned

**Peer Recognition:**
- What creative solutions did classmates find?
- Which projects demonstrate most Module 1 concepts?
- What problems did people solve uniquely?

**Looking Forward:**
- Module 2: Sensors (rangefinder, reflectance, IMU)
- Module 3: Autonomous behavior (navigation, obstacle avoidance)
- Module 4: Data logging & analysis
- Module 5: Advanced challenges

**Big Picture:** You now understand:
- ✓ Programming fundamentals (loops, functions)
- ✓ Robotics (motor control, movement)
- ✓ From visual (Blockly) to text (Python)
- ✓ Building real-world projects

"Congratulations! You're now a robot programmer."
