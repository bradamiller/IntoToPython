# Lesson 1: Meet the XRP

**Module:** 1 — Learning How to Drive the Robot  
**Phase:** A — Blockly Foundation  
**Duration:** 50–60 minutes (or 25–30 minutes in a 3-hour format)  
**Target Audience:** High school students, no prior programming experience

---

## Learning Objectives

By the end of this lesson, students will be able to:
- Identify the key hardware components of the XRP robot (motors, wheels, sensors, controller board)
- Understand the purpose of each component (what does it do?)
- Navigate and use the Blockly programming environment (XRP Code)
- Write a simple Blockly program that makes the robot drive forward and backward
- Upload and run a program on the robot
- Debug basic issues (robot doesn't move, moves in wrong direction, etc.)

---

## Key Concepts

- **Hardware Components:** Motors drive the wheels. The controller board tells the motors what to do. Sensors let the robot "see" the world.
- **Blockly Programming:** Visual, block-based programming. Drag and drop commands; no syntax errors.
- **Command Sequencing:** Commands run one after another. Drive happens, then turn happens, then next command.
- **Effort/Power Levels:** How much power goes to each motor (0 = off, 1 = full power). Positive = forward, negative = backward.

---

## Materials & Prerequisites

**Hardware:**
- 1 XRP robot (per student or pair)
- USB cable (robot to computer)
- Fully charged battery

**Software:**
- XRP Code IDE (xrpcode.wpi.edu)
- Modern web browser (Chrome, Firefox, Safari, Edge)

**Physical Setup:**
- Open floor or large whiteboard material for robot to drive on
- Tape or marks to show distance (optional, but helpful for testing)

**Prerequisites:**
- Basic computer literacy (using a browser, copying files, etc.)
- No prior robotics or programming experience required

---

## Lesson Flow

### Introduction (5–10 minutes)

**Hook:** Show students a video clip (1–2 min) of an XRP robot driving around, or demonstrate a working robot in action. Ask: "What makes this robot move? How does it know what to do?"

**Learning Goal:** "Today, you'll learn about the robot's hardware, and you'll write your first program to make it move."

### Direct Instruction: Hardware Tour (15–20 minutes)

**Part 1: Physical Components (10 min)**

Walk through each major part of the robot:

1. **The Wheels & Motors**
   - Two DC motors, one on each side
   - Motors spin the wheels
   - Motor power is controlled by the controller board
   - Demo: Point out left and right motor; ask students which motor would spin to turn the robot left

2. **The Controller Board** (XRP Control Board)
   - The "brain" of the robot
   - Receives programs via USB
   - Tells the motors what to do
   - Has sensors for line detection (front), distance measurement (ultrasonic), etc.
   - Demo: Show where USB plugs in; explain that this is where we upload programs

3. **The Battery**
   - Powers the entire robot
   - Must be charged regularly
   - Low battery = slow/sluggish robot

4. **Sensors (Briefly Introduce)**
   - Two reflectance sensors (front, bottom) — detect white vs. black (for line following, later)
   - Ultrasonic rangefinder (front) — measures distance to objects (for obstacle detection, later)
   - These will be used in Modules 2–5; for now, just acknowledge they exist

5. **Other Components**
   - Caster wheel (rear) — helps with balance
   - USB cable, battery connector

**Part 2: How Robots Get Instructions (5 min)**

Explain the workflow:
1. Write a program (we'll use Blockly)
2. Upload to robot via USB
3. Robot runs the program automatically
4. Program tells motors what to do: speed, direction, duration

### Direct Instruction: Blockly Introduction (10–15 minutes)

**Part 1: Navigating XRP Code (5 min)**

Open xrpcode.wpi.edu on the projector/screen. Show:
- Project creation (blue "+" button)
- Block palette (left side) — categories: Drive, Turn, Wait, Loops, Variables, etc.
- Work area (center) — where you drag blocks
- Start/Stop blocks (already there by default)
- Upload button (right side in top menu)

**Part 2: Key Blocks for This Lesson (8–10 min)**

Show and explain three main blocks:

1. **Drive Block**
   - `Drive [forward/backward] for [distance] cm at [power] %`
   - Distance: in centimeters (positive = forward, negative = backward)
   - Power: 0–100% (recommended: 30–70% for learning)
   - Demo: Show block in action in a program

2. **Turn Block**
   - `Turn [left/right] for [angle] °`
   - Angle: in degrees (90° = quarter turn, 180° = half turn)
   - Demo: Show how to use it

3. **Wait Block**
   - `Wait [time] seconds`
   - Useful for pauses between commands
   - Optional for this lesson, but good to know

**Worked Example: Drive Forward and Back**

Build this program on the projector step-by-step:

```blockly
[Start block]
  Drive forward for 30 cm at 50%
  Drive backward for 30 cm at 50%
[Stop block]
```

Ask students to predict what will happen:
- "What will the robot do?"
- "How far will it go?"
- "Will it come back to where it started?"

Explain: "The robot runs these commands in order, one after another."

### Guided Practice: First Upload (10–15 minutes)

**Activity 1: Prepare and Upload**

1. Have students (or you, if time is tight) go to xrpcode.wpi.edu and create a new project
2. Name it something simple like "Lesson_1_First_Drive"
3. Build the same program as the worked example:
   - Start block (already there)
   - Drive forward 30 cm at 50%
   - Drive backward 30 cm at 50%
   - Stop block (already there)

4. Plug robot into USB (if not already)
5. Click Upload
6. Select the robot from the list
7. Wait for confirmation "Upload Successful"
8. Press the button on the robot to run (or it may auto-run)

**Expected Behavior:**
- Robot beeps or shows a light (ready)
- Robot drives forward 30 cm (roughly)
- Robot backs up 30 cm (should return near start)
- Robot stops

**Troubleshooting:**
- **Robot doesn't move:** Check battery (is it charged?), check USB connection, re-upload
- **Robot moves wrong direction:** Motor directions might be reversed; this is normal and can be fixed later
- **Robot doesn't go exactly 30 cm:** Wheels might be slightly different sizes or battery is low; this is expected
- **Can't find robot in upload list:** Check USB connection, try different USB port, restart browser

### Independent Practice / Small Group Work (15–20 minutes)

**Exercise 1: Modify and Re-upload (Scaffolded)**

Ask students to modify the program:
- Change the distance to 20 cm (instead of 30 cm)
- Keep power at 50%
- Change the sequence: forward 20, backward 20

Expected outcome: Robot drives a smaller pattern.

Allow students to:
- Work in pairs
- Help each other troubleshoot
- Try multiple times if needed

**Exercise 2 (Optional Challenge):** 

"Add a turn in the middle. Can you make the robot drive forward, turn right, then drive backward?"

Block sequence:
```blockly
Drive forward 20 cm at 50%
Turn right 90°
Drive backward 20 cm at 50%
```

This introduces the Turn block and sequencing.

### Wrap-Up (5–10 minutes)

**Review Learning Objectives:**
- "What are the main parts of the robot?" (motor, wheels, controller, battery, sensors)
- "What does a Blockly program do?" (tells the robot commands in order)
- "How do we get the program onto the robot?" (USB upload)

**Common Misconceptions to Address:**
- Each block is a separate command; they run in order
- Distance in cm, angles in degrees, power as percentage
- The robot can't think for itself; it just follows the program you write

**Preview Next Lesson:**
"Next time, we'll make the robot draw shapes on the whiteboard. We'll use the Turn block to make it turn corners, and we'll think about math (angles) to make perfect shapes."

---

## Exercises

### Exercise 1: Drive Forward and Back (Warm-Up)

**Difficulty:** Beginner  
**Time:** 10 minutes  
**Objective:** Create and upload your first program.

**Instructions:**

1. Open xrpcode.wpi.edu
2. Create a new project called "Lesson_1_Ex1_Drive_Forward_Back"
3. In your program:
   - Start block (already there)
   - Add: Drive forward 30 cm at 50%
   - Add: Drive backward 30 cm at 50%
   - Stop block (already there)
4. Upload to your robot
5. Run the program

**Success Criteria:**
- [ ] Program uploads successfully
- [ ] Robot drives forward approximately 30 cm
- [ ] Robot drives backward approximately 30 cm
- [ ] Robot stops
- [ ] Robot ends up near where it started

**Reflection Questions:**
1. Did the robot travel exactly 30 cm? If not, why might that be?
2. What would happen if you changed the power to 100%? 20%?
3. What would happen if you removed the backward command?

---

### Exercise 2: Try Different Distances (Challenge)

**Difficulty:** Intermediate  
**Time:** 15 minutes  
**Objective:** Experiment with distances and power levels.

**Instructions:**

1. Open xrpcode.wpi.edu
2. Create a new project called "Lesson_1_Ex2_Different_Distances"
3. Build this program:
   - Drive forward 20 cm at 50%
   - Drive backward 20 cm at 50%
   - Drive forward 40 cm at 50%
   - Drive backward 40 cm at 50%
4. Upload and run

**Success Criteria:**
- [ ] Program uploads
- [ ] Robot completes all four drive commands
- [ ] You can see the difference between 20 cm and 40 cm distances

**Reflection Questions:**
1. Is it easier to control the robot with short distances or long distances?
2. What would happen if power was 10%? 90%?
3. If you wanted the robot to go twice as far, what would you change?

**Extension:**
Try adding Turn blocks:
- Drive forward 30 cm
- Turn right 90°
- Drive forward 30 cm
- Turn right 90°
- Drive forward 30 cm
- Turn right 90°
- Drive forward 30 cm

(This makes a square, which you'll do officially in Lesson 2!)

---

## Common Misconceptions

| Misconception | Reality | How to Address |
|---|---|---|
| "The robot will run my program if I just write it" | Program must be uploaded via USB first | Show upload process step-by-step; use a checklist |
| "If I write two Drive blocks, they happen at the same time" | Blocks execute in order, one after another | Show with arrow pointing down: "→ then →" |
| "Power = speed in distance" | Power affects how fast it moves, not how far in a single command | Explain: set distance separately from power |
| "The robot always goes exactly the distance I set" | Wheel friction, battery voltage, and floor surface affect actual distance | Acknowledge: "Close is good enough for now" |
| "I can run the program without uploading" | Upload creates executable code on robot; Blockly is just the editor | Show the upload step is mandatory |

---

## Assessment

**Formative Assessment (During Lesson):**
- Observation: Can students navigate XRP Code and drag blocks?
- Questions: Do they understand what a Blockly block does?
- Running program: Does it run without errors?

**Summative Assessment (End of Lesson):**
Students successfully complete Exercise 1:
- Program uploads without errors
- Robot drives forward and backward as intended
- Student can explain what each block does

**Grading (if using a rubric):**
- [ ] Program runs (10 pts)
- [ ] Robot drives forward correctly (10 pts)
- [ ] Robot drives backward correctly (10 pts)
- [ ] Can explain hardware components (5 pts)
- [ ] Can explain command sequencing (5 pts)
- **Total: 40 pts** (or just "Complete/Not Yet")

---

## Extensions & Differentiation

### For Students Who Need More Challenge

**Extension 1: Experiment with Power Levels**
- Modify the program to use different power percentages: 30%, 50%, 70%, 100%
- Measure distances and see if higher power goes farther
- Report findings: "At 100% power, the robot went ___ cm. At 30% power, it went ___ cm."

**Extension 2: Add a Turn**
- Modify to include a Turn block
- Try to make the robot return to start by doing:
  - Forward 30, turn 45°, forward 30, turn 45°, back to start?
  - (This won't form a perfect path, but it's exploratory)

**Extension 3: Create a "Circuit"**
- Drive forward 30, turn left 90°, forward 30, turn left 90° (repeat this 4 times to form a square)
- This preview's Lesson 2

### For Students Who Need More Support

**Scaffolded Version:**
- Provide a starter Blockly file with some blocks pre-filled
- Ask students to just change the distance (e.g., "Change 30 cm to 25 cm")
- Provide a checklist for upload steps (1. Plug in USB, 2. Click Upload, 3. Select robot, 4. Wait for confirmation, 5. Press robot button)

**Pair Programming:**
- Pair a confident student with one who needs support
- Roles: "Driver" (clicks and drags blocks), "Navigator" (decides what blocks to use)
- Rotate roles halfway through

**Use Starter Code:**
- Provide a screenshot of the program to rebuild (visual reference)
- Provide a text description: "First, make the robot drive forward 30 cm. Then, make it drive backward 30 cm."

---

## Resources

- **XRP Code IDE:** https://xrpcode.wpi.edu/
- **XRP Robot User Guide:** https://xrpusersguide.readthedocs.io/
- **XRP Curriculum:** https://introtoroboticsv2.readthedocs.io/
- **XRP Support Forum:** https://xrp.discourse.group/
- **Troubleshooting Guide:** See teacher-guide/xrp-setup-guide.md

---

## Notes for Instructors

### Time Management

- **For 50-min classes:** Focus on hardware tour (10 min) + one upload (30 min) + wrap-up (10 min). Skip Exercise 2 or do it next class.
- **For 3-hour sessions:** Do full lesson with both exercises and time for tinkering.

### Common Setup Issues

1. **USB not detected:**
   - Try different USB port
   - Try different cable (some cables are charge-only, not data)
   - Restart browser/computer

2. **Upload "fails":**
   - Check that robot is powered on (look for LED)
   - Wait 10 seconds before trying again
   - Try uploading again with robot unplugged, then plugged back in

3. **Robot moves slowly or erratically:**
   - Battery might be low; charge it
   - Motor might be stuck; manually spin wheels to check
   - Software version mismatch; update firmware (see xrpcode.wpi.edu setup guide)

### Classroom Management

- Have one "robot station" where you demo first
- Rotate students to try uploading in small groups
- Keep battery charger accessible
- Have a "robot hospital" area for debugging

### Next Lesson Preview

Mention: "Next lesson, we'll use the Turn block to make the robot draw shapes. We'll think about angles (like in geometry) to make perfect squares and triangles."

---

## Files

- **Starter Code:** None (students build from scratch)
- **Solution Code:** See `module-01-driving/code/solutions/lesson-01-meet-xrp.blockly` (Blockly export)
- **Worksheet:** See `module-01-driving/worksheets/01-robot-parts-labels.md`
- **Slides:** See `module-01-driving/slides/01-meet-the-xrp-slides.md`

---

## Feedback & Iteration

After teaching this lesson:
- Did students understand hardware components?
- How many struggled with USB upload?
- Did anyone finish both exercises?
- What questions came up?

Use this feedback to adjust pacing and support for Lesson 2.
