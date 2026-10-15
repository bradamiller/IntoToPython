# Lesson 8: Driving the Path - SOLUTION
# Functions that drive the robot along a Manhattan path using the
# Module 2/3 driving toolkit for line following and turning.

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
        left = BASE_EFFORT - error * KP
        right = BASE_EFFORT + error * KP
        drivetrain.set_effort(left, right)
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


# ===== Driving Functions (SOLUTION) =====
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
    """Turn from heading to desired the short way round. Returns desired."""
    # Quarter turns clockwise to get there: 0 = none, 1 = right, 2 = around,
    # 3 = left (one counterclockwise turn beats three clockwise ones).
    turns = (desired - heading) % 4
    if turns == 3:
        turn_counterclockwise()
    else:
        for i in range(turns):
            turn_clockwise()
    return desired


def drive_path(path, position, heading):
    for next_pos in path:
        needed = desired_heading(position, next_pos)
        heading = turn_to(heading, needed)
        track_to_intersection()
        drive_past_intersection()
        position = next_pos
    return position, heading


# ===== Test the Integration =====

# Test 1: Manhattan path computation
print("=== Test 1: Manhattan Paths ===")
path = compute_manhattan_path((0, 0), (2, 2))
print("Path from (0,0) to (2,2):", path)
print("Steps:", len(path))
print()

# Test 2: Starting state
print("=== Test 2: Starting State ===")
position, heading = (0, 0), 0
print("Position:", position)
print("Heading:", HEADING_NAMES[heading])
print()

# Test 3: Drive one path
print("=== Test 3: Drive (0,0) to (2,2) ===")
path = compute_manhattan_path(position, (2, 2))
print("Path:", path)
position, heading = drive_path(path, position, heading)
print("Final position:", position)
print("Final heading:", HEADING_NAMES[heading])
print()

# Test 4: Drive a second path (continuing from where we are)
print("=== Test 4: Drive (2,2) to (0,3) ===")
path2 = compute_manhattan_path(position, (0, 3))
print("Path:", path2)
position, heading = drive_path(path2, position, heading)
print("Final position:", position)
print("Final heading:", HEADING_NAMES[heading])
print()

# Test 5: Multi-destination loop
print("=== Test 5: Multi-Destination ===")
position, heading = (0, 0), 0
destinations = [(2, 0), (2, 3), (0, 3)]

for dest in destinations:
    print("--- Navigating to", dest, "---")
    path = compute_manhattan_path(position, dest)
    print("Path:", path)
    position, heading = drive_path(path, position, heading)
    print("Arrived at:", position,
          "heading", HEADING_NAMES[heading])
    print()

print("=== All tests complete ===")
