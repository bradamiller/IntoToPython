# Lesson 9: Module 5 Capstone Project - SOLUTION
# Full autonomous navigation with obstacle detection and learning.

from XRPLib.rangefinder import Rangefinder
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board


# ===== Dijkstra Functions =====

def build_dijkstra_graph(rows, cols, blocked):
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


def compute_dijkstra_path(position, destination, graph):
    if destination not in graph:
        return []
    distances = {}
    previous = {}
    to_visit = []
    for node in graph:
        distances[node] = 999999
        previous[node] = None
        to_visit.append(node)
    distances[position] = 0
    while len(to_visit) > 0:
        current = to_visit[0]
        for node in to_visit:
            if distances[node] < distances[current]:
                current = node
        if current == destination:
            break
        to_visit.remove(current)
        for neighbor in graph[current]:
            if neighbor in to_visit:
                new_dist = distances[current] + 1
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    previous[neighbor] = current
    path = []
    current = destination
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    if len(path) == 0 or path[0] != position:
        return []
    return path


# ===== Driving Functions =====

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


# ===== File I/O =====

def save_obstacles(blocked, filename="obstacles.txt"):
    """Save obstacles to a file."""
    f = open(filename, "w")
    for node in blocked:
        f.write(str(node[0]) + "," + str(node[1]) + "\n")
    f.close()
    print("Saved", len(blocked), "obstacles to", filename)


def load_obstacles(filename="obstacles.txt"):
    """Load obstacles from a file."""
    blocked = []
    try:
        f = open(filename, "r")
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 2:
                blocked.append((int(parts[0]), int(parts[1])))
        f.close()
        print("Loaded", len(blocked), "obstacles from", filename)
    except:
        print("No obstacle file found. Starting fresh.")
    return blocked


# ===== Navigation with Detection =====

def navigate_with_detection(position, heading, destination, blocked_nodes, rangefinder, threshold):
    """Navigate to destination, detecting obstacles along the way.

    Returns (position, heading, step_count, reroute_count).
    """
    step_count = 0
    reroute_count = 0

    arrived = False
    while not arrived:
        graph = build_dijkstra_graph(4, 4, blocked_nodes)
        path = compute_dijkstra_path(position, destination, graph)

        if len(path) == 0:
            print("  No path to", destination, "! Skipping.")
            return position, heading, step_count, reroute_count

        rerouted = False
        for i in range(1, len(path)):
            next_pos = path[i]
            direction = get_needed_direction(position, next_pos)
            heading = turn_to_direction(heading, direction)

            distance = rangefinder.distance()
            if distance < threshold:
                blocked_nodes.append(next_pos)
                print("  OBSTACLE at", next_pos, "! Rerouting...")
                reroute_count = reroute_count + 1
                rerouted = True
                break
            else:
                drive_one_step()
                position = next_pos
                step_count = step_count + 1

        if not rerouted:
            arrived = True

    return position, heading, step_count, reroute_count


# ===== Main Program =====

board = Board.get_default_board()
rangefinder = Rangefinder.get_default_rangefinder()
THRESHOLD = 15

blocked_nodes = load_obstacles()

position = (0, 0)
heading = "N"

destinations = [(1, 3), (3, 3), (3, 0), (0, 0)]

board.wait_for_button()
print("=== CAPSTONE PROJECT ===")
print("Known obstacles:", blocked_nodes)
print()

total_steps = 0
total_reroutes = 0

for i in range(len(destinations)):
    dest = destinations[i]
    print("--- Leg", i + 1, ": Heading to", dest, "---")

    position, heading, steps, reroutes = navigate_with_detection(
        position, heading, dest, blocked_nodes, rangefinder, THRESHOLD
    )

    total_steps = total_steps + steps
    total_reroutes = total_reroutes + reroutes
    print("  Arrived at", dest)
    print()

save_obstacles(blocked_nodes)

print("=== FINAL REPORT ===")
print("Destinations visited:", len(destinations))
print("Total steps:", total_steps)
print("Total reroutes:", total_reroutes)
print("Obstacles discovered:", blocked_nodes)
print()
print("Run again to see improvement!")
