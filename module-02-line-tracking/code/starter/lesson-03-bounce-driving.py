# Lesson 3: Bounce Driving
# Robot drives until it hits the line, turns around, repeats forever

from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board

reflectance = Reflectance.get_default_reflectance()
drivetrain = DifferentialDrive.get_default_differential_drive()
board = Board.get_default_board()

threshold = 0.5  # TODO: Replace with your threshold

board.wait_for_button()
print("Bounce driving started!")

# TODO: Write a while True loop that:
#   1. Reads the left sensor
#   2. If the sensor is above threshold (on the line):
#      - Stop the robot
#      - Print "Bounce!"
#      - Turn 180 degrees
#   3. Else (sensor is below threshold, on white):
#      - Drive forward with set_effort(0.3, 0.3)
