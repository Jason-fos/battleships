"""
Battleships terminal game written in python

"""
# Import modules
import random
import sys
import time

# CPU and player boards
player_board = [['.' for _ in range(9)] for _ in range(9)]
cpu_board = [['.' for _ in range(9)] for _ in range(9)]

# Dictionary to form key value pairs for board co-ordinates
coordinates = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9
}

# Ship sizes
the_ships = [2, 2, 3, 4, 5]


def type_fast(string):
    """
    Creates fast typing effect for introduction/logo
    """
    for ltr in string:
        sys.stdout.write(ltr)
        sys.stdout.flush()
        time.sleep(0.03)


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
    type_slow('Welcome to...\n')
    type_fast(
        """
    ____        _   _   _           _     
   |  _ \      | | | | | |         | |   (_)
   | |_) | __ _| |_| |_| | ___  ___| |__  _ _ __  ___
   |  _ < / _` | __| __| |/ _ \/ __| '_ \| | '_ \/ __|
   | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) \__ |
   |____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/|___/
                                           | |
                                           |_|
    """
    )

    print('')
    time.sleep(1)
    type_slow('Do you know how to play?\n')
    print('')
    answer = input('Enter Y or N\n').upper()
    print('')
    while True:
        if answer == 'Y':
            start_game()
        elif answer == 'N':
            show_instructions()
            break
        else:
            type_slow('Please enter Y or N\n')
            answer = input('').upper()


def show_instructions():
    """
    Displays the instructions to the user
    by reading instuctions.txt file and
    printing the lines to the terminal

    """
    with open('instructions.txt') as file:
        contents = file.read()
        print(contents)
        start_game()


def display_board(board):
    """
    Prints the boards to the terminal

    """
    print('  a b c d e f g h i')
    row_num = 1
    for row in board:
        print(row_num, ' '.join(row))
        row_num += 1


def add_ships(board, ships):
    """
    Adds the ships to both player and cpu boards
    whilst checking that they fit and don't overlap

    """
    for ship_length in ships:
        while True:
            position = random.choice(['hor', 'vert'])
            if position == 'hor':
                row = random.randint(0, len(board) - 1)
                col = random.randint(0, len(board) - ship_length)
            else:
                row = random.randint(0, len(board) - ship_length)
                col = random.randint(0, len(board) - 1)
            if location_check(board, row, col, position, ship_length):
                if position == 'hor':
                    for i in range(col, col + ship_length):
                        board[row][i] = '@'
                else:
                    for i in range(row, row + ship_length):
                        board[i][col] = '@'
                break


def location_check(board, row, col, position, ship_length):
    """
    Checks if the ship fits on the board

    """
    if position == 'hor':
        for i in range(col, col + ship_length):
            if board[row][i] != '.':
                return False
    else:
        for i in range(row, row + ship_length):
            if board[i][col] != '.':
                return False
    return True


def count_hits(board):
    """
    The count_hits function counts successful
    hits from the player and cpu.

    """
    count = 0
    for row in board:
        for col in row:
            if col == 'X':
                count += 1
    return count


def start_game():
    """
    This is the main game loop

    """
    add_ships(cpu_board, the_ships)
    add_ships(player_board, the_ships)
    type_slow('CPU Board:\n')
    print('')
    display_board(cpu_board)
    print('')
    type_slow('Player Board:\n')
    print('')
    display_board(player_board)


# intro()
start_game()
