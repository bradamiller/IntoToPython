# Lesson 8: Implementing the Navigator Class - STARTER
# The Navigator class drives the robot along a Manhattan path.
#
# Team: ________________________
# Date: ________________________
#
# The Navigator needs to:
#   1. Know its current position and heading
#   2. Figure out which direction to go for the next step
#   3. Turn the robot to face that direction
#   4. Drive forward one grid cell
#   5. Repeat for every step in the path

from XRPLib.differential_drive import DifferentialDrive


# ===== Manhattan Class (complete — from Lesson 5) =====

class Manhattan:

    def __init__(self, start):
        """Create a Manhattan navigator starting at the given position."""
        self.position = start

    def compute_path(self, destination):
        """Compute a Manhattan path from current position to destination.
        Returns a list of (row, col) tuples."""
        path = [self.position]

        current_row = self.position[0]
        current_col = self.position[1]
        dest_row = destination[0]
        dest_col = destination[1]

        if dest_row > current_row:
            row_step = 1
        else:
            row_step = -1

        if dest_col > current_col:
            col_step = 1
        else:
            col_step = -1

        while current_row != dest_row:
            current_row = current_row + row_step
            path.append((current_row, current_col))

        while current_col != dest_col:
            current_col = current_col + col_step
            path.append((current_row, current_col))

        return path


# ===== Navigator Class (YOU COMPLETE THIS) =====

class Navigator:

    def __init__(self, start, heading):
        """Create a Navigator at the given start position and heading.

        start:   a (row, col) tuple
        heading: "N", "S", "E", or "W"

        Attributes to set:
          - self.position = the starting position
          - self.heading  = the starting heading
          - self.drivetrain = DifferentialDrive.get_default_differential_drive()
        """
        # TODO: Set self.position to start
        # TODO: Set self.heading to heading
        # TODO: Set self.drivetrain using DifferentialDrive
        pass

    def get_needed_direction(self, next_pos):
        """Determine direction (N/S/E/W) to move from current position to next_pos.

        next_pos: a (row, col) tuple one step away from self.position

        Returns: "N", "S", "E", or "W"

        Logic:
          - row_diff = next_pos[0] - self.position[0]
          - col_diff = next_pos[1] - self.position[1]
          - row_diff == 1  --> "S"
          - row_diff == -1 --> "N"
          - col_diff == 1  --> "E"
          - col_diff == -1 --> "W"
        """
        # TODO: Calculate row_diff and col_diff
        # TODO: Return the correct direction based on the diff values
        pass

    def turn_to(self, direction):
        """Turn the robot to face the given direction.

        direction: "N", "S", "E", or "W"

        Logic:
          - If already facing the right direction, do nothing
          - If direction is a right turn from current heading, turn 90 degrees
          - If direction is a left turn from current heading, turn -90 degrees
          - Otherwise (opposite direction), turn 180 degrees
          - Always update self.heading after turning

        Hints:
          right_turns = {"N": "E", "E": "S", "S": "W", "W": "N"}
          left_turns  = {"N": "W", "W": "S", "S": "E", "E": "N"}
          self.drivetrain.turn(90)   # right turn
          self.drivetrain.turn(-90)  # left turn
          self.drivetrain.turn(180)  # U-turn
        """
        # TODO: Define right_turns and left_turns dictionaries
        # TODO: Check if heading == direction (no turn needed)
        # TODO: Check if right_turns[self.heading] == direction (turn right)
        # TODO: Check if left_turns[self.heading] == direction (turn left)
        # TODO: Otherwise turn 180
        # TODO: Update self.heading = direction after any turn
        pass

    def drive_path(self, path):
        """Drive the robot along the given path.

        path: a list of (row, col) tuples from Manhattan.compute_path()

        Logic:
          - Loop from index 1 to the end of the path (skip index 0, we are already there)
          - For each step:
            1. Get the next position from the path
            2. Determine the needed direction using get_needed_direction()
            3. Turn to face that direction using turn_to()
            4. Drive forward one cell using self.drivetrain.straight(20)
            5. Update self.position to the new position
        """
        # TODO: Write the for loop
        # TODO: For each step, get direction, turn, drive, update position
        pass


# ===== Test Your Code =====

# Step 1: Test Manhattan path computation
manhattan = Manhattan((0, 0))
path = manhattan.compute_path((2, 2))
print("Path from (0,0) to (2,2):", path)
print()

# Step 2: Create Navigator and test
# TODO: Uncomment these lines after completing the Navigator class
# navigator = Navigator((0, 0), "N")
# print("Navigator position:", navigator.position)
# print("Navigator heading:", navigator.heading)
# print()

# Step 3: Test the full integration
# TODO: Uncomment after testing steps 1 and 2
# print("--- Driving path ---")
# navigator.drive_path(path)
# print("Final position:", navigator.position)
# print("Final heading:", navigator.heading)
