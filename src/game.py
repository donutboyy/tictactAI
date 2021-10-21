import sys
from asciimatics.effects import Cycle, Stars, Print
from asciimatics.renderers import FigletText, Box
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError

def demo(screen):
    bigBoxLength = int(screen.width / 4 * 3) if screen.width < screen.height else int(screen.height / 4 * 3)
    effects = [
        Print(screen,
            Box(bigBoxLength * 2, bigBoxLength),
            int(bigBoxLength / 8)),
        Print(screen,
            FigletText("tic tac toe"),
            int(screen.height * 13/16))
    ]
    screen.play([Scene(effects, 500)])

while True:
    try:
        Screen.wrapper(demo)
        sys.exit(0)
    except ResizeScreenError:
        pass