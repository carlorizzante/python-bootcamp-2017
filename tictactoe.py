# Tic Tac Toe game
# Launch with start_game()

from IPython.display import clear_output
import random

# Main functions, runs the game
def start_game():
    print("Welcome, we are going to play a Tic Tac Toe game!")
    print("")
    player1 = input("Please enter Player1 name ")
    player2 = input("Please enter Player2 name ")

    clear_output()
    print("Very good, " + player1 + " and " + player2 + ", we are ready to start.")
    print(player1 + " will place X, " + player2 + " will place O.")
    p1 = [player1, "X"]
    p2 = [player2, "O"]
    running = True

    print("Game start!\n")

    while running:

        board = "1 2 3 4 5 6 7 8 9".split()
        display_board(board)
        players = pick_first(p1, p2)
        print("")
        print(players[0][0] + " moves first.")
        game_on = True

        while game_on:

            # First player turn
            if game_on:
                board = next_move(players[0], board) # returns a new board
                clear_output()
                display_board(board)
                if end_game(board):
                    game_on = False
                    print("Great job, " + players[0][0] + ", you won!")
                elif is_board_full(board):
                    game_on = False
                    print("Bummer, no one wins.")

            # Second player turn
            if game_on:
                board = next_move(players[1], board) # returns a new board
                clear_output()
                display_board(board)
                if end_game(board):
                    game_on = False
                    print("Great job, " + players[1][0] + ", you won!")
                elif is_board_full(board):
                    game_on = False
                    print("Bummer, no one wins.")

        if replay():
            clear_output()
            print("Great, let's have a new game!\n")
            game_on = True
        else:
            clear_output()
            print("Thanks, " + player1 + " and " + player2 + ", it was a pleasure.")
            running = False

    print("Bye!!!!")
    return


# Draws the board
# board is an array of 9 strings, "X", "O", or numbers[1,9] as strings
def display_board(board):
    print(str(board[0]) + " | " + str(board[1]) + " | " + str(board[2]))
    print("---------")
    print(str(board[3]) + " | " + str(board[4]) + " | " + str(board[5]))
    print("---------")
    print(str(board[6]) + " | " + str(board[7]) + " | " + str(board[8]))


# Returns an array of players
# p1, p2 are arrays with player's name and player's marker
def pick_first(p1, p2):
    i = random.randint(1,2)
    if i == 1:
        players = [p1, p2]
    else:
        players = [p2, p1]
    return players


# Updates the board with a new move
# Requires current player and current board
# player is array[player's name, player's marker]
def next_move(player, board):
    print("What's your next move, " + player[0] + "?")
    move = ""
    valid = ("1 2 3 4 5 6 7 8 9").split()

    while (move not in valid) or is_square_taken(board, int(move) - 1):
        move = input("Pick a free square from 1 to 9...")

    board[int(move)-1] = player[1]
    return board


# Returns true if the square is taken on the current board, false otherwise
def is_square_taken(board, position):
    return ((board[position] == "X") or (board[position] == "O"))


# Returns true if the square is free on the current board, false otherwise
def is_square_free(board, position):
    return not is_square_taken(board, position)


# Returns true if all squares are taken on a board, false otherwise
def is_board_full(board):
    for i in range(9):
        if is_square_free(board, i):
            return False
    return True


# Returns true if there is a winning condition, false otherwise
# use this at the end of one player's move
def end_game(board):
    return (   (board[0] == board[1] and board[1] == board[2]) # row 1
            or (board[3] == board[4] and board[4] == board[5]) # row 2
            or (board[6] == board[7] and board[7] == board[8]) # row 3
            or (board[0] == board[4] and board[4] == board[8]) # diagonal \
            or (board[2] == board[4] and board[4] == board[6]) # diagonal /
            or (board[0] == board[3] and board[3] == board[6]) # col 1
            or (board[1] == board[4] and board[4] == board[7]) # col 2
            or (board[2] == board[5] and board[5] == board[8])) # col 3


# Returns true if the user's response starts with "Y", false otherwise
def replay():
    return input("New game? Y/N ").upper().startswith("Y")
