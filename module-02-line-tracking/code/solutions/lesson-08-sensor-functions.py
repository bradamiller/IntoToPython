# Lesson 8: Sensor Functions - SOLUTION
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


def get_error():
    return get_left() - get_right()


def is_at_cross():
    return get_left() > THRESHOLD and get_right() > THRESHOLD


def is_off_line():
    return get_left() < THRESHOLD and get_right() < THRESHOLD


# --- Test Program ---
board = Board.get_default_board()

board.wait_for_button()

for i in range(30):
    error = get_error()
    at_cross = is_at_cross()
    off_line = is_off_line()
    print("Error:", error, "Cross:", at_cross, "Off line:", off_line)
    time.sleep(0.3)
