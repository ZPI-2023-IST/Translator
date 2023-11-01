from translator.freecell_translator.freecell_translator import FreecellTranslator

class Game:
    def __init__(self):
        self.board = [
            ["AH", "2H"],
            ["3S", "4S", "5S", "6S", "9C", "10C", "BC", "QC", "KC"],
            [],
            ["7C", "8C"],
            [],
            ["AD"],
            [],
            []
        ]

        self.freecells = [
            "9S"
        ]

        self.heap = [
            "AC",
            "AS"
        ]


    def make_move(self, move):
        pass

    def get_moves(self):
        return [("2H", "0"), ("10C", "8C"), ("AD", "F"), ("AD", "S"), ("9S", "0"), ("BC", "AD")]


    def get_board(self):
        return self.board, self.freecells, self.heap

    def get_state(self):
        return "Active"
        
    def start_game(self):
        pass

ml_no_cards = [
    0,
    1,
    0,
    0,
    0
]

ml_src = [
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

ml_dst = [
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

game = Game()
fc_translator = FreecellTranslator(game)
fc_translator.make_move(ml_no_cards, ml_src, ml_dst)
print(fc_translator.get_moves())
print(fc_translator.get_board())
print(fc_translator.get_state())
fc_translator.start_game()
print(fc_translator.get_reward())
