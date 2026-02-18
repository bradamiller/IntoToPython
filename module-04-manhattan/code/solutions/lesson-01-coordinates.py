# Lesson 1: Coordinates on the Grid - SOLUTION
# Learn how to describe positions using row and column numbers
#
# Our grid uses (row, col) coordinates:
#   - Row 0 is the top row, rows increase going SOUTH
#   - Column 0 is the left column, columns increase going EAST
#   - Example: (2, 3) means row 2, column 3


# ===== PART 1: Creating Position Variables =====
start_row = 0
start_col = 0
print("Starting position: row", start_row, "col", start_col)


# ===== PART 2: A Destination =====
dest_row = 2
dest_col = 3
print("Destination: row", dest_row, "col", dest_col)


# ===== PART 3: How Far Apart? =====
row_distance = dest_row - start_row
col_distance = dest_col - start_col
print("Row distance:", row_distance)
print("Column distance:", col_distance)


# ===== PART 4: Total Manhattan Distance =====
total_distance = row_distance + col_distance
print("Manhattan distance:", total_distance, "blocks")


# ===== PART 5: Try Another Destination =====
dest2_row = 1
dest2_col = 4
row_distance2 = dest2_row - start_row
col_distance2 = dest2_col - start_col
total_distance2 = row_distance2 + col_distance2
print()
print("Second destination: row", dest2_row, "col", dest2_col)
print("Row distance:", row_distance2)
print("Column distance:", col_distance2)
print("Manhattan distance:", total_distance2, "blocks")
