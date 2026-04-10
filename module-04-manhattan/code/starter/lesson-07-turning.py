# Lesson 7: Turning — Figuring Out Which Way to Face
# Before the robot can drive, it needs to face the right direction.
#
# Team: ________________________
# Date: ________________________
#
# Headings are numbers that go clockwise:
#   0 = NORTH (moving to a smaller row)
#   1 = EAST  (moving to a larger column)
#   2 = SOUTH (moving to a larger row)
#   3 = WEST  (moving to a smaller column)
#
# To figure out how many right turns are needed:
#   Count clockwise from the current heading to the needed heading.
#   0 right turns = already facing the right way
#   1 right turn  = turn right once (90 degrees)
#   2 right turns = turn around (180 degrees)
#   3 right turns = turn right three times (same as one left turn)
#
# In Lesson 8, the Navigator class will do this with a while loop
# that turns right and increments the heading until it matches.

HEADING_NAMES = ["N", "E", "S", "W"]


# ===== PART 1: get_needed_heading =====
# Given the current position and the next position, figure out
# which heading number (0-3) the robot needs.

def get_needed_heading(current, next_pos):
    """Return 0, 1, 2, or 3 based on how next_pos differs from current.

    current:  a (row, col) tuple
    next_pos: a (row, col) tuple one step away
    """
    # TODO: Compare the rows and columns to determine heading
    # If next_pos row < current row, return 0 (North)
    # If next_pos col > current col, return 1 (East)
    # If next_pos row > current row, return 2 (South)
    # If next_pos col < current col, return 3 (West)
    pass


# ===== PART 2: Test Your Functions =====

# TODO: Uncomment and test get_needed_heading
# print("===== Testing get_needed_heading =====")
# print("(0,0) to (1,0):", get_needed_heading((0,0), (1,0)))  # should be 2 (South)
# print("(1,0) to (0,0):", get_needed_heading((1,0), (0,0)))  # should be 0 (North)
# print("(0,0) to (0,1):", get_needed_heading((0,0), (0,1)))  # should be 1 (East)
# print("(0,1) to (0,0):", get_needed_heading((0,1), (0,0)))  # should be 3 (West)
# print()

# TODO: Trace through a path on paper
# The path does not include the start, so track position separately.
# Path: [(1,0), (2,0), (2,1), (2,2)]
# Start position: (0, 0)
# Starting heading: 0 (North)
#
# Step 1: At (0,0), next is (1,0) — need heading ___, right turns: ___
# Step 2: At (1,0), next is (2,0) — need heading ___, right turns: ___
# Step 3: At (2,0), next is (2,1) — need heading ___, right turns: ___
# Step 4: At (2,1), next is (2,2) — need heading ___, right turns: ___
