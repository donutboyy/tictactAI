from src.board import *
from src.player import *
from src.game import *
import pytest
import sys
sys.path.append('../src/tictactai/')

game : Game

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

def test_player_can_fill_row():
    game.player_turn(0)
    game.player_turn(8)
    game.player_turn(1)
    game.player_turn(7)
    game.player_turn(2)
    assert game.board.view_board()[0] == "X" and game.board.view_board()[
        1] == "X" and game.board.view_board()[2] == "X"

def test_player_wins_by_row_of_three():
    game.player_turn(3)
    game.player_turn(8)
    game.player_turn(4)
    game.player_turn(7)
    game.player_turn(5)
    assert game.check_win() == "X"

def test_player_wins_by_col_of_three():
    game.player_turn(0)
    game.player_turn(8)
    game.player_turn(3)
    game.player_turn(7)
    game.player_turn(6)
    assert game.check_win() == "X"

def test_player_wins_by_diagonal():
    game.player_turn(0)
    game.player_turn(2)
    game.player_turn(4)
    game.player_turn(7)
    game.player_turn(8)
    assert game.check_win() == "X"

def test_if_there_is_winner_then_game_over_is_true():
    game.player_turn(0)
    game.player_turn(2)
    game.player_turn(4)
    game.player_turn(7)
    game.player_turn(8)
    assert game.check_win() != "" and game.get_game_over()

def test_game_over_when_draw():
    game.player_turn(0)
    game.player_turn(1)
    game.player_turn(3)
    game.player_turn(4)
    game.player_turn(7)
    game.player_turn(6)
    game.player_turn(2)
    game.player_turn(5)
    game.player_turn(8)
    assert game.get_game_over() and game.check_win() == ""

def test_no_draw_when_game_not_over():
    game.player_turn(0)
    game.player_turn(1)
    game.player_turn(3)
    game.player_turn(4)
    game.player_turn(7)
    game.player_turn(6)
    game.player_turn(2)
    game.player_turn(5)
    assert not game.get_game_over() and game.check_win() == ""
