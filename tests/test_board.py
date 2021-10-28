import pytest
import sys
sys.path.append('../src')
from board import *

board = None

@pytest.fixture(autouse=True)
def test_init():
    global board
    board = Board()

def test_starts_empty():
    assert all(x is "" for x in board.view_board())

def test_can_place_symbol_on_board():
    board.place_symbol(1, "X")
    assert board.view_board()[1] == "X"

def test_cannot_replace_symbol_with_symbol():
    board.place_symbol(1, "X")
    board.place_symbol(1, "O")
    assert board.view_board()[1] == "X"

def test_exception_when_attempt_to_place_symbol_out_of_board_index_range():
    with pytest.raises(Exception) as e_info:
        board.place_symbol(10, "X")
