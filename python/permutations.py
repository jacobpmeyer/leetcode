# Upper Bound: O(n^2*n!) Time | O(n*n!) Space
# Roughly O(n*n!) Time | O(n*n!) Space
# def getPermutations(array):
# 	permutations = []
# 	permutationsHelper(array, [], permutations)
# 	return permutations

# def permutationsHelper(array, currentPermutation, permutations):
# 	if not len(array) and len(currentPermutation):
# 		premutations.append(currentPermutation)
# 	else:
# 		# Iterate over the input array
# 		for i in range(len(array)):
# 			# Create a new array at each index, slicing around i to exclude
# 			newArray = array[:i] + array[i + 1:]
# 			newPermutation = currentPermutation + [array[i]]
# 			permutationsHelper(newArray, newPermutation, permutations)

# O(n*n!) Time | O(n*n!) Space
def getPermutations(array):
	permutations = []
	permutationsHelper(0, array, permutations)
	return permutations

def permutationsHelper(i, array, permutations):
	if i == len(array) - 1:
		permutations.append(array[:])
	else:
		for j in range(i, len(array)):
			swap(i, j, array)
			permutationsHelper(i + 1, array, permutations)
			swap(i, j, array)

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]

arr = [1, 2, 3]
print(getPermutations(arr))