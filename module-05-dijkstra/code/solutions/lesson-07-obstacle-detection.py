# Lesson 7: Obstacle Detection with the Rangefinder - SOLUTION
# Use the ultrasonic sensor to detect blocked intersections. The planner was
# already tested on paper in Lesson 6; the only new thing here is DETECTION:
# read the rangefinder and call add_blocked(), then ask for a new path.

from XRPLib.rangefinder import Rangefinder
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


# ===== Driving Functions (this module's simplified turn+drive style) =====

drivetrain = DifferentialDrive.get_default_differential_drive()


def get_needed_direction(position, next_pos):
    row_diff = next_pos[0] - position[0]
    col_diff = next_pos[1] - position[1]
    if row_diff == 1:
        return "S"
    elif row_diff == -1:
        return "N"
    elif col_diff == 1:
        return "E"
    elif col_diff == -1:
        return "W"


def turn_to_direction(heading, direction):
    """Turn the robot to face direction. Returns the new heading."""
    right_turns = {"N": "E", "E": "S", "S": "W", "W": "N"}
    left_turns = {"N": "W", "W": "S", "S": "E", "E": "N"}

    if heading == direction:
        pass
    elif right_turns[heading] == direction:
        drivetrain.turn(90)
        heading = direction
    elif left_turns[heading] == direction:
        drivetrain.turn(-90)
        heading = direction
    else:
        drivetrain.turn(180)
        heading = direction

    return heading


def drive_one_step():
    drivetrain.straight(20)


# ===== Setup =====

board = Board.get_default_board()
rangefinder = Rangefinder.get_default_rangefinder()

THRESHOLD = 15  # cm -- closer than this means blocked

position = (0, 0)
heading = "N"
destination = (3, 3)

# Plan and PRINT the path before the robot moves. Read it: is it what you
# expected? This is the Lesson 6 paper test, built into every run.
path = compute_bfs_path(position, destination)
print("Planned path:", path)

board.wait_for_button()
print("Starting obstacle detection demo!")


# ===== Navigate with Obstacle Detection =====

for next_pos in path:

    # Turn to face the next intersection
    direction = get_needed_direction(position, next_pos)
    heading = turn_to_direction(heading, direction)

    # Check rangefinder
    distance = rangefinder.distance()
    print("At", position, "checking ahead:", distance, "cm")

    if distance < THRESHOLD:
        # Obstacle detected! Tell the planner, the same way the tests did.
        add_blocked(next_pos)
        print("Obstacle at", next_pos, "! Rerouting...")

        # Ask for a new path from where we are. The planner rebuilds its
        # graph from BLOCKED, so the wall is already missing from it.
        path = compute_bfs_path(position, destination)
        print("New path:", path)
        break  # Restart the path-following loop (in a full program, this
               # would be an outer while loop -- see Lesson 8)
    else:
        # No obstacle -- drive forward
        drive_one_step()
        position = next_pos
        print("Drove to", position)

print("Navigation complete!")
print("Final position:", position)
print("Obstacles found:", BLOCKED)
