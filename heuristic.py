

import numpy as np

class Heuristic:
    def __ini__(self):
        self.board = None
        self.height = None
        self.holes = None
        self.score = None
        self.max_height_value = None
        
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
    
    def holes_in_range(self, initial, final):
        total_holes = 0
        for col_index in range(initial, final + 1):
            block_found = False
            for row_index in range(len(self.board)):
                if self.board[row_index][col_index] == 1:
                    block_found = True
                elif block_found and self.board[row_index][col_index] == 0:
                    total_holes += 1
                elif self.board[row_index][col_index] == 1:
                    break
        return total_holes
    def min_height_piece(self, initial, final):
        min_height_value = float('inf')  # Inicializar con un valor muy grande
        
        # Iterar sobre las columnas en el rango especificado
        for col in range(initial, final+1):
            # Iterar sobre las filas en la columna actual
            for row in range(len(self.board)):
                if self.board[row, col] == 1:
                    height = len(self.board) - row
                    # Actualizar el valor mínimo de altura
                    min_height_value = min(min_height_value, height)
                    break  # Detener la búsqueda en esta columna después de encontrar el primer 1
        return min_height_value

    def max_height_piece(self, initial, final):
        height = 0

        for i in range(len(self.board)):
            if np.any(self.board[i, initial:final+1] == 1):
                height = len(self.board) - i 
                break
        return height
        
    def calculate_heuristics(self,board,initial,final):
        self.board = board
        lines = self.complete_lines()
        self.max_height_value = self.max_height()
        height_piece = self.max_height_piece(initial=initial,final=final)
        holes_piece = self.holes_in_range(initial=initial,final=final)
        holes_value = self.holes()
        min_height_value =  self.min_height_piece(initial, final) 
        height_difference = self.max_height_value-min_height_value
        lines = self.complete_lines()
        score =  (holes_piece*.65 +height_piece*.35)
        
        return {
            'holes':holes_piece,
            'height': height_piece,
            'min': min_height_value,
            'height diference':height_difference,

            'score': score
        }