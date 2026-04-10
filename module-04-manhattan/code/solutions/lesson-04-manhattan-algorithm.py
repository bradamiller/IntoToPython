# Lesson 4: The Manhattan Algorithm - SOLUTION
# Build a compute_path function step by step.
#
# The Manhattan algorithm finds a path between two grid positions:
#   1. Move along ROWS until you reach the destination row
#   2. Move along COLUMNS until you reach the destination column
#
# The path does NOT include the starting position (the robot is already there).


# ===== PART 1: Positive Directions Only =====
# This version only works when the destination is
# south (larger row) and east (larger column) of the start.

def compute_path(start, end):
    path = []
    current_row, current_col = start
    dest_row, dest_col = end

    # Move south (rows increase)
    while current_row < dest_row:
        current_row = current_row + 1
        path.append((current_row, current_col))

    # Move east (columns increase)
    while current_col < dest_col:
        current_col = current_col + 1
        path.append((current_row, current_col))

    return path


# Test Part 1
print("===== Part 1: Positive Directions =====")
path = compute_path((0, 0), (2, 3))
print("(0,0) to (2,3):", path)

path = compute_path((1, 1), (3, 4))
print("(1,1) to (3,4):", path)
print()


# ===== PART 2: All Directions =====
# Try: compute_path((3, 3), (1, 0)) — returns [] because 3 is not less than 1!
#
# Fix: Add two more while loops for north and west.
# Only the loops that need to run will execute.
# No if statements needed!

def compute_path(start, end):
    path = []
    current_row, current_col = start
    dest_row, dest_col = end

    # Move south (rows increase)
    while current_row < dest_row:
        current_row = current_row + 1
        path.append((current_row, current_col))

    # Move north (rows decrease)
    while current_row > dest_row:
        current_row = current_row - 1
        path.append((current_row, current_col))

    # Move east (columns increase)
    while current_col < dest_col:
        current_col = current_col + 1
        path.append((current_row, current_col))

    # Move west (columns decrease)
    while current_col > dest_col:
        current_col = current_col - 1
        path.append((current_row, current_col))

    return path


# Test Part 2 — all directions
print("===== Part 2: All Directions =====")
path = compute_path((0, 0), (2, 3))
print("(0,0) to (2,3):", path)

path = compute_path((3, 3), (1, 0))
print("(3,3) to (1,0):", path)

path = compute_path((1, 3), (3, 1))
print("(1,3) to (3,1):", path)

# Edge cases
path = compute_path((2, 0), (2, 3))
print("(2,0) to (2,3):", path)

path = compute_path((0, 2), (3, 2))
print("(0,2) to (3,2):", path)

path = compute_path((1, 1), (1, 1))
print("(1,1) to (1,1):", path)
