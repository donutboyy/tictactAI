from player import *
import evaluator

class AI_Player(Player):
    def __init__(self, symbol="O"):
        super().__init__(self)
        self.__symbol = symbol

    def place_symbol_on_board(self, board) -> int:
        bestMove = evaluator.get_best_move(board, False)
        board.place_symbol(bestMove, self.__symbol)
        return bestMove

    def get_symbol(self) -> str:
        return self.__symbol