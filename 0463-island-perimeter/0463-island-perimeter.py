class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #dfs on each item
        row, column = len(grid),len(grid[0])
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        res = 0
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    res += 4
                    if i > 0 and grid[i-1][j] == 1:
                        res -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        res -= 2

        return res
