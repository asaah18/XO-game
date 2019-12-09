from random import randint

DEFAULT_VALUE = " "


def is_odd(number: int):
    return number % 2 != 0


# done: game board(grid) input interface
def validate_input(choice: str, included_start: int, excluded_end: int):
    # validate for acceptable input[1-9]
    if not choice.isdigit():
        return False
    # validate for input is in range[included_start-excluded_end)
    if not int(choice) in range(included_start, excluded_end):
        return False
    else:
        return True


def check_availability(board: list, choice: int):
    row_index, column_index = get_coordinate(choice)
    # position is available
    if board[row_index][column_index] == DEFAULT_VALUE:
        return True
        # position is not available
    else:
        return False


def get_coordinate(choice: int):
    # offset choice to be suitable as an index
    number = choice - 1
    # convert choice into coordinate
    column_index = number % 3
    row_index = int(number / 3)
    return row_index, column_index


def print_board(board: list):
    for main_index, row in enumerate(board):
        text = ""
        for index, position in enumerate(row):
            text += str(position)
            if index != 2:
                text += "|"
        print(text)
        if main_index != 2:
            print("-" * len(text))


def score(board: list, player: str):
    # row by row
    for row in board:
        if determine_winner(row, player) == player:
            return player

    # column by column
    for column_index in range(0, 3):
        column = [row[column_index] for row in board]
        if determine_winner(column, player) == player:
            return player

    # Diagonally
    # from left to right
    left_to_right = [board[index][index] for index in range(0, 3)]
    if determine_winner(left_to_right, player) == player:
        return player

        # from right to left
    right_to_left = [board[index][index] for index in range(2, -1, -1)]
    if determine_winner(right_to_left, player) == player:
        return player

    # if no one win
    return None


def determine_winner(piece_of_board: list, player: str):
    for position in piece_of_board:
        if position != player:
            return None
    else:
        return player


# done: main function to lead the program
# def get_mode():
#     mode = None
#     while mode is None:
#         user_input = input("choose game mode ([1] human vs computer, [2] human vs human):")
#         if validate_input(user_input, 1, 3):
#             mode = user_input
#
#     if mode is 1:
#         return "H", "C"
#     elif mode is 2:
#         return "H", "H"


def play():
    template = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    board = [[DEFAULT_VALUE, DEFAULT_VALUE, DEFAULT_VALUE],
             [DEFAULT_VALUE, DEFAULT_VALUE, DEFAULT_VALUE],
             [DEFAULT_VALUE, DEFAULT_VALUE, DEFAULT_VALUE]]
    separate = "*" * 15
    player_letter = "X"
    computer_letter = "O"

    # welcome page
    print("welcome to XO game,")
    # player1, player2 = get_mode()
    print("you will play against computer, and computer will play first. and your letter will be 'X'")
    print("please use the numbers in the board below as a coordinating system.")
    print(separate)
    print_board(template)
    print(separate)

    for counter in range(1, 10):
        choice = None
        while choice is None:
            # odd number -> computer
            if is_odd(counter):
                computer_input = randint(1, 9)
                if check_availability(board, computer_input):
                    choice = computer_input
                    print("computer play in ", choice)
                    print(separate)

            # even number -> human
            elif not is_odd(counter):
                user_input = input("where do you want to play[from 1 to 9]: ")
                if validate_input(user_input, 1, 10):
                    user_input = int(user_input)
                    if not check_availability(board, user_input):
                        print(" place is unavailable!")
                    else:
                        # valid and available input
                        choice = user_input
                        print(separate)
                else:
                    print("invalid input!")

        # assign choice into board
        row_index, column_index = get_coordinate(choice)
        board[row_index][column_index] = computer_letter if is_odd(counter) else player_letter

        # print the board
        print_board(board)
        print(separate)

        # match state
     if score(board, (computer_letter if is_odd(counter) else player_letter)):
        print((computer_letter if is_odd(counter) else player_letter), "is the winner")
        break

    else:
        print("no one win")


play()
