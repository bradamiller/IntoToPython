# Lesson 1: Introduction to the Grid
# Drive to the first intersection on the grid and stop
#
# Team: ________________________
# Date: ________________________

from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board

# ===== SENSOR TOOLKIT (from Module 2 Lesson 8) =====
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


# ===== DRIVING TOOLKIT (from Module 2 Lesson 9) =====
drivetrain = DifferentialDrive.get_default_differential_drive()
BASE_EFFORT = 0.4
KP = 0.5

def clear_intersection():
    drivetrain.straight(8, 0.5)

# TODO: Copy your track_until_cross() function here

# TODO: Copy your turn_right() function here

# TODO: Copy your turn_left() function here


# ===== MAIN PROGRAM =====
board = Board.get_default_board()

board.wait_for_button()

# TODO: Drive to the first intersection
# Use track_until_cross()
print("Driving to first intersection...")

# TODO: Print a message when you arrive

# TODO (bonus): Add a turn_right() and then drive to another intersection
