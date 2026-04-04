# Lesson 8: Implementing the Navigator Class - SOLUTION
# The Navigator class drives the robot along a Manhattan path
# using LineTrack for line following and turning.

from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board
import time


# ===== LineSensor Class (from Module 2) =====

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


# ===== LineTrack Class (from Module 2) =====

class LineTrack:
    def __init__(self):
        self.sensor = LineSensor()
        self.drivetrain = DifferentialDrive.get_default_differential_drive()
        self.base_effort = 0.4
        self.Kp = 0.5

    def track_until_cross(self):
        while not self.sensor.is_at_cross():
            error = self.sensor.get_error()
            correction = error * self.Kp
            self.drivetrain.arcade(self.base_effort, -correction)
        self.drivetrain.stop()

    def turn_right(self):
        self.drivetrain.arcade(self.base_effort, 0)
        time.sleep(0.3)
        self.drivetrain.arcade(0, 0.3)
        time.sleep(0.3)
        while self.sensor.is_off_line():
            pass
        self.drivetrain.stop()

    def turn_left(self):
        self.drivetrain.arcade(self.base_effort, 0)
        time.sleep(0.3)
        self.drivetrain.arcade(0, -0.3)
        time.sleep(0.3)
        while self.sensor.is_off_line():
            pass
        self.drivetrain.stop()


# ===== Manhattan Class (complete — from Lesson 5) =====

class Manhattan:

    def __init__(self, start):
        self.position = start

    def compute_path(self, destination):
        path = [self.position]

        current_row = self.position[0]
        current_col = self.position[1]
        dest_row = destination[0]
        dest_col = destination[1]

        if dest_row > current_row:
            row_step = 1
        else:
            row_step = -1

        if dest_col > current_col:
            col_step = 1
        else:
            col_step = -1

        while current_row != dest_row:
            current_row = current_row + row_step
            path.append((current_row, current_col))

        while current_col != dest_col:
            current_col = current_col + col_step
            path.append((current_row, current_col))

        return path


# ===== Navigator Class (SOLUTION) =====
# Headings: 0 = North, 1 = East, 2 = South, 3 = West

HEADING_NAMES = ["N", "E", "S", "W"]


class Navigator:

    def __init__(self, start, heading):
        self.position = start
        self.heading = heading
        self.line_track = LineTrack()

    def get_needed_heading(self, next_pos):
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

    def turn_to(self, needed_heading):
        turns = (needed_heading - self.heading) % 4
        for i in range(turns):
            self.line_track.turn_right()
        self.heading = needed_heading

    def drive_path(self, path):
        for i in range(1, len(path)):
            next_pos = path[i]
            needed = self.get_needed_heading(next_pos)
            turns = (needed - self.heading) % 4
            if turns == 0:
                self.line_track.drivetrain.straight(8)
            self.turn_to(needed)
            self.line_track.track_until_cross()
            self.position = next_pos


# ===== Test the Integration =====

# Test 1: Manhattan path computation
print("=== Test 1: Manhattan Paths ===")
manhattan = Manhattan((0, 0))
path = manhattan.compute_path((2, 2))
print("Path from (0,0) to (2,2):", path)
print("Steps:", len(path) - 1)
print()

# Test 2: Navigator creation
print("=== Test 2: Navigator Setup ===")
navigator = Navigator((0, 0), 0)
print("Position:", navigator.position)
print("Heading:", HEADING_NAMES[navigator.heading])
print()

# Test 3: Drive one path
print("=== Test 3: Drive (0,0) to (2,2) ===")
path = manhattan.compute_path((2, 2))
print("Path:", path)
navigator.drive_path(path)
print("Final position:", navigator.position)
print("Final heading:", HEADING_NAMES[navigator.heading])
print()

# Test 4: Drive a second path (continuing from where we are)
print("=== Test 4: Drive (2,2) to (0,3) ===")
manhattan.position = navigator.position
path2 = manhattan.compute_path((0, 3))
print("Path:", path2)
navigator.drive_path(path2)
print("Final position:", navigator.position)
print("Final heading:", HEADING_NAMES[navigator.heading])
print()

# Test 5: Multi-destination loop
print("=== Test 5: Multi-Destination ===")
manhattan = Manhattan((0, 0))
navigator = Navigator((0, 0), 0)
destinations = [(2, 0), (2, 3), (0, 3)]

for dest in destinations:
    print("--- Navigating to", dest, "---")
    path = manhattan.compute_path(dest)
    print("Path:", path)
    navigator.drive_path(path)
    manhattan.position = navigator.position
    print("Arrived at:", navigator.position,
          "heading", HEADING_NAMES[navigator.heading])
    print()

print("=== All tests complete ===")
