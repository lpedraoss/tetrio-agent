import numpy as np
import random
from core.tetris.pieces import pieces
from core.tetris.rotation import checkRotation

class BaseBoard:
    def __init__(self):
        self.board = np.zeros((30, 10), dtype=np.uint8)
        self.current_height = 4
        self.MAX_HEIGHT = 30

    def moveInBoard(self, times=0, initial=2, direction=None, piece=None):
        width = len(piece[0]) if piece is not None else 0
        if direction == 'center':
            return initial
        elif direction == 'left':
            return max(0, initial - times)
        elif direction == 'right':
            return min(initial + times, 9 - (width - 1))
        return initial

    def detectCollision(self, row, col, piece):
        """Detect if a piece collides with the board"""
        piece_height, piece_width = piece.shape
        for i in range(piece_height):
            for j in range(piece_width):
                if row + i >= self.board.shape[0] or col + j >= self.board.shape[1]:
                    return True
                if piece[i, j] and self.board[row + i, col + j]:
                    return True
        return False

    def addPiece(self, row, col, piece):
        piece_height, piece_width = piece.shape
        for i in range(piece_height):
            for j in range(piece_width):
                if piece[i, j]:
                    self.board[row + i, col + j] = 1

    def checkLines(self):
        full_rows = [i for i in range(self.board.shape[0]) if all(self.board[i])]
        for row in full_rows:
            self.board = np.delete(self.board, row, axis=0)
            self.board = np.insert(self.board, 0, np.zeros((1, self.board.shape[1]), dtype=np.uint8), axis=0)

    def increase_height(self, row):
        if (row - self.current_height) < -self.current_height:
            increaseToAdd = min(4, self.MAX_HEIGHT - 1 - self.current_height)
            self.board = np.vstack((np.zeros((increaseToAdd, self.board.shape[1]), dtype=np.uint8), self.board))
            self.current_height += increaseToAdd

    def generateMoves(self, piece):
        moves = []
        piece_rotations = pieces[piece]
        for rot, piece_matrix in enumerate(piece_rotations):
            width = piece_matrix.shape[1]
            initial_col = 3  # Columna inicial base
            for direction in ['left', 'center', 'right']:
                if direction == 'center':
                    moves.append((piece, rot, direction, 0, self.moveInBoard(0, initial_col, direction, piece_matrix)))
                elif direction == 'right':
                    for t in range(1, 10 - width):
                        moves.append((piece, rot, direction, t, self.moveInBoard(t, initial_col, direction, piece_matrix)))
                elif direction == 'left':
                    for t in range(1, 10 - width):
                        moves.append((piece, rot, direction, t, self.moveInBoard(t, initial_col, direction, piece_matrix)))
        return moves

    def pressAdd(self, piece, times, rotation, direction):
        piece_matrix = pieces[piece][rotation]
        initial_col = checkRotation(piece=piece, rotate=rotation)  # Columna inicial base
        col = self.moveInBoard(times, initial_col, direction, piece_matrix)
        row = 0
        while row + piece_matrix.shape[0] <= self.board.shape[0] and not self.detectCollision(row, col, piece_matrix):
            row += 1
        row -= 1
        self.increase_height(row)
        self.addPiece(row, col, piece_matrix)
        self.checkLines()

    def showBoard(self):
        print('--------------------BOARD----------------------')
        for row in self.board:
            print(''.join(['#' if cell else '.' for cell in row]))

    def copy(self):
        new_board = BaseBoard()
        new_board.board = np.copy(self.board)
        new_board.current_height = self.current_height
        new_board.MAX_HEIGHT = self.MAX_HEIGHT
        return new_board

