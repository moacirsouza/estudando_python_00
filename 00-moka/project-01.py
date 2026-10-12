import os
from random import randrange

computer_sign = '✘'
player_sign = '◯'

board = [
          [1, 2, 3],
          [4, computer_sign, 6],
          [7, 8, 9]
        ]


# Centralises all the messages the user may receive from the program.
def message_handler(function_name, extra_parameters = None):
  prefix = ""
  action_prompt = "\nPress [ENTER] to CONTINUE "
  will_return = False
  message_body = ""

  match function_name:
    case 'draw_move':
      message_body = f"The computer will play at cell [{extra_parameters}]!"

    case 'enter_move':
      match extra_parameters:
        case 0:
          message_body = "Your next move: "
          action_prompt = ""
          will_return = True

        case 1:
          prefix = "WARNING: "
          message_body = "The value must be between 1 and 9."
        
        case 2:
          prefix = "WRONG MOVE: "
          message_body = "Choose a field not yet used!"

        case 3:
          prefix = "ERROR: "
          message_body = "You must choose an integer number!"

        case 4:
          prefix = "ERROR: "
          message_body = "Unknown error. Please read the instructions!"
    
    case 'victory_for':
      prefix = "GAME OVER!\n"
      action_prompt = "\nPress [ENTER] to exit!"

      match extra_parameters:
        case 1:
          message_body = "It's a DRAW!"
        case _:
          message_body = f"Winner: {extra_parameters}!"

  registered_return = input(f"{prefix}{message_body}{action_prompt}")

  if will_return:
    return registered_return 


# Clears the screen using the appropriate command, according to the operating 
# system type.
def clear_screen():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")


# The function accepts one parameter containing the board's current status and 
# prints it out to the console.
def display_board(board):
  clear_screen()

  l1 = "        |       |"
  l2 = "    {0}   |   {1}   |   {2}"
  l3 = " -------+-------+-------"

  for i in range(len(board)):
    a, b, c = board[i]

    if i != 1:
      print(l1, l2.format(a, b, c), l1, sep="\n")
    else:
      print(l3, l1, l2.format(a, b, c), l1, l3, sep="\n")


# The function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column 
# numbers.
def make_list_of_free_fields(board):
  free_fields = []

  for row in range(3):
    for column in range(3):
      if board[row][column] in range(1, 10):
        free_fields.append((row, column))

  return free_fields


# The function draws the computer's move and updates the board.
def draw_move(board):
  possible_moves = make_list_of_free_fields(board)
  total_moves_left = len(possible_moves)

  next_move = randrange(total_moves_left)

  row = possible_moves[next_move][0]
  column = possible_moves[next_move][1]

  # Stores computer's next move. This will be used to display the cell address 
  # to the user BEFORE actually registering it to the board
  cpu_move = board[row][column]

  message_handler('draw_move', cpu_move)

  # Actually registers the computer move
  board[row][column] = computer_sign


# The function accepts the board's current status, asks the user about their 
# move, checks the input, and updates the board according to the user's 
# decision.
def enter_move(board):

  while True:
    display_board(board)
    try:
      user_input = int(message_handler('enter_move', 0))

      if user_input < 1 or user_input > 9:
        message_handler('enter_move', 1)
        continue
      else:
        row = -1
        offset = -1
        if user_input in range(1, 4):
          row = 0
          offset = 1
        elif user_input in range(4, 7):
          row = 1
          offset = 4
        elif user_input in range(7, 10):
          row = 2
          offset = 7

        column = user_input - offset

      move = board[row][column]

      if move in [computer_sign, player_sign]:
        message_handler('enter_move', 2)
        continue
      else:
        # Register the player move
        board[row][column] = player_sign
        break

    except ValueError:
      message_handler('enter_move', 3)
    except:
      message_handler('enter_move', 4)


# The function analyzes the board's status in order to check if 
# the player using 'O's or 'X's has won the game
def victory_for(board, sign):

  display_board(board)
  won_in_vertical = False
  won_in_horizontal = False
  player_sign_results = [won_in_horizontal, won_in_vertical]
  computer_sign_results = [won_in_horizontal, won_in_vertical]

  for row in range(3):
    row_counter = 0
    column_counter = 0

    for column in range(3):
      if board[row][column] != sign:
        row_counter = 0
      else:
        row_counter += 1
      
      if board[column][row] != sign:
        column_counter = 0
      else:
        column_counter += 1

      # Hipóstese: Se os dois contadores permanecerem 
      # zero, significa que o símbolo NÃO PODE vencer
      # nem na vertical, nem na horizontal!
      if row_counter == 0 and column_counter == 0:
        break

    if row_counter == 3:
      won_in_horizontal = True
      break

    if column_counter == 3:
      won_in_vertical = True
      break

  if sign == player_sign:
    player_sign_results = [won_in_horizontal, won_in_vertical]
  elif sign == computer_sign:
    computer_sign_results = [won_in_horizontal, won_in_vertical]

    # Validates the DIAGONALS wins
    # Main diagonal:  (0, 0), (1, 1), (2, 2)
    # Secondary diagonal: (0, 2), (1, 1), (2, 0)
    if (board[0][0] == computer_sign and board[2][2] == computer_sign) or\
       (board[0][2] == computer_sign and board[2][0] == computer_sign):
      computer_sign_results = [True, True]
  else:
    print(f"The parameter {sign} is not recognised by the program")
    print("Plase, check the function 'victory_for()' and try again")

  if True in player_sign_results:
    winner = "Player"
  elif True in computer_sign_results:
    winner = "Computer"
  else:
    winner = None

  # Someone won
  if winner != None:
    message_handler("victory_for", winner)
    exit()

  # A draw happened
  if len(make_list_of_free_fields(board)) == 0:
    message_handler("victory_for", 1)
    exit()


def main():
  while True:
    enter_move(board)
    victory_for(board, player_sign)
    draw_move(board)
    victory_for(board, computer_sign)


main()
