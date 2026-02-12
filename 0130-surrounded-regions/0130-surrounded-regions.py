class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row , column = len(board), len(board[0])
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        def inBound(x,y):
            return x >= 0 and x < row and y >= 0 and y < column
        def dfs(i,j):
            for x, y in direction:
                new_x = x + i
                new_y = y + j
                if inBound(new_x,new_y) and board[new_x][new_y] == "O":
                    board[new_x][new_y] = "T"
                    dfs(new_x,new_y)
        for i in range(row):
            for j in range(column):
                if i == 0 or j == 0  or i == row - 1 or j == column -1:
                    if board[i][j] == 'O':
                        board[i][j] = "T"
                        dfs(i,j)
                
        for i in range(row):
            for j in range(column):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
        print(board)