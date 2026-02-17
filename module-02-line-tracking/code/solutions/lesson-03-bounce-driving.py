# Lesson 3: Bounce Driving - SOLUTION
# Robot drives until it hits the line, turns around, repeats forever

from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board

reflectance = Reflectance.get_default_reflectance()
drivetrain = DifferentialDrive.get_default_differential_drive()
board = Board.get_default_board()

threshold = 0.5
bounce_count = 0

board.wait_for_button()
print("Bounce driving started!")

while True:
    left = reflectance.get_left()
    right = reflectance.get_right()

    if left > threshold or right > threshold:
        drivetrain.stop()
        bounce_count = bounce_count + 1
        print("Bounce #", bounce_count)
        drivetrain.turn(180)
    else:
        drivetrain.set_effort(0.3, 0.3)
