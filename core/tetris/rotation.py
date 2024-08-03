def checkRotation(piece, rotate=0):
    if piece in ['l', 'j', 't']:
        return 4 if rotate == 1 else 3
    elif piece in ['z', 's']:
        return 4 if rotate == 1 else 3
    elif piece == 'o':
        return 4
    elif piece == 'i':
        return 5 if rotate == 1 else 3
    return 3