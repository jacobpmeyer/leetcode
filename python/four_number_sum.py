"""
in: array: List[int], targetSum: int
out: quads: List[List[int]]

example: array = [7, 6, 4, -1, 1, 2], targetSum = 16
output: quads = [[7, 6, 4, -1], [7, 6, 1, 2]]
"""


def fourNumberSum(array, targetSum):
    quads = []
    allPairSums = {}
    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            currentSum = array[i] + array[j]
            difference = targetSum - currentSum
            if difference in allPairSums:
                for pair in allPairSums[difference]:
                    quads.append(pair + [array[i], array[j]])

        for k in range(0, i):
            currentSum = array[k] + array[i]
            if currentSum not in allPairSums:
                allPairSums[currentSum] = [[array[k], array[i]]]
            else:
                allPairSums[currentSum].append([array[k], array[i]])
        
    return quads