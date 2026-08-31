# Lesson 5 Optional Extension: The Manhattan Class
# Classes-track reference: compute_manhattan_path() from
# lesson-05-manhattan-function.py, repackaged as a class.
# Output is identical to the function version.


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

path = nav.compute_path((2, 3))
print("Start: (0, 0)")
print("Destination: (2, 3)")
print("Path:", path)
print("Steps:", len(path))
print()

nav2 = Manhattan((3, 3))
path2 = nav2.compute_path((1, 0))
print("Start: (3, 3)")
print("Destination: (1, 0)")
print("Path:", path2)
print("Steps:", len(path2))
