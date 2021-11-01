import pytest
import sys
sys.path.append('../src')
import evaluator
from board import *

board = None

@pytest.fixture(autouse=True)
def test_init():
    global board
    board = Board()

def test_return_minus_10_when_o_wins():
    board.set_board(["X", "X", "O",
                    "", "O", "X",
                    "O", "", "X"])
    assert evaluator.evaluate_board(board.view_board()) == -10

def test_return_10_when_x_wins():
    board.set_board(["X", "X", "X",
                    "", "O", "",
                    "O", "", ""])
    assert evaluator.evaluate_board(board.view_board()) == 10

def test_return_0_when_tied():
    board.set_board(["X", "O", "X",
                    "X", "O", "O",
                    "O", "X", "O"])
    assert evaluator.evaluate_board(board.view_board()) == 0

def test_minimax_returns_10_when_X_is_one_move_away_from_winning():
    board.set_board(["X", "O", "",
                    "X", "O", "",
                    "", "", ""])
    assert evaluator.minimax(board, True) == 9

def test_minimax_returns_minus_11_when_O_is_one_move_away_from_winning():
    board.set_board(["X", "O", "X",
                    "X", "O", "",
                    "", "", ""])
    assert evaluator.minimax(board, False) == -9

def test_minimax_returns_0_when_tied():
    board.set_board(["X", "O", "X",
                    "X", "O", "O",
                    "O", "X", "O"])
    assert evaluator.minimax(board, True) == 0

def test_get_best_move_should_be_6_for_X():
    board.set_board(["X", "O", "",
                    "X", "O", "",
                    "", "", ""])
    assert evaluator.get_best_move(board, True) == 6

def test_get_best_move_should_be_7_for_O():
    board.set_board(["X", "O", "",
                    "X", "O", "",
                    "", "", ""])
    assert evaluator.get_best_move(board, False) == 7

def test_get_best_move_should_be_6_for_O():
    board.set_board(["O", "X", "",
                    "O", "X", "",
                    "", "", ""])
    assert evaluator.get_best_move(board, False) == 6

def test_get_best_move_should_be_3_for_O():
    board.set_board(["O", "", "",
                    "", "X", "X",
                    "", "", ""])
    assert evaluator.get_best_move(board, False) == 3

def test_get_best_move_should_be_3_for_X():
    board.set_board(["X", "", "",
                    "", "O", "O",
                    "X", "", ""])
    assert evaluator.get_best_move(board, True) == 3