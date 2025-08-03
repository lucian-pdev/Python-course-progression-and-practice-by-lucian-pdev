# Py 1 course final project

# Tic-tac-toe
# Your task is to write a simple program which pretends to play tic-tac-toe with the user.
# To make it all easier for you, we've decided to simplify the game. Here are our assumptions:
# DONE     all the squares are numbered row by row starting with 1 (see the example session below for reference)

#     the first move belongs to the computer − it always puts its first 'X' in the middle of the board;

#     the computer (i.e., your program) should play the game using 'X's;
#     the user (e.g., you) should play the game using 'O's;
#     the user inputs their move by entering the number of the square they choose − the number must be valid,
#     i.e., it must be an integer, it must be greater than 0 and less than 10,
#     and it cannot point to a field which is already occupied;

#     the computer responds with its move and the check is repeated;

#     the program checks if the game is over − there are four possible verdicts:
#     the game should continue, the game ends with a tie, you win, or the computer wins;

#     don't implement any form of artificial intelligence
#     − a random field choice made by the computer is good enough for the game.

# imports
from random import randrange
import os


# set-up: permanent functions
def setup_board_state():
    board = []
    cell = 1
    for y in range(3):
        row = []
        for x in range(3):
            row.append(cell)
            cell += 1
        board.append(row)
    return board


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for o in range(3):
        print(f"+-------+-------+-------+", sep="")
        print("|", " " * 7, "|", " " * 7, "|", " " * 7, "|", sep="")
        print("|", " " * 3, board[o][0], " " * 3, "|", " " * 3, board[o][1], " " * 3, "|", " " * 3, board[o][2],
              " " * 3, "|", sep="")
        print("|", " " * 7, "|", " " * 7, "|", " " * 7, "|", sep="")
    print(f"+-------+-------+-------+", sep="")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    try:
        user_move = int(input(f"Which square will you mark? [1-9]"))
        if type(user_move) is not int:
            print("Unrecognised input detected, exiting...")
            return None
        elif 0 < user_move < 10:
            user_move = int(user_move)
            coordinate_x = (user_move - 1) // 3
            coordinate_y = (user_move - 1) % 3
            if type(board[coordinate_x][coordinate_y]) != str:
                board[coordinate_x][coordinate_y] = "O"
            else:
                print(f"That square already has been marked with {board[coordinate_x][coordinate_y]}. Choose another.")
                return enter_move(board)
        else:
            print("Unrecognised input detected, exiting...")
            return None
    except ValueError:
        print("Unrecognised input detected, exiting...")
        return None
    return board


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for row in range(3):
        for cell in range(3):
            if board[row][cell] is not str:
                tuple_a = (row + 1)
                tuple_b = (cell + 1)
                free_cell_tuple = (tuple_a, tuple_b)
                free_fields.append(free_cell_tuple)
    return free_fields


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    # check_counter = 0
    # the method of checking only win-scenarios:
    for rows in range(3):
        if board[rows] is [sign, sign, sign]:
            return sign
    for columns in range(3):
        if board[0][columns] == sign and board[1][columns] == sign and board[2][columns] == sign:
            return sign
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return sign
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return sign
    free_fields = make_list_of_free_fields(board)
    if len(free_fields) < 2:
        return 5
    return None


def draw_move(board):
    # The function draws the computer's move and updates the board.
    for attempt in range(9):
        target = randrange(1, 9)
        coordinate_x = (target - 1) // 3
        coordinate_y = (target - 1) % 3
        if type(board[coordinate_x][coordinate_y]) == str:
            pass
        else:
            print(f"I'll place my X at {board[coordinate_x][coordinate_y]}.")
            board[coordinate_x][coordinate_y] = "X"
            break
    return board


# main loop
while True:
    board = setup_board_state()
    print(f"Tic-tac-toe, I'll go first. You'll be 'O'.")
    board[1][1] = "X"
    game = True
    while game:
        display_board(board)
        for sign in ("O", "X"):
            result = victory_for(board, sign)
            if result == sign:
                if sign == "O":
                    print("It's a victory for the Player!")
                    game = False
                    break
                else:
                    print("It's a victory for the Machine!")
                    game = False
                    break
            elif result == 5:
                print("It's a tie!")
                game = False
                break
        player_action = enter_move(board)
        if player_action is None:
            game = False
            continue
        os.system("clear")
        draw_move(board)
    break