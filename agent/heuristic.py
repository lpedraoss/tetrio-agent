import numpy as np

class Heuristic:
    def __init__(self):
        self.board = None
        self.height = 0
        self.holes = 0
        self.score = 0
        self.max_height_value = 0
        
    def complete_lines(self):
        count = 0
        for row in self.board:
            if all(cell == 1 for cell in row):
                count += 1
        return count

    def max_height(self):
        height = 0

        for i, row in enumerate(self.board):
            if np.any(row == 1):
                height = len(self.board) - i
                break
        
        self.height = height
        return height

    def count_holes(self):
        total_holes = 0
        for col in zip(*self.board):
            block_found = False
            for block in col:
                if block == 1:
                    block_found = True
                elif block_found:
                    total_holes += 1
        self.holes = total_holes
        return total_holes
    
    def holes_in_range(self, initial, final):
        total_holes = 0
        rows = len(self.board)
        cols = len(self.board[0])  # Supongo que todas las filas tienen la misma longitud
        
        for col_index in range(initial, final + 1):
            block_found = False
            for row_index in range(rows):
                # Verificar si el índice de fila y columna está dentro del rango válido
                if 0 <= row_index < rows and 0 <= col_index < cols:
                    if self.board[row_index][col_index] == 1:
                        block_found = True
                    elif block_found and self.board[row_index][col_index] == 0:
                        total_holes += 1
                    elif self.board[row_index][col_index] == 1:
                        break
        return total_holes

    def max_height_piece(self, initial, final):
        height = 0

        for i in range(len(self.board)):
            if np.any(self.board[i, initial:final+1] == 1):
                height = len(self.board) - i 
                break
        return height
        
    def calculate_heuristics(self, board, initial, final):
        self.board = np.copy(board)
        self.max_height_value = self.max_height()
        height_piece = self.max_height_piece(initial= initial, final= final)
        holes_piece = self.holes_in_range(initial= initial, final= final)
        self.count_holes()
    
        lines = self.complete_lines()
        score =  (holes_piece * .35 +  (height_piece) * .75)
        
        return {
            'holes': holes_piece,
            'height': height_piece,
            'lines': lines,
            'score': score
        }