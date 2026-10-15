# Lesson 1: Introduction to the Grid - SOLUTION
# Drive to the first intersection on the grid and stop

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
        correction = error * KP
        drivetrain.arcade(BASE_EFFORT, -correction)
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


# ===== MAIN PROGRAM =====
board = Board.get_default_board()

board.wait_for_button()

# Drive to the first intersection
print("Driving to first intersection...")
track_to_intersection()
drive_past_intersection()      # wheels over the intersection
print("Intersection reached!")

# Bonus: Turn right and drive to another intersection
print("Turning clockwise...")
turn_clockwise()
print("Driving to next intersection...")
track_to_intersection()
print("Second intersection reached!")
