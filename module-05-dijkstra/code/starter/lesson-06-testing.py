# Lesson 6: Testing and Swapping
# Compare Manhattan and Dijkstra pathfinders.
#
# Team: ________________________
# Date: ________________________
#
# compute_manhattan_path(position, destination) and
# compute_dijkstra_path(position, destination, graph) don't quite match --
# Dijkstra needs a graph, and its path includes the start position.
# The compute_path() dispatch function below hides those differences.


# ===== Manhattan (from Module 4) =====

def compute_manhattan_path(position, destination):
    path = [position]
    current_row = position[0]
    current_col = position[1]
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


# ===== Dijkstra (from Lesson 5) =====

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


# ===== The Dispatch Function (YOU COMPLETE THIS) =====
# TODO: Write compute_path(algorithm, position, destination, blocked)
# - If algorithm == "manhattan": return compute_manhattan_path(position, destination)
# - Otherwise: build a 4x4 graph, call compute_dijkstra_path,
#              and return path[1:] to drop the start position
#              (so both branches return the SAME shape of result)

# def compute_path(algorithm, position, destination, blocked):
#     if algorithm == "manhattan":
#         return ???
#     else:
#         graph = ???
#         path = ???
#         return path[???]


# ===== Test Helper =====

def run_comparison(test_name, position, destination, blocked):
    """Compare Manhattan and Dijkstra for the same position/destination."""
    m_path = compute_path("manhattan", position, destination, blocked)
    d_path = compute_path("dijkstra", position, destination, blocked)

    print(test_name)
    print("  Manhattan:", m_path, " Steps:", len(m_path))
    print("  Dijkstra: ", d_path, " Steps:", len(d_path))
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
# path = compute_path("dijkstra", (0, 0), (3, 0), blocked)
# print("=== With obstacles [(1,0), (1,1)] ===")
# print("Dijkstra path to (3,0):", path)
# print()


# ===== PART 3: The One-Argument Swap =====
# Both branches of compute_path() return the same shape of result.
# This means the caller can swap algorithms just by changing the argument!

# TODO: Write a function that uses compute_path() for any algorithm
# def navigate_to(algorithm, position, destination, blocked):
#     path = compute_path(algorithm, position, destination, blocked)
#     print("Path to", destination, ":", path)
#     print("Steps:", len(path))
#     return destination  # new position after "driving" this path

# TODO: Test with Manhattan
# print("=== Using Manhattan ===")
# position = navigate_to("manhattan", (0, 0), (2, 3), [])
# position = navigate_to("manhattan", position, (0, 1), [])

# TODO: Test with Dijkstra — same navigate_to function, different argument!
# print("\n=== Using Dijkstra ===")
# position = navigate_to("dijkstra", (0, 0), (2, 3), [])
# position = navigate_to("dijkstra", position, (0, 1), [])
