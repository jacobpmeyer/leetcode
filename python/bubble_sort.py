def bubbleSort(array):
	sorted = False
	while not sorted:
		sorted = True
		for i in range(1, len(array)):
			if array[i] < array[i - 1]:
				array[i], array[i - 1] = array[i - 1], array[i]
				sorted = False
	return array