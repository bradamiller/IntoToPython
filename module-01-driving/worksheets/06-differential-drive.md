# Lesson 6 Worksheet: Differential Drive & Motor Control

**Name:** __________________ **Date:** __________________ **Team:** __________________

## Part 1: Motor Effort Combinations

Fill in the table showing what the robot does for each motor effort combination.

| Left Motor | Right Motor | Expected Behavior |
|---|---|---|
| 0.5 | 0.5 | Goes _________________ |
| 0.5 | 0.0 | Curves _________________ |
| 0.0 | 0.5 | Curves _________________ |
| 0.5 | -0.5 | _________________ in place |
| -0.5 | 0.5 | _________________ in place (opposite direction) |
| 0.3 | 0.3 | Goes _________________ (slower) |
| 0.0 | 0.0 | _________________ (no motion) |

## Part 2: Predict Motor Behavior

Draw arrows showing the direction of rotation for each motor, then predict robot motion.

**Scenario A:**
```
Left motor: 0.5 (forward)
Right motor: 0.5 (forward)

Left wheel: ↑ (forward)
Right wheel: ↑ (forward)

Robot moves: STRAIGHT / LEFT / RIGHT / SPINS
```

**Scenario B:**
```
Left motor: 0.3 (forward)
Right motor: 0.6 (forward)

Left wheel: slower forward
Right wheel: faster forward

Robot moves: STRAIGHT / LEFT / RIGHT / SPINS
```

**Scenario C:**
```
Left motor: 0.5 (forward)
Right motor: -0.5 (backward)

Left wheel: ↑ (forward)
Right wheel: ↓ (backward)

Robot moves: STRAIGHT / LEFT / RIGHT / SPINS
```

## Part 3: Effort vs. Arcade Control

Compare two ways to control the robot:

**Method 1: Set Effort (Direct Motor Control)**
```blockly
Set effort (left: 0.5, right: 0.3)
Wait 3 seconds
Stop motors
```

**Method 2: Arcade (Steering Control)**
```blockly
Arcade (speed: 0.5, turn: 0.2)
Wait 3 seconds
Stop motors
```

**Questions:**

1. Which method is easier to understand? ____________________________

2. Which method is more precise? ____________________________

3. When would you use Method 1? ________________________________________

4. When would you use Method 2? ________________________________________

## Part 4: Compare to Straight/Turn

**Approach 1: High-Level (Lesson 1)**
```blockly
Straight(100)
Turn(90°)
```

**Approach 2: Motor Control (This Lesson)**
```blockly
Set effort (left: 0.5, right: 0.5)
Wait 4 seconds
Stop motors
Set effort (left: 0.5, right: -0.5)
Wait 1 second
Stop motors
```

**Compare:**

| Aspect | Straight/Turn | Set Effort |
|---|---|---|
| Precision | _____________ | _____________ |
| Ease of use | _____________ | _____________ |
| Control | _____________ | _____________ |
| Predictability | _____________ | _____________ |

## Part 5: Design Motor Programs

**Task 1: Create a Figure-Eight Pattern**

Design a set_effort program that makes the robot trace a figure-eight:

```blockly
[Your program here]
Set effort (left: ____, right: ____)
Wait ____ seconds

[Turn]
Set effort (left: ____, right: ____)
Wait ____ seconds

[etc.]
```

**Task 2: Create a Spiral Pattern**

Design a program where the robot spirals outward by gradually changing effort:

```blockly
[Your program here]
```

## Part 6: Debugging Motor Problems

**Problem 1: Robot spins instead of going straight**

You intended: `Set effort (left: 0.5, right: 0.5)`

Possible causes:
- Wheels are _________________ sized
- Motors have _________________ amounts of friction
- Surface is _________________ (tilted)

Solution: ________________________________________________________________

**Problem 2: Robot doesn't respond to motor commands**

Possible causes:
- _________________ is disconnected
- _________________ is too low
- Code has _________________ error

Solution: ________________________________________________________________

## Part 7: Motor Math

**If the robot's wheel diameter is 7cm and 1 motor rotation = 1 circle:**

- At 0.5 effort, the robot travels approximately _____ cm per second
- At 0.7 effort, the robot travels approximately _____ cm per second
- Higher effort = _________________ speed

**Prediction Challenge:**
```blockly
Set effort (left: 0.5, right: 0.5)
Wait 2 seconds
```

Distance traveled ≈ _____ cm (estimate: _____ cm/sec × 2 sec)

## Part 8: Real-World Comparison

**In a real car:**
- Gas pedal = effort (0-1)
- Steering wheel = turn amount (-1 to 1)
- ABS prevents wheels from locking = safety features

**How is the XRP robot like a car?**

_________________________________________________________________

**How is it different?**

_________________________________________________________________

## Reflection

**Explain the difference between:**
- `straight(100)` - ___________________________________________________________
- `set_effort(0.5, 0.5); wait 2; stop motors` - ____________________________

_________________________________________________________________

**When would an engineer prefer each approach?**

_________________________________________________________________
