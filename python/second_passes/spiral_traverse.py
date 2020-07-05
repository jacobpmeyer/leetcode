def spiralTraverse(array):
    output = [array[0]]
    size = len(array) * len(array[0])
    row = 0
    col = 1
    currentLen = len(array)
    currentMin = 0
    while len(output) < size:
        while col < currentLen:
            output.append(array[row][col])
            col += 1
        col -= 1
        while row < currentLen:
            output.append(array[row][col])
            row += 1
        row -= 1
        col -= 1
        while col >= currentMin:
            output.append(array[row][col])
            col -= 1
        col += 1
        while row >= currentMin:
            output.append(array[row][col])
            row -= 1
        currentMin += 1
        currentLen -= 1
        row = currentMin
        col = currentMin
    return output
