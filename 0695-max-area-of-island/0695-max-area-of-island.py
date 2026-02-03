class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        row, column = len(grid), len(grid[0])
        def inBound(r,c):
            return r >= 0 and r < row and c >= 0 and c < column
        
        visited = set()
        def dfs(i,j):
            val = 1
            visited.add((i,j))
            for x, y in direction:
                new_r = i + x
                new_c = j + y
                if inBound(new_r,new_c) and grid[new_r][new_c] == 1:
                    if (new_r,new_c) not in visited:
                        val += dfs(new_r,new_c)
            return val
        res = 0
        for i in range(row):
            for j in range(column):
                if (i,j) not in visited and grid[i][j] == 1:
                    res = max(res,dfs(i,j))
        return res