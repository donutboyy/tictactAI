from src.player import *
from src.ai_player import *
from src.evaluator import *

class Game():
    def __init__(self, playerX=Player("X"), playerO=Player("O")):
        self.winner = None
        self.playerX = playerX
        self.playerO = playerO
        self.board = Board()
        self.__turn_counter = 0
        self.__current_player = playerX
        self.__game_over = False

    def get_turn(self) -> int:
        return self.__turn_counter

    def get_current_player(self) -> Player:
        return self.__current_player

    def player_turn(self, position_index) -> bool:
        if not self.__game_over:
            self.__current_player = self.playerX if self.__turn_counter % 2 == 0 else self.playerO
            successfully_place_symbol = self.__current_player.place_symbol_on_board(position_index, self.board)
            self.__turn_counter += 1 if successfully_place_symbol else 0
            self.__game_over = has_winner(self.board.view_board()) or has_draw(self.board.view_board())
            return successfully_place_symbol
        else: return False
        
    def ai_player_turn(self) -> int:
        if not self.__game_over:
            self.__current_player = self.playerX if self.__turn_counter % 2 == 0 else self.playerO
            bestMove = self.playerO.place_symbol_on_board(self.board)
            self.__turn_counter += 1
            self.__game_over = has_winner(self.board.view_board()) or has_draw(self.board.view_board())
            return bestMove

    def get_game_over(self) -> bool:
        return self.__game_over

    def check_win(self) -> str:
        winner = get_winner(self.board.view_board())
        self.__game_over = has_winner(self.board.view_board()) or has_draw(self.board.view_board())
        return winner

    
    
