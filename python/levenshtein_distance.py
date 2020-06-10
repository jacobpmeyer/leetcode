

# O(nm) Time | O(nm) Space where n is the length of str1 and m is the length
# of str2 in both time and space
def levenshteinDistance(str1, str2):
	edits = [[x for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
	for i in range(1, len(str2) + 1):
		edits[i][0] = edits[i - 1][0] + 1
	for r in range(1, len(str2) + 1):
		for c in range(1, len(str1) + 1):
			if str2[r - 1] == str1[c - 1]:
				edits[r][c] = edits[r - 1][c - 1]
			else:
				edits[r][c] = 1 + min(edits[r - 1][c - 1], edits[r][c - 1], edits[r - 1][c])
	return edits[-1][-1]

# O(nm) Time where n is the length of str1 and m is the length of str2
# O(min(n, m)) Space where the length of the array is equal to the shorter of 
# the two strings
def levenshteinDistance(str1, str2):
	small = str1 if len(str1) < len(str2) else str2
	big = str1 if len(str1) >= len(str2) else str2
	evenRow = [x for x in range(len(small) + 1)]
	oddRow = [None for x in range(len(small) + 1)]
	for i in range(1, len(big) + 1):
		if i % 2 == 0:
			currentRow = evenRow
			previousRow = oddRow
		else:
			currentRow = oddRow
			previousRow = evenRow
		currentRow[0] = i
		for j in range(1, len(small) + 1):
			if big[i - 1] == small[j - 1]:
				currentRow[j] = previousRow[j - 1]
			else:
				currentRow[j] = 1 + min(currentRow[j - 1], previousRow[j], previousRow[j - 1])
	return evenRow[-1] if len(big) % 2 == 0 else oddRow[-1]