# Lesson 7: Turning — Figuring Out Which Way to Face
# Before the robot can drive, it needs to face the right direction.
#
# Team: ________________________
# Date: ________________________
#
# Directions on our grid:
#   NORTH = moving to a smaller row     (row decreases)
#   SOUTH = moving to a larger row      (row increases)
#   EAST  = moving to a larger column   (col increases)
#   WEST  = moving to a smaller column  (col decreases)
#
# The robot can face: "N", "S", "E", "W"
# Turns: "LEFT", "RIGHT", "REVERSE", "NONE"
#
# Turning chart (from current facing -> needed direction):
#   Same direction        -> "NONE"
#   90 degrees clockwise  -> "RIGHT"
#   90 degrees counter-cw -> "LEFT"
#   Opposite direction    -> "REVERSE"


# ===== PART 1: get_needed_direction =====
# Given the current position and the next position, figure out
# which direction the robot needs to face.

def get_needed_direction(current, next_pos):
    """Return "N", "S", "E", or "W" based on how next_pos differs from current.

    current:  a (row, col) tuple
    next_pos: a (row, col) tuple one step away
    """
    # TODO: Compare the rows and columns to determine direction
    # If next_pos row < current row, return "N" (moving north)
    # If next_pos row > current row, return "S" (moving south)
    # If next_pos col > current col, return "E" (moving east)
    # If next_pos col < current col, return "W" (moving west)
    pass


# ===== PART 2: get_turn =====
# Given the direction the robot is currently facing and the
# direction it needs to face, return the turn needed.

def get_turn(facing, needed):
    """Return "NONE", "LEFT", "RIGHT", or "REVERSE".

    facing: current direction ("N", "S", "E", or "W")
    needed: direction robot needs to face ("N", "S", "E", or "W")
    """
    # TODO: If facing and needed are the same, return "NONE"

    # TODO: Define the opposites — N<->S and E<->W
    # If needed is the opposite of facing, return "REVERSE"

    # TODO: Define right turns
    # N -> right turn -> E
    # E -> right turn -> S
    # S -> right turn -> W
    # W -> right turn -> N
    # Hint: use a dictionary: right_turns = {"N": "E", "E": "S", ...}
    # If needed equals right_turns[facing], return "RIGHT"

    # TODO: Otherwise, return "LEFT"

    pass


# ===== PART 3: Test Your Functions =====

# TODO: Uncomment and test get_needed_direction
# print("===== Testing get_needed_direction =====")
# print("(0,0) to (1,0):", get_needed_direction((0,0), (1,0)))  # should be "S"
# print("(1,0) to (0,0):", get_needed_direction((1,0), (0,0)))  # should be "N"
# print("(0,0) to (0,1):", get_needed_direction((0,0), (0,1)))  # should be "E"
# print("(0,1) to (0,0):", get_needed_direction((0,1), (0,0)))  # should be "W"
# print()

# TODO: Uncomment and test get_turn
# print("===== Testing get_turn =====")
# print("Facing N, need N:", get_turn("N", "N"))  # should be "NONE"
# print("Facing N, need S:", get_turn("N", "S"))  # should be "REVERSE"
# print("Facing N, need E:", get_turn("N", "E"))  # should be "RIGHT"
# print("Facing N, need W:", get_turn("N", "W"))  # should be "LEFT"
# print("Facing E, need S:", get_turn("E", "S"))  # should be "RIGHT"
# print("Facing W, need N:", get_turn("W", "N"))  # should be "RIGHT"
