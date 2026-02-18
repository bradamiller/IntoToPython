# Lesson 1: Coordinates on the Grid
# Learn how to describe positions using row and column numbers
#
# Team: ________________________
# Date: ________________________
#
# Our grid uses (row, col) coordinates:
#   - Row 0 is the top row, rows increase going SOUTH
#   - Column 0 is the left column, columns increase going EAST
#   - Example: (2, 3) means row 2, column 3
#
#   Col: 0   1   2   3   4
#  Row 0: +---+---+---+---+
#         |   |   |   |   |
#  Row 1: +---+---+---+---+
#         |   |   |   |   |
#  Row 2: +---+---+---+---+
#         |   |   |   |   |
#  Row 3: +---+---+---+---+


# ===== PART 1: Creating Position Variables =====
# TODO: Create variables for the robot's starting position
# The robot starts at row 0, column 0 (top-left corner)
# start_row = ???
# start_col = ???

# TODO: Print the starting position
# print("Starting position: row", start_row, "col", start_col)


# ===== PART 2: A Destination =====
# TODO: Create variables for a destination at row 2, column 3
# dest_row = ???
# dest_col = ???

# TODO: Print the destination
# print("Destination: row", dest_row, "col", dest_col)


# ===== PART 3: How Far Apart? =====
# To find how far apart two positions are on a grid,
# we calculate the difference in rows and columns.

# TODO: Calculate the row distance (how many rows apart)
# row_distance = ???
# Hint: subtract start_row from dest_row

# TODO: Calculate the column distance (how many columns apart)
# col_distance = ???

# TODO: Print the distances
# print("Row distance:", row_distance)
# print("Column distance:", col_distance)


# ===== PART 4: Total Manhattan Distance =====
# The Manhattan distance is the total number of blocks you
# must travel (only moving along grid lines, no diagonals).

# TODO: Calculate the total Manhattan distance
# total_distance = ???
# Hint: add row_distance and col_distance

# TODO: Print the total distance
# print("Manhattan distance:", total_distance, "blocks")


# ===== PART 5: Try Another Destination =====
# TODO: Create variables for a new destination at row 1, column 4
# TODO: Calculate and print the Manhattan distance from start to this new spot
