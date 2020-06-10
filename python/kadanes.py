def kadanesAlgorithm(array):
	largest, largestCurrent = array[0], array[0]
	for num in array[1:]:
		largestCurrent = max(num, largestCurrent + num)
		largest = max(largest, largestCurrent)
	return largest