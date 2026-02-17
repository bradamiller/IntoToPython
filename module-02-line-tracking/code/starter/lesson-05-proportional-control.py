# Lesson 5: Proportional Control with One Sensor
# Robot follows the edge of the line using proportional control

from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board

reflectance = Reflectance.get_default_reflectance()
drivetrain = DifferentialDrive.get_default_differential_drive()
board = Board.get_default_board()

# Control parameters
setpoint = 0.5      # Target sensor value (edge of line)
Kp = 0.5            # Proportional gain - adjust this!
base_effort = 0.3   # Base forward speed

board.wait_for_button()
print("Proportional line following started!")

while True:
    # TODO: Read the left sensor
    # sensor = ???

    # TODO: Calculate error (setpoint - sensor)
    # error = ???

    # TODO: Calculate left and right motor efforts
    # left_effort = base_effort + error * Kp
    # right_effort = base_effort - error * Kp

    # TODO: Apply efforts to motors
    # drivetrain.set_effort(left_effort, right_effort)
    pass
