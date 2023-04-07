"""
Battleships terminal game written in python

"""
# Import modules
import random
import sys
import time

# CPU and player boards, small and big
player_board_small = [[''] * 6 for x in range(6)]
cpu_board_small = [[''] * 6 for x in range(6)]
player_board_big = [[''] * 9 for x in range(9)]
cpu_board_big = [[''] * 9 for x in range(9)]

# Dictionary to form key value pairs for board co-ordinates
coordinates = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8
}
# Number of ships and their lengths for boards
ships_small = [2, 3, 4, 5]
ships_big = [2, 3, 3, 4, 4, 5]


def print_fast(string):
    """
    Creates fast typing effect for introduction/logo
    """
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)


def print_slow(string):
    """
    Creates a slow typing effect for short print statements

    """
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
