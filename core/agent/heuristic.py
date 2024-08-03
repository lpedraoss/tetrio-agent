import numpy as np

class Heuristic:
    def __init__(self):
        self.hole_penalty = 10
        self.height_penalty = 5
        self.line_bonus = 100

    def calculate_heuristics(self, board, initial, final):
        holes = self.count_holes(board)
        height = self.calculate_height(board)
        cleared_lines = self.count_cleared_lines(board)
        
        score = (holes * self.hole_penalty) + (height * self.height_penalty) - (cleared_lines * self.line_bonus)
        return {'score': score, 'holes': holes, 'height': height, 'cleared_lines': cleared_lines}

    def count_holes(self, board):
        # Count holes in each column
        holes = 0
        for col in range(board.shape[1]):
            column = board[:, col]
            first_block_idx = np.argmax(column)  # Index of the first non-zero block
            if column[first_block_idx] == 1:
                holes += np.sum(column[first_block_idx + 1:] == 0)
        return holes

    def calculate_height(self, board):
        # Find the first row from the top that has any blocks
        row_indices = np.where(board.any(axis=1))[0]
        if row_indices.size > 0:
            return board.shape[0] - row_indices[0]
        return 0

    def count_cleared_lines(self, board):
        # Count how many rows are completely filled with blocks
        return np.sum(np.all(board, axis=1))
