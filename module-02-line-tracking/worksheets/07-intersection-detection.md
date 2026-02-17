# Lesson 7 Worksheet: Intersection Detection

**Name:** ________________________
**Date:** ________________________

---

## Part 1: Sensor States at the Intersection

For each robot position, predict the sensor readings and whether a cross is detected:

| Position | Left Sensor | Right Sensor | `left > 0.5 and right > 0.5` | Cross? |
|---|---|---|---|---|
| Following line (left on line, right off) | ~0.8 | ~0.2 | __________ | __________ |
| Following line (right on line, left off) | ~0.2 | ~0.8 | __________ | __________ |
| At the cross (both on line) | ~0.8 | ~0.8 | __________ | __________ |
| Off the line completely | ~0.2 | ~0.2 | __________ | __________ |
| On white, near the edge | ~0.4 | ~0.3 | __________ | __________ |

---

## Part 2: and vs. or

For each condition, write the result (True or False):

| left | right | `left > 0.5 and right > 0.5` | `left > 0.5 or right > 0.5` |
|---|---|---|---|
| 0.8 | 0.9 | __________ | __________ |
| 0.8 | 0.2 | __________ | __________ |
| 0.2 | 0.8 | __________ | __________ |
| 0.1 | 0.1 | __________ | __________ |

**When do we use `and`?** ________________________________________________

**When do we use `or`?** ________________________________________________

---

## Part 3: Code Tracing

Trace through this code with the given sensor values and write what happens:

```python
threshold = 0.5
Kp = 0.5
base_effort = 0.3

left = 0.8    # Sensor reading
right = 0.9   # Sensor reading

if left > threshold and right > threshold:
    drivetrain.stop()
    print("Cross detected!")
    drivetrain.turn(180)
else:
    error = left - right
    left_effort = base_effort - error * Kp
    right_effort = base_effort + error * Kp
    drivetrain.set_effort(left_effort, right_effort)
```

**Which branch runs?** (if / else) __________

**What gets printed?** __________

Now with `left = 0.7, right = 0.2`:

**Which branch runs?** (if / else) __________

**Calculate:** error = __________, left_effort = __________, right_effort = __________

---

## Part 4: Putting It Together

Number these steps in the correct order for the robot's behavior:

___ The robot continues following the line in the opposite direction
___ The robot detects both sensors above threshold
___ The robot follows the line using proportional control
___ The robot stops at the intersection
___ The robot turns 180 degrees
___ time.sleep(0.3) prevents re-detection

---

## Part 5: Design Question

**Why do we need `time.sleep(0.3)` after turning at the cross?**

____________________________________________________________________

**What would happen without it?**

____________________________________________________________________

**Could we use a different approach instead of time.sleep?** Describe one:

____________________________________________________________________

---

## Part 6: Counting Crosses

If the robot follows a circle with one cross and we want it to stop after 4 reversals:

**What type of loop should we use?** (for / while / while True) __________

**Write the loop condition:**

```python
while ________________________________:
    # follow and detect code
```

**What variable do we need to track?** __________

**When does the loop end?** __________

---

## Reflection

**This lesson combined line following (Lessons 5-6) with intersection detection. Why is it important to check for the cross BEFORE doing normal line following in the if/else?**

_________________________________________________________________

_________________________________________________________________

---

**Next Lesson:** We'll package all this sensor logic into a reusable Python CLASS — your first class!
