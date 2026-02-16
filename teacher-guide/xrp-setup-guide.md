# XRP Robot Setup Guide

## Overview

This guide provides step-by-step instructions for setting up the XRP robot hardware, software environment, and classroom infrastructure for the Python Programming Course.

## Prerequisites

- XRP Robot kit(s) — one per student or pair of students
- Computers with Python 3.8+ installed
- IDE: VS Code recommended (with Python extension)
- XRP software framework

## Hardware Setup

### XRP Robot Assembly

(Reference the official [XRP Assembly Guide](https://docs.wpilib.org/en/stable/docs/hardware/hardware-intro/index.html) for detailed instructions)

**Basic components:**
- 2× DC motors with encoders (wheels)
- 1× servo motor (optional, for gripper or arm)
- Ultrasonic rangefinder (Module 5)
- Reflectance sensors (2×, for line tracking)
- Gyroscope (optional, for heading)
- Battery + charging system
- Control board (microcontroller)

**Assembly checklist:**
- [ ] Motors mounted securely to chassis
- [ ] Wheels attached and rotate freely
- [ ] Sensors attached and connected to control board
- [ ] Battery secured and tested
- [ ] All electronics connections firm
- [ ] Robot drives forward in a straight line when commanded

### Grid Setup (For Modules 3–5)

**Materials:**
- White poster board or whiteboard plastic (8'×8' or larger)
- Black electrical tape or painter's tape
- Ruler or measuring tape
- Grid dimensions: 5×5 or 6×6 intersections (recommended)
- Tape line width: ~1.5 inches
- Intersection spacing: ~12–18 inches (adjust for your space)

**Setup:**
1. Divide board into a grid (e.g., 5×5 with 12" spacing)
2. Lay tape along grid lines forming a rectangular grid
3. Ensure lines are straight and perpendicular
4. Mark coordinate labels (row 0–4, col 0–4) at edges
5. Designate start position (e.g., (0,0) at lower-left)
6. Test with robot to ensure lines are detectable

**Diagram:**
```
     0     1     2     3     4
  ┌────┬────┬────┬────┬────┐
0 │    │    │    │    │    │
  ├────┼────┼────┼────┼────┤
1 │    │    │    │    │    │
  ├────┼────┼────┼────┼────┤
2 │ S  │    │    │    │    │  (S = start)
  ├────┼────┼────┼────┼────┤
3 │    │    │    │    │    │
  ├────┼────┼────┼────┼────┤
4 │    │    │    │    │    │
  └────┴────┴────┴────┴────┘
```

**Testing:**
- Drive robot to each grid corner to verify accuracy
- Mark any "dead zones" or problem areas
- Recalibrate if robot drifts significantly

---

## Software Setup

### 1. Install Python

**macOS / Linux:**
```bash
# Check if Python 3.8+ is installed
python3 --version

# If needed, install via Homebrew
brew install python@3.9
```

**Windows:**
- Download from [python.org](https://www.python.org/downloads/)
- Run installer; **check "Add Python to PATH"**

### 2. Install VS Code & Python Extension

1. Download [VS Code](https://code.visualstudio.com/)
2. Install extension: Python (Microsoft)
3. Install extension: Pylance (for better code completion)

### 3. Install XRP Framework

Follow the official [XRP setup documentation](https://www.xrpcode.org/). Typically:

```bash
# Create a virtual environment (recommended)
python3 -m venv xrp-env
source xrp-env/bin/activate  # On Windows: xrp-env\Scripts\activate

# Install XRP package
pip install xrp

# Verify installation
python3 -c "import xrp; print(xrp.__version__)"
```

### 4. Verify Robot Communication

1. Connect robot to computer via USB
2. Run a simple test script:

```python
from xrp.drivetrain import Drivetrain

# Create drivetrain object
drivetrain = Drivetrain()

# Test: drive forward 1 meter
drivetrain.straight(1.0)

print("Robot drove forward successfully!")
```

3. If robot doesn't move:
   - Check USB connection
   - Verify power (battery charged)
   - Check port in VS Code (should auto-detect)
   - Review XRP documentation for troubleshooting

---

## Classroom Setup

### Hardware Distribution

**Option 1: One robot per pair**
- Promotes collaboration
- Reduces equipment cost
- Students take turns driving/coding

**Option 2: One robot per student**
- More hands-on time per student
- Faster iteration
- Higher cost

**Recommendation:** Start with pairs; upgrade to individual if budget allows.

### Workspace Organization

**Station 1: Coding Area**
- Computers with Python IDE
- Starter code and documentation readily available
- Quiet space for focused coding

**Station 2: Robot Testing Area**
- Grid setup
- Charging station(s) for batteries
- Spare parts (wheels, sensors)
- Visual instructions for basic troubleshooting

**Station 3: Collaboration/Reflection**
- Whiteboard for tracing algorithms
- Worksheets and graph paper
- Space for code reviews and pair programming

### Pre-Class Checklist

**Before each lesson:**
- [ ] All robot batteries charged
- [ ] Robots tested: basic drive commands work
- [ ] Sensors calibrated (especially line sensors)
- [ ] Grid lines clean and well-lit
- [ ] Computers verified: Python and XRP framework working
- [ ] Starter code and solutions downloaded/accessible
- [ ] Presentation slides ready

**Weekly:**
- [ ] Visual inspection of all robots (loose connections, damaged motors)
- [ ] Sensor calibration as needed
- [ ] Battery health check (replace if degraded)
- [ ] Software updates (if available)

---

## Sensor Calibration

### Reflectance Sensors (Line Tracking, Modules 2–5)

**Purpose:** Detect black line on white surface.

**Calibration process:**

```python
from xrp.reflectance_sensor import ReflectanceSensor

# Create sensor objects for left and right
left_sensor = ReflectanceSensor(port=0)
right_sensor = ReflectanceSensor(port=1)

# Read sensor values in different positions
print("Place sensor ON the black line:")
input("Press Enter when ready...")
on_line_left = left_sensor.get_value()
on_line_right = right_sensor.get_value()
print(f"ON LINE: left={on_line_left}, right={on_line_right}")

print("\nPlace sensor OFF the line (on white):")
input("Press Enter when ready...")
off_line_left = left_sensor.get_value()
off_line_right = right_sensor.get_value()
print(f"OFF LINE: left={off_line_left}, right={off_line_right}")

# Calculate threshold (use average or weighted value)
threshold = (on_line_left + off_line_left) / 2
print(f"\nSuggested threshold: {threshold}")
```

**Typical values:**
- On line (black): ~500–700
- Off line (white): ~900–1000
- Use ~750 as threshold for most setups

**Recalibrate if:**
- Robot isn't detecting line properly
- Lighting changes significantly
- Sensors are dirty (gently wipe lens)

### Ultrasonic Rangefinder (Module 5)

**Purpose:** Detect obstacles at distance.

**Setup & testing:**

```python
from xrp.rangefinder import Rangefinder

rangefinder = Rangefinder()

# Test: measure distance to obstacle
for i in range(5):
    distance = rangefinder.get_distance()  # in meters or cm (check docs)
    print(f"Distance: {distance}")
```

**Typical values:**
- Max range: ~2 meters
- Resolution: ~1 cm
- At intersection, obstacle typically detectable at ~20–50 cm

**Calibration:**
- Place obstacle at known distances (10 cm, 20 cm, etc.)
- Record sensor values
- Note: Accuracy depends on surface reflectivity

---

## Troubleshooting Reference

| Problem | Likely Cause | Solution |
|---|---|---|
| Robot doesn't respond to commands | USB not connected or no power | Check port in IDE; recharge battery |
| Robot drives in circles | Wheel alignment off | Check W  heel mount; recalibrate motor speeds |
| Line sensor not detecting line | Dirty lens or wrong threshold | Clean sensor; run calibration script |
| Robot goes off the line | Proportional control gains too low/high | Adjust control constants (see Module 2) |
| Rangefinder gives crazy values | Reflective surface or wrong angle | Reorient sensor; test with different objects |
| Code works on simulator, fails on robot | Port or hardware configuration mismatch | Check XRP documentation; verify connections |

---

## Safety Considerations

1. **Electrical Safety**
   - Don't modify battery connections without supervision
   - Keep liquids away from electronics
   - Report damaged wires or loose connections immediately

2. **Robot Safety**
   - Keep fingers away from spinning wheels
   - Don't leave robots running unattended
   - Secure charging cables to prevent tripping

3. **Workspace Safety**
   - Keep grid area clear of obstacles (except as intended)
   - Mark grid area so students don't trip over tape
   - Ensure adequate lighting

---

## Professional Development

**Before teaching this course, familiarize yourself with:**
1. XRP hardware and software documentation
2. Python basics (at your students' level)
3. Basic robotics concepts (motors, sensors, feedback control)
4. Pathfinding algorithms (Manhattan, Dijkstra)

**Resources:**
- [XRP Official Documentation](https://www.xrpcode.org/)
- [Python.org Tutorials](https://docs.python.org/3/tutorial/)
- [Khan Academy: Algorithms](https://www.khanacademy.org/computing/computer-science/algorithms)
- This course outline and lesson plans

---

## Additional Resources

- **XRP Community:** [Discussion forum / GitHub](https://www.xrpcode.org/community)
- **Python Debugging:** VS Code debugger tutorial
- **Robotics Concepts:** VEX Robotics library, FRC documentation

---

## Support & Contact

For setup issues:
1. Check XRP official documentation
2. Review troubleshooting section above
3. Post in XRP community forum
4. Contact your equipment supplier or course maintainer

---

**Last Updated:** [Date]

**Next Review:** [Date +1 year]
