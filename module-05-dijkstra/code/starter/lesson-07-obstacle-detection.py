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


# ===== Dijkstra Class (from Lesson 5) =====

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


# ===== Navigator Class (from Module 4) =====

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


# ===== Setup =====

board = Board.get_default_board()
rangefinder = Rangefinder.get_default_rangefinder()

THRESHOLD = 15  # cm — closer than this means blocked

blocked_nodes = []
start = (0, 0)
destination = (3, 3)
heading = "N"

nav = Navigator(start, heading)

board.wait_for_button()
print("Starting obstacle detection demo!")


# ===== Navigate with Obstacle Detection =====

# TODO: Create a Dijkstra pathfinder with the current blocked list
# pathfinder = Dijkstra(start, blocked_nodes)

# TODO: Compute initial path
# path = pathfinder.compute_path(destination)
# print("Initial path:", path)

# TODO: Walk through the path one step at a time
# For each step:
#   1. Turn to face the next intersection
#   2. Check the rangefinder
#   3. If distance < THRESHOLD:
#      - Add the blocked intersection to blocked_nodes
#      - Recompute the path from current position
#      - Print a message about the obstacle
#   4. If no obstacle:
#      - Drive forward one step
#      - Update position

# for i in range(1, len(path)):
#     next_pos = path[i]
#
#     # Turn to face the next intersection
#     direction = nav.get_needed_direction(next_pos)
#     nav.turn_to(direction)
#
#     # Check rangefinder
#     distance = rangefinder.distance()
#     print("At", nav.position, "checking ahead:", distance, "cm")
#
#     if distance < THRESHOLD:
#         # TODO: Obstacle detected!
#         # Add next_pos to blocked_nodes
#         # blocked_nodes.append(???)
#         # print("Obstacle at", next_pos, "! Rerouting...")
#
#         # TODO: Recompute path from current position
#         # pathfinder = Dijkstra(nav.position, blocked_nodes)
#         # path = pathfinder.compute_path(destination)
#         # print("New path:", path)
#         # break  # Restart the path-following loop
#         pass
#     else:
#         # TODO: No obstacle — drive forward
#         # nav.drive_one_step()
#         # nav.position = next_pos
#         # print("Drove to", nav.position)
#         pass

print("Navigation complete!")
print("Final position:", nav.position)
print("Obstacles found:", blocked_nodes)
