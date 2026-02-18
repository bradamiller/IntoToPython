# Lesson 4: The Dijkstra Class
# Organizing our pathfinding code into a class.
#
# Team: ________________________
# Date: ________________________
#
# A class groups related data (attributes) and functions (methods) together.
# Our Dijkstra class will have:
#   - Attributes: position, blocked, graph
#   - Methods: __init__, build_graph, compute_path


class Dijkstra:
    def __init__(self, start, blocked):
        """
        Initialize the Dijkstra pathfinder.

        Parameters:
            start: tuple (row, col) — the robot's starting position
            blocked: list of (row, col) tuples — blocked cells
        """
        self.position = start
        self.blocked = blocked
        # TODO: Call build_graph to create the graph for a 4x4 grid
        # self.graph = self.build_graph(???, ???)
        self.graph = {}  # Placeholder — replace with build_graph call

    def build_graph(self, rows, cols):
        """
        Build a graph dictionary for a rows x cols grid.
        Blocked nodes are excluded. Each node maps to its list of neighbors.

        Parameters:
            rows: number of rows in the grid
            cols: number of columns in the grid

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

    def compute_path(self, destination):
        """
        Compute the shortest path from current position to destination.
        (Placeholder — we will implement this in Lesson 5)

        Parameters:
            destination: tuple (row, col) — where we want to go

        Returns:
            list of (row, col) tuples representing the path
        """
        print("compute_path is not implemented yet!")
        return []


# ===== PART 1: Create a Dijkstra Object =====
# TODO: Create a Dijkstra pathfinder starting at (0, 0) with no blocked cells
# pathfinder = Dijkstra(???, ???)
# print("Position:", pathfinder.position)
# print("Blocked:", pathfinder.blocked)
# print("Number of nodes in graph:", len(pathfinder.graph))


# ===== PART 2: Examine the Graph =====
# TODO: Print all nodes and their neighbors
# print("\n===== Graph =====")
# for node in pathfinder.graph:
#     print(node, "->", pathfinder.graph[node])


# ===== PART 3: Test with Blocked Cells =====
# TODO: Create a new pathfinder with (1, 1) blocked
# pathfinder2 = Dijkstra((0, 0), [(1, 1)])
# print("\n===== Graph with (1,1) blocked =====")
# print("Number of nodes:", len(pathfinder2.graph))
# print("(1,1) in graph?", (1, 1) in pathfinder2.graph)
# print("Neighbors of (0,1):", pathfinder2.graph[(0, 1)])


# ===== PART 4: Test compute_path (placeholder) =====
# TODO: Try calling compute_path — it should print the placeholder message
# path = pathfinder.compute_path((3, 3))
# print("Path:", path)
