
# Average: O(log(n)) Time where in is the size of the tree | O(1) Space
# Worst: O(n) Time if we had an unbalanced BST and we had to traverse the entire
# tree | O(1) Space
def findClosestValueInBst(tree, target):
	node = tree
	closestVal = node.value
	while node is not None:
		potentialDif = abs(node.value - target)
		closestDif = abs(closestVal - target)
		if potentialDif < closestDif:
			closestVal = node.value
		if node.value == target:
			break
		elif target < node.value:
			node = node.left
		elif target > node.value:
			node = node.right
	return closestVal