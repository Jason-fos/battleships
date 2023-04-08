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
ship_lengths_small = [2, 3, 4, 5]
ship_lengths_big = [2, 2, 3, 3, 4, 5]


def type_fast(string):
    """
    Creates fast typing effect for introduction/logo
    """
    for ltr in string:
        sys.stdout.write(ltr)
        sys.stdout.flush()
        time.sleep(0.05)


def type_slow(string):
    """
    Creates a slow typing effect for short print statements

    """
    for ltr in string:
        sys.stdout.write(ltr)
        sys.stdout.flush()
        time.sleep(0.1)


def intro():
    """
    This is the introduction to the game
    which will display the battleship logo
    followed by a welcome message asking if
    the user needs to see instructions

    """
    type_fast(
        """\
    \u001B[31m
    ____        _   _   _           _     _
   |  _ \      | | | | | |         | |   (_)
   | |_) | __ _| |_| |_| | ___  ___| |__  _ _ __  ___
   |  _ < / _` | __| __| |/ _ \/ __| '_ \| | '_ \/ __|
   | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) \__ |
   |____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/|___/
                                         | |
                                         |_|
    \u001b[0m
    """
    )

    type_slow('Welcome to Battleships!\n')
    time.sleep(1.5)
    type_slow('Do you need to see the game instructions?\n')
    answer = input('Enter "Y" or "N"\n').upper()


intro()