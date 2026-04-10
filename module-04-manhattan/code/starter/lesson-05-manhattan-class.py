# Lesson 5: The Manhattan Class
# Turn the compute_path function into a reusable class.
#
# Team: ________________________
# Date: ________________________
#
# In Lesson 4 you wrote a compute_path function.
# Now wrap it in a class so it can store the robot's position.
#
# The Manhattan class will:
#   - Store the robot's current position in __init__
#   - Have a compute_path method that uses self.position as the start


class Manhattan:

    def __init__(self, start):
        self.position = start

    def compute_path(self, destination):
        path = []

        current_row, current_col = self.position
        dest_row, dest_col = destination

        # TODO: Copy your 4 while loops from Lesson 4 here.
        # The only change: use self.position instead of the
        # start parameter (already done above with tuple unpacking).

        # Move south (rows increase)

        # Move north (rows decrease)

        # Move east (columns increase)

        # Move west (columns decrease)

        return path


# ===== Test Your Class =====
# TODO: Uncomment the code below to test your Manhattan class

# nav = Manhattan((0, 0))
# path = nav.compute_path((2, 3))
# print("Start: (0, 0)")
# print("Destination: (2, 3)")
# print("Path:", path)
# print("Steps:", len(path))
# print()

# TODO: Test with another start and destination
# nav2 = Manhattan((3, 3))
# path2 = nav2.compute_path((1, 0))
# print("Start: (3, 3)")
# print("Destination: (1, 0)")
# print("Path:", path2)
# print("Steps:", len(path2))
