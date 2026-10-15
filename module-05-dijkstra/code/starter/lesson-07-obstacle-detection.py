# Lesson 7: Obstacle Detection with the Rangefinder
# Use the ultrasonic sensor to detect blocked intersections.
#
# Team: ________________________
# Date: ________________________
#
# The rangefinder measures distance in cm.
# If the distance is less than a threshold, the intersection ahead is blocked.

from XRPLib.rangefinder import Rangefinder
from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board


# ===== Pathfinding toolkit (Lessons 4-5) =====
# compute_bfs_path(position, destination) is TOLD where the robot is and
# returns the intersections to drive TO. BLOCKED is shared: the rangefinder
# loop below adds to it with add_blocked(), exactly as the paper tests do.

ROWS = 4
COLS = 4
BLOCKED = []


def add_blocked(intersection):
    if intersection not in BLOCKED:
        BLOCKED.append(intersection)


def clear_blocked():
    while len(BLOCKED) > 0:
        BLOCKED.pop()


def build_graph(rows, cols, blocked):
    graph = {}
    for r in range(rows):
        for c in range(cols):
            if (r, c) in blocked:
                continue
            neighbors = []
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in blocked:
                    neighbors.append((nr, nc))
            graph[(r, c)] = neighbors
    return graph


def compute_bfs_path(position, destination):
    graph = build_graph(ROWS, COLS, BLOCKED)
    if position not in graph or destination not in graph:
        return []
    previous = {position: None}
    to_visit = [position]
    while len(to_visit) > 0:
        current = to_visit.pop(0)
        if current == destination:
            break
        for neighbor in graph[current]:
            if neighbor not in previous:
                previous[neighbor] = current
                to_visit.append(neighbor)
    if destination not in previous:
        return []
    path = []
    current = destination
    while current != position:
        path.append(current)
        current = previous[current]
    path.reverse()
    return path


# ===== Driving toolkit (from Modules 2 and 4) =====
# Exactly the functions the robot drove with in Module 4. Nothing new here.

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


# ===== Setup =====

board = Board.get_default_board()
rangefinder = Rangefinder.get_default_rangefinder()

OBSTACLE_CM = 15     # rangefinder reading closer than this means blocked

position = (0, 0)
heading = 0          # 0 = N, 1 = E, 2 = S, 3 = W, as in Module 4
destination = (3, 3)

# TODO: Plan and PRINT the path BEFORE the button press. Read it before the
# robot moves -- this is the Lesson 6 paper test, built into every run.
# path = compute_bfs_path(position, destination)
# print("Planned path:", path)

board.wait_for_button()
print("Starting obstacle detection demo!")


# ===== Navigate with Obstacle Detection =====
# (The planner rebuilds its graph from BLOCKED on every call -- nothing to build here.)

# TODO: Walk through the path one step at a time. This is Module 4's
# drive_path() with ONE extra step: look before you drive.
# For each step:
#   1. Turn to face the next intersection:
#        needed = desired_heading(position, next_pos)
#        heading = turn_to(heading, needed)
#   2. NEW: read the rangefinder
#   3. If distance < OBSTACLE_CM:
#      - Tell the planner with add_blocked(next_pos)
#      - Ask the planner for a new path from where we are
#      - Print a message about the obstacle
#   4. If no obstacle:
#      - track_to_intersection(), then drive_past_intersection()
#      - Update position

# for next_pos in path:
#
#     # Turn to face the next intersection
#     needed = desired_heading(position, next_pos)
#     heading = turn_to(heading, needed)
#
#     # NEW: look ahead before driving
#     distance = rangefinder.distance()
#     print("At", position, "facing", HEADING_NAMES[heading], "- ahead:", distance, "cm")
#
#     if distance < OBSTACLE_CM:
#         # TODO: Obstacle detected!
#         # Tell the planner: add_blocked(next_pos)
#         # add_blocked(???)
#         # print("Obstacle at", next_pos, "! Rerouting...")
#
#         # TODO: Ask the planner for a new path from where we are
#         # path = compute_bfs_path(position, destination)
#         # print("New path:", path)
#         # break  # Restart the path-following loop
#         pass
#     else:
#         # TODO: No obstacle -- drive to the next intersection
#         # track_to_intersection()
#         # drive_past_intersection()
#         # position = next_pos
#         # print("Drove to", position)
#         pass

print("Navigation complete!")
print("Final position:", position)
print("Obstacles found:", BLOCKED)
