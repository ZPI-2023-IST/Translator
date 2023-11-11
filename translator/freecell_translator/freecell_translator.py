from ..abstract_translator.abstract_translator import AbstractTranslator
from .functions import *

# WHOLE CLASS TO POTENTIALLY FIX AFTER CONNECTING TO GAME
class FreecellTranslator(AbstractTranslator):
    def __init__(self, game=None):
        super().__init__(game)
        self.all_moves = self._get_all_moves_dict()
        self.all_moves_rev = {v:k for k,v in self.all_moves.items()}

    def make_move(self, ml_no_cards, ml_src, ml_dst):
        board, free_cells, _ = self.game.get_board()

        src_card = get_source_card(board, free_cells, ml_no_cards, ml_src)
        dst_card = get_dest_card(board, ml_dst)

        self.game.make_move((src_card, dst_card))

    def get_moves(self):
        board, free_cells, _ = self.game.get_board()
        moves = self.game.get_moves()

        move_vectors = []
        for move in moves:
            src_card, dst_card = move
            cards_moved_vector, src_vector = get_source_card_vector(board, free_cells, src_card)
            dst_vector = get_dest_card_vector(board, dst_card)
            move_vectors.append((cards_moved_vector, src_vector, dst_vector))

        return move_vectors

    def get_board(self):
        board, free_cells, heap = self.game.get_board()

        board = convert_board_to_ar_ohe(board)
        free_cells = convert_fc_to_ar_ohe(free_cells)
        heap = convert_heap_to_ar_ohe(heap)

        return board, free_cells, heap

    def get_state(self):
        return self.game.get_state()
    
    def start_game(self):
        self.game.start_game()

    # TO IMPLEMENT AFTER CONNECTING TO GAME
    def get_reward(self):
        return 0
    
    def _get_all_moves_dict(self):
        result_dict = {}
        n_move = 0

        # Perform all one move cards 
        for src in CARDS_SOURCE.keys():
            for dst in CARDS_DEST.keys():
                no_cards = REV_NUMBER_OF_CARDS[1]
                result_dict[(no_cards, src, dst)] = n_move
                n_move +=1

        # Perform all more than one card moves
        for no_cards_k, no_cards_v in NUMBER_OF_CARDS.items():
            if no_cards_v != 1:
                for src_k, src_v in CARDS_SOURCE.items():
                    if src_v[0] == CARD_LOCATIONS.COLUMN.value:
                        for dst_k, dst_v in CARDS_DEST.items():
                            if dst_v[0] == CARD_LOCATIONS.COLUMN.value:
                                result_dict[(no_cards_k, src_k, dst_k)] = n_move
                                n_move += 1

        return result_dict 
