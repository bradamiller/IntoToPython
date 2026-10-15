# Lesson 2: Driving Multiple Intersections - SOLUTION
# Drive past intersections and count them using a for loop

from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board

# ===== SENSOR TOOLKIT (from Module 2 Lesson 8) =====
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


# ===== DRIVING TOOLKIT (from Module 2 Lesson 9) =====
drivetrain = DifferentialDrive.get_default_differential_drive()
BASE_EFFORT = 0.4
KP = 0.5
TURN_EFFORT = 0.25

def drive_past_intersection():
    # The sensors stop ON the cross, but the wheels are 8.75 cm behind them.
    # Drive that far so the axle is over the intersection: a turn then pivots
    # on it, and the next track_to_intersection() does not see this same cross.
    drivetrain.straight(8.75, 0.5)

def track_to_intersection():
    while not is_at_cross():
        error = get_error()
        left = BASE_EFFORT - error * KP
        right = BASE_EFFORT + error * KP
        drivetrain.set_effort(left, right)
    drivetrain.stop()

def turn_clockwise():
    # A blind turn first, far enough to get both sensors off the line we were
    # on. Then keep turning until a sensor finds the cross street. No timing
    # involved: the sensors say when the turn is done.
    drivetrain.turn(-60, TURN_EFFORT)
    drivetrain.arcade(0, -TURN_EFFORT)
    while not is_either_on_line():
        pass
    drivetrain.stop()

def turn_counterclockwise():
    drivetrain.turn(60, TURN_EFFORT)
    drivetrain.arcade(0, TURN_EFFORT)
    while not is_either_on_line():
        pass
    drivetrain.stop()


# ===== HELPER FUNCTION =====
def drive_intersections(count):
    for i in range(count):
        print("  Intersection", i + 1, "of", count)
        track_to_intersection()
        drive_past_intersection()


# ===== MAIN PROGRAM =====
board = Board.get_default_board()

board.wait_for_button()

# Drive 3 intersections using the helper function
print("Driving 3 intersections...")
drive_intersections(3)
print("Done! Stopped at intersection 3.")
