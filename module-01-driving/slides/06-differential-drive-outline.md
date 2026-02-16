# Lesson 6 Slide Outline: Differential Drive & Motor Control

## Slide 1: Title & Learning Objectives
**Title:** Differential Drive & Motor Control

**Learning Objectives:**
- Understand how differential drive steering works
- Control motors independently with set_effort
- Compare high-level (Straight/Turn) vs. low-level (set_effort) control
- Design complex movement patterns

**Agenda:**
- Motor basics review (5 min)
- set_effort block introduction (5 min)
- Guided: Arcade control patterns (8 min)
- Challenge: Design figure-eight and spiral (15 min)

---

## Slide 2: Hook - How Does a Robot Turn?
**Scenario:** You have two motors

**Straight:** Both motors at same speed
```
Left motor: 50% effort →
Right motor: 50% effort →
Result: Robot goes straight
```

**Turn Right:** Left motor faster than right
```
Left motor: 70% effort →
Right motor: 30% effort →
Result: Robot curves right
```

**Question:** "How much effort on each motor to make the robot turn 90°?"
**This is differential drive steering!**

---

## Slide 3: Motor Control Architecture
**Two-Motor Drive System:**

| Component | Function |
|-----------|----------|
| Left Motor | Controls left wheel speed |
| Right motor | Controls right wheel speed |
| Combined effect | Steering (turn left/right) |

**Effort Range:** 0.0 to 1.0
- 0.0 = Stopped
- 0.5 = Half speed
- 1.0 = Full speed

**Negative Effort:**
- Reverses motor direction
- -0.5 = Half speed backward

---

## Slide 4: The set_effort Block
**What it does:** Set motor speed directly (NOT distance-based)

**Syntax:**
```
Set left_motor effort to [0.5]
Set right_motor effort to [0.5]
```

**Differences from Straight:**
- **Straight:** "Go forward 30cm" (robot does it)
- **set_effort:** "Run at 50% speed" (keeps running until you stop it)

**When to use set_effort:**
- ✓ Continuous motion (don't know distance)
- ✓ Obstacle avoidance (change speed based on sensors)
- ✗ Precise distance (use Straight instead)

---

## Slide 5: Straight Line Movement
**Balanced Effort:**
```
Set left_motor effort to [0.5]
Set right_motor effort to [0.5]
Wait [2] seconds
Set left_motor effort to [0]
Set right_motor effort to [0]
```

**Result:**
- Both motors same speed
- Robot goes forward 2 seconds
- Then stops

**Key:** Equal effort = straight line

---

## Slide 6: Turning Right
**Asymmetric Effort:**
```
Set left_motor effort to [0.7]   ← Left faster
Set right_motor effort to [0.3]  ← Right slower
Wait [1] second
Set left_motor effort to [0]
Set right_motor effort to [0]
```

**What Happens:**
- Left wheel travels faster
- Robot pivots around right wheel
- Results in clockwise turn

**Effort Difference:**
- Just slightly unequal: Gentle curve
- Very unequal: Sharp turn

---

## Slide 7: Turning Radius & Control
**Gentle Turn (subtle effort difference):**
```
Left: 0.6, Right: 0.4 → Wide curve
```

**Sharp Turn (large effort difference):**
```
Left: 0.8, Right: 0.2 → Tight curve
```

**Spin in Place (opposite efforts):**
```
Left: 0.5, Right: -0.5 → Rotates without moving forward
```

**Relationship:**
- Effort difference → Steering sharpness
- Motor speed → Forward/backward speed

---

## Slide 8: Arcade Control Pattern
**Simpler abstraction for differential drive:**

```
def arcade_drive(forward_speed, turn_rate):
    left_effort = forward_speed + turn_rate
    right_effort = forward_speed - turn_rate
```

**Parameters:**
- **forward_speed:** -1 to 1 (negative = backward)
- **turn_rate:** -0.5 to 0.5 (negative = turn left)

**Examples:**
```
arcade_drive(0.5, 0):     ✓ Straight forward at 50%
arcade_drive(0.5, 0.3):   ✓ Forward + turn right
arcade_drive(0, 0.5):     ✓ Spin right in place
arcade_drive(-0.5, 0.3):  ✓ Backward while turning right
```

---

## Slide 9: Complex Movement Patterns
**Figure-Eight Pattern:**
```
Turn right (effort 0.7, 0.3) for 1.5 seconds
Turn left (effort 0.3, 0.7) for 1.5 seconds
Repeat to create infinity loop
```

**Spiral Pattern:**
```
Start: 0.5, 0.5 (straight)
Gradually: Left motor increases, right decreases
Create outward spiral
```

**Zigzag Pattern:**
```
Straight (0.5, 0.5) for 1 second
Turn left (0.3, 0.7) for 0.5 second
Turn right (0.7, 0.3) for 0.5 second
Repeat
```

---

## Slide 10: set_effort vs. Straight Comparison
**Movement Comparison:**

| Task | Use set_effort | Use Straight |
|------|--------|----------|
| Go forward exactly 50cm | ✗ | ✓ |
| Continuous movement | ✓ | ✗ |
| Obstacle avoidance | ✓ | ✗ |
| Precise path | ✗ | ✓ |
| Speed control only | ✓ | - |
| Complex patterns | ✓ | ✗ |

**Key Difference:**
- **set_effort:** You manage duration (with Wait blocks)
- **Straight:** Robot manages distance (you just specify it)

---

## Slide 11: Safety with Continuous Motion
**Always Include:**
1. Set effort (start motor)
2. Wait (duration)
3. Set effort to 0 (stop motor!)

**DANGER - No Wait Block:**
```
Set left_motor to 0.5
Set right_motor to 0.5
→ Robot NEVER STOPS (infinite forward)
→ Crashes into wall
```

**DANGER - No Stop Block:**
```
Set left_motor to 0.5        ← Goes forward
... later ...
Set left_motor to 0.7        ← Changes speed, keeps going
→ No explicit stop → keeps moving
```

**CORRECT:**
```
Set left_motor to 0.5
Wait 2 seconds
Set left_motor to 0   ← STOP!
```

---

## Slide 12: Connection to Python (Lessons 9-10)
**Preview:**
- Today: Blockly set_effort blocks for motor control
- Lesson 9: Python loops to automate Wait/set_effort cycles
- Lesson 10: Python functions for arcade_drive and patterns

**Python Version (sneak peek):**
```python
left_motor = 0.5
right_motor = 0.5
wait(2)
left_motor = 0
right_motor = 0
```

**Teaser:** "Python makes repeated motor patterns much cleaner!"
