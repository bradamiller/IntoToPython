# Lesson 5: A Reusable Manhattan Function - SOLUTION
# Rename and document the compute_path function from Lesson 4.
#
# The algorithm itself does NOT change -- this is a rename, not a rewrite.


def compute_manhattan_path(position, destination):
    """Compute a Manhattan path from position to destination.

    position:    a (row, col) tuple -- where the robot is now
    destination: a (row, col) tuple -- where it needs to go

    Returns a list of (row, col) tuples the robot should move to,
    not including position itself.
    """
    path = []

    current_row, current_col = position
    dest_row, dest_col = destination

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


# ===== Test the Function =====

# Test 1: (0,0) to (2,3) — south then east
path = compute_manhattan_path((0, 0), (2, 3))
print("Start: (0, 0)")
print("Destination: (2, 3)")
print("Path:", path)
print("Steps:", len(path))
print()

# Test 2: (0,0) to (3,1) — south then east
path2 = compute_manhattan_path((0, 0), (3, 1))
print("Start: (0, 0)")
print("Destination: (3, 1)")
print("Path:", path2)
print("Steps:", len(path2))
print()

# Test 3: Starting from a different position
path3 = compute_manhattan_path((3, 3), (1, 0))
print("Start: (3, 3)")
print("Destination: (1, 0)")
print("Path:", path3)
print("Steps:", len(path3))
print()

# Test 4: Same row — only column movement
path4 = compute_manhattan_path((2, 0), (2, 4))
print("Start: (2, 0)")
print("Destination: (2, 4)")
print("Path:", path4)
print("Steps:", len(path4))
