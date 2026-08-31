# Lesson 9: Final Project - SOLUTION
# Multi-destination grid navigation with the XRP robot.

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


# ===== Manhattan algorithm (from Lesson 5) =====

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


# ===== Driving functions (from Lesson 8) =====
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


# ===== Main Program =====

board = Board.get_default_board()

position = (0, 0)
heading = 0  # heading North

# Four destinations that form a tour of the grid
destinations = [(3, 0), (3, 3), (0, 3), (0, 0)]

print("=== XRP Grid Navigation: Final Project ===")
print("Starting at:", position)
print("Heading:", HEADING_NAMES[heading])
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
    path = compute_manhattan_path(position, dest)
    print("Path:", path)
    print("Steps:", len(path))

    # Drive the computed path
    position, heading = drive_path(path, position, heading)

    print("Arrived at:", position)
    print("Heading:", HEADING_NAMES[heading])
    print()

print("=== All destinations reached! ===")
print("Final position:", position)
print("Total destinations visited:", len(destinations))
