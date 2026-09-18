# Lesson 8: Driving the Path - STARTER
# Functions that drive the robot along a Manhattan path using the
# Module 2/3 driving toolkit for line following and turning.
#
# Team: ________________________
# Date: ________________________
#
# We need functions that:
#   1. Know the current position and heading (0=N, 1=E, 2=S, 3=W)
#   2. Figure out which heading is needed for the next step
#   3. Turn right the correct number of times
#   4. Follow the line to the next intersection
#   5. Repeat for every step in the path
#   6. Return the updated position and heading when done

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


# ===== Driving Functions (YOU COMPLETE THESE) =====
# Headings: 0 = North, 1 = East, 2 = South, 3 = West

HEADING_NAMES = ["N", "E", "S", "W"]


def desired_heading(position, next_pos):
    """Determine heading number to move from position to next_pos.

    position: a (row, col) tuple -- the robot's current position
    next_pos: a (row, col) tuple one step away from position

    Returns: 0, 1, 2, or 3

    Logic:
      - row_diff = next_pos[0] - position[0]
      - col_diff = next_pos[1] - position[1]
      - row_diff == -1 --> 0 (North)
      - col_diff == 1  --> 1 (East)
      - row_diff == 1  --> 2 (South)
      - col_diff == -1 --> 3 (West)
    """
    # TODO: Calculate row_diff and col_diff
    # TODO: Return the correct heading number based on the diff values
    pass


def turn_to(heading, desired):
    """Turn the robot to face the needed heading. Returns the new heading.

    heading: the robot's current heading (0-3)
    desired: the heading it needs to face (0-3)

    Logic:
      - While heading != desired:
        - Call turn_right() to turn right once
        - Add 1 to heading
        - If heading == 4, reset it to 0
      - Return heading

    Examples:
      - heading 0, need 1: one right turn (0 -> 1)
      - heading 0, need 2: two right turns (0 -> 1 -> 2)
      - heading 3, need 0: one right turn (3 -> 0, wraps around)
    """
    # TODO: Use a while loop that keeps turning right
    #       until heading equals desired
    # TODO: Inside the loop: turn right, add 1 to heading,
    #       reset to 0 if heading reaches 4
    # TODO: Return heading
    pass


def drive_path(path, position, heading):
    """Drive the robot along the given path. Returns (position, heading).

    path:     a list of (row, col) tuples from compute_manhattan_path()
              (does not include the starting position)
    position: the robot's current position
    heading:  the robot's current heading

    Logic:
      - Loop through each position in the path
      - For each step:
        1. Determine the needed heading using desired_heading()
        2. If already facing the right way, clear the intersection
        3. Turn to face the right direction using turn_to()
        4. Follow the line to the next intersection: track_until_cross()
        5. Update position to the new position
      - Return position, heading
    """
    # TODO: Write the for loop (for next_pos in path:)
    # TODO: For each step, get heading, clear if straight, turn, track, update
    # TODO: Return position, heading
    pass


# ===== Test Your Code =====

# Step 1: Test Manhattan path computation
path = compute_manhattan_path((0, 0), (2, 2))
print("Path from (0,0) to (2,2):", path)
print()

# Step 2: Set up starting state and test drive_path
# TODO: Uncomment these lines after completing the driving functions
# position, heading = (0, 0), 0
# print("Starting position:", position)
# print("Starting heading:", HEADING_NAMES[heading])
# print()

# Step 3: Test the full integration
# TODO: Uncomment after testing steps 1 and 2
# print("--- Driving path ---")
# position, heading = drive_path(path, position, heading)
# print("Final position:", position)
# print("Final heading:", HEADING_NAMES[heading])
