from pieces import pieces
from board import board
import time
def pressAdd(piece, rote=0):
    pieceToAdd = pieces[piece][rote]
    rowPiece = len(pieceToAdd)

    columnPiece = len(pieceToAdd[0])
    columnInitial = (len(board[0]) - columnPiece) //2
    columnFinal = columnInitial + columnPiece
    columnFinal-=1
    print ('piece initial: ', columnInitial)
    print ('piece final: ', columnFinal)
    print('len piece: ',columnPiece)
    index = moveInBoard(funInit=moveToLeft(times=2,initial=columnInitial),funFin=moveToRight(times=2,init=columnInitial,fin=columnFinal), lenght= columnPiece)

    row = detectedCollition(initial=index, final=columnPiece)
    row += 20
    print("se decide entonces apilarla en la fila: {}".format(row))
    print("con el siguiente rango en columna: ({},{})".format(index,index+columnPiece-1))
    addPiece(piece=pieceToAdd,row=row,column=index)

def moveInBoard(funInit=None, funFin=None,lenght=3):
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

def moveToLeft(times = 1, initial = 2):
    initial = max(0, initial - times)
    print("esto es de left: ",initial)
    return initial

def moveToRight(times=1, init = 2, fin = 5):
    indexInit = max(0, min(init, 9))
    indexFin = max(0, min(fin, 9))
    initial = max(0, min(indexInit + times, 9))
    final = max(0, min(indexFin + times, 9))
    
    if final == 9 and len(range(initial, final)) != len(range(init, fin)):
        initial = initial - len(range(init, fin))

    print("esto es de right: ",initial)
    return initial

def detectedCollition(row=-1, initial = 3,final = 6):
    print('row: ',row)
    print('detect initial: ',initial)
    print('detect final: ',final+initial)
    print('detect range: ',board[row][initial:initial+final])
    
    if 1 in (board[row][initial:initial+final]):
        print("se detectó una colision en la fila: {}".format(row))
        return detectedCollition(row=row-1,initial = initial,final = final)
    else:
        return row

def addPiece(piece,row = 2, column = 5):
    height = len(piece)
    width = len(piece[0])
    print('altura: ',height)
    print('ancho',width)
    for i in range(height):
        for j in range(width):
            if  piece[i][j] == 1:
                board[row - i][+column + j] = 1
                

pressAdd(piece='i',rote=0)
pressAdd(piece='s',rote=0)   


for fila in board:
    print(fila)

#initial = moveToLeft(times=4)
#print('resultado de izquierda: {}'.format(initial))
#initial = moveToRight(timesdd(piece='l',rote=0) = 9, init = initial,fin = 3)
#print("resultado de derecha: {}".format(initial))
#index = moveInBoard(funInit = moveToLeft(times=4), funFin = moveToRight(times=9))
#print("resultado board: {}".format(index))