

# O(n) Time where n is the length of array
# O(1) Space
def isValidSubsequence(array, sequence):
	seqIdx = 0
	for num in array:
		if num == sequence[seqIdx]:
			seqIdx += 1
		if seqIdx == len(sequence):
			return True
	return False