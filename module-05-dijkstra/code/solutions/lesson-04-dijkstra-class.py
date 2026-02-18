# Lesson 4: The Dijkstra Class - SOLUTION
# Organizing our pathfinding code into a class.
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
        self.graph = self.build_graph(4, 4)

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
pathfinder = Dijkstra((0, 0), [])
print("Position:", pathfinder.position)
print("Blocked:", pathfinder.blocked)
print("Number of nodes in graph:", len(pathfinder.graph))
print()


# ===== PART 2: Examine the Graph =====
print("===== Graph =====")
for node in pathfinder.graph:
    print(node, "->", pathfinder.graph[node])
print()


# ===== PART 3: Test with Blocked Cells =====
pathfinder2 = Dijkstra((0, 0), [(1, 1)])
print("===== Graph with (1,1) blocked =====")
print("Number of nodes:", len(pathfinder2.graph))
print("(1,1) in graph?", (1, 1) in pathfinder2.graph)
print("Neighbors of (0,1):", pathfinder2.graph[(0, 1)])
print()


# ===== PART 4: Test compute_path (placeholder) =====
path = pathfinder.compute_path((3, 3))
print("Path:", path)
