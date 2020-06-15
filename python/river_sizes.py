
# O(nm) Time where n is the height of the matrix and m is the width of the matrix
# O(nm) Space
def riverSizes(matrix):
	visited = [[False for el in row] for row in matrix]
	sizes = []
	for r in range(len(matrix)):
		for c in range(len(matrix[0])):
			if visited[r][c]:
				continue
			explore(r, c, visited, sizes, matrix)
	return sizes

def explore(r, c, visited, sizes, matrix):
	riverSize = 0
	nodesToExplore = [[r, c]]
	while len(nodesToExplore):
		r, c = nodesToExplore.pop()
		if visited[r][c]:
			continue
		visited[r][c] = True
		if matrix[r][c] == 0:
			continue
		riverSize += 1
		unexploredNodes = getUnexploredNodes(r, c, matrix, visited)
		for node in unexploredNodes:
			nodesToExplore.append(node)
	if riverSize > 0:
		sizes.append(riverSize)

def getUnexploredNodes(r, c, matrix, visited):
	unexploredNodes = []
	if r > 0 and not visited[r - 1][c]:
		unexploredNodes.append([r - 1, c])
	if r < len(matrix) - 1 and not visited[r + 1][c]:
		unexploredNodes.append([r + 1, c])
	if c > 0 and not visited[r][c - 1]:
		unexploredNodes.append([r, c - 1])
	if c < len(matrix[0]) - 1 and not visited[r][c + 1]:
		unexploredNodes.append([r, c + 1])
	return unexploredNodes