# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return isValid(tree, float("-inf"), float("inf"))

def isValid(tree, minVal, maxVal):
    if tree is None:
        return True
    if tree.value < minVal or tree.value >= maxVal:
        return False
    left = isValid(tree.left, minVal, tree.value)
    right = isValid(tree.right, tree.value, maxVal)
    return left and right
