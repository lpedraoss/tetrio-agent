from pieces import pieces
from board import board
import time
class Tetrio:

    def __init__(self):
        self.board = board
        self.pieces = pieces

    def pressAdd(self,piece, rote=0):
        pieceToAdd = self.pieces[piece][rote]
        rowPiece = len(pieceToAdd)

        columnPiece = len(pieceToAdd[0])
        columnInitial = (len(self.board[0]) - columnPiece) //2
        columnFinal = columnInitial + columnPiece
        columnFinal-=1
        print ('piece initial: ', columnInitial)
        print ('piece final: ', columnFinal)
        print('len piece: ',columnPiece)
        index = self.moveInBoard(funInit = self.moveToLeft(times = 2,initial = columnInitial),
                                funFin = self.moveToRight(times=2,init=columnInitial,fin=columnFinal),
                                lenght= columnPiece)

        row = self.detectedCollition(initial=index, final=columnPiece)
        row += 20
        print("se decide entonces apilarla en la fila: {}"
            .format(row))
        print("con el siguiente rango en columna: ({},{})"
            .format(index,index+columnPiece-1))
        self.addPiece(piece=pieceToAdd,row=row,column=index)

    def moveInBoard(self,funInit=None, funFin=None,lenght=3):
        init = 0
        fin = 0

        if funInit is not None:
            init = funInit

        if funFin is not None:
            fin = funFin

        index = abs(init - fin)
        if(lenght >= 3):
            index-=1
        print('resultado bordL: {}'.format(init))
        print('resultado bordR: {}'.format(fin))

        print('resultado bordI: {}'.format(index))
        
        return index

    def moveToLeft(self,times = 1, initial = 2):
        initial = max(0, initial - times)
        print("esto es de left: ",initial)
        return initial

    def moveToRight(self,times=1, init = 2, fin = 5):
        indexInit = max(0, min(init, 9))
        indexFin = max(0, min(fin, 9))
        initial = max(0, min(indexInit + times, 9))
        final = max(0, min(indexFin + times, 9))
        
        if final == 9 and len(range(initial, final)) != len(range(init, fin)):
            initial = initial - len(range(init, fin))

        print("esto es de right: ",initial)
        return initial

    def detectedCollition(self, row=-1, initial = 3,final = 6):
        print('row: ',row)
        print('detect initial: ',initial)
        print('detect final: ',final+initial)
        print('detect range: ',self.board[row][initial:initial+final])
        
        if 1 in (self.board[row][initial:initial+final]):
            print("se detectó una colision en la fila: {}".format(row))
            return self.detectedCollition(row=row-1,initial = initial,final = final)
        else:
            return row

    def addPiece(self, piece,row = 2, column = 5):
        height = len(piece)
        width = len(piece[0])
        print('altura: ',height)
        print('ancho',width)
        for i in range(height):
            for j in range(width):
                if  piece[i][j] == 1:
                    self.board[row - i][+column + j] = 1
                   
    def showBoard(self):
        for i in self.board:
            print(i)


tetrio = Tetrio()
tetrio.pressAdd(piece='i',rote=0)
tetrio.pressAdd(piece='s',rote=0)  
tetrio.showBoard()

