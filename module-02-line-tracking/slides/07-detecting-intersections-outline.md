# Lesson 7 Slide Outline: Detecting Intersections

## Slide 1: Title & Learning Objectives
**Title:** Detecting Intersections

**Learning Objectives:**
- Detect when both sensors are on the line simultaneously
- Use the `and` logical operator for combined conditions
- Integrate intersection detection with line following
- Program the robot to reverse direction at a cross

**Agenda:**
- What intersections look like to sensors (10 min)
- Cross detection code (15 min)
- Follow + detect + reverse (20 min)

---

## Slide 2: Adding the Cross
**New physical setup:** A taped cross — a perpendicular line crossing the circle.

**Question:** "When the robot reaches this cross while following the line, what will the sensors see?"

**Answer:** BOTH sensors will be on the line at the same time!

---

## Slide 3: How Sensors See an Intersection
**During normal line following:**
- One sensor on line, one off → different values
- `left ≈ 0.8, right ≈ 0.2` or vice versa

**At an intersection (cross):**
- BOTH sensors on the line → both read high
- `left > 0.5 AND right > 0.5`

**This is our detection signal!**

---

## Slide 4: The `and` Operator
```python
if left > 0.5 and right > 0.5:
    print("CROSS DETECTED!")
```

**`and` truth table:**
| left > 0.5 | right > 0.5 | Result |
|---|---|---|
| True | True | **True** ← Cross! |
| True | False | False |
| False | True | False |
| False | False | False |

**Both must be True for `and` to be True.**

---

## Slide 5: Line Following + Cross Detection
```python
while True:
    left = reflectance.get_left()
    right = reflectance.get_right()

    if left > threshold and right > threshold:
        # Cross detected!
        drivetrain.stop()
        print("Cross!")
        drivetrain.turn(180)
        time.sleep(0.3)
    else:
        # Normal line following
        error = left - right
        left_effort = base_effort - error * Kp
        right_effort = base_effort + error * Kp
        drivetrain.set_effort(left_effort, right_effort)
```

**Check for cross FIRST, then do normal following.**

---

## Slide 6: Why time.sleep() After Turning?
**Without sleep:** Robot turns 180° → immediately re-reads sensors → still at the cross → turns again!

**With sleep(0.3):** Robot turns 180° → pauses briefly → moves past the cross → resumes following

**The sleep gives the robot time to move away from the intersection.**

---

## Slide 7: Counting Crossings
```python
cross_count = 0

while cross_count < 4:
    left = reflectance.get_left()
    right = reflectance.get_right()

    if left > threshold and right > threshold:
        cross_count = cross_count + 1
        drivetrain.stop()
        print("Cross #", cross_count)
        drivetrain.turn(180)
        time.sleep(0.3)
    else:
        # line following code...

print("Done! Crossed", cross_count, "times.")
```

**This previews the final project!**

---

## Slide 8: Your Turn!
**Exercise 1:** Follow the circle and reverse at the cross
- Use two-sensor line following from Lesson 6
- Add cross detection with `and`
- Turn 180° when cross is detected

**Exercise 2 (Challenge):** Count crossings and stop after 4

**Test:** Does the robot reliably detect the cross?

---

## Slide 9: Connection to Next Lesson
**What you've built so far (all as loose code):**
- Sensor reading, error calculation, cross detection
- Proportional control, differential steering
- All mixed together in one big program

**Next (Lesson 8):** Package sensor logic into a **LineSensor class**
- `get_error()`, `is_at_cross()`, `is_off_line()`
- First time writing a Python class!

**Why?** Organized code is easier to understand, test, and reuse.
