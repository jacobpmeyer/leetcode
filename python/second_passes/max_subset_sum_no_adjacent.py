def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    result = [None for el in array]
    result[0] = array[0]
    result[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        result[i] = max((result[i - 2] + array[i]), result[i - 1])
    return result[-1]

array = [75, 105, 120, 75, 90, 135]
print(maxSubsetSumNoAdjacent(array))