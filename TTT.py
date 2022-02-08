board = [['_','_','_'],
         ['_','_','_'],
         ['_','_','_']]

symbols = ['X', 'O']
turn = 0

# Prints the board
def print_board():
  for row in board:
    for col in row:
      print(col, end=' ')
    print()

# Inserts a move at a given row & column
def make_move(row, col, symbol):
  board[row][col] = symbol

# Returns true when the game is over 
# Note: Just a stub. Doesn't work yet
def is_game_over():
  return False

# Alternates the turn between 0 and 1
def change_turn():
  global turn
  turn = (turn + 1) % 2

while not is_game_over():
  # Print the board and whose turn it is
  print_board()
  print('Player {}'.format(turn+1))

  # Get the user input
  row_choice = int(input('Which row would you like to choose? '))
  col_choice = int(input('Which row would you like to choose? '))

  # Put their move on the board
  make_move(row_choice, col_choice, symbols[turn])

  # Next turn
  change_turn()