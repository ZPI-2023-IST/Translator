from ..abstract_translator.abstract_translator import AbstractTranslator
from .functions import *

class FreecellTranslator(AbstractTranslator):
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

        board = convert_board_to_array_of_one_hot_encoded_values(board)
        free_cells = convert_free_cells_to_array_of_one_hot_encoded_values(free_cells)
        heap = convert_heap_to_array_of_one_hot_encoded_values(heap)

        return board, free_cells, heap

    def get_state(self):
        return self.game.get_state()
    
    def start_game(self):
        self.game.start_game()
