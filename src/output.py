from re import I
import sys
from asciimatics.effects import Background, Cycle, Stars, Print, Sprite
from asciimatics.renderers import FigletText, Box, StaticRenderer, SpeechBubble
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
from asciimatics.paths import DynamicPath
from asciimatics.event import KeyboardEvent, MouseEvent
import evaluator
from game import *
import ai_player

symbol_placer = None
current_turn = 0
bigBoxLength = 0

game = Game(playerO = ai_player.AI_Player())

class MouseController(DynamicPath):
    def __init__(self, sprite, scene, x, y):
        super(MouseController, self).__init__(scene, x, y)
        self._sprite = sprite

    def process_event(self, event):
        if isinstance(event, MouseEvent):
            self._x = event.x
            self._y = event.y
            if event.buttons & MouseEvent.LEFT_CLICK != 0:
                # Try to whack the other sprites when mouse is clicked
                self._sprite.place_symbol()
        else:
            return event

class SymbolPlacer(Sprite):
    def __init__(self, screen):
        """
        See :py:obj:`.Sprite` for details.
        """
        super(SymbolPlacer, self).__init__(
            screen,
            renderer_dict={
                "default": StaticRenderer(images=["X"])
            },
            path=MouseController(
                self, screen, screen.width // 2, screen.height // 2),
            colour=Screen.COLOUR_RED)

    def place_symbol(self):
        global board_vals

        if game.get_game_over():
            return

        x, y = self._path.next_pos()
        symbolX, symbolY = 0, 0
        boxOriginX = int(self._screen.width / 2 - bigBoxLength / 2 * 2)
        boxOriginY = int(self._screen.height / 2 - bigBoxLength / 2)
        validPos = True

        this_turn_board_row = 0
        this_turn_board_col = 0
        if x > boxOriginX and x < boxOriginX + bigBoxLength * 2:
            if x < int(boxOriginX + bigBoxLength / 3 * 2):
                this_turn_board_col = 0
                symbolX = int(boxOriginX + bigBoxLength / 6 * 2)
            elif x > int(boxOriginX + bigBoxLength * 2 / 3 * 2):
                this_turn_board_col = 2
                symbolX = int(boxOriginX + bigBoxLength * 5 / 6 * 2)
            else:
                this_turn_board_col = 1
                symbolX = int(boxOriginX + bigBoxLength / 2 * 2)
        else:
            validPos = False
        
        if y > boxOriginY and y < boxOriginY + bigBoxLength:
            if y < int(boxOriginY + bigBoxLength / 3):
                this_turn_board_row = 0
                symbolY = int(boxOriginY + bigBoxLength / 6)
            elif y > int(boxOriginY + bigBoxLength * 2 / 3):
                this_turn_board_row = 2
                symbolY = int(boxOriginY + bigBoxLength * 5 / 6)
            else:
                this_turn_board_row = 1
                symbolY = int(boxOriginY + bigBoxLength / 2)
        else:
            validPos = False

        selected_square = 3 * (this_turn_board_row) + this_turn_board_col
        if validPos and game.player_turn(selected_square):
            if not game.get_game_over():
                game.ai_player_turn()

            self.print_board()

        if game.check_win() != "":
            self._scene.add_effect(Print(self._screen,
            FigletText("Winner is: " + str(game.check_win())),
            int(bigBoxLength * 9 / 8), transparent=False))
        elif game.get_game_over():
            self._scene.add_effect(Print(self._screen,
            FigletText("Nobody wins"),
            int(bigBoxLength * 9 / 8), transparent=False))

    def print_board(self):
        boxOriginX = int(self._screen.width / 2 - bigBoxLength / 2 * 2)
        boxOriginY = int(self._screen.height / 2 - bigBoxLength / 2)
        symbolX, symbolY = 0, 0

        for i in range(9):
            # get screen pos of col
            if i % 3 == 0:
                symbolX = int(boxOriginX + bigBoxLength / 6 * 2)
            elif i % 3 == 1:
                symbolX = int(boxOriginX + bigBoxLength / 2 * 2)
            elif i % 3 == 2:
                symbolX = int(boxOriginX + bigBoxLength * 5 / 6 * 2)

            # get screen pos of row
            if i / 3 == 0:
                symbolY = int(boxOriginY + bigBoxLength / 6)
            elif i / 3 == 1:
                symbolY = int(boxOriginY + bigBoxLength / 2)
            elif i / 3 == 2:
                symbolY = int(boxOriginY + bigBoxLength * 5 / 6)

            self._scene.add_effect(Print(self._screen,
                FigletText(game.board.view_board()[i]),
                symbolY-4, symbolX-2))
        
        

        


def demo(screen):
    global symbol_placer, bigBoxLength
    symbol_placer = SymbolPlacer(screen)
    bigBoxLength = int(screen.width / 4 * 3) if screen.width < screen.height else int(screen.height / 4 * 3)
    effects = [
        Print(screen,
            Box(bigBoxLength * 2, bigBoxLength),
            int(bigBoxLength / 8)),
        Print(screen,
            FigletText("tic tac toe"),
            int(bigBoxLength * 9 / 8)),
        symbol_placer
    ]
    screen.play([Scene(effects, 500)])

if __name__ == "__main__":
    while True:
        try:
            Screen.wrapper(demo)
            sys.exit(0)
        except ResizeScreenError:
            pass