
import math

def get_winner(board, square) -> str:
    return check_row_win(board, square)

def has_winner(board) -> bool:
    return get_winner(board) != ""

def check_row_win(board, index=0) -> str:
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
    
