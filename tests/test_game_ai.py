from board import *
from player import *
from ai_player import *
from game import *
import pytest
import sys
sys.path.append('../src')

game = None

@pytest.fixture(autouse=True)
def test_init():
    global game
    game = Game(playerO=AI_Player())

def test_ai_win():
    game.player_turn(0)
    print(game.ai_player_turn())
    game.player_turn(6)
    print(game.ai_player_turn())
    game.player_turn(2)
    print(game.ai_player_turn())
    print(game.board.view_board())
    assert game.get_game_over() and game.check_win() == "O"