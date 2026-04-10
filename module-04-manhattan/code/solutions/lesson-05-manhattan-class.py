# Lesson 5: The Manhattan Class - SOLUTION
# Turn the compute_path function into a reusable class.
#
# A class bundles data and functions together.
# Our Manhattan class will:
#   - Store the robot's current position
#   - Compute a path to any destination using the Manhattan algorithm


class Manhattan:

    def __init__(self, start):
        self.position = start

    def compute_path(self, destination):
        path = []

        current_row, current_col = self.position
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


# ===== Test the Class =====
nav = Manhattan((0, 0))

# Test 1: (0,0) to (2,3) — south then east
path = nav.compute_path((2, 3))
print("Start: (0, 0)")
print("Destination: (2, 3)")
print("Path:", path)
print("Steps:", len(path))
print()

# Test 2: (0,0) to (3,1) — south then east
path2 = nav.compute_path((3, 1))
print("Start: (0, 0)")
print("Destination: (3, 1)")
print("Path:", path2)
print("Steps:", len(path2))
print()

# Test 3: Starting from a different position
nav2 = Manhattan((3, 3))
path3 = nav2.compute_path((1, 0))
print("Start: (3, 3)")
print("Destination: (1, 0)")
print("Path:", path3)
print("Steps:", len(path3))
print()

# Test 4: Same row — only column movement
nav3 = Manhattan((2, 0))
path4 = nav3.compute_path((2, 4))
print("Start: (2, 0)")
print("Destination: (2, 4)")
print("Path:", path4)
print("Steps:", len(path4))
