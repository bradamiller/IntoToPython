# Lesson 5: Implementing compute_dijkstra_path() - SOLUTION
# Complete the Dijkstra algorithm to find shortest paths.


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
    """
    Compute the shortest path from position to destination
    using Dijkstra's algorithm.

    Returns a list of (row, col) tuples representing the path.
    """
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


# ===== Test Cases =====

print("=== Test 1: No obstacles ===")
graph = build_dijkstra_graph(4, 4, [])
path = compute_dijkstra_path((0, 0), (3, 3), graph)
print("Path:", path)
print("Steps:", len(path) - 1)
print()

print("=== Test 2: With obstacles ===")
graph2 = build_dijkstra_graph(4, 4, [(1, 0), (1, 1)])
path2 = compute_dijkstra_path((0, 0), (3, 0), graph2)
print("Path:", path2)
print("Steps:", len(path2) - 1)
print()

print("=== Test 3: Same position ===")
graph3 = build_dijkstra_graph(4, 4, [])
path3 = compute_dijkstra_path((1, 1), (1, 1), graph3)
print("Path:", path3)
print()

print("=== Test 4: Adjacent ===")
graph4 = build_dijkstra_graph(4, 4, [])
path4 = compute_dijkstra_path((0, 0), (0, 1), graph4)
print("Path:", path4)
