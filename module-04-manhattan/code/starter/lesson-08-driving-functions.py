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
#   3. Turn to face it, the short way round
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

def is_either_on_line():
    return get_left() > THRESHOLD or get_right() > THRESHOLD


# ===== Driving toolkit (from Module 2 Lesson 9) =====

drivetrain = DifferentialDrive.get_default_differential_drive()
BASE_EFFORT = 0.4
KP = 0.5
TURN_EFFORT = 0.25

def drive_past_intersection():
    # The sensors stop ON the cross, but the wheels are 8.75 cm behind them.
    # Drive that far so the axle is over the intersection: a turn then pivots
    # on it, and the next track_to_intersection() does not see this same cross.
    drivetrain.straight(8.75, 0.5)

def track_to_intersection():
    while not is_at_cross():
        error = get_error()
        correction = error * KP
        drivetrain.arcade(BASE_EFFORT, -correction)
    drivetrain.stop()

def turn_clockwise():
    # A blind turn first, far enough to get both sensors off the line we were
    # on. Then keep turning until a sensor finds the cross street. No timing
    # involved: the sensors say when the turn is done.
    drivetrain.turn(-60, TURN_EFFORT)
    drivetrain.arcade(0, -TURN_EFFORT)
    while not is_either_on_line():
        pass
    drivetrain.stop()

def turn_counterclockwise():
    drivetrain.turn(60, TURN_EFFORT)
    drivetrain.arcade(0, TURN_EFFORT)
    while not is_either_on_line():
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
      - col unchanged and row_diff == -1 --> 0 (North)
      - row unchanged and col_diff == 1  --> 1 (East)
      - col unchanged and row_diff == 1  --> 2 (South)
      - row unchanged and col_diff == -1 --> 3 (West)
      - anything else: raise ValueError -- they are not neighbors
    """
    # TODO: Calculate row_diff and col_diff
    # TODO: Return the correct heading number, checking both diffs each time
    # TODO: raise ValueError(...) if nothing matched
    pass


def turn_to(heading, desired):
    """Turn the robot to face the needed heading. Returns the new heading.

    heading: the robot's current heading (0-3)
    desired: the heading it needs to face (0-3)

    Logic:
      - turns = (desired - heading) % 4   is how many quarter turns clockwise
        get you there: 0 = none, 1 = one clockwise, 2 = turn around,
        3 = three clockwise -- which is the same as ONE counterclockwise
      - If turns == 3: call turn_counterclockwise() once
      - Otherwise: call turn_clockwise() that many times (a for loop)
      - Return desired (that is the heading now)

    Examples:
      - heading 0, need 1: turns = 1, one clockwise
      - heading 0, need 2: turns = 2, two clockwise
      - heading 3, need 0: turns = (0 - 3) % 4 = 1, one clockwise
      - heading 0, need 3: turns = 3, ONE counterclockwise
    """
    # TODO: compute turns
    # TODO: if turns == 3 turn counterclockwise once, else turn clockwise
    #       `turns` times
    # TODO: return desired
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
        2. Turn to face it: heading = turn_to(heading, needed)
        3. Follow the line to the next intersection: track_to_intersection()
        4. Put the wheels over the intersection: drive_past_intersection()
           (so the next turn pivots on it, and the next track does not see
           this same cross and stop at once)
        5. Update position to the new position
      - Return position, heading
    """
    # TODO: Write the for loop (for next_pos in path:)
    # TODO: For each step: needed heading, turn, track, drive past, update
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
