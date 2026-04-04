# Lesson 7: The Challenge of Turning - SOLUTION
# Headings are numbers: 0 = North, 1 = East, 2 = South, 3 = West
# Turning uses modular arithmetic: (needed - current) % 4 = right turns needed

HEADING_NAMES = ["N", "E", "S", "W"]


def get_needed_heading(current, next_pos):
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


def count_right_turns(current_heading, needed_heading):
    return (needed_heading - current_heading) % 4


# Test: Heading from coordinates
print("=== Heading from Coordinates ===")
test_pairs = [((0, 0), (1, 0)), ((1, 0), (0, 0)), ((0, 0), (0, 1)), ((0, 1), (0, 0))]
for current, next_pos in test_pairs:
    h = get_needed_heading(current, next_pos)
    print(f"  {current} to {next_pos}: {h} ({HEADING_NAMES[h]})")

# Test: Count right turns
print("\n=== Right Turns Needed ===")
turn_tests = [(0, 1), (0, 2), (0, 3), (1, 1), (2, 0), (3, 1)]
for current_h, needed_h in turn_tests:
    turns = count_right_turns(current_h, needed_h)
    print(f"  Heading {HEADING_NAMES[current_h]}, need {HEADING_NAMES[needed_h]}"
          f" --> {turns} right turn(s)")

# Test: Full path trace
print("\n=== Full Path Trace ===")
path = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
heading = 0  # North
for i in range(len(path) - 1):
    current = path[i]
    next_pos = path[i + 1]
    needed = get_needed_heading(current, next_pos)
    turns = count_right_turns(heading, needed)
    print(f"  At {current} heading {HEADING_NAMES[heading]}, need {HEADING_NAMES[needed]}"
          f" --> {turns} right turn(s)")
    heading = needed
    print(f"    Now heading {HEADING_NAMES[heading]}, drive to {next_pos}")
