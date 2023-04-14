"""
Battleships terminal game written in python

"""
# Import modules
import random
import sys
import time

# CPU and player boards
player_board = [['.' for _ in range(10)] for _ in range(10)]
cpu_board = [['.' for _ in range(10)] for _ in range(10)]
hidden_board = [['.' for _ in range(10)] for _ in range(10)]

# Ships
the_ships = [2, 2, 3, 3, 4, 5]


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
    the user knows how to play

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
    time.sleep(0.8)
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
    printing the contents to the terminal
    it waits for user to input valid data
    then calls start_game when ready

    """
    with open('instructions.txt') as file:
        contents = file.read()
        print(contents)
    answer = input('Enter Y to play or N to leave\n').upper()
    while True:
        if answer == 'Y':
            start_game()
        elif answer == 'N':
            type_slow('Ah maybe next time, Goodbye!\n')
            sys.exit()
        else:
            answer = input('Please enter Y or N\n').upper()


def display_board(board):
    """
    Prints the boards to the terminal

    """
    print('  0 1 2 3 4 5 6 7 8 9')
    row_num = 0
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
    hits from the player and cpu boards after each turn

    """
    count = 0
    for row in board:
        for col in row:
            if col == 'X':
                count += 1
    return count


def player_guess(board, hidden):
    """
    Function to allow the player to
    input x and y coordinates to target
    the computers ships on the grid

    """
    while True:
        try:
            row = int(input('\nEnter target row 0-9 \n'))
            if row > 9 or not int(row):
                raise ValueError(
                    'Please enter a valid number between 0-9\n'
                )
            break
        except ValueError as e_e:
            type_slow(f'Invalid input: {e_e}')
    while True:
        try:
            col = int(input('Enter target column 0-9 \n'))
            if row > 9 or not int(col):
                raise ValueError(
                    'Please enter a valid number between 0-9\n'
                )
            break
        except ValueError as e_e:
            type_slow(f'Invalid input: {e_e}')

    if hidden[row][col] == '.':
        print('')
        type_slow('You missed!\n')
        print('')
        board[row][col] = 'O'
        hidden[row][col] = 'O'
    elif hidden[row][col] == '@':
        print('')
        type_slow('You hit an enemy ship!\n')
        print('')
        board[row][col] = 'X'
        hidden[row][col] = 'X'
    else:
        print('You already tried those coordinates! Try again\n')
        row = int(input('Target row number 0-9\n'))
        col = int(input('Target column number 0-9\n'))
    return board[row][col]


def cpu_guess(board):
    """
    Function to allow the computer
    to choose random x an y coordinates
    to target the players ships

    """
    row = random.randint(0, len(board) - 1)
    col = random.randint(0, len(board) - 1)
    if board[row][col] == '.':
        type_slow('CPU missed the target!\n')
        print('')
        board[row][col] = 'O'
    elif board[row][col] == '@':
        type_slow('CPU hit one of your ships!\n')
        print('')
        board[row][col] = 'X'
    return board[row][col]


def play_again():
    """
    play_again function will reset the boards
    and call the start_game function so the user
    can play again

    """
    global player_board
    global cpu_board
    global hidden_board
    player_board = [['.' for _ in range(10)] for _ in range(10)]
    cpu_board = [['.' for _ in range(10)] for _ in range(10)]
    hidden_board = [['.' for _ in range(10)] for _ in range(10)]
    start_game()


def start_game():
    """
    This is the main game loop it
    allows the computer and player to
    take turns guessing coordinates to hit
    each others ships. The game ends when
    all ships from one board have been sunk

    """
    # Add the ships to the boards
    add_ships(hidden_board, the_ships)
    add_ships(player_board, the_ships)

    # Print the boards to the screen
    type_slow('Player Board:\n')
    display_board(player_board)
    type_slow('CPU Board:\n')
    display_board(cpu_board)

    # Player turns
    while True:
        time.sleep(0.3)
        player_guess(cpu_board, hidden_board)
        if count_hits(cpu_board) == 19:
            type_slow('You win! Well done captain!\n')
            print('')
            type_slow('Want to play again?\n')
            answer = input('Y or N \n').upper()
            while True:
                if answer == 'Y':
                    play_again()
                elif answer == 'N':
                    type_slow('See you next time captain!\n')
                    sys.exit()
                else:
                    type_slow('Please enter Y or N')
                    input('').upper()
        # Computer turns
        else:
            time.sleep(0.3)
            cpu_guess(player_board)
            time.sleep(0.3)
            type_slow('Player Board:\n')
            display_board(player_board)
            type_slow('CPU Board:\n')
            display_board(cpu_board)
            if count_hits(player_board) == 19:
                print('You lose! They sank all you"re ships! \n')
                print('')
                type_slow('Want to play again?\n')
                answer = input('Y or N \n').upper()
                while True:
                    if answer == 'Y':
                        play_again()
                    elif answer == 'N':
                        type_slow('See you next time captain!\n')
                        sys.exit()
                    else:
                        type_slow('Please enter Y or N')
                        input('').upper()


intro()
