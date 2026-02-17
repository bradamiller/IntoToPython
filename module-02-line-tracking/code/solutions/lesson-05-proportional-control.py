# Lesson 5: Proportional Control with One Sensor - SOLUTION
# Robot follows the edge of the line using proportional control

from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board

reflectance = Reflectance.get_default_reflectance()
drivetrain = DifferentialDrive.get_default_differential_drive()
board = Board.get_default_board()

setpoint = 0.5
Kp = 0.5
base_effort = 0.3

board.wait_for_button()
print("Proportional line following started!")

while True:
    sensor = reflectance.get_left()
    error = setpoint - sensor
    left_effort = base_effort + error * Kp
    right_effort = base_effort - error * Kp
    drivetrain.set_effort(left_effort, right_effort)
