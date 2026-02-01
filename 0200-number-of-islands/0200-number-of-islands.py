class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, column = len(grid), len(grid[0])
        def inBound(r,c):
            return r >= 0 and c >= 0 and r < row and c < column
        visited = set()
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        res = 0
        def dfs(r,c):
            grid[r][c] = "0"
            for x, y in direction:
                new_r = x + r
                new_c = y + c
                if inBound(new_r,new_c) and grid[new_r][new_c] == "1":
                    grid[new_r][new_c] = "0"
                    dfs(new_r,new_c)

        for i in range(row):
            for j in range(column):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i,j)
        return res

