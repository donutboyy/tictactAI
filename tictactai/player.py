from tictactai.board import *

class Player():
    def __init__(self, symbol="X"):
        self.__symbol = symbol

    def place_symbol_on_board(self, index, board) -> bool:
        return board.place_symbol(index, self.__symbol)

    def get_symbol(self) -> str:
        return self.__symbol