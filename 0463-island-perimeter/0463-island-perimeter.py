class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #dfs on each item
        row, column = len(grid),len(grid[0])
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        def inBound(r,c):
            return r >= 0 and r < row and c >= 0 and c < column

        def dfs(i,j):
            count = 0
            for x, y in direction:
                new_r = i + x
                new_c = j + y
                if inBound(new_r,new_c):
                    if grid[new_r][new_c] == 1:
                        count += 1
            return 4 - count
        res = 0
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    res += dfs(i,j)
        return res
