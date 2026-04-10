# Lesson 6: Testing — Does Our Algorithm Work? - SOLUTION
# Write test cases to verify the Manhattan class produces correct paths.
#
# Good tests cover:
#   - Normal cases (south-east, north-west, etc.)
#   - Edge cases (same row, same column, same position)


# The Manhattan class (complete — use this for testing)
class Manhattan:

    def __init__(self, start):
        self.position = start

    def compute_path(self, destination):
        path = []

        current_row, current_col = self.position
        dest_row, dest_col = destination

        while current_row < dest_row:
            current_row = current_row + 1
            path.append((current_row, current_col))

        while current_row > dest_row:
            current_row = current_row - 1
            path.append((current_row, current_col))

        while current_col < dest_col:
            current_col = current_col + 1
            path.append((current_row, current_col))

        while current_col > dest_col:
            current_col = current_col - 1
            path.append((current_row, current_col))

        return path


# ===== Test Helper Function =====
def run_test(test_name, start, destination, expected_path):
    nav = Manhattan(start)
    actual_path = nav.compute_path(destination)
    if actual_path == expected_path:
        print("PASS:", test_name)
    else:
        print("FAIL:", test_name)
        print("  Expected:", expected_path)
        print("  Got:     ", actual_path)


# ===== Test Cases =====

# Test 1: South and East
run_test(
    "South-East: (0,0) to (2,3)",
    (0, 0),
    (2, 3),
    [(1,0), (2,0), (2,1), (2,2), (2,3)]
)

# Test 2: North and West
run_test(
    "North-West: (3,3) to (1,0)",
    (3, 3),
    (1, 0),
    [(2,3), (1,3), (1,2), (1,1), (1,0)]
)

# Test 3: Same row (only column movement)
run_test(
    "Same row: (2,0) to (2,4)",
    (2, 0),
    (2, 4),
    [(2,1), (2,2), (2,3), (2,4)]
)

# Test 4: Same column (only row movement)
run_test(
    "Same col: (0,2) to (3,2)",
    (0, 2),
    (3, 2),
    [(1,2), (2,2), (3,2)]
)

# Test 5: Already at destination
run_test(
    "Already there: (1,1) to (1,1)",
    (1, 1),
    (1, 1),
    []
)

# Test 6: One step only
run_test(
    "One step south: (0,0) to (1,0)",
    (0, 0),
    (1, 0),
    [(1,0)]
)
