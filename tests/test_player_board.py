from board import *
from player import *
import pytest
import sys
sys.path.append('../src')

board = None
player = None

@pytest.fixture(autouse=True)
def test_init():
    global board, player
    board = Board()
    player = Player()

def test_player_can_place_symbol_on_board():
    player.place_symbol_on_board(2, board)
    assert board.view_board()[2] == player.get_symbol()
