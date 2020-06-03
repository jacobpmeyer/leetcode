# Write a function that takes in an array of integers and returns a boolean
# representing whether the array is monotonic.
# An array is said to be monotonic if its elements, from left to right,
# are entirely non-increasing or non-decreasing.


def isMonotonic(array):
	decreasing = False
	increasing = False
	for i in range(1, len(array)):
		if array[i] > array[i - 1]:
			increasing = True
		elif array[i] < array[i - 1]:
			decreasing = True
	if decreasing and increasing:
		return False
	else:
		return True
	