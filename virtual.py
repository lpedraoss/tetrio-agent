from pieces import pieces
from board import board

def pressAdd(piece, rote=0):
    pieceToAdd = pieces[piece][rote]
    rowPiece = len(pieceToAdd)

    columnPiece = len(pieceToAdd[0])
    columnInitial = (len(board[0]) - columnPiece) //2
    columnFinal = columnInitial + columnPiece
    
    print ('piece initial: ', columnInitial)
    print ('piece final: ', columnFinal)
    print('len piece: ',columnPiece)
    index = moveInBoard(funInit=moveToLeft(times=4,initial=columnInitial),funFin=moveToRight(times=9,fin=columnFinal))
    row = detectedCollition(initial=index, final=columnPiece)
    print("se decide entonces apilarla en la fila: {}".format(row))

def moveInBoard(funInit=None, funFin=None):
    init = 0
    fin = 0

    if funInit is not None:
        init = funInit

    if funFin is not None:
        fin = funFin

    index = abs(init - fin)
    print('resultado bordL: {}'.format(init))
    print('resultado bordR: {}'.format(fin))
    print('resultado bordI: {}'.format(index))
    return index

def moveToLeft(times = 1, initial = 3):
    initial = max(0, initial - times)
    return initial

def moveToRight(times=1, init = 3, fin=6):
    indexInit = max(0, min(init, 9))
    indexFin = max(0, min(fin, 9))
    initial = max(0, min(indexInit + times, 9))
    final = max(0, min(indexFin + times, 9))
    
    if final == 9 and len(range(initial, final)) != len(range(init, fin)):
        initial = initial - len(range(init, fin))

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

pressAdd(piece='l',rote=1)


for fila in board:
    print(fila)

#initial = moveToLeft(times=4)
#print('resultado de izquierda: {}'.format(initial))
#initial = moveToRight(times = 9, init = initial,fin = 3)
#print("resultado de derecha: {}".format(initial))
#index = moveInBoard(funInit = moveToLeft(times=4), funFin = moveToRight(times=9))
#print("resultado board: {}".format(index))