

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

# Same time and space. Just a different implementation
def isValidSubsequence(array, sequence):
	arrIdx = 0
	seqIdx = 0
	while arrIdx < len(array) and seqIdx < len(sequence):
		if array[arrIdx] == sequence[seqIdx]:
			seqIdx += 1
		arrIdx += 1
	return seqIdx == len(sequence)