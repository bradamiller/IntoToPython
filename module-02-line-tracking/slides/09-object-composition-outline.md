# Lesson 9 Slide Outline: Object Composition — LineTrack

## Slide 1: Title & Learning Objectives
**Title:** Object Composition — LineTrack

**Learning Objectives:**
- Understand object composition (one class using another)
- Build a LineTrack class that uses LineSensor
- Create methods for line following and turning
- Test classes with a simple main program

**Agenda:**
- Object composition concept (10 min)
- Building LineTrack (20 min)
- Testing and practice (15 min)

---

## Slide 2: From Messy Code to Clean Code
**Lesson 7 (50+ lines, everything mixed together):**
```python
while True:
    left = reflectance.get_left()
    right = reflectance.get_right()
    if left > 0.5 and right > 0.5:
        drivetrain.stop()
        drivetrain.turn(180)
        time.sleep(0.3)
    else:
        error = left - right
        # ... more code ...
```

**What we want (3 lines!):**
```python
tracker = LineTrack()
tracker.track_until_cross()
tracker.turn_right()
```

**Classes hide complexity behind simple names.**

---

## Slide 3: What Is Object Composition?
**Composition:** One class contains and uses another class's object.

**Real-world analogy:**
- A **car** HAS AN **engine** and HAS **wheels**
- The car doesn't build the engine — it uses one
- The car delegates "go fast" to the engine

**In our code:**
- **LineTrack** HAS A **LineSensor** and HAS A **DifferentialDrive**
- LineTrack delegates "check sensor" to LineSensor

---

## Slide 4: LineTrack.__init__()
```python
class LineTrack:
    def __init__(self):
        self.sensor = LineSensor()       # Create a LineSensor
        self.drivetrain = DifferentialDrive.get_default_differential_drive()
        self.base_effort = 0.4
        self.Kp = 0.5
```

**`self.sensor = LineSensor()`** — creates a LineSensor object and stores it.

**Now LineTrack can use `self.sensor.get_error()`, `self.sensor.is_at_cross()`, etc.**

---

## Slide 5: track_until_cross()
```python
def track_until_cross(self):
    while not self.sensor.is_at_cross():
        error = self.sensor.get_error()
        left = self.base_effort - error * self.Kp
        right = self.base_effort + error * self.Kp
        self.drivetrain.set_effort(left, right)
    self.drivetrain.stop()
```

**`while not self.sensor.is_at_cross()`:**
- Keep following while NOT at a cross
- When cross detected → loop exits → stop

**Uses LineSensor methods for ALL sensor work.**

---

## Slide 6: turn_right() and turn_left()
```python
def turn_right(self):
    # Drive forward to clear intersection
    self.drivetrain.set_effort(self.base_effort, self.base_effort)
    time.sleep(0.3)
    # Turn right
    self.drivetrain.set_effort(0.3, -0.3)
    time.sleep(0.3)
    # Keep turning until line is found
    while self.sensor.is_off_line():
        pass
    self.drivetrain.stop()
```

**Three phases:** Clear intersection → start turning → find line again

**`turn_left()` is the same but with opposite motor directions.**

---

## Slide 7: Using LineTrack in a Main Program
```python
board = Board.get_default_board()
tracker = LineTrack()

board.wait_for_button()

tracker.track_until_cross()
print("Cross found!")
tracker.turn_right()
print("Turned right!")
tracker.track_until_cross()
print("Done!")
```

**The main program is clean and readable.**
**All the complex sensor/motor code is hidden inside the classes.**

---

## Slide 8: The Building Block Pattern
```
LineSensor          DifferentialDrive
    ↓                      ↓
    └──────┬───────────────┘
           ↓
       LineTrack
           ↓
      Main Program
```

**Each layer builds on the layer below.**
**This is how professional software is built!**

---

## Slide 9: Your Turn!
**Exercise 1:** Build LineTrack and test each method
- `track_until_cross()` — does it follow and stop?
- `turn_right()` — does it turn and find the line?

**Exercise 2 (Challenge):** Chain multiple maneuvers
```python
for i in range(4):
    tracker.track_until_cross()
    tracker.turn_right()
```

---

## Slide 10: Connection to Final Project
**You now have two reusable classes:**
- `LineSensor` — reads and interprets sensors
- `LineTrack` — follows lines and handles intersections

**Next (Lesson 10 — Final Project):**
- Follow circle → detect cross → reverse → repeat 4 times
- Uses BOTH classes together
- The capstone of Module 2!
