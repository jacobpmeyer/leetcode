def findThreeLargestNumbers(array):
	largestArr = [None, None, None]
	for num in array:
		checkLargest(num, largestArr)
	return largestArr

def checkLargest(num, largestArr):
	if largestArr[2] is None or num > largestArr[2]:
		shiftLargest(2, num, largestArr)
	elif largestArr[1] is None or num > largestArr[1]:
		shiftLargest(1, num, largestArr)
	elif largestArr[0] is None or num > largestArr[0]:
		shiftLargest(0, num, largestArr)

def shiftLargest(idx, num, largestArr):
	for i in range(idx + 1):
		if i == idx:
			largestArr[i] = num
		else:
			largestArr[i] = largestArr[i + 1]
