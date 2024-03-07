def checkRotation(piece,rotate=0):
    index = 3
    if piece == "l":
        if rotate == 0 or rotate == 2 or rotate ==3:
            index = 3
        elif rotate == 1:
            index = 4
    elif piece == 'j':
        if rotate == 0 or rotate == 2 or rotate == 3:
            index = 3
        elif rotate == 1:
            index = 4
    elif piece == 'z':
        if rotate == 0:
            index = 3
        elif rotate == 1:
            index = 4
    elif piece == 's':
        if rotate == 0:
            index = 3
        elif rotate == 1:
            index = 4
    elif piece == 't':
        if rotate == 0 or rotate == 2 or rotate == 3:
            index = 3
        elif rotate == 1:
            index = 4
    elif piece == 'o':
        index = 4
    elif piece == 'i':
        if rotate == 0:
            index = 3
        elif rotate == 1:
            index = 5
    return index