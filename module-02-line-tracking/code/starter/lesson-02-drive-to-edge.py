# Lesson 2: Drive to the Edge and Stop
# Robot drives forward until it detects the line, then stops

from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board

reflectance = Reflectance.get_default_reflectance()
drivetrain = DifferentialDrive.get_default_differential_drive()
board = Board.get_default_board()

threshold = 0.5  # TODO: Replace with your threshold from Lesson 1

board.wait_for_button()

# Read initial sensor value
left = reflectance.get_left()
print("Starting value:", left)

# TODO: Write a while loop that keeps driving while left < threshold
# Inside the loop:
#   - Set motor effort to drive forward (0.3, 0.3)
#   - Update the left sensor reading
#   - Print the sensor value

# TODO: After the loop, stop the robot
# drivetrain.stop()

print("Done!")
