# O(nlogn + mlogm) Time | O(1) Space

def smallestDifference(arrayOne, arrayTwo):
	arrayOne.sort()
	arrayTwo.sort()
	i = 0
	j = 0
	current = float("inf")
	smallest = float("inf")
	difArr = []
	while i < len(arrayOne) and j < len(arrayTwo):
		numOne = arrayOne[i]
		numTwo = arrayTwo[j]
		if numOne < numTwo:
			current = numTwo - numOne
			i += 1
		elif numOne > numTwo:
			current = numOne - numTwo
			j += 1
		else:
			return [numOne, numTwo]
		if current < smallest:
			smallest = current
			difArr = [numOne, numTwo]
	return difArr