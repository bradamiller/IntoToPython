# Lesson 2: Dictionaries — Mapping Nodes to Neighbors
# A dictionary maps KEYS to VALUES, perfect for representing a graph.
#
# Team: ________________________
# Date: ________________________
#
# Dictionary syntax:
#   my_dict = {key1: value1, key2: value2}
#   my_dict[key1]   # gets value1
#
# For our graph:
#   graph = {(0,0): [(0,1), (1,0)], ...}
#   graph[(0,0)] gives the list of neighbors of (0,0)


# ===== PART 1: Creating a Dictionary =====
# TODO: Create a dictionary called "student" with keys "name" and "grade"
# student = ???
# print("Student:", student)
# print("Name:", student["name"])
# print("Grade:", student["grade"])


# ===== PART 2: Adding and Changing Values =====
# TODO: Add a new key "school" to the student dictionary
# student[???] = ???
# print("Updated student:", student)

# TODO: Change the grade to a new value
# student[???] = ???
# print("After grade change:", student)


# ===== PART 3: A Graph as a Dictionary =====
# Each key is a node (row, col), each value is a list of neighbor tuples.

# TODO: Create a graph dictionary for just the four corners of the grid:
# (0,0) connects to (0,1) and (1,0)
# (0,3) connects to (0,2) and (1,3)
# (3,0) connects to (2,0) and (3,1)
# (3,3) connects to (2,3) and (3,2)

# graph = {
#     (0, 0): ???,
#     (0, 3): ???,
#     (3, 0): ???,
#     (3, 3): ???,
# }

# TODO: Print the neighbors of (0, 0)
# print("Neighbors of (0,0):", graph[(0, 0)])

# TODO: Print the neighbors of (3, 3)
# print("Neighbors of (3,3):", graph[(3, 3)])


# ===== PART 4: Building a Full Grid Graph =====
# TODO: Build a graph dictionary for the full 4x4 grid using loops.
# For each cell, find its valid neighbors (up, down, left, right).
# A neighbor is valid if its row is 0-3 and its column is 0-3.

# graph = {}
# for row in range(4):
#     for col in range(4):
#         neighbors = []
#         # TODO: Check each of the four directions
#         # Up:    (row - 1, col)   — valid if row - 1 >= 0
#         # Down:  (row + 1, col)   — valid if row + 1 < 4
#         # Left:  (row, col - 1)   — valid if col - 1 >= 0
#         # Right: (row, col + 1)   — valid if col + 1 < 4
#
#         graph[(row, col)] = neighbors

# TODO: Print the graph entry for a corner, edge, and interior node
# print("(0, 0):", graph[(0, 0)])
# print("(0, 2):", graph[(0, 2)])
# print("(2, 2):", graph[(2, 2)])


# ===== PART 5: Looping Through a Dictionary =====
# TODO: Print every node and its neighbors using a for loop
# for node in graph:
#     print(node, "->", graph[node])
