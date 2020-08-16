# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getAncestorDepth(descendantOne, topAncestor)
    depthTwo = getAncestorDepth(descendantTwo, topAncestor)
    if depthOne > depthTwo:
        return backtrackTree(descendantOne, descendantTwo, depthOne - depthTwo)
    else:
        return backtrackTree(descendantTwo, descendantOne, depthTwo - depthOne)

def getAncestorDepth(descendant, topAncestor):
    depth = 0
    node = descendant
    while node != topAncestor:
        depth += 1
        node = node.ancestor
    return depth

def backtrackTree(larger, smaller, diff):
    while diff > 0:
        larger = larger.ancestor
        diff -= 1
    while larger != smaller:
        larger = larger.ancestor
        smaller = smaller.ancestor
    return larger