"""
Lesson 11: Module 1 Final Project — Solution Code
Option A: Polygon Artist

This program draws a series of polygons, demonstrating
loops, functions, and parameters.
"""

from XRPLib.differential_drive import DifferentialDrive
import time

drivetrain = DifferentialDrive.get_default_differential_drive()


# ===== Functions =====

def draw_polygon(sides, distance):
    """Draw a regular polygon with the given number of sides and side length."""
    angle = 360 / sides
    for i in range(sides):
        drivetrain.straight(distance)
        drivetrain.turn(angle)


def space_between():
    """Add some spacing between shapes."""
    drivetrain.straight(15)
    time.sleep(0.5)


# ===== Main Program =====

print("=" * 30)
print("  Module 1 Final Project")
print("  Polygon Artist")
print("=" * 30)
print()

# Draw a gallery of shapes from triangle to octagon
shapes = [3, 4, 5, 6, 8]
shape_names = ["Triangle", "Square", "Pentagon", "Hexagon", "Octagon"]

for i in range(len(shapes)):
    sides = shapes[i]
    name = shape_names[i]

    print("Drawing shape", i + 1, "of", len(shapes), ":", name)
    draw_polygon(sides, 20)

    # Add spacing between shapes (except after the last one)
    if i < len(shapes) - 1:
        space_between()

print()
print("=" * 30)
print("  All shapes complete!")
print("  Drew", len(shapes), "polygons")
print("=" * 30)
