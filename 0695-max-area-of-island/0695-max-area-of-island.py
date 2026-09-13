class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        direction = [(-1,0),(1,0),(0,1),(0,-1)]
        row, col = len(grid), len(grid[0])
        def inBound(r,c):
            return r >= 0 and c >= 0 and r < row and c < col
        
        res = 0
        def dfs(i,j):
            res = 1
            for x, y in direction:
                new_x  = x + i
                new_y = y + j
                if inBound(new_x,new_y) and grid[new_x][new_y] == 1:
                    grid[new_x][new_y] = 0
                    res += dfs(new_x,new_y)
            
            return res
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    res = max(res,dfs(i,j))
        return res
                
