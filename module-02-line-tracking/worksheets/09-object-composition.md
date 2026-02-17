# Lesson 9 Worksheet: Object Composition

**Name:** ________________________
**Date:** ________________________

---

## Part 1: Composition Concept

1. **In your own words, what does "object composition" mean?**

   ____________________________________________________________________

2. **Give a real-world example of composition (not from code):**

   "A _____________ HAS A _____________ and HAS A _____________"

3. **In our code, what does LineTrack "have"?**

   a. ________________________________

   b. ________________________________

---

## Part 2: Class Relationship Diagram

Fill in the blanks to complete the composition diagram:

```
┌──────────────────┐       ┌──────────────────────┐
│   LineSensor     │       │  DifferentialDrive    │
│                  │       │                       │
│ get_error()      │       │ set_effort(l, r)      │
│ is_at_cross()    │       │ stop()                │
│ is_off_line()    │       │                       │
└──────┬───────────┘       └──────────┬────────────┘
       │                              │
       │    ┌────────────────────┐    │
       └────│    _____________   │────┘
            │                    │
            │ track_until_cross()│
            │ turn_right()       │
            │ _____________()    │
            └────────────────────┘
```

**Fill in the class name and missing method.**

---

## Part 3: Code Tracing — track_until_cross()

```python
def track_until_cross(self):
    while not self.sensor.is_at_cross():
        error = self.sensor.get_error()
        left = self.base_effort - error * self.Kp
        right = self.base_effort + error * self.Kp
        self.drivetrain.set_effort(left, right)
    self.drivetrain.stop()
```

1. **What does `self.sensor` refer to?** ________________________________

2. **What does `self.sensor.is_at_cross()` call?** A method on the _____________ class.

3. **What does `while not` mean here?** ________________________________

4. **When does the loop exit?** ________________________________

5. **What happens after the loop exits?** ________________________________

---

## Part 4: Code Tracing — turn_right()

```python
def turn_right(self):
    self.drivetrain.set_effort(self.base_effort, self.base_effort)
    time.sleep(0.3)
    self.drivetrain.set_effort(0.3, -0.3)
    time.sleep(0.3)
    while self.sensor.is_off_line():
        pass
    self.drivetrain.stop()
```

Number the steps of what the robot does:

___ Robot stops when line is found
___ Robot drives forward briefly to clear the intersection
___ Robot keeps turning while off the line
___ Robot starts turning right (left forward, right backward)
___ `pass` — do nothing, just keep checking

**Why does the robot drive forward first?**

____________________________________________________________________

---

## Part 5: Main Program Design

You have a `LineTrack` object called `tracker`. Write the main program code for each task:

1. **Follow the line until a cross, then stop:**
   ```python
   ________________________________
   ```

2. **Follow to cross, turn right, follow to cross again:**
   ```python
   ________________________________
   ________________________________
   ________________________________
   ```

3. **Follow and reverse 4 times using a for loop:**
   ```python
   for i in range(____):
       ________________________________
       ________________________________
       ________________________________
   ```

---

## Part 6: Composition vs. No Composition

**With classes (composition):**
```python
tracker = LineTrack()
tracker.track_until_cross()
tracker.turn_right()
```

**Without classes (everything in main):**
```python
while not (reflectance.get_left() > 0.5 and reflectance.get_right() > 0.5):
    error = reflectance.get_left() - reflectance.get_right()
    left = 0.4 - error * 0.5
    right = 0.4 + error * 0.5
    drivetrain.set_effort(left, right)
drivetrain.stop()
drivetrain.set_effort(0.4, 0.4)
time.sleep(0.3)
drivetrain.set_effort(0.3, -0.3)
time.sleep(0.3)
while reflectance.get_left() < 0.5 and reflectance.get_right() < 0.5:
    pass
drivetrain.stop()
```

**Which version is easier to read?** __________

**Which version is easier to reuse?** __________

**Which version is easier to debug?** __________

---

## Reflection

**How does object composition make your code better?**

_________________________________________________________________

_________________________________________________________________

---

**Next Lesson:** The final project — use both classes together for the Module 2 capstone!
