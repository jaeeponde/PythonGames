

def display_board(board):
   print("Here is your board : ")

   print (board[1]+"|"+board[2]+"|"+board[3])
   print (board[4]+"|"+board[5]+"|"+board[6])
   print (board[7]+"|"+board[8]+"|"+board[9])

   pass

def player_input():
  player1= " "
  player2= " "


  while player1 not in ["X","O"]:
    player1 = input("Player1 - choose your symbol: X or O")

  if player1=="X":
    player2="O"
  else:
    player2="X"



  return (player1,player2)

def place_marker(board, marker, position):
  board[position] = marker
  pass

def win_check(board, mark):
  check=0
  cond1 = (board[1] == board[2] == board[3]) == mark
  cond2 = (board[1] == board[4] == board[7]) == mark
  cond3 = (board[7] == board[8] == board[9]) == mark
  cond4 = (board[3] == board[6] == board[9]) == mark
  cond5 = (board[1] == board[5] == board[9]) == mark
  cond6 = board[3] == board[5] == board[7] == mark
  cond7 = board[2] == board[5] == board[8] == mark

  checklist = [cond1,cond2,cond3,cond4,cond5,cond6,cond7]

  for item in checklist:
    if item == True:
      check =+1
    else:
      pass

  if check ==0:
    return False
  else :
    return True

def space_check(board, position):

    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):

  pos = 100

  while pos not in [1,2,3,4,5,6,7,8,9] or not space_check(board,pos):
     pos = int(input("Choose a position from 1-9 : "))

  return pos

def replay():
  answer = input("Would you like to play again? Y or N")
  if answer == "Y":
    return True
  else:
    return False

    pass

print('Welcome to Tic Tac Toe!')
position=0

while True :

  the_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

  player1marker,player2marker = player_input()

  print("Player 1 will play first :")
  turn = "player1"

  playgame = input("Ready to play? y or n")

  if playgame=="y":
    gameon=True


  else:
    gameon=False

  while gameon==True:

    if turn == "player1":
      display_board(the_board)

      position = player_choice(the_board)

      place_marker(the_board, player1marker, position)

    if win_check(the_board, player1marker):
      display_board(the_board)
      print("PLAYER 1 HAS WON!")
      gameon = False

    else:
      if full_board_check(the_board):
        display_board(the_board)
        print ("You have tied.")
        gameon = False
      else:
        turn = "player2"


    if turn == "player2":
      display_board(the_board)

      position = player_choice(the_board)

      place_marker(the_board, player2marker, position)

    if win_check(the_board, player2marker):
      display_board(the_board)
      print("PLAYER 2 HAS WON!")
      gameon = False

    else:
      if full_board_check(the_board):
        display_board(the_board)
        print ("You have tied.")
        gameon = False
      else:
        turn = "player1"

  if not replay():
      break