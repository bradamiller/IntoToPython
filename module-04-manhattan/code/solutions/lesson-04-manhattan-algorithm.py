# Lesson 4: The Manhattan Algorithm — Paper First - SOLUTION
# Trace the algorithm by hand before writing code.
#
# The Manhattan algorithm finds a path between two grid positions:
#   1. Start at the current position
#   2. Move along ROWS until you reach the destination row
#   3. Move along COLUMNS until you reach the destination column


# ===== EXAMPLE: Tracing the Algorithm =====
# Start: (0, 0)  Destination: (2, 3)
#
# Step 1: We are at (0, 0). Destination row is 2.
#         Current row (0) < destination row (2), so move SOUTH.
# Step 2: Move south: (0,0) -> (1,0) -> (2,0)  [now at destination row]
# Step 3: We are at (2, 0). Destination col is 3.
#         Current col (0) < destination col (3), so move EAST.
# Step 4: Move east: (2,0) -> (2,1) -> (2,2) -> (2,3)  [arrived!]

print("===== Example: (0,0) to (2,3) =====")
print("Path: [(0,0), (1,0), (2,0), (2,1), (2,2), (2,3)]")
print()


# ===== EXERCISE 1: Trace (1, 1) to (3, 4) =====
# Row: 1 -> 3, moving south (+1)
# Col: 1 -> 4, moving east (+1)
# Path: (1,1) -> (2,1) -> (3,1) -> (3,2) -> (3,3) -> (3,4)
print("===== Exercise 1: (1,1) to (3,4) =====")
print("Row direction: south")
print("Col direction: east")
print("Path: [(1,1), (2,1), (3,1), (3,2), (3,3), (3,4)]")
print()


# ===== EXERCISE 2: Trace (3, 3) to (1, 0) =====
# Row: 3 -> 1, moving north (-1)
# Col: 3 -> 0, moving west (-1)
# Path: (3,3) -> (2,3) -> (1,3) -> (1,2) -> (1,1) -> (1,0)
print("===== Exercise 2: (3,3) to (1,0) =====")
print("Row direction: north")
print("Col direction: west")
print("Path: [(3,3), (2,3), (1,3), (1,2), (1,1), (1,0)]")
print()


# ===== EXERCISE 3: Trace (0, 2) to (3, 2) =====
# Row: 0 -> 3, moving south (+1)
# Col: 2 -> 2, no movement needed!
# Path: (0,2) -> (1,2) -> (2,2) -> (3,2)
print("===== Exercise 3: (0,2) to (3,2) =====")
print("Row direction: south")
print("Col direction: (none — already there!)")
print("Path: [(0,2), (1,2), (2,2), (3,2)]")
print()


# ===== EXERCISE 4: Trace (2, 0) to (2, 4) =====
# Row: 2 -> 2, no movement needed!
# Col: 0 -> 4, moving east (+1)
# Path: (2,0) -> (2,1) -> (2,2) -> (2,3) -> (2,4)
print("===== Exercise 4: (2,0) to (2,4) =====")
print("Row direction: (none — already there!)")
print("Col direction: east")
print("Path: [(2,0), (2,1), (2,2), (2,3), (2,4)]")
print()


# ===== EXERCISE 5: How Many Steps? =====
print("===== Step Counts =====")
print("Exercise 1 steps:", 5)   # 6 positions - 1 = 5 steps
print("Exercise 2 steps:", 5)   # 6 positions - 1 = 5 steps
print("Exercise 3 steps:", 3)   # 4 positions - 1 = 3 steps
print("Exercise 4 steps:", 4)   # 5 positions - 1 = 4 steps
