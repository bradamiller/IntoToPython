"""
Lesson 11: Module 1 Final Project — Starter Code
Create a complete Python program that draws multiple shapes.

Team: ________________________
Date: ________________________

Project: Choose one option below and complete it.

Option A: Polygon Artist — Draw 3+ different polygons
Option B: Precision Navigation — Navigate a course with waypoints
Option C: Design Your Own — Create your own robot program

Requirements:
- Use at least one function with parameters
- Use at least one for loop
- Include print statements showing progress
- Code runs without errors
"""

from XRPLib.differential_drive import DifferentialDrive
import time

drivetrain = DifferentialDrive.get_default_differential_drive()


# ===== Your Functions Go Here =====

# TODO: Define your polygon function (from Lesson 10)
# def draw_polygon(sides, distance):
#     angle = 360 / sides
#     for i in range(sides):
#         drivetrain.straight(distance)
#         drivetrain.turn(angle)


# TODO: Define any additional helper functions you need
# For example:
# def drive_to_start():
#     """Move to starting position between shapes."""
#     drivetrain.straight(10)


# ===== Main Program =====

print("=" * 30)
print("  Module 1 Final Project")
print("=" * 30)

# TODO: Write your main program here
# Example for Option A (Polygon Artist):

# shapes = [3, 4, 5, 6]  # Triangle, square, pentagon, hexagon
# for sides in shapes:
#     print("Drawing shape with", sides, "sides")
#     draw_polygon(sides, 20)
#     time.sleep(1)  # Pause between shapes

print("\nProject complete!")
