# Lesson 5: The Manhattan Class
# Turn the Manhattan algorithm into a reusable class.
#
# Team: ________________________
# Date: ________________________
#
# A class bundles data and functions together.
# Our Manhattan class will:
#   - Store the robot's current position
#   - Compute a path to any destination using the Manhattan algorithm
#
# Review of the algorithm:
#   1. Start at current position
#   2. Move rows first (south if dest_row > current_row, north otherwise)
#   3. Move columns second (east if dest_col > current_col, west otherwise)


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

        # TODO: Determine the row step direction.
        # If dest_row > current_row, we need to go south (step = 1)
        # Otherwise, we need to go north (step = -1)
        # row_step = ???

        # TODO: Determine the column step direction.
        # If dest_col > current_col, we need to go east (step = 1)
        # Otherwise, we need to go west (step = -1)
        # col_step = ???

        # TODO: Use a while loop to move along rows until
        # current_row equals dest_row.
        # Each iteration:
        #   - Update current_row by adding row_step
        #   - Append the new position (current_row, current_col) to path
        # while ???:
        #     current_row = ???
        #     path.append(???)

        # TODO: Use a while loop to move along columns until
        # current_col equals dest_col.
        # Each iteration:
        #   - Update current_col by adding col_step
        #   - Append the new position (current_row, current_col) to path
        # while ???:
        #     current_col = ???
        #     path.append(???)

        return path


# ===== Test Your Class =====
# TODO: Uncomment the code below to test your Manhattan class

# nav = Manhattan((0, 0))
# path = nav.compute_path((2, 3))
# print("Start: (0, 0)")
# print("Destination: (2, 3)")
# print("Path:", path)
# print("Steps:", len(path) - 1)
# print()

# TODO: Test with another start and destination
# path2 = nav.compute_path((3, 1))
# print("Start: (0, 0)")
# print("Destination: (3, 1)")
# print("Path:", path2)
# print("Steps:", len(path2) - 1)
