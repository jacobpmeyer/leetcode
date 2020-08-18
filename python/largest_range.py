def largestRange(array):
	hash = {}
	bestRange = []
	longestRange = 0
	for num in array:
		hash[num] = True
	for num in array:
		if not hash[num]:
			continue
		currentRange = 1
		left = num - 1
		right = num + 1
		while left in hash:
			hash[left] = False
			left -= 1
			currentRange += 1			
		while right in hash:
			hash[right] = False
			right += 1
			currentRange += 1
		if currentRange > longestRange:
			longestRange = currentRange
			bestRange = [left + 1, right - 1]
	return bestRange