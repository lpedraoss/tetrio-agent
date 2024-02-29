from pieces import pieces
from board import board

def pressAdd(piece, rote=0, column='center'):
    pieceToAdd = pieces[piece][rote]
    rowPiece = len(pieceToAdd)
    columnPiece = len(pieceToAdd[0])
    # Determinar la columna inicial según la indicación
    #if column == 'left':
    #   column_initial = 0
    #elif column == 'right':
    #    column_initial = len(boardMaster[0]) - columnPiece
    #else:  # Por defecto, centrar la pieza
    #    column_initial = (len(boardMaster[0]) - columnPiece) // 2
    columnInitial = len(board[0])- columnPiece
    #index = moveInBoard(funInit=moveToLeft(initial=columnInitial))
    #print(index)
    detectedCollition(initial=columnInitial, final=columnPiece)
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
    print('initial: ',initial)
    print('final: ',final)
    print('range: ',board[row][initial:final+3])
    if 1 in (board[row][initial:final+3]):
        print("se detectó una colision en la fila: {}".format(row))
        detectedCollition(row=row-1,initial=initial,final=final)
        return True
    else:
        return False
pressAdd(piece='l')


for fila in board:
    print(fila)

initial = moveToLeft(times=4)
print('resultado de izquierda: {}'.format(initial))
initial = moveToRight(times = 9, init = initial,fin = 3)
print("resultado de derecha: {}".format(initial))
index = moveInBoard(funInit = moveToLeft(times=4), funFin = moveToRight(times=9))
print("resultado board: {}".format(index))