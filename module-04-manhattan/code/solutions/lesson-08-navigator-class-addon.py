# Lesson 8 Optional Extension: The Navigator Class
# Classes-track reference: the driving functions from
# lesson-08-driving-functions.py, repackaged as a Navigator class
# that composes a LineTrack object. Robot behavior is identical.

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

    def is_either_on_line(self):
        return self.get_left() > self.threshold or self.get_right() > self.threshold


class LineTrack:
    def __init__(self):
        self.sensor = LineSensor()
        self.drivetrain = DifferentialDrive.get_default_differential_drive()
        self.base_effort = 0.4
        self.kp = 0.5
        self.turn_effort = 0.25

    def drive_past_intersection(self):
        # The sensors stop ON the cross, but the wheels are 8.75 cm behind
        # them. Drive that far so the axle is over the intersection.
        self.drivetrain.straight(8.75, 0.5)

    def track_to_intersection(self):
        while not self.sensor.is_at_cross():
            error = self.sensor.get_error()
            left = self.base_effort - error * self.kp
            right = self.base_effort + error * self.kp
            self.drivetrain.set_effort(left, right)
        self.drivetrain.stop()

    def turn_clockwise(self):
        # A blind turn first, far enough to get both sensors off the line we
        # were on. Then keep turning until a sensor finds the cross street.
        # No timing involved: the sensors say when the turn is done.
        self.drivetrain.turn(-60, self.turn_effort)
        self.drivetrain.arcade(0, -self.turn_effort)
        while not self.sensor.is_either_on_line():
            pass
        self.drivetrain.stop()

    def turn_counterclockwise(self):
        self.drivetrain.turn(60, self.turn_effort)
        self.drivetrain.arcade(0, self.turn_effort)
        while not self.sensor.is_either_on_line():
            pass
        self.drivetrain.stop()


class Manhattan:
    """The Lesson 5 planner as a class.

    It holds NO state: compute_path() is told the robot's position every
    time, and the Navigator is the only thing that tracks where the robot
    is. Manhattan is a class only so that it has the same shape as the
    Module 5 and 6 planners (BFS, Dijkstra) -- then one main program and one test
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
        self.heading = heading  # 0=N, 1=E, 2=S, 3=W
        self.line_track = LineTrack()

    def desired_heading(self, next_pos):
        row_diff = next_pos[0] - self.position[0]
        col_diff = next_pos[1] - self.position[1]
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
        raise ValueError(str(self.position) + " and " + str(next_pos) + " are not neighbors")

    def turn_to(self, desired):
        """Turn to face desired the short way round."""
        # Quarter turns clockwise to get there: 0 = none, 1 = right,
        # 2 = around, 3 = left (one counterclockwise beats three clockwise).
        turns = (desired - self.heading) % 4
        if turns == 3:
            self.line_track.turn_counterclockwise()
        else:
            for i in range(turns):
                self.line_track.turn_clockwise()
        self.heading = desired

    def drive_path(self, path):
        for next_pos in path:
            needed = self.desired_heading(next_pos)
            self.turn_to(needed)
            self.line_track.track_to_intersection()
            self.line_track.drive_past_intersection()
            self.position = next_pos


# ===== Test the Integration =====
# The Navigator owns position and heading. The planner is TOLD the position.

print("=== Test 1: Manhattan Paths ===")
manhattan = Manhattan()
path = manhattan.compute_path((0, 0), (2, 2))
print("Path from (0,0) to (2,2):", path)
print()

print("=== Test 2: Navigator Setup ===")
navigator = Navigator((0, 0), 0)
print("Position:", navigator.position)
print("Heading:", HEADING_NAMES[navigator.heading])
print()

print("=== Test 3: Drive (0,0) to (2,2) ===")
path = manhattan.compute_path(navigator.position, (2, 2))
print("Planned path:", path)
navigator.drive_path(path)
print("Final position:", navigator.position)
print("Final heading:", HEADING_NAMES[navigator.heading])
print()

print("=== Test 4: Drive on to (0,3) ===")
# No "sync" step: the planner asks the Navigator where the robot is.
path2 = manhattan.compute_path(navigator.position, (0, 3))
print("Planned path:", path2)
navigator.drive_path(path2)
print("Final position:", navigator.position)
print("Final heading:", HEADING_NAMES[navigator.heading])
