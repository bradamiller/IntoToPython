# Lesson 1 Slide Outline: Meet the XRP

## Slide 1: Title & Learning Objectives
**Title:** Meet the XRP Robot

**Learning Objectives:**
- Identify parts of the XRP robot and their functions
- Upload and run your first Blockly program
- Understand robot coordinate system and movement
- Build confidence with hands-on robotics

**Agenda:**
- Hardware tour (15 min)
- Safety & best practices (5 min)
- First program demo (10 min)
- Hands-on practice (15 min)

---

## Slide 2: Hook - What Is a Robot?
**Question:** "What makes something a robot?"

**Show:** Photos of different robots (factory robot, room vacuum, Mars rover, humanoid)

**Discussion:** What do they have in common?
- Senses (sensors)
- Thinking (code)
- Action (motors)

**Transition:** "The XRP has all three. Let's build one!"

---

## Slide 3: Meet Your Robot - The XRP
**What is XRP?**
- Stands for: eXploring Robotics Project
- Built at Worcester Polytechnic Institute (WPI)
- Educational platform for learning programming & robotics

**Size & Specs:**
- Wheeled robot ~20cm long
- Powered by rechargeable battery
- Connects to computer via USB or Bluetooth
- Runs MicroPython (robot language)

---

## Slide 4: Robot Part 1 - The Brain
**Controller Board:**
- The "brain" of the robot
- Controls motors, reads sensors, runs your code
- Three buttons: Reset, Boot Sel, User (for programs)
- Power switch on side

**Show:** Photo of board with labels
- What's the brain of YOUR robot at home?

---

## Slide 5: Robot Part 2 - The Motors
**Drive Motors (Left & Right):**
- Two motor-driven wheels
- With encoders (measure rotation)
- Controlled independently or together
- Power the robot's movement

**Optional Motors (3 & 4):**
- Additional motors for mechanisms
- Servo motor for arm/gripper

**Demo:** Show motors spinning when powered

---

## Slide 6: Robot Part 3 - The Sensors
**Sensors on XRP:**
- **Motor Encoders**: Know how far wheels have turned
- **Rangefinder**: Detect objects in front (ultrasonic)
- **Reflectance sensors**: Detect surface color/darkness
- **IMU (Inertial Measurement Unit)**: Know robot heading & tilt
- **User button**: Trigger programs

**Why sensors?**
- Let robot "see" and "feel" the world
- Used for navigation, collision detection, line-following

---

## Slide 7: Introduction to Blockly
**What is Blockly?**
- Visual programming language
- Drag-and-drop blocks (no typing)
- Blocks snap together like puzzle pieces
- Blockly → Python (translation happens automatically)

**Where?**
- XRPCode website: https://xrpcode.wpi.edu
- Works in Chrome or Edge browser
- No installation needed

**Show:** Screenshot of Blockly palette with categories

---

## Slide 8: Building Your First Program
**Program Flow:**
1. Wait for button press (safe start)
2. Turn on LED (visual feedback)
3. Drive straight 30cm
4. Turn 90°
5. Report "Complete!"

**Blockly Blocks Needed:**
- Control Board → Wait for button press
- LED → Turn LED on
- Drivetrain → Straight
- Drivetrain → Turn
- Text → Print

**Show:** Demo loading and running program on robot

---

## Slide 9: The Movement Blocks
**Straight Block:**
- Parameter: Distance (cm)
- Parameter: Effort (power 0-1)
- Robot drives forward and stops

**Turn Block:**
- Parameter: Angle (degrees)
- Parameter: Effort (power 0-1)
- Uses IMU to turn precisely
- Positive = counterclockwise, Negative = clockwise

**Interactive:** Ask students what distance/angle they'd like to test

---

## Slide 10: Safety & Best Practices
**Before Running Code:**
1. Check the floor is clear
2. Know where the robot will drive
3. Be ready to stop it if needed
4. Battery safe? (No overcharging)
5. Secure any loose cables

**During Program:**
- Stand back when code runs
- Don't block the robot's path
- Watch for signs of problems (wheel slip, spinning, stuck)

**After Program:**
- Stop the robot (power off)
- Check for damage
- Document what happened

---

## Slide 11: Your Turn!
**Activity:**
1. Open xrpcode.wpi.edu
2. Create new Blockly program
3. Build: Wait → Straight(30) → Turn(90) → Print "Done"
4. Test on your robot

**Checkpoints:**
- Program loads without errors?
- Robot moves forward?
- Robot turns?
- Program finishes?

**Success:** Your first robot program works!

---

## Slide 12: Connection to Next Lesson
**What You Did Today:**
- Met the robot hardware
- Learned basic movement blocks
- Uploaded and ran code

**Next Lesson (Lesson 2):**
- Use **Repeat blocks** to make shapes
- Combine straight + turn in loops
- Learn about angles and geometry

**Challenge:** How would you make the robot draw a square?
