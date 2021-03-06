# Write a function that takes in an array of integers and returns a boolean
# representing whether the array is monotonic.
# An array is said to be monotonic if its elements, from left to right,
# are entirely non-increasing or non-decreasing.


# O(n) Time where n is the length of the input array
# O(1) Space as we are not creating any new variables that depend on the input

def isMonotonic(array):
	increasing = False
	decreasing = False
	for i in range(1, len(array)):
		if array[i] > array[i - 1]:
			increasing = True
		elif array[i] < array[i - 1]:
			decreasing = True
	if increasing and decreasing:
		return False
	else:
		return True
