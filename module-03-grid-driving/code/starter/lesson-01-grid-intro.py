# Lesson 1: Introduction to the Grid
# Drive to the first intersection on the grid and stop
#
# Team: ________________________
# Date: ________________________

from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board
import time


# ===== LINESENSOR CLASS =====
# (Copy your working LineSensor class from Module 2 here)
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


# ===== LINETRACK CLASS =====
# (Copy your working LineTrack class from Module 2 here)
class LineTrack:
    def __init__(self):
        self.sensor = LineSensor()
        self.drivetrain = DifferentialDrive.get_default_differential_drive()
        self.base_effort = 0.4
        self.Kp = 0.5

    # TODO: Copy your track_until_cross() method here

    # TODO: Copy your turn_right() method here

    # TODO: Copy your turn_left() method here


# ===== MAIN PROGRAM =====
board = Board.get_default_board()
tracker = LineTrack()

board.wait_for_button()

# TODO: Drive to the first intersection
# Use tracker.track_until_cross()
print("Driving to first intersection...")

# TODO: Print a message when you arrive

# TODO (bonus): Add a turn_right() and then drive to another intersection
