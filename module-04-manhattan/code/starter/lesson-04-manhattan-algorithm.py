# Lesson 4: The Manhattan Algorithm — Paper First
# Trace the algorithm by hand before writing code.
#
# Team: ________________________
# Date: ________________________
#
# The Manhattan algorithm finds a path between two grid positions:
#   1. Start at the current position
#   2. Move along ROWS until you reach the destination row
#   3. Move along COLUMNS until you reach the destination column
#
# The robot always moves rows first, then columns.
#
#   Col: 0   1   2   3   4
#  Row 0: +---+---+---+---+
#         |   |   |   |   |
#  Row 1: +---+---+---+---+
#         |   |   |   |   |
#  Row 2: +---+---+---+---+
#         |   |   |   |   |
#  Row 3: +---+---+---+---+


# ===== EXAMPLE: Tracing the Algorithm =====
# Start: (0, 0)  Destination: (2, 3)
#
# Step 1: We are at (0, 0). Destination row is 2.
#         Current row (0) < destination row (2), so move SOUTH.
# Step 2: Move south: (0,0) -> (1,0) -> (2,0)  [now at destination row]
# Step 3: We are at (2, 0). Destination col is 3.
#         Current col (0) < destination col (3), so move EAST.
# Step 4: Move east: (2,0) -> (2,1) -> (2,2) -> (2,3)  [arrived!]
#
# Full path: [(0,0), (1,0), (2,0), (2,1), (2,2), (2,3)]

print("===== Example: (0,0) to (2,3) =====")
print("Path: [(0,0), (1,0), (2,0), (2,1), (2,2), (2,3)]")
print()


# ===== EXERCISE 1: Trace (1, 1) to (3, 4) =====
# TODO: Trace the algorithm by hand on paper, then type the path here.
# Which direction do rows move? (north/south) ???
# Which direction do columns move? (east/west) ???

# TODO: Uncomment and fill in the path
# print("===== Exercise 1: (1,1) to (3,4) =====")
# print("Row direction: ???")
# print("Col direction: ???")
# print("Path: ???")
# print()


# ===== EXERCISE 2: Trace (3, 3) to (1, 0) =====
# This time the robot moves NORTH and WEST!
# TODO: Trace the algorithm by hand, then type the path.

# TODO: Uncomment and fill in the path
# print("===== Exercise 2: (3,3) to (1,0) =====")
# print("Row direction: ???")
# print("Col direction: ???")
# print("Path: ???")
# print()


# ===== EXERCISE 3: Trace (0, 2) to (3, 2) =====
# What happens when the column is already correct?
# TODO: Trace and type the path.

# TODO: Uncomment and fill in the path
# print("===== Exercise 3: (0,2) to (3,2) =====")
# print("Row direction: ???")
# print("Col direction: (none — already there!)")
# print("Path: ???")
# print()


# ===== EXERCISE 4: Trace (2, 0) to (2, 4) =====
# What happens when the row is already correct?
# TODO: Trace and type the path.

# TODO: Uncomment and fill in the path
# print("===== Exercise 4: (2,0) to (2,4) =====")
# print("Row direction: (none — already there!)")
# print("Col direction: ???")
# print("Path: ???")
# print()


# ===== EXERCISE 5: How Many Steps? =====
# TODO: For each exercise above, count how many steps the path takes.
# Remember: the number of steps = len(path) - 1 (don't count the start)
# print("Exercise 1 steps: ???")
# print("Exercise 2 steps: ???")
# print("Exercise 3 steps: ???")
# print("Exercise 4 steps: ???")
