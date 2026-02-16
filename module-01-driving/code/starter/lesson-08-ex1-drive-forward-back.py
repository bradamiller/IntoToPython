"""
Lesson 8: Hello, Python — Starter Code
Exercise 1: Drive Forward and Back

This is starter code for Exercise 1. Replace each TODO with actual Python code.
Goal: Make the robot drive forward 30 cm, then backward 30 cm.

Tips:
- print() displays a message
- drivetrain.straight(distance) drives the robot (positive = forward, negative = backward)
- Each line of code runs in order
"""

from XRPLib.differential_drive import DifferentialDrive

# Get the robot's drivetrain (the wheels and motors)
drivetrain = DifferentialDrive.get_default_differential_drive()

# TODO: Add a print statement that says "Driving forward..."
# Hint: print("Driving forward...")

# TODO: Drive forward 30 cm
# Hint: drivetrain.straight(30)

# TODO: Add a print statement that says "Driving backward..."

# Drive backward 30 cm
drivetrain.straight(-30)

# TODO: Uncomment the line below by removing the # symbol
# print("Done!")
