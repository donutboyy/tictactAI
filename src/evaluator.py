import sys
import math
sys.path.append('../src')
from board import *

def get_winner(board) -> str:
    row_winner = check_row_win(board)
    col_winner = check_col_win(board)
    diagonal_winner = check_diagonal_win(board)
    if not row_winner == "":
        return row_winner
    elif not col_winner == "":
        return col_winner
    elif not diagonal_winner == "":
        return diagonal_winner
    else:
        return ""

def has_winner(board) -> bool:
    return get_winner(board) != ""

def has_draw(board) -> bool:
    if not has_winner(board) and "" not in board:
        return True
    else: 
        return False

def check_row_win(board) -> str:
    x_count = 0
    o_count = 0
    winner = ""

    for row in range(3):
        x_count = 0
        o_count = 0

        for col in range(3):
            if board[row * 3 + col] == "X":
                x_count +=  1
            elif board[row * 3 + col] == "O":
                o_count += 1
            if x_count == 3: 
                winner = "X"
            elif o_count == 3: 
                winner = "O"
    
    return winner

def check_col_win(board) -> str:
    x_count = 0
    o_count = 0
    winner = ""

    for col in range(3):
        x_count = 0
        o_count = 0

        for row in range(3):
            if board[row * 3 + col] == "X":
                x_count += 1
            elif board[row * 3 + col] == "O":
                o_count += 1
            if x_count == 3:
                winner = "X"
            elif o_count == 3:
                winner = "O"

    return winner
        
def check_diagonal_win(board) -> str:
    if board[0] == "X" and board[4] == "X" and board[8] == "X":
        return "X"
    elif board[0] == "O" and board[4] == "O" and board[8] == "O":
        return "O"
    elif board[2] == "X" and board[4] == "X" and board[6] == "X":
        return "X"
    elif board[2] == "O" and board[4] == "O" and board[6] == "O":
        return "O"

    return ""
    
# X is maximizer, O is minimizer
def evaluate_board(board) -> int:
    if get_winner(board) == "X": return 10
    elif get_winner(board) == "O": return -10
    elif has_draw(board): return 0

# considers all possible game outcomes and returns the value of the board
def minimax(boardObj, isMaximizingPlayer, depth=0):
    score = evaluate_board(boardObj.view_board())

    # game ended with winner
    if score == 10:
        return score - depth

    if score == -10:
        return score + depth

    if has_draw(boardObj.view_board()):
        return 0

    # player X
    if isMaximizingPlayer:
        bestVal = -1000

        #check each move
        for i in range(9):
            if boardObj.view_board()[i] == "":
                boardObj.place_symbol(i, "X")

                #replace best value by calling minimax recursively on subsequent moves after this one
                bestVal = max(bestVal, minimax(boardObj, not isMaximizingPlayer, depth+1))
                
                #reverse move
                boardObj.remove_symbol(i)

        return bestVal

    # player O, minimizing player
    else:
        bestVal = 1000

        #check each move
        for i in range(9):
            if boardObj.view_board()[i] == "":
                boardObj.place_symbol(i, "O")

                #replace best value by calling minimax recursively on subsequent moves after this one
                bestVal = min(bestVal, minimax(boardObj, not isMaximizingPlayer, depth+1))
                
                #reverse move
                boardObj.remove_symbol(i)

        return bestVal

# returns best position to place symbol
def get_best_move(boardObj, isMaximizingPlayer) -> int:
    # player X
    if isMaximizingPlayer:
        bestVal = -1000
        bestMove = -1

        #check each move
        for i in range(9):
            if boardObj.view_board()[i] == "":
                boardObj.place_symbol(i, "X")

                #replace best value by calling minimax recursively on subsequent moves after this one
                moveVal = minimax(boardObj, not isMaximizingPlayer)
                
                #reverse move
                boardObj.remove_symbol(i)

                if moveVal > bestVal: 
                    bestVal = moveVal
                    bestMove = i

        return bestMove

    # player O, minimizing player
    else:
        bestVal = 1000
        bestMove = -1

        #check each move
        for i in range(9):
            if boardObj.view_board()[i] == "":
                boardObj.place_symbol(i, "O")

                #replace best value by calling minimax recursively on subsequent moves after this one
                moveVal = minimax(boardObj, not isMaximizingPlayer)
                
                #reverse move
                boardObj.remove_symbol(i)

                if moveVal < bestVal: 
                    bestVal = moveVal
                    bestMove = i

        return bestMove
