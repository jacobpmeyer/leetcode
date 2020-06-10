
class Node:
	def __init__(self, name):
		self.children = []
		self.name = name

	def addChild(self, name):
		self.children.append(Node(name))
		return self

	def breadthFirstSearch(self, array):
		names = []
		queue = [self]
		while len(queue) > 0:
			currentNode = queue.pop(0)
			names.append(currentNode.name)
			queue.extend(currentNode.children)
		return names

