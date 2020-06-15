

def riverSizes(matrix):
	visited = [[False for x in range(len(matrix[0]))] for y in range(len(matrix))]
    sizes = []
	for r in range(len(matrix)):
		for c in range(len(matrix[r])):
			if visited[r][c]:
				continue
			explore(r, c, visited, sizes, matrix)
	return sizes

def explore(r, c, visited, sizes, matrix):
	riverSize = 0
	nodesToExplore = [[r, c]]
	while len(nodesToExplore):
		# check to see if this works by calling .pop(0)
		r, c = nodesToExplore.pop()
		if visited[r][c]:
			continue
		if matrix[r][c] == 0:
			continue
		unexploredNodes = 