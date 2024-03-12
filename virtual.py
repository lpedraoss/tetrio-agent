from pieces import pieces
from rotation import checkRotation
#from board import board
import time
import numpy as np
from heuristic import Heuristic

class Tetrio:

    def __init__(self):
        self.board = np.zeros((5, 10), dtype=int)
        #self.board = board
        self.checkRotation = checkRotation
        self.piece = None
        self.height = None
        self.current_height = 4
        self.MAX_HEIGHT = 20
        self.width = None 
        self.rotations = None  
        self.heuristic = Heuristic()
    def selectBestMove(self, moves,board):
        # Evaluar cada movimiento usando la heurística y seleccionar el mejor
        best_move = None
        best_score = float('inf')

        for move in moves:
            piece, rot, direction, t, move_column = move
            initial = move_column
            final = move_column + len(pieces[piece][rot][0]) - 1
            score = self.heuristic.calculate_heuristics(board, initial, final)['score']

            if score <= best_score:
                best_score = score
                best_move = move

        return best_move
    def pressAdd(self, piece,times,rotation,dir):
        self.rotations = len(pieces[piece]) 
        #rotate = self.rotations-2
        rotate = rotation
        self.piece = pieces[piece][rotate]
        self.height = len(self.piece)
        self.width = len(self.piece[0]) 
        columnInitial = self.checkRotation(piece=piece,rotate=rotate)
        #altura heuristica:  {'height': 2, 'holes': 2, 'score': 0.03353920515574651}
        column = self.moveInBoard(times=times, initial=columnInitial,direction=dir)
        moves = self.generateMoves(initial=columnInitial,piece=piece)
        print('moves: ------- ',moves)
        best_move = self.selectBestMove(moves,board= self.board)  # Nueva función para seleccionar el mejor movimiento
        print(best_move, 'mejor jugada!!!!!!!!!!!')
        row = self.detectCollision(initial=column)
        self.increase_height(row)

        print("se decide entonces apilarla en la fila: {}".format(row))
        print(
            "con el siguiente rango en columna: ({},{})".format(
                column, column + self.width - 1
            )
        )
      
        self.addPiece(row=row, column=column)
        heuristic = self.heuristic.calculate_heuristics(board = self.board,initial=column,final=column+self.width-1)
        print("altura heuristica: ", heuristic)
        self.checkLines()
        

    def moveInBoard(self, times=0,initial=2,direction = None,piece = None):
        if piece == None:
            width = self.width 
        else:
            width = len(piece[0]) 
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
                min(initial + width-1, 9),
            )
            # Calcular el nuevo valor teniendo en cuenta times
            index = max(0, min(start + times, 9))
            final = max(0, min(end + times, 9))

            if final >= 9 and len(range(index, final)) != len(
                range(initial, initial + width-1)
            ):
                final = 9
                index -= len(range(initial, initial+ width-1 ))

            print("esto es de right: ", index)
        return index

    def generateMoves(self,piece,initial=3):
        moves = []
        pieceToAdd = pieces[piece]
        times = (len(self.board[0]))-(initial+self.width-2)
        for rot in range(self.rotations):
            for direction in ['left', 'center', 'right']:
                if direction == 'center':
                    t = 0
                    move = self.moveInBoard(times=t, direction=direction,initial=initial,piece=pieceToAdd[rot])
                    moves.append((piece, rot, direction, t, move))
                else:
                    for t in range(1,times-1):
                    
                        move = self.moveInBoard(times=t, direction=direction,initial=initial,piece=pieceToAdd[rot])
                        moves.append((piece, rot, direction, t, move))
        return moves

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

    def increase_height(self, row):
            if (row - self.height) < -self.current_height:
                increaseToAdd = min(4, self.MAX_HEIGHT-1 - self.current_height)
                increase = np.zeros((increaseToAdd,self.board.shape[1]),dtype = int)
                self.board = np.vstack((increase,self.board))
                self.current_height += increaseToAdd

    def showBoard(self):
        for i in self.board:
            print(i)


tetrio = Tetrio()


def startGame():
    
    for p in range(1):
        tetrio.pressAdd(piece="l",rotation=0,times=4,dir='right')
        #tetrio.pressAdd(piece="i",rotation=0,times=2,dir='right')
        #tetrio.pressAdd(piece="l",rotation=1,times=4,dir='left')
        #tetrio.pressAdd(piece="t",rotation=0,times=2,dir='left')
        #tetrio.pressAdd(piece="o",rotation=0,times=1,dir='right')
        #tetrio.pressAdd(piece="s",rotation=0,times=4,dir='right')


startGame()


tetrio.showBoard()
