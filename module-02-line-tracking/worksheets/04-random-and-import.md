# Lesson 4 Worksheet: Random Numbers and Import

**Name:** ________________________
**Date:** ________________________

---

## Part 1: import and Modules

1. **What does `import random` do?**

   ____________________________________________________________________

2. **Where should `import` statements go in your code?**

   ____________________________________________________________________

3. **Name two modules we have imported so far in this course:**

   a. ________________________________

   b. ________________________________

---

## Part 2: random.randint() Predictions

For each call, write ALL the possible values it could return:

| Call | Possible Values |
|---|---|
| `random.randint(1, 3)` | ________________________ |
| `random.randint(5, 5)` | ________________________ |
| `random.randint(0, 1)` | ________________________ |
| `random.randint(10, 15)` | ________________________ |
| `random.randint(90, 270)` | "Any integer from ___ to ___" |

---

## Part 3: Why Randomness?

1. **What happens when the robot always turns exactly 180°?**

   ____________________________________________________________________

2. **What happens when the robot turns a random angle between 90° and 270°?**

   ____________________________________________________________________

3. **Why is the range 90–270 better than 10–350?**

   ____________________________________________________________________

4. **What would happen with `random.randint(0, 360)`? Why might this be a problem?**

   ____________________________________________________________________

---

## Part 4: Code Prediction

```python
import random

for i in range(5):
    angle = random.randint(1, 4)
    if angle == 1:
        print("North")
    elif angle == 2:
        print("East")
    elif angle == 3:
        print("South")
    else:
        print("West")
```

**Can you predict the exact output?** (yes/no) __________

**Why or why not?** ____________________________________________________________________

**How many lines of output will there be?** __________

---

## Part 5: Design Challenge

You want the robot to turn a random amount, but you want it to always turn AT LEAST 120° and AT MOST 240°.

**Write the `random.randint()` call:**

```python
angle = random.randint(_____, _____)
```

Now you want the robot to drive at a random speed between 20% and 60% power. The effort value needs to be between 0.2 and 0.6.

**Hint:** Generate a random integer and divide by 100.

```python
speed_percent = random.randint(_____, _____)
effort = speed_percent / 100
```

---

## Part 6: Experiment Results

Record the behavior for each random range:

| Range | Robot Behavior |
|---|---|
| `randint(170, 190)` | ________________________________ |
| `randint(90, 270)` | ________________________________ |
| `randint(45, 315)` | ________________________________ |

**Which range worked best for staying inside the circle?** __________

**Why do you think that range worked best?**

____________________________________________________________________

---

## Reflection

**What is one thing `import` lets you do that you couldn't do without it?**

_________________________________________________________________

---

**Next Lesson:** We stop bouncing and start FOLLOWING the line using proportional control!
