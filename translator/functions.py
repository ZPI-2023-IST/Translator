from constants import NO_CARD, CARD_SUITS, REV_CARD_SUITS, CARD_VALUES, REV_CARD_VALUES

import numpy as np

# Convert given card to one hot encoded vector e.g. 7C = 01000000001000000
# Every digit is stored as a separate value in the array
def convert_card_to_one_hot_encoded_vector(card):
    suit = CARD_SUITS[card[-1]]
    value = CARD_VALUES[card[:-1]]
    vector = list(map(int, list(suit + value)))
    return vector

# Convert one hot encoded vector into card e.g. 01000000001000000 = 7C
# Every digit of one hot encoded is stored separately
def convert_one_hot_encoded_vector_to_card(vector):
    value = ''.join(map(str, vector))
    suit = REV_CARD_SUITS[value[:4]]
    value = REV_CARD_VALUES[value[4:]]
    return value + suit

def convert_board_to_array_of_one_hot_encoded_values(board):
    # Fill entire array with no card symbol
    array_one_hot_encoded = np.full((8, 19, 17), fill_value=list(map(int, list(NO_CARD))))
    # Fill array with actual cards
    for i, column in enumerate(board):
        for j, card in enumerate(column):
            array_one_hot_encoded[i][j] = convert_card_to_one_hot_encoded_vector(card)

    return array_one_hot_encoded

def convert_free_cell_to_array_of_one_hot_encoded_values(free_cell):
    array_one_hot_encoded = np.full((4, 17), fill_value=list(map(int, list(NO_CARD))))
    for i, card in enumerate(free_cell):
        array_one_hot_encoded[i] = convert_card_to_one_hot_encoded_vector(card)

    return array_one_hot_encoded

def convert_heap_to_array_of_one_hot_encoded_values(heap):
    array_one_hot_encoded = np.full((4, 17), fill_value=list(map(int, list(NO_CARD))))
    for i, card in enumerate(heap):
        array_one_hot_encoded[i] = convert_card_to_one_hot_encoded_vector(card)

    return array_one_hot_encoded

def convert_to_game_vector(board, free_cell, heap):
    board = convert_board_to_array_of_one_hot_encoded_values(board)
    free_cell = convert_free_cell_to_array_of_one_hot_encoded_values(free_cell)
    heap = convert_heap_to_array_of_one_hot_encoded_values(heap)

    return board, free_cell, heap
