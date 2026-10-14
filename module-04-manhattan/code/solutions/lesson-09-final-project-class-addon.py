# Lesson 9 Optional Extension: Final Project with Classes
# Classes-track reference: combines the Manhattan and Navigator classes
# from lesson-05-manhattan-class-addon.py and
# lesson-08-navigator-class-addon.py. Robot behavior is identical to
# lesson-09-final-project.py.

from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board


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


class LineTrack:
    def __init__(self):
        self.sensor = LineSensor()
        self.drivetrain = DifferentialDrive.get_default_differential_drive()
        self.base_effort = 0.4
        self.kp = 0.5

    def clear_intersection(self):
        self.drivetrain.straight(8, 0.5)

    def track_until_cross(self):
        while not self.sensor.is_at_cross():
            error = self.sensor.get_error()
            left = self.base_effort - error * self.kp
            right = self.base_effort + error * self.kp
            self.drivetrain.set_effort(left, right)
        self.drivetrain.stop()

    def turn_right(self):
        self.clear_intersection()
        self.drivetrain.set_effort(0.3, -0.3)
        while self.sensor.is_off_line():
            pass
        self.drivetrain.stop()


class Manhattan:
    """The Lesson 5 planner as a class.

    It holds NO state: compute_path() is told the robot's position every
    time, and the Navigator is the only thing that tracks where the robot
    is. Manhattan is a class only so that it has the same shape as the
    Module 5 planners (BFS, Dijkstra) -- then one main program and one test
    harness work with any of them by changing one name.
    """

    def __init__(self):
        pass        # nothing to set up

    def compute_path(self, position, destination):
        path = []
        current_row, current_col = position
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


HEADING_NAMES = ["N", "E", "S", "W"]


class Navigator:

    def __init__(self, start, heading):
        self.position = start
        self.heading = heading
        self.line_track = LineTrack()

    def desired_heading(self, next_pos):
        row_diff = next_pos[0] - self.position[0]
        col_diff = next_pos[1] - self.position[1]
        if row_diff == -1:
            return 0  # North
        elif col_diff == 1:
            return 1  # East
        elif row_diff == 1:
            return 2  # South
        elif col_diff == -1:
            return 3  # West

    def turn_to(self, desired):
        while self.heading != desired:
            self.line_track.turn_right()
            self.heading = self.heading + 1
            if self.heading == 4:
                self.heading = 0

    def drive_path(self, path):
        for next_pos in path:
            needed = self.desired_heading(next_pos)
            if self.heading == needed:
                self.line_track.clear_intersection()
            self.turn_to(needed)
            self.line_track.track_until_cross()
            self.position = next_pos


# ===== Main Program =====

board = Board.get_default_board()

manhattan = Manhattan()
navigator = Navigator((0, 0), 0)  # Start at (0,0) heading North

# Four destinations that form a tour of the grid
destinations = [(3, 0), (3, 3), (0, 3), (0, 0)]

print("=== XRP Grid Navigation: Final Project ===")
print("Starting at:", navigator.position)
print("Heading:", HEADING_NAMES[navigator.heading])
print("Destinations:", destinations)
# Print the first leg's plan BEFORE the button press -- read it before the
# robot moves. This is the Lesson 6 paper test, built into every run.
print("Planned path for leg 1:", manhattan.compute_path(navigator.position, destinations[0]))
print()

print("Press the button to begin navigation...")
board.wait_for_button()
print()

for dest in destinations:
    print("--- Navigating to", dest, "---")

    # The planner is told where the robot is; the Navigator is the only
    # thing that tracks it, so there is nothing to keep "in sync".
    path = manhattan.compute_path(navigator.position, dest)
    print("Path:", path)
    print("Steps:", len(path))

    navigator.drive_path(path)

    print("Arrived at:", navigator.position)
    print("Heading:", HEADING_NAMES[navigator.heading])
    print()

print("=== All destinations reached! ===")
print("Final position:", navigator.position)
print("Total destinations visited:", len(destinations))
