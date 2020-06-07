def invertBinaryTree(tree):
  if tree is None:
		return tree
	temp = invertBinaryTree(tree.left)
	tree.left = invertBinaryTree(tree.right)
  tree.right = temp
	return tree