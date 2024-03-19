import numpy as np


def calculate_drop_units( grid, piece, i):
    drop_units = []
    for col in range(piece.shape[1]):
        if np.all(piece[:, col] == 0):
            drop_units.append(piece.shape[0])
        else:
            grid_row = np.argmax(grid[i:, col] == 1)
            piece_row = np.argmax(piece[::-1, col] == 1)
            drop_units.append(grid_row - piece_row)
    return drop_units