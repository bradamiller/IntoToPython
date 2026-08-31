# Lesson 4: The Dijkstra Functions - SOLUTION
# Organizing our pathfinding code into two functions.


def build_dijkstra_graph(rows, cols, blocked):
    """
    Build a graph dictionary for a rows x cols grid.
    Blocked nodes are excluded. Each node maps to its list of neighbors.
    """
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
    Compute the shortest path from position to destination.
    (Placeholder -- we will implement this in Lesson 5)
    """
    print("compute_dijkstra_path is not implemented yet!")
    return []


# ===== PART 1: Build a Graph =====
graph = build_dijkstra_graph(4, 4, [])
print("Number of nodes in graph:", len(graph))


# ===== PART 2: Examine the Graph =====
print("\n===== Graph =====")
for node in graph:
    print(node, "->", graph[node])


# ===== PART 3: Test with Blocked Cells =====
graph2 = build_dijkstra_graph(4, 4, [(1, 1)])
print("\n===== Graph with (1,1) blocked =====")
print("Number of nodes:", len(graph2))
print("(1,1) in graph?", (1, 1) in graph2)
print("Neighbors of (0,1):", graph2[(0, 1)])


# ===== PART 4: Test compute_dijkstra_path (placeholder) =====
path = compute_dijkstra_path((0, 0), (3, 3), graph)
print("Path:", path)
