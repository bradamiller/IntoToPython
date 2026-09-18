# Lesson 5: A Reusable Manhattan Function
# Rename and document the compute_path function from Lesson 4.
#
# Team: ________________________
# Date: ________________________
#
# In Lesson 4 you wrote a compute_path function.
# Now give it a name specific to the algorithm (compute_manhattan_path)
# and a docstring, since Module 5 will introduce a second algorithm
# (Dijkstra) that needs its own, differently-named function.
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

    # TODO: Copy your 4 while loops from Lesson 4 here.
    # The only change: parameters are named position/destination
    # instead of start/end (already handled above via tuple unpacking).

    # Move south (rows increase)

    # Move north (rows decrease)

    # Move east (columns increase)

    # Move west (columns decrease)

    return path


# ===== Regression Test: Confirm the Rename Didn't Change Behavior =====
# TODO: Uncomment the code below and compare against your Lesson 4 output

# path = compute_manhattan_path((0, 0), (2, 3))
# print("Start: (0, 0)")
# print("Destination: (2, 3)")
# print("Path:", path)
# print("Steps:", len(path))
# print()

# TODO: Test with another position and destination
# path2 = compute_manhattan_path((3, 3), (1, 0))
# print("Start: (3, 3)")
# print("Destination: (1, 0)")
# print("Path:", path2)
# print("Steps:", len(path2))
