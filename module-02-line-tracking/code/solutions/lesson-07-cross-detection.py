# Lesson 7: Line Following with Cross Detection - SOLUTION
# Robot follows the line and reverses direction when it detects the cross

from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board
import time

reflectance = Reflectance.get_default_reflectance()
drivetrain = DifferentialDrive.get_default_differential_drive()
board = Board.get_default_board()

threshold = 0.5
Kp = 0.5
base_effort = 0.3
cross_count = 0

board.wait_for_button()
print("Line following with cross detection...")

while True:
    left = reflectance.get_left()
    right = reflectance.get_right()

    if left > threshold and right > threshold:
        # Cross detected!
        drivetrain.stop()
        cross_count = cross_count + 1
        print("Cross #", cross_count, "- Turning around!")
        drivetrain.turn(180)
        time.sleep(0.3)
    else:
        # Normal two-sensor line following
        error = left - right
        left_effort = base_effort - error * Kp
        right_effort = base_effort + error * Kp
        drivetrain.set_effort(left_effort, right_effort)
