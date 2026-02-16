"""
Lesson 8: Hello, Python — Solution Code
Exercise 2: Drive in an L-Shape (Challenge)

This program makes the robot drive in an L-shape:
- Forward 30 cm
- Turn right 90 degrees
- Forward 30 cm
"""

from XRPLib.differential_drive import DifferentialDrive

# Get the robot's drivetrain
drivetrain = DifferentialDrive.get_default_differential_drive()

print("Starting...")

# Drive forward
print("Driving forward (first leg)...")
drivetrain.straight(30)

# Turn right
print("Turning right 90 degrees...")
drivetrain.turn(90)

# Drive forward again
print("Driving forward (second leg)...")
drivetrain.straight(30)

print("Done! The robot drove in an L-shape.")

# BONUS: Triangle variant
# Uncomment the code below to make the robot drive a triangle instead

"""
# Triangle shape (3 sides, 120 degree exterior angle)
def drive_triangle():
    for i in range(3):
        print(f"Driving side {i+1}...")
        drivetrain.straight(30)
        
        print(f"Turning at corner {i+1}...")
        drivetrain.turn(120)
    
    print("Triangle complete!")

# Uncomment below to run:
# drive_triangle()
"""
