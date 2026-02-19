# Lesson 6: Testing and Swapping
# Compare Manhattan and Dijkstra pathfinders.
#
# Team: ________________________
# Date: ________________________
#
# Both Manhattan and Dijkstra have compute_path() that returns a list of tuples.
# This shared interface lets us swap one for the other!


# ===== Manhattan Class (from Module 4) =====

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

        return path


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


# ===== Test Helper =====

def run_comparison(test_name, start, destination, blocked):
    """Compare Manhattan and Dijkstra for the same start/destination."""
    m = Manhattan(start)
    d = Dijkstra(start, blocked)

    m_path = m.compute_path(destination)
    d_path = d.compute_path(destination)

    print(test_name)
    print("  Manhattan:", m_path, " Steps:", len(m_path) - 1)
    print("  Dijkstra: ", d_path, " Steps:", len(d_path) - 1)
    print("  Same length?", len(m_path) == len(d_path))
    print()


# ===== PART 1: Compare with No Obstacles =====
# When there are no obstacles, both should find paths of the same length.

# TODO: Run comparisons for these destinations with no blocked nodes:
# run_comparison("Test 1: (0,0) to (3,3)", (0,0), (3,3), [])
# run_comparison("Test 2: (0,0) to (0,3)", (0,0), (0,3), [])
# run_comparison("Test 3: (0,0) to (3,0)", (0,0), (3,0), [])
# run_comparison("Test 4: (2,1) to (0,3)", (2,1), (0,3), [])


# ===== PART 2: Compare with Obstacles =====
# With obstacles, Manhattan may try to go through blocked nodes.
# Dijkstra routes around them.

# TODO: Test with blocked nodes
# blocked = [(1, 0), (1, 1)]
# d = Dijkstra((0, 0), blocked)
# path = d.compute_path((3, 0))
# print("=== With obstacles [(1,0), (1,1)] ===")
# print("Dijkstra path to (3,0):", path)
# print()


# ===== PART 3: The Swap =====
# Both pathfinders have compute_path() returning a list of tuples.
# This means we can swap one for the other!

# TODO: Write a function that takes ANY pathfinder and uses it
# def navigate_to(pathfinder, destination):
#     path = pathfinder.compute_path(destination)
#     print("Path to", destination, ":", path)
#     print("Steps:", len(path) - 1)
#     # Update pathfinder position
#     pathfinder.position = destination

# TODO: Test with Manhattan
# print("=== Using Manhattan ===")
# pathfinder = Manhattan((0, 0))
# navigate_to(pathfinder, (2, 3))
# navigate_to(pathfinder, (0, 1))

# TODO: Test with Dijkstra — same function, different pathfinder!
# print("\n=== Using Dijkstra ===")
# pathfinder = Dijkstra((0, 0), [])
# navigate_to(pathfinder, (2, 3))
# navigate_to(pathfinder, (0, 1))
