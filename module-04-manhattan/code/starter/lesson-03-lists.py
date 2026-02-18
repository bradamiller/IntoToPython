# Lesson 3: Lists — Building a Path
# A list stores an ordered sequence of items that can grow and change.
#
# Team: ________________________
# Date: ________________________
#
# Lists use square brackets []:
#   my_list = []              # empty list
#   my_list.append("hello")   # add an item
#   my_list[0]                # first item
#   len(my_list)              # how many items
#
# We will use a list of tuples to represent a path on the grid.
# Example path: [(0,0), (1,0), (2,0), (2,1)]


# ===== PART 1: Creating a List =====
# TODO: Create an empty list called "path"
# path = ???

# TODO: Print the empty path and its length
# print("Path:", path)
# print("Length:", len(path))


# ===== PART 2: Adding Positions with Append =====
# TODO: Append the starting position (0, 0) to the path
# path.append(???)

# TODO: Append position (1, 0) to the path
# path.append(???)

# TODO: Append position (2, 0) to the path

# TODO: Print the path and its length
# print("Path:", path)
# print("Length:", len(path))


# ===== PART 3: Accessing Items in a List =====
# TODO: Print the first position in the path (index 0)
# print("First position:", path[0])

# TODO: Print the last position in the path (index -1 or len-1)
# print("Last position:", path[???])


# ===== PART 4: Iterating Through a Path =====
# A for loop visits each item in a list, one at a time.

# TODO: Use a for loop to print each position in the path
# for position in path:
#     print("  Visiting:", position)


# ===== PART 5: Building a Longer Path with a Loop =====
# Let's build a path that goes from (0,0) to (0,4) — straight east.

# TODO: Create an empty list called "east_path"
# TODO: Use a for loop with range(5) to append (0, col) for each col
# for col in range(5):
#     east_path.append(???)

# TODO: Print the east path
# print("East path:", east_path)


# ===== PART 6: Building a Two-Part Path =====
# Build a path from (0,0) going south to (3,0), then east to (3,2)

# TODO: Create an empty list called "two_part_path"
# TODO: First loop: go south (rows 0 through 3, column stays 0)
# TODO: Second loop: go east (row stays 3, columns 1 through 2)
# TODO: Print the complete path and its length
