class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row, col = len(board), len(board[0])
        def inBound(r,c):
            return r>= 0 and r < row and c >= 0 and c < col
        direction = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        def dfs(i,j):
            if board[i][j] == "M":
                board[i][j] = "X"
                return
            board[i][j] = "B"
            for x, y in direction:
                new_x = x + i
                new_y = y + j
                if inBound(new_x,new_y):
                    if board[new_x][new_y] == "M":
                        board[i][j]  = 1 if board[i][j] == "B" else board[i][j] + 1
            if board[i][j] == "B":
                for x,y in direction:
                    new_x = x + i
                    new_y = y + j
                    if inBound(new_x,new_y):
                        if board[new_x][new_y] == "E":
                            dfs(new_x,new_y)
        dfs(click[0],click[1])
        for i in range(row):
            for j in range(col):
                board[i][j] = str(board[i][j])
                    
        
        # print(board)
        return board