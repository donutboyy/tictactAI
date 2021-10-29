from board import *
from player import *
from game import *
import pytest
import sys
sys.path.append('../src')

game = None

@pytest.fixture(autouse=True)
def test_init():
    global game
    game = Game()

def test_player_can_place_symbol_on_board():
    game.player_turn(2)
    assert game.board.view_board()[2] == game.playerX.get_symbol()

def test_turn_count_increases_after_turn():
    game.player_turn(2)
    assert game.get_turn() == 1

def test_turn_count_does_not_increase_after_attempting_to_replace_symbol():
    game.player_turn(2)
    game.player_turn(2)
    assert game.get_turn() == 1

def test_player_cannot_go_twice_in_a_row():
    game.player_turn(2)
    first_p = game.get_current_player()
    game.player_turn(3)
    second_p = game.get_current_player()
    assert not first_p == second_p

def test_exception_when_attempt_to_place_symbol_out_of_board_index_range():
    with pytest.raises(Exception):
        game.player_turn(10)
