from pieces import pieces
import time
import numpy as np


class Tetrio:

    def __init__(self):
        self.board = np.zeros((20, 10), dtype=int)
        self.pieces = pieces
        self.piece = None
        self.height = None
        self.width = None

    def pressAdd(self, piece, rote=0):
        self.piece = self.pieces[piece][rote]
        self.height = len(self.piece)
        self.width = len(self.piece[0])
        columnInitial = (len(self.board[0]) - self.width) // 2


        column = self.moveInBoard(
            funInit=self.moveToLeft(times=2, initial=columnInitial),
            funFin=self.moveToRight(times=2, initial=columnInitial),
        )

        row = self.detectCollision(initial=column)
        # row += 20
        print("se decide entonces apilarla en la fila: {}".format(row))
        print(
            "con el siguiente rango en columna: ({},{})".format(
                column, column + self.width - 1
            )
        )
        self.addPiece(row=row, column=column)

    def moveInBoard(self, funInit=None, funFin=None):
        init = 0
        fin = 0

        if funInit is not None:
            init = funInit

        if funFin is not None:
            fin = funFin

        index = abs(init - fin)
        if self.width  >= 3:
            index -= 1
        return index

    def moveToLeft(self, times=1, initial=2):
        initial = max(
            0,
            initial - times,
        )
        print("esto es de left: ", initial)
        return initial

    def moveToRight(self, times=1, initial=2):
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

        if final == 9 and len(range(index, final)) != len(
            range(initial, initial + self.width-1)
        ):
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

    def showBoard(self):
        for i in self.board:
            print(i)


tetrio = Tetrio()


def startGame():
    for p in range(2):
        tetrio.pressAdd(piece="l", rote=1)
        tetrio.pressAdd(piece="i")
        tetrio.pressAdd(piece="o", rote=0)
        tetrio.pressAdd(piece="z", rote=1)

startGame()
tetrio.showBoard()
