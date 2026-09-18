# Lesson 9 Optional Extension: LineTrack Class (Object Composition)
# Classes-track reference: the driving toolkit from lesson-09-line-tracking-functions.py,
# repackaged as a class that composes a LineSensor. Robot behavior is identical either way.

from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board


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


class LineTrack:
    def __init__(self):
        self.sensor = LineSensor()
        self.drivetrain = DifferentialDrive.get_default_differential_drive()
        self.base_effort = 0.4
        self.kp = 0.5

    def clear_intersection(self):
        self.drivetrain.straight(8, 0.5)

    def track_until_cross(self):
        while not self.sensor.is_at_cross():
            error = self.sensor.get_error()
            left = self.base_effort - error * self.kp
            right = self.base_effort + error * self.kp
            self.drivetrain.set_effort(left, right)
        self.drivetrain.stop()

    def turn_right(self):
        self.clear_intersection()
        self.drivetrain.set_effort(0.3, -0.3)
        while self.sensor.is_off_line():
            pass
        self.drivetrain.stop()

    def turn_left(self):
        self.clear_intersection()
        self.drivetrain.set_effort(-0.3, 0.3)
        while self.sensor.is_off_line():
            pass
        self.drivetrain.stop()


# --- Test Program ---
board = Board.get_default_board()
tracker = LineTrack()

board.wait_for_button()

print("Following line...")
tracker.track_until_cross()
print("Cross detected! Turning right...")
tracker.turn_right()
print("Following line again...")
tracker.track_until_cross()
print("Done!")
