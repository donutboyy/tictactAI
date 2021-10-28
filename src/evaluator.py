
import math

def get_winner(board, square) -> str:
    return check_row_win(board, square)

def has_winner(board) -> bool:
    return get_winner(board) != ""

def check_row_win(board, square) -> str:
    '''x_count = 0
    o_count = 0
    winner = ""

    for row in range(len(board)):
        x_count = 0
        o_count = 0

        for col in range(len(board[0])):
            if board[row][col] == "X":
                x_count += 1
            elif board[row][col] == "O":
                o_count += 1
            if x_count == 3: 
                winner = "X"
            elif o_count == 3: 
                winner = "O"
    
    return winner'''
    # check the row
    row_ind = math.floor(square / 3)
    row = board[row_ind*3:(row_ind+1)*3]
    # print('row', row)
    if all([s == "X" for s in row]):
        return "X"
    if all([s == "O" for s in row]):
        return "O"
    return ""

def check_col_win(board) -> str:
    for row in board:
        x_count = 0
        o_count = 0

        for col in row:
            if col == "X":
                x_count += 1
            elif col == "O":
                o_count += 1
        
        if x_count == 3: return "X"
        elif o_count == 3: return "O"
        else: return ""
        