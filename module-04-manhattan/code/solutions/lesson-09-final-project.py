# Lesson 9: Final Project - SOLUTION
# Multi-destination grid navigation with the XRP robot.

from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board


# ===== Manhattan Class =====

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


# ===== Navigator Class =====

class Navigator:

    def __init__(self, start, heading):
        """Create a Navigator at the given start position and heading."""
        self.position = start
        self.heading = heading
        self.drivetrain = DifferentialDrive.get_default_differential_drive()

    def get_needed_direction(self, next_pos):
        """Determine direction (N/S/E/W) to move from current position to next_pos."""
        row_diff = next_pos[0] - self.position[0]
        col_diff = next_pos[1] - self.position[1]
        if row_diff == 1:
            return "S"
        elif row_diff == -1:
            return "N"
        elif col_diff == 1:
            return "E"
        elif col_diff == -1:
            return "W"

    def turn_to(self, direction):
        """Turn the robot to face the given direction."""
        right_turns = {"N": "E", "E": "S", "S": "W", "W": "N"}
        left_turns = {"N": "W", "W": "S", "S": "E", "E": "N"}

        if self.heading == direction:
            pass
        elif right_turns[self.heading] == direction:
            self.drivetrain.turn(90)
            self.heading = direction
        elif left_turns[self.heading] == direction:
            self.drivetrain.turn(-90)
            self.heading = direction
        else:
            self.drivetrain.turn(180)
            self.heading = direction

    def drive_path(self, path):
        """Drive the robot along the given path."""
        for i in range(1, len(path)):
            next_pos = path[i]
            direction = self.get_needed_direction(next_pos)
            self.turn_to(direction)
            self.drivetrain.straight(20)
            self.position = next_pos


# ===== Main Program =====

board = Board.get_default_board()

manhattan = Manhattan((0, 0))
navigator = Navigator((0, 0), "N")

# Four destinations that form a tour of the grid
destinations = [(3, 0), (3, 3), (0, 3), (0, 0)]

print("=== XRP Grid Navigation: Final Project ===")
print("Starting at:", manhattan.position)
print("Heading:", navigator.heading)
print("Destinations:", destinations)
print()

# Wait for button press to start
print("Press the button to begin navigation...")
board.wait_for_button()
print()

# Navigate to each destination
for dest in destinations:
    print("--- Navigating to", dest, "---")

    # Compute the path from current position to this destination
    path = manhattan.compute_path(dest)
    print("Path:", path)
    print("Steps:", len(path) - 1)

    # Drive the computed path
    navigator.drive_path(path)

    # Update Manhattan's position for the next leg
    manhattan.position = navigator.position

    print("Arrived at:", navigator.position)
    print("Heading:", navigator.heading)
    print()

print("=== All destinations reached! ===")
print("Final position:", navigator.position)
print("Total destinations visited:", len(destinations))
