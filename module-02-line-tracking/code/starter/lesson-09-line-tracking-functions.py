# Lesson 9: Line-Tracking Functions
# A second toolkit of functions that uses the sensor functions from Lesson 8
# for line following and turning.

from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board

reflectance = Reflectance.get_default_reflectance()
THRESHOLD = 0.5


def get_left():
    return reflectance.get_left()


def get_right():
    return reflectance.get_right()


def get_error():
    return get_left() - get_right()


def is_at_cross():
    return get_left() > THRESHOLD and get_right() > THRESHOLD


def is_off_line():
    return get_left() < THRESHOLD and get_right() < THRESHOLD


drivetrain = DifferentialDrive.get_default_differential_drive()
BASE_EFFORT = 0.4
KP = 0.5


def clear_intersection():
    # Drive 8 cm forward so the turning center is over the intersection
    drivetrain.straight(8, 0.5)


# TODO: Write track_until_cross()
# Follow the line until an intersection is detected
# Use a while loop with is_at_cross()
# Inside the loop: calculate error, set motor efforts with drivetrain.set_effort()
# After the loop: stop the robot
# def track_until_cross():
#     ???

# TODO: Write turn_right()
# 1. Call clear_intersection() to drive past the cross
# 2. Start turning right: drivetrain.set_effort(0.3, -0.3)
# 3. Keep turning while is_off_line()
# 4. Stop when the line is found
# def turn_right():
#     ???

# TODO: Write turn_left() (same as turn_right but opposite direction)
# def turn_left():
#     ???


# --- Test Program ---
board = Board.get_default_board()

board.wait_for_button()

print("Following line to cross...")
track_until_cross()
print("Cross found! Turning right...")
turn_right()
print("Following line again...")
track_until_cross()
print("Done!")
