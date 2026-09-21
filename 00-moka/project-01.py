from os import system, name
from random import randrange

xis = '✘'
circulo = '◯'

### Variáveis com as mensagens de tratamento de erros e/ou alertas para o 
### usuário
prefixo_erro="ERROR: "
prefixo_aviso="WARNING: "
erro_posicao_incorreta="The value must be between 1 and 9. Try again!"
enter_para_continuar="[Press ENTER to CONTINUE]"

board = [
          [1, 2, 3],
          [4, xis, 6],
          [7, 8, 9]
        ]


# Clears the screen, using the appropriate command, according to the operating 
# system type
def clear_screen():
  if name == "nt":
    _ = system("cls")
  else:
    _ = system("clear")


# The function accepts one parameter containing the board's current status and 
# prints it out to the console.
def display_board(board):
  clear_screen()

  l1 = "        |       |"
  l2 = "    {0}   |   {1}   |   {2}"
  l3 = " -------+-------+-------"

  for i in range(3):
    a, b, c = board[i]

    if i != 1:
      print(l1, l2.format(a, b, c), l1, sep="\n")
    else:
      print(l3, l1, l2.format(a, b, c), l1, l3, sep="\n")


# The function browses the board and builds a list of all the free squares; the 
# list consists of tuples, while each tuple is a pair of row and column 
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

  # Stores the position of the computer move. This will be used to display the 
  # value to the user BEFORE actually registering it to the board
  cpu_move = board[row][column]

  input(f"O computador vai jogar na posição [{cpu_move}]!\nContinuar > [ENTER]")

  # Actually registers the computer move
  board[row][column] = xis


# The function accepts the board's current status, asks the user about their 
# move, checks the input, and updates the board according to the user's 
# decision.
def enter_move(board):
  primeira_celula = 1
  ultima_celula = 9

  while True:
    display_board(board)
    try:
      user_input = int(input("Enter your move: "))

      ### Valida se o usuário digitou um número que existe no tabuleiro
      if user_input < primeira_celula or user_input > ultima_celula:
        input(f"{prefixo_erro}{erro_posicao_incorreta}\n{enter_para_continuar}")
        continue
      else: ### Se o número existir, associa à variável 'move' a posição escolhida
        if user_input in board[0]:
          move_address = [0, user_input-1]
        elif user_input in board[1]:
          move_address = [1, user_input-4]
        elif user_input in board[2]:
          move_address = [2, user_input-7]

      row = move_address[0]
      column = move_address[1]

      move = board[row][column]

      if move in [xis, circulo]:
        input(f"{prefixo_erro}Choose a field not yet used!\n{enter_para_continuar}")
        continue
      else:
        # Register the player move
        board[row][column] = circulo
        break

    except ValueError:
      input(f"{prefixo_erro}You must choose an integer number!\n{enter_para_continuar}")
    except:
      input(f"\n{prefixo_erro}Unknown error. Please read the instructions.\n{enter_para_continuar}")

  #victory_for(board, circulo)
  #draw_move( board )

# The function analyzes the board's status in order to check if 
# the player using 'O's or 'X's has won the game
def victory_for(board, sign):

  display_board(board)
  venceu_vertical = False
  venceu_horizontal = False
  resultado_circulo = [venceu_horizontal, venceu_vertical]
  resultado_xis = [venceu_horizontal, venceu_vertical]

  # Validação de vitória na HORIZONTAL
  for row in board:
    contador = 0
    for cell in row:
      if cell != sign:
        break
      contador += 1

    if contador == 3:
      venceu_horizontal = True
      break

  # Validação de vitória na VERTICAL
  for row in range(3):
    contador = 0
    for column in range(3):
      if board[column][row] != sign:
        break
      contador += 1

    if contador == 3:
      venceu_vertical = True
      break

  if sign == circulo:
    resultado_circulo = [venceu_horizontal, venceu_vertical]
  elif sign == xis:
    resultado_xis = [venceu_horizontal, venceu_vertical]

    # Validação de vitória nas DIAGONAIS
    # Diagonal principal:  (0, 0), (1, 1), (2, 2)
    # Diagonal secundária: (0, 2), (1, 1), (2, 0)
    if (board[0][0] == xis and board[2][2] == xis) or\
       (board[0][2] == xis and board[2][0] == xis):
      resultado_xis = [True, True]
  else:
    print(f"O parâmetro {sign} não é reconhecido pelo programa")
    print("Verifique a chamada da função victory_for() e tente novamente")

  if True in resultado_circulo:
    vencedor = "jogador"
  elif True in resultado_xis:
    vencedor = "computador"
  else:
    vencedor = None

  if vencedor != None:
    input(f"O {vencedor} venceu!\nPressione [ENTER] para sair!")
    exit()

  if len(make_list_of_free_fields(board)) == 0:
    input(f"O jogo empatou!\nPressione [ENTER] para sair!")
    exit()


#    # verificações verticais
#    for i in range(0, 3, 2): # Checks only first and last rows (indices 0 and 2)
#      circulo_venceu_horizontal = True
#      for j in range(3):
#        if board[i][j] != circulo:
#          print(board[i][j], end=" ")
#          circulo_venceu_horizontal = False
#          break
#        
#        #print("vert", circulo_venceu_vertical)
#        #if board[j][i] != circulo:
#        #  #print(board[j][i], end=" ")
#        #  circulo_venceu_vertical = False
#
#    # verificações horizontais
#    #for i in range
#


def main():
  while True:
    enter_move(board)
    victory_for(board, circulo)
    draw_move(board)
    victory_for(board, xis)


main()
