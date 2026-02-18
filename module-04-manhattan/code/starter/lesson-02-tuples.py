# Lesson 2: Tuples — Packaging Coordinates Together
# Instead of separate row/col variables, use a tuple: (row, col)
#
# Team: ________________________
# Date: ________________________
#
# A tuple groups values together:
#   position = (2, 3)    # row 2, col 3
#   position[0]          # gets the row (2)
#   position[1]          # gets the col (3)
#
# Tuples use parentheses () and cannot be changed after creation.


# ===== PART 1: Creating Position Tuples =====
# TODO: Create a tuple for the starting position (0, 0)
# start = ???

# TODO: Create a tuple for the destination (2, 3)
# destination = ???

# TODO: Print both positions
# print("Start:", start)
# print("Destination:", destination)


# ===== PART 2: Accessing Row and Column =====
# You can get individual values from a tuple using [0] and [1]

# TODO: Print the row and column of the destination separately
# print("Destination row:", destination[???])
# print("Destination col:", destination[???])


# ===== PART 3: Comparing Positions =====
# You can compare tuples with == to check if two positions are the same

# TODO: Create a position variable set to (0, 0)
# current = ???

# TODO: Check if current equals start — print the result
# print("At start?", current == start)

# TODO: Check if current equals destination — print the result
# print("At destination?", current == destination)


# ===== PART 4: Manhattan Distance with Tuples =====
# TODO: Calculate Manhattan distance between start and destination
# Use start[0], start[1], destination[0], destination[1]
# row_dist = ???
# col_dist = ???
# total = ???
# print("Manhattan distance:", total)


# ===== PART 5: Multiple Destinations =====
# TODO: Create 3 destination tuples and calculate the Manhattan
# distance from start to each one. Print the results.
# dest_a = (1, 2)
# dest_b = (3, 1)
# dest_c = (2, 4)
