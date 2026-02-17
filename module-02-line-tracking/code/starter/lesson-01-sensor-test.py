# Lesson 1: Sensor Calibration
# Read reflectance sensor values to calibrate your robot

from XRPLib.reflectance import Reflectance
from XRPLib.board import Board
import time

reflectance = Reflectance.get_default_reflectance()
board = Board.get_default_board()

board.wait_for_button()

# TODO: Read and print sensor values 20 times
# Use a for loop with range(20)
# Read left and right sensors
# Print the values
# Sleep 0.5 seconds between readings

for i in range(20):
    # TODO: Read left sensor value
    # left = ???

    # TODO: Read right sensor value
    # right = ???

    # TODO: Print both values
    # print("Reading", i + 1, "- Left:", ???, "  Right:", ???)

    time.sleep(0.5)
