"""
Tic Tac Toe Player
"""

import math
import copy

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
    -> Returns O if the game is over.
    """
    x_count = count_actions(board)[0]
    o_count = count_actions(board)[1]
    if x_count == o_count + 1:
        return O
    elif x_count == o_count:
        return X

def count_actions(board):
    """
    Returns the number of X's and O's as a tuple.
    """
    x_count = 0
    o_count = 0
    for row in board:
        for action in row:
            if action == X:
                x_count += 1
            elif action == O:
                o_count += 1
    return (x_count, o_count)   


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    actions = ()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action = (i,j)
                actions_set.add(action)

    return actions_set

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    Still need to figure out how to raise exceptions. 
    """
    new_board = copy.deepcopy(board)
    turn = player(board)
    #print(turn)
    if new_board[action[0]][action[1]] == EMPTY:
        new_board[action[0]][action[1]] = turn
    else:
        print("Illegal Move")
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return board[0][i]
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    x = count_actions(board)[0]
    o = count_actions(board)[1]
    if x + o == 9:
        return True
    if winner(board) == X or winner(board) == O:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    move = ()
        
    if terminal(board):
        return None
    
    if player(board) == X:
        move = maxvalue(board)
    else:
        move = minvalue(board)
    #print(move)
    return move[1]

def maxvalue(board):
    """
    """
    if terminal(board):
        return utility(board), (None, None)
    v = float("-inf")
    next_x = ()
    for action in actions(board):
        #v = max(v, minvalue(result(board, action)))
        temp = minvalue(result(board, action))
        if temp[0] > v:
            v = temp[0]
            next_x = action
    return v, next_x



def minvalue(board):
    """
    """
    if terminal(board):
        return utility(board), (None, None)
    v = float("inf")
    next_o = ()
    for action in actions(board):
        temp = maxvalue(result(board, action))
        if temp[0] < v:
            v = temp[0]
            next_o = action
    return v, next_o