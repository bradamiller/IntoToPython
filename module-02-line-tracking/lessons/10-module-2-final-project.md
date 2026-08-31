# Lesson 10: Module 2 Final Project

## Overview
Students bring together everything from Module 2 — sensor reading, proportional control, and organizing code into toolkits — into a capstone program. Using their sensor and driving toolkits from Lessons 8-9, students write a main program that follows the taped circle, detects the cross intersection, reverses direction, and repeats for 4 total reversals before stopping. This serves as both a comprehensive assessment and a portfolio piece.

This lesson stands on its own -- classes are never required. An **optional extension** at the end of this file shows the same final project built on the `LineSensor`/`LineTrack` classes from the Lesson 8-9 extensions, for courses that also cover OOP.

## Learning Objectives
By the end of this lesson, students will be able to:
- Integrate multiple function toolkits into a single working program
- Write a main program that orchestrates toolkit behavior
- Test, debug, and refine a complete robot program
- Demonstrate mastery of while loops, if/else, functions, and global variables
- Present and explain their code to peers
- Reflect on the design process and identify improvements

## Key Concepts
- **Integration**: Combining multiple toolkits and concepts into one program
- **Main program**: The top-level code that calls functions in sequence
- **Testing strategy**: Test components individually, then test them together
- **Debugging methodology**: Print, observe, adjust, repeat
- **Code organization**: Imports → sensor toolkit → driving toolkit → main program

## Materials Required
- XRP Robot with reflectance sensors
- White surface with taped circle AND taped cross
- VS Code with XRPLib installed
- Working sensor and driving toolkits from Lessons 8-9
- Project rubric (below)

## Lesson Flow

### Introduction & Project Overview (10 minutes)

1. **Module Reflection**:
   - Review the journey: sensor reading → while loops → if/else → proportional control → functions → toolkits
   - "You now have two reusable toolkits. Let's use them to build something impressive."

2. **Project Requirements**:
   - The robot must:
     1. Follow the taped circle using `track_until_cross()`
     2. Detect the cross intersection
     3. Turn around (reverse direction)
     4. Continue following the circle
     5. Repeat for 4 total reversals
     6. Stop and print a completion message
   - Code must use the sensor and driving toolkit functions
   - Code must include print statements showing progress
   - Code must be organized and commented

3. **Project Options** (students choose one):

   **Option A: Standard (Recommended)**
   - Follow the circle, reverse at cross, repeat 4 times, stop
   - Uses existing toolkit functions without modification
   - Focus on clean main program and debugging

   **Option B: Enhanced**
   - Same behavior as Option A, plus:
   - Add a `turn_around()` function
   - Track and print timing for each leg
   - LED or beep feedback at each reversal

   **Option C: Advanced**
   - Same behavior as Option A, plus:
   - Handle "off line" recovery (what if the robot loses the line?)
   - Adjustable speed (slow for first lap, faster for subsequent laps)
   - Creative additions approved by instructor

### Planning Phase (15 minutes)

1. **Pseudocode the Main Program**:
   ```
   Wait for button press

   Repeat 4 times:
       Follow line until cross
       Print which leg we're on
       Turn around

   Stop and print "Done!"
   ```

2. **Review the Toolkits**:
   - Open the sensor and driving toolkit code from Lessons 8-9
   - Verify both toolkits are working individually
   - List the functions available:
     - Sensor toolkit: `get_error()`, `is_at_cross()`, `is_off_line()`
     - Driving toolkit: `track_until_cross()`, `turn_right()`, `turn_left()`, `clear_intersection()`

3. **Plan the Turn-Around**:
   - To reverse direction on the circle: two right turns, or two left turns, or one 180° turn
   - Students should experiment to find what works best for their robot

### Implementation (30 minutes)

1. **Complete Program Structure**:
   ```python
   from XRPLib.reflectance import Reflectance
   from XRPLib.differential_drive import DifferentialDrive
   from XRPLib.board import Board


   # ===== SENSOR TOOLKIT =====
   reflectance = Reflectance.get_default_reflectance()
   THRESHOLD = 0.5

   def get_left():
       return reflectance.get_left()

   def get_right():
       return reflectance.get_right()

   def get_error():
       return get_left() - get_right()

   def is_at_cross():
       return get_left() > THRESHOLD and get_right() > THRESHOLD

   def is_off_line():
       return get_left() < THRESHOLD and get_right() < THRESHOLD


   # ===== DRIVING TOOLKIT =====
   drivetrain = DifferentialDrive.get_default_differential_drive()
   BASE_EFFORT = 0.4
   KP = 0.5

   def clear_intersection():
       drivetrain.straight(8, 0.5)

   def track_until_cross():
       while not is_at_cross():
           error = get_error()
           left = BASE_EFFORT - error * KP
           right = BASE_EFFORT + error * KP
           drivetrain.set_effort(left, right)
       drivetrain.stop()

   def turn_right():
       clear_intersection()
       drivetrain.set_effort(0.3, -0.3)
       while is_off_line():
           pass
       drivetrain.stop()

   def turn_left():
       clear_intersection()
       drivetrain.set_effort(-0.3, 0.3)
       while is_off_line():
           pass
       drivetrain.stop()


   # ===== MAIN PROGRAM =====
   board = Board.get_default_board()

   board.wait_for_button()
   print("Module 2 Final Project - Starting!")

   for i in range(4):
       print("Leg", i + 1, "- Following line to cross...")
       track_until_cross()
       print("Cross detected! Reversing direction...")
       turn_right()
       turn_right()  # Two right turns = 180 degree reversal

   print("Complete! 4 reversals done.")
   ```

2. **Testing Strategy**:
   - Test 1: Does `track_until_cross()` work? (Follow to cross, stop)
   - Test 2: Does the turn-around work? (Turn and find line again)
   - Test 3: Does the full loop work for 1 reversal?
   - Test 4: Full program — 4 reversals

3. **Common Issues & Solutions**:
   - **Robot doesn't detect cross**: Threshold may need adjustment, or tape is too thin
   - **Robot loses line after turning**: Check `clear_intersection()`'s 8 cm distance against your robot
   - **Robot goes wrong direction after turn**: Try `turn_left()` instead of `turn_right()`
   - **Robot overshoots the cross**: Reduce `BASE_EFFORT` for slower, more accurate driving

### Presentation & Reflection (15 minutes)

1. **Live Demo**:
   - Each student/team demonstrates their robot
   - 2–3 minutes: "What did you build? Show it working."
   - Peers observe and provide feedback

2. **Individual Reflection** (written):
   - What was the hardest part of this module?
   - How did organizing your code into toolkits make the final project easier?
   - What would you improve if you had more time?
   - What programming concepts do you feel confident about now?

### Assessment

**Project Rubric** (50 points total)

**Code Organization** (10 points)
- Sensor toolkit is correct and complete (3 pts)
- Driving toolkit is correct and complete (4 pts)
- Main program is clean and well-commented (3 pts)

**Functionality** (20 points)
- Robot follows the line smoothly (5 pts)
- Robot detects the cross reliably (5 pts)
- Robot reverses direction correctly (5 pts)
- Robot completes 4 reversals and stops (5 pts)

**Testing & Debugging** (10 points)
- Evidence of incremental testing (3 pts)
- Print statements show progress (3 pts)
- Student can explain how they debugged issues (4 pts)

**Presentation & Reflection** (10 points)
- Live demo works (4 pts)
- Clear explanation of code (3 pts)
- Thoughtful reflection on learning (3 pts)

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "I need to rewrite everything from scratch" | No — use your tested toolkit functions from Lessons 8–9! |
| "Two right turns won't reverse direction" | On a line, two right turns (each ~90°) effectively reverse direction |
| "The main program should be complex" | The beauty of organized toolkits is that the main program is simple and readable |
| "If it doesn't work the first time, it's broken" | Tuning parameters (effort, KP) is normal engineering |

## Differentiation

**For struggling students**:
- Provide complete sensor and driving toolkits; focus only on the main program
- Reduce to 2 reversals instead of 4
- Pair with a stronger student for debugging

**For advanced students**:
- Add timing: print how long each leg takes
- Add speed control: slow on first leg, faster on subsequent legs
- Create a `turn_around()` function instead of calling `turn_right()` twice
- Add error recovery: if the robot loses the line, search for it
- Work through the Optional Extension below and compare the two versions directly

## Teaching Notes
- **This is the culmination**: Celebrate the achievement. Students went from zero programming to building working robot toolkits.
- **Debugging is learning**: The final project will require tuning. This IS the learning — not a sign of failure.
- **Keep the bar reasonable**: 4 reversals is the goal, but 2 successful reversals still shows mastery.
- **Module 3 preview**: Mention that these toolkits will be used on the grid in Module 3.
- **The Optional Extension is a separate, self-contained add-on.** If your course doesn't cover classes, skip it entirely — Module 3 only depends on the functions above, never on the class version.

## Connections to Future Modules
- **Module 3** uses the driving toolkit directly on the grid — `track_until_cross()` drives between intersections
- **Module 4** builds Manhattan pathfinding and navigation functions on top of this toolkit
- **Module 5** replaces the Manhattan pathfinding function with a Dijkstra one — same interface, different algorithm
- The toolkit design pattern established here carries through the entire course

---

## Optional Extension: The Final Project with Classes

*For courses that also cover classes/objects -- combines the Lesson 8 and Lesson 9 Optional Extensions. Skip this section entirely otherwise; nothing later in the course depends on it.*

```python
from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board


class LineSensor:
    def __init__(self):
        self.reflectance = Reflectance.get_default_reflectance()
        self.threshold = 0.5

    def get_left(self):
        return self.reflectance.get_left()

    def get_right(self):
        return self.reflectance.get_right()

    def get_error(self):
        return self.get_left() - self.get_right()

    def is_at_cross(self):
        return self.get_left() > self.threshold and self.get_right() > self.threshold

    def is_off_line(self):
        return self.get_left() < self.threshold and self.get_right() < self.threshold


class LineTrack:
    def __init__(self):
        self.sensor = LineSensor()
        self.drivetrain = DifferentialDrive.get_default_differential_drive()
        self.base_effort = 0.4
        self.kp = 0.5

    def clear_intersection(self):
        self.drivetrain.straight(8, 0.5)

    def track_until_cross(self):
        while not self.sensor.is_at_cross():
            error = self.sensor.get_error()
            left = self.base_effort - error * self.kp
            right = self.base_effort + error * self.kp
            self.drivetrain.set_effort(left, right)
        self.drivetrain.stop()

    def turn_right(self):
        self.clear_intersection()
        self.drivetrain.set_effort(0.3, -0.3)
        while self.sensor.is_off_line():
            pass
        self.drivetrain.stop()

    def turn_left(self):
        self.clear_intersection()
        self.drivetrain.set_effort(-0.3, 0.3)
        while self.sensor.is_off_line():
            pass
        self.drivetrain.stop()


# ===== MAIN PROGRAM =====
board = Board.get_default_board()
tracker = LineTrack()

board.wait_for_button()
print("Module 2 Final Project - Starting!")

for i in range(4):
    print("Leg", i + 1, "- Following line to cross...")
    tracker.track_until_cross()
    print("Cross detected! Reversing direction...")
    tracker.turn_right()
    tracker.turn_right()  # Two right turns = 180 degree reversal

print("Complete! 4 reversals done.")
```

Every method call in this version has a direct, one-to-one counterpart in the functions version above (`tracker.track_until_cross()` ↔ `track_until_cross()`, and so on) -- the robot's behavior is identical either way.
