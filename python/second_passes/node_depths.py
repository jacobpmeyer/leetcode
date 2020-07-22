def nodeDepths(root):
    return sumHelper(root, 0)

def sumHelper(node, depth):
    if node is None:
        return 0
    leftSum = sumHelper(node.left, depth + 1)
    rightSum = sumHelper(node.right, depth + 1)
    return leftSum + rightSum + depth

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
