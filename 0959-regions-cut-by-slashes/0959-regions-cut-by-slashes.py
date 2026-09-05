class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        new_grid = [[0 for _ in range(n*3)] for _ in range(n*3)]
        def inBound(r,c):
            return r >= 0 and c >= 0 and r < n * 3 and c < n * 3
         
        #building the new grid
        for i in range(n):
            for j in range(n):
                new_i = i * 3
                new_j = j * 3
                if grid[i][j] == "\\":
                    new_grid[new_i][new_j] = 1
                    new_grid[new_i+1][new_j+1] = 1
                    new_grid[new_i+2][new_j+2] = 1
                elif grid[i][j] == "/":
                    new_grid[new_i][new_j+2] = 1
                    new_grid[new_i+1][new_j+1] = 1
                    new_grid[new_i+2][new_j] = 1
      
        #direction
        direction = [(1,0),(-1,0),(0,1),(0,-1)]

        #dfs algorithm
        def dfs(i,j):
            
            for x, y in direction:
                new_x = i + x
                new_y = j + y
                if inBound(new_x,new_y) and new_grid[new_x][new_y] == 0:
                    new_grid[new_x][new_y] = 1
                    dfs(new_x,new_y)
                    
        
        res = 0
        for i in range(n*3):
            for j in range(n*3):
                if new_grid[i][j] == 0:
                    res += 1
                    dfs(i,j)
        return res

