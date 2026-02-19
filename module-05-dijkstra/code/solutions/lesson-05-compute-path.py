# Lesson 5: Implementing compute_path() - SOLUTION
# Complete Dijkstra's algorithm for shortest path finding.


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
        """Compute shortest path using Dijkstra's algorithm."""
        if destination not in self.graph:
            print("Destination is blocked or not in graph!")
            return []

        # Initialize distances, previous, and to_visit
        distances = {}
        previous = {}
        to_visit = []

        for node in self.graph:
            distances[node] = 999999
            previous[node] = None
            to_visit.append(node)

        distances[self.position] = 0

        # Main loop
        while len(to_visit) > 0:
            # Find node with smallest distance in to_visit
            current = to_visit[0]
            for node in to_visit:
                if distances[node] < distances[current]:
                    current = node

            # If we reached the destination, stop
            if current == destination:
                break

            # Remove current from to_visit
            to_visit.remove(current)

            # Update distances to neighbors
            for neighbor in self.graph[current]:
                if neighbor in to_visit:
                    new_dist = distances[current] + 1
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        previous[neighbor] = current

        # Reconstruct path
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


# ===== Test Cases =====

print("=== Test 1: No obstacles ===")
d = Dijkstra((0, 0), [])
path = d.compute_path((3, 3))
print("Path:", path)
print("Steps:", len(path) - 1)
print()

print("=== Test 2: With obstacles ===")
d2 = Dijkstra((0, 0), [(1, 0), (1, 1)])
path2 = d2.compute_path((3, 0))
print("Path:", path2)
print("Steps:", len(path2) - 1)
print()

print("=== Test 3: Same position ===")
d3 = Dijkstra((1, 1), [])
path3 = d3.compute_path((1, 1))
print("Path:", path3)
print()

print("=== Test 4: Adjacent ===")
d4 = Dijkstra((0, 0), [])
path4 = d4.compute_path((0, 1))
print("Path:", path4)
print()

print("=== Test 5: Heavily blocked ===")
d5 = Dijkstra((0, 0), [(0, 1), (1, 0)])
path5 = d5.compute_path((0, 2))
print("Path:", path5)
print("Steps:", len(path5) - 1)
