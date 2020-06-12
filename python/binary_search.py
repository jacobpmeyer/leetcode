
# O(log(n)) Time where n is the length of the array
# O(log(n)) Space where n is the length of the array, because we add, at worst,
# log(n) stack frames to the call stack
def binarySearch(array, target):
	if len(array) < 1:
		return -1
	mid = len(array) // 2
	pivot = array[mid]
	if target < pivot:
		return binarySearch(array[:mid], target)
	elif target > pivot:
		res = binarySearch(array[mid + 1:], target)
		return res + 1 + mid if res != -1 else -1
	else:
		return mid
