"""
Lesson 8: Hello, Python — Solution Code
Exercise 1: Drive Forward and Back

This program drives the robot forward 30 cm, then backward 30 cm.
It includes print() statements to show what's happening.
"""

from XRPLib.differential_drive import DifferentialDrive

# Get the robot's drivetrain (the wheels and motors)
drivetrain = DifferentialDrive.get_default_differential_drive()

# Drive forward
print("Driving forward...")
drivetrain.straight(30)

# Drive backward
print("Driving backward...")
drivetrain.straight(-30)

# Done
print("Done!")
