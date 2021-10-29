from player import *
import evaluator

class Game():
    def __init__(self, playerX=Player("X"), playerO=Player("O")):
        self.winner = None
        self.playerX = playerX
        self.playerO = playerO
        self.board = Board()
        self.__turn_counter = 0
        self.__current_player = playerX

    def get_turn(self) -> int:
        return self.__turn_counter

    def get_current_player(self) -> Player:
        return self.__current_player

    def player_turn(self, position_index) -> bool:
        self.__current_player = self.playerX if self.__turn_counter % 2 == 0 else self.playerO
        successfully_place_symbol = self.__current_player.place_symbol_on_board(position_index, self.board)
        self.__turn_counter += 1 if successfully_place_symbol else 0
        return successfully_place_symbol
        
    def check_win(self) -> str:
        row_winner = evaluator.check_row_win(self.board.view_board())
        col_winner = evaluator.check_col_win(self.board.view_board())
        diagonal_winner = evaluator.check_diagonal_win(self.board.view_board())
        if not row_winner == "":
            return row_winner
        elif not col_winner == "":
            return col_winner
        elif not diagonal_winner == "":
            return diagonal_winner
        else:
            return ""

    
    
