"""
Battleships terminal game written in python

"""
# Import modules
import random
import sys
import time

# CPU and player boards
player_board = [[''] * 9 for x in range(9)]
cpu_board = [[''] * 9 for x in range(9)]

# Dictionary to form key value pairs for board co-ordinates
coordinates = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8
}
# Number of ships and their lengths for boards
ship_sizes = [2, 2, 3, 3, 4, 5]


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
    print('   a b c d e f g h i')
    print('  *******************')
    row_no = 1
    for row in board:
        print(' %d| %s|' % (row_no, '| '.join(row)))
        row_no += 1


def add_ships(board):
    """
    Adds the ships to both player and cpu boards

    """
    for ship in ship_sizes:
        while True:
            if board == cpu_board:
                axis, row, col = random.choice(['X', 'Y']), \
                    random.randint(0, 8), random.randint(0, 8)
                if check_ship(ship, row, col, axis):
                    if not ship_ovlap(board, row, col, axis, ship):
                        if axis == 'X':
                            for i in range(col, col + ship):
                                board[row][i] = '@'
                        else:
                            for i in range(row, row + ship):
                                board[i][col] = '@'
                        break
            if board == player_board:
                axis, row, col = random.choice(['X', 'Y']), \
                    random.randint(0, 8), random.randint(0, 8)
                if check_ship(ship, row, col, axis):
                    if not ship_ovlap(board, row, col, axis, ship):
                        if axis == 'X':
                            for i in range(col, col + ship):
                                board[row][i] = '@'
                        else:
                            for i in range(row, row + ship):
                                board[i][col] = '@'


def start_game():
    """
    This is the main game loop

    """
    display_board(cpu_board)
    print('')
    display_board(player_board)
    add_ships(cpu_board)
    add_ships(player_board)


intro()
