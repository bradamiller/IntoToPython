# Lesson 9: Final Project - STARTER
# Multi-destination grid navigation with the XRP robot.
#
# Team: ________________________
# Date: ________________________
#
# Your mission:
#   The robot starts at (0, 0) facing North (heading 0).
#   It must visit 4 or more destinations on the grid in order.
#   For each destination, compute the path and drive it.
#
# Requirements:
#   - At least 4 destinations
#   - Print each path before driving it
#   - Update manhattan.position after each leg
#   - Robot must physically navigate the grid

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


# ===== Manhattan Class (complete) =====

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


# ===== Navigator Class (complete) =====
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


# ===== YOUR MAIN PROGRAM (YOU COMPLETE THIS) =====

# TODO: Create a Board object for wait_for_button()
# Hint: board = Board.get_default_board()


# TODO: Create a Manhattan object starting at (0, 0)


# TODO: Create a Navigator object starting at (0, 0) heading North (0)


# TODO: Define your list of 4 or more destinations
# Example: destinations = [(2, 0), (2, 3), (0, 3), (0, 0)]
# Choose your own destinations!


# Print the mission briefing
# TODO: Uncomment after defining your variables
# print("=== XRP Grid Navigation: Final Project ===")
# print("Starting at:", manhattan.position)
# print("Destinations:", destinations)
# print()

# TODO: Wait for button press before starting
# Hint: board.wait_for_button()


# TODO: Write a for loop that goes through each destination
# For each destination:
#   1. Print which destination you are navigating to
#   2. Compute the path using manhattan.compute_path(dest)
#   3. Print the path and number of steps
#   4. Drive the path using navigator.drive_path(path)
#   5. Update manhattan.position = navigator.position
#   6. Print arrival confirmation


# TODO: Print a completion message
# print("=== All destinations reached! ===")
# print("Final position:", navigator.position)


# ===== EXTENSION CHALLENGES =====
# Try these after your basic program works!
#
# Challenge 1: Return Home
#   Add (0, 0) as the last destination so the robot returns to start.
#
# Challenge 2: Round Trip
#   After visiting all destinations, reverse the list and visit them
#   all again in reverse order.
#   Hint: reversed_dests = list(reversed(destinations))
#
# Challenge 3: Button Pause
#   Add board.wait_for_button() between each leg so you can
#   check the robot's position before it continues.
#
# Challenge 4: Custom Destinations
#   Ask the user to type in destinations:
#   row = int(input("Enter row: "))
#   col = int(input("Enter col: "))
