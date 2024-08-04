import numpy as np

class Heuristic:
    def __init__(self):
        self.hole_penalty = 10
        self.height_penalty = 5
        self.line_bonus = 100
        self.height_threshold = 15
        self.extra_height_penalty = 50  # Penalización adicional si la altura es mayor a 15
        self.current_score = 0  # Puntaje actual
        self.height_priority_threshold = 12  # Umbral de altura para priorizar el completado de líneas

    def calculate_heuristics(self, board, initial, final):
        holes = self.count_holes(board)
        height, extra_penalty = self.calculate_height(board)
        cleared_lines = self.count_cleared_lines(board)
        
        # Ajustar penalizaciones y bonificaciones si el puntaje está cerca de 35
        if self.current_score >= 35:
            self.hole_penalty = 5
            self.height_penalty = 2
            self.line_bonus = 200
        
        # Priorizar el completado de líneas si la altura máxima de las piezas supera el umbral
        if height >= self.height_priority_threshold:
            self.line_bonus = 300
        
        score = (holes * self.hole_penalty) + (height * self.height_penalty) + extra_penalty - (cleared_lines * self.line_bonus)
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
        # Find the maximum height of the pieces in the board
        row_indices = np.where(board.any(axis=1))[0]
        if row_indices.size > 0:
            height = board.shape[0] - row_indices[0]
            extra_penalty = 0
            if height > self.height_threshold:
                extra_penalty = (height - self.height_threshold) * self.extra_height_penalty
            return height, extra_penalty
        return 0, 0

    def count_cleared_lines(self, board):
        # Count how many rows are completely filled with blocks
        return np.sum(np.all(board, axis=1))