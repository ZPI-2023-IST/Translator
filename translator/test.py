from functions import convert_to_game_vector

test_board = [
    ["AH", "2H"],
    ["3S", "4S", "5S", "6S", "9C", "10C", "BC", "QC", "KC"],
    [],
    ["7C", "8C"],
    [],
    ["AD"],
    [],
    []
]

test_freecell = [
    "9S",
]

test_heap = [
    "AC",
    "AS",
    "4C"
]

board, freecell, heap = convert_to_game_vector(test_board, test_freecell, test_heap)
print(heap)