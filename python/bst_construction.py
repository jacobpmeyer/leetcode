# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value >= self.value:
					if not self.right:
						self.right = BST(value)
					else:
						self.right.insert(value)
				else: 
					if not self.left:
						self.left = BST(value)
					else:
						self.left.insert(value)
        return self

    def contains(self, value):
        if self.value == value:
					return true
				elif self.left and value < self.value:
					return self.left.contains(value)
				elif self.right and value >= self.value:
					return self.right.contains(value)
				else: 
					return False

    def remove(self, value):
        if self.left:
					if self.left
        return self