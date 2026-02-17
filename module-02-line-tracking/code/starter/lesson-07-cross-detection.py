# Lesson 7: Line Following with Cross Detection
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

board.wait_for_button()
print("Line following with cross detection...")

while True:
    left = reflectance.get_left()
    right = reflectance.get_right()

    # TODO: Check if both sensors are above threshold (cross detected)
    # If so:
    #   - Stop the robot
    #   - Print "Cross detected!"
    #   - Turn 180 degrees
    #   - Sleep 0.3 seconds
    # Else:
    #   - Do normal two-sensor line following
    #   - error = left - right
    #   - Calculate and apply motor efforts
    pass
