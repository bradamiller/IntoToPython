# Lesson 9: Final Project - SOLUTION
# Multi-destination grid navigation with the XRP robot.

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


# ===== Manhattan Class =====

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


# ===== Navigator Class =====
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
        while self.heading != needed_heading:
            self.line_track.turn_right()
            self.heading = self.heading + 1
            if self.heading == 4:
                self.heading = 0

    def drive_path(self, path):
        for next_pos in path:
            needed = self.get_needed_heading(next_pos)
            if self.heading == needed:
                self.line_track.drivetrain.straight(8)
            self.turn_to(needed)
            self.line_track.track_until_cross()
            self.position = next_pos


# ===== Main Program =====

board = Board.get_default_board()

manhattan = Manhattan((0, 0))
navigator = Navigator((0, 0), 0)  # Start heading North

# Four destinations that form a tour of the grid
destinations = [(3, 0), (3, 3), (0, 3), (0, 0)]

print("=== XRP Grid Navigation: Final Project ===")
print("Starting at:", manhattan.position)
print("Heading:", HEADING_NAMES[navigator.heading])
print("Destinations:", destinations)
print()

# Wait for button press to start
print("Press the button to begin navigation...")
board.wait_for_button()
print()

# Navigate to each destination
for dest in destinations:
    print("--- Navigating to", dest, "---")

    # Compute the path from current position to this destination
    path = manhattan.compute_path(dest)
    print("Path:", path)
    print("Steps:", len(path))

    # Drive the computed path
    navigator.drive_path(path)

    # Update Manhattan's position for the next leg
    manhattan.position = navigator.position

    print("Arrived at:", navigator.position)
    print("Heading:", HEADING_NAMES[navigator.heading])
    print()

print("=== All destinations reached! ===")
print("Final position:", navigator.position)
print("Total destinations visited:", len(destinations))
