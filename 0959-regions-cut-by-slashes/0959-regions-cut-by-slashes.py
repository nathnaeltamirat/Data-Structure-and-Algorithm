

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        #scaling upt to 3x3
        row1, col1 = len(grid),len(grid[0])
        row2, col2 = row1 * 3, col1*3
        matrix = [["0"] * col2 for _ in range(row2)]
        for i in range(row1):
            for j in range(col1):
                new_r,new_col = i * 3, j * 3
                if grid[i][j] == "/":
                    matrix[new_r][new_col+2] = "1"
                    matrix[new_r+1][new_col+1] = "1"
                    matrix[new_r+2][new_col] = "1"
                elif grid[i][j] == "\\":
                    matrix[new_r][new_col] = "1"
                    matrix[new_r+1][new_col+1] = "1"
                    matrix[new_r+2][new_col+2] = "1"
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        def inBound(x,y):
            return x >= 0 and x < row2 and y >= 0 and y < col2

        def dfs(r,c):
            matrix[r][c] = "1"
            for x,y in direction:
                new_x = x + r
                new_y = y + c
                if inBound(new_x,new_y) and matrix[new_x][new_y] != "1":
                    dfs(new_x,new_y)
        
        res = 0
        print(matrix)
        for i in range(row2):
            for j in range(col2):
                if matrix[i][j] == "0":
                    dfs(i,j)
                    res += 1
        
        print(res)
        return res