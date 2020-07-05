def threeNumberSum(array, targetSum):
    sortedArray = sorted(array)
    threeSumsArray = []
    for i in range(len(sortedArray)):
        left = i + 1
        right = len(sortedArray) - 1
        while left < right:
            currentSum = sortedArray[i] + sortedArray[left] + sortedArray[right]
            if currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
            else:
                threeSumsArray.append(
                    [sortedArray[i], sortedArray[left], sortedArray[right]]
                )
                left += 1
                right -= 1
    return threeSumsArray

array = [12, 3, 1, 2, -6, 5, -8, 6]
print(threeNumberSum(array, 0))