def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    if len(array) < 2:
        return array[0]
    maxSum = [None for el in range(len(array))]
    maxSum[0] = array[0]
    maxSum[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        maxSum[i] = max(array[i] + maxSum[i - 2], maxSum[i - 1])
    return maxSum[-1]
