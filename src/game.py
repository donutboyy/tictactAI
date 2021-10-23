import sys
from asciimatics.effects import Cycle, Stars, Print, Sprite
from asciimatics.renderers import FigletText, Box, StaticRenderer, SpeechBubble
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
from asciimatics.paths import DynamicPath
from asciimatics.event import KeyboardEvent, MouseEvent

symbol_placer = None
current_turn = 0
bigBoxLength = 0

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
                self._sprite.place_symbol(str(self._x) + " " + str(self._y))
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

    def place_symbol(self, message):
        x, y = self._path.next_pos()
        symbolX, symbolY = 0, 0
        boxOriginX = int(self._screen.width / 2 - bigBoxLength / 2 * 2)
        boxOriginY = int(self._screen.height / 2 - bigBoxLength / 2)
        validPos = True
        if x > boxOriginX and x < boxOriginX + bigBoxLength * 2:
            if x < int(boxOriginX + bigBoxLength / 3 * 2):
                symbolX = int(boxOriginX + bigBoxLength / 6 * 2)
            elif x > int(boxOriginX + bigBoxLength * 2 / 3 * 2):
                symbolX = int(boxOriginX + bigBoxLength * 5 / 6 * 2)
            else:
                symbolX = int(boxOriginX + bigBoxLength / 2 * 2)
        else:
            validPos = False
        
        if y > boxOriginY and y < boxOriginY + bigBoxLength:
            if y < int(boxOriginY + bigBoxLength / 3):
                symbolY = int(boxOriginY + bigBoxLength / 6)
            elif y > int(boxOriginY + bigBoxLength * 2 / 3):
                symbolY = int(boxOriginY + bigBoxLength * 5 / 6)
            else:
                symbolY = int(boxOriginY + bigBoxLength / 2)
        else:
            validPos = False

        if validPos:
            self._scene.add_effect(Print(self._screen,
                FigletText("O"),
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