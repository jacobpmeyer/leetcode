# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        left = self.bstHelper(root.left, float("-inf"), root.val)
        right = self.bstHelper(root.right, root.val, float("inf"))
        return left and right

    def bstHelper(self, node: TreeNode, minVal: int, maxVal: int) -> bool:
        if node is None:
            return True
        if node.val <= minVal or node.val >= maxVal:
            return False
        left = self.bstHelper(node.left, minVal, node.val)
        right = self.bstHelper(node.right, node.val, maxVal)
        return left and right