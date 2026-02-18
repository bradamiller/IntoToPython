# Lesson 1: The Grid as a Graph
# Understanding how our grid can be represented as a graph
#
# Team: ________________________
# Date: ________________________
#
# Key idea: A GRAPH is a collection of NODES connected by EDGES.
# Our 4x4 grid is a graph where:
#   - Each cell is a NODE (16 total)
#   - Each cell connects to its neighbors (up, down, left, right)
#   - These connections are EDGES
#
#   Col: 0   1   2   3
#  Row 0: +---+---+---+---+
#         | * - * - * - * |
#  Row 1: + | + | + | + | +
#         | * - * - * - * |
#  Row 2: + | + | + | + | +
#         | * - * - * - * |
#  Row 3: + | + | + | + | +
#         | * - * - * - * |
#         +---+---+---+---+
#
# The * are nodes, the - and | are edges connecting them.


# ===== PART 1: Nodes on the Grid =====
# Every cell on the grid is a node. We describe nodes as (row, col).

# TODO: Print all 16 node positions on a 4x4 grid
# Hint: Use two nested for loops, one for rows and one for columns
# for row in range(???):
#     for col in range(???):
#         print((row, col))


# ===== PART 2: What Are Neighbors? =====
# Two nodes are NEIGHBORS if they are directly next to each other
# (up, down, left, or right -- no diagonals!).

# TODO: List the neighbors of (0, 0) by hand and print them
# print("Neighbors of (0, 0):", ???)
# Hint: (0, 0) is in the top-left corner. It can only go right or down.

# TODO: List the neighbors of (1, 1) by hand and print them
# print("Neighbors of (1, 1):", ???)
# Hint: (1, 1) is in the middle area. It can go up, down, left, right.

# TODO: List the neighbors of (3, 3) by hand and print them
# print("Neighbors of (3, 3):", ???)
# Hint: (3, 3) is in the bottom-right corner.


# ===== PART 3: Counting Neighbors =====
# Corner nodes have 2 neighbors
# Edge nodes (on the border, not corner) have 3 neighbors
# Interior nodes have 4 neighbors

# TODO: How many neighbors does each of these have?
# print("(0, 0) has ??? neighbors")  # corner
# print("(0, 2) has ??? neighbors")  # edge
# print("(2, 2) has ??? neighbors")  # interior


# ===== PART 4: What Happens with Blocked Cells? =====
# If a cell is BLOCKED (obstacle), it is removed from the graph.
# Its neighbors also lose it as a neighbor.

# Example: If (1, 1) is blocked:
# TODO: List the neighbors of (1, 0) if (1, 1) is blocked
# print("Neighbors of (1, 0) with (1,1) blocked:", ???)
# Hint: normally (1, 0) connects to (0, 0), (2, 0), (1, 1)
#       but (1, 1) is blocked, so remove it from the list.

# TODO: List the neighbors of (0, 1) if (1, 1) is blocked
# print("Neighbors of (0, 1) with (1,1) blocked:", ???)


# ===== PART 5: Why Graphs Matter =====
# TODO: Fill in the blanks and uncomment:
# print("Manhattan distance goes in straight lines and cannot avoid ___.")
# print("Dijkstra's algorithm uses a ___ to find paths around obstacles.")
# print("A graph tells us which cells ___ to which other cells.")
