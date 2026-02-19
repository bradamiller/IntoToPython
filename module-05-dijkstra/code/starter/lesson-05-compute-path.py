# Lesson 5: Implementing compute_path()
# Complete the Dijkstra algorithm to find shortest paths.
#
# Team: ________________________
# Date: ________________________
#
# The compute_path method uses Dijkstra's algorithm:
#   1. Set all distances to infinity except start (distance 0)
#   2. Repeatedly pick the closest unvisited node
#   3. Update distances to its neighbors
#   4. Reconstruct the path using the "previous" dictionary


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
        """
        Compute the shortest path from self.position to destination
        using Dijkstra's algorithm.

        Returns a list of (row, col) tuples representing the path.
        """
        # Step 1: Check if destination is reachable
        if destination not in self.graph:
            print("Destination is blocked or not in graph!")
            return []

        # Step 2: Create a distances dictionary
        # Every node starts at 999999 (infinity), except the start which is 0
        distances = {}
        previous = {}
        to_visit = []

        for node in self.graph:
            # TODO: Set distance for this node to 999999
            # distances[node] = ???
            # TODO: Set previous for this node to None
            # previous[node] = ???
            # TODO: Add this node to the to_visit list
            # to_visit.append(???)
            pass

        # TODO: Set the start node's distance to 0
        # distances[self.position] = ???

        # Step 3: Main loop — process nodes until we reach destination
        while len(to_visit) > 0:
            # TODO: Find the node in to_visit with the smallest distance
            # current = to_visit[0]
            # for node in to_visit:
            #     if distances[node] < distances[current]:
            #         current = ???
            pass

            # TODO: If we reached the destination, stop
            # if current == ???:
            #     break

            # TODO: Remove current from to_visit
            # to_visit.remove(???)

            # TODO: Check each neighbor of current
            # for neighbor in self.graph[current]:
            #     if neighbor in to_visit:
            #         # Calculate new distance through current
            #         new_dist = distances[current] + 1
            #         # If this is shorter than the known distance, update
            #         if new_dist < distances[neighbor]:
            #             distances[neighbor] = ???
            #             previous[neighbor] = ???

        # Step 4: Reconstruct the path by following "previous" links
        # Start at the destination and work backward to the start
        path = []
        # TODO: Start at the destination
        # current = destination
        # TODO: Follow previous links back to the start
        # while current is not None:
        #     path.append(current)
        #     current = previous[current]
        # TODO: Reverse the path (we built it backward)
        # path.reverse()

        # Check that we actually found a path
        if len(path) == 0 or path[0] != self.position:
            print("No path found!")
            return []

        return path


# ===== Test Cases =====

# Test 1: No obstacles — basic path
# print("=== Test 1: No obstacles ===")
# d = Dijkstra((0, 0), [])
# path = d.compute_path((3, 3))
# print("Path:", path)
# print("Steps:", len(path) - 1)
# print()

# Test 2: With obstacles — must route around
# print("=== Test 2: With obstacles ===")
# d2 = Dijkstra((0, 0), [(1, 0), (1, 1)])
# path2 = d2.compute_path((3, 0))
# print("Path:", path2)
# print("Steps:", len(path2) - 1)
# print()

# Test 3: Same position — trivial path
# print("=== Test 3: Same position ===")
# d3 = Dijkstra((1, 1), [])
# path3 = d3.compute_path((1, 1))
# print("Path:", path3)
# print()

# Test 4: Adjacent cells
# print("=== Test 4: Adjacent ===")
# d4 = Dijkstra((0, 0), [])
# path4 = d4.compute_path((0, 1))
# print("Path:", path4)
