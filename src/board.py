from typing import List

class Board():
    def __init__(self):
        self.__board = ["", "", "",
                        "", "", "",
                        "", "", ""]
                        
    def view_board(self) -> List[str]:
        return self.__board.copy()
    
    def place_symbol(self, index, symbol) -> bool:
        if self.__board[index] == "":
            self.__board[index] = symbol
            return True
        else:
            return False

    def set_board(self, boardList):
        self.__board = boardList

    def remove_symbol(self, index) -> bool:
        if not self.__board[index] == "":
            self.__board[index] = ""
            return True
        else:
            return False

    def __str__(self):
        return self.__board.__str__()
