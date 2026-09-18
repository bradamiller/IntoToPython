# Module 3 Final Project: Square Pattern on the Grid
# Drive a square: 2 intersections per side, 4 right turns
#
# Team: ________________________
# Date: ________________________

from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board

# ===== SENSOR TOOLKIT =====
# (Copy your working sensor toolkit from Module 2 Lesson 8 here)


# ===== DRIVING TOOLKIT =====
# (Copy your working driving toolkit from Module 2 Lesson 9 here)


# ===== HELPER FUNCTION =====
# TODO: Write drive_intersections(count) function


# ===== MAIN PROGRAM =====
board = Board.get_default_board()

board.wait_for_button()
print("Module 3 Final Project - Square Pattern!")

# TODO: Use a for loop to repeat 4 times:
#   1. Print which side you're on (e.g., "Side 1 of 4")
#   2. Drive 2 intersections forward
#   3. Turn right at the intersection

# TODO: Print completion message
print("Square complete! Back at start.")
