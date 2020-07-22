# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        level = 0
        q = [root]
        res = []
        while len(q):
            tempQ = deque()
            for i in range(len(q)):
                node = q.pop()
                if node is None:
                    continue
                while len(res) < level + 1:
                    res.append(deque())
                if level % 2 == 1:
                    res[level].append(node.val)
                else:
                    res[level].appendleft(node.val)
                tempQ.appendleft(node.right)
                tempQ.appendleft(node.left)
            level += 1
            q = tempQ
        return res

# [3,9,20,null,null,15,7]
# [1,2,3,4,null,null,5]
# [3,9,20,23,32,15,7]