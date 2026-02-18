# Lesson 6: Testing — Does Our Algorithm Work?
# Write test cases to verify the Manhattan class produces correct paths.
#
# Team: ________________________
# Date: ________________________
#
# A test case checks that code produces the expected output.
# We will write a helper function that:
#   1. Runs compute_path with a given start and destination
#   2. Compares the result to the expected path
#   3. Prints PASS or FAIL
#
# Good tests cover:
#   - Normal cases (south-east, north-west, etc.)
#   - Edge cases (same row, same column, same position)


# The Manhattan class (complete — use this for testing)
class Manhattan:

    def __init__(self, start):
        self.position = start

    def compute_path(self, destination):
        path = [self.position]
        current_row = self.position[0]
        current_col = self.position[1]
        dest_row = destination[0]
        dest_col = destination[1]

        if dest_row > current_row:
            row_step = 1
        else:
            row_step = -1

        if dest_col > current_col:
            col_step = 1
        else:
            col_step = -1

        while current_row != dest_row:
            current_row = current_row + row_step
            path.append((current_row, current_col))

        while current_col != dest_col:
            current_col = current_col + col_step
            path.append((current_row, current_col))

        return path


# ===== PART 1: A Test Helper Function =====
# This function runs one test and prints the result.
def run_test(test_name, start, destination, expected_path):
    nav = Manhattan(start)
    actual_path = nav.compute_path(destination)
    if actual_path == expected_path:
        print("PASS:", test_name)
    else:
        print("FAIL:", test_name)
        print("  Expected:", expected_path)
        print("  Got:     ", actual_path)


# ===== PART 2: Write Your Test Cases =====

# Test 1 (example): South and East
run_test(
    "South-East: (0,0) to (2,3)",
    (0, 0),
    (2, 3),
    [(0,0), (1,0), (2,0), (2,1), (2,2), (2,3)]
)

# TODO: Test 2 — North and West
# Go from (3, 3) to (1, 0). What should the path be?
# run_test(
#     "North-West: (3,3) to (1,0)",
#     ???,
#     ???,
#     ???
# )

# TODO: Test 3 — Same row (only column movement)
# Go from (2, 0) to (2, 4). The row does not change.
# run_test(
#     "Same row: (2,0) to (2,4)",
#     ???,
#     ???,
#     ???
# )

# TODO: Test 4 — Same column (only row movement)
# Go from (0, 2) to (3, 2). The column does not change.
# run_test(
#     ???,
#     ???,
#     ???,
#     ???
# )

# TODO: Test 5 — Already at destination
# Go from (1, 1) to (1, 1). The path should be just the start.
# run_test(
#     ???,
#     ???,
#     ???,
#     ???
# )

# TODO: Test 6 — One step only
# Go from (0, 0) to (1, 0). Just one step south.
# run_test(
#     ???,
#     ???,
#     ???,
#     ???
# )
