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
        holes = 0
        for col in range(board.shape[1]):
            block_found = False
            for row in range(board.shape[0]):
                if board[row, col] == 1:
                    block_found = True
                elif block_found and board[row, col] == 0:
                    holes += 1
        return holes

    def calculate_height(self, board):
        for row in range(board.shape[0]):
            if np.any(board[row]):
                return board.shape[0] - row
        return 0

    def count_cleared_lines(self, board):
        return np.sum(np.all(board, axis=1))
