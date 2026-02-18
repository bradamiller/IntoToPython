# Lesson 9: Final Project - STARTER
# Multi-destination grid navigation with the XRP robot.
#
# Team: ________________________
# Date: ________________________
#
# Your mission:
#   The robot starts at (0, 0) facing North.
#   It must visit 4 or more destinations on the grid in order.
#   For each destination, compute the path and drive it.
#
# Requirements:
#   - At least 4 destinations
#   - Print each path before driving it
#   - Update manhattan.position after each leg
#   - Robot must physically navigate the grid

from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board


# ===== Manhattan Class (complete) =====

class Manhattan:

    def __init__(self, start):
        """Create a Manhattan navigator starting at the given position."""
        self.position = start

    def compute_path(self, destination):
        """Compute a Manhattan path from current position to destination.
        Returns a list of (row, col) tuples."""
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


# ===== Navigator Class (complete) =====

class Navigator:

    def __init__(self, start, heading):
        """Create a Navigator at the given start position and heading."""
        self.position = start
        self.heading = heading
        self.drivetrain = DifferentialDrive.get_default_differential_drive()

    def get_needed_direction(self, next_pos):
        """Determine direction (N/S/E/W) to move from current position to next_pos."""
        row_diff = next_pos[0] - self.position[0]
        col_diff = next_pos[1] - self.position[1]
        if row_diff == 1:
            return "S"
        elif row_diff == -1:
            return "N"
        elif col_diff == 1:
            return "E"
        elif col_diff == -1:
            return "W"

    def turn_to(self, direction):
        """Turn the robot to face the given direction."""
        right_turns = {"N": "E", "E": "S", "S": "W", "W": "N"}
        left_turns = {"N": "W", "W": "S", "S": "E", "E": "N"}

        if self.heading == direction:
            pass
        elif right_turns[self.heading] == direction:
            self.drivetrain.turn(90)
            self.heading = direction
        elif left_turns[self.heading] == direction:
            self.drivetrain.turn(-90)
            self.heading = direction
        else:
            self.drivetrain.turn(180)
            self.heading = direction

    def drive_path(self, path):
        """Drive the robot along the given path."""
        for i in range(1, len(path)):
            next_pos = path[i]
            direction = self.get_needed_direction(next_pos)
            self.turn_to(direction)
            self.drivetrain.straight(20)
            self.position = next_pos


# ===== YOUR MAIN PROGRAM (YOU COMPLETE THIS) =====

# TODO: Create a Board object for wait_for_button()
# Hint: board = Board.get_default_board()


# TODO: Create a Manhattan object starting at (0, 0)


# TODO: Create a Navigator object starting at (0, 0) heading "N"


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
