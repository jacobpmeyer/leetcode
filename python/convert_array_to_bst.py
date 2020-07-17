# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(l, r):
            if left > right:
                return None
            p = (left + right) // 2
            if (left + right) % 2:
                p += randint(0, 1)
            root = TreeNode(nums[p])
            root.left = helper(l, p - 1)
            root.right = helper(p + 1, r)
            return root
        helper(0, len(nums) - 1)