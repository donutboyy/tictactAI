from src.player import *
from src.evaluator import *

class AI_Player(Player):
    def __init__(self, symbol="O"):
        self.__symbol = symbol
        super().__init__(self.__symbol)

    def place_symbol_on_board(self, board) -> int:
        bestMove = get_best_move(board, False)
        board.place_symbol(bestMove, self.__symbol)
        return bestMove

    def get_symbol(self) -> str:
        return self.__symbol
