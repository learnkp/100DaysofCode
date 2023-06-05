import random


# create print board
def print_board(board):
    print(f" {board[0]}  |  {board[1]}  |  {board[2]} ")
    print("----|-----|----")
    print(f" {board[3]}  |  {board[4]}  |  {board[5]} ")
    print("----|-----|----")
    print(f" {board[6]}  |  {board[7]}  |  {board[8]} ")


# Take a player input
def player_input(board):
    global currentPlayer
    print("NOTE: Opponent has automatic random choice to make a position")
    playerInp = int(input("User's input, Enter a number between 1 to 9: "))
    if 1 <= playerInp <= 9 and board[playerInp - 1] == "-":
        board[playerInp - 1] = currentPlayer
    elif playerInp > 9:
        print("You have entered a wrong input.")
    else:
        print("Position has already taken.")


# check if it's win or tie..
def check_horizantally(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True


def check_vertically(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True


def check_diagonally(board):
    global winner
    if board[0] == board[4] == board[8] and board[4] != "-":
        winner = board[4]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[4]
        return True


# check win ..
def check_win():
    if check_vertically(board) \
            or check_horizantally(board) \
            or check_diagonally(board) == True:
        global is_game_on
        print_board(board)
        print(f"The Winner is '{winner}'🤩")
        is_game_on = False


# check tie..
def check_tie(board):
    global is_game_on
    if "-" not in board:
        if check_vertically(board) \
                or check_horizantally(board) \
                or check_diagonally(board):
            is_game_on = False
        else:
            print_board(board)
            print("It's a tie..")
            is_game_on = False


# switch a player..
def switch_player():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


# computers play.........
def computer_position(board):
    while currentPlayer == "O":
        rand_position = random.randint(0, 8)
        if board[rand_position] == "-":
            board[rand_position] = "O"
            switch_player()


board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None
is_game_on = True

while is_game_on:
    print_board(board)
    player_input(board)
    check_tie(board)
    check_win()
    if check_vertically(board) \
            or check_horizantally(board) \
            or check_diagonally(board):
        break
    switch_player()
    computer_position(board)
    check_win()
    check_tie(board)
