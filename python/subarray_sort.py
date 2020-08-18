
# O(nlog(n)) Time | O(n) Space
def subarraySort(array):
    sortedArray = sorted(array)
    left = 0
    while left < len(array) and array[left] == sortedArray[left]:
        left += 1

    right = len(array) - 1

    while right >= 0 and array[right] == sortedArray[right]:
        right -= 1
        
    return [left, right] if left < right else [-1, -1]