
# O(n) Time | O(n) Space where n is the size of the return array

# In the situation where we weren't storing the array, but only traversing the
# array in the orders, it would be O(d) space, where d is the depth of the tree.

def inOrderTraverse(tree, array):
	if tree is not None:
		inOrderTraverse(tree.left, array)
		array.append(tree.value)
		inOrderTraverse(tree.right, array)
	return array


def preOrderTraverse(tree, array):
	if tree is not None:
		array.append(tree.value)
		preOrderTraverse(tree.left, array)
		preOrderTraverse(tree.right, array)
	return array


def postOrderTraverse(tree, array):
	if tree is not None:
		postOrderTraverse(tree.left, array)
		postOrderTraverse(tree.right, array)
		array.append(tree.value)
	return array