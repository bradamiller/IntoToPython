# Module 2 Final Project: Circle Follower with Cross Reversal
# Follow the taped circle, reverse at the cross, repeat 4 times
#
# Team: ________________________
# Date: ________________________

from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board
import time


# ===== LINESENSOR CLASS =====
# (Copy your working LineSensor class from Lesson 8 here)


# ===== LINETRACK CLASS =====
# (Copy your working LineTrack class from Lesson 9 here)


# ===== MAIN PROGRAM =====
board = Board.get_default_board()

# TODO: Create a LineTrack object
# tracker = ???

board.wait_for_button()
print("Module 2 Final Project - Starting!")

# TODO: Use a for loop to repeat 4 times:
#   1. Print which leg you're on
#   2. Follow line until cross (track_until_cross)
#   3. Print that cross was detected
#   4. Turn around (how will you reverse direction?)

# TODO: Stop and print completion message
print("Complete! 4 reversals done.")
