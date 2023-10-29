from translator.freecell_translator.freecell_translator import FreecellTranslator

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

test_freecells = [
    "9S",
]

test_heap = [
    "AC",
    "AS"
]

test_no_cards = [
    0,
    1,
    0,
    0,
    0
]

test_source = [
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
]

test_destination = [
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
]

game_output = (test_board, test_freecells, test_heap)
model_output = (test_no_cards, test_source, test_destination)

FreecellTranslator()

a = FreecellTranslator.convert_game_output_to_model_input(game_output)

d = FreecellTranslator.convert_model_output_to_game_input(game_output, model_output)

print(d)