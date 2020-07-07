# You are given a map in form of a two-dimensional integer grid where 1 
# represents land and 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is 
# completely surrounded by water, and there is exactly one island (i.e., one or 
# more connected land cells).

# The island doesn't have "lakes" (water inside that isn't connected to the 
# water around the island). One cell is a square with side length 1. The grid is 
# rectangular, width and height don't exceed 100. Determine the perimeter of the 
# island.

# Example:

# Input:
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]

# Output: 16

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        landToExplore = []
        explored = {}
        edges = 0
        x = 0
        while not len(landToExplore):
            for j in range(len(grid[x])):
                if grid[x][j] == 1:
                    landToExplore.append([x, j])
                    break
            x += 1
        while len(landToExplore):
            i, j = landToExplore.pop()
            if (i, j) in explored:
                break
            else:
                explored[(i, j)] = True
            if i - 1 < 0 or grid[i - 1][j] == 0:
                edges += 1
            else:
                landToExplore.append((i - 1, j))
            if i + 1 >= len(grid) or grid[i + 1][j] == 0:
                edges += 1
            else:
                landToExplore.append((i + 1, j))
            if j - 1 < 0 or grid[i][j - 1] == 0:
                edges += 1
            else:
                landToExplore.append((i, j - 1))
            if j + 1 > len(grid[i]) or grid[i][j + 1] == 0:
                edges += 1
            else:
                landToExplore.append((i, j + 1))
        return edges