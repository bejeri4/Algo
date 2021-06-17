# https://leetcode.com/problems/number-of-islands/

def getNeigs(node, grid):
    result = []
    i = node[0]
    j  = node[1]
    posNeigs = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    for posNeig in posNeigs:
        if posNeig[0] >= 0 and posNeig[0] < len(grid) and posNeig[1] >= 0 and posNeig[1] < len(grid[posNeig[0]]) and grid[posNeig[0]][posNeig[1]] == "1":
            result.append(posNeig)
    return result

def dfs(start, grid, visited):
	stack = []
	stack.append(start)
	visited.add(start)
	while stack:
		cur = stack.pop()
		for neig in getNeigs(cur, grid):
			if neig not in visited:
				visited.add(neig)
				stack.append(neig)
		


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    result += 1
                    dfs((i, j), grid, visited)
        return result
