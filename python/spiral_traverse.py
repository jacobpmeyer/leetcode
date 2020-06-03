
# Iterative
# O(n) Time | O(n) Space

def spiralTraverse(array):
	spiralArray = []
	startCol, endCol = 0, len(array[0]) - 1
	startRow, endRow = 0, len(array) - 1
	while startRow <= endRow and startCol <= endCol:
		for col in range(startCol, endCol + 1):
			spiralArray.append(array[startRow][col])
		for row in range(startRow + 1, endRow + 1):
			spiralArray.append(array[row][endCol])
		for col in reversed(range(startCol, endCol)):
			if startRow == endRow:
				break
			spiralArray.append(array[endRow][col])
		for row in reversed(range(startRow + 1, endRow)):
			if startCol == endCol:
				break
			spiralArray.append(array[row][startCol])
		startRow += 1
		endRow -= 1
		startCol += 1
		endCol -= 1
	return spiralArray


# Rerursive
# O(n) Time | O(n) Space

def spiralTraverse(array):
	results = []
	spiralFill(array, 0, len(array) - 1, 0, len(array[0]) - 1, results)
	return results

def spiralFill(array, startRow, endRow, startCol, endCol, results):
	if startRow > endRow or startCol > endCol:
		return 
	for col in range(startCol, endCol + 1):
		results.append(array[startRow][col])
	for row in range(startRow + 1, endRow + 1):
		results.append(array[row][endCol])
	for col in reversed(range(startCol, endCol)):
		if startRow == endRow:
			break
		results.append(array[endRow][col])
	for row in reversed(range(startRow + 1, endRow)):
		if startCol == endCol:
			break
		results.append(array[row][startCol])
	spiralFill(array, startRow + 1, endRow - 1, startCol + 1, endCol - 1, results)