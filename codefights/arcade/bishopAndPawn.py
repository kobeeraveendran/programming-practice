def bishopAndPawn(bishop, pawn):
    bishopX = ord(bishop[0]) - 96
    bishopY = eval(bishop[1])
    pawnX = ord(pawn[0]) - 96
    pawnY = eval(pawn[1])

    return abs(pawnX - bishopX) ==  abs(pawnY - bishopY)