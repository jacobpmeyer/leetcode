def minHeightBst(array):
    return minHeightBstHelper(array, 0, len(array) - 1)

def minHeightBstHelper(array, leftIdx, rightIdx):
    if leftIdx > rightIdx:
        return
    midIdx = (leftIdx + rightIdx) // 2
    bst = BST(array[midIdx])
    bst.left = minHeightBstHelper(array, leftIdx, midIdx - 1)
    bst.right = minHeightBstHelper(array, midIdx + 1, rightIdx)
    return bst

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
