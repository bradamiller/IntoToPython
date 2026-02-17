# Module 2 Final Project: Circle Follower with Cross Reversal - SOLUTION
# Follow the taped circle, reverse at the cross, repeat 4 times

from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board
import time


# ===== LINESENSOR CLASS =====
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
class LineTrack:
    def __init__(self):
        self.sensor = LineSensor()
        self.drivetrain = DifferentialDrive.get_default_differential_drive()
        self.base_effort = 0.4
        self.Kp = 0.5

    def track_until_cross(self):
        while not self.sensor.is_at_cross():
            error = self.sensor.get_error()
            left = self.base_effort - error * self.Kp
            right = self.base_effort + error * self.Kp
            self.drivetrain.set_effort(left, right)
        self.drivetrain.stop()

    def turn_right(self):
        self.drivetrain.set_effort(self.base_effort, self.base_effort)
        time.sleep(0.3)
        self.drivetrain.set_effort(0.3, -0.3)
        time.sleep(0.3)
        while self.sensor.is_off_line():
            pass
        self.drivetrain.stop()

    def turn_left(self):
        self.drivetrain.set_effort(self.base_effort, self.base_effort)
        time.sleep(0.3)
        self.drivetrain.set_effort(-0.3, 0.3)
        time.sleep(0.3)
        while self.sensor.is_off_line():
            pass
        self.drivetrain.stop()


# ===== MAIN PROGRAM =====
board = Board.get_default_board()
tracker = LineTrack()

board.wait_for_button()
print("Module 2 Final Project - Starting!")

for i in range(4):
    print("Leg", i + 1, "- Following line to cross...")
    tracker.track_until_cross()
    print("Cross detected! Reversing direction...")
    tracker.turn_right()
    tracker.turn_right()  # Two right turns = 180 degree reversal

tracker.drivetrain.stop()
print("Complete! 4 reversals done.")
