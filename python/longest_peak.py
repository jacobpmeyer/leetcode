
# O(n) Time | O(n) Space
def longestPeak(array):
	longest = 0
	i = 1
	while i < len(array) - 1:
		isPeak = array[i] > array[i - 1] and array[i] > array[i + 1]
		if not isPeak:
			i += 1
			continue
		leftIdx = i - 2
		while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
			leftIdx -= 1
		rightIdx = i + 2
		while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
			rightIdx += 1
		current = rightIdx - leftIdx - 1
		longest = max(longest, current)
		i = rightIdx
	return longest