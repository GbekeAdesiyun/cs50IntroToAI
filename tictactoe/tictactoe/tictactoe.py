"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

# Dictionary to store actions in minimax alpha beta function
DictX = {}
DictO = {}

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
    if board == initial_state():
        return X
    elif phelp(board, X) < 3 and phelp(board,O) < 3 :
        if phelp(board,X) == phelp(board, O):
            return X
        else:
            return O
    elif phelp(board, X) >= 3 and phelp(board,O) >= 3:
        if phelp(board,X) == phelp(board, O):
           return X
        elif phelp(board,O) < phelp(board,X) and phelp(board,X) < 5:
            return O
    elif terminal(board) == False:
        return 0


#Helper function for player
def phelp(board,number):
    counted = board[0].count(number) + board[1].count(number) + board[2].count(number)
    return counted


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    print(board)
    if terminal(board) == False:
        return 0
    else:
        answer = []
        m = 0
        for i in board:
            for j in i:
                if board[i][j] == EMPTY:
                    answer[m] = (i,j)
                    m += 1
        return set(answer)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    print("result board", board)
    print("action ",action)
  
    # Deep copy of board
    new_board = copy.deepcopy(board)
    if board[action[0]][action[1]]:
        raise Exception
    else:
        new_board[action[0]][action[1]] = player(board)
        return new_board
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Variables to store number of "X" and "O" from board
    # "X" and "O" appearing horizontally
    Hnum_x, Hnum_o = 0,0

    """ Count number of X and O in the loop and check for
    "X" or "O" winning horizontally """
    count = 0
    for i in board:
        for j in range(len(i)):
            if board[count][j] == X:
                Hnum_x += 1
            elif board[count][j] == O:
                Hnum_o += 1
        count += 1
        if Hnum_x == 3:
            return X
        elif Hnum_o == 3:
            return O
        Hnum_x, Hnum_o = 0,0

 # Check for X or O winning vertically 
    if board[0][0] == X and board[1][0] == X and board[2][0] == X:
        return X
    elif board[0][0] == O and board[1][0] == O and board[2][0] == O:
        return X
    elif board[0][1] == X and board[1][1] == X and board[2][1] == X:
        return X
    elif board[0][1] == O and board[1][1] == O and board[2][1] == O:
        return X
    elif board[0][2] == X and board[1][2] == X and board[2][2] == X:
        return X
    elif board[0][2] == O and board[1][2] == O and board[2][2] == O:
        return X
    
    # Check for X or O winning diagonally
    else:
        if board[0][0] == X and board[1][1] == X and board[2][2] == X:
            return X
        elif board[0][0] == O and board[1][1] == O and board[2][2] == O:
            return X
        elif board[0][2] == X and board[1][1] == X and board[2][0] == X:
            return X
        elif board[0][2] == O and board[1][1] == O  and board[2][0] == O:
            return X
        

# Gbeke - need to check the for loop here
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Loop to check for if there is a tie in the game and the game is not over
    playvalue, count = 0,0 
    for i in board:
        j = 0
        for j in range(len(i)):
            if board[count][j] != EMPTY:
                playvalue += 1
            else:
                continue
        count += 1   
    # Check if X or O won the game
    if winner(board) == X or winner(board) == O:
        return True
    # Check if all cells of the game are filled
    elif playvalue == 9 and winner(board) == None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    playvalue = 0
    for i in board:
        for j in i:
            if board[i][j] != EMPTY:
                playvalue += 1
            else:
                continue

    if terminal(board) == True:
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0
    else:
        return None

# Reference: "Alpha–beta pruning"
# Wikepedia, 02-07-2020 . [Online]. Available:
# https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
# [Accessed : 12-08-2020]


# Mimimax helper function with alpha-beta pruning
def minimax_alpha_beta(board, alpha, beta, maximizingPlayer):
    if terminal(board) == True:
        return utility(board)

    # X player - maximizing player
    if maximizingPlayer == X:
        v = -math.inf
        for action in range(actions(board)):
            if v > max(v,minimax_alpha_beta(result(board, action), alpha, beta, maximizingPlayer)):
                DictX[action] = v
            v = max(v,minimax_alpha_beta(result(board, action), alpha, beta, maximizingPlayer))
            alpha = max(v,alpha)
            if beta < alpha:
                break
        for key, value in DictX.items():
            if value == v:
                return key
    else:
        v = math.inf
        for action in range(actions(board)):
            print(action)
            if v < min(v, minimax_alpha_beta(result(board, action),alpha,beta,maximizingPlayer)):
                DictO[action] = v
            v = min(v, minimax_alpha_beta(result(board, action),alpha,beta,maximizingPlayer))
            beta = min(v,beta)
            if beta > alpha:
                break
        for key, value in DictO.items():
            if value == v:
                return key

# Reference:
# "Minimax Algorithm in Game Theory | Set 4 (Alpha-Beta Pruning)"
# GeekforGeeks, 05-12-2019. [Online]. Available:
#  https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/
# [Accessed : 10-08-2020]
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Using the player fucntion to determine who the maximizing player is 
    maximizingPlayer = player(board)


    if terminal(board) == True:
        return None 
    elif player(board) == X:
        return minimax_alpha_beta(board, -math.inf, math.inf, maximizingPlayer)
    elif player(board) == O:
        return minimax_alpha_beta(board, -math.inf, math.inf, maximizingPlayer)
        




