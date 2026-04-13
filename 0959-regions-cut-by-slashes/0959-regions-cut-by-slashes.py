class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        def inBound(r,c):
            return r >= 0 and c >= 0 and r < n*3 and c < n*3
        
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        new_grid = [[0 for _ in range(n*3)] for _ in range(n*3)]
        for i in range(n):
            for j in range(n):
                new_r = i * 3
                new_j = j *3
                if grid[i][j] == "/" or grid[i][j] == "\\":
                    if grid[i][j] == "/":
                        new_grid[new_r][new_j+2] = 1
                        new_grid[new_r+1][new_j+1] = 1
                        new_grid[new_r+2][new_j] = 1
                    else:
                        new_grid[new_r][new_j] = 1
                        new_grid[new_r+1][new_j+1] = 1
                        new_grid[new_r+2][new_j+2] = 1
        print(new_grid)
        res = 0
        def dfs(i,j):
            for x, y in direction:
                new_x, new_y = x + i, y + j
                if inBound(new_x,new_y):
                    if new_grid[new_x][new_y] == 0:
                        new_grid[new_x][new_y] = 1
                        dfs(new_x,new_y)
        for i in range(n*3):
            for j in range(n*3):
                if new_grid[i][j] == 0:
                    res += 1
                    dfs(i,j)
        return res