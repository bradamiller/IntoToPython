# Module 2 Final Project: Circle Follower with Cross Reversal - SOLUTION
# Follow the taped circle, reverse at the cross, repeat 4 times

from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board


# ===== SENSOR TOOLKIT =====
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

def is_off_line():
    return get_left() < THRESHOLD and get_right() < THRESHOLD


# ===== DRIVING TOOLKIT =====
drivetrain = DifferentialDrive.get_default_differential_drive()
BASE_EFFORT = 0.4
KP = 0.5

def clear_intersection():
    drivetrain.straight(8, 0.5)

def track_until_cross():
    while not is_at_cross():
        error = get_error()
        left = BASE_EFFORT - error * KP
        right = BASE_EFFORT + error * KP
        drivetrain.set_effort(left, right)
    drivetrain.stop()

def turn_right():
    clear_intersection()
    drivetrain.set_effort(0.3, -0.3)
    while is_off_line():
        pass
    drivetrain.stop()

def turn_left():
    clear_intersection()
    drivetrain.set_effort(-0.3, 0.3)
    while is_off_line():
        pass
    drivetrain.stop()


# ===== MAIN PROGRAM =====
board = Board.get_default_board()

board.wait_for_button()
print("Module 2 Final Project - Starting!")

for i in range(4):
    print("Leg", i + 1, "- Following line to cross...")
    track_until_cross()
    print("Cross detected! Reversing direction...")
    turn_right()
    turn_right()  # Two right turns = 180 degree reversal

print("Complete! 4 reversals done.")
