
# O(n) Time where n is the length of the input array
# O(1) Space because we are creating a fixed number of variables
def kadanesAlgorithm(array):
	largest, largestCurrent = array[0], array[0]
	for num in array[1:]:
		largestCurrent = max(num, largestCurrent + num)
		largest = max(largest, largestCurrent)
	return largest