# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
from collections import deque
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        node = self
        queue = deque()
        queue.append(node)
        while len(queue):
            currentNode = queue.popleft()
            for child in currentNode.children:
                queue.append(child)
            array.append(currentNode.name)
        return array
