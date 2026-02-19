# Lesson 9: Module 5 Capstone Project
# Full autonomous navigation with obstacle detection and learning.
#
# Team: ________________________
# Date: ________________________
#
# Your robot will:
#   1. Load known obstacles from a file
#   2. Visit 4+ destinations using Dijkstra pathfinding
#   3. Detect new obstacles with the rangefinder
#   4. Reroute around obstacles
#   5. Save all obstacles for the next run
#   6. Demonstrate improvement on Run 2

from XRPLib.rangefinder import Rangefinder
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board


# ===== Dijkstra Class =====

class Dijkstra:

    def __init__(self, start, blocked):
        self.position = start
        self.blocked = blocked
        self.graph = self.build_graph(4, 4)

    def build_graph(self, rows, cols):
        graph = {}
        for r in range(rows):
            for c in range(cols):
                if (r, c) in self.blocked:
                    continue
                neighbors = []
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in self.blocked:
                        neighbors.append((nr, nc))
                graph[(r, c)] = neighbors
        return graph

    def compute_path(self, destination):
        if destination not in self.graph:
            return []
        distances = {}
        previous = {}
        to_visit = []
        for node in self.graph:
            distances[node] = 999999
            previous[node] = None
            to_visit.append(node)
        distances[self.position] = 0
        while len(to_visit) > 0:
            current = to_visit[0]
            for node in to_visit:
                if distances[node] < distances[current]:
                    current = node
            if current == destination:
                break
            to_visit.remove(current)
            for neighbor in self.graph[current]:
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
        if len(path) == 0 or path[0] != self.position:
            return []
        return path


# ===== Navigator Class =====

class Navigator:

    def __init__(self, start, heading):
        self.position = start
        self.heading = heading
        self.drivetrain = DifferentialDrive.get_default_differential_drive()

    def get_needed_direction(self, next_pos):
        row_diff = next_pos[0] - self.position[0]
        col_diff = next_pos[1] - self.position[1]
        if row_diff == 1:
            return "S"
        elif row_diff == -1:
            return "N"
        elif col_diff == 1:
            return "E"
        elif col_diff == -1:
            return "W"

    def turn_to(self, direction):
        right_turns = {"N": "E", "E": "S", "S": "W", "W": "N"}
        left_turns = {"N": "W", "W": "S", "S": "E", "E": "N"}
        if self.heading == direction:
            pass
        elif right_turns[self.heading] == direction:
            self.drivetrain.turn(90)
            self.heading = direction
        elif left_turns[self.heading] == direction:
            self.drivetrain.turn(-90)
            self.heading = direction
        else:
            self.drivetrain.turn(180)
            self.heading = direction

    def drive_one_step(self):
        self.drivetrain.straight(20)


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

def navigate_with_detection(nav, destination, blocked_nodes, rangefinder, threshold):
    """Navigate to destination, detecting obstacles along the way."""
    step_count = 0
    reroute_count = 0

    arrived = False
    while not arrived:
        pathfinder = Dijkstra(nav.position, blocked_nodes)
        path = pathfinder.compute_path(destination)

        if len(path) == 0:
            print("  No path to", destination, "! Skipping.")
            return step_count, reroute_count

        rerouted = False
        for i in range(1, len(path)):
            next_pos = path[i]
            direction = nav.get_needed_direction(next_pos)
            nav.turn_to(direction)

            distance = rangefinder.distance()
            if distance < threshold:
                blocked_nodes.append(next_pos)
                print("  OBSTACLE at", next_pos, "! Rerouting...")
                reroute_count = reroute_count + 1
                rerouted = True
                break
            else:
                nav.drive_one_step()
                nav.position = next_pos
                step_count = step_count + 1

        if not rerouted:
            arrived = True

    return step_count, reroute_count


# ===== Main Program =====

board = Board.get_default_board()
rangefinder = Rangefinder.get_default_rangefinder()
THRESHOLD = 15

# TODO: Load obstacles from previous runs
# blocked_nodes = load_obstacles()
blocked_nodes = []

# TODO: Create Navigator at starting position
# nav = Navigator((0, 0), "N")

# TODO: Define your list of 4+ destinations
# destinations = [(1, 3), (3, 3), (3, 0), (0, 0)]

board.wait_for_button()
print("=== CAPSTONE PROJECT ===")
print("Known obstacles:", blocked_nodes)
print()

# TODO: Main navigation loop
# Visit each destination in order
# total_steps = 0
# total_reroutes = 0
#
# for i in range(len(destinations)):
#     dest = destinations[i]
#     print("--- Leg", i + 1, ": Heading to", dest, "---")
#
#     steps, reroutes = navigate_with_detection(
#         nav, dest, blocked_nodes, rangefinder, THRESHOLD
#     )
#
#     total_steps = total_steps + steps
#     total_reroutes = total_reroutes + reroutes
#     print("  Arrived at", dest)
#     print()

# TODO: Save obstacles for next run
# save_obstacles(blocked_nodes)

# TODO: Print final report
# print("=== FINAL REPORT ===")
# print("Destinations visited:", len(destinations))
# print("Total steps:", total_steps)
# print("Total reroutes:", total_reroutes)
# print("Obstacles discovered:", blocked_nodes)
# print()
# print("Run again to see improvement!")
