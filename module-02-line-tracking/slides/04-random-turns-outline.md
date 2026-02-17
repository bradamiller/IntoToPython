# Lesson 4 Slide Outline: Random Turns

## Slide 1: Title & Learning Objectives
**Title:** Random Turns

**Learning Objectives:**
- Use `import` to bring in Python's `random` module
- Generate random numbers with `random.randint()`
- Explain why predictable behavior is a problem
- Modify bounce driving to use random turn angles

**Agenda:**
- The predictability problem (5 min)
- import and random module (10 min)
- Random bounce driving (15 min)
- Experimentation (15 min)

---

## Slide 2: The Predictability Problem
**Observe the Lesson 3 robot:**
- Drives forward → hits line → turns 180° → drives back → hits line → turns 180°...
- **Same path every time!** Never explores the circle.

**Why?** 180° always sends it straight back.

**Fix:** Turn a DIFFERENT amount each time → explore the whole area.

---

## Slide 3: import — Using Python Modules
**Python has thousands of built-in tools** organized into modules.

**To use one:** `import module_name`

```python
import random      # Makes random functions available
import time        # Makes time functions available
```

**You've already done this:**
```python
from XRPLib.reflectance import Reflectance
```

**Rule:** Import at the TOP of your file.

---

## Slide 4: random.randint()
**`random.randint(a, b)`** — returns a random integer between a and b (inclusive)

```python
import random

random.randint(1, 6)    # Like rolling a die: 1, 2, 3, 4, 5, or 6
random.randint(90, 270)  # Random angle for turning
random.randint(1, 100)   # Random percentage
```

**Each call gives a DIFFERENT number:**
```python
print(random.randint(1, 10))  # Maybe 7
print(random.randint(1, 10))  # Maybe 3
print(random.randint(1, 10))  # Maybe 9
```

---

## Slide 5: Adding Randomness to Bounce Driving
**Before (predictable):**
```python
drivetrain.turn(180)  # Always 180°
```

**After (random):**
```python
angle = random.randint(90, 270)
print("Turning", angle, "degrees")
drivetrain.turn(angle)
```

**Result:** Robot turns a different amount each bounce → explores the circle!

---

## Slide 6: Complete Random Bounce Program
```python
from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board
import random

reflectance = Reflectance.get_default_reflectance()
drivetrain = DifferentialDrive.get_default_differential_drive()
board = Board.get_default_board()

threshold = 0.5
board.wait_for_button()

while True:
    left = reflectance.get_left()
    right = reflectance.get_right()

    if left > threshold or right > threshold:
        drivetrain.stop()
        angle = random.randint(90, 270)
        print("Turning", angle, "degrees")
        drivetrain.turn(angle)
    else:
        drivetrain.set_effort(0.3, 0.3)
```

---

## Slide 7: Experimenting with Ranges
**Try different ranges and observe:**

| Range | Behavior |
|---|---|
| `randint(170, 190)` | Small variation around 180° — mostly back and forth |
| `randint(90, 270)` | Wide range — good exploration |
| `randint(45, 315)` | Very wide — may turn too little sometimes |
| `randint(90, 90)` | Always 90° — not random at all! |

**Question:** Which range keeps the robot inside the circle best?

---

## Slide 8: Your Turn!
**Exercise 1:** Add random turns to your bounce program
- Change `drivetrain.turn(180)` to use `random.randint()`

**Exercise 2 (Challenge):** Experiment with different ranges
- Record which range works best

**Bonus:** Randomize the speed too!

---

## Slide 9: Connection to Next Lesson
**Module 2 so far:**
- Lesson 1: Read sensors ✓
- Lesson 2: While loops — drive to edge ✓
- Lesson 3: if/else — bounce driving ✓
- Lesson 4: import random — random turns ✓

**Next (Lesson 5):** Instead of BOUNCING off the line, FOLLOW it!
- **Proportional control** — smooth, continuous line following
- The robot adjusts steering based on how far it is from the line

**Big shift:** From bouncing to tracking!
