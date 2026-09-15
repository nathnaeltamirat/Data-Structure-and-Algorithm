class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        def inBound(r,c):
            return r >= 0 and r < row and c >= 0 and c < col
        def inEdge(r,c):
            return r == 0 or r == row -1 or c == 0 or c == col - 1
        
        def dfs(i,j):
            board[i][j] = "N"
            for x,y in direction:
                new_x, new_y = i + x, y + j
                if inBound(new_x,new_y):
                    if board[new_x][new_y] == "O":
                        dfs(new_x,new_y)
        for i in range(row):
            for j in range(col):
                if inEdge(i,j) and board[i][j] == "O":
                    dfs(i,j)
        for i in range(row):
            for j in range(col):
                if board[i][j] == "N":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
       
