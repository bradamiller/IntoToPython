# Lesson 10: Module 2 Final Project

## Overview
Students bring together everything from Module 2 — sensor reading, proportional control, class design, and object composition — into a capstone program. Using their `LineSensor` and `LineTrack` classes, students write a main program that follows the taped circle, detects the cross intersection, reverses direction, and repeats for 4 total reversals before stopping. This serves as both a comprehensive assessment and a portfolio piece.

## Learning Objectives
By the end of this lesson, students will be able to:
- Integrate multiple classes into a single working program
- Write a main program that orchestrates class-based behavior
- Test, debug, and refine a complete robot program
- Demonstrate mastery of while loops, if/else, classes, methods, and object composition
- Present and explain their code to peers
- Reflect on the design process and identify improvements

## Key Concepts
- **Integration**: Combining multiple classes and concepts into one program
- **Main program**: The top-level code that creates objects and calls methods
- **Testing strategy**: Test components individually, then test them together
- **Debugging methodology**: Print, observe, adjust, repeat
- **Code organization**: Imports → class definitions → main program

## Materials Required
- XRP Robot with reflectance sensors
- White surface with taped circle AND taped cross
- VS Code with XRPLib installed
- Working `LineSensor` and `LineTrack` classes from Lessons 8–9
- Project rubric (below)

## Lesson Flow

### Introduction & Project Overview (10 minutes)

1. **Module Reflection**:
   - Review the journey: sensor reading → while loops → if/else → proportional control → classes → composition
   - "You now have two reusable classes. Let's use them to build something impressive."

2. **Project Requirements**:
   - The robot must:
     1. Follow the taped circle using `LineTrack.track_until_cross()`
     2. Detect the cross intersection
     3. Turn around (reverse direction)
     4. Continue following the circle
     5. Repeat for 4 total reversals
     6. Stop and print a completion message
   - Code must use the `LineSensor` and `LineTrack` classes
   - Code must include print statements showing progress
   - Code must be organized and commented

3. **Project Options** (students choose one):

   **Option A: Standard (Recommended)**
   - Follow the circle, reverse at cross, repeat 4 times, stop
   - Uses existing classes without modification
   - Focus on clean main program and debugging

   **Option B: Enhanced**
   - Same behavior as Option A, plus:
   - Add a `turn_around()` method to LineTrack
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
   Create a LineTrack object
   Wait for button press

   Repeat 4 times:
       Follow line until cross
       Print which leg we're on
       Turn around

   Stop and print "Done!"
   ```

2. **Review the Classes**:
   - Open LineSensor and LineTrack code from Lessons 8–9
   - Verify both classes are working individually
   - List the methods available:
     - `LineSensor`: `get_error()`, `is_at_cross()`, `is_off_line()`
     - `LineTrack`: `track_until_cross()`, `turn_right()`, `turn_left()`

3. **Plan the Turn-Around**:
   - To reverse direction on the circle: two right turns, or two left turns, or one 180° turn
   - Students should experiment to find what works best for their robot

### Implementation (30 minutes)

1. **Complete Program Structure**:
   ```python
   from XRPLib.reflectance import Reflectance
   from XRPLib.differential_drive import DifferentialDrive
   from XRPLib.board import Board
   import time


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
           self.Kp = 0.5

       def track_until_cross(self):
           while not self.sensor.is_at_cross():
               error = self.sensor.get_error()
               left = self.base_effort - error * self.Kp
               right = self.base_effort + error * self.Kp
               self.drivetrain.set_effort(left, right)
           self.drivetrain.stop()

       def turn_right(self):
           self.drivetrain.set_effort(self.base_effort, self.base_effort)
           time.sleep(0.3)
           self.drivetrain.set_effort(0.3, -0.3)
           time.sleep(0.3)
           while self.sensor.is_off_line():
               pass
           self.drivetrain.stop()

       def turn_left(self):
           self.drivetrain.set_effort(self.base_effort, self.base_effort)
           time.sleep(0.3)
           self.drivetrain.set_effort(-0.3, 0.3)
           time.sleep(0.3)
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
       tracker.turn_right()  # Two right turns = 180° reversal

   tracker.drivetrain.stop()
   print("Complete! 4 reversals done.")
   ```

2. **Testing Strategy**:
   - Test 1: Does `track_until_cross()` work? (Follow to cross, stop)
   - Test 2: Does the turn-around work? (Turn and find line again)
   - Test 3: Does the full loop work for 1 reversal?
   - Test 4: Full program — 4 reversals

3. **Common Issues & Solutions**:
   - **Robot doesn't detect cross**: Threshold may need adjustment, or tape is too thin
   - **Robot loses line after turning**: Adjust `time.sleep()` values in turn methods
   - **Robot goes wrong direction after turn**: Try `turn_left()` instead of `turn_right()`
   - **Robot overshoots the cross**: Reduce `base_effort` for slower, more accurate driving

### Presentation & Reflection (15 minutes)

1. **Live Demo**:
   - Each student/team demonstrates their robot
   - 2–3 minutes: "What did you build? Show it working."
   - Peers observe and provide feedback

2. **Individual Reflection** (written):
   - What was the hardest part of this module?
   - How did using classes make the final project easier?
   - What would you improve if you had more time?
   - What programming concepts do you feel confident about now?

### Assessment

**Project Rubric** (50 points total)

**Code Organization** (10 points)
- LineSensor class is correct and complete (3 pts)
- LineTrack class is correct and complete (4 pts)
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
| "I need to rewrite everything from scratch" | No — use your tested classes from Lessons 8–9! |
| "Two right turns won't reverse direction" | On a line, two right turns (each ~90°) effectively reverse direction |
| "The main program should be complex" | The beauty of classes is that the main program is simple and readable |
| "If it doesn't work the first time, it's broken" | Tuning parameters (effort, Kp, sleep times) is normal engineering |

## Differentiation

**For struggling students**:
- Provide complete LineSensor and LineTrack classes; focus only on the main program
- Reduce to 2 reversals instead of 4
- Pair with a stronger student for debugging

**For advanced students**:
- Add timing: print how long each leg takes
- Add speed control: slow on first leg, faster on subsequent legs
- Create a `turn_around()` method instead of calling `turn_right()` twice
- Add error recovery: if the robot loses the line, search for it

## Teaching Notes
- **This is the culmination**: Celebrate the achievement. Students went from zero programming to class-based robot control.
- **Debugging is learning**: The final project will require tuning. This IS the learning — not a sign of failure.
- **Keep the bar reasonable**: 4 reversals is the goal, but 2 successful reversals still shows mastery.
- **Module 3 preview**: Mention that these classes will be used on the grid in Module 3.

## Connections to Future Modules
- **Module 3** uses `LineTrack` directly on the grid — `track_until_cross()` drives between intersections
- **Module 4** builds `Navigator` and `Manhattan` classes on top of `LineTrack`
- **Module 5** replaces `Manhattan` with `Dijkstra` — same interface, different algorithm
- The class design pattern established here carries through the entire course
