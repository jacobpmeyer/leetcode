"""
matrix may not be a perfect square
rivers are ones that are vertically and horizontally adjacent, not diagonally.
the size of the river is the number of 1s adjacent 
"""

def riverSizes(matrix):
    rivers = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                rivers.append(findRiverSize(matrix, i, j))
    return rivers

def findRiverSize(matrix, i, j):
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    queue = [[i, j]]
    size = 0
    matrix[i][j] = -1
    while len(queue):
        curr = queue.pop()
        size += 1
        for direction in dirs:
            r, c = curr[0] + direction[0], curr[1] + direction[1]
            if r >= 0 and r < len(matrix) and c >= 0 and c < len(matrix[0]) \
                    and matrix[r][c] == 1:
                queue.append([r, c])
                matrix[r][c] = -1   
    return size