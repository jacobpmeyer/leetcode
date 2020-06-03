# O(nlogn + mlogm) Time | O(1) Space

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
	arrayTwo.sort()
	left = 0
	right = 0
	leastDif = float("inf")
	leastTuple = []
	while left < len(arrayOne) and right < len(arrayTwo):
		possibleDif = abs(arrayOne[left] - arrayTwo[right])
		if possibleDif < leastDif:
			leastDif = possibleDif
			leastTuple = [arrayOne[left], arrayTwo[right]]
		if arrayOne[left] < arrayTwo[right]:
			left += 1
		elif arrayOne[left] > arrayTwo[right]:
			right += 1
		else:
			return [arrayOne[left], arrayTwo[right]]
	return leastTuple