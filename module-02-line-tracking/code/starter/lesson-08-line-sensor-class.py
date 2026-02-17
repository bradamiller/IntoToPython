# Lesson 8: LineSensor Class
# Create a class that wraps the reflectance sensor

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

    # TODO: Write get_error() method
    # Returns: left sensor value minus right sensor value
    # def get_error(self):
    #     ???

    # TODO: Write is_at_cross() method
    # Returns: True when BOTH sensors are above threshold
    # def is_at_cross(self):
    #     ???

    # TODO: Write is_off_line() method
    # Returns: True when BOTH sensors are below threshold
    # def is_off_line(self):
    #     ???


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
