# Selection sort moves through an array several times, each time picking the
# smallest of the array, sorting from left to right in this case

# O(n^2) Time where n is the length of our input array
# O(1) Space or O(n) Space depending on if you are modifying the input array
def selectionSort(array):
	for i in range(len(array) - 1):
		s = i
		smallest = array[i]
		for j in range(i + 1, len(array)):
			if array[j] < smallest:
				s = j
				smallest = array[j]
		array[s], array[i] = array[i], array[s]
	return array