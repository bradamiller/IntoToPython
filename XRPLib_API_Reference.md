# XRPLib API Reference for Course

Quick reference for the key XRPLib classes and methods used throughout the course. For complete documentation, see [XRPLib MicroPython Docs](https://open-stem.github.io/XRP_MicroPython/).

---

## Getting Started

```python
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.reflectance import Reflectance
from XRPLib.rangefinder import Rangefinder
from XRPLib.board import Board
```

---

## DifferentialDrive (Drivetrain)

The main class for controlling the robot's movement.

### Basic Usage

```python
drivetrain = DifferentialDrive.get_default_differential_drive()
```

### Key Methods

#### Drive Straight
```python
drivetrain.straight(distance, max_effort=0.5, timeout=None)
```
- **distance** (float): Distance to drive in centimeters
- **max_effort** (float): Power level, -1 (reverse full) to 1 (forward full). Default: 0.5
- **timeout** (float): Max seconds to allow. If None, no timeout
- **Returns**: `True` if distance reached before timeout, `False` otherwise

**Example:**
```python
drivetrain.straight(30)  # Drive forward 30 cm at half power
drivetrain.straight(50, max_effort=0.75)  # Drive 50 cm at 75% power
drivetrain.straight(-20)  # Drive backward 20 cm
```

#### Turn
```python
drivetrain.turn(turn_degrees, max_effort=0.5, timeout=None, use_imu=True)
```
- **turn_degrees** (float): Angle to turn in degrees. Positive = clockwise, negative = counterclockwise
- **max_effort** (float): Power level, -1 to 1. Default: 0.5
- **timeout** (float): Max seconds to allow
- **use_imu** (bool): Use IMU for accurate turning (default True). Set to `False` for encoder-based turning
- **Returns**: `True` if angle reached before timeout

**Example:**
```python
drivetrain.turn(90)  # Turn clockwise 90°
drivetrain.turn(-45)  # Turn counterclockwise 45°
drivetrain.turn(360, max_effort=0.3)  # Spin full circle at lower speed
```

#### Stop
```python
drivetrain.stop()
```
Stops both motors immediately.

#### Set Effort (Raw Power)
```python
drivetrain.set_effort(left_effort, right_effort)
```
- **left_effort** (float): Power for left motor, -1 to 1
- **right_effort** (float): Power for right motor, -1 to 1

**Example:**
```python
drivetrain.set_effort(0.5, 0.5)  # Both motors at 50% forward
drivetrain.set_effort(0.5, 0.2)  # Left faster than right (will turn right)
drivetrain.set_effort(0.5, -0.5)  # Sharp right turn (pivot)
```

#### Set Speed (Closed-Loop Control)
```python
drivetrain.set_speed(left_speed, right_speed)
```
- **left_speed** (float): Target speed in cm/s
- **right_speed** (float): Target speed in cm/s

**Example:**
```python
drivetrain.set_speed(25, 25)  # Drive both wheels at 25 cm/s
drivetrain.set_speed(0, 0)  # Stop (same as stop())
```

#### Get Encoder Position
```python
drivetrain.get_left_encoder_position()  # Returns: float (distance in cm)
drivetrain.get_right_encoder_position()  # Returns: float (distance in cm)
```

#### Reset Encoders
```python
drivetrain.reset_encoder_position()
```
Resets both encoder positions to 0.

---

## Reflectance (Line Sensors)

Two sensor object for detecting lines (for modules 2+).

### Basic Usage

```python
reflectance = Reflectance.get_default_reflectance()
```

### Key Methods

#### Get Sensor Values
```python
left_value = reflectance.get_left()   # Returns: float 0.0 to 1.0
right_value = reflectance.get_right() # Returns: float 0.0 to 1.0
```

- **Returns**: `0.0` = white/light, `1.0` = black/dark
- Typical calibration:
  - On white surface: ~0.1 - 0.3
  - On black line: ~0.7 - 0.9
  - Use ~0.5 as default threshold

**Example:**
```python
left = reflectance.get_left()
if left > 0.5:
    print("Left sensor is on the dark line")
else:
    print("Left sensor is on white surface")
```

---

## Rangefinder (Ultrasonic Distance Sensor)

Measures distance to objects using ultrasonic sound.

### Basic Usage

```python
rangefinder = Rangefinder.get_default_rangefinder()
```

### Key Methods

#### Get Distance
```python
distance = rangefinder.distance()  # Returns: float (distance in cm)
```

- **Returns**: Distance in centimeters
- **Range**: 2 cm to 400 cm
- **Timeout**: Returns 65535 if no reading (object too far or too close)

**Example:**
```python
distance = rangefinder.distance()
if distance < 20:
    print(f"Object is {distance} cm away")
else:
    print("Object is far away")
```

---

## Board

Board-level functions (button, LED, power).

### Basic Usage

```python
board = Board.get_default_board()
```

### Key Methods

#### Button
```python
if board.is_button_pressed():
    print("Button is pressed")

board.wait_for_button()  # Halt program until button pressed
```

#### LED
```python
board.led_on()              # Turn on LED
board.led_off()             # Turn off LED
board.led_blink(5)          # Blink LED at 5 Hz
board.led_blink(0)          # Stop blinking
```

#### RGB Light (v2 boards only)
```python
board.set_rgb_led(255, 0, 0)    # Red
board.set_rgb_led(0, 255, 0)    # Green
board.set_rgb_led(0, 0, 255)    # Blue
board.set_rgb_led(255, 255, 0)  # Yellow
```

#### Power Check
```python
if board.are_motors_powered():
    print("Battery is connected and has power")
```

---

## Typical Module 1 Program Structure

```python
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board

# Get robot objects
drivetrain = DifferentialDrive.get_default_differential_drive()
board = Board.get_default_board()

# Wait for button press to start
board.wait_for_button()

# Drive sequence
drivetrain.straight(30)  # Drive forward 30 cm
drivetrain.turn(90)      # Turn 90° clockwise
drivetrain.straight(30)  # Drive forward 30 cm
drivetrain.turn(90)      # Turn 90° clockwise

print("Done!")
```

---

## Common Sequences

### Drive a Square
```python
drivetrain = DifferentialDrive.get_default_differential_drive()

for i in range(4):
    drivetrain.straight(30)  # Drive forward
    drivetrain.turn(90)      # Turn 90° right
```

### Draw a Polygon (Any Number of Sides)
```python
def draw_polygon(sides, distance_per_side):
    drivetrain = DifferentialDrive.get_default_differential_drive()
    angle = 360 / sides  # Angle to turn each side
    
    for i in range(sides):
        drivetrain.straight(distance_per_side)
        drivetrain.turn(angle)

# Use it
draw_polygon(3, 20)  # Triangle, 20 cm per side
draw_polygon(4, 15)  # Square, 15 cm per side
draw_polygon(6, 10)  # Hexagon, 10 cm per side
```

### Circle by Differential Speed
```python
drivetrain = DifferentialDrive.get_default_differential_drive()

# Slower right = turns right
drivetrain.set_effort(0.5, 0.3)  # Gentle right curve
# Let it run for a while by checking encoder position
while drivetrain.get_right_encoder_position() < 50:  # Travel ~50 cm
    pass  # Keep running
drivetrain.stop()
```

---

## Notes

- **Measurements**: Distance in centimeters, angles in degrees, speeds in cm/s
- **Effort/Power**: Ranges from -1 (full reverse) to 1 (full forward)
- **MicroPython vs Python**: XRPLib uses MicroPython, slightly different syntax than regular Python
- **Singletons**: Methods like `get_default_differential_drive()` return the same object every time
- **Timeouts**: If not specified, the robot will wait indefinitely. Always use timeouts in safety-critical code

---

## Resources

- [Full XRPLib Documentation](https://open-stem.github.io/XRP_MicroPython/)
- [XRPLib GitHub](https://github.com/Open-STEM/XRP_MicroPython)
- [XRP Support Forum](https://xrp.discourse.group/)
