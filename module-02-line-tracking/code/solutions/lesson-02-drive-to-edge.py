# Lesson 2: Drive to the Edge and Stop - SOLUTION
# Robot drives forward until it detects the line, then stops

from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board

reflectance = Reflectance.get_default_reflectance()
drivetrain = DifferentialDrive.get_default_differential_drive()
board = Board.get_default_board()

threshold = 0.5

board.wait_for_button()

left = reflectance.get_left()
print("Starting value:", left)

while left < threshold:
    drivetrain.set_effort(0.3, 0.3)
    left = reflectance.get_left()
    print("Sensor:", left)

drivetrain.stop()
print("Line detected! Final value:", left)
