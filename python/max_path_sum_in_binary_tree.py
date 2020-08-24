# My version
def maxPathSum(tree):
   currentMax = [float("-inf")]
   getMaxPath(tree, currentMax)
   return currentMax[0]

def getMaxPath(node, currentMax):
    if node is None:
        return 0
    
    leftMax = getMaxPath(node.left, currentMax)
    rightMax = getMaxPath(node.right, currentMax)

    totalSubTree = leftMax + rightMax + node.value
    leftPlusNode = leftMax + node.value
    rightPlusNode = rightMax + node.value
    currentMax[0] = max(currentMax[0], totalSubTree, leftPlusNode, rightPlusNode)

    if leftMax > rightMax:
        return leftMax + node.value
    else:
        return rightMax + node.value
    