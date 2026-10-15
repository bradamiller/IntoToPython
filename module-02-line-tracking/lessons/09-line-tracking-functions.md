# Lesson 9: Line-Tracking Functions

## Overview
Students add a second toolkit of functions -- `track_to_intersection()`, `drive_past_intersection()`, `turn_clockwise()`, `turn_counterclockwise()` -- that combine the sensor functions from Lesson 8 with motor control to follow a line to an intersection, park on it, and turn onto the crossing line. The driving functions never read the hardware themselves: they call `get_error()`, `is_at_cross()` and `is_either_on_line()`, which is the lesson's main idea -- functions built on functions. These four names are used unchanged through the end of Module 5, so they are introduced here exactly as later modules will use them.

Two physical facts shape the toolkit. The sensors sit in front of the wheels, so when `track_to_intersection()` stops the wheels are still short of the cross; `drive_past_intersection()` drives the sensor-to-axle distance (8.75 cm on an XRP) so the wheels are over the intersection -- a turn then pivots on it -- and the sensors are past the tape, so the next track does not stop on the cross it is sitting on. And a 90-degree turn is never timed: `turn_clockwise()` makes a blind 60-degree turn to get both sensors off the old line, then spins until `is_either_on_line()` finds the crossing line. Nothing in this lesson stops because a clock ran out; that rule carries through the course.

This lesson stands on its own -- classes are never required. The **Optional Extension** at the end repackages both toolkits as cooperating `LineSensor` and `LineTrack` classes, where `LineTrack` holds a `LineSensor` (composition).

## Learning Objectives
By the end of this lesson, students will be able to:
- Write `track_to_intersection()` from the Lesson 5-7 control loop and `is_at_cross()`
- Explain why the robot drives a fixed distance after the sensors reach a cross, and write `drive_past_intersection()`
- Write `turn_clockwise()` and `turn_counterclockwise()` as sensor-ended turns, and explain the blind first part
- Say what ends each of the four functions, and why none of them uses a timer
- Drive a follow, drive past, turn, follow course with four function calls
- *(Extension)* Explain composition: a `LineTrack` that has a `LineSensor`

## Key Concepts
- **Functions built on functions**: `track_to_intersection()` calls `get_error()` and `is_at_cross()`; the turns call `is_either_on_line()`. Nothing in the driving toolkit reads `reflectance` directly.
- **Driving constants**: `BASE_EFFORT = 0.4`, `KP = 0.5`, `TURN_EFFORT = 0.25` as file-level globals, the same pattern as `THRESHOLD`. 0.4 is up from Lessons 5-7's 0.3 because the steering is now tuned; drop it back if the robot weaves.
- **Sensors lead the wheels**: `track_to_intersection()` ends with the sensors on the cross and the wheels 8.75 cm behind. `drive_past_intersection()` is `drivetrain.straight(8.75, 0.5)`: wheels onto the cross, sensors past it. It follows every track.
- **Sensor-ended turns**: `drivetrain.turn(-60, TURN_EFFORT)` blind, then `drivetrain.arcade(0, -TURN_EFFORT)` and `while not is_either_on_line(): pass`, then `stop()`. The blind part exists because both sensors are still on the old line; without it the loop ends before the turn starts. Counterclockwise is the mirror image.
- **Distances and sensors, never timers**: a distance is the same with a full or flat battery; a duration is not.
- **`pass`**: a do-nothing statement. The motors are already running; the loop's only job is to keep checking.

## Materials Required
- XRP robot; the taped circle with a perpendicular cross line
- `code/starter/lesson-09-line-tracking-functions.py` (sensor toolkit complete; driving functions as TODOs); `code/solutions/lesson-09-line-tracking-functions.py`
- `worksheets/09-line-tracking-functions.md`
- Extension: `code/solutions/lesson-09-linetrack-class-addon.py`

## Lesson Flow

### Introduction (10 minutes)
1. **Hook.** "Last lesson the robot could answer questions: am I at a cross? is either sensor on the line? Today it acts on the answers." Show the four-line program from the end of the lesson first:
   ```python
   track_to_intersection()
   drive_past_intersection()
   turn_clockwise()
   track_to_intersection()
   ```
   "By the end of the hour this drives the course. Every line is a function you write today."
2. **Two toolkits, one file.** The driving functions need the sensor functions, so the Lesson 8 toolkit sits at the top of the file unchanged, with the driving constants under it.

### Guided Practice (25 minutes)
1. **`track_to_intersection()`.** The Lesson 5-7 control loop with `is_at_cross()` as the exit:
   ```python
   def track_to_intersection():
       while not is_at_cross():
           error = get_error()
           correction = error * KP
           drivetrain.arcade(BASE_EFFORT, -correction)
       drivetrain.stop()
   ```
   Read it as a sentence: until you're at a cross, steer toward the line; then stop. Test it alone on the circle before anything else.

2. **Where the wheels stop.** Hold the robot up; point at the sensors, then the wheels. "When this function stops, the sensors are on the cross. Where are the wheels?" Behind it. "Now turn." The robot pivots about its wheels, short of the intersection, and the sensors swing down off the new line. So:
   ```python
   def drive_past_intersection():
       drivetrain.straight(8.75, 0.5)
   ```
   Two jobs in one call: wheels onto the cross so a turn pivots there; sensors past the tape so the next track has a line to follow instead of stopping on this cross. Ask why it's a distance and not `time.sleep(0.5)`.

3. **Turning until a sensor says stop.** "How far is 90 degrees? You could time it -- and it would be right until the battery dropped." Instead:
   ```python
   def turn_clockwise():
       drivetrain.turn(-60, TURN_EFFORT)      # blind: get both sensors off this line
       drivetrain.arcade(0, -TURN_EFFORT)     # keep spinning...
       while not is_either_on_line():
           pass                               # ...until a sensor sees the cross street
       drivetrain.stop()

   def turn_counterclockwise():
       drivetrain.turn(60, TURN_EFFORT)
       drivetrain.arcade(0, TURN_EFFORT)
       while not is_either_on_line():
           pass
       drivetrain.stop()
   ```
   Ask: "What is `is_either_on_line()` the moment the turn starts?" (`True` -- the sensors are on the line it was following.) "So what would the while loop do without the blind turn?" (End at once.) The blind 60 degrees clears the old line; the sensor finishes the turn, the same way whether the battery is full or flat. Why 60 and not 90? Because the sensor is what finishes it; the blind part only has to be big enough to clear the old line. `pass`: nothing extra to do; the motors are already running.

4. **The program.** Put the four lines from the hook under both toolkits and run it on the circle-with-cross.

### Independent Practice (20 minutes)
1. **Build in order.** Students complete the starter: `track_to_intersection()` alone; then add `drive_past_intersection()` and check the wheels end on the cross; then one turn, watching the blind part clear the line before the sensor takes over; then the full four-line program.
2. **`turn_around()`.** Write it as two `turn_clockwise()` calls. Does the second call need its blind part? (Yes -- after the first turn a sensor is on the new line.) Test: follow to the cross, drive past, turn around, follow back.
3. **Tune.** `TURN_EFFORT` (0.25 to start) and the blind angle: too small and a sensor is still on the old line when the loop begins; too large and the robot passes the new line blind. Record what worked.
4. **Advanced:** a timeout for a turn that never finds a line, counting loop passes rather than seconds.

### Assessment
- **Formative:** trace `track_to_intersection()`; explain the blind turn and `pass`; say what ends each function.
- **Exit ticket:** "Write `track_and_turn_clockwise()` that follows to a cross, parks on it, and turns." "Why does `turn_clockwise()` start with a blind turn?"
- **Worksheet:** `worksheets/09-line-tracking-functions.md`.

## Common Misconceptions
| Misconception | Reality |
|---|---|
| "The turn should be timed to 90 degrees" | It ends when a sensor finds the next line. Timing drifts with battery and floor; sensors don't. |
| "Skip `drive_past_intersection()` when going straight on" | Then the next track starts with the sensors on the cross and returns instantly. Every arrival is the pair. |
| "The blind turn is 90 degrees" | 60. It only has to clear the old line; the sensor does the rest. 90 would risk spinning past the new line blind. |
| "`pass` does something" | It does nothing; Python needs a statement in the loop body. The loop keeps re-checking its condition on its own. |
| "I need to re-read the sensors inside `track_to_intersection()`" | Call `get_error()` and `is_at_cross()`. One place knows how the hardware is read. |
| "`is_either_on_line()` is the opposite of `is_at_cross()`" | `is_at_cross()` is both sensors on tape; `is_either_on_line()` is at least one. Off the line entirely, both are `False`. |

## Differentiation
- **Support:** give the sensor toolkit complete; students write only the driving functions, starting with `track_to_intersection()`. Have them narrate the arrival pair with the robot in hand.
- **Extension:** a `track_for_distance()` using the encoders rather than a timer; a `set_speed()` that changes `BASE_EFFORT` (needs `global`); the class extension below.

## Materials & Code Examples
`code/solutions/lesson-09-line-tracking-functions.py` is both toolkits and the four-line test program. The relationship:
```
Sensor toolkit (Lesson 8)              Driving toolkit (Lesson 9)
reflectance, THRESHOLD                 drivetrain, BASE_EFFORT, KP, TURN_EFFORT
get_left(), get_right()
get_error()                    <----   track_to_intersection()
is_at_cross()                  <----   track_to_intersection()
is_either_on_line()            <----   turn_clockwise(), turn_counterclockwise()
                                       drive_past_intersection()
```

## Teaching Notes
- Say the rule out loud: *timing is never good for programs like this; sensors always work.* Then point at each function and ask what ends it: a cross, a distance, a line, a line.
- 8.75 cm is sensor-to-axle on an XRP. A robot with a different mounting needs a different number; measure it.
- The cross line must be clearly perpendicular to the circle, or `is_at_cross()` fires unreliably and the turn finds the new line at an angle.
- These four names are the Module 3, 4 and 5 vocabulary. Insist on them now.

## Connections to Next Lessons
- **Lesson 10** reverses at the cross with two sensor-ended turns, four times.
- **Module 3** drives a grid with the same four functions, unchanged.
- **Module 4** builds `drive_path()` on them; **Module 5** adds one rangefinder read between `turn_to()` and `track_to_intersection()`.

---

## Optional Extension: The `LineTrack` Class (Composition)

*Do this after the functions version works on the robot. For students who did the Lesson 8 extension.*

### The idea
`LineTrack` is a class that **contains** a `LineSensor` object as one of its attributes -- a "has-a" relationship, called composition. A car has an engine; `LineTrack` has a `LineSensor` for sensing and a drivetrain for driving, and coordinates them.

```
LineTrack
  |-- self.sensor = LineSensor()           <-- has-a LineSensor
  |-- self.drivetrain = DifferentialDrive  <-- has-a drivetrain
  |-- self.base_effort, self.kp, self.turn_effort
  |
  |-- drive_past_intersection()
  |-- track_to_intersection()    uses self.sensor and self.drivetrain
  |-- turn_clockwise()           uses self.sensor and self.drivetrain
  |-- turn_counterclockwise()
```

### The class
```python
class LineTrack:
    def __init__(self):
        self.sensor = LineSensor()
        self.drivetrain = DifferentialDrive.get_default_differential_drive()
        self.base_effort = 0.4
        self.kp = 0.5
        self.turn_effort = 0.25

    def drive_past_intersection(self):
        self.drivetrain.straight(8.75, 0.5)

    def track_to_intersection(self):
        while not self.sensor.is_at_cross():
            error = self.sensor.get_error()
            correction = error * self.kp
            self.drivetrain.arcade(self.base_effort, -correction)
        self.drivetrain.stop()

    def turn_clockwise(self):
        self.drivetrain.turn(-60, self.turn_effort)
        self.drivetrain.arcade(0, -self.turn_effort)
        while not self.sensor.is_either_on_line():
            pass
        self.drivetrain.stop()

    def turn_counterclockwise(self):
        self.drivetrain.turn(60, self.turn_effort)
        self.drivetrain.arcade(0, self.turn_effort)
        while not self.sensor.is_either_on_line():
            pass
        self.drivetrain.stop()
```

| Functions (required) | Class (extension) |
|---|---|
| `track_to_intersection()` | `tracker = LineTrack()` then `tracker.track_to_intersection()` |
| `is_at_cross()` inside the loop | `self.sensor.is_at_cross()` |
| `BASE_EFFORT`, `KP` globals | `self.base_effort`, `self.kp` attributes |

`self.sensor = LineSensor()` is the composition step: creating a `LineTrack` builds its own `LineSensor`. The four functions are the same four, with the same names; the settings moved from file-level capitals into `self.` attributes, and the sensor calls go through `self.sensor`.

### Discussion prompt
"Why doesn't `LineTrack` just copy the five sensor methods into itself?" (One job per class. If the sensor logic changes, it changes in `LineSensor` and `LineTrack` never knows.)

### Code
`code/solutions/lesson-09-linetrack-class-addon.py`.
