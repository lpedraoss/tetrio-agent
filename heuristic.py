

import numpy as np

def max_height(board, initial, final):
    height = 0

    for i in range(len(board)):
        if np.any(board[i, initial:final+1] == 1):
            height = len(board) - i 
            break
    return height

def holes(board):
    total_holes = 0
    for col in zip(*board):
        block_found = False
        for block in col:
            if block == 1:
                block_found = True
            elif block_found:
                total_holes += 1
    return total_holes

def calculate_heuristics(board,initial,final):
    max_height_value = max_height(board,initial,final)
    holes_value = holes(board)


    return {
        'max_height': max_height_value,
        'holes': holes_value,

    }