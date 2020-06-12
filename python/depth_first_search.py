class Node:
	def __init__(self, name):
		self.children = []
		self.name = name

	def addChild(self, name):
		self.children.append(Node(name))
		return self


	# O(v + e) where v is every vertex in the tree, which we have to traverse
	# and e is each edge, which is an element in the node's children array
	def depthFirstSearch(self, array):
		if self is None:
			return []
		array.append(self.name)
		for child in self.children:
			child.depthFirstSearch(array)
		return array