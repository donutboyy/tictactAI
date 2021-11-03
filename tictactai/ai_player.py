from tictactai.player import *
from tictactai.evaluator import *

class AI_Player(Player):
    def __init__(self, symbol="O"):
        super().__init__(self)
        self.__symbol = symbol

    def place_symbol_on_board(self, board) -> int:
        bestMove = get_best_move(board, False)
        board.place_symbol(bestMove, self.__symbol)
        return bestMove

    def get_symbol(self) -> str:
        return self.__symbol
