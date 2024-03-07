from pieces import pieces
from rotation import checkRotation
#from board import board
import time
import numpy as np
from heuristic import calculate_heuristics

class Tetrio:

    def __init__(self):
        self.board = np.zeros((20, 10), dtype=int)
        #self.board = board
        self.checkRotation = checkRotation
        self.piece = None
        self.height = None
        self.width = None
        self.rotations = None

    def pressAdd(self, piece):
        
        self.rotations = len(pieces[piece]) 
        rotate = self.rotations-1
        self.piece = pieces[piece][rotate]
        self.height = len(self.piece)
        self.width = len(self.piece[0]) 
        columnInitial = self.checkRotation(piece=piece,rotate=rotate)
        column = self.moveInBoard(times=2, initial=columnInitial,direction='left')

        row = self.detectCollision(initial=column)
        print("se decide entonces apilarla en la fila: {}".format(row))
        print(
            "con el siguiente rango en columna: ({},{})".format(
                column, column + self.width - 1
            )
        )
        self.addPiece(row=row, column=column)
        self.checkLines()
        heuristic = calculate_heuristics(self.board)

        print(len(self.board), heuristic)
                
    def moveInBoard(self, times=0,initial=2,direction = None):
        index = 0
        if direction == None or direction == 'center':
            index = initial
        elif direction == 'left':
            index = max(
            0,
            initial - times,
            )
            print("esto es de left: ", index)
        elif direction == 'right':
            # Asegurarse de que start esté en el rango [0, 9]
            start = max(0, min(initial, 9))
            # Asegurarse de que end esté en el rango [0, 9]
            end = max(
                0,
                min(initial + self.width-1, 9),
            )
            # Calcular el nuevo valor teniendo en cuenta times
            index = max(0, min(start + times, 9))
            final = max(0, min(end + times, 9))

            if final >= 9 and len(range(index, final)) != len(
                range(initial, initial + self.width-1)
            ):
                final = 9
                index -= len(range(initial, self.width-1 ))

            print("esto es de right: ", index)
        return index


    def detectCollision(self, row=-1, initial=3, column=0):

        if column <= (self.width - 1) and row > (-len(self.board)+1):
            print("detect range: ", self.board[row][initial : initial + self.width-1])
            index = row -1
            collision = any(self.board[i][initial+column] == 1 for i in range(index, -len(self.board)-1, -1))
            isPiece = self.piece[self.height-1][column] == 0 and self.board[row][column+initial] == 1
            isBoard = self.piece[self.height-1][column]==1 and self.board[row][column+initial]==0
            both = self.piece[self.height-1][column] == 0 and self.board[row][column+initial]==0
            isHole = isPiece or isBoard or both
            
            if not collision:
                if isHole:
                    row = self.detectCollision(row=row, initial=initial, column=column + 1)
                else:
                    row = self.detectCollision(row=row - 1, initial=initial, column=0)
            else:
                row = self.detectCollision(row=row - 1, initial=initial, column=0)
        return row

    def addPiece(self, row=2, column=5):
        print("altura de pieza: ", self.height)
        print("ancho de pieza", self.width)
        for i in range(self.height):
            for j in range(self.width):
                if self.piece[i][j] == 1:
                    self.board[row + i - self.height + 1][column + j] = 1


    def checkLines(self):
        # Revisa si alguna fila está completamente llena de 1 y haz "pop"
        full_rows = [idx for idx, row in enumerate(self.board) if all(cell == 1 for cell in row)]
        for full_row in full_rows:
            self.cleanLine(full_row)

    def cleanLine(self, row):
        self.board = np.delete(self.board, row, axis=0)
        new_row = np.zeros((1, self.board.shape[1]), dtype=int)
        self.board = np.insert(self.board, 0, new_row, axis=0)
        
    def showBoard(self):
        for i in self.board:
            print(i)


tetrio = Tetrio()


def startGame():
    for p in range(1):
        tetrio.pressAdd(piece="t")


startGame()
tetrio.showBoard()
