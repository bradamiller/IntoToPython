# Module 2 Final Project Optional Extension: Circle Follower with Cross Reversal
# Classes-track reference: combines the LineSensor and LineTrack classes from
# lesson-08-linesensor-class-addon.py and lesson-09-linetrack-class-addon.py.
# Robot behavior is identical to lesson-10-final-project.py.

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

    def is_either_on_line(self):
        return self.get_left() > self.threshold or self.get_right() > self.threshold


class LineTrack:
    def __init__(self):
        self.sensor = LineSensor()
        self.drivetrain = DifferentialDrive.get_default_differential_drive()
        self.base_effort = 0.4
        self.kp = 0.5
        self.turn_effort = 0.25

    def drive_past_intersection(self):
        # The sensors stop ON the cross, but the wheels are 8.75 cm behind
        # them. Drive that far so the axle is over the intersection.
        self.drivetrain.straight(8.75, 0.5)

    def track_to_intersection(self):
        while not self.sensor.is_at_cross():
            error = self.sensor.get_error()
            left = self.base_effort - error * self.kp
            right = self.base_effort + error * self.kp
            self.drivetrain.set_effort(left, right)
        self.drivetrain.stop()

    def turn_clockwise(self):
        # A blind turn first, far enough to get both sensors off the line we
        # were on. Then keep turning until a sensor finds the cross street.
        # No timing involved: the sensors say when the turn is done.
        self.drivetrain.turn(-60, self.turn_effort)
        self.drivetrain.arcade(0, -self.turn_effort)
        while not self.sensor.is_either_on_line():
            pass
        self.drivetrain.stop()

    def turn_counterclockwise(self):
        self.drivetrain.turn(60, self.turn_effort)
        self.drivetrain.arcade(0, self.turn_effort)
        while not self.sensor.is_either_on_line():
            pass
        self.drivetrain.stop()


# ===== MAIN PROGRAM =====
board = Board.get_default_board()
tracker = LineTrack()

board.wait_for_button()
print("Module 2 Final Project - Starting!")

for i in range(4):
    print("Leg", i + 1, "- Following line to cross...")
    tracker.track_to_intersection()
    tracker.drive_past_intersection()
    print("Cross detected! Reversing direction...")
    tracker.turn_clockwise()
    tracker.turn_clockwise()  # two 90-degree turns = 180-degree reversal

print("Complete! 4 reversals done.")
