def display_board(board):
    print("Here is your board:")
    for i in range(1, 10, 3):
        print("|".join(board[i:i+3]))
    print()

def player_input():
    player1 = input("Player 1, choose your symbol (X or O): ").upper()
    while player1 not in ["X", "O"]:
        player1 = input("Invalid input. Please choose 'X' or 'O': ").upper()
    player2 = "O" if player1 == "X" else "X"
    return player1, player2

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    winning_combinations = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9), # Horizontal
        (1, 4, 7), (2, 5, 8), (3, 6, 9), # Vertical
        (1, 5, 9), (3, 5, 7)            # Diagonals
    ]
    return any(board[a] == board[b] == board[c] == mark for a, b, c in winning_combinations)

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    return all(space != ' ' for space in board[1:])

def player_choice(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input("Choose a position from 1-9: "))
    return position

def replay():
    return input("Would you like to play again? (Y/N): ").upper() == 'Y'

print('Welcome to Tic Tac Toe!')

while True:
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = 'player1'
    game_on = input("Ready to play? (Y/N): ").lower() == 'y'

    while game_on:
        if turn == 'player1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("PLAYER 1 HAS WON!")
                break
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("It's a tie.")
                    break
                else:
                    turn = 'player2'
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("PLAYER 2 HAS WON!")
                break
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("It's a tie.")
                    break
                else:
                    turn = 'player1'

    if not replay():
        break
