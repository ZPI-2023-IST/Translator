from enum import Enum

# State of game from FreeCell game
class State(Enum):
    ONGOING = 0
    WON = 1
    LOST = 2

SIZE_BOARD = (8, 19, 17)
SIZE_FREE_CELL = (4, 17)
SIZE_HEAP = (4, 17)

# Used for scaling the reward
NO_ALL_CARDS = 52
MAX_DEPTH_SUM = 196

class CARD_LOCATIONS(Enum):
    COLUMN = "C"
    FREE_CELL = "F"
    HEAP = "S"
    EMPTY_COLUMN = "0"

# Constants used to translate game output into model input
NO_CARD = "00000000000000000"

CARD_SUITS= {
    "S": "1000",
    "C": "0100",
    "D": "0010",
    "H": "0001"
}

# T - Ten
CARD_VALUES = {
    "A": "1000000000000",
    "2": "0100000000000",
    "3": "0010000000000",
    "4": "0001000000000",
    "5": "0000100000000",
    "6": "0000010000000",
    "7": "0000001000000",
    "8": "0000000100000",
    "9": "0000000010000",
    "T": "0000000001000",
    "J": "0000000000100",
    "Q": "0000000000010",
    "K": "0000000000001"
}

# Constants used to translate model output to game input
NUMBER_OF_CARDS = {
    "10000": 1,
    "01000": 2,
    "00100": 3,
    "00010": 4,
    "00001": 5
}

CARDS_SOURCE = {
    "100000000000": "C1",
    "010000000000": "C2",
    "001000000000": "C3",
    "000100000000": "C4",
    "000010000000": "C5",
    "000001000000": "C6",
    "000000100000": "C7",
    "000000010000": "C8",
    "000000001000": "F1",
    "000000000100": "F2",
    "000000000010": "F3",
    "000000000001": "F4",
}

CARDS_DEST = {
    "1000000000": "C1",
    "0100000000": "C2",
    "0010000000": "C3",
    "0001000000": "C4",
    "0000100000": "C5",
    "0000010000": "C6",
    "0000001000": "C7",
    "0000000100": "C8",
    "0000000010": "F0",
    "0000000001": "S0",
}

# Constants used to translate moves into moves vector
REV_NUMBER_OF_CARDS = {v:k for k,v in NUMBER_OF_CARDS.items()}
REV_CARDS_SOURCE = {v:k for k,v in CARDS_SOURCE.items()}
REV_CARDS_DEST = {v:k for k,v in CARDS_DEST.items()}
