# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        return self.levelHelper(root, [], 0)

    def levelHelper(self, node, arr, lvl):
        if node is None:
            return arr
        while len(arr) < lvl + 1:
            arr.append([])
        arr[lvl].append(node.val)
        self.levelHelper(node.left, arr, lvl + 1)
        self.levelHelper(node.right, arr, lvl + 1)
        return arr
