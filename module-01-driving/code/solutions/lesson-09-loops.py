"""
Lesson 9: Python Loops — Solution Code
Convert Blockly Repeat blocks to Python for loops.
"""

from XRPLib.differential_drive import DifferentialDrive

drivetrain = DifferentialDrive.get_default_differential_drive()


# ===== Exercise 1: Draw a Square =====
print("=== Drawing a Square ===")
for i in range(4):
    drivetrain.straight(30)
    drivetrain.turn(90)
print("Square complete!")


# ===== Exercise 2: Draw a Triangle =====
print("\n=== Drawing a Triangle ===")
for i in range(3):
    drivetrain.straight(30)
    drivetrain.turn(120)
print("Triangle complete!")


# ===== Exercise 3: Loop with Print =====
print("\n=== Square with Progress ===")
for i in range(4):
    print("Drawing side", i + 1, "of 4")
    drivetrain.straight(30)
    drivetrain.turn(90)
print("Done!")


# ===== Challenge: Hexagon =====
print("\n=== Drawing a Hexagon ===")
for i in range(6):
    print("Side", i + 1, "of 6")
    drivetrain.straight(20)
    drivetrain.turn(60)
print("Hexagon complete!")
