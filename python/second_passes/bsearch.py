def binarySearch(array, target):
    startIdx = 0
    endIdx = len(array) - 1
    while startIdx <= endIdx:
        mid = (startIdx + endIdx) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            endIdx = mid - 1
        else:
            startIdx = mid + 1
    return -1