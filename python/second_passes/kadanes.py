def kadanesAlgorithm(array):
    totalMax = array[0]
    currentMax = array[0]
    for i in range(1, len(array)):
        num = array[i]
        currentMax = max(currentMax + num, num)
        totalMax = max(currentMax, totalMax)
    return totalMax