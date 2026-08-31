# Lesson 6 Optional Extension: True Polymorphism with Classes
# Classes-track reference: instead of a dispatch function with an if/else,
# both classes share an identical compute_path(destination) method signature,
# so the caller never needs to know which one it's using.


class Manhattan:
    def __init__(self, start):
        self.position = start

    def compute_path(self, destination):
        path = [self.position]
        current_row = self.position[0]
        current_col = self.position[1]
        dest_row = destination[0]
        dest_col = destination[1]

        if dest_row > current_row:
            row_step = 1
        else:
            row_step = -1

        if dest_col > current_col:
            col_step = 1
        else:
            col_step = -1

        while current_row != dest_row:
            current_row = current_row + row_step
            path.append((current_row, current_col))

        while current_col != dest_col:
            current_col = current_col + col_step
            path.append((current_row, current_col))

        return path[1:]  # drop the start position, matching Dijkstra below


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

        return path[1:]  # drop the start position, matching Manhattan above


# ===== Test Helper -- works with EITHER class, unmodified =====

def navigate_to(pathfinder, destination):
    path = pathfinder.compute_path(destination)
    print("  Path to", destination, ":", path, " Steps:", len(path))
    pathfinder.position = destination


# Using Manhattan
print("Using Manhattan:")
pathfinder = Manhattan((0, 0))
navigate_to(pathfinder, (2, 3))
navigate_to(pathfinder, (0, 1))
print()

# Using Dijkstra — same navigate_to function, no if/else needed anywhere!
print("Using Dijkstra:")
pathfinder = Dijkstra((0, 0), [(1, 1)])
navigate_to(pathfinder, (2, 3))
navigate_to(pathfinder, (0, 1))
