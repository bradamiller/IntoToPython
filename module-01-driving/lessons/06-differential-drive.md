# Lesson 6: Differential Drive & Motor Control Blocks

## Overview
Students transition from the abstracted `straight()` and `turn()` functions to lower-level **Differential Drive** and **Individual Motor** blocks. This lesson explores how the robot actually moves—controlling left and right motors independently using effort levels. Students will understand that `straight()` and `turn()` are built on top of motor control, and they can do more by controlling motors directly.

## Learning Objectives
By the end of this lesson, students will be able to:
- Understand differential drive concepts (left/right motor independent control)
- Use **set_effort** block to control motor power directly
- Use **arcade** block for steering with proportional control
- Compare high-level vs. low-level movement commands
- Recognize when to use each approach

## Key Concepts
- **Differential drive**: Robot that steers by varying left/right motor speeds
- **Effort**: Raw motor power (-1 to 1, where -1 is full reverse, 1 is full forward)
- **Arcade control**: Forward speed + turn amount (steering angle)
- **Proportional control**: Turn amount scales with turn parameter
- **Motor symmetry**: Equal left/right effort = straight; different efforts = curved motion
- **Trade-off**: More control (motors) vs. more abstraction (straight/turn)

## Materials Required
- XRP Robot with clear driving space
- xrpcode.wpi.edu access
- Reference: Blockly Dictionary (Motor and Drivetrain sections)
- Measuring tape to track robot position
- Whiteboard for motor effort combinations

## Lesson Flow

### Introduction (12 minutes)
**For 50-min classes:** 8 min
**For 3-hour sessions:** 12-15 min

1. **Hook: Transparency Question**:
   - Show: A program using `straight(30)` and `turn(90°)`
   - Ask: "What's the robot actually doing? How does it turn?"
   - Students may guess: "Stopping the motors" or "Spinning in place"
   - Reveal: "It's controlling LEFT and RIGHT motors SEPARATELY"

2. **Introduce Differential Drive Concept**:
   - Show simple diagram:
     ```
     Left motor at 0.5  +  Right motor at 0.5  = Robot goes straight
     Left motor at 0.5  +  Right motor at 0.0  = Robot curves left
     Left motor at -0.5 +  Right motor at 0.5  = Robot spins right
     ```
   - Insight: By controlling motors differently, we can make any motion
   - Example: Smooth curves, arcs, "dancing" patterns, precise maneuvers

3. **Contrast: Abstraction vs. Control**:
   - High-level (Lessons 1-5): `straight(30)` - Robot figures out motors
   - Low-level (this lesson): Individual motor control - We figure out motors
   - Trade-off: Easy vs. Powerful

4. **Introduce Blockly Blocks**:
   - **Set effort(left, right)**: Direct motor control (-1 to 1 for each)
   - **Arcade(speed, turn)**: Proportional steering (easier for human-like control)
   - **Wait(seconds)**: Needed because motors run continuously until stopped

### Guided Practice: Understanding Motor Combinations (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 20-25 min

1. **The Set Effort Block**:
   - Drag: **Set effort** block (Drivetrain category)
   - Parameters: left effort, right effort
   - Behavior: Set motors and let them run continuously
   - Unlike `straight()`, we must add our own `stop motors` command

2. **Test: Straight Movement**:
   - Program:
     ```blockly
     Wait for button press
     Set effort (left: 0.5, right: 0.5)
     Wait 3 seconds
     Stop motors
     ```
   - Prediction: Robot drives straight forward at 50% power for 3 seconds
   - Run and observe: Does it go straight? (Should, if wheels are balanced)
   - Measurement: How far did it travel? (Varies by surface)

3. **Test: Left Turn**:
   - Program:
     ```blockly
     Wait for button press
     Set effort (left: 0.3, right: 0.5)
     Wait 3 seconds
     Stop motors
     ```
   - Prediction: Robot curves left (right motor faster)
   - Run and observe: Does it turn left?
   - Measurement: What's the radius of the curve?

4. **Test: Spin in Place**:
   - Program:
     ```blockly
     Wait for button press
     Set effort (left: 0.5, right: -0.5)
     Wait 2 seconds
     Stop motors
     ```
   - Prediction: Left motor forward, right motor backward → counterclockwise rotation
   - Run and observe: Robot spins!
   - Note: This is different from `turn()`—it doesn't use IMU, just motor speeds

5. **Compare to Lesson 1 Turn**:
   - Discuss differences:
     - `turn(90°)`: Uses IMU sensor, precise angle, stops at exact heading
     - `set_effort(0.5, -0.5)`: Raw motors, no angle measurement, "kind of spins"
   - When to use each: Precision vs. Simplicity

6. **Introduce Arcade Block** (Easier steering):
   - Drag: **Arcade(speed, turn)** block
   - Parameters: 
     - speed: Forward speed (-1 to 1)
     - turn: Turn amount (-1 to 1), where negative = left, positive = right
   - Behavior: Combines speed and steering in one command (like a game controller)
   - Advantage: More intuitive than separate left/right efforts

7. **Test: Arcade Steering**:
   - Program:
     ```blockly
     Wait for button press
     Arcade (speed: 0.5, turn: 0.3)
     Wait 3 seconds
     Stop motors
     ```
   - Prediction: Robot drives forward at 50% speed while turning slightly right
   - Run and observe: Smooth curve to the right
   - Arcade is proportional: More turn = tighter curve; less turn = wider curve

### Independent Practice: Motor Exploration (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

**Exercise 1: Figure-Eight Pattern**
- Goal: Use set_effort to draw a figure-eight
- Idea: Left curve, then right curve
- Steps:
  ```blockly
  Wait for button press
  Set effort (left: 0.3, right: 0.5)  ← Right turn
  Wait 3 seconds
  Set effort (left: 0.5, right: 0.3)  ← Left turn
  Wait 3 seconds
  Stop motors
  ```
- Result: Robot traces a curvy S-shape (not a perfect figure-eight, but close)
- Challenge: Adjust times or efforts to make the pattern more symmetric

**Exercise 2: Spiral Pattern**
- Goal: Gradually change motor efforts to create a spiral
- Idea: Start wheels at same effort, gradually increase one side
- Concept: This requires multiple set_effort commands sequentially
- Advanced approach:
  ```blockly
  Set effort (left: 0.2, right: 0.5)
  Wait 2 seconds
  Set effort (left: 0.3, right: 0.5)
  Wait 2 seconds
  Set effort (left: 0.4, right: 0.5)
  Wait 2 seconds
  Stop motors
  ```
- Result: Robot spirals outward
- Challenge: What if we reverse? (Spirals inward)

**Exercise 3: Compare Approaches**
- Goal: Draw the same shape using `straight/turn` vs. `set_effort`
- Task 1: Use Lessons 1-5 code to draw a square with `straight()` and `turn()`
- Task 2: Use `set_effort` to approximate a square (harder without IMU)
- Observation:
  - Approach 1 is precise, returns to start, predictable
  - Approach 2 is harder to get exact, but shows the "under the hood" mechanics
- Conclusion: High-level abstractions hide complexity (good for basic tasks); low-level control gives power (good for creative movement)

**Exercise 4: Arcade Challenge**
- Goal: Use arcade block to navigate a simple obstacle course
- Setup: Mark a path with obstacles (cones, tape, etc.)
- Task: Drive through course using arcade block
  - Forward sections: `arcade(0.5, 0)`
  - Left turns: `arcade(0.3, -0.5)`
  - Right turns: `arcade(0.3, 0.5)`
  - Tight turns: `arcade(0.1, -1.0)`
- Observation: Arcade is more natural for smooth navigation than set_effort

### Assessment

**Formative (during lesson)**:
- Can students predict motor behavior from effort values?
- Do they understand when proportional control (arcade) is easier than direct motor control?
- Can they recognize the relationship between high-level and low-level movement?

**Summative (worksheet/exit ticket)**:
1. If left motor = 0.5 and right motor = 0.3, will the robot go straight? Why/why not?
2. Fill in efforts to make the robot spin clockwise: left = ____, right = ____ 
3. When would you use `set_effort(0.5, 0.5)` instead of `straight(30)`?
4. Explain: "Arcade is like steering a car; set_effort is like controlling each wheel separately"

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "Higher effort is always faster" | Effort is power; speed depends on load, surface, battery voltage |
| "set_effort(-0.5, 0.5) makes a left turn" | It makes a rightward turn (right wheel faster) |
| "Arcade block is always better" | Arcade is better for smooth steering; set_effort gives precise motor control |
| "I can ignore stop motors" | Motors keep running; they'll drain battery or cause unexpected behavior |
| "Effort 0.0 is slower than 0.1" | 0.0 is stopped; 0.1 is running at 10% power |

## Differentiation

**For struggling students**:
- Provide a table of effort combinations with expected results
- Start with symmetric efforts only (0.3, 0.3 or 0.6, 0.6) before curves
- Work through Exercise 1 as a group; have them modify it
- Use arcade block first (more intuitive) before diving into set_effort
- Provide a checklist: "Always stop motors? Y/N"

**For advanced students**:
- Challenge: Create a function `move_forward_for_distance()` using set_effort + timer + distance estimation
  - Without encoders or straight/turn, estimate distance by time
  - May not be accurate, but shows the challenge of low-level control
- Design: Create a "smooth turn" that's not instant (gradually phase out left, speed up right)
- Research: How do game controllers map to robot movement? What's the math?
- Extension: Implement PID-like control manually by adjusting efforts based on observed behavior

## Materials & Code Examples

### Set Effort for Straight
```blockly
Wait for button press
Set effort (left: 0.5, right: 0.5)
Wait 3 seconds
Stop motors  ← Critical!
```

### Set Effort for Curves
```blockly
Set effort (left: 0.3, right: 0.5)  ← Right turn
Wait 3 seconds
Stop motors

Set effort (left: 0.5, right: 0.3)  ← Left turn
Wait 3 seconds
Stop motors
```

### Arcade for Steering
```blockly
Wait for button press
Arcade (speed: 0.5, turn: 0.2)  ← Forward w/ slight right
Wait 3 seconds
Stop motors
```

### Python Equivalent (Reference for Teachers)
```python
from XRPLib.differential_drive import DifferentialDrive
import time

drivetrain = DifferentialDrive.get_default_differential_drive()
board = Board.get_default_board()

board.wait_for_button_press()

# Set effort approach
drivetrain.set_effort(0.5, 0.5)  # left_effort, right_effort
time.sleep(3)
drivetrain.set_effort(0, 0)

# Arcade approach (may not exist in all XRPLib versions)
# drivetrain.arcade(0.5, 0.2)  # speed, turn
```

## Teaching Notes
- **Stop motors is critical**: Emphasize that motors keep running; students often forget to stop
- **Asymmetry due to hardware**: If robot doesn't go straight at (0.5, 0.5), wheels may be slightly misaligned—it's a hardware issue, not a programming error
- **Time vs. encoder trade-off**: Set_effort uses timing (imprecise); straight/turn uses encoders (precise)
- **Proportional steering**: Arcade block is easier to learn but less precise than direct motor control
- **Common errors**:
  - Forgetting stop motors (motors stay at last effort)
  - Confusing left/right sign conventions
  - Assuming effort 0.5 always goes the same speed (depends on battery, load)
- **Success criteria**: Program runs, motors stop on command, student can explain motor behavior from effort values

## Connections to Next Lessons
- Lesson 7 will use these motor control blocks to create more complex challenges and behaviors
- Python Lesson 9 will use the same `set_effort()` and potentially `arcade()` concepts
- Advanced courses may use these blocks for line-following, obstacle avoidance, and swarm robotics
