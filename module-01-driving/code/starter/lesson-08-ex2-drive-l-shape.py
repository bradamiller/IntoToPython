"""
Lesson 8: Hello, Python — Starter Code
Exercise 2: Drive in an L-Shape (Challenge)

This is starter code for Exercise 2. Complete the program to make the robot:
1. Drive forward 30 cm
2. Turn right 90 degrees
3. Drive forward 30 cm again

Add print() statements between each command to show progress.
"""

from XRPLib.differential_drive import DifferentialDrive

# Get the robot's drivetrain
drivetrain = DifferentialDrive.get_default_differential_drive()

print("Starting...")

# Drive forward
drivetrain.straight(30)

# TODO: Add a print statement
# TODO: Turn right 90 degrees
# Hint: drivetrain.turn(90)

# Drive forward again
drivetrain.straight(30)

print("Done!")

# CHALLENGE: Can you modify this to make a triangle shape instead?
# Hints:
# - A triangle has 3 sides
# - Each exterior angle is 120 degrees (360 / 3 = 120)
# - You'll need 3 forward drives and 3 turns
