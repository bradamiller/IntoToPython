# Module 2: Line Tracking

## Overview

**Duration:** 4–5 weeks

**Theme:** Sensors, control loops, and building toolkits of functions (with classes as an optional extension)

**Final Project:** Robot follows a taped circle to its intersection point, detects the cross, reverses direction, and repeats for 4 total reversals before stopping

## Learning Objectives

By the end of this module, students will be able to:
- Read and interpret analog sensor values in Python
- Understand and implement `while` loops and `if`/`else` logic
- Organize sensor logic into a toolkit of functions that share global settings, and know when `global` is needed
- Build a driving toolkit on the sensor toolkit: line tracking to an intersection, parking on it, and sensor-ended turns
- *(Optional)* Repackage the toolkits as `LineSensor` and `LineTrack` classes, one holding the other
- Implement proportional control for smooth line following
- Detect intersections using sensor logic
- Debug a system in the real world (robot on its physical setup)

## Key Concepts

- **Sensors:** Reading raw values; understanding thresholds (on the line vs. off the line)
- **Comparison & Logical Operators:** `<`, `>`, `<=`, `>=`, `==`, `and`, `or`, `not`
- **Control Loops:** `while` loops that continue until a condition is met
- **Proportional Control:** Error-based steering (smoother than bang-bang control)
- **Toolkits of Functions:** Sensor functions (`get_error`, `is_at_cross`, `is_either_on_line`) and driving functions (`track_to_intersection`, `drive_past_intersection`, `turn_clockwise`, `turn_counterclockwise`) sharing file-level settings
- **Sensors, not timers:** Every driving function ends on a sensor reading or a distance, never a clock
- **Classes (optional extension):** `LineSensor` and `LineTrack`, one holding the other
- **Debugging Physical Systems:** Testing on the robot, not just in code

## Module Structure

### Phase A: Understanding Sensors (Lessons 1–4)
Students learn sensor basics and implement simple edge-following loops.
- Lesson 1: The Reflectance Sensor
- Lesson 2: Drive to the Edge and Stop
- Lesson 3: Bounce Driving
- Lesson 4: Random Turns

### Phase B: Line Following (Lessons 5–7)
Students implement proportional control and multi-sensor line following.
- Lesson 5: Proportional Control with One Sensor
- Lesson 6: Two-Sensor Line Following
- Lesson 7: Detecting Intersections

### Phase C: Building Toolkits (Lessons 8–10)
Students organize their code into reusable functions and integrate them into a complete program.
- Lesson 8: Sensor Functions (optional extension: the `LineSensor` class)
- Lesson 9: Line-Tracking Functions (optional extension: the `LineTrack` class)
- Lesson 10: Module 2 Final Project

## Python Concepts Introduced

| Concept | Lesson | Usage |
|---|---|---|
| `while` loops | 2 | Keep doing something until a condition is met |
| `if`/`elif`/`else` | 2 | Make decisions in code |
| Comparison operators | 2 | `<`, `>`, `<=`, `>=`, `==`, `!=` |
| Logical operators | 3 | `and`, `or`, `not` for combining conditions |
| `import` | 2 | Using the `random` module |
| `random` module | 4 | `random.randint()` for random numbers |
| Global variables and `global` | 8 | Functions sharing a sensor and a threshold |
| Functions calling functions | 8, 9 | `get_error()` on `get_left()`; the driving toolkit on the sensor toolkit |
| `pass` | 9 | An empty loop body that only re-checks its condition |
| Classes (optional extension) | 8, 9 | `LineSensor`, `LineTrack`, `self`, composition |
| Booleans (`True`/`False`) | 2 | Boolean values for conditions |

## Progression

1. **Weeks 5–6:** Sensor basics and edge-following — students get comfortable reading sensors and using loops
2. **Week 7:** Proportional control and intersection detection — smoother tracking, detection logic
3. **Weeks 8–9:** Toolkit design and integration — abstract sensor logic into functions, then build the driving functions on them

**This is the heaviest module — allow adequate time for debugging and testing.**

## Key Milestones

- ✓ **End of Week 5:** Sensor calibration complete; robot detects line edge and stops
- ✓ **Week 6 mid:** "Bounce driving" works — robot bounces off edges continuously
- ✓ **Week 6 end:** Proportional control working; smooth line following observed
- ✓ **Week 7 end:** Two-sensor line following smooth; intersection detection working
- ✓ **Week 8 end:** sensor toolkit written, tested by hand, and working independently
- ✓ **Week 9 end:** Full program complete — 4 reversals on circle crossing

## Assessment

Students demonstrate mastery by:
1. **Sensor calibration worksheet:** Understanding threshold values
2. **Exercise code submissions:** Each exercise builds on the last
3. **Code reviews:** Peer feedback on function names and organization
4. **Final project demo:** Robot correctly follows circle and reverses 4 times

## Debugging Notes

**Common issues in this module:**
- **Sensor doesn't detect line:** Lens dirty or threshold wrong; recalibrate
- **Robot oscillates (over-correcting):** Proportional gain too high; reduce coefficient
- **Robot doesn't turn enough:** Proportional gain too low; increase coefficient
- **Intersection detection fails:** Thresholds not set correctly for "both sensors on line"; fine-tune in Lesson 7
- **Function errors:** a `global` missing where a function assigns to a setting; a turn that ends instantly because the blind part was skipped

## Resources

- Module 1 code (functions and loops)
- Sensor calibration scripts (provided in Lesson 1)
- Worksheet templates for tracing logic
- Solution code at each stage (use progressively as needed)

## Next Module

Module 3 applies the driving toolkit to the grid—students use existing code, unchanged, to navigate intersections and drive patterns.

---

## Lesson-by-Lesson Details

For detailed plans on each lesson, see the `lessons/` folder. Each lesson includes objectives, concept explanations, worked examples, exercises, and solutions.

---

**Note:** This module is where students transition from simple sequences to more complex control logic. Be patient; debugging on real hardware takes time. Success here builds confidence for algorithmic thinking in Modules 4–5.
