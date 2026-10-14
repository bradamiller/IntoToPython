# Lesson 5 Optional Extension: The Manhattan Class
# Classes-track reference: compute_manhattan_path() from
# lesson-05-manhattan-function.py, repackaged as a class.
# Output is identical to the function version. No robot needed to run this.
#
# The only change from the function: it moved inside the class and gained
# self. The position is still passed IN -- a planner never remembers where
# the robot is. (Why make it a class at all? So it has the same shape as the
# Module 5 planners. See the docstring.)


class Manhattan:
    """The Lesson 5 planner as a class.

    It holds NO state: compute_path() is told the robot's position every
    time, and the Navigator is the only thing that tracks where the robot
    is. Manhattan is a class only so that it has the same shape as the
    Module 5 planners (BFS, Dijkstra) -- then one main program and one test
    harness work with any of them by changing one name.
    """

    def __init__(self):
        pass        # nothing to set up

    def compute_path(self, position, destination):
        path = []
        current_row, current_col = position
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


# ===== Test the Class =====
planner = Manhattan()

path = planner.compute_path((0, 0), (2, 3))
print("Start: (0, 0)")
print("Destination: (2, 3)")
print("Path:", path)
print("Steps:", len(path))
print()

path2 = planner.compute_path((3, 3), (1, 0))
print("Start: (3, 3)")
print("Destination: (1, 0)")
print("Path:", path2)
print("Steps:", len(path2))
