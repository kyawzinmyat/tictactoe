"""
Tic Tac Toe Player
"""

import copy

import math

X = "X"
O = "O"
EMPTY = None


steps = 0


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
    """
    term = 0
    for row in board:
        term += row.count(EMPTY)
    if term:
        return X if term %2 != 0 else O
    return "The game is over"



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    set_of_actions = []
    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                set_of_actions.append((i, j))
    return set_of_actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_state = copy.deepcopy(board)
    if new_state[action[0]][action[1]]:
        return Exception
    new_state[action[0]][action[1]] = player(board)
    return new_state


def row_col_check(board):
    for index_col, row in enumerate(board):
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O
        result = ''
        for index_row, col in enumerate(row):
            try:
                result +=  board[index_row][index_col]
            except:
                pass
        if result == X*3:
            return X
        elif result == O*3:
            return O
    ## diagonal check
    diagonal = ''
    try:
        diagonal = board[0][0] + board[1][1] + board[2][2]
    except:
        pass
    if diagonal == 3 * X:
        return X
    elif diagonal == 3 * O:
            return O
    try:
        diagonal = board[2][0] + board[1][1] + board[0][2]
    except:
        pass
    if diagonal == 3 * X:
        return X
    elif diagonal == 3 * O:
            return O

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    return row_col_check(board)



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)
    if result == X:
        return 1
    elif result == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if not terminal(board):
        o_action = None
        value = -math.inf
        if player(board) == X:
            print(X)
            for action in actions(board):
                n_value = Min(result(board, action), 0)
                if n_value > value:
                    value = n_value
                    o_action = action
        value = math.inf
        if player(board) == O:
            print(O)
            for action in actions(board):
                n_value = Max(result(board, action), 0)
                if n_value < value:
                    value = n_value
                    o_action = action
        global steps
        print("Total steps ", steps)
        steps = 0
        return o_action


def Max(board, depth, alpha = -math.inf, beta = math.inf):
    global steps
    steps += 1
    if not terminal(board):
        value = -math.inf
        for action in actions(board):
            new_value = Min(result(board, action), depth + 1, alpha, beta) + depth
            if value < new_value:
                value = new_value
                alpha = new_value
            if beta < value:
                return value
        return value
    return utility(board)

def Min(board, depth, alpha = -math.inf, beta = math.inf):
    global steps
    steps += 1
    if not terminal(board):
        value = math.inf
        for action in actions(board):
            new_value = Max(result(board, action), depth, alpha, beta) - depth
            if value > new_value:
                value = new_value
                beta = new_value
            if alpha > value:
                return value
        return value
    return utility(board)


