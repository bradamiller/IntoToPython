# Lesson 4: The Dijkstra Functions
# Organizing our pathfinding code into two functions.
#
# Team: ________________________
# Date: ________________________
#
# build_dijkstra_graph(rows, cols, blocked) builds the graph dictionary.
# compute_dijkstra_path(position, destination, graph) finds the shortest path.


def build_dijkstra_graph(rows, cols, blocked):
    """
    Build a graph dictionary for a rows x cols grid.
    Blocked nodes are excluded. Each node maps to its list of neighbors.

    Parameters:
        rows: number of rows in the grid
        cols: number of columns in the grid
        blocked: list of (row, col) tuples -- blocked cells

    Returns:
        dictionary mapping (row, col) to list of neighbor tuples
    """
    graph = {}

    # TODO: Loop through every cell in the grid
    # for r in range(???):
    #     for c in range(???):

            # TODO: Skip blocked cells
            # if (r, c) in ???:
            #     continue

            # TODO: Find all valid neighbors (up, down, left, right)
            # neighbors = []
            # for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            #     nr, nc = ???, ???
            #     # Check if neighbor is in bounds AND not blocked
            #     if ??? and ???:
            #         neighbors.append((nr, nc))

            # TODO: Add this node and its neighbors to the graph
            # graph[???] = ???

    return graph


def compute_dijkstra_path(position, destination, graph):
    """
    Compute the shortest path from position to destination.
    (Placeholder -- we will implement this in Lesson 5)

    Parameters:
        position: tuple (row, col) -- where the robot is now
        destination: tuple (row, col) -- where we want to go
        graph: dictionary mapping (row, col) to list of neighbor tuples

    Returns:
        list of (row, col) tuples representing the path
    """
    print("compute_dijkstra_path is not implemented yet!")
    return []


# ===== PART 1: Build a Graph =====
# TODO: Build a graph for a 4x4 grid with no blocked cells
# graph = build_dijkstra_graph(???, ???, ???)
# print("Number of nodes in graph:", len(graph))


# ===== PART 2: Examine the Graph =====
# TODO: Print all nodes and their neighbors
# print("\n===== Graph =====")
# for node in graph:
#     print(node, "->", graph[node])


# ===== PART 3: Test with Blocked Cells =====
# TODO: Build a graph with (1, 1) blocked
# graph2 = build_dijkstra_graph(4, 4, [(1, 1)])
# print("\n===== Graph with (1,1) blocked =====")
# print("Number of nodes:", len(graph2))
# print("(1,1) in graph?", (1, 1) in graph2)
# print("Neighbors of (0,1):", graph2[(0, 1)])


# ===== PART 4: Test compute_dijkstra_path (placeholder) =====
# TODO: Try calling compute_dijkstra_path -- it should print the placeholder message
# graph = build_dijkstra_graph(4, 4, [])
# path = compute_dijkstra_path((0, 0), (3, 3), graph)
# print("Path:", path)
