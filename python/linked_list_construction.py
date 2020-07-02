# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
			self.head = node
		else:
			self.head.prev = node
			node.next = self.head
			self.head = node

    def setTail(self, node):
        if self.tail is None:
			self.tail = node
			self.tail.prev = self.head
			if self.head is not None:
				self.head.next = node
		else:
			self.tail.next = node
			node.prev = self.tail
			self.tail = node

    def insertBefore(self, node, nodeToInsert):
        if node == self.head:
			self.setHead(nodeToInsert)
		elif node == self.tail:
			self.setTail(nodeToInsert)
		else:
			node.prev.next = nodeToInsert
			nodeToInsert.next = node
			nodeToInsert.prev = node.prev
			node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if node == self.head:
			self.setHead(nodeToInsert)
		elif node == self.tail:
			self.setTail(nodeToInsert)
		else:
			node.next.prev = nodeToInsert
			nodeToInsert.next = node.next
			nodeToInsert.prev = node
			node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        currentPos = 1
		currentNode = self.head
		while currentPos < position and currentNode is not None:
			currentNode = currentNode.next
		nodeToInsert.prev = currentNode.prev
		nodeToInsert.next = currentNode
		if currentNode.prev:
			currentNode.prev.next = nodeToInsert
			currentNode.prev = nodeToInsert

    def removeNodesWithValue(self, value):
        currentNode = self.head
		removedNodes = []
		while currentNode is not None:
			if value == currentNode.value:
				if currentNode.prev:
					currentNode.prev.next = currentNode.next
				if currentNode.next:
					currentNode.next.prev = currentNode.prev
				removedNodes.append(currentNode)
			currentNode = currentNode.next


    def remove(self, node):
        currentNode = self.head
		while currentNode is not None:
			if node == currentNode:
				if node.prev:
					node.prev.next = node.next
				if node.next:
					node.next.prev = node.prev
				return node
			else:
				currentNode = currentNode.next

    def containsNodeWithValue(self, value):
        currentNode = self.head
		while currentNode is not None:
			if currentNode.value == value:
				return true
			else:
				currentNode = currentNode.next
