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
# To figure out how to turn:
#   Count quarter turns clockwise from the current heading to the needed one.
#   0 = already facing the right way
#   1 = one clockwise turn (90 degrees)
#   2 = turn around (180 degrees)
#   3 = three clockwise turns -- or ONE counterclockwise turn, which is what
#       the robot will actually do
#
# In Lesson 8, turn_to() computes that count with (desired - heading) % 4
# and makes the turns.

HEADING_NAMES = ["N", "E", "S", "W"]


# ===== PART 1: desired_heading =====
# Given the current position and the next position, figure out
# which heading number (0-3) the robot needs.

def desired_heading(current, next_pos):
    """Return 0, 1, 2, or 3 based on how next_pos differs from current.

    current:  a (row, col) tuple
    next_pos: a (row, col) tuple one step away
    """
    # TODO: Compute row_diff and col_diff (next minus current)
    # TODO: Check BOTH differences in each case:
    #   col unchanged and row_diff == -1  -> return 0 (North)
    #   row unchanged and col_diff ==  1  -> return 1 (East)
    #   col unchanged and row_diff ==  1  -> return 2 (South)
    #   row unchanged and col_diff == -1  -> return 3 (West)
    # TODO: If none matched, the two positions are not neighbors:
    #   raise ValueError(str(current) + " and " + str(next_pos) + " are not neighbors")
    pass


# ===== PART 2: Test Your Functions =====

# TODO: Uncomment and test desired_heading
# print("===== Testing desired_heading =====")
# print("(0,0) to (1,0):", desired_heading((0,0), (1,0)))  # should be 2 (South)
# print("(1,0) to (0,0):", desired_heading((1,0), (0,0)))  # should be 0 (North)
# print("(0,0) to (0,1):", desired_heading((0,0), (0,1)))  # should be 1 (East)
# print("(0,1) to (0,0):", desired_heading((0,1), (0,0)))  # should be 3 (West)
# print()

# TODO: Trace through a path on paper
# The path does not include the start, so track position separately.
# Path: [(1,0), (2,0), (2,1), (2,2)]
# Start position: (0, 0)
# Starting heading: 0 (North)
#
# Step 1: At (0,0), next is (1,0) — need heading ___, clockwise turns: ___
# Step 2: At (1,0), next is (2,0) — need heading ___, clockwise turns: ___
# Step 3: At (2,0), next is (2,1) — need heading ___, clockwise turns: ___
# Step 4: At (2,1), next is (2,2) — need heading ___, clockwise turns: ___
