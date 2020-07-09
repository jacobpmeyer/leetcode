# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        maxWidth = 0
        # queue of elements [(node, colIndex)]
        queue = deque()
        queue.append((root, 0))

        while queue:
            levelLength = len(queue)
            _, levelHeadIndex = queue[0]
            # iterate through the current level
            for _ in range(levelLength):
                node, colIndex = queue.popleft()
                # preparing for the next level
                if node.left:
                    queue.append((node.left, 2 * colIndex))
                if node.right:
                    queue.append((node.right, 2 * colIndex + 1))

            # calculate the length of the current level,
            #   by comparing the first and last colIndex.
            maxWidth = max(maxWidth, colIndex - levelHeadIndex + 1)

        return maxWidth

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:

        # table contains the first colIndex for each level
        firstColIndexTable = {}
        maxWidth = 0

        def DFS(node, depth, colIndex):
            nonlocal maxWidth
            if node is None:
                return
            # if the entry is empty, set the value
            if depth not in firstColIndexTable:
                firstColIndexTable[depth] = colIndex

            maxWidth = max(maxWidth, colIndex - firstColIndexTable[depth] + 1)

            # Preorder DFS, with the priority on the left child
            DFS(node.left, depth+1, 2*colIndex)
            DFS(node.right, depth+1, 2*colIndex + 1)

        DFS(root, 0, 0)

        return maxWidth