"""
Lesson 10: Python Functions — Solution Code
Create reusable functions for robot shapes.
"""

from XRPLib.differential_drive import DifferentialDrive

drivetrain = DifferentialDrive.get_default_differential_drive()


# ===== Exercise 1: draw_square Function =====

def draw_square(distance):
    """Draw a square with the given side length."""
    for i in range(4):
        drivetrain.straight(distance)
        drivetrain.turn(90)


print("=== Exercise 1: Squares ===")
print("Drawing big square (30 cm sides)")
draw_square(30)

print("Drawing small square (20 cm sides)")
draw_square(20)


# ===== Exercise 2: draw_triangle Function =====

def draw_triangle(distance):
    """Draw an equilateral triangle with the given side length."""
    for i in range(3):
        drivetrain.straight(distance)
        drivetrain.turn(120)


print("\n=== Exercise 2: Triangles ===")
print("Drawing big triangle")
draw_triangle(30)

print("Drawing small triangle")
draw_triangle(15)


# ===== Exercise 3: The Polygon Function =====

def draw_polygon(sides, distance):
    """Draw a regular polygon with the given number of sides and side length."""
    angle = 360 / sides
    for i in range(sides):
        drivetrain.straight(distance)
        drivetrain.turn(angle)


print("\n=== Exercise 3: Polygons ===")
print("Square:")
draw_polygon(4, 30)

print("Triangle:")
draw_polygon(3, 30)

print("Hexagon:")
draw_polygon(6, 20)

print("Octagon:")
draw_polygon(8, 15)


# ===== Challenge: Shape Gallery =====

print("\n=== Challenge: Shape Gallery ===")
shapes = [3, 4, 5, 6]
for sides in shapes:
    print("Drawing shape with", sides, "sides")
    draw_polygon(sides, 20)

print("Gallery complete!")
