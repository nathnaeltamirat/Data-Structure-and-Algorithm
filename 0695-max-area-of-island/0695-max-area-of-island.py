class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        row,column = len(grid), len(grid[0])
        def inBound(r,c):
            return r >= 0 and c >= 0 and r < row and c < column
        direction = [(-1,0),(0,-1),(1,0),(0,1)]
        def dfs(i,j):
            val = 1
            for x, y in direction:
                new_r = x + i
                new_c = y + j
                if inBound(new_r,new_c) and grid[new_r][new_c] == 1:
                    grid[new_r][new_c] = 0
                    val +=   dfs(new_r,new_c)
            return val
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    curr_max = dfs(i,j)
                    res= max(res,curr_max) 
        return res