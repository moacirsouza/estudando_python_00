import os
from random import randrange

xis = '✘'
circulo = '◯'
primeira_celula = 1
ultima_celula = 9


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

## Exemplo de tabuleiro desenhado
#         |       |
#     1   |   2   |   3   
#         |       |
# --------+-------+--------
#         |       |
#     4   |   5   |   6   
#         |       |
# --------+-------+--------
#         |       |
#     7   |   8   |   9    
#         |       |

## Tipos de linha
# Linha 1: +-------+-------+-------+
# Linha 2: |       |       |       |
# Linha 3: |   1   |   2   |   3   |

l1 = " -------+-------+-------"
l2 = "        |       |       "
l3 = "    {0}   |   {1}   |   {2}   "

def ponta( indice_do_tabuleiro ):
  a, b, c = indice_do_tabuleiro
  #print(l1, l2, l3.format(a, b, c), l2, l1, sep="\n")
  print(l2, l3.format(a, b, c), l2, sep="\n")

def meio():
  a, b, c = board[1]
  #print(l2, l3.format(a, b, c), l2, sep="\n")
  print(l1, l2, l3.format(a, b, c), l2, l1, sep="\n")
  #print(l2, l3.format(a, b, c), l2, sep="\n")


def display_board(board):
# The function accepts one parameter containing the board's current status
# and prints it out to the console.
  os.system('clear')
  ponta( board[0] )
  meio()
  ponta( board[2] )

# the user inputs their move by entering the number of the square they choose − 
# the number must be valid, i.e., it must be an integer, it must be greater 
# than 0 and less than 10, and it cannot point to a field which is already 
# occupied;

def make_list_of_free_fields(board):
# The function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers.
  free_fields = []

  for linha in range(3):
    for coluna in range(3):
      if board[linha][coluna] in range(1, 10):
        free_fields.append((linha, coluna))

  return free_fields


def draw_move(board):
## The function draws the computer's move and updates the board.
  possible_moves = make_list_of_free_fields( board )
  bla = len(possible_moves)
  #print("Jogadas possíveis:", possible_moves)

  pos = randrange(bla)
  input(f"O computador escolheu: {board[possible_moves[pos][0]][possible_moves[pos][1]]}")
  board[ possible_moves[pos][0] ][ possible_moves[pos][1] ] = xis
  enter_move( board )



def enter_move(board):
# The function accepts the board's current status, asks the user about their move, 
# checks the input, and updates the board according to the user's decision.
  while True:
    display_board(board)
    try:
      user_input = int(input("Enter your move: "))

      ### Valida se o usuário digitou um número que existe no tabuleiro
      if user_input < primeira_celula or user_input > ultima_celula:
        display_board(board)
        input(f"{prefixo_erro}{erro_posicao_incorreta}\n{enter_para_continuar}")
        os.system('clear')
        continue
      else: ### Se o número existir, associa à variável 'move' a posição escolhida
        if user_input >= 1 and user_input <= 3:
          move_address = [0, user_input-1]
        elif user_input >= 4 and user_input <= 6:
          move_address = [1, user_input-4]
        elif user_input >= 7 and user_input <= 9:
          move_address = [2, user_input-7]

      move = board[ move_address[0] ][ move_address[1] ]

      if move == xis or move == circulo:
        display_board(board)
        input(f"{prefixo_erro}Choose a field not yet used!\n{enter_para_continuar}")
        os.system('clear')
        continue
      else:
        display_board(board)
        board[move_address[0]][move_address[1]] = circulo
        break

    except ValueError:
      display_board(board)
      input(f"{prefixo_erro}You must choose an integer number!\n{enter_para_continuar}")
      os.system('clear')
    except:
      display_board(board)
      input(f"{prefixo_erro}Uknown error. Please read the instructions.\n{enter_para_continuar}")
      os.system('clear')

  display_board(board)
  input("Jogada registrada.\nPressione [ENTER] para receber a jogada do computador")
  draw_move( board )


enter_move( board )

#def victory_for(board, sign):
## The function analyzes the board's status in order to check if 
## the player using 'O's or 'X's has won the game

