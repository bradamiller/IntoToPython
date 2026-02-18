# Lesson 5: The Manhattan Class - SOLUTION
# Turn the Manhattan algorithm into a reusable class.
#
# A class bundles data and functions together.
# Our Manhattan class will:
#   - Store the robot's current position
#   - Compute a path to any destination using the Manhattan algorithm


class Manhattan:

    def __init__(self, start):
        """Create a Manhattan navigator starting at the given position."""
        self.position = start

    def compute_path(self, destination):
        """Compute a Manhattan path from current position to destination.
        Returns a list of (row, col) tuples."""
        path = [self.position]

        current_row = self.position[0]
        current_col = self.position[1]
        dest_row = destination[0]
        dest_col = destination[1]

        # Determine the row step direction
        if dest_row > current_row:
            row_step = 1
        else:
            row_step = -1

        # Determine the column step direction
        if dest_col > current_col:
            col_step = 1
        else:
            col_step = -1

        # Move along rows until we reach the destination row
        while current_row != dest_row:
            current_row = current_row + row_step
            path.append((current_row, current_col))

        # Move along columns until we reach the destination column
        while current_col != dest_col:
            current_col = current_col + col_step
            path.append((current_row, current_col))

        return path


# ===== Test the Class =====
nav = Manhattan((0, 0))

# Test 1: (0,0) to (2,3) — south then east
path = nav.compute_path((2, 3))
print("Start: (0, 0)")
print("Destination: (2, 3)")
print("Path:", path)
print("Steps:", len(path) - 1)
print()

# Test 2: (0,0) to (3,1) — south then east
path2 = nav.compute_path((3, 1))
print("Start: (0, 0)")
print("Destination: (3, 1)")
print("Path:", path2)
print("Steps:", len(path2) - 1)
print()

# Test 3: Starting from a different position
nav2 = Manhattan((3, 3))
path3 = nav2.compute_path((1, 0))
print("Start: (3, 3)")
print("Destination: (1, 0)")
print("Path:", path3)
print("Steps:", len(path3) - 1)
print()

# Test 4: Same row — only column movement
nav3 = Manhattan((2, 0))
path4 = nav3.compute_path((2, 4))
print("Start: (2, 0)")
print("Destination: (2, 4)")
print("Path:", path4)
print("Steps:", len(path4) - 1)
