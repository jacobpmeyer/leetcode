
# O(n) Time | O(d) Space where d is the depth of the tree

class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

def validateBst(tree):
	return validateBstHelper(tree, float("-inf"), float("inf"))

def validateBstHelper(tree, minVal, maxVal):
	if tree is None:
		return True
	if tree.value < minVal or tree.value >= maxVal:
		return False
	leftTree = validateBstHelper(tree.left, minVal, tree.value)
	return leftTree and validateBstHelper(tree.right, tree.value, maxVal)
