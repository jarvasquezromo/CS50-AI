"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
  
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

    

    return [[EMPTY, X, O],
            [O, X, EMPTY],
            [X, EMPTY, O]]


def player(board):
    """
    Returns player who has the next turn on a board.

    We have to count the empty spaces
    if empty space are odd, then Xs have to play
    else Os play
    """
    count = 0
    for row in board:
        count += row.count (EMPTY)

    if count % 2 == 1:
        return X
    else:
        return O
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = []

    for i in range (len (board)):
        for j in range (len (board[i])):
            if board[i][j] == EMPTY:
                moves.append ((i, j))
    
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # get the user
    user = player (board)

    # make the change
    board[action[0]][action[1]] = user

    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(len(board)):

        # Horizontal
        if (board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != EMPTY):
            return board[i][0]

        # Vertical
        if (board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] != EMPTY):
            return board[0][i]

    # Diagonal 1
    if (board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[1][1] != EMPTY):
        return board[1][1]

    # Diagonal 2
    if (board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] != EMPTY):
        return board[1][1]

    return EMPTY


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner (board) != EMPTY:
        # If a player winns, the game end
        return True

    for row in board:
        if EMPTY in row:
            # if exist an empty space, the game cotinue
            return False

    # if no empty space, then the game is over
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    user_winner = winner (board)

    if user_winner == X:
        return 1
    elif user_winner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    user = player (board)

    posible_actions = actions (board)

    # we creat a initial point ideal for compare
    value = -2 if user == X else 2
    best_option = (posible_actions[0], value)

    for action in posible_actions:
        if user == X:
            # we search the max_value
            value = min_value (result (copy(board), action))
            if value > best_option[1]:
                best_option = (action, value)

        elif user == O:
            # we search the min_value
            value = max_value (result (copy(board), action))
            if value < best_option[1]:
                best_option = (action, value)


    print("MINIMAX:", best_option)
    return best_option[0]
              

def max_value (state):
    if terminal (state):
        return utility (state)

    value = -10

    for action in actions (state):
        value = max (value, min_value(result(copy(state), action)))
    return value


def min_value (state):
    if terminal (state):
        return utility (state)

    value = 10

    for action in actions (state):
        value = min (value, max_value(result(copy(state), action)))
    return value


def copy (matrix):
  new_matrix = []
  for row in matrix:
      new_matrix.append (row.copy())

  return new_matrix

def print_table (board):
    for i in range (len (board)):
        for j in range (len (board[i])):
            if board[i][j] == EMPTY:
                print("-", end=" ")
            else:
                print(board[i][j], end=" ")
        print()

if __name__ == "__main__":
    from random import choice
  
    tablero = initial_state ()

    print_table (tablero)

    while not terminal(tablero):

        user = player (tablero)

        # posible_actions = actions (tablero)

        # move = choice (posible_actions)
        if user == X:
            i = int(input("Row:"))
            j = int(input("Col:"))

            move = (i, j)
        else:
            move = minimax (tablero)
      
        result (tablero, move)
      
        print("\n", user, "moves to", move)
        print_table (tablero)

        # print("Winner", winner (tablero))

    print ("The utility of the board is", utility (tablero))
