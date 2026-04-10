# Lesson 4: The Manhattan Algorithm
# Build a compute_path function step by step.
#
# Team: ________________________
# Date: ________________________
#
# The Manhattan algorithm finds a path between two grid positions:
#   1. Move along ROWS until you reach the destination row
#   2. Move along COLUMNS until you reach the destination column
#
# The path does NOT include the starting position (the robot is already there).
#
#   Col: 0   1   2   3   4
#  Row 0: +---+---+---+---+
#         |   |   |   |   |
#  Row 1: +---+---+---+---+
#         |   |   |   |   |
#  Row 2: +---+---+---+---+
#         |   |   |   |   |
#  Row 3: +---+---+---+---+


# ===== PART 1: Positive Directions Only =====
# Write a compute_path function that works when the destination
# is south (larger row) and east (larger column) of the start.
#
# Parameters:
#   start - a (row, col) tuple
#   end   - a (row, col) tuple
#
# Returns: a list of (row, col) tuples (not including start)

def compute_path(start, end):
    path = []
    current_row, current_col = start
    dest_row, dest_col = end

    # TODO: While current_row is less than dest_row,
    #   add 1 to current_row
    #   append (current_row, current_col) to path

    # TODO: While current_col is less than dest_col,
    #   add 1 to current_col
    #   append (current_row, current_col) to path

    return path


# Test Part 1
print("===== Part 1: Positive Directions =====")
path = compute_path((0, 0), (2, 3))
print("(0,0) to (2,3):", path)
# Expected: [(1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]

path = compute_path((1, 1), (3, 4))
print("(1,1) to (3,4):", path)
# Expected: [(2, 1), (3, 1), (3, 2), (3, 3), (3, 4)]
print()


# ===== PART 2: All Directions =====
# Try your function with a path that goes north or west:
#   compute_path((3, 3), (1, 0))
# It returns [] because 3 is not less than 1!
#
# Fix: Add two more while loops — one for north (current_row > dest_row)
# and one for west (current_col > dest_col).
#
# Only the loops that need to run will execute.
# No if statements needed!

# TODO: Rewrite compute_path below with 4 while loops:
#   south (current_row < dest_row, add 1)
#   north (current_row > dest_row, subtract 1)
#   east  (current_col < dest_col, add 1)
#   west  (current_col > dest_col, subtract 1)

# def compute_path(start, end):
#     path = []
#     current_row, current_col = start
#     dest_row, dest_col = end
#
#     # TODO: 4 while loops here
#
#     return path


# Test Part 2 — uncomment after writing the 4-loop version
# print("===== Part 2: All Directions =====")
# path = compute_path((0, 0), (2, 3))
# print("(0,0) to (2,3):", path)
#
# path = compute_path((3, 3), (1, 0))
# print("(3,3) to (1,0):", path)
#
# path = compute_path((1, 3), (3, 1))
# print("(1,3) to (3,1):", path)
#
# # Edge cases
# path = compute_path((2, 0), (2, 3))
# print("(2,0) to (2,3):", path)
#
# path = compute_path((0, 2), (3, 2))
# print("(0,2) to (3,2):", path)
#
# path = compute_path((1, 1), (1, 1))
# print("(1,1) to (1,1):", path)
