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
#   turns = (needed_heading - current_heading) % 4
#
# Examples:
#   0 right turns = already facing the right way
#   1 right turn  = turn right once (90 degrees)
#   2 right turns = turn around (180 degrees)
#   3 right turns = turn right three times (same as one left turn)

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


# ===== PART 2: count_right_turns =====
# Given the current heading and the needed heading,
# figure out how many right turns are needed.

def count_right_turns(current_heading, needed_heading):
    """Return the number of right turns needed (0, 1, 2, or 3).

    current_heading: 0-3 (the direction the robot is facing)
    needed_heading:  0-3 (the direction the robot needs to face)

    Hint: Use the modulo operator %
    """
    # TODO: Calculate and return the number of right turns
    # Formula: (needed_heading - current_heading) % 4
    pass


# ===== PART 3: Test Your Functions =====

# TODO: Uncomment and test get_needed_heading
# print("===== Testing get_needed_heading =====")
# print("(0,0) to (1,0):", get_needed_heading((0,0), (1,0)))  # should be 2 (South)
# print("(1,0) to (0,0):", get_needed_heading((1,0), (0,0)))  # should be 0 (North)
# print("(0,0) to (0,1):", get_needed_heading((0,0), (0,1)))  # should be 1 (East)
# print("(0,1) to (0,0):", get_needed_heading((0,1), (0,0)))  # should be 3 (West)
# print()

# TODO: Uncomment and test count_right_turns
# print("===== Testing count_right_turns =====")
# print("Heading N, need N:", count_right_turns(0, 0))  # should be 0
# print("Heading N, need E:", count_right_turns(0, 1))  # should be 1
# print("Heading N, need S:", count_right_turns(0, 2))  # should be 2
# print("Heading N, need W:", count_right_turns(0, 3))  # should be 3
# print("Heading E, need S:", count_right_turns(1, 2))  # should be 1
# print("Heading W, need N:", count_right_turns(3, 0))  # should be 1
