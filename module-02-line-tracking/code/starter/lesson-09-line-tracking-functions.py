# Lesson 9: Line-Tracking Functions
# A second toolkit of functions that uses the sensor functions from Lesson 8
# for line following and turning.

from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board

reflectance = Reflectance.get_default_reflectance()
THRESHOLD = 0.5


def get_left():
    return reflectance.get_left()


def get_right():
    return reflectance.get_right()


def get_error():
    return get_left() - get_right()


def is_at_cross():
    return get_left() > THRESHOLD and get_right() > THRESHOLD


def is_either_on_line():
    return get_left() > THRESHOLD or get_right() > THRESHOLD


drivetrain = DifferentialDrive.get_default_differential_drive()
BASE_EFFORT = 0.4
KP = 0.5


def drive_past_intersection():
    # The sensors stop ON the cross, but the wheels are 8.75 cm behind them.
    # Drive that far so the axle is over the intersection: a turn then pivots
    # on it, and the next track_to_intersection() does not see this same cross.
    drivetrain.straight(8.75, 0.5)


# TODO: Write track_to_intersection()
# Follow the line until an intersection is detected
# Use a while loop with is_at_cross()
# Inside the loop: calculate error, set motor efforts with drivetrain.set_effort()
# After the loop: stop the robot
# def track_to_intersection():
#     ???

# TODO: Write turn_clockwise()
# The robot is sitting with its wheels over an intersection (someone called
# drive_past_intersection() after the last track). To turn 90 degrees:
# 1. Make a blind turn to get BOTH sensors off the line you were following:
#        drivetrain.turn(-60, TURN_EFFORT)      (negative = clockwise)
# 2. Keep rotating in place:  drivetrain.arcade(0, -TURN_EFFORT)
# 3. Wait until a sensor finds the cross street:  while not is_either_on_line(): pass
# 4. Stop the robot
# No time.sleep() anywhere -- the sensors decide when the turn is done.
# def turn_clockwise():
#     ???

# TODO: Write turn_counterclockwise() -- the same with the signs flipped
# (turn(60, ...) and arcade(0, TURN_EFFORT))
# def turn_counterclockwise():
#     ???


# --- Test Program ---
board = Board.get_default_board()

board.wait_for_button()

print("Following line to cross...")
track_to_intersection()
drive_past_intersection()      # wheels over the intersection before turning
print("Cross found! Turning clockwise...")
turn_clockwise()
print("Following line again...")
track_to_intersection()
print("Done!")
