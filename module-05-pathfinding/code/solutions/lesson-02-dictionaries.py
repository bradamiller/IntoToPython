# Lesson 2: Dictionaries — Mapping Nodes to Neighbors - SOLUTION
# A dictionary maps KEYS to VALUES, perfect for representing a graph.
#
# Dictionary syntax:
#   my_dict = {key1: value1, key2: value2}
#   my_dict[key1]   # gets value1
#
# For our graph:
#   graph = {(0,0): [(0,1), (1,0)], ...}
#   graph[(0,0)] gives the list of neighbors of (0,0)


# ===== PART 1: Creating a Dictionary =====
student = {"name": "Alice", "grade": 10}
print("Student:", student)
print("Name:", student["name"])
print("Grade:", student["grade"])
print()


# ===== PART 2: Adding and Changing Values =====
student["school"] = "Riverside High"
print("Updated student:", student)

student["grade"] = 11
print("After grade change:", student)
print()


# ===== PART 3: A Graph as a Dictionary =====
graph = {
    (0, 0): [(0, 1), (1, 0)],
    (0, 3): [(0, 2), (1, 3)],
    (3, 0): [(2, 0), (3, 1)],
    (3, 3): [(2, 3), (3, 2)],
}
print("===== Corner Graph =====")
print("Neighbors of (0,0):", graph[(0, 0)])
print("Neighbors of (3,3):", graph[(3, 3)])
print()


# ===== PART 4: Building a Full Grid Graph =====
graph = {}
for row in range(4):
    for col in range(4):
        neighbors = []
        if row - 1 >= 0:
            neighbors.append((row - 1, col))
        if row + 1 < 4:
            neighbors.append((row + 1, col))
        if col - 1 >= 0:
            neighbors.append((row, col - 1))
        if col + 1 < 4:
            neighbors.append((row, col + 1))
        graph[(row, col)] = neighbors

print("===== Full 4x4 Grid Graph =====")
print("(0, 0):", graph[(0, 0)])
print("(0, 2):", graph[(0, 2)])
print("(2, 2):", graph[(2, 2)])
print()


# ===== PART 5: Looping Through a Dictionary =====
print("===== All Nodes and Neighbors =====")
for node in graph:
    print(node, "->", graph[node])
