from tetris.pieces import pieces
from tetris.rotation import checkRotation
import numpy as np
from agent.heuristic import Heuristic

class TestBoard:

    def __init__(self):
        self.board = np.zeros((40, 10), dtype=int)
        self.board_test=None
        self.isNone = None
        #self.board = board
        self.checkRotation = checkRotation
        self.piece = None
        self.height = None
        self.current_height = 4
        self.MAX_HEIGHT = 20
        self.width = None 
        self.rotations = None  
        self.heuristic = Heuristic()


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
        elif direction == 'right':
            # Calcular el nuevo valor teniendo en cuenta times
            index = min(initial + times, 9 - (width-1))
        return index
 
    def detectCollision(self, row=-1, initial=3, column=0,board=None,deeph=[]):
        if self.isNone:
            board = np.copy(self.board)
        
        deep=0
        if column <= (self.width - 1) and row > (-len(board)+1):
            index = row -1
    
            collision = any(board[i][initial+column] == 1 for i in range(index, -len(board)-1, -1))
            isPiece = self.piece[self.height-1][column] == 0 and board[row][column+initial] == 1
            isBoard = self.piece[self.height-1][column]==1 and board[row][column+initial]==0
            both = self.piece[self.height-1][column] == 0 and board[row][column+initial]==0
            
            isHole = isPiece or isBoard or both

            if not collision:
                for i in range(self.height):
                    down_peace = self.height-i-1
                    if self.piece[down_peace][column] == 0:
                        deep+=1
                    elif self.piece[down_peace][column] == 1:
                        break
                if deep >= 1:
                    deep-=1
                deeph.append(deep)
                if isHole:
                    row,deeph = self.detectCollision(row=row, initial=initial, column=column + 1,board=board,deeph=deeph)
                else:
                    row,deeph = self.detectCollision(row=row-1, initial=initial, column=column,board=board,deeph=deeph)
            else:
                row,deeph = self.detectCollision(row=row - 1, initial=initial, column=column,board=board,deeph=[])
        if max(deeph) ==0 and deeph != []:
            deeph = []
            deeph.append(0)
        return row,deeph

    def addPiece(self, row=2, column=5,board=None):
        
        if self.isNone:
            board = np.copy(self.board)
        for i in range(self.height):
            for j in range(self.width):
                if self.piece[i][j] == 1:
                    board[row + i - self.height + 1][column + j] = 1
        if self.isNone:
            self.board = np.copy(board)
        else:
            self.board_test = np.copy(board)

    def checkLines(self,board=None):
        if self.isNone:
            board = np.copy(self.board)
        # Revisa si alguna fila está completamente llena de 1 y haz "pop"
        full_rows = [idx for idx, row in enumerate(board) if all(cell == 1 for cell in row)]
        for full_row in full_rows:
            self.cleanLine(row = full_row,board = board)

    def cleanLine(self, row,board=None):
        if self.isNone:
            board = np.copy(self.board)

        board = np.delete(board, row, axis=0)
        new_row = np.zeros((1, board.shape[1]), dtype=int)
        board = np.insert(board, 0, new_row, axis=0)
        if self.isNone:
            self.board = np.copy(board)
        else:
            self.board_test =  np.copy(board)
            
    def increase_height(self, row,board=None):
            if board is None:
                board = np.copy(self.board)
            if (row - self.height) < -self.current_height:
                increaseToAdd = min(4, self.MAX_HEIGHT-1 - self.current_height)
                increase = np.zeros((increaseToAdd,board.shape[1]),dtype = int)
                board = np.vstack((increase, board))
                if self.isNone:
                    self.board = np.copy(board)
                else:
                    self.board_test = np.copy(board)
                self.current_height += increaseToAdd


    def pressAdd(self, piece,times,rotation,dir,board=None):
        self.isNone = board is None
        
        if self.isNone:
            board = np.copy(self.board)
        self.rotations = len(pieces[piece]) 
        #rotate = self.rotations-2
        rotate = rotation
        self.piece = pieces[piece][rotate]
        self.height = len(self.piece)
        self.width = len(self.piece[0]) 
        columnInitial = self.checkRotation(piece=piece,rotate=rotate)
        #altura heuristica:  {'height': 2, 'holes': 2, 'score': 0.03353920515574651}
        column = self.moveInBoard(times=times, initial=columnInitial,direction=dir)
        row,deeph = self.detectCollision(initial=column,board = board)
        if row >= -2:
            deeph = []
        if deeph == []:
            deeph.append(0)

        row+=max(deeph)
        self.increase_height(row=row,board = board)
    
        self.addPiece(row=row, column=column,board=board)
        self.checkLines(board=board)


