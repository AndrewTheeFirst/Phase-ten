from enum import Enum

class Faces(Enum):
    BACK = -1
    BLANK = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    ELEVEN = 11
    TWELVE = 12
    SKIP = 15
    WILD = 25

class Colors(Enum):
    NONE = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
    BLUE = 4
    ANY = 5

CARD_RENDERS = {Faces.ONE: "|    +    |\n|    |    |\n|    |    |\n|    |    |\n|    +    |",
               Faces.TWO: "|  ----+  |\n|      |  |\n|  +---+  |\n|  |      |\n|  +----  |",
               Faces.THREE: "|  ----+  |\n|      |  |\n|  ----+  |\n|      |  |\n|  ----+  |",
               Faces.FOUR: "|  +   +  |\n|  |   |  |\n|  +---+  |\n|      |  |\n|      +  |",
               Faces.FIVE: "|  +----  |\n|  |      |\n|  +---+  |\n|      |  |\n|  ----+  |",
               Faces.SIX: "|  +----  |\n|  |      |\n|  +---+  |\n|  |   |  |\n|  +---+  |",
               Faces.SEVEN: "|  +---+  |\n|  |   |  |\n|      +  |\n|      |  |\n|      +  |",
               Faces.EIGHT: "|  +---+  |\n|  |   |  |\n|  +---+  |\n|  |   |  |\n|  +---+  |",
               Faces.NINE: "|  +---+  |\n|  |   |  |\n|  +---+  |\n|      |  |\n|      +  |",
               Faces.TEN: "| + +---+ |\n| | |   | |\n| | |   | |\n| | |   | |\n| + +---+ |",
               Faces.ELEVEN: "|  +   +  |\n|  |   |  |\n|  |   |  |\n|  |   |  |\n|  +   +  |",
               Faces.TWELVE: "| + ----+ |\n| |     | |\n| | ----+ |\n| | |     |\n| + +---- |",
               Faces.SKIP: "|         |\n|         |\n| S K I P |\n|         |\n|         |",
               Faces.WILD: "|         |\n|         |\n| W I L D |\n|         |\n|         |",
               Faces.BACK: "|  P      |\n|   H     |\n|    A    |\n|     S   |\n|      E  |",
               Faces.BLANK: "|         |\n|         |\n|         |\n|         |\n|         |"}

CARD_TOP_BOT = "+---------+"

ANSI = "\x1b[{}m"
RED = ANSI.format(31)
GREEN = ANSI.format(32)
YELLOW = ANSI.format(33)
BLUE = ANSI.format(34)
CLEAR = ANSI.format(0)

PRINT_COLOR = {Colors.NONE: "",
               Colors.RED: RED,
               Colors.GREEN: GREEN,
               Colors.YELLOW: YELLOW,
               Colors.BLUE: BLUE,
               Colors.ANY: "",}

class Card:
    '''Represents phaseten phasecards'''
    def __init__(self, face: Faces, color: Colors):
        self.face = face
        self.color = color
        self._repr = color.name.lower()[0] + str(face.value) if face not in [Faces.WILD, Faces.SKIP] else face.name.lower()[0]
        
    def __str__(self):
        card = ""
        card += PRINT_COLOR[self.color] + CARD_TOP_BOT + CLEAR + '\n'
        card_render = CARD_RENDERS[self.face].split('\n')
        for card_line in card_render:
            card += PRINT_COLOR[self.color] + card_line[0] + CLEAR +\
                    card_line[1:-1] +\
                    PRINT_COLOR[self.color] + card_line[-1] + CLEAR + '\n'
        card += PRINT_COLOR[self.color] + CARD_TOP_BOT + CLEAR + '\n'
        return card

    def __repr__(self):
        return f"Card({self.face}, {self.color})"

    def value(self) -> int:
        return self.face.value