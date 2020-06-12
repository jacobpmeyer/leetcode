def nodeDepths(root, depth = 0):
	if root is None:
		return 0
	left = nodeDepths(root.left, depth + 1)
	right = nodeDepths(root.right, depth + 1)
	return depth + left + right

class BinaryTree:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None