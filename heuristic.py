

import numpy as np

class Heuristic:
    def __ini__(self):
        self.board = None
        self.height = None
        self.holes = None
        self.score = None
    def complete_lines(self):
        count = 0
        for row in self.board:
            if all(cell == 1 for cell in row):
                count += 1
        return count

    def max_height(self, initial, final):
        height = 0

        for i in range(len(self.board)):
            if np.any(self.board[i, initial:final+1] == 1):
                height = len(self.board) - i 
                break
        return height

    def holes(self):
        total_holes = 0
        for col in zip(*self.board):
            block_found = False
            for block in col:
                if block == 1:
                    block_found = True
                elif block_found:
                    total_holes += 1
        return total_holes

    def calculate_heuristics(self,board,initial,final):
        self.board = board
        lines = self.complete_lines()
        max_height_value = self.max_height(initial,final)
        holes_value = self.holes()
        #max_height_normalized = (max_height_value - 1) / (20 - 1)  # Normalizar max_height
        #holes_normalized = (holes_value - 0) / (20 * len(board[0]) - np.sum(board))  # Normalizar holes
        #lines_normalized = (lines - 0) / (20 - 0)  # Normalizar lines
        score =  (max_height_value * 0.65) + (holes_value * 0.35)
        
        return {
            'height': max_height_value,
            'holes':holes_value,
            'lines':lines,
            'score': score
        }