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

def is_either_on_line():
    return get_left() > THRESHOLD or get_right() > THRESHOLD


# ===== DRIVING TOOLKIT (from Module 2 Lesson 9) =====
drivetrain = DifferentialDrive.get_default_differential_drive()
BASE_EFFORT = 0.4
KP = 0.5

def drive_past_intersection():
    # The sensors stop ON the cross, but the wheels are 8.75 cm behind them.
    # Drive that far so the axle is over the intersection: a turn then pivots
    # on it, and the next track_to_intersection() does not see this same cross.
    drivetrain.straight(8.75, 0.5)

# TODO: Copy your track_to_intersection() function here

# TODO: Copy your turn_clockwise() function here

# TODO: Copy your turn_counterclockwise() function here


# ===== MAIN PROGRAM =====
board = Board.get_default_board()

board.wait_for_button()

# TODO: Drive to the first intersection
# Use track_to_intersection(), then drive_past_intersection() so the wheels
# end up over the intersection (the sensors stop short of it)
print("Driving to first intersection...")

# TODO: Print a message when you arrive

# TODO (bonus): Add a turn_clockwise() and then drive to another intersection
