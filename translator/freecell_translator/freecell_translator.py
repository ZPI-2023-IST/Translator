from ..abstract_translator.abstract_translator import AbstractTranslator
from .functions import *

class FreecellTranslator(AbstractTranslator):
    def __init__(self, game=None):
        super().__init__(game)
        # ML vectors mapped to given index
        self.all_moves = self._get_all_moves_dict()
        self.all_moves_rev = {v:k for k,v in self.all_moves.items()}
        self.config_model = {
            "n_observations": np.prod(SIZE_BOARD) + np.prod(SIZE_FREE_CELL) + np.prod(SIZE_HEAP),
            "n_actions": len(self.all_moves)
        }

        # Store destination card for future reward calculation
        self.dst_card = None

    def make_move(self, move):
        ml_no_cards, ml_src, ml_dst = self.all_moves_rev[move]
        board, free_cells, _ = self.game.get_board()

        src_card = get_source_card(board, free_cells, ml_no_cards, ml_src)
        dst_card = get_dest_card(board, ml_dst)

        self.game.make_move((src_card, dst_card))

    # Returns list of index of all moves
    def get_moves(self):
        board, free_cells, _ = self.game.get_board()
        moves = self.game.get_moves()

        move_vectors = []
        for move in moves:
            src_card, dst_card = move
            # Store destination card for future reward calculation
            self.dst_card = dst_card

            cards_moved_vector, src_vector = get_source_card_vector(board, free_cells, src_card)
            dst_vector = get_dest_card_vector(board, dst_card)

            move_id = self.all_moves[(cards_moved_vector, src_vector, dst_vector)]
            move_vectors.append(move_id)

        return move_vectors

    # Our ml model takes one dimensional inputs
    def get_board(self):
        board, free_cells, heap = self.game.get_board()

        board = convert_board_to_ar_ohe(board)
        free_cells = convert_fc_to_ar_ohe(free_cells)
        heap = convert_heap_to_ar_ohe(heap)

        return np.concatenate((board, free_cells, heap)).tolist()

    def get_state(self):
        return self.game.get_state()
    
    def start_game(self):
        self.game.start_game()

    def get_reward(self):
        state = self.game.get_state()
        if state.value == State.WON.value:
            return 5
        elif state.value == State.LOST.value:
            return -5
        else:
            if self.dst_card == CARD_LOCATIONS.HEAP.value:
                return 1
            else:
                return 0   
    
    def get_config_model(self):
        return self.config_model
    
    def _get_all_moves_dict(self):
        result_dict = {}
        n_move = 0

        # Perform all one move cards 
        for src, src_v in CARDS_SOURCE.items():
            for dst, dst_v in CARDS_DEST.items():
                if not self._is_the_same_col(src_v, dst_v):
                    no_cards = REV_NUMBER_OF_CARDS[1]
                    result_dict[(no_cards, src, dst)] = n_move
                    n_move += 1

        return result_dict 
    
    def _is_the_same_col(self, src, dst):
        if src == dst:
            return True
        
        if src[0] == CARD_LOCATIONS.FREE_CELL.value and dst[0] == CARD_LOCATIONS.FREE_CELL.value:
            return True
        
        return False
