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
#   - Reassign position, heading after each leg's drive_path() call
#   - Robot must physically navigate the grid

from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board


# ===== Sensor toolkit (from Module 2 Lesson 8) =====

reflectance = Reflectance.get_default_reflectance()
THRESHOLD = 0.5

def get_left():
    return reflectance.get_left()

def get_right():
    return reflectance.get_right()

def get_error():
    return get_left() - get_right()

def is_at_cross():
    return get_left() > THRESHOLD and get_right() > THRESHOLD

def is_off_line():
    return get_left() < THRESHOLD and get_right() < THRESHOLD


# ===== Driving toolkit (from Module 2 Lesson 9) =====

drivetrain = DifferentialDrive.get_default_differential_drive()
BASE_EFFORT = 0.4
KP = 0.5

def clear_intersection():
    drivetrain.straight(8, 0.5)

def track_until_cross():
    while not is_at_cross():
        error = get_error()
        left = BASE_EFFORT - error * KP
        right = BASE_EFFORT + error * KP
        drivetrain.set_effort(left, right)
    drivetrain.stop()

def turn_right():
    clear_intersection()
    drivetrain.set_effort(0.3, -0.3)
    while is_off_line():
        pass
    drivetrain.stop()


# ===== Manhattan algorithm (complete — from Lesson 5) =====

def compute_manhattan_path(position, destination):
    path = []
    current_row, current_col = position
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


# ===== Driving functions (complete — from Lesson 8) =====
# Headings: 0 = North, 1 = East, 2 = South, 3 = West

HEADING_NAMES = ["N", "E", "S", "W"]


def desired_heading(position, next_pos):
    row_diff = next_pos[0] - position[0]
    col_diff = next_pos[1] - position[1]
    if row_diff == -1:
        return 0  # North
    elif col_diff == 1:
        return 1  # East
    elif row_diff == 1:
        return 2  # South
    elif col_diff == -1:
        return 3  # West


def turn_to(heading, desired):
    while heading != desired:
        turn_right()
        heading = heading + 1
        if heading == 4:
            heading = 0
    return heading


def drive_path(path, position, heading):
    for next_pos in path:
        needed = desired_heading(position, next_pos)
        if heading == needed:
            clear_intersection()
        heading = turn_to(heading, needed)
        track_until_cross()
        position = next_pos
    return position, heading


# ===== YOUR MAIN PROGRAM (YOU COMPLETE THIS) =====

# TODO: Create a Board object for wait_for_button()
# Hint: board = Board.get_default_board()


# TODO: Set up starting position and heading
# Hint: position = (0, 0)
#       heading = 0


# TODO: Define your list of 4 or more destinations
# Example: destinations = [(2, 0), (2, 3), (0, 3), (0, 0)]
# Choose your own destinations!


# Print the mission briefing
# TODO: Uncomment after defining your variables
# print("=== XRP Grid Navigation: Final Project ===")
# print("Starting at:", position)
# print("Destinations:", destinations)
# print()

# TODO: Wait for button press before starting
# Hint: board.wait_for_button()


# TODO: Write a for loop that goes through each destination
# For each destination:
#   1. Print which destination you are navigating to
#   2. Compute the path using compute_manhattan_path(position, dest)
#   3. Print the path and number of steps
#   4. Drive the path: position, heading = drive_path(path, position, heading)
#   5. Print arrival confirmation


# TODO: Print a completion message
# print("=== All destinations reached! ===")
# print("Final position:", position)


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
