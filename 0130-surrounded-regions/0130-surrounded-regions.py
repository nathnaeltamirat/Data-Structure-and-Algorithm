class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        row, col = len(board), len(board[0])
        def inBound(r,c):
            return r >= 0 and c >= 0 and r < row and c < col
        
        direction = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(i,j):
            for x, y in direction:
                new_x = x + i
                new_y = y + j
                if inBound(new_x,new_y) and board[new_x][new_y] == "O":
                    board[new_x][new_y] = "T"
                    dfs(new_x,new_y)
                
                
        for i in range(row):
            for j in range(col):
                if i == 0 or j == 0 or  i == row - 1 or j == col -1:
                    if board[i][j] == "O":
                        board[i][j] = "T"
                        dfs(i,j)
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
        print(board)
        