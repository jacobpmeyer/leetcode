def tpos(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            array[i][j], array[j][i] = array[j][i], array[i][j]
    # for i in range(len(array)):
    #     array[i].reverse()
    return array

array = [
    [1, 2],
    [3, 4]
]

print(tpos(array))

