"""
Lesson 9: Python Loops — Starter Code
Convert Blockly Repeat blocks to Python for loops.

Team: ________________________
Date: ________________________

Tips:
- for i in range(N): repeats N times
- Everything indented under the for is inside the loop
- range(4) gives 0, 1, 2, 3
"""

from XRPLib.differential_drive import DifferentialDrive

drivetrain = DifferentialDrive.get_default_differential_drive()


# ===== Exercise 1: Draw a Square =====
# A square has 4 sides. Each side: drive forward, then turn right 90 degrees.
# Use a for loop instead of writing the same code 4 times!

# TODO: Write a for loop that repeats 4 times
# for i in range(???):
#     drivetrain.straight(30)
#     drivetrain.turn(90)


# ===== Exercise 2: Draw a Triangle =====
# A triangle has 3 sides. What angle do you turn? (Hint: 360 / 3 = 120)

# TODO: Write a for loop that draws a triangle
# for i in range(???):
#     drivetrain.straight(???)
#     drivetrain.turn(???)


# ===== Exercise 3: Loop with Print =====
# Add a print statement inside the loop to track progress.

# TODO: Write a loop that prints which side it's drawing
# for i in range(4):
#     print("Drawing side", i + 1)
#     drivetrain.straight(30)
#     drivetrain.turn(90)


# ===== Challenge: Hexagon =====
# A hexagon has 6 sides. Turn angle = 360 / 6 = 60 degrees.

# TODO: Draw a hexagon using a for loop
