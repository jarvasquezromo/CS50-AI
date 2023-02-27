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
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

def print_table (board):
    for i in range (len (board)):
        for j in range (len (board[i])):
            if board[i][j] == EMPTY:
                print("-", end=" ")
            else:
                print(board[i][j], end=" ")
        print()

if __name__ == "__main__":
    tablero = initial_state ()

    print_table (tablero)
    
    posible_actions = actions (tablero)

    print (posible_actions)

    print (result (tablero, posible_actions[0]))




