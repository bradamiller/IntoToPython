# Module 6, Lesson 4: Drive It
#
# Team: ________________________
# Date: ________________________
# The robot on the slow-segment grid. Same trip twice: once planned by BFS,
# once by Dijkstra. The program prints each planner's path and COST before
# the button, then times the drive, so the class can see steps vs. seconds.
#
# Driving is Module 4's toolkit, unchanged. The only Module 6 line is which
# planner gets called. Type the slow segment you measured in Lesson 1 into
# SLOW_SEGMENT below.

import time
from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board


# ===== The grid, the blocked list, and (NEW) the slow edges =====

ROWS = 4
COLS = 4
BLOCKED = []
SLOW_EDGES = []      # NEW: each entry is (intersection_a, intersection_b, cost)


def add_blocked(intersection):
    if intersection not in BLOCKED:
        BLOCKED.append(intersection)


def clear_blocked():
    while len(BLOCKED) > 0:
        BLOCKED.pop()


def add_slow_edge(a, b, cost):
    """NEW: the segment between a and b takes 'cost' blocks' worth of time.
    Measure it with a stopwatch: if a normal block takes 4 seconds and this
    one takes 12, its cost is 3."""
    SLOW_EDGES.append((a, b, cost))


def clear_slow_edges():
    while len(SLOW_EDGES) > 0:
        SLOW_EDGES.pop()


def weight(a, b):
    """NEW: how much the segment from a to b costs. 1 unless it is slow."""
    for (x, y, cost) in SLOW_EDGES:
        if (a == x and b == y) or (a == y and b == x):
            return cost
    return 1


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


def print_grid(rows, cols, blocked, numbers):
    """Draw the grid: X for a blocked intersection, otherwise the number in
    the numbers dictionary (a ring number, a distance, ...), or . if none."""
    print("     ", end="")
    for c in range(cols):
        print(str(c).rjust(3), end="")
    print()
    print("    " + "-" * (3 * cols + 1))
    for r in range(rows):
        print(str(r).rjust(2) + " | ", end="")
        for c in range(cols):
            if (r, c) in blocked:
                print("  X", end="")
            elif (r, c) in numbers:
                print(str(numbers[(r, c)]).rjust(3), end="")
            else:
                print("  .", end="")
        print()


# ===== Planner 2: BFS, unchanged from Lesson 5 (for comparison) =====

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


# ===== Planner 3: Dijkstra -- a copy of BFS with two changes =====

def closest(intersections, distance):
    """CHANGED (helper): of the intersections still to visit, the one with
    the smallest distance so far."""
    best = intersections[0]
    for node in intersections:
        if distance[node] < distance[best]:
            best = node
    return best


def compute_dijkstra_path(position, destination):
    graph = build_graph(ROWS, COLS, BLOCKED)
    if position not in graph or destination not in graph:
        return []

    previous = {position: None}
    distance = {position: 0}                 # NEW: best total cost found so far
    to_visit = [position]

    while len(to_visit) > 0:
        current = closest(to_visit, distance)    # CHANGED: was to_visit.pop(0)
        to_visit.remove(current)
        if current == destination:
            break
        for neighbor in graph[current]:
            new_distance = distance[current] + weight(current, neighbor)   # CHANGED: was "+1 step"
            if neighbor not in distance or new_distance < distance[neighbor]:  # CHANGED: keep the cheaper way
                distance[neighbor] = new_distance
                previous[neighbor] = current
                if neighbor not in to_visit:
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


def dijkstra_distances(position):
    """Every intersection's cheapest cost from position (for the picture)."""
    graph = build_graph(ROWS, COLS, BLOCKED)
    distance = {position: 0}
    to_visit = [position]
    while len(to_visit) > 0:
        current = closest(to_visit, distance)
        to_visit.remove(current)
        for neighbor in graph[current]:
            new_distance = distance[current] + weight(current, neighbor)
            if neighbor not in distance or new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                if neighbor not in to_visit:
                    to_visit.append(neighbor)
    return distance


# ===== One more property for the harness: total cost =====

def path_cost(position, path):
    """NEW: add up the weight of every segment the path drives."""
    total = 0
    here = position
    for step in path:
        total = total + weight(here, step)
        here = step
    return total


# ===== Sensor functions (from Module 2 Lesson 8) =====
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


# ===== Line-tracking functions (from Module 2 Lesson 9) =====

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


HEADING_NAMES = ["N", "E", "S", "W"]


def desired_heading(position, next_pos):
    row_diff = next_pos[0] - position[0]
    col_diff = next_pos[1] - position[1]
    if col_diff == 0 and row_diff == -1:
        return 0  # North
    if row_diff == 0 and col_diff == 1:
        return 1  # East
    if col_diff == 0 and row_diff == 1:
        return 2  # South
    if row_diff == 0 and col_diff == -1:
        return 3  # West
    # Not one step apart: say so now, where the problem is found,
    # instead of handing back None and letting turn_to() go wrong later.
    raise ValueError(str(position) + " and " + str(next_pos) + " are not neighbors")


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


# ===== Setup =====

board = Board.get_default_board()

# The slow segment you timed in Lesson 1: (intersection_a, intersection_b, weight).
# The detour round one segment is 3 normal blocks, so a weight of exactly 3
# ties with it; the slow segment has to be clearly worse than that (4 or more)
# for the two planners to disagree.
# TODO: type in the segment you timed and its weight (seconds / seconds per normal block)
SLOW_SEGMENT = ((0, 1), (0, 2), 1)
add_slow_edge(SLOW_SEGMENT[0], SLOW_SEGMENT[1], SLOW_SEGMENT[2])

# TODO: a start and destination for which the slow road is the fewest-steps route
position = (0, 0)
heading = 0          # 0 = N, 1 = E, 2 = S, 3 = W, as in Module 4
destination = (0, 3)

# Which planner drives this run? Change this line between runs.
PLANNER_NAME = "BFS"          # or "Dijkstra"

if PLANNER_NAME == "Dijkstra":
    planner = compute_dijkstra_path
else:
    planner = compute_bfs_path

# Plan and PRINT before the robot moves -- both planners, so the comparison
# is on screen before either run.
for (name, p) in [("BFS", compute_bfs_path), ("Dijkstra", compute_dijkstra_path)]:
    path = p(position, destination)
    print(name.ljust(9), "steps:", len(path), " cost:", path_cost(position, path), " ", path)

path = planner(position, destination)
print()
print("Driving the", PLANNER_NAME, "path. Press the button.")
board.wait_for_button()

start_time = time.time()
position, heading = drive_path(path, position, heading)
elapsed = time.time() - start_time

print("Arrived at", position, "facing", HEADING_NAMES[heading])
print(PLANNER_NAME, "took", round(elapsed, 1), "seconds for", len(path), "steps (cost", path_cost((0, 0), path), ")")
