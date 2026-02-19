# Lesson 8: Building Experience — Updating Obstacles Over Time
# The robot remembers obstacles across runs and improves over time.
#
# Team: ________________________
# Date: ________________________
#
# Run 1: Robot discovers obstacles the hard way
# Run 2: Robot starts with prior knowledge and performs better

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


# ===== File I/O for Obstacle Persistence =====

def save_obstacles(blocked, filename="obstacles.txt"):
    """Save the blocked list to a file."""
    # TODO: Open the file for writing
    # TODO: Write each blocked node as "row,col" on its own line
    # TODO: Close the file
    # f = open(filename, "w")
    # for node in blocked:
    #     f.write(str(node[0]) + "," + str(node[1]) + "\n")
    # f.close()
    # print("Saved", len(blocked), "obstacles to", filename)
    pass


def load_obstacles(filename="obstacles.txt"):
    """Load the blocked list from a file. Returns empty list if file doesn't exist."""
    blocked = []
    # TODO: Try to open and read the file
    # TODO: For each line, parse "row,col" into a tuple
    # TODO: Handle the case where the file doesn't exist
    # try:
    #     f = open(filename, "r")
    #     for line in f:
    #         parts = line.strip().split(",")
    #         blocked.append((int(parts[0]), int(parts[1])))
    #     f.close()
    #     print("Loaded", len(blocked), "obstacles from", filename)
    # except:
    #     print("No obstacle file found. Starting fresh.")
    return blocked


# ===== Navigation Function (from Lesson 7) =====

def navigate_with_detection(nav, destination, blocked_nodes, rangefinder, threshold):
    """Navigate to destination, detecting obstacles along the way."""
    step_count = 0
    reroute_count = 0

    arrived = False
    while not arrived:
        pathfinder = Dijkstra(nav.position, blocked_nodes)
        path = pathfinder.compute_path(destination)

        if len(path) == 0:
            print("No path to", destination, "!")
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

# TODO: Load obstacles from file (will be empty on first run)
# blocked_nodes = load_obstacles()
blocked_nodes = []

nav = Navigator((0, 0), "N")
destination = (3, 3)

board.wait_for_button()

# TODO: Navigate to destination
# print("=== Starting Navigation ===")
# print("Known obstacles:", blocked_nodes)
# steps, reroutes = navigate_with_detection(
#     nav, destination, blocked_nodes, rangefinder, THRESHOLD
# )

# TODO: Save obstacles for next run
# save_obstacles(blocked_nodes)

# TODO: Print results
# print("\n=== Run Results ===")
# print("Total steps:", steps)
# print("Reroutes:", reroutes)
# print("All known obstacles:", blocked_nodes)

# TODO: Compare Run 1 vs Run 2
# Think about: How many fewer reroutes on Run 2?
# How many fewer total steps on Run 2?
