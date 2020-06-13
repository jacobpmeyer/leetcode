
# O(n^2) Time where n is the length of the array, because of the double for loop
# O(1) Space
def insertionSort(array):
	for i in range(1, len(array)):
		j = i
		while j > 0 and array[j] < array[j - 1]:
			array[j - 1], array[j] = array[j], array[j - 1]
			j -= 1
	return array