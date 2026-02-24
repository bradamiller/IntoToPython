# Lesson 6: Two-Sensor Line Following - SOLUTION
# Robot follows the center of the line using both sensors

from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board

reflectance = Reflectance.get_default_reflectance()
drivetrain = DifferentialDrive.get_default_differential_drive()
board = Board.get_default_board()

Kp = 0.5
base_effort = 0.3

board.wait_for_button()
print("Two-sensor line following started!")

while True:
    left = reflectance.get_left()
    right = reflectance.get_right()

    error = left - right

    correction = error * Kp
    drivetrain.arcade(base_effort, -correction)
