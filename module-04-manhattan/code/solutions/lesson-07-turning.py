# Lesson 7: The Challenge of Turning - SOLUTION

right_turns = {"N": "E", "E": "S", "S": "W", "W": "N"}
left_turns = {"N": "W", "W": "S", "S": "E", "E": "N"}

def get_direction(current, next_pos):
    row_diff = next_pos[0] - current[0]
    col_diff = next_pos[1] - current[1]
    if row_diff == 1:
        return "S"
    elif row_diff == -1:
        return "N"
    elif col_diff == 1:
        return "E"
    elif col_diff == -1:
        return "W"

def decide_turn(heading, needed):
    if heading == needed:
        return "none"
    elif right_turns[heading] == needed:
        return "right 90"
    elif left_turns[heading] == needed:
        return "left 90"
    else:
        return "180"

# Test: Direction from coordinates
print("=== Direction from Coordinates ===")
test_pairs = [((0,0), (1,0)), ((1,0), (0,0)), ((0,0), (0,1)), ((0,1), (0,0))]
for current, next_pos in test_pairs:
    print(f"  {current} to {next_pos}: {get_direction(current, next_pos)}")

# Test: Turn decisions
print("\n=== Turn Decisions ===")
turn_tests = [("N","E"), ("N","S"), ("E","E"), ("W","N"), ("S","W")]
for heading, needed in turn_tests:
    print(f"  Heading: {heading}, Need: {needed} --> {decide_turn(heading, needed)}")

# Test: Full path trace
print("\n=== Full Path Trace ===")
path = [(0,0), (1,0), (2,0), (2,1), (2,2)]
heading = "N"
for i in range(len(path) - 1):
    current = path[i]
    next_pos = path[i + 1]
    needed = get_direction(current, next_pos)
    turn = decide_turn(heading, needed)
    print(f"  At {current} heading {heading}, need {needed} --> {turn}")
    if turn == "right 90":
        heading = right_turns[heading]
    elif turn == "left 90":
        heading = left_turns[heading]
    elif turn == "180":
        opposite = {"N":"S", "S":"N", "E":"W", "W":"E"}
        heading = opposite[heading]
    print(f"    Now heading {heading}, drive to {next_pos}")
