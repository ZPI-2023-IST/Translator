from .constants import *

import numpy as np

# Convert given card to one hot encoded vector e.g. 7C = 01000000001000000
# Every digit is stored as a separate value in the array
def convert_card_to_ohe_vector(card):
    card = str(card).upper()
    suit = CARD_SUITS[card[1]]
    value = CARD_VALUES[card[0]]
    vector = list(map(int, list(suit + value)))
    return vector

def convert_board_to_ar_ohe(board):
    # Fill entire array with no card symbol
    array_one_hot_encoded = np.full(SIZE_BOARD, fill_value=list(map(int, list(NO_CARD))))
    # Fill array with actual cards
    for i, column in enumerate(board):
        for j, card in enumerate(column):
            array_one_hot_encoded[i][j] = convert_card_to_ohe_vector(card)

    return array_one_hot_encoded.flatten()

def convert_fc_to_ar_ohe(free_cell):
    array_one_hot_encoded = np.full(SIZE_FREE_CELL, fill_value=list(map(int, list(NO_CARD))))
    for i, card in enumerate(free_cell):
        if card is None:
            array_one_hot_encoded[i] = NO_CARD
        else:
            array_one_hot_encoded[i] = convert_card_to_ohe_vector(card)

    return array_one_hot_encoded.flatten()

def convert_heap_to_ar_ohe(heap):
    array_one_hot_encoded = np.full(SIZE_HEAP, fill_value=list(map(int, list(NO_CARD))))
    for i, card in enumerate(heap):
        if card is None:
            array_one_hot_encoded[i] = NO_CARD
        else:
            array_one_hot_encoded[i] = convert_card_to_ohe_vector(card)

    return array_one_hot_encoded.flatten()

# Get the card that should be moved for game input
def get_source_card(board, free_cells, vector_no_cards, vector_source):
    no_cards_move = NUMBER_OF_CARDS[''.join(map(str, vector_no_cards))]

    conv_vector_source = CARDS_SOURCE[''.join(map(str, vector_source))]
    source, no_col_source = conv_vector_source[0], int(conv_vector_source[1]) - 1

    if source == CARD_LOCATIONS.FREE_CELL.value:
        return free_cells[no_col_source]
    elif source == CARD_LOCATIONS.COLUMN.value:
        return board[no_col_source][-no_cards_move]
    else:
        raise Exception("Illegal source")

# Get the card to which source card should be moved (or freecell or heap or empty column)
def get_dest_card(board, vector_dest):
    conv_vector_dest = CARDS_DEST[''.join(map(str, vector_dest))]
    dest, no_col_dest = conv_vector_dest[0], int(conv_vector_dest[1]) - 1

    if dest == CARD_LOCATIONS.HEAP.value:
        return CARD_LOCATIONS.HEAP.value
    elif dest == CARD_LOCATIONS.FREE_CELL.value:
        return CARD_LOCATIONS.FREE_CELL.value
    elif dest == CARD_LOCATIONS.COLUMN.value:
        if len(board[no_col_dest]) == 0:
            return CARD_LOCATIONS.EMPTY_COLUMN.value
        else:
            return board[no_col_dest][-1]
    else:
        raise Exception("Illegal destination")
    
# Return the column where card is located and the number of cards before this card (including this card)
# Returns None if no card was found
def find_card_board(board, searched_card):
    for i, column in enumerate(board, start=1):
        for j, card in enumerate(reversed(column), start=1):
            if searched_card == card:
                return  j, i
            
    return None, None

# Return the column where card is located
# Returns None if no card was found
def find_card_fc(free_cells, searched_card):
    for i, card in enumerate(free_cells, start=1):
        if searched_card == card:
            return i
            
    return None
    
# Get the location of the source card and the number of cards moved as a vector
def get_source_card_vector(board, free_cells, src_card):
    # Iterate through board
    no_cards_moved, card_location = find_card_board(board, src_card)
    if card_location is not None:
        return REV_NUMBER_OF_CARDS[no_cards_moved], REV_CARDS_SOURCE[CARD_LOCATIONS.COLUMN.value + str(card_location)]
    
    # Iterate through free_cells (if card is not on board it will be in free_cells)
    card_location = find_card_fc(free_cells, src_card)
    return REV_NUMBER_OF_CARDS[1], REV_CARDS_SOURCE[CARD_LOCATIONS.FREE_CELL.value + str(card_location)]

# Get the location of the destination card
def get_dest_card_vector(board, dest_card):
    if dest_card == CARD_LOCATIONS.FREE_CELL.value:
        return REV_CARDS_DEST[CARD_LOCATIONS.FREE_CELL.value + "0"]
    
    elif dest_card == CARD_LOCATIONS.HEAP.value:
        return REV_CARDS_DEST[CARD_LOCATIONS.HEAP.value + "0"]
    
    # There may be more than one free column. We choose the first one that is free
    elif dest_card == CARD_LOCATIONS.EMPTY_COLUMN.value:
        for i, column in enumerate(board, start=1):
            if column == []:
                return REV_CARDS_DEST[CARD_LOCATIONS.COLUMN.value + str(i)]
            
    else:
        _, card_location = find_card_board(board, dest_card)
        return REV_CARDS_DEST[CARD_LOCATIONS.COLUMN.value + str(card_location)]
