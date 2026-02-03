class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        row , column = len(board),len(board[0])
        def inBound(r,c):
            return r >= 0 and r < row and c >= 0  and c < column
        def inBorder(r,c):
            return r == 0 or c == 0  or r == row-1 or c == column-1
        
        def dfs(r,c):
            board[r][c] = "T"
            for x, y in direction:
                new_r = x + r
                new_c = y + c
                if inBound(new_r,new_c) and board[new_r][new_c] == "O":
                    dfs(new_r,new_c)
        for i in range(row):
            for j in range(column):
                if inBorder(i,j) and board[i][j] == "O":

                    dfs(i,j)
        print(board)
        for i in range(row):
            for j in range(column):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
