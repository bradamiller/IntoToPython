# Lesson 8 Optional Extension: The Navigator Class
# Classes-track reference: the driving functions from
# lesson-08-driving-functions.py, repackaged as a Navigator class
# that composes a LineTrack object. Robot behavior is identical.

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


class Manhattan:

    def __init__(self, start):
        self.position = start

    def compute_path(self, destination):
        path = []
        current_row, current_col = self.position
        dest_row, dest_col = destination

        while current_row < dest_row:
            current_row = current_row + 1
            path.append((current_row, current_col))
        while current_row > dest_row:
            current_row = current_row - 1
            path.append((current_row, current_col))
        while current_col < dest_col:
            current_col = current_col + 1
            path.append((current_row, current_col))
        while current_col > dest_col:
            current_col = current_col - 1
            path.append((current_row, current_col))

        return path


HEADING_NAMES = ["N", "E", "S", "W"]


class Navigator:

    def __init__(self, start, heading):
        self.position = start
        self.heading = heading  # 0=N, 1=E, 2=S, 3=W
        self.line_track = LineTrack()

    def desired_heading(self, next_pos):
        row_diff = next_pos[0] - self.position[0]
        col_diff = next_pos[1] - self.position[1]
        if row_diff == -1:
            return 0  # North
        elif col_diff == 1:
            return 1  # East
        elif row_diff == 1:
            return 2  # South
        elif col_diff == -1:
            return 3  # West

    def turn_to(self, desired):
        while self.heading != desired:
            self.line_track.turn_right()
            self.heading = self.heading + 1
            if self.heading == 4:
                self.heading = 0

    def drive_path(self, path):
        for next_pos in path:
            needed = self.desired_heading(next_pos)
            if self.heading == needed:
                self.line_track.clear_intersection()
            self.turn_to(needed)
            self.line_track.track_until_cross()
            self.position = next_pos


# ===== Test the Integration =====

print("=== Test 1: Manhattan Paths ===")
manhattan = Manhattan((0, 0))
path = manhattan.compute_path((2, 2))
print("Path from (0,0) to (2,2):", path)
print()

print("=== Test 2: Navigator Setup ===")
navigator = Navigator((0, 0), 0)
print("Position:", navigator.position)
print("Heading:", HEADING_NAMES[navigator.heading])
print()

print("=== Test 3: Drive (0,0) to (2,2) ===")
path = manhattan.compute_path((2, 2))
navigator.drive_path(path)
print("Final position:", navigator.position)
print("Final heading:", HEADING_NAMES[navigator.heading])
print()

print("=== Test 4: Drive (2,2) to (0,3) ===")
manhattan.position = navigator.position
path2 = manhattan.compute_path((0, 3))
navigator.drive_path(path2)
print("Final position:", navigator.position)
print("Final heading:", HEADING_NAMES[navigator.heading])
