# Lesson 8: Sensor Functions
# Organize the reflectance sensor code into a toolkit of functions.

from XRPLib.reflectance import Reflectance
from XRPLib.board import Board
import time

reflectance = Reflectance.get_default_reflectance()
THRESHOLD = 0.5


def get_left():
    return reflectance.get_left()


def get_right():
    return reflectance.get_right()


# TODO: Write get_error()
# Returns: left sensor value minus right sensor value
# Hint: call get_left() and get_right() -- don't read reflectance directly
# def get_error():
#     ???

# TODO: Write is_at_cross()
# Returns: True when BOTH sensors are above THRESHOLD
# def is_at_cross():
#     ???

# TODO: Write is_off_line()
# Returns: True when BOTH sensors are below THRESHOLD
# def is_off_line():
#     ???


# --- Test Program ---
board = Board.get_default_board()

board.wait_for_button()

for i in range(30):
    error = get_error()
    at_cross = is_at_cross()
    off_line = is_off_line()
    print("Error:", error, "Cross:", at_cross, "Off line:", off_line)
    time.sleep(0.3)
