"""
Lesson 10: Python Functions — Starter Code
Create reusable functions for robot shapes.

Team: ________________________
Date: ________________________

Tips:
- def function_name(parameter): defines a function
- Call it with: function_name(value)
- Parameters make functions flexible
"""

from XRPLib.differential_drive import DifferentialDrive

drivetrain = DifferentialDrive.get_default_differential_drive()


# ===== Exercise 1: Define a draw_square Function =====
# Instead of writing the square loop every time, put it in a function.

# TODO: Define a function called draw_square that takes a distance parameter
# def draw_square(distance):
#     for i in range(4):
#         drivetrain.straight(???)
#         drivetrain.turn(90)

# TODO: Call draw_square with distance 30
# draw_square(30)

# TODO: Call draw_square with distance 20 (smaller square)
# draw_square(20)


# ===== Exercise 2: Define a draw_triangle Function =====

# TODO: Define a function called draw_triangle that takes a distance parameter
# def draw_triangle(distance):
#     for i in range(???):
#         drivetrain.straight(distance)
#         drivetrain.turn(???)

# TODO: Call it with different distances
# draw_triangle(30)
# draw_triangle(15)


# ===== Exercise 3: The Polygon Function =====
# One function that draws ANY regular polygon!

# TODO: Define draw_polygon(sides, distance)
# Hint: Turn angle = 360 / sides
# def draw_polygon(sides, distance):
#     angle = 360 / sides
#     for i in range(???):
#         drivetrain.straight(???)
#         drivetrain.turn(???)

# TODO: Use draw_polygon to draw different shapes
# draw_polygon(4, 30)   # Square
# draw_polygon(3, 30)   # Triangle
# draw_polygon(6, 20)   # Hexagon
# draw_polygon(8, 15)   # Octagon


# ===== Challenge: Shape Gallery =====
# Use your polygon function to draw a sequence of shapes.

# TODO: Draw a triangle, then a square, then a pentagon, then a hexagon
# Hint: Use a for loop with a list of side counts!
# shapes = [3, 4, 5, 6]
# for sides in shapes:
#     print("Drawing shape with", sides, "sides")
#     draw_polygon(sides, 20)
