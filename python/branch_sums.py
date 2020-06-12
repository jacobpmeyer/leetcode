
# branch sums takes in a tree and calculates the sum from the root to each
# leaf node, from left to right, for the entire tree and returns those values 
# as an array, in the same order


class BinaryTree:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


# O(n) Time where n is the size of the tree because we traverse each node in 
# the tree
# O(n) Space => The recursive calls are O(log(n)) and the output array is going
# to be n / 2, which gives us O(n), so the final space complexity is O(n) as
# O(n) dwarfs the O(log(n)) space being used by the recursive calls
def branchSums(root):
	sumsArr = []
	branchSumsHelper(root, sumsArr, 0)
	return sumsArr

def branchSumsHelper(node, sumsArr, currentSum):
	newCurrent = currentSum + node.value
	if node.left is None and node.right is None:
		sumsArr.append(newCurrent)
	if node.left is not None:
		branchSumsHelper(node.left, sumsArr, newCurrent)
	if node.right is not None:
		branchSumsHelper(node.right, sumsArr, newCurrent)