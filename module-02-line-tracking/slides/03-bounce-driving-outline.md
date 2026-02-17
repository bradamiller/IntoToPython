# Lesson 3 Slide Outline: Bounce Driving

## Slide 1: Title & Learning Objectives
**Title:** Bounce Driving

**Learning Objectives:**
- Write `if/else` statements in Python
- Use `while True` for continuous robot behavior
- Combine sensor checks with decision-making
- Program the robot to bounce between circle edges

**Agenda:**
- if/else explained (10 min)
- Bounce driving walkthrough (15 min)
- Practice and experiment (20 min)

---

## Slide 2: From Stopping to Bouncing
**Lesson 2:** Robot drives to edge → STOPS. Done.

**Today:** Robot drives to edge → TURNS AROUND → drives again → repeat forever!

**Like a ball bouncing off walls.**

---

## Slide 3: if/else Syntax
```python
if condition:
    # runs when condition is True
else:
    # runs when condition is False
```

**Example:**
```python
temperature = 85
if temperature > 80:
    print("It's hot!")
else:
    print("It's comfortable.")
```

**Only ONE block runs — never both.**

---

## Slide 4: if/else for Robot Decisions
```python
left = reflectance.get_left()

if left > threshold:
    # ON the line — turn around!
    drivetrain.stop()
    drivetrain.turn(180)
else:
    # OFF the line — keep driving
    drivetrain.set_effort(0.3, 0.3)
```

**The robot checks the sensor and decides what to do.**

---

## Slide 5: while True — The Infinite Loop
```python
while True:
    # this code runs FOREVER
```

**Why?** `True` is always True — the condition never becomes False.

**For robots:** The robot should keep running until you turn it off.

**Common in robotics** — the robot continuously senses and acts.

---

## Slide 6: Complete Bounce Program
```python
threshold = 0.5

board.wait_for_button()

while True:
    left = reflectance.get_left()

    if left > threshold:
        drivetrain.stop()
        print("Bounce!")
        drivetrain.turn(180)
    else:
        drivetrain.set_effort(0.3, 0.3)
```

**Flow:** Drive → check sensor → on line? turn : keep driving → repeat

---

## Slide 7: Logical Operators — or
**`or` — at least one must be True:**
```python
if left > 0.5 or right > 0.5:
    print("At least one sensor on the line!")
```

**`and` — both must be True:**
```python
if left > 0.5 and right > 0.5:
    print("BOTH sensors on the line!")
```

**`not` — reverses True/False:**
```python
if not (left > 0.5):
    print("Left is NOT on the line")
```

---

## Slide 8: Using Both Sensors
```python
while True:
    left = reflectance.get_left()
    right = reflectance.get_right()

    if left > threshold or right > threshold:
        drivetrain.stop()
        drivetrain.turn(180)
    else:
        drivetrain.set_effort(0.3, 0.3)
```

**Why both?** If the robot approaches the line at an angle, only one sensor may detect it first. Using `or` catches both cases.

---

## Slide 9: Your Turn!
**Exercise 1:** Build the bounce driving program
- Robot bounces back and forth inside the circle

**Exercise 2 (Challenge):** Use both sensors with `or`
- Add a bounce counter

**Observe:** What pattern does the robot follow? Does it always bounce on the same line?

---

## Slide 10: Connection to Next Lesson
**The problem:** The robot bounces back and forth on the SAME line. Boring!

**Next lesson (Lesson 4):** Add randomness!
- `import random`
- `random.randint()` — generate random numbers
- Random turn angles → robot explores the whole circle

**Preview:**
```python
angle = random.randint(90, 270)
drivetrain.turn(angle)
```
