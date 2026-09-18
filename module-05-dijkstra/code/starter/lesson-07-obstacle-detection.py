# Lesson 7: Obstacle Detection with the Rangefinder
# Use the ultrasonic sensor to detect blocked intersections.
#
# Team: ________________________
# Date: ________________________
#
# The rangefinder measures distance in cm.
# If the distance is less than a threshold, the intersection ahead is blocked.

from XRPLib.rangefinder import Rangefinder
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board


# ===== Dijkstra Functions (from Lesson 5) =====

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
        print("Destination is blocked or not in graph!")
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
        print("No path found!")
        return []
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

THRESHOLD = 15  # cm — closer than this means blocked

blocked_nodes = []
position = (0, 0)
heading = "N"
destination = (3, 3)

board.wait_for_button()
print("Starting obstacle detection demo!")


# ===== Navigate with Obstacle Detection =====

# TODO: Build a graph with the current blocked list
# graph = build_dijkstra_graph(4, 4, blocked_nodes)

# TODO: Compute initial path
# path = compute_dijkstra_path(position, destination, graph)
# print("Initial path:", path)

# TODO: Walk through the path one step at a time
# For each step:
#   1. Turn to face the next intersection (heading = turn_to_direction(heading, direction))
#   2. Check the rangefinder
#   3. If distance < THRESHOLD:
#      - Add the blocked intersection to blocked_nodes
#      - Rebuild the graph and recompute the path from current position
#      - Print a message about the obstacle
#   4. If no obstacle:
#      - Drive forward one step
#      - Update position

# for i in range(1, len(path)):
#     next_pos = path[i]
#
#     # Turn to face the next intersection
#     direction = get_needed_direction(position, next_pos)
#     heading = turn_to_direction(heading, direction)
#
#     # Check rangefinder
#     distance = rangefinder.distance()
#     print("At", position, "checking ahead:", distance, "cm")
#
#     if distance < THRESHOLD:
#         # TODO: Obstacle detected!
#         # Add next_pos to blocked_nodes
#         # blocked_nodes.append(???)
#         # print("Obstacle at", next_pos, "! Rerouting...")
#
#         # TODO: Rebuild the graph and recompute the path from current position
#         # graph = build_dijkstra_graph(4, 4, blocked_nodes)
#         # path = compute_dijkstra_path(position, destination, graph)
#         # print("New path:", path)
#         # break  # Restart the path-following loop
#         pass
#     else:
#         # TODO: No obstacle — drive forward
#         # drive_one_step()
#         # position = next_pos
#         # print("Drove to", position)
#         pass

print("Navigation complete!")
print("Final position:", position)
print("Obstacles found:", blocked_nodes)
