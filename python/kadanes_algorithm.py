def kadanesAlgorithm(array):
    maxSoFar = array[0]
    maxEndingHere = array[0]
    for i in range(1, len(array)):
        maxEndingHere = max(maxEndingHere + array[i], array[i])
        maxSoFar = max(maxSoFar, maxEndingHere)
    return maxSoFar