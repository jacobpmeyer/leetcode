# O(n) Time | O(1) Space where n is the length of the array
def isMonotonic(array):
    increasing = False
    decreasing = False
    for i in range(len(array) - 1):
        if array[i] < array[i + 1]:
            increasing = True
        elif array[i] > array[i + 1]:
            decreasing = True
    return increasing != decreasing or (not increasing and not decreasing)