# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return self.depthHelper(root, 1)
        
    def depthHelper(self, node: TreeNode, level: int) -> int:
        if node is None:
            return level - 1
        left = self.depthHelper(node.left, level + 1)
        right = self.depthHelper(node.right, level + 1)
        return max(left, right)