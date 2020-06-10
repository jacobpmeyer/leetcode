
# O(n) Time where n is the length of the array
# O(1) Space because of constant operations
def hasSingleCycle(array):
	numOfJumps = 0
	index = 0
	while numOfJumps < len(array):
		if numOfJumps > 0 and index == 0:
			return False
		numOfJumps += 1
		index = getIndex(index, array)
	return index == 0

def getIndex(index, array):
	nextIdx = array[index]
	nextIdx = (index + nextIdx) % len(array)
	return nextIdx