# Lesson 8: Implementing the Navigator Class - SOLUTION
# The Navigator class drives the robot along a Manhattan path.

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


# ===== Navigator Class (SOLUTION) =====

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
            pass  # Already facing the right way
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


# ===== Test the Integration =====

# Test 1: Manhattan path computation
print("=== Test 1: Manhattan Paths ===")
manhattan = Manhattan((0, 0))
path = manhattan.compute_path((2, 2))
print("Path from (0,0) to (2,2):", path)
print("Steps:", len(path) - 1)
print()

# Test 2: Navigator creation
print("=== Test 2: Navigator Setup ===")
navigator = Navigator((0, 0), "N")
print("Position:", navigator.position)
print("Heading:", navigator.heading)
print()

# Test 3: Drive one path
print("=== Test 3: Drive (0,0) to (2,2) ===")
path = manhattan.compute_path((2, 2))
print("Path:", path)
navigator.drive_path(path)
print("Final position:", navigator.position)
print("Final heading:", navigator.heading)
print()

# Test 4: Drive a second path (continuing from where we are)
print("=== Test 4: Drive (2,2) to (0,3) ===")
manhattan.position = navigator.position
path2 = manhattan.compute_path((0, 3))
print("Path:", path2)
navigator.drive_path(path2)
print("Final position:", navigator.position)
print("Final heading:", navigator.heading)
print()

# Test 5: Multi-destination loop
print("=== Test 5: Multi-Destination ===")
manhattan = Manhattan((0, 0))
navigator = Navigator((0, 0), "N")
destinations = [(2, 0), (2, 3), (0, 3)]

for dest in destinations:
    print("--- Navigating to", dest, "---")
    path = manhattan.compute_path(dest)
    print("Path:", path)
    navigator.drive_path(path)
    manhattan.position = navigator.position
    print("Arrived at:", navigator.position, "heading", navigator.heading)
    print()

print("=== All tests complete ===")
