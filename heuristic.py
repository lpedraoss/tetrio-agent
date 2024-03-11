

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
    max_height_value = max_height(board,initial,final)*0.7
    holes_value = holes(board)*0.3
    max_height_normalized = (max_height_value - 1) / (20 - 1)  # Normalizar max_height
    holes_normalized = (holes_value - 0) / (20 * len(board[0]) - np.sum(board))  # Normalizar holes
    score = (max_height_normalized * 0.7) + (holes_normalized * 0.3)
    
    return {
        'height': max_height_value,
        'holes':holes_value,
        'score': score
    }