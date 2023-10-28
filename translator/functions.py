from constants import NO_CARD, CARD_SUITS, CARD_VALUES, NUMBER_OF_CARDS, CARDS_SOURCE, CARDS_DEST

import numpy as np

# Convert given card to one hot encoded vector e.g. 7C = 01000000001000000
# Every digit is stored as a separate value in the array
def convert_card_to_one_hot_encoded_vector(card):
    suit = CARD_SUITS[card[-1]]
    value = CARD_VALUES[card[:-1]]
    vector = list(map(int, list(suit + value)))
    return vector

def convert_board_to_array_of_one_hot_encoded_values(board):
    # Fill entire array with no card symbol
    array_one_hot_encoded = np.full((8, 19, 17), fill_value=list(map(int, list(NO_CARD))))
    # Fill array with actual cards
    for i, column in enumerate(board):
        for j, card in enumerate(column):
            array_one_hot_encoded[i][j] = convert_card_to_one_hot_encoded_vector(card)

    return array_one_hot_encoded

def convert_free_cells_to_array_of_one_hot_encoded_values(free_cell):
    array_one_hot_encoded = np.full((4, 17), fill_value=list(map(int, list(NO_CARD))))
    for i, card in enumerate(free_cell):
        array_one_hot_encoded[i] = convert_card_to_one_hot_encoded_vector(card)

    return array_one_hot_encoded

def convert_heap_to_array_of_one_hot_encoded_values(heap):
    array_one_hot_encoded = np.full((4, 17), fill_value=list(map(int, list(NO_CARD))))
    for i, card in enumerate(heap):
        array_one_hot_encoded[i] = convert_card_to_one_hot_encoded_vector(card)

    return array_one_hot_encoded

def convert_game_output_to_model_input(board, free_cells, heap):
    board = convert_board_to_array_of_one_hot_encoded_values(board)
    free_cells = convert_free_cells_to_array_of_one_hot_encoded_values(free_cells)
    heap = convert_heap_to_array_of_one_hot_encoded_values(heap)

    return board, free_cells, heap

# Get the card that should be moved for game input
def get_source_card(board, free_cells, vector_no_cards, vector_source):
    no_cards_move = NUMBER_OF_CARDS[''.join(map(str, vector_no_cards))]

    conv_vector_source = CARDS_SOURCE[''.join(map(str, vector_source))]
    source, no_col_source = conv_vector_source[0], int(conv_vector_source[1]) - 1

    if source == 'F':
        return free_cells[no_col_source]
    elif source == 'C':
        return board[no_col_source][-no_cards_move]
    else:
        raise Exception("Illegal source")

# Get the card to which source card should be moved (or freecell or heap or empty column)
def get_dest_card(board, vector_dest):
    conv_vector_dest = CARDS_DEST[''.join(map(str, vector_dest))]
    dest, no_col_dest = conv_vector_dest[0], int(conv_vector_dest[1]) - 1

    if dest == 'S':
        return "S"
    elif dest == 'F':
        return "F"
    elif dest == 'C':
        if len(board[no_col_dest]) == 0:
            return '0'
        else:
            return board[no_col_dest][-1]
    else:
        raise Exception("Illegal destination")


def convert_model_output_to_game_input(board, free_cells, vector_no_cards, vector_source, vector_dest):
    source_card = get_source_card(board, free_cells, vector_no_cards, vector_source)
    dest_card = get_dest_card(board, vector_dest)

    return source_card, dest_card