# Lesson 9: LineTrack Class
# A class that uses LineSensor for line following and turning

from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
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


class LineTrack:
    def __init__(self):
        self.sensor = LineSensor()
        self.drivetrain = DifferentialDrive.get_default_differential_drive()
        self.base_effort = 0.4
        self.Kp = 0.5

    # TODO: Write track_until_cross() method
    # Follow the line until an intersection is detected
    # Use a while loop with self.sensor.is_at_cross()
    # Inside the loop: calculate error, set motor efforts
    # After the loop: stop the robot
    # def track_until_cross(self):
    #     ???

    # TODO: Write turn_right() method
    # 1. Drive forward briefly to clear intersection
    # 2. Start turning right (left forward, right backward)
    # 3. Keep turning while off the line
    # 4. Stop when line is found
    # def turn_right(self):
    #     ???

    # TODO: Write turn_left() method (same as turn_right but opposite direction)
    # def turn_left(self):
    #     ???


# --- Test Program ---
board = Board.get_default_board()
tracker = LineTrack()

board.wait_for_button()

print("Following line to cross...")
tracker.track_until_cross()
print("Cross found! Turning right...")
tracker.turn_right()
print("Following line again...")
tracker.track_until_cross()
print("Done!")
