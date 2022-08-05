# print('Game')
# player_1 = input(" Player_1: Pick X or O: ")
# player_2 = input(" Player_2: Pick X or O: ")
# print()

from numpy import diagonal


board = ["*", "*", "*",
        "*", "*", "*",
        "*", "*", "*"]

game_on = True
winner = None
player = "X"

def play():
    while game_on:
        display_board()
        action()
        is_game_over()
        change_player()

        if game_on == False:
            if winner == "X" or winner == "O":
                print(winner + "Won")
            elif winner == None:
                display_board()
                print("Tie!")


def display_board():
    print()
    print('''{}  |  {}  |  {}        1 | 2 | 3
{}  |  {}  |  {}        4 | 5 | 6
{}  |  {}  |  {}        7 | 8 | 9'''\
    .format(board[0], board[1], board[2], board[3], \
        board[4], board[5], board[6], board[7], board[8]))


def change_player():
    global player
    if player == "X":
        player = "O"
        print(player + '\'s' + "turn")
    elif player == "O":
        player = "X"
        print(player + '\'s' + "turn")


def check_row():
    global winner
    global game_on

    row_1 = board[0] == board[1] == board[2] != "*"
    row_2 = board[3] == board[4] == board[5] != "*"
    row_3 = board[6] == board[7] == board[8] != "*"

    if row_1:
        game_on = False
        winner = board[0]
    elif row_2:
        game_on = False
        winner = board[3]
    elif row_3:
        game_on = False
        winner = board[6]
    else:
        pass


def check_columns():
    global winner
    global game_on

    column_1 = board[0] == board[3] == board[6] != "*"
    column_2 = board[1] == board[4] == board[7] != "*"
    column_3 = board[2] == board[5] == board[8] != "*"

    if column_1:
        game_on = False
        winner = board[0]
    elif column_2:
        game_on = False
        winner = board[1]
    elif column_3:
        game_on = False
        winner = board[2]
    else:
        pass


def check_diagonals():
    global winner
    global game_on
    diag_1 = board[0] == board[4] == board[8] != "*"
    diag_2 = board[2] == board[4] == board[6] != "*"

    if diag_1:
        game_on = False
        winner = board[0]
    elif diag_2:
        game_on = False
        winner = board[2]


def is_winner():
    global winner

    row_winner = check_row()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_for_tie():
    global game_on
    if "*" not in board:
        game_on = True
        return False
    else:
        return True 


def is_game_over():
    is_winner()
    check_for_tie()


def action():
    while game_on:
        action = int(input("Choose position of where you want to play (1-9): "))
        if action == 1:
            if board[0] != "*":
                print("This position has been taken, play somewhere else")
                continue
            else:
                board[0] = player

        elif action == 2:
            if board[1] != "*":
                print("This position has been taken, play somewhere else")
                continue
            else:
                board[1]= player

        elif action == 3:
            if board[2] != "*":
                print("This position has been taken, play somewhere else")
                continue
            else:
                board[2] = player

        elif action == 4:
            if board[3] != "*":
                print("This position has been taken, play somewhere else")
                continue
            else:
                board[3] = player

        elif action == 5:
            if board[4] != "*":
                print("This position has been taken, play somewhere else")
                continue
            else:
                board[4] = player

        elif action == 6:
            if board[5] != "*":
                print("This position has been taken, play somewhere else")
                continue
            else:
                board[5] = player

        elif action == 7:
            if board[6] != "*":
                print("This position has been taken, play somewhere else")
                continue
            else:
                board[6] = player

        elif action == 8:
            if board[7] != "*":
                print("This position has been taken, play somewhere else")
                continue
            else:
                board[7] = player

        elif action == 9:
            if board[8] != "*":
                print("This position has been taken, play somewhere else")
                continue
            else:
                board[8] = player

        else:
            print("Please enter a number from 0 - 9")
            continue
        break


play()