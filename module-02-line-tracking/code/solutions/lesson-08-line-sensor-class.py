# Lesson 8: LineSensor Class - SOLUTION
# A class that wraps the reflectance sensor

from XRPLib.reflectance import Reflectance
from XRPLib.board import Board
import time


class LineSensor:
    def __init__(self):
        self.reflectance = Reflectance.get_default_reflectance()
        self.threshold = 0.5

    def get_left(self):
        return self.reflectance.get_left()

    def get_right(self):
        return self.reflectance.get_right()

    def get_error(self):
        return self.get_left() - self.get_right()

    def is_at_cross(self):
        return self.get_left() > self.threshold and self.get_right() > self.threshold

    def is_off_line(self):
        return self.get_left() < self.threshold and self.get_right() < self.threshold


# --- Test Program ---
board = Board.get_default_board()
sensor = LineSensor()

board.wait_for_button()

for i in range(30):
    error = sensor.get_error()
    at_cross = sensor.is_at_cross()
    off_line = sensor.is_off_line()
    print("Error:", error, "Cross:", at_cross, "Off line:", off_line)
    time.sleep(0.3)
