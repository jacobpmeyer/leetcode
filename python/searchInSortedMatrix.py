def searchInSortedMatrix(matrix, target):
    row, col = 0, len(matrix)
    while row < len(matrix) and col >= 0:
        if matrix[row][col] < target:
            row += 1
        elif matrix[row][col] > target:
            col -= 1
        else:
            return [row, col]
    return [-1, -1]