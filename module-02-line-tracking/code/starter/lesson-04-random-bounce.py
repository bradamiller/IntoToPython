# Lesson 4: Random Bounce Driving
# Robot bounces off edges with random turn angles

from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board
# TODO: Import the random module

reflectance = Reflectance.get_default_reflectance()
drivetrain = DifferentialDrive.get_default_differential_drive()
board = Board.get_default_board()

threshold = 0.5

board.wait_for_button()
print("Random bounce driving started!")

while True:
    left = reflectance.get_left()
    right = reflectance.get_right()

    if left > threshold or right > threshold:
        drivetrain.stop()
        # TODO: Generate a random angle between 90 and 270
        # angle = ???
        # TODO: Print the angle
        # TODO: Turn by that angle
        pass
    else:
        drivetrain.set_effort(0.3, 0.3)
