
# O(n) Time | O(log(n)) Space

def minHeightBst(array):
	mid = int(len(array) / 2)
	root = BST(array[mid])
	if len(array) > 1:
		root.left = minHeightBst(array[:mid])
	if len(array) > 2:
		root.right = minHeightBst(array[mid + 1:])
	return root

class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def insert(self, value):
		if value < self.value:
			if self.left is None:
				self.left = BST(value)
			else:
				self.left.insert(value)
		else:
			if self.right is None:
				self.right = BST(value)
			else:
				self.right.insert(value)