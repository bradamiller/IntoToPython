# Lesson 7: The Challenge of Turning - SOLUTION
# Headings are numbers: 0 = North, 1 = East, 2 = South, 3 = West.
# Quarter turns clockwise from heading to desired: (desired - heading) % 4.
# Three clockwise is the same as one counterclockwise, so turn_to() in
# Lesson 8 turns the short way round.
#
# No robot needed: this file only prints.

HEADING_NAMES = ["N", "E", "S", "W"]


def desired_heading(position, next_pos):
    row_diff = next_pos[0] - position[0]
    col_diff = next_pos[1] - position[1]
    if col_diff == 0 and row_diff == -1:
        return 0  # North
    if row_diff == 0 and col_diff == 1:
        return 1  # East
    if col_diff == 0 and row_diff == 1:
        return 2  # South
    if row_diff == 0 and col_diff == -1:
        return 3  # West
    # Not one step apart: say so now, where the problem is found,
    # instead of handing back None and letting turn_to() go wrong later.
    raise ValueError(str(position) + " and " + str(next_pos) + " are not neighbors")


def turns_needed(heading, desired):
    """Quarter turns clockwise to get from heading to desired (0, 1, 2 or 3)."""
    return (desired - heading) % 4


def describe_turn(turns):
    if turns == 0:
        return "no turn"
    if turns == 3:
        return "1 turn counterclockwise"
    return str(turns) + " turn(s) clockwise"


# ===== Heading from coordinates =====
print("=== Heading from Coordinates ===")
test_pairs = [((0, 0), (1, 0)), ((1, 0), (0, 0)), ((0, 0), (0, 1)), ((0, 1), (0, 0))]
for position, next_pos in test_pairs:
    h = desired_heading(position, next_pos)
    print("  " + str(position) + " to " + str(next_pos) + ": " + str(h) + " (" + HEADING_NAMES[h] + ")")

# ===== The % 4 table =====
print("\n=== Quarter turns: (desired - heading) % 4 ===")
print("  heading desired  diff  %4  meaning")
for heading, desired in [(0, 1), (2, 1), (1, 1), (3, 0), (0, 2)]:
    diff = desired - heading
    turns = turns_needed(heading, desired)
    print("     " + HEADING_NAMES[heading] + "       " + HEADING_NAMES[desired] + "     " + str(diff).rjust(2)
          + "    " + str(turns) + "   " + describe_turn(turns))

# ===== Full path trace =====
# The path from compute_manhattan_path does not include the start,
# so position and heading are tracked separately -- as drive_path will.
print("\n=== Full Path Trace ===")
path = [(1, 0), (2, 0), (2, 1), (2, 2)]
position = (0, 0)
heading = 0  # North
for next_pos in path:
    needed = desired_heading(position, next_pos)
    turns = turns_needed(heading, needed)
    print("  At " + str(position) + " heading " + HEADING_NAMES[heading] + ", need "
          + HEADING_NAMES[needed] + ": " + describe_turn(turns))
    heading = needed
    position = next_pos
print("  Arrived at " + str(position) + " facing " + HEADING_NAMES[heading])

# ===== Asking something it cannot answer =====
# Uncomment the next line to see the program stop with the message
#   ValueError: (1, 1) and (2, 2) are not neighbors
# -- on THIS line, naming both positions, instead of somewhere later.
# desired_heading((1, 1), (2, 2))
