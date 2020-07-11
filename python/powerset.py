
# Recursive approach
# O(n*n^2) Time | O(n*n^2) Space
# def powerset(array, idx = None):
# 	if idx is None:
# 		idx = len(array) - 1
# 	if idx < 0:
# 		return [[]]
# 	ele = array[idx]
# 	subsets = powerset(array, idx - 1)
# 	for i in range(len(subsets)):
# 		currentSubset = subsets[i]
# 		subsets.append(currentSubset + [ele])
# 	return subsets

# Iterative approach
# O(n*n^2) Time | O(n*n^2) Space
def powerset(array):
	subsets = [[]]
	for ele in array:
		for i in range(len(subsets)):
			currentSubset = subsets[i]
			subsets.append(currentSubset + [ele])
	return subsets



array = [1, 2, 3]
# => [1, 2, 3] => el = 3
# => [1, 2] => el = 2
# => [1] => el = 1
# => [] => return up []
# => subsets = [] => currentSub = subsets[0] => subsets.append(current + [el])
# => subsets = [[],[1]] el = 2 => subsets.append([] + [2] ) 
print(powerset(array))
