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
            return r == 0 or r == row - 1 or c == 0 or c == col -1

        #doing dfs from the edge to know which board is not enclosed by X
        def dfs(i,j):
            for x, y in direction:
                new_x = i + x
                new_y = j + y
                if inBound(new_x,new_y):
                    if board[new_x][new_y] == "O":
                    
                        board[new_x][new_y] = "M"
                        dfs(new_x,new_y)
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O" and inEdge(i,j) :
                    board[i][j] = "M"
                    dfs(i,j)
        #Mapping back
        for i in range(row):
            for j in range(col):
                if board[i][j] == "M":
                    board[i][j] = "O"
                elif board[i][j] == 'O':
                    board[i][j] = "X"
        