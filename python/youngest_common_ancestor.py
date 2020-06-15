
class AncestralTree:
	def __init__(self, name):
		self.name = name
		self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
	depthOne = getDepth(descendantOne, topAncestor)
	depthTwo = getDepth(descendantTwo, topAncestor)
	if depthOne > depthTwo:
		return findCommon(descendantOne, descendantTwo, depthOne - depthTwo)
	else:
		return findCommon(descendantTwo, descendantOne, depthTwo - depthOne)
	
def getDepth(descendant, topAncestor):
	depth = 0
	while descendant != topAncestor:
		depth += 1
		descendant = descendant.ancestor
	return depth

def findCommon(lowerDes, higherDes, diff):
	while diff > 0:
		lowerDes = lowerDes.ancestor
		diff -= 1
	while lowerDes != higherDes:
		lowerDes = lowerDes.ancestor
		higherDes = higherDes.ancestor
	return lowerDes