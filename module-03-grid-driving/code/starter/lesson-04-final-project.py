# Module 3 Final Project: Square Pattern on the Grid
# Drive a square: 2 intersections per side, 4 right turns
#
# Team: ________________________
# Date: ________________________

from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board
import time


# ===== LINESENSOR CLASS =====
# (Copy your working LineSensor class here)


# ===== LINETRACK CLASS =====
# (Copy your working LineTrack class here)


# ===== HELPER FUNCTION =====
# TODO: Write drive_intersections(tracker, count) function


# ===== MAIN PROGRAM =====
board = Board.get_default_board()

# TODO: Create a LineTrack object
# tracker = ???

board.wait_for_button()
print("Module 3 Final Project - Square Pattern!")

# TODO: Use a for loop to repeat 4 times:
#   1. Print which side you're on (e.g., "Side 1 of 4")
#   2. Drive 2 intersections forward
#   3. Turn right at the intersection

# TODO: Print completion message
print("Square complete! Back at start.")
