# O(n) Time | O(1) Space
def moveElementToEnd(array, toMove):
	end = len(array) - 1
	i = 0
	while i < end:
		if array[end] == toMove:
			end -= 1
			continue
		if array[i] == toMove:
			swap(i, end, array)
		i += 1
	return array

def swap(i, j, arr):
	arr[i], arr[j] = arr[j], arr[i]