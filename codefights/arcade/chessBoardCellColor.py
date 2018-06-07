def chessBoardCellColor(cell1, cell2):
    cell1color = determineColor(cell1)
    cell2color = determineColor(cell2)

    return cell1color == cell2color

def determineColor(cell):
    # if the sum of their numeric representations is even - dark
    # if sum is odd - light

    first = ord(cell[0]) - 65
    second = eval(cell[1])

    return 'dark' if (first + second) % 2 == 0 else 'light'