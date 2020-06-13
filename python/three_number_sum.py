

# O(n^2) Time where n is the length of the input array
# O(n) Space because the number of possible triplets is based on the size of the
# array

def threeNumberSum(array, targetSum):
	array.sort()
	sumsArr = []
	for i in range(len(array) - 2):
		j = i + 1
		x = len(array) - 1
		while j < x:
			current = array[i] + array[j] + array[x]
			if current == targetSum:
				sumsArr.append([array[i], array[j], array[x]])
				j += 1
				x -= 1
			elif current < targetSum:
				j += 1
			elif current > targetSum:
				x -= 1
	return sumsArr