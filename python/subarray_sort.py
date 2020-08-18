
# O(nlog(n)) Time | O(n) Space
# def subarraySort(array):
#     sortedArray = sorted(array)
#     left = 0
#     while left < len(array) and array[left] == sortedArray[left]:
#         left += 1

#     right = len(array) - 1

#     while right >= 0 and array[right] == sortedArray[right]:
#         right -= 1
        
#     return [left, right] if left < right else [-1, -1]


def subarraySort(array):
    minOutOfOrder = float("inf")
    maxOutOfOrder = float("-inf")
    for i in range(len(array)):
        num = array[i]
        if numOutOfOrder(i, num, array):
            minOutOfOrder = min(minOutOfOrder, num)
            maxOutOfOrder = max(maxOutOfOrder, num)
    if minOutOfOrder == float("inf"):
        return [-1, -1]
    subLeft = 0
    subRight = len(array) - 1
    while array[subLeft] <= minOutOfOrder:
        subLeft += 1
    while array[subRight] >= maxOutOfOrder:
        subRight -= 1
    return [subLeft, subRight]

def numOutOfOrder(i, num, array):
    if i == 0:
        return num > array[i + 1]
    if i == len(array) - 1:
        return num < array[i - 1]
    return num < array[i - 1] or num > array[i + 1]