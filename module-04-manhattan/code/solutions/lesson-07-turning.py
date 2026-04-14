# Lesson 7: The Challenge of Turning - SOLUTION
# Headings are numbers: 0 = North, 1 = East, 2 = South, 3 = West
# To turn: keep turning right until the current heading matches the needed heading

HEADING_NAMES = ["N", "E", "S", "W"]


def desired_heading(current, next_pos):
    row_diff = next_pos[0] - current[0]
    col_diff = next_pos[1] - current[1]
    if row_diff == -1:
        return 0  # North
    elif col_diff == 1:
        return 1  # East
    elif row_diff == 1:
        return 2  # South
    elif col_diff == -1:
        return 3  # West


# Test: Heading from coordinates
print("=== Heading from Coordinates ===")
test_pairs = [((0, 0), (1, 0)), ((1, 0), (0, 0)), ((0, 0), (0, 1)), ((0, 1), (0, 0))]
for current, next_pos in test_pairs:
    h = desired_heading(current, next_pos)
    print(f"  {current} to {next_pos}: {h} ({HEADING_NAMES[h]})")

# Test: Full path trace
# The path from compute_path does not include the start,
# so we track position separately — just like Navigator will.
print("\n=== Full Path Trace ===")
path = [(1, 0), (2, 0), (2, 1), (2, 2)]
position = (0, 0)
heading = 0  # North
for next_pos in path:
    needed = desired_heading(position, next_pos)
    print(f"  At {position} heading {HEADING_NAMES[heading]}, need {HEADING_NAMES[needed]}")
    heading = needed
    position = next_pos
    print(f"    Now heading {HEADING_NAMES[heading]}, drive to {position}")
