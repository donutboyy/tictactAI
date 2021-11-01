from typing import List

class Board():
    def __init__(self):
        self.__board = ["", "", "",
                        "", "", "",
                        "", "", ""]
                        
    def view_board(self) -> List[str]:
        temp_board = self.__board
        return temp_board
    
    def place_symbol(self, index, symbol) -> bool:
        if self.__board[index] == "":
            self.__board[index] = symbol
            return True
        else:
            return False


    
