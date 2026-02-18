# Lesson 3: Lists — Building a Path - SOLUTION
# A list stores an ordered sequence of items that can grow and change.
#
# We will use a list of tuples to represent a path on the grid.


# ===== PART 1: Creating a List =====
path = []
print("Path:", path)
print("Length:", len(path))


# ===== PART 2: Adding Positions with Append =====
path.append((0, 0))
path.append((1, 0))
path.append((2, 0))
print("Path:", path)
print("Length:", len(path))


# ===== PART 3: Accessing Items in a List =====
print("First position:", path[0])
print("Last position:", path[-1])


# ===== PART 4: Iterating Through a Path =====
print("Walking the path:")
for position in path:
    print("  Visiting:", position)


# ===== PART 5: Building a Longer Path with a Loop =====
east_path = []
for col in range(5):
    east_path.append((0, col))
print("East path:", east_path)


# ===== PART 6: Building a Two-Part Path =====
two_part_path = []

# Go south from row 0 to row 3
for row in range(4):
    two_part_path.append((row, 0))

# Go east from col 1 to col 2
for col in range(1, 3):
    two_part_path.append((3, col))

print("Two-part path:", two_part_path)
print("Length:", len(two_part_path))
print("Walking the two-part path:")
for position in two_part_path:
    print("  Visiting:", position)
