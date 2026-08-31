# Lesson 6: Testing and Swapping - SOLUTION
# Compare Manhattan and Dijkstra pathfinders and demonstrate swapping.


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


# ===== The Dispatch Function =====

def compute_path(algorithm, position, destination, blocked):
    """Compute a path using the named algorithm. Always returns a path
    NOT including position, regardless of which algorithm ran."""
    if algorithm == "manhattan":
        return compute_manhattan_path(position, destination)[1:]
    else:
        graph = build_dijkstra_graph(4, 4, blocked)
        path = compute_dijkstra_path(position, destination, graph)
        return path[1:]


# ===== Test Helper =====

def run_comparison(test_name, position, destination, blocked):
    m_path = compute_path("manhattan", position, destination, blocked)
    d_path = compute_path("dijkstra", position, destination, blocked)

    print(test_name)
    print("  Manhattan:", m_path, " Steps:", len(m_path))
    print("  Dijkstra: ", d_path, " Steps:", len(d_path))
    print("  Same length?", len(m_path) == len(d_path))
    print()


# ===== PART 1: Compare with No Obstacles =====
print("========== NO OBSTACLES ==========")
run_comparison("Test 1: (0,0) to (3,3)", (0, 0), (3, 3), [])
run_comparison("Test 2: (0,0) to (0,3)", (0, 0), (0, 3), [])
run_comparison("Test 3: (0,0) to (3,0)", (0, 0), (3, 0), [])
run_comparison("Test 4: (2,1) to (0,3)", (2, 1), (0, 3), [])


# ===== PART 2: Compare with Obstacles =====
print("========== WITH OBSTACLES ==========")
blocked = [(1, 0), (1, 1)]

path = compute_path("dijkstra", (0, 0), (3, 0), blocked)
print("=== With obstacles", blocked, "===")
print("Dijkstra path to (3,0):", path)
print()


# ===== PART 3: The One-Argument Swap =====
print("========== SWAPPING DEMO ==========")


def navigate_to(algorithm, position, destination, blocked):
    path = compute_path(algorithm, position, destination, blocked)
    print("  Path to", destination, ":", path, " Steps:", len(path))
    return destination  # new position after "driving" this path


# Using Manhattan
print("Using Manhattan:")
position = navigate_to("manhattan", (0, 0), (2, 3), [])
position = navigate_to("manhattan", position, (0, 1), [])
print()

# Using Dijkstra — same navigate_to function, only the argument changed!
print("Using Dijkstra (no obstacles):")
position = navigate_to("dijkstra", (0, 0), (2, 3), [])
position = navigate_to("dijkstra", position, (0, 1), [])
print()

# Using Dijkstra with obstacles
print("Using Dijkstra (with obstacles [(1,1)]):")
blocked = [(1, 1)]
position = navigate_to("dijkstra", (0, 0), (2, 3), blocked)
position = navigate_to("dijkstra", position, (0, 1), blocked)
