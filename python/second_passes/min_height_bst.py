def minHeightBst(array):
    return bstHelper(array, 0, len(array) - 1)
    
def bstHelper(array, startIdx, endIdx):
    if startIdx > endIdx:
        return
    mid = (startIdx + endIdx) // 2
    root = BST(array[mid])
    root.left = bstHelper(array, startIdx, mid - 1)
    root.right = bstHelper(array, mid + 1, endIdx)
    return root


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
