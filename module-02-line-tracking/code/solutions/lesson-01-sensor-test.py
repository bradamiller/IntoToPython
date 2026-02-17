# Lesson 1: Sensor Calibration - SOLUTION
# Read reflectance sensor values to calibrate your robot

from XRPLib.reflectance import Reflectance
from XRPLib.board import Board
import time

reflectance = Reflectance.get_default_reflectance()
board = Board.get_default_board()

board.wait_for_button()

# Read and print sensor values 20 times
for i in range(20):
    left = reflectance.get_left()
    right = reflectance.get_right()
    print("Reading", i + 1, "- Left:", left, "  Right:", right)
    time.sleep(0.5)

print("Calibration complete!")
