# Lesson 8: Implementing the Navigator Class - STARTER
# The Navigator class drives the robot along a Manhattan path
# using LineTrack for line following and turning.
#
# Team: ________________________
# Date: ________________________
#
# The Navigator needs to:
#   1. Know its current position and heading (0=N, 1=E, 2=S, 3=W)
#   2. Figure out which heading is needed for the next step
#   3. Turn right the correct number of times using LineTrack
#   4. Follow the line to the next intersection
#   5. Repeat for every step in the path

from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board
import time


# ===== LineSensor Class (from Module 2) =====

class LineSensor:
    def __init__(self):
        self.reflectance = Reflectance.get_default_reflectance()
        self.threshold = 0.5

    def get_left(self):
        return self.reflectance.get_left()

    def get_right(self):
        return self.reflectance.get_right()

    def get_error(self):
        return self.get_left() - self.get_right()

    def is_at_cross(self):
        return self.get_left() > self.threshold and self.get_right() > self.threshold

    def is_off_line(self):
        return self.get_left() < self.threshold and self.get_right() < self.threshold


# ===== LineTrack Class (from Module 2) =====

class LineTrack:
    def __init__(self):
        self.sensor = LineSensor()
        self.drivetrain = DifferentialDrive.get_default_differential_drive()
        self.base_effort = 0.4
        self.Kp = 0.5

    def track_until_cross(self):
        while not self.sensor.is_at_cross():
            error = self.sensor.get_error()
            correction = error * self.Kp
            self.drivetrain.arcade(self.base_effort, -correction)
        self.drivetrain.stop()

    def turn_right(self):
        self.drivetrain.arcade(self.base_effort, 0)
        time.sleep(0.3)
        self.drivetrain.arcade(0, 0.3)
        time.sleep(0.3)
        while self.sensor.is_off_line():
            pass
        self.drivetrain.stop()

    def turn_left(self):
        self.drivetrain.arcade(self.base_effort, 0)
        time.sleep(0.3)
        self.drivetrain.arcade(0, -0.3)
        time.sleep(0.3)
        while self.sensor.is_off_line():
            pass
        self.drivetrain.stop()


# ===== Manhattan Class (complete — from Lesson 5) =====

class Manhattan:

    def __init__(self, start):
        self.position = start

    def compute_path(self, destination):
        path = []

        current_row, current_col = self.position
        dest_row, dest_col = destination

        while current_row < dest_row:
            current_row = current_row + 1
            path.append((current_row, current_col))

        while current_row > dest_row:
            current_row = current_row - 1
            path.append((current_row, current_col))

        while current_col < dest_col:
            current_col = current_col + 1
            path.append((current_row, current_col))

        while current_col > dest_col:
            current_col = current_col - 1
            path.append((current_row, current_col))

        return path


# ===== Navigator Class (YOU COMPLETE THIS) =====
# Headings: 0 = North, 1 = East, 2 = South, 3 = West

HEADING_NAMES = ["N", "E", "S", "W"]


class Navigator:

    def __init__(self, start, heading):
        """Create a Navigator at the given start position and heading.

        start:   a (row, col) tuple
        heading: 0, 1, 2, or 3 (N, E, S, W)

        Attributes to set:
          - self.position = the starting position
          - self.heading  = the starting heading number
          - self.line_track = LineTrack()
        """
        # TODO: Set self.position to start
        # TODO: Set self.heading to heading
        # TODO: Set self.line_track to a new LineTrack object
        pass

    def desired_heading(self, next_pos):
        """Determine heading number to move from current position to next_pos.

        next_pos: a (row, col) tuple one step away from self.position

        Returns: 0, 1, 2, or 3

        Logic:
          - row_diff = next_pos[0] - self.position[0]
          - col_diff = next_pos[1] - self.position[1]
          - row_diff == -1 --> 0 (North)
          - col_diff == 1  --> 1 (East)
          - row_diff == 1  --> 2 (South)
          - col_diff == -1 --> 3 (West)
        """
        # TODO: Calculate row_diff and col_diff
        # TODO: Return the correct heading number based on the diff values
        pass

    def turn_to(self, desired):
        """Turn the robot to face the needed heading.

        desired: 0, 1, 2, or 3

        Logic:
          - While self.heading != desired:
            - Call self.line_track.turn_right() to turn right once
            - Add 1 to self.heading
            - If self.heading == 4, reset it to 0

        Examples:
          - Heading 0, need 1: one right turn (0 -> 1)
          - Heading 0, need 2: two right turns (0 -> 1 -> 2)
          - Heading 3, need 0: one right turn (3 -> 0, wraps around)
        """
        # TODO: Use a while loop that keeps turning right
        #       until self.heading equals desired
        # TODO: Inside the loop: turn right, add 1 to heading,
        #       reset to 0 if heading reaches 4
        pass

    def drive_path(self, path):
        """Drive the robot along the given path.

        path: a list of (row, col) tuples from Manhattan.compute_path()
              (does not include the starting position)

        Logic:
          - Loop through each position in the path
          - For each step:
            1. Determine the needed heading using desired_heading()
            2. If already facing the right way, clear the intersection: straight(8)
            3. Turn to face the right direction using turn_to()
            4. Follow the line to the next intersection: track_until_cross()
            5. Update self.position to the new position
        """
        # TODO: Write the for loop (for next_pos in path:)
        # TODO: For each step, get heading, clear if straight, turn, track, update
        pass


# ===== Test Your Code =====

# Step 1: Test Manhattan path computation
manhattan = Manhattan((0, 0))
path = manhattan.compute_path((2, 2))
print("Path from (0,0) to (2,2):", path)
print()

# Step 2: Create Navigator and test
# TODO: Uncomment these lines after completing the Navigator class
# navigator = Navigator((0, 0), 0)
# print("Navigator position:", navigator.position)
# print("Navigator heading:", HEADING_NAMES[navigator.heading])
# print()

# Step 3: Test the full integration
# TODO: Uncomment after testing steps 1 and 2
# print("--- Driving path ---")
# navigator.drive_path(path)
# print("Final position:", navigator.position)
# print("Final heading:", HEADING_NAMES[navigator.heading])
