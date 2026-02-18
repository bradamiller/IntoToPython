# Lesson 1: The Grid as a Graph - SOLUTION
# Understanding how our grid can be represented as a graph
#
# Key idea: A GRAPH is a collection of NODES connected by EDGES.
# Our 4x4 grid is a graph where:
#   - Each cell is a NODE (16 total)
#   - Each cell connects to its neighbors (up, down, left, right)
#   - These connections are EDGES


# ===== PART 1: Nodes on the Grid =====
print("===== All Nodes on a 4x4 Grid =====")
for row in range(4):
    for col in range(4):
        print((row, col))
print()


# ===== PART 2: What Are Neighbors? =====
print("===== Neighbors =====")
print("Neighbors of (0, 0):", [(0, 1), (1, 0)])
print("Neighbors of (1, 1):", [(0, 1), (2, 1), (1, 0), (1, 2)])
print("Neighbors of (3, 3):", [(2, 3), (3, 2)])
print()


# ===== PART 3: Counting Neighbors =====
print("===== Neighbor Counts =====")
print("(0, 0) has 2 neighbors")   # corner
print("(0, 2) has 3 neighbors")   # edge
print("(2, 2) has 4 neighbors")   # interior
print()


# ===== PART 4: What Happens with Blocked Cells? =====
print("===== Blocked Cell: (1, 1) =====")
print("Neighbors of (1, 0) with (1,1) blocked:", [(0, 0), (2, 0)])
print("Neighbors of (0, 1) with (1,1) blocked:", [(0, 0), (0, 2)])
print()


# ===== PART 5: Why Graphs Matter =====
print("===== Why Graphs Matter =====")
print("Manhattan distance goes in straight lines and cannot avoid obstacles.")
print("Dijkstra's algorithm uses a graph to find paths around obstacles.")
print("A graph tells us which cells connect to which other cells.")
