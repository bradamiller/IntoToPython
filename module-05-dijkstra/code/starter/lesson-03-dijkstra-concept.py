# Lesson 3: Dijkstra's Algorithm — The Concept
# Understanding how Dijkstra finds shortest paths by tracing it by hand.
#
# Team: ________________________
# Date: ________________________
#
# Dijkstra's algorithm finds the shortest path in a graph by:
#   1. Starting at the source node (distance = 0)
#   2. Visiting the closest unvisited node
#   3. Updating distances to its neighbors
#   4. Repeating until the destination is reached
#   5. Tracing back through "previous" pointers to get the path


# ===== HELPER: Build a Graph =====
# This function builds a graph dictionary for a grid.
# Each node maps to a list of its neighbors.
# Blocked nodes are excluded.

def build_graph(rows, cols, blocked):
    """Build a graph dictionary for a rows x cols grid, excluding blocked nodes."""
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


# ===== PART 1: Explore the Graph =====
# Build a 3x3 graph with no obstacles and print it.

# TODO: Call build_graph for a 3x3 grid with no blocked nodes
# graph = build_graph(???, ???, ???)

# TODO: Print each node and its neighbors
# for node in graph:
#     print(node, "->", graph[node])


# ===== PART 2: Graph with Blocked Node =====
# Build a 3x3 graph with (1, 1) blocked.

# TODO: Call build_graph with (1, 1) blocked
# blocked = ???
# graph = build_graph(???, ???, blocked)

# TODO: Print each node and its neighbors
# print("\n===== Graph with (1,1) blocked =====")
# for node in graph:
#     print(node, "->", graph[node])


# ===== PART 3: Trace Dijkstra by Hand =====
# We will trace through Dijkstra's algorithm using print statements.
# Start: (0, 0), Destination: (2, 2), Blocked: [(1, 1)]

# TODO: Set up the data structures
# graph = build_graph(3, 3, [(1, 1)])
# start = (0, 0)
# destination = (2, 2)
#
# # Initialize distances (all nodes start at infinity except start)
# distances = {}
# previous = {}
# to_visit = []
#
# for node in graph:
#     distances[node] = 999999
#     previous[node] = None
#     to_visit.append(node)
#
# distances[start] = 0
#
# print("Initial distances:")
# for node in distances:
#     print("  ", node, "=", distances[node])


# ===== PART 4: Run the Algorithm Step by Step =====
# TODO: Implement the main loop with print statements to trace each step.
#
# step = 0
# while len(to_visit) > 0:
#     # Find the node in to_visit with the smallest distance
#     current = to_visit[0]
#     for node in to_visit:
#         if distances[node] < distances[current]:
#             current = node
#
#     step = step + 1
#     print("\n--- Step", step, "---")
#     print("Visiting:", current, "(distance =", distances[current], ")")
#
#     # Check if we reached the destination
#     if current == destination:
#         print("Reached destination!")
#         break
#
#     # Remove current from to_visit
#     to_visit.remove(current)
#
#     # Update neighbors
#     for neighbor in graph[current]:
#         if neighbor in to_visit:
#             new_dist = distances[current] + 1
#             if new_dist < distances[neighbor]:
#                 print("  Updated", neighbor, ":", distances[neighbor], "->", new_dist)
#                 distances[neighbor] = new_dist
#                 previous[neighbor] = current


# ===== PART 5: Reconstruct the Path =====
# TODO: Trace back from destination to start using the previous dictionary.
#
# print("\n===== Path Reconstruction =====")
# path = []
# current = destination
# while current is not None:
#     path.append(current)
#     print("  At", current, ", previous =", previous[current])
#     current = previous[current]
#
# path.reverse()
# print("\nShortest path:", path)
# print("Path length:", len(path) - 1, "steps")
