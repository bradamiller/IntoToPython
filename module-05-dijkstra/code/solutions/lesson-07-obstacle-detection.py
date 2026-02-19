# Lesson 7: Obstacle Detection with the Rangefinder - SOLUTION
# Navigate to a destination while detecting and avoiding obstacles.

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
            print("Destination is blocked or not in graph!")
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
            print("No path found!")
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


# ===== Navigate with Obstacle Detection =====

def navigate_with_detection(nav, destination, blocked_nodes, rangefinder, threshold):
    """Navigate to destination, detecting obstacles along the way."""
    step_count = 0
    reroute_count = 0

    arrived = False
    while not arrived:
        pathfinder = Dijkstra(nav.position, blocked_nodes)
        path = pathfinder.compute_path(destination)

        if len(path) == 0:
            print("No path to", destination, "! Skipping.")
            return step_count, reroute_count

        print("Path:", path)
        rerouted = False

        for i in range(1, len(path)):
            next_pos = path[i]

            # Turn to face the next intersection
            direction = nav.get_needed_direction(next_pos)
            nav.turn_to(direction)

            # Check rangefinder
            distance = rangefinder.distance()
            print("  At", nav.position, "checking ahead:", distance, "cm")

            if distance < threshold:
                # Obstacle detected!
                blocked_nodes.append(next_pos)
                print("  OBSTACLE at", next_pos, "! Rerouting...")
                reroute_count = reroute_count + 1
                rerouted = True
                break
            else:
                # No obstacle — drive forward
                nav.drive_one_step()
                nav.position = next_pos
                step_count = step_count + 1
                print("  Drove to", nav.position)

        if not rerouted:
            arrived = True

    return step_count, reroute_count


# ===== Main Program =====

board = Board.get_default_board()
rangefinder = Rangefinder.get_default_rangefinder()

THRESHOLD = 15  # cm
blocked_nodes = []
nav = Navigator((0, 0), "N")

board.wait_for_button()
print("Starting obstacle detection demo!")
print()

destination = (3, 3)
steps, reroutes = navigate_with_detection(
    nav, destination, blocked_nodes, rangefinder, THRESHOLD
)

print()
print("=== Results ===")
print("Destination:", destination)
print("Final position:", nav.position)
print("Total steps:", steps)
print("Reroutes:", reroutes)
print("Obstacles found:", blocked_nodes)
